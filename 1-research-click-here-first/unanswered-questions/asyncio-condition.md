# Four questions about asyncio.Condition.notify_all answered by tests

## Link to the original question

https://discuss.python.org/t/90932

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the tests yet which means the page is unconfirmed. The tests used plain asyncio and not the web framework from the post.

## The question

On 6 May 2025 somebody asked on the Python help forum four things about a broadcast built on asyncio.Condition where an admin request calls notify_all and every connected client waits on the condition in a loop and sends the newest data after each wake-up.

1. With two notify_all calls in quick succession does the client loop run only once?
2. Can a cancelled admin request interrupt notify_all half way so that some clients miss the notification?
3. Does notify_all take longer with more waiting clients and could the admin request time out?
4. Can one client loop run many times before another client loop runs?

The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

1. Two notify_all calls before the waiting client got a chance to run produced exactly 1 pass through the client loop. Notifications are not counted or queued. Because the client sends the newest data after waking the client still ends up with the latest value.
2. notify_all is an ordinary function and not a coroutine so notify_all contains no point where a cancellation can interrupt the call. Either every waiting client is marked for wake-up or the call never started.
3. notify_all took 0.018 milliseconds with 10 waiting clients and 0.159 milliseconds with 200 waiting clients and about 15 milliseconds with 20000 waiting clients. The time grows with the number of clients and stays far below any web timeout at these sizes.
4. Over three rounds with clients A and B and C the wake-up order was ABCABCABC so every client ran once per round. A client can only wake again after waiting again and the next notify_all.
5. One extra finding: the posted line "broadcast_condition = asyncio.Condition" has no parentheses so the name holds the class and not a condition object and "async with broadcast_condition" fails with a TypeError. The line needs to read asyncio.Condition().

## Best-guess answer

The design delivers "the latest value at least once after the last change" and does not deliver "one send per change".
A client that needs every single change needs a queue per client (asyncio.Queue) in place of one shared condition.
The sends themselves happen while a client holds the lock of the condition in the posted code so one slow client delays the wake-up of the others and copying the data and leaving the "async with" block before sending avoids that delay. The delay was reasoned from how the lock works and was not measured.

The test file named condition_test.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
