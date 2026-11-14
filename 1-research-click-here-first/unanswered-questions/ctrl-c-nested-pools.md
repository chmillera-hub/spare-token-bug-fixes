# Stopping a thread pool inside a process pool right away on Ctrl-C

## Link to the original question

https://discuss.python.org/t/88003

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 on Linux and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 11 April 2025 somebody asked on the Python help forum how to shut down a program cleanly on Ctrl-C on Linux when a process pool runs a function that itself runs a 10 second job inside a thread pool.
The asker treats the 10 second job as a black box that cannot be changed.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test sent the Ctrl-C signal to the whole process group after 1.5 seconds (the same thing a terminal does).

- The posted program exited 8.6 seconds after Ctrl-C which is the full remaining run time of the 10 second job.
- The repaired program exited 0.0 seconds after Ctrl-C with exit code 130 and left no worker processes behind.

## Why the posted program waits

A thread that is inside a sleep or another blocking call cannot be interrupted from outside in Python and a thread pool waits for its threads when the pool shuts down. The worker process therefore stays alive until the job ends and the parent waits for the worker.

## Best-guess answer

Because the job cannot be interrupted the fast route is to end the whole worker process. The repair that worked in the test has two parts:

- Workers ignore Ctrl-C (an initializer calls signal.signal(signal.SIGINT, signal.SIG_IGN)) so only the parent reacts.
- The parent catches KeyboardInterrupt and kills the worker processes and shuts the pool down without waiting.

except KeyboardInterrupt:
    for proc in list(pool._processes.values()): proc.kill()
    pool.shutdown(wait=False, cancel_futures=True)
    sys.exit(130)

The attribute pool._processes is a private detail of the Python library that could change in a later version and Python 3.14 added public methods for ending workers as remembered from the Python documentation.
Killing a worker gives the job no chance to clean up after itself so half-written files are possible.

The test file named sigint_nested.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
