# a small child program: answers every input line in capital letters and stops when it reads "quit" or its input ends
import sys
for line in sys.stdin:
    if line.strip() == "quit": break
    sys.stdout.write(line.upper()); sys.stdout.flush()
