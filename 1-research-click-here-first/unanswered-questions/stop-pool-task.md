# Stopping a job that is already running in a Python ProcessPoolExecutor

## Link to the original question

https://discuss.python.org/t/100128

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 on Linux and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 25 July 2025 somebody asked on the Python help forum what happens to a job in a ProcessPoolExecutor when the web request that started the job is cancelled and how to stop the process that is still running.
The asker knew the approach of passing a stop signal into the heavy function and disliked adding checks throughout the function.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

The test job was a loop that burns processor time with no stop checks inside.

- Calling future.cancel() on a job that was already running returned False and the job ran to the end (2 more seconds in the test). Cancelling only removes jobs that have not started yet.
- Killing the worker process of the pool from outside stopped the job and the job raised BrokenProcessPool and after that the whole pool refused every new job. Killing a pool worker therefore costs the entire pool.
- The executor of Python 3.13 has no method named terminate_workers and Python 3.14 added one according to the Python documentation as remembered. A test on Python 3.14 was not run.
- Starting one dedicated process per cancellable job worked cleanly: terminate() stopped a 30 second job in under 0.01 seconds and a new dedicated process ran normally afterwards.

## Best-guess answer

A cancelled request does not stop a running pool job by itself because the pool has no channel for interrupting a worker in the middle of a job.
For jobs that must be stoppable without checks inside the function a dedicated multiprocessing.Process per job (stopped with terminate()) is the route that worked in the test and the price is the start-up time of a new process for every job.
A stop signal checked inside the function remains the only route that lets the job clean up after itself because terminate() ends the process without running clean-up code.

The test file named stop_task.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
