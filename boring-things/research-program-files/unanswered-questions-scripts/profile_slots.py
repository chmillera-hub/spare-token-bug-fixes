# Tests which calls into C code reach sys.setprofile and which reach sys.monitoring (Python forum topic 92391)
# Uses C types from the standard library in place of a hand-compiled extension.
import sys, array, collections
print("Python", sys.version.split()[0])
events = []
def handler(frame, event, arg):
    if event == "c_call": events.append(getattr(arg, "__qualname__", repr(arg)))
    return handler

def under_test():
    a = array.array("i", [1, 2])        # creating an object of a C type: runs the type's creation and init slots
    d = collections.OrderedDict(x=1)    # same for another C type
    a.append(3)                         # an ordinary C method
    len(a)                              # a built-in function
    a[0]                                # item access: runs a C slot (no method object involved)
    a + a                               # addition: runs a C slot
    d.__init__()                        # the init slot called by name through its wrapper object
    a.__len__()                         # the length slot called by name through its wrapper object

sys.setprofile(handler); under_test(); sys.setprofile(None)
print("sys.setprofile c_call events:", events)

seen = []
mon = sys.monitoring; TOOL = mon.PROFILER_ID
mon.use_tool_id(TOOL, "demo")
def on_call(code, offset, callable_, arg0):
    if code is under_test.__code__: seen.append(getattr(callable_, "__qualname__", repr(callable_)))
mon.register_callback(TOOL, mon.events.CALL, on_call)
mon.set_events(TOOL, mon.events.CALL)
under_test()
mon.set_events(TOOL, 0); mon.free_tool_id(TOOL)
print("sys.monitoring CALL events:  ", seen)
