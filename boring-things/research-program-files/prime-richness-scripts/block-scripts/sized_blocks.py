# Digit rows read in blocks sized to the circle: the block is as many digits long as the number of marks is written
# (1 digit for 2 to 9 marks and 2 digits for 10 to 99 marks and 3 digits for 100 to 999 marks and 4 digits for 1000 to 5000 marks).
# Both circles get the same blocks. Every circle size from 2 to 5000 marks is tested with 30 steps for each mark.
# Run with: python3 sized_blocks.py   (needs the free Python packages numpy and mpmath)
import sys
import numpy as np
from mpmath import mp

NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER
WMAX = len(str(NMAX))
mp.dps = WMAX * K + 50


def digits(x):
    s = mp.nstr(x, WMAX * K + 20).split('.')[1][:WMAX * K]
    return np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int64) - 48


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


L = WMAX * K
champ = np.frombuffer(''.join(str(i) for i in range(1, 140000)).encode(), dtype=np.uint8).astype(np.int64)[:L] - 48
assert len(champ) == L
rng = np.random.default_rng(1)
src = {
    'digits of pi': digits(mp.pi), 'digits of e': digits(mp.e), 'digits of the golden ratio': digits(mp.phi),
    'digits of the root of 2': digits(mp.sqrt(2)), 'digits of the root of 3': digits(mp.sqrt(3)), 'digits of the root of 5': digits(mp.sqrt(5)),
    'digits of the root of 7': digits(mp.sqrt(7)), 'digits of the natural logarithm of 2': digits(mp.log(2)),
    'digits from a random number generator': rng.integers(0, 10, L),
    'the counting numbers written in a line (123456789101112)': champ,
    'digits of 1 divided by 7 (repeats 142857)': np.resize(np.array([1, 4, 2, 8, 5, 7], dtype=np.int64), L),
    '1 + 1 + 1 + 1 (read as 11 or 111 or 1111)': np.ones(L, dtype=np.int64),
    '7 + 7 + 7 + 7 (read as 77 or 777 or 7777)': np.full(L, 7, dtype=np.int64),
    '1 + 2 + 1 + 2 (read as 12 or 121 and 212 or 1212)': np.resize(np.array([1, 2], dtype=np.int64), L),
}
pw = {w: 10 ** np.arange(w - 1, -1, -1) for w in range(1, WMAX + 1)}
blocks = {name: {w: d[:(L // w) * w].reshape(-1, w) @ pw[w] for w in range(1, WMAX + 1)} for name, d in src.items()}
print('circle sizes tested:', NMAX - 1)
print('total out of 200 | cumulative average, literal average | sizes filled: cumulative, literal, both | lowest literal share and the size')
rows = []
for name in src:
    a = np.array([cover(np.mod(blocks[name][len(str(N))][:PER * N], N), N) for N in range(2, NMAX + 1)])
    rows.append((name, a))
for name, a in sorted(rows, key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())):
    i = int(a[:, 0].argmin())
    print('%-58s %6.1f | %5.1f %5.1f | %4d %4d %4d | %5.1f%% at %d' % (name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum()), 100 * a[i, 0], i + 2))
a = dict(rows)['digits of pi']
for N in (9, 10, 99, 100, 360, 999, 1000, 5000):
    if N <= NMAX: print('pi on %4d marks: literal %5.1f%%  cumulative %5.1f%%  block length %d' % (N, 100 * a[N - 2, 0], 100 * a[N - 2, 1], len(str(N))))
print('pi literal circle not full on sizes:', [N for N in range(2, NMAX + 1) if a[N - 2, 0] < 1][:20])
