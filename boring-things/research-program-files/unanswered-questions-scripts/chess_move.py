# The ordering that produces the expected output for the "Move to square" exercise (Python forum topic 98946)
import io, contextlib
def get_column(text):
    if not ("a" <= text <= "h") or len(text) != 1: raise ValueError("Column must be between a and h")
    return text
def get_row(text):
    row = int(text)
    if not (1 <= row <= 8): raise ValueError("Row must be between 1 and 8")
    return row
def posted_order(col_text, row_text):
    try:
        column = get_column(col_text)
        print(f"Move to square {column}{row_text}")      # printing before the row has been checked
        row = get_row(row_text)
    except ValueError as excpt:
        print(excpt)
def fixed_order(col_text, row_text):
    try:
        column = get_column(col_text)
        row = get_row(row_text)
        print(f"Move to square {column}{row}")            # printing only after both checks passed
    except ValueError as excpt:
        print(excpt)
for f in (posted_order, fixed_order):
    for col, row in (("b", "0"), ("b", "3"), ("k", "3")):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): f(col, row)
        print(f"{f.__name__} with input {col} {row}: {buf.getvalue().strip().splitlines()}")
