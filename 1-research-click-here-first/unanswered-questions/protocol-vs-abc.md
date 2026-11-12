# What Python Protocol classes and ABC classes each enforce

## Link to the original question

https://discuss.python.org/t/97537

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 3 July 2025 somebody asked on the Python help forum why a Protocol class can carry a method with a real body that subclasses inherit and whether any reason remains to use ABC classes and what the catch is.
A Protocol describes the shape a class needs (structural typing) and an ABC is a base class with abstract methods that subclasses have to fill in.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

1. A class that inherits a protocol method with a body can be created and the body runs. Python allows protocol methods with bodies as default behaviour for classes that inherit the protocol on purpose.
2. A class that inherits a protocol and forgets the method can still be created and calling the method silently runs the empty placeholder and returns None. Nothing warns at run time.
3. An ABC subclass that forgets an abstract method cannot be created because Python raises a TypeError that names the missing method.
4. A protocol method marked with abstractmethod is enforced the same way for classes that inherit the protocol.
5. An isinstance check against a runtime_checkable protocol only looks for the method name: a class with a method of the wrong signature passed the check.
6. A class that never inherits anything counted as an instance of the protocol and did not count as an instance of the ABC.
7. An ABC can carry stored state and shared helper methods.
8. A protocol class itself cannot be created directly.

## Best-guess answer

The catch is in results 2 and 5: a plain Protocol enforces nothing at run time for subclasses that forget a method and the isinstance check is shallow so the protection of a Protocol comes mostly from a type checker run before the program starts.
An ABC still fits when missing methods should stop the program at object creation and when subclasses should share stored state or helper methods and when "is a member of this family" should mean "inherits from this base class on purpose".
A Protocol fits when unrelated classes (including classes from other libraries) should count without inheriting anything.
The two tools combine because abstractmethod works inside a Protocol (result 4).

The test file named protocol_vs_abc.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
