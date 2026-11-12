# Why a lambda inside a string annotation cannot find a global name after get_type_hints

## Link to the original question

https://discuss.python.org/t/103831

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the checks yet which means the page is unconfirmed.

## The question

On 19 September 2025 somebody asked on the Python help forum why calling a lambda recovered from a string annotation raises "NameError: name FIND_ME is not defined".
The class in the post has two annotations (a regular function and a lambda that returns the module-level value FIND_ME) and the file starts with "from __future__ import annotations" which stores every annotation as text.
Calling typing.get_type_hints(Example) with default settings gave a working function and a broken lambda while passing globalns and localns explicitly made the lambda work.
The post had zero replies when the forum list was read on 12 November 2026.

## What the checks show

- The error reproduced on Python 3.13.18.
- The broken lambda does not have the module dictionary as its global namespace. The global namespace of the broken lambda is a dictionary holding the contents of the class which has no entry named FIND_ME.
- The source code of get_type_hints contains the line "base_globals, base_locals = base_locals, base_globals". For a class with no namespaces passed in the function swaps the two namespaces before evaluating the annotation text so the class contents are used as globals and the module dictionary is used as locals.
- A lambda remembers only the globals of the place where the lambda was created and never the locals. The lambda is created during that evaluation so the lambda remembers the class contents and loses the module dictionary.
- The regular function is only looked up by name during the evaluation and the lookup succeeds through the locals. The regular function was created earlier in the module so the function still has the module dictionary as globals.
- Passing both namespaces explicitly gave 42 and passing only globalns also gave 42 because the swap happens only when neither namespace is passed.

## Best-guess answer

The default behaviour differs from the commented-out lines in the post by exactly the swap: the defaults are the same two dictionaries in the opposite roles.
The repair that worked in the test is passing globalns=sys.modules[Example.__module__].__dict__ to get_type_hints.

The check file named lambda_hints.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
