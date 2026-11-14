# Tests three routes for parallel work with objects that the standard pickle module cannot serialize (Python forum topic 106518)
import sys, pickle
from concurrent.futures import ProcessPoolExecutor
import dill

def run_dill_payload(payload):
    func, arg = dill.loads(payload)      # the worker rebuilds the function and the argument from dill bytes
    return func(arg)

def make_adder(n):
    return lambda x: x + n               # a lambda made inside a function: standard pickle refuses it

if __name__ == "__main__":
    print("Python", sys.version.split()[0], "| dill", dill.__version__)
    add5 = make_adder(5)
    try:
        pickle.dumps(add5); print("standard pickle: worked")
    except Exception as e:
        print("standard pickle fails:", type(e).__name__)
    try:
        with ProcessPoolExecutor(2) as ex:
            print("route 0 (plain ProcessPoolExecutor):", list(ex.map(add5, range(4))))
    except Exception as e:
        print("route 0 (plain ProcessPoolExecutor) fails:", type(e).__name__)
    with ProcessPoolExecutor(2) as ex:
        payloads = [dill.dumps((add5, i)) for i in range(4)]
        print("route 1 (standard ProcessPoolExecutor carrying dill bytes):", list(ex.map(run_dill_payload, payloads)))
    import multiprocess
    with multiprocess.Pool(2) as pool:
        print("route 2 (the multiprocess package, version " + multiprocess.__version__ + "):", pool.map(add5, range(4)))
