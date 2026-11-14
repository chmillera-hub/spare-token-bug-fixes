# Rebuilds the "dollar format is not applied" problem with pandas and xlsxwriter and tests the repair (Python forum topic 79453)
import pandas, xlsxwriter, openpyxl
print("pandas", pandas.__version__, "| xlsxwriter", xlsxwriter.__version__)
headers = ["Sales rep", "Proforma date", "Job id", "Proforma amt", "Cost", "Reason"]
rows = [["Jim Sales", "12/1/24", "12345", str(130.8), str(99.88), "no reason"],
        ["Joan Sales", "12/2/24", "12346", str(1200.39), str(500.31), "no reason"],
        ["Jane Smith", "12/3/24", "12350", str(788), str(650.01), "Reason A"]]

def write(fn, df, money_cols):
    with pandas.ExcelWriter(fn, engine="xlsxwriter", date_format="MM/DD/YYYY") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False, freeze_panes=(1, 0))
        book, sheet = writer.book, writer.sheets["Sheet1"]
        dlr = book.add_format({"num_format": "$0.00", "align": "right"})
        sheet.set_column("B:B", 10, book.add_format({"num_format": "mm/dd/yy"}))
        sheet.set_column(money_cols, 12, dlr)

def report(label, fn):
    ws = openpyxl.load_workbook(fn)["Sheet1"]
    for col in "DE":
        c = ws[f"{col}2"]
        print(f"{label} | cell {col}2: value {c.value!r} | stored as {'number' if c.data_type == 'n' else 'text'} | number format {c.number_format!r}")
    print(f"{label} | date cell B2: value {ws['B2'].value!r} | stored as {'date' if ws['B2'].is_date else 'text'}")

df = pandas.DataFrame(rows, columns=headers)                  # every value is text, as in the posted script
write("posted.xlsx", df, "E:F")                               # the posted column letters
report("posted ", "posted.xlsx")

fixed = df.copy()
for col in ("Proforma amt", "Cost"): fixed[col] = pandas.to_numeric(fixed[col])
fixed["Proforma date"] = pandas.to_datetime(fixed["Proforma date"], format="%m/%d/%y")
fixed["Job id"] = pandas.to_numeric(fixed["Job id"])
write("fixed.xlsx", fixed, "D:E")                             # Proforma amt is column D and Cost is column E
report("repaired", "fixed.xlsx")
