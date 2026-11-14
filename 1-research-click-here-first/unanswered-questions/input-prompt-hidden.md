# Why the input() prompt of a child process shows up only after the answer is sent

## Link to the original question

https://discuss.python.org/t/87697

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 on Linux and no other person has rerun the test yet which means the page is unconfirmed. The program of the asker was only partly readable so the test rebuilt the situation from the description.

## The question

On 9 April 2025 somebody asked on the Python help forum why the prompt text of input() in a child script does not appear on the captured output until after the parent program has already sent the answer.
The parent starts the child with subprocess.Popen and python -u and reads the output of the child line by line in a reader thread.
A plain print("123") before the input() call appeared normally.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The child prints 123 and then asks "Enter your name: " and then prints a greeting.

- With a reader that reads line by line the parent received only "123" before any answer was sent. After the answer was sent the parent received "Enter your name: hello Ada" as one single line.
- With a reader that takes whatever bytes have arrived the parent received "123" and "Enter your name: " before any answer was sent and the greeting afterwards.

## Best-guess answer

The child writes the prompt at the right moment. The prompt has no line break at its end and a line-by-line reader hands text over only after a line break arrives. The first line break after the prompt comes from the greeting so the prompt stays stuck inside the reader until then.
The repair that worked in the test is a reader that does not wait for line breaks:

def read_chunks():
    while chunk := os.read(p.stdout.fileno(), 4096):
        q.put(chunk.decode())

The Popen call for that reader uses bufsize=0 and leaves out text=True so the pipe hands over raw bytes right away.

The two test files sit in boring-things inside research-program-files inside unanswered-questions-scripts inside a folder named prompt-test.
