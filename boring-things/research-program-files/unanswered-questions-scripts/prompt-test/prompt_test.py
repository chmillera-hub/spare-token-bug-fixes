# Tests why an input() prompt of a child process stays invisible to a line-based reader (Python forum topic 87697)
import os, queue, subprocess, sys, threading, time
print("Python", sys.version.split()[0])

def run(reader_kind):
    p = subprocess.Popen([sys.executable, "-u", "child_prompt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=(reader_kind == "lines"), bufsize=1 if reader_kind == "lines" else 0)
    q = queue.Queue()
    def read_lines():
        for line in p.stdout: q.put(line)                       # waits for a line break before handing anything over
    def read_chunks():
        while chunk := os.read(p.stdout.fileno(), 4096):        # hands over whatever has arrived, line break or not
            q.put(chunk.decode())
    threading.Thread(target=read_lines if reader_kind == "lines" else read_chunks, daemon=True).start()
    time.sleep(1.0)
    before = []
    while not q.empty(): before.append(q.get())
    p.stdin.write("Ada\n" if reader_kind == "lines" else b"Ada\n"); p.stdin.flush()
    time.sleep(0.5)
    after = []
    while not q.empty(): after.append(q.get())
    p.wait()
    print(f"{reader_kind} reader | received before any input was sent: {before} | received after the input was sent: {after}")

run("lines"); run("chunks")
