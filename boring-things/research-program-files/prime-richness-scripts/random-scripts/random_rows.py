# Random sequences under the cumulative rule and the literal rule on every circle size from 2 to 5000 marks with 30 steps for each mark.
# Run with: python3 random_rows.py   (needs the free Python package numpy)
import sys
import numpy as np
NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


def make(seed):
    g = np.random.default_rng(seed)
    return {
        'random whole numbers from 0 to 9': g.integers(0, 10, K),
        'random whole numbers from 0 to 99': g.integers(0, 100, K),
        'random whole numbers from 0 to 999': g.integers(0, 1000, K),
        'random whole numbers from 0 to 9999': g.integers(0, 10000, K),
        'random whole numbers from 0 to 999999': g.integers(0, 1000000, K),
        'random whole numbers from 1 to 1000000000000': g.integers(1, 10 ** 12 + 1, K),
        'random even numbers from 0 to 999998': 2 * g.integers(0, 500000, K),
        'random multiples of 3 from 0 to 999999': 3 * g.integers(0, 333334, K),
        'random choice of +1 or −1': g.choice(np.array([1, -1]), K),
        'random choice of 1 or 2': g.integers(1, 3, K),
        'random primes below 1000000': None,
    }


s = np.ones(10 ** 6, dtype=bool); s[:2] = False
for i in range(2, 1000):
    if s[i]: s[i * i::i] = False
PR = np.flatnonzero(s)
print('circle sizes tested:', NMAX - 1, ' three different random seeds for each kind')
print('total out of 200 for each seed | cumulative average, literal average (first seed) | sizes filled: cumulative, literal, both (first seed)')
names = list(make(0).keys()); rows = []
for name in names:
    tots = []; first = None
    for seed in (1, 2, 3):
        d = make(seed); t = d[name]
        if t is None: t = np.random.default_rng(100 + seed).choice(PR, K)
        a = np.array([cover(np.mod(t[:PER * N], N), N) for N in range(2, NMAX + 1)])
        tots.append(100 * (a[:, 0].mean() + a[:, 1].mean()))
        if first is None: first = a
    rows.append((name, tots, first))
for name, tots, a in sorted(rows, key=lambda r: -r[1][0]):
    print('%-46s %6.1f %6.1f %6.1f | %5.1f %5.1f | %4d %4d %4d' % (name, *tots, 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum())))
a = dict((r[0], r[2]) for r in rows)['random choice of +1 or −1']
for N in (10, 100, 360, 1000, 5000): print('+1 or −1 on %4d marks: cumulative %5.1f%%  steps used %d' % (N, 100 * a[N - 2, 1], PER * N))
