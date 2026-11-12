# Tests two ways to turn the text "(missing)" red in one column of a pandas/xlsxwriter spreadsheet (Python forum topic 74598)
import pandas, openpyxl
headers = ["Sales rep", "Proforma date", "Job num", "Cust code", "Cost"]
rows = [["Jim", "12/1/24", 3, "ACME", 10.5], ["Joan", "12/2/24", 1, "(missing)", 20.0], ["Jane", "12/3/24", 2, "ZETA", 5.0], ["Jo", "12/4/24", 4, "(missing)", 7.0]]
df = pandas.DataFrame(rows, columns=headers).sort_values(["Job num"])
n = len(df)

# route 1: a conditional format over the data rows of column D (rows 2 to n+1, because row 1 is the header)
with pandas.ExcelWriter("red1.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    red = writer.book.add_format({"font_color": "red"})
    writer.sheets["Sheet1"].conditional_format(f"D2:D{n + 1}", {"type": "text", "criteria": "containing", "value": "(missing)", "format": red})
ws = openpyxl.load_workbook("red1.xlsx")["Sheet1"]
rules = [(str(rng.sqref), r.type, r.operator, r.text, r.dxf.font.color.rgb) for rng, rs in ws.conditional_formatting._cf_rules.items() for r in rs]
print("route 1 rule stored in the file (range, type, operator, text, font colour):", rules)
print("route 1 cells with (missing):", [c.coordinate for c in ws["D"] if c.value == "(missing)"], "| all inside the range D2:D%d:" % (n + 1), all(2 <= c.row <= n + 1 for c in ws["D"] if c.value == "(missing)"))

# route 2: write the matching cells again with a red format
with pandas.ExcelWriter("red2.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    red = writer.book.add_format({"font_color": "red"})
    col = df.columns.get_loc("Cust code")
    for r, value in enumerate(df["Cust code"], start=1):          # start=1 skips the header row
        if value == "(missing)": writer.sheets["Sheet1"].write(r, col, value, red)
ws = openpyxl.load_workbook("red2.xlsx")["Sheet1"]
print("route 2 font colours in column D:", [(c.coordinate, c.value, "red" if (c.font.color is not None and c.font.color.rgb == "FFFF0000") else "default colour") for c in ws["D"][1:]])
