# the approach from the forum post (output copied with shutil.copyfileobj into sys.stdout.buffer)
import shutil, subprocess, sys
from threading import Thread
proc = subprocess.Popen([sys.executable, "child_echo.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0)
Thread(target=shutil.copyfileobj, args=(sys.stdin.buffer, proc.stdin), daemon=True).start()
Thread(target=shutil.copyfileobj, args=(proc.stdout, sys.stdout.buffer), daemon=True).start()
proc.wait()
