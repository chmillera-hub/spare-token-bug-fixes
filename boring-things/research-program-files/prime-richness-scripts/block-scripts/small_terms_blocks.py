# Sequences with small terms written in a line and read in blocks sized to the circle
# (the block is as many digits long as the number of marks is written). Both circles get the same blocks.
# Every circle size from 2 to 5000 marks is tested with 30 steps for each mark.
# Run with: python3 small_terms_blocks.py   (needs the free Python package numpy)
import sys
import numpy as np

NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER
WMAX = len(str(NMAX)); L = WMAX * K
M = 700000
s = np.ones(12 * M, dtype=bool); s[:2] = False
for i in range(2, int((12 * M) ** 0.5) + 1):
    if s[i]: s[i * i::i] = False
pr = np.flatnonzero(s)[:M]
div = np.zeros(M + 1, dtype=np.int64)
for d in range(1, M + 1): div[d::d] += 1
steps = []; odd = []
cache = {1: (0, 0)}
for st in range(1, 400001):
    n = st; stack = []
    while n not in cache:
        stack.append(n); n = n // 2 if n % 2 == 0 else 3 * n + 1
    c, o = cache[n]
    for v in reversed(stack):
        c += 1; o += v % 2; cache[v] = (c, o)
    steps.append(cache[st][0]); odd.append(cache[st][1])
rep = np.floor(0.5 + np.sqrt(2.0 * np.arange(1, M + 1))).astype(np.int64)


def line(vals):
    t = ''.join(map(str, vals))
    assert len(t) >= L, len(t)
    return np.frombuffer(t[:L].encode(), dtype=np.uint8).astype(np.int64) - 48


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


src = {
    'gaps between neighboring primes (1 2 2 4 2 4 2 4 6 2)': line(np.diff(pr).tolist()),
    'number of divisors of n (1 2 2 3 2 4 2 4 3 4)': line(div[1:].tolist()),
    'Collatz steps for each start (0 1 7 2 5 8 16 3 19 6)': line(steps),
    'Collatz odd steps for each start (0 0 2 0 1 2 5 0 6 1)': line(odd),
    'each number n repeated n times (1 2 2 3 3 3 4 4 4 4)': line(rep.tolist()),
    'the primes written in a line (2 3 5 7 11 13 17 19 23)': line(pr.tolist()),
    'the doublings written in a line (1 2 4 8 16 32 64 128)': line([2 ** k for k in range(0, 2100)]),
}
f = [1, 1]; tot = 2
while tot < L:
    f.append(f[-1] + f[-2]); tot += len(str(f[-1]))
src['the Fibonacci numbers written in a line (1 1 2 3 5 8 13 21)'] = line(f)
pw = {w: 10 ** np.arange(w - 1, -1, -1) for w in range(1, WMAX + 1)}
print('circle sizes tested:', NMAX - 1)
print('total out of 200 | cumulative average, literal average | sizes filled: cumulative, literal, both | on 360 marks: cumulative, literal')
out = []
for name, d in src.items():
    blocks = {w: d[:(L // w) * w].reshape(-1, w) @ pw[w] for w in range(1, WMAX + 1)}
    a = np.array([cover(np.mod(blocks[len(str(N))][:PER * N], N), N) for N in range(2, NMAX + 1)])
    out.append((name, a))
for name, a in sorted(out, key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())):
    print('%-62s %6.1f | %5.1f %5.1f | %4d %4d %4d | %3d %3d' % (name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum()), round(a[358, 1] * 360), round(a[358, 0] * 360)))
