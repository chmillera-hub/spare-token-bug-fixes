# Shows why a lambda inside a string annotation loses its global names after typing.get_type_hints (Python forum topic 103831)
from __future__ import annotations
from typing import get_type_hints
import sys, typing, inspect

FIND_ME = 42

def function():
    return FIND_ME

class Example:
    my_function: function
    my_lambda: lambda: FIND_ME

print("Python", sys.version.split()[0])
hints = get_type_hints(Example)
print("my_function() ->", hints["my_function"]())
try: print("my_lambda() ->", hints["my_lambda"]())
except NameError as e: print("my_lambda() with default namespaces -> NameError:", e)
lam = hints["my_lambda"]
module_dict = sys.modules[Example.__module__].__dict__
print("the lambda's global namespace is the module dictionary:", lam.__globals__ is module_dict)
print("the lambda's global namespace holds the class contents instead:", "my_lambda" not in lam.__globals__ and "__annotations__" in lam.__globals__, "| has FIND_ME:", "FIND_ME" in lam.__globals__)
print("the regular function keeps the module dictionary it was defined in:", hints["my_function"].__globals__ is module_dict)
src = inspect.getsource(typing.get_type_hints)
print("get_type_hints contains the swap of the two namespaces:", "base_globals, base_locals = base_locals, base_globals" in src)
hints2 = get_type_hints(Example, globalns=module_dict, localns=dict(vars(Example)))
print("with both namespaces passed explicitly: my_lambda() ->", hints2["my_lambda"](), "| lambda globals is the module dictionary:", hints2["my_lambda"].__globals__ is module_dict)
hints3 = get_type_hints(Example, globalns=module_dict)
print("with only globalns passed: my_lambda() ->", hints3["my_lambda"]())
