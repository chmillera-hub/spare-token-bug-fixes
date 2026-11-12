# A Python "nothing was passed" marker that type checkers accept

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python version 3.13.18 and no other person has rerun the tests yet which means the results on this page are unconfirmed.

## The question

On 14 June 2026 somebody asked on the Python help forum (discuss.python.org topic number 107758) whether a one-line trick is a good method for making a sentinel in Python versions 3.12 to 3.14.
A sentinel is a special marker object that a function uses as a default value so the function can tell "the caller passed nothing" apart from "the caller passed None".
The trick in the post was the line "type _MISSING = _MISSING" which defines a type name in terms of itself.
The post said the trick works when the program runs and that the type checker rejects the trick.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- The trick runs without an error on Python 3.13.18 and the function prints the expected text.
- The type checker named mypy rejects the first line with the message "Cannot resolve name _MISSING (possible cyclic definition)".
- The type checker named pyright rejects the first line with the message "Type alias _MISSING cannot use itself in its definition".
- A marker built from an enum class with exactly one member passes both type checkers with zero errors. After the check "if value is MISSING" both type checkers narrow the remaining type to plain text (str) which means string methods can be called without a complaint.

## Best-guess answer

The self-referencing trick is a poor fit for typed code because two widely used type checkers reject the trick at the first line.
The enum marker is a working substitute for Python 3.12 to 3.14 because the enum marker runs correctly and passes both type checkers.
The enum marker looks like the following six lines:

import enum
from typing import Final
class _Missing(enum.Enum):
    MISSING = enum.auto()
MISSING: Final = _Missing.MISSING
def my_func(need_value: int, not_need_value: str | _Missing = MISSING) -> None: ...

The test files named sentinel_rejected.py and sentinel_enum.py sit in boring-things inside research-program-files inside unanswered-questions-scripts.
