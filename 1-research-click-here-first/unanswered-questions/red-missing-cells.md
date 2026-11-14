# Turning the text "(missing)" red in one spreadsheet column with pandas and xlsxwriter

## Link to the original question

https://discuss.python.org/t/74598

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with pandas 3.0.5 and xlsxwriter 3.2.9 and no other person has rerun the test yet which means the page is unconfirmed. The file was read back with a second library and was not opened in Excel itself.

## The question

On 18 December 2024 somebody asked on the Python help forum how to make the text "(missing)" red in column D of a spreadsheet written with pandas and the xlsxwriter engine.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test table had four data rows with "(missing)" in two rows of column D.

- Route 1 (a conditional format): the finished file held one rule on the range D2:D5 of the kind "text contains (missing)" with a red font and both "(missing)" cells sat inside that range.
- Route 2 (writing the matching cells again with a red format): the two "(missing)" cells carried a red font and the other two cells kept the default colour.

## Best-guess answer

Route 1 is two lines after df.to_excel:

red = writer.book.add_format({"font_color": "red"})
writer.sheets[sheetname].conditional_format(f"D2:D{len(df) + 1}", {"type": "text", "criteria": "containing", "value": "(missing)", "format": red})

The range starts at D2 because row 1 is the header and ends at len(df) + 1 because the data starts one row down. A range that ends at len(df) leaves out the last data row.
Route 2 colours only the matching cells with a fixed format:

col = df.columns.get_loc("Cust code")
for r, value in enumerate(df["Cust code"], start=1):
    if value == "(missing)":
        writer.sheets[sheetname].write(r, col, value, red)

Route 1 keeps working when a person edits the cells later in Excel and route 2 does not react to later edits.

The test file named red_missing.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
