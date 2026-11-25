"""Count the ways each even number is a sum of two primes (order ignored).

Method: sieve the primes up to N then multiply the prime indicator list by
itself with a fast Fourier transform. The product at position n counts the
ordered pairs (p then q) with p + q = n. Ways = (ordered + 1 if n/2 is prime) / 2.
Run: python3 pair_sum_counts.py   (needs numpy and about 2 GB of memory)
"""
import json, math
import numpy as np

N = 16_000_000
s = np.ones(N + 1, dtype=bool); s[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if s[i]:
        s[i * i::i] = False
L = 1 << 25
f = np.fft.rfft(s.astype(np.float64), L)
c = np.rint(np.fft.irfft(f * f, L)).astype(np.int64)[:N + 1]
del f
half = np.zeros(N + 1, dtype=np.int64)
idx = np.arange(0, N + 1, 2)
half[idx] = s[idx // 2]
u = (c + half) // 2            # u[n] = ways for even n
ev = np.arange(4, N + 1, 2)
ue = u[ev]

# self checks against hand counts
assert u[4] == 1 and u[10] == 2 and u[12] == 1 and u[100] == 6 and u[102] == 8 and u[104] == 5

out = {"N": N}
# largest even number with exactly k ways
last_exact = {}
small = ue <= 30
for n, k in zip(ev[small].tolist(), ue[small].tolist()):
    last_exact[k] = n
out["largest_with_exactly"] = {str(k): last_exact[k] for k in sorted(last_exact)}
# last even number with fewer than k ways, and how many such numbers exist
thr = {}
for k in (2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000):
    w = ev[ue < k]
    thr[str(k)] = {"last": int(w.max()), "how_many": int(len(w))}
out["last_with_fewer_than"] = thr
# floor in each range against the simple formula 0.6601618 n / ln(n)^2
C2 = 0.6601618158
rows = []
for lo, hi in ((10**3, 10**4), (10**4, 10**5), (10**5, 10**6), (10**6, 2*10**6), (2*10**6, 4*10**6), (4*10**6, 8*10**6), (8*10**6, 16*10**6)):
    m = (ev >= lo) & (ev <= hi)
    j = ue[m].argmin(); n = int(ev[m][j]); k = int(ue[m][j])
    rows.append({"range": [lo, hi], "floor_number": n, "floor_ways": k,
                 "formula": round(C2 * n / math.log(n) ** 2, 1),
                 "ratio": round(k / (C2 * n / math.log(n) ** 2), 4)})
out["floors"] = rows
# average boost for multiples of 3 against non multiples near the top of the range
m = ev >= 8 * 10**6
three = ue[m & (ev % 3 == 0)].mean(); non = ue[m & (ev % 3 != 0)].mean()
out["multiple_of_3_average_over_other_average"] = round(float(three / non), 4)
# powers of two
out["powers_of_two"] = {str(1 << e): int(u[1 << e]) for e in range(2, 24)}
json.dump(out, open("pair_sum_results.json", "w"), indent=1)
print(json.dumps(out, indent=1))
