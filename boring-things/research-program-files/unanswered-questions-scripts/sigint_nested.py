# Tests how long a program with a thread pool inside a process pool takes to stop after Ctrl-C, and one repair (Python forum topic 88003)
import os, signal, subprocess, sys, time
POSTED = '''
from time import sleep
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
def payload(): sleep(10)
def wrapper():
    with ThreadPoolExecutor(1) as pool: pool.submit(payload).result()
if __name__ == "__main__":
    with ProcessPoolExecutor(1) as pool: pool.submit(wrapper).result()
'''
FIXED = '''
import os, signal, sys
from time import sleep
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
def payload(): sleep(10)
def wrapper():
    with ThreadPoolExecutor(1) as pool: pool.submit(payload).result()
def ignore_sigint(): signal.signal(signal.SIGINT, signal.SIG_IGN)      # workers leave Ctrl-C to the parent
if __name__ == "__main__":
    pool = ProcessPoolExecutor(1, initializer=ignore_sigint)
    try:
        pool.submit(wrapper).result()
    except KeyboardInterrupt:
        for proc in list(pool._processes.values()): proc.kill()         # private attribute: stop the workers at once
        pool.shutdown(wait=False, cancel_futures=True)
        print("stopped on Ctrl-C", flush=True)
        sys.exit(130)
    pool.shutdown()
'''
print("Python", sys.version.split()[0])
for name, src in (("posted program", POSTED), ("repaired program", FIXED)):
    open("prog.py", "w").write(src)
    p = subprocess.Popen([sys.executable, "prog.py"], start_new_session=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(1.5)
    t = time.time(); os.killpg(p.pid, signal.SIGINT)                  # Ctrl-C reaches the whole group, like in a terminal
    try: p.wait(timeout=15); took = f"{time.time() - t:.1f} s"
    except subprocess.TimeoutExpired: took = "more than 15 s"; os.killpg(p.pid, signal.SIGKILL)
    left = subprocess.run(["pgrep", "-g", str(p.pid)], capture_output=True, text=True).stdout.split()
    print(f"{name}: exited {took} after Ctrl-C | exit code {p.returncode} | leftover worker processes: {len(left)}")
