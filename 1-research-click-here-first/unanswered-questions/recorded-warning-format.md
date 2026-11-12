# Getting custom-formatted text for warnings recorded with catch_warnings

## Link to the original question

https://discuss.python.org/t/83807

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 9 March 2025 somebody asked on the Python help forum why a custom warnings.formatwarning function leaves no trace in the list returned by warnings.catch_warnings(record=True).
The asker maintains a testing tool that has to record warnings and also has to test code that formats warnings and asked for alternatives that avoid private parts of the Python library.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

1. Without recording the custom formatter was called and the printed text carried the custom prefix.
2. With record=True the custom formatter was not called at all. The recorded entry is a WarningMessage object that keeps the raw parts: the message and the category and the file name and the line number.
3. Calling the public function warnings.formatwarning on the raw parts of a recorded entry afterwards produced the custom-formatted text.
4. A small custom recorder that replaces warnings.showwarning inside a catch_warnings block stored both the entry and the custom-formatted text at the moment of the warning and printed nothing.
5. After the block ended normal printing with the custom formatter was back.

## Best-guess answer

Recording skips formatting because formatting only happens on the way to printing and recording stores the raw parts in place of printing.
Two routes that use only public functions worked in the tests:

- Format later: text = warnings.formatwarning(w.message, w.category, w.filename, w.lineno, w.line) for each recorded entry w.
- Format at the moment of the warning: inside "with warnings.catch_warnings():" set warnings.showwarning to a function that appends both a warnings.WarningMessage(...) and warnings.formatwarning(...) to a list.

The second route matters when the custom formatter depends on the state of the program at the moment of the warning.

The test file named record_format.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
