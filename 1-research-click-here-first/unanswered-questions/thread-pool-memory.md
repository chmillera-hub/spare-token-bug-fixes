# Where memory stays after a thread pool returned large lists

## Link to the original question

https://discuss.python.org/t/85149

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 on Linux with made-up data and no other person has rerun the test yet which means the page is unconfirmed. The real task of the asker (a Celery task reading cloud storage listings) was not available so the page tests one possible cause.

## The question

On 19 March 2025 somebody asked on the Python help forum why a worker process keeps about 1 GB of memory after a task that fetched two large object lists through a ThreadPoolExecutor with two workers.
A ProcessPoolExecutor avoided the leftover memory and caused memory spikes from copying the lists between processes so the asker wants to stay with threads.
The posted code stores the two futures in a set named pending_thread_tasks.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test task returned two lists of one million small records each through a thread pool and stored the futures in a set like the posted code.

- Memory use was 17 MiB at the start and 768 MiB while both lists were in use.
- After the task function returned with the set of finished futures still referenced from outside memory use stayed at 768 MiB.
- After the last references to the futures were dropped memory use fell to 35 MiB.
- Asking the C library to hand unused memory back to the operating system (malloc_trim) changed nothing further in the test.

## Best-guess answer

A finished future keeps its result. A set or list of futures that outlives the task (for example a module-level variable or an attribute of a long-lived object) therefore keeps both large lists alive after the task ends.
One possibility that fits the report is such a surviving reference: the futures set or the variables source_objects and target_objects or a traceback or a log record that holds the lists.
The repair that worked in the test is dropping the references when the work is done:

pending_thread_tasks.clear()
del source_objects, target_objects

A process pool hides the problem because the big lists live in child processes that end.
If memory stays high after every reference is gone the next thing worth testing is the memory allocator of the C library which can hold on to freed memory and the call ctypes.CDLL("libc.so.6").malloc_trim(0) asks the allocator to give the memory back.

The test file named thread_memory.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
