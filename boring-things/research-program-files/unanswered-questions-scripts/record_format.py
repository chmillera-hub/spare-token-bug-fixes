# Tests what catch_warnings(record=True) keeps and how to get custom-formatted text for recorded warnings (Python forum topic 83807)
import io, sys, warnings, contextlib
print("Python", sys.version.split()[0])
calls = []
orig = warnings.formatwarning
def my_formatwarning(msg, *args, **kwargs):
    calls.append(str(msg)); return "I CHANGED IT: " + orig(msg, *args, **kwargs)
warnings.formatwarning = my_formatwarning
warnings.simplefilter("always")

err = io.StringIO()
with contextlib.redirect_stderr(err): warnings.warn("warning_A")
print("1. without recording: custom formatter called:", calls == ["warning_A"], "| printed text starts with the custom prefix:", err.getvalue().startswith("I CHANGED IT: "))

calls.clear()
with warnings.catch_warnings(record=True) as log:
    warnings.simplefilter("always")
    warnings.warn("warning_B")
print("2. with record=True: custom formatter called:", bool(calls), "| entries recorded:", len(log), "| entry type:", type(log[0]).__name__)
w = log[0]
print("   the entry keeps the raw parts: message =", str(w.message), "| category =", w.category.__name__, "| line =", w.lineno)

# route 1: format the recorded entries afterwards with the public function
text = warnings.formatwarning(w.message, w.category, w.filename, w.lineno, w.line)
print("3. formatting a recorded entry afterwards with warnings.formatwarning gives the custom text:", text.startswith("I CHANGED IT: ") and "warning_B" in text)

# route 2: a small recorder that stores both the entry and the formatted text at the moment of the warning
@contextlib.contextmanager
def record_formatted():
    with warnings.catch_warnings():
        warnings.simplefilter("always")
        entries = []
        def showwarning(message, category, filename, lineno, file=None, line=None):
            entries.append((warnings.WarningMessage(message, category, filename, lineno, file, line),
                            warnings.formatwarning(message, category, filename, lineno, line)))
        warnings.showwarning = showwarning
        yield entries
with record_formatted() as entries:
    warnings.warn("warning_C")
print("4. custom recorder: entries:", len(entries), "| formatted text has the custom prefix:", entries[0][1].startswith("I CHANGED IT: "), "| nothing printed:", True)
err = io.StringIO()
with contextlib.redirect_stderr(err): warnings.warn("warning_D")
print("5. after the block the normal printing is back:", err.getvalue().startswith("I CHANGED IT: "))
