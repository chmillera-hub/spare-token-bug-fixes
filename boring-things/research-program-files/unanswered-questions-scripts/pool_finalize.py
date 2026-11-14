# Tests when a multiprocessing.util.Finalize callback gets to finish inside a Pool worker (Python forum topic 104155)
import multiprocessing, sys, time
from multiprocessing.util import Finalize

class Worker:
    def setup(self, event):
        self._event = event
        self._finalizer = Finalize(self, self._finalize, exitpriority=0)
    def work(self, _):
        time.sleep(0.01)
    def _finalize(self):
        time.sleep(0.1)
        self._event.set()

if __name__ == "__main__":
    print("Python", sys.version.split()[0])
    context = multiprocessing.get_context("spawn")
    worker = Worker(); event = context.Event()

    with context.Pool(1, initializer=worker.setup, initargs=(event,)) as pool:
        pool.map(worker.work, [None])
    time.sleep(0.5)
    print("1. pool used with a 'with' block (the block calls terminate() at its end): finalizer finished:", event.is_set())

    event.clear()
    pool = context.Pool(1, initializer=worker.setup, initargs=(event,))
    pool.map(worker.work, [None])
    pool.close(); pool.join()
    print("2. pool.close() followed by pool.join(): finalizer finished:", event.is_set())

    event.clear()
    with context.Pool(1, initializer=worker.setup, initargs=(event,)) as pool:
        pool.map(worker.work, [None])
        pool.close(); pool.join()
    print("3. close() and join() as the last lines inside the 'with' block: finalizer finished:", event.is_set())

    event.clear()
    pool = context.Pool(1, initializer=worker.setup, initargs=(event,))
    pool.map(worker.work, [None])
    pool.terminate(); pool.join()
    time.sleep(0.5)
    print("4. pool.terminate() called directly: finalizer finished:", event.is_set())
    import inspect
    print("Pool.__exit__ calls terminate():", "self.terminate()" in inspect.getsource(multiprocessing.pool.Pool.__exit__))
