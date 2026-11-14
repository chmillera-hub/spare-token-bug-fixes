# Tests what Protocol classes and ABC classes each enforce (Python forum topic 97537)
import sys
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
print("Python", sys.version.split()[0])

@runtime_checkable
class Proto(Protocol):
    def my_method(self) -> None: ...

class ProtoWithBody(Proto, Protocol):
    def my_method(self) -> None: print("   body inherited from the protocol ran")

class Inherits(ProtoWithBody): ...
print("1. a class that inherits a protocol method with a body can be created and the body runs:")
Inherits().my_method()

class ForgetsMethod(Proto): ...
print("2. a class that inherits a protocol and forgets the method can still be created:", ForgetsMethod() is not None, "| calling the method returns", ForgetsMethod().my_method(), "(the empty placeholder body ran silently)")

class Base(ABC):
    @abstractmethod
    def my_method(self) -> None: ...
class ForgetsAbstract(Base): ...
try: ForgetsAbstract(); print("3. ABC subclass without the method was created")
except TypeError as e: print("3. an ABC subclass that forgets an abstract method cannot be created:", e)

class ProtoStrict(Protocol):
    @abstractmethod
    def my_method(self) -> None: ...
class ForgetsStrict(ProtoStrict): ...
try: ForgetsStrict(); print("4. created")
except TypeError as e: print("4. a protocol method marked with abstractmethod is enforced for classes that inherit the protocol:", type(e).__name__)

class Unrelated:
    def my_method(self, extra, arguments): return "wrong shape"
class Missing: ...
print("5. isinstance with runtime_checkable only looks for the method name: wrong signature passes:", isinstance(Unrelated(), Proto), "| missing method passes:", isinstance(Missing(), Proto))
print("6. a class that never inherits anything still counts for the protocol:", isinstance(Unrelated(), Proto), "| for the ABC:", isinstance(Unrelated(), Base))
class WithState(ABC):
    def __init__(self): self.count = 0
    def bump(self): self.count += 1; return self.count
print("7. an ABC can carry stored state and shared helper methods for its subclasses:", WithState().bump() == 1)
try: Proto(); print("8. the protocol class itself was created")
except TypeError as e: print("8. a protocol class itself cannot be created directly:", e)
