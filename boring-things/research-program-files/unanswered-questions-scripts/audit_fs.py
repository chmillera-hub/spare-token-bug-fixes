# Tests which file system calls raise audit events and whether one patch of os.stat sees the existence checks (Python forum topic 84064)
import sys, os, glob, pathlib, tempfile
print("Python", sys.version.split()[0], "on", sys.platform)
events = []
sys.addaudithook(lambda name, args: events.append(name))
d = tempfile.mkdtemp(); f = os.path.join(d, "a.txt"); open(f, "w").close()
def audited(label, fn):
    events.clear(); fn()
    names = sorted({e for e in events if e.split(".")[0] in ("open", "os", "glob", "pathlib", "shutil")})
    print(f"{label}: {names if names else 'no audit event'}")
audited("open(f)", lambda: open(f).close())
audited("glob.glob(pattern)", lambda: glob.glob(os.path.join(d, "*.txt")))
audited("os.listdir(d)", lambda: os.listdir(d))
audited("os.scandir(d)", lambda: list(os.scandir(d)))
audited("os.stat(f)", lambda: os.stat(f))
audited("os.path.exists(f)", lambda: os.path.exists(f))
audited("os.path.isfile(f)", lambda: os.path.isfile(f))
audited("os.path.isdir(d)", lambda: os.path.isdir(d))
audited("pathlib.Path(f).exists()", lambda: pathlib.Path(f).exists())
audited("pathlib.Path(f).is_file()", lambda: pathlib.Path(f).is_file())
audited("os.access(f, os.R_OK)", lambda: os.access(f, os.R_OK))

# one patch instead of many: on this platform the existence checks all go through os.stat
seen = []; real_stat = os.stat
def watching_stat(path, *a, **k):
    seen.append(os.fspath(path) if not isinstance(path, int) else path); return real_stat(path, *a, **k)
os.stat = watching_stat
try:
    for label, fn in (("os.path.exists", lambda: os.path.exists(f)), ("os.path.isfile", lambda: os.path.isfile(f)), ("os.path.isdir", lambda: os.path.isdir(d)),
                      ("Path.exists", lambda: pathlib.Path(f).exists()), ("Path.is_file", lambda: pathlib.Path(f).is_file()), ("os.access", lambda: os.access(f, os.R_OK))):
        seen.clear(); fn(); print(f"with os.stat patched: {label} was seen: {bool(seen)}")
finally:
    os.stat = real_stat
