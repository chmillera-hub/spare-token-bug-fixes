# Why "Move to square b0" printed before the row error in a try block exercise

## Link to the original question

https://discuss.python.org/t/98946

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) rebuilt the exercise in a single chat on 12 November 2026 from the text of the post (the screenshot in the post was not readable) and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 16 July 2025 somebody asked on the Python help forum about a code-ordering exercise from an online textbook.
The exercise has a function get_column that raises a ValueError for a column outside a to h and a function get_row that raises a ValueError for a row outside 1 to 8 and a try block that gets both values and prints the move.
For the input "b 0" the submitted program printed "Move to square b0" and then "Row must be between 1 and 8" while the expected output was only the error line.
The asker wondered whether the textbook site was wrong.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

- An ordering with the print line before the row check printed both lines for the input b 0 which matches the output the asker reported.
- An ordering with both value lines first and the print line last printed only "Row must be between 1 and 8" for the input b 0 which matches the expected output.
- Both orderings printed "Move to square b3" for the input b 3 and the column error for the input k 3.

## Best-guess answer

The expected output of the site is correct because a raised error stops the try block at the line where the error happens and jumps to the except block so every line that ran before the error has already had its effect.
The print line therefore has to come after both value lines:

try:
    column = get_column()
    row = get_row()
    print(f"Move to square {column}{row}")
except ValueError as excpt:
    print(excpt)

The check file named chess_move.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
