# Measures where memory stays after a thread pool returned two large lists (Python forum topic 85149)
import ctypes, gc, os, sys, psutil
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
print("Python", sys.version.split()[0])
proc = psutil.Process()
def rss(): return proc.memory_info().rss / 2**20
def get_bucket_objects(kind):
    return kind, [{"Key": f"folder/{kind}/object-{i:09d}.bin", "Size": i, "ETag": f"{i:032x}"} for i in range(1_000_000)]

def task():
    pending = set()
    with ThreadPoolExecutor(max_workers=2) as ex:
        pending.add(ex.submit(get_bucket_objects, "source")); pending.add(ex.submit(get_bucket_objects, "target"))
        done, _ = wait(pending, return_when=ALL_COMPLETED)
        for fut in done:
            kind, objects = fut.result()
            if kind == "source": source_objects = objects
            else: target_objects = objects
    in_use = rss()
    return in_use, pending                      # the caller keeps the set of finished futures alive, like a long-lived variable would

start = rss()
in_use, leftover = task()
print(f"start {start:.0f} MiB | while both lists are in use {in_use:.0f} MiB")
gc.collect(); print(f"after the task returned, with the finished futures still referenced: {rss():.0f} MiB")
leftover.clear(); del leftover; gc.collect()
after_refs = rss(); print(f"after the last references to the futures are dropped: {after_refs:.0f} MiB")
try:
    trimmed = ctypes.CDLL("libc.so.6").malloc_trim(0)
    print(f"after malloc_trim(0) (returned {trimmed}): {rss():.0f} MiB")
except OSError as e: print("malloc_trim not available:", e)
