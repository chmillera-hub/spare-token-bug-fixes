# Tests what can and cannot stop a running job in a ProcessPoolExecutor (Python forum topic 100128)
import multiprocessing as mp, os, signal, sys, time
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool

def busy(seconds):
    end = time.time() + seconds
    while time.time() < end: pass          # CPU-bound loop with no stop checks inside
    return os.getpid()

def quick(x): return x * 2

def worker(q, seconds): q.put(busy(seconds))

if __name__ == "__main__":
    print("Python", sys.version.split()[0])
    ctx = mp.get_context("spawn")
    # 1. cancel() on a job that is already running
    with ProcessPoolExecutor(1, mp_context=ctx) as ex:
        fut = ex.submit(busy, 3); time.sleep(1.0)
        t = time.time()
        print("future.cancel() on a running job returns:", fut.cancel(), "| job still finished normally:", isinstance(fut.result(), int), f"| waited {time.time() - t:.1f} s more")
    # 2. killing the worker process of the pool from outside
    ex = ProcessPoolExecutor(2, mp_context=ctx)
    fut = ex.submit(busy, 30); time.sleep(1.0)
    pid = next(iter(ex._processes))        # private attribute, shown only to demonstrate the effect
    os.kill(pid, signal.SIGKILL)
    try: fut.result(timeout=10)
    except BrokenProcessPool: print("killing one worker of the pool: the job raises BrokenProcessPool")
    try: ex.submit(quick, 1).result(timeout=10); print("the pool still accepts new jobs")
    except BrokenProcessPool: print("after that the whole pool is broken and refuses every new job")
    ex.shutdown(wait=False)
    print("the executor offers terminate_workers():", hasattr(ProcessPoolExecutor, "terminate_workers"), "(added in Python 3.14)")
    # 3. one dedicated process per cancellable job
    q = ctx.Queue()
    def start(seconds):
        p = ctx.Process(target=worker, args=(q, seconds)); p.start(); return p
    p = start(30); time.sleep(1.0)
    t = time.time(); p.terminate(); p.join()
    print(f"dedicated process: terminate() stopped the 30 second job in {time.time() - t:.2f} s | exit code {p.exitcode}")
    p2 = start(0.2); p2.join()
    print("a new dedicated process still works afterwards and returned:", q.get(timeout=5) == p2.pid)
