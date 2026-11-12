# Why a dollar format on spreadsheet columns is ignored with pandas and xlsxwriter

## Link to the original question

https://discuss.python.org/t/79453

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with pandas 3.0.5 and xlsxwriter 3.2.9 and no other person has rerun the test yet which means the page is unconfirmed. The asker used older versions on Windows.

## The question

On 4 February 2025 somebody asked on the Python help forum why the dollar format set with set_column is not applied to the money columns of a spreadsheet written with pandas and xlsxwriter.
The posted script builds every row by joining values into one text line and splitting the line again and then calls set_column("E:F", 12, dlrformat).
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test rebuilt the data of the post and read the finished file back.

- With the posted approach cell D2 (Proforma amt) held the text "130.8" with the format General and cell E2 (Cost) held the text "99.88" with the dollar format attached. The date cell held the text "12/1/24".
- After converting the two money columns to numbers and the date column to dates and setting the format on columns D to E both money cells were stored as numbers with the format $0.00 and the date cell was stored as a real date.

## Two causes

1. Every value in the posted table is text because the rows are built from text lines. A number format changes how numbers are shown and does nothing to text so "99.88" stays as typed even with the dollar format attached.
2. The column letters are shifted by one. The header order is Sales rep (A) and Proforma date (B) and Job id (C) and Proforma amt (D) and Cost (E) and Reason (F) so "E:F" formats Cost and Reason and leaves Proforma amt out.

## Best-guess answer

The repair that worked in the test:

for col in ("Proforma amt", "Cost"):
    df[col] = pandas.to_numeric(df[col])
df["Proforma date"] = pandas.to_datetime(df["Proforma date"], format="%m/%d/%y")
...
worksheet.set_column("D:E", 12, dlrformat)

Keeping the numbers as numbers from the start (a list of lists in place of joined text lines) avoids the conversion step.

The test file named dollar_columns.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
