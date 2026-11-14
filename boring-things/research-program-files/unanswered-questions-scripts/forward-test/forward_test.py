# Drives both forwarders the way a terminal would and reports what arrives and when (Python forum topic 103413)
import subprocess, sys, time, select, os
print("Python", sys.version.split()[0])
def run(script):
    p = subprocess.Popen([sys.executable, script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0)
    p.stdin.write(b"hello\n")
    ready, _, _ = select.select([p.stdout], [], [], 3.0)
    first = os.read(p.stdout.fileno(), 100) if ready else None
    p.stdin.write(b"quit\n")                      # the child stops here while the forwarder's own input stays open
    t = time.time()
    try: p.wait(timeout=5); ended = f"exited {time.time() - t:.2f} s after the child stopped with code {p.returncode}"
    except subprocess.TimeoutExpired: ended = "still running 5 s after the child stopped"; p.kill()
    rest = p.stdout.read()
    print(f"{script}: answer to the first line within 3 s: {first!r} | {ended} | output that arrived only at the end: {rest!r}")
run("forward_posted.py"); run("forward_fixed.py")
