# Running parallel Python work with objects that pickle cannot handle

## Link to the original question

https://discuss.python.org/t/106518

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 with dill 0.4.1 and multiprocess 0.70.19 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

Somebody asked on the Python help forum (discuss.python.org topic number 106518) how to run parallel processing when a project holds objects that the standard pickle module cannot serialize and the library named dill can.
Serializing means turning an object into bytes so the object can travel to another process.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

The test object was a small function created inside another function (a lambda) because standard pickle refuses that kind of object.

- Standard pickle failed on the test object and the plain ProcessPoolExecutor failed for the same reason.
- Route 1 worked: the main program turns the function and the argument into bytes with dill.dumps and the standard ProcessPoolExecutor carries the bytes and a small helper function in the worker rebuilds the function with dill.loads and calls the function. The four results came back as 5 and 6 and 7 and 8 as expected.
- Route 2 worked: the separate package named multiprocess is a copy of the standard multiprocessing module that uses dill inside so multiprocess.Pool(2).map accepted the test object directly and returned the same four results.

## Best-guess answer

Route 2 needs the smallest code change because only the import line changes (import multiprocess in place of import multiprocessing).
Route 1 keeps the standard library pool and needs one helper function:

def run_dill_payload(payload):
    func, arg = dill.loads(payload)
    return func(arg)

payloads = [dill.dumps((func, arg)) for arg in args]
results = list(executor.map(run_dill_payload, payloads))

Results that travel back from the worker still go through standard pickle in route 1 so a result that standard pickle cannot handle needs the same dill wrapping on the way back.

The test file named dill_parallel.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
