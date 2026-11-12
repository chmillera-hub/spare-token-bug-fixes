# Shows why "finished" lines printed inside an as_completed loop fall behind, and two ways to record true finish times
# (Python forum topic 89833)
import sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
print("Python", sys.version.split()[0])
def job(i):
    time.sleep(0.05)                                   # every job takes the same short time
    return i, time.perf_counter()                      # the job itself notes when it finished
def slow_disk_write(): time.sleep(0.04)                # stands in for writing a result to disk in the main loop

start = time.perf_counter(); done_callback_times = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    futures = []
    for i in range(24):
        f = ex.submit(job, i)
        f.add_done_callback(lambda fut, i=i: done_callback_times.__setitem__(i, time.perf_counter()))
        futures.append(f)
    loop_times, true_times = {}, {}
    for f in as_completed(futures):
        i, finished_at = f.result()
        loop_times[i] = time.perf_counter(); true_times[i] = finished_at
        slow_disk_write()
last_true = max(true_times.values()) - start; last_loop = max(loop_times.values()) - start
lag = [loop_times[i] - true_times[i] for i in range(24)]
print(f"all 24 jobs had really finished after {last_true:.2f} s | the loop reached the last result after {last_loop:.2f} s")
print(f"lag between real finish and the loop seeing the result: smallest {min(lag):.3f} s | largest {max(lag):.3f} s")
print(f"largest gap between the time noted by the job and the time noted by the done callback: {max(abs(done_callback_times[i] - true_times[i]) for i in range(24)) * 1000:.2f} ms")
