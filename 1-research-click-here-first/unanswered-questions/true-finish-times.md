# Recording true finish times when an as_completed loop also writes to disk

## Link to the original question

https://discuss.python.org/t/89833

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the test yet which means the page is unconfirmed. The post had no code so the test rebuilt the situation from the description.

## The question

On 27 April 2025 somebody asked on the Python help forum why progress lines printed inside a concurrent.futures.as_completed loop fall further and further behind the real work.
The loop also writes each result to disk and near the end about 20 "finished" lines print within one second even though the threads finished long before.
The asker wanted to print the completion time of each thread accurately.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test ran 24 short jobs on 8 threads and handled each result in a loop with a slow step that stands in for the disk write.

- All 24 jobs had really finished after 0.15 seconds.
- The loop reached the last result after 0.98 seconds.
- The lag between a job really finishing and the loop seeing the result grew from 0 to 0.83 seconds.
- A time noted by the job itself and a time noted by a done callback agreed within 0.21 milliseconds.

## Best-guess answer

The loop handles one result at a time so every disk write delays the moment when the loop notices the next finished job. The threads keep finishing in the background and the finished results pile up which matches the burst of lines at the end.
Two repairs gave true finish times in the test:

- Let the job note its own finish time and return the time together with the result (return result, time.perf_counter()).
- Attach a callback with future.add_done_callback(...) because the callback runs at the moment the job finishes and does not wait for the loop.

Moving the disk writes into the jobs or into a separate writer thread would also stop the pile-up and that change was not tested for this page.

The test file named completion_times.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
