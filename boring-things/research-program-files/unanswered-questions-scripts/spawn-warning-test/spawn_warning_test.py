# Tests three ways to silence a warning that a module raises on import inside a spawned child process (Python forum topic 105472)
import multiprocessing as mp, os, subprocess, sys

def run(module_name):
    mod = __import__(module_name)
    ctx = mp.get_context("spawn"); q = ctx.Queue()
    p = ctx.Process(target=mod.target, args=(q,)); p.start(); print("result", q.get()); p.join()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        import warnings; warnings.filterwarnings("ignore", category=UserWarning)   # silences the parent only
        if sys.argv[2] == "env": os.environ["PYTHONWARNINGS"] = "ignore::UserWarning"   # read by every child at startup
        run(sys.argv[1]); sys.exit()
    print("Python", sys.version.split()[0])
    for label, module, mode in (("import at the top of the file, nothing else", "child_top", "plain"),
                                ("route 1: PYTHONWARNINGS set in the parent before the child starts", "child_top", "env"),
                                ("route 2: filter set inside the target function before a late import", "child_lazy", "plain"),
                                ("route 3: a tiny filter module imported first", "child_quiet_first", "plain")):
        r = subprocess.run([sys.executable, __file__, module, mode], capture_output=True, text=True)
        print(f"{label} | {r.stdout.strip()} | warning printed by the child: {'UserWarning' in r.stderr}")
