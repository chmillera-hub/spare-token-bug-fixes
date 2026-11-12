# Replacing a method in a Python test with a quick stand-in that uses self

## Link to the original question

https://discuss.python.org/t/104184

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 6 October 2025 somebody asked on the Python help forum whether a better or more common method exists for giving a mocked method access to self.
The posted test replaced a slow method with a mock and set a side effect function that takes self and the test failed with "missing 1 required positional argument: self".
The asker had found one repair (adding autospec=True) and asked about alternatives.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

Five tests passed.

- The posted version fails with a TypeError as reported because a plain mock placed on a class does not hand the object over as the first argument.
- Route 1 worked: patch.object(Pipeline, "very_expensive_method", new=quick_method). A plain function placed on the class becomes an ordinary method so self arrives without any extra work. Route 1 keeps no record of calls.
- Route 2 worked: patch.object(Pipeline, "very_expensive_method", autospec=True, side_effect=quick_method). Route 2 keeps the call record and the record includes the object as the first argument so m.assert_called_once_with(p) passes.
- Route 3 worked: patching the method on one single object with a side effect that already knows the object. Other objects of the class keep the real method.
- After each patch block ended the original method was back.

## Best-guess answer

The repair that the asker found (autospec=True) is a standard route and fits tests that also check how the method was called.
Route 1 with new= is the shortest route when the test only needs the quick behaviour and no call record.

The test file named mock_self.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
