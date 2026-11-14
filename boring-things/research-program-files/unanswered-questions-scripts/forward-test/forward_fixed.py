# a repaired forwarder: small reads, a flush after every piece, the child's input closed at end of input, output drained before exit
import os, subprocess, sys
from threading import Thread
proc = subprocess.Popen([sys.executable, "child_echo.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0)

def pump_in():
    try:
        while chunk := os.read(sys.stdin.fileno(), 65536):   # returns as soon as any bytes are available
            proc.stdin.write(chunk)
    except (BrokenPipeError, OSError):
        pass
    finally:
        try: proc.stdin.close()                                # tells the child that no more input is coming
        except OSError: pass

def pump_out():
    while chunk := proc.stdout.read(65536):                    # unbuffered pipe: returns as soon as any bytes are available
        sys.stdout.buffer.write(chunk); sys.stdout.buffer.flush()

Thread(target=pump_in, daemon=True).start()                    # daemon: a read that is still waiting for input cannot keep the program alive
out = Thread(target=pump_out); out.start()
proc.wait()
out.join()                                                     # every byte the child wrote has been forwarded
sys.exit(proc.returncode)
