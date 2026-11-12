# Why a home-made Python match pattern gives "Invalid CFG, inconsistent stackdepth"

One AI model (Claude) read the Python source code and ran a small check in a single chat on 12 November 2026 and no other person has checked the work yet. The suggested fix was not tested because testing needs a rebuilt copy of Python with the asker's changes which means the fix is an unconfirmed best guess.

## The question

On 13 October 2026 somebody on the Python help forum (discuss.python.org topic number 109464) described a learning project that adds a new kind of pattern to the match statement inside the Python compiler (Python 3.14).
The new pattern calls a function and treats a true result as a match.
One pattern alone worked and two patterns joined with the "or" bar gave the error "ValueError: Invalid CFG, inconsistent stackdepth".
The asker wanted to know whether a function call leaves exactly one value on top of the stack and where to look for the cause.
The post had zero replies when the forum list was read on 12 November 2026.

## What the source code and the check show

1. A function call leaves exactly one new value on the stack. The check measured the stack change of the call instruction for a call with 1 argument as −2 which means the call removes the function slot and one extra slot and the argument (3 values) and puts back 1 result.

2. The Python 3.14 source file Python/codegen.c carries a comment above the pattern routines (lines 5670 to 5672) that says every pattern routine follows the convention of consuming the top of the stack (the value being matched) and jumping to the failure code when the pattern does not match.

3. The built-in value pattern follows the convention because the comparison instruction removes both the value being matched and the constant and leaves one true or false result. The bytecode of "case 1 | 0" shows the steps for each alternative: copy the value being matched (+1) then load the constant (+1) then compare (−1) then jump on false (−1). The stack is back to the starting height after each alternative.

4. The asker's routine pushes the result of the call and turns the result into true or false and jumps on false. Nothing in the routine removes the copy of the value being matched so the routine ends one value higher than the convention promises.

## Best-guess answer

One possibility for the cause is the missing removal of the value being matched because the "or" code makes a copy for every alternative and expects each alternative to use the copy up. Paths that should meet at the same stack height then meet at different heights and the compiler reports the inconsistent stack depth.

A fix worth testing is one extra line before the call that removes the copy when the function does not need the value:

ADDOP(c, LOC(p), POP_TOP);
VISIT(c, expr, p->v.MatchFunc.e);
ADDOP(c, LOC(p), TO_BOOL);
RETURN_IF_ERROR(jump_to_fail_pop(c, LOC(p), pc, POP_JUMP_IF_FALSE));

A pattern that should pass the matched value into the function can keep the copy and hand the copy to the call as an argument so the call uses the copy up.

One guess about why the constant version worked for the asker is that the compiler removes a jump whose condition is a known constant so the mismatched paths never meet. The guess was not tested.

The check file named match_stack.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
