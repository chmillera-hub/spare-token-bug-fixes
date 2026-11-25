"""Time checking one 500 digit prime against finding one 500 digit prime (plain Python)."""
import random, time, json
SMALL = [p for p in range(3, 2000, 2) if all(p % q for q in range(3, int(p**.5) + 1, 2))]
def rounds_test(n, rounds=20):
    d, r = n - 1, 0
    while d % 2 == 0: d //= 2; r += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1); x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def find(digits):
    tried = full = 0
    while True:
        n = random.randrange(10 ** (digits - 1), 10 ** digits) | 1; tried += 1
        if any(n % p == 0 for p in SMALL): continue
        full += 1
        if rounds_test(n): return n, tried, full
random.seed(7)
res = {}
for digits in (100, 300, 500, 1000):
    ft, ct, tr, fu = [], [], [], []
    for _ in range(12 if digits < 1000 else 5):
        t = time.perf_counter(); p, tried, full = find(digits); ft.append(time.perf_counter() - t)
        t = time.perf_counter(); assert rounds_test(p); ct.append(time.perf_counter() - t)
        tr.append(tried); fu.append(full)
    m = lambda v: sum(v) / len(v)
    res[digits] = {"check_seconds": round(m(ct), 4), "find_seconds": round(m(ft), 4), "ratio": round(m(ft) / m(ct), 1),
                   "candidates_tried": round(m(tr)), "full_checks_run": round(m(fu)), "runs": len(ft)}
json.dump(res, open("prime_timing_results.json", "w"), indent=1); print(json.dumps(res, indent=1))
