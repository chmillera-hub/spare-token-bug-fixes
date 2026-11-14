# Which calls into C code reach sys.setprofile and which reach sys.monitoring

## Link to the original question

https://discuss.python.org/t/92391

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 with C types from the standard library in place of the hand-written extension from the post and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 18 May 2025 somebody asked on the Python help forum why special methods (such as __init__) defined in a C extension produce no events in sys.setprofile while ordinary C functions and Python-level __init__ methods do.
The asker wanted to know whether the behaviour is expected and whether another route exists for logging those calls.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test ran eight kinds of calls into C code under both tools.

- sys.setprofile reported c_call events only for array.append (an ordinary C method) and len (a built-in function).
- sys.setprofile reported nothing for creating objects of C types and nothing for item access and nothing for addition and nothing for d.__init__() or a.__len__() called by name.
- sys.monitoring (available since Python 3.12) reported CALL events for creating the two objects (with the type itself as the thing being called) and for array.append and len and also for OrderedDict.__init__ and array.__len__ called by name.
- sys.monitoring reported nothing for item access and nothing for addition.

## Best-guess answer

The missing events fit the design of the profiler hook: c_call events are tied to calls of built-in function and method objects. Creating an object of a C type runs the creation and init slots of the type directly inside the interpreter with no function object involved so no c_call event exists to report. The same applies to operators.
The route that worked in the test for logging object creation is sys.monitoring with the CALL event because the event fires for every call made by Python code and hands over the type being called. The init slot itself still stays invisible and the event for the type call stands in for the init slot.
Operators and item access on C types stayed invisible to both tools in the test.

The test file named profile_slots.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
