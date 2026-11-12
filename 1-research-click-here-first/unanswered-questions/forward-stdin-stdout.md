# Forwarding input and output between a Python program and a child process without hanging

## Link to the original question

https://discuss.python.org/t/103413

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 on Linux with input and output connected through pipes and no other person has rerun the tests yet which means the page is unconfirmed. Behaviour in a real terminal window and on Windows was not tested.

## The question

On 29 August 2025 somebody asked on the Python help forum how to pass the input of a program on to a child process and pass the output of the child back out at the same time.
The posted program used two background threads with shutil.copyfileobj and then waited for the child and the program hung.
The asker wanted the program to exit once the child finishes.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

The child in the test answers every line in capital letters and stops when the line "quit" arrives.

- With the posted program the answer to the first line never arrived within 3 seconds and the program was still running 5 seconds after the "quit" line was sent.
- With the repaired program the answer HELLO arrived right away and the program exited 0.02 seconds after the child stopped with exit code 0.

## Why the posted program hangs (three causes)

1. shutil.copyfileobj reads in large blocks through a buffered reader and a buffered read waits until the whole block is full or the input ends so a single typed line can sit unread.
2. Writing into sys.stdout.buffer collects output in a buffer and nothing flushes the buffer so output can stay invisible.
3. Nothing closes the input of the child when the input of the program ends so a child that waits for the end of input waits forever.

## Best-guess answer

The repaired program worked in the test:

def pump_in():
    try:
        while chunk := os.read(sys.stdin.fileno(), 65536):
            proc.stdin.write(chunk)
    except (BrokenPipeError, OSError):
        pass
    finally:
        try: proc.stdin.close()
        except OSError: pass

def pump_out():
    while chunk := proc.stdout.read(65536):
        sys.stdout.buffer.write(chunk); sys.stdout.buffer.flush()

Thread(target=pump_in, daemon=True).start()
out = Thread(target=pump_out); out.start()
proc.wait()
out.join()
sys.exit(proc.returncode)

os.read returns as soon as any bytes are available and each piece of output is flushed at once and the input thread is a daemon thread so a read that is still waiting cannot keep the program alive after the child ends and joining the output thread makes sure every byte from the child is passed on before the exit.

The four test files sit in boring-things inside research-program-files inside unanswered-questions-scripts inside a folder named forward-test.
