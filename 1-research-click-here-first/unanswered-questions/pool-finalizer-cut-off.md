# Why clean-up callbacks in multiprocessing Pool workers get cut off

## Link to the original question

https://discuss.python.org/t/104155

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 on Linux with the spawn start method and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 4 October 2025 somebody asked on the Python help forum why a clean-up callback registered with multiprocessing.util.Finalize finishes in a stand-alone Process and gets cut off half way in a worker of a multiprocessing.Pool.
In the posted program the callback starts when the pool block ends and the worker process is shut down before the callback can finish.
The asker warned that a lock held by such a worker might never be released and asked whether the behaviour is known and how to let the callback finish.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- A pool used with a "with" block: the callback did not finish (the event was never set) which matches the report.
- The source code of Pool.__exit__ calls terminate() so leaving the "with" block stops the workers abruptly.
- Calling pool.terminate() directly gave the same cut-off.
- Calling pool.close() followed by pool.join(): the callback finished.
- Calling close() and join() as the last two lines inside the "with" block: the callback finished.

## Best-guess answer

The cut-off comes from terminate() and the "with" block of a Pool calls terminate() at its end by design (the Python documentation states that leaving the block calls terminate as remembered).
The repair that worked in the test is to shut the pool down gently: call pool.close() and then pool.join() before the block ends because close() lets every worker finish its work and exit normally and a normal exit runs the registered callbacks to the end.
A library that cannot control how its users close their pools cannot rely on Finalize callbacks finishing in pool workers because any user who relies on the "with" block triggers the abrupt stop.

The test file named pool_finalize.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
