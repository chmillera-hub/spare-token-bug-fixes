# Does mypy work out the type of an assignment from the right side like pyright does

## Link to the original question

https://discuss.python.org/t/105786

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 with mypy version 2.3.1 and a current pyright and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 18 January 2026 somebody asked on the Python help forum whether the type checker mypy handles an assignment the same way as the type checker pyright.
The pyright documentation says that the checker first works out the type of the right side of an assignment and that a declared type on the left side can influence how the right side is understood.
The asker could not find a matching statement in the mypy documentation.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

Both checkers gave the same verdict on every test line.

- The line a = [1, 2] has no declared type on the left and both checkers reported the type list[int] which comes from the right side.
- The line b: list[object] = [1, 2] was accepted by both checkers which means both checkers used the declared type on the left while reading the right side.
- The line c: list[object] = a was rejected by both checkers because the right side already had the fixed type list[int] before the assignment.
- The line d: list[float] = [] gave the type list[float] in both checkers because the empty list takes the element type from the left side.

One difference showed up on the line e = [] with nothing on the left to help: mypy asked for a type annotation and pyright reported no error.

## Best-guess answer

The tests point to yes because mypy behaved like the pyright description on every line: the type comes from the right side and a declared type on the left side shapes how the right side is read.
The answer rests on four test lines and not on a reading of the mypy source code so unusual cases could still differ.

The test file named inference_direction.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
