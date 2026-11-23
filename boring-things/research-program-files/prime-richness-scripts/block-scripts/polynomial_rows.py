# Polynomial rows under the cumulative rule and the literal rule on every circle size from 2 to 5000 marks.
# The terms are the polynomial at x = 1 and 2 and 3 and onward.
# A polynomial repeats on a circle so each row is run for one full cycle of the running total, which makes the counts exact (no step limit).
# Run with: python3 polynomial_rows.py   (needs the free Python package numpy)
import sys, math
import numpy as np

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
FAUL = {0: 1, 1: 2, 2: 6, 3: 4, 4: 30, 5: 12, 6: 42, 7: 24}   # the running total of x to the k repeats after this many laps of the circle

# name, coefficients from the highest power down, flip signs
ROWS = [
    ('x', [1, 0], False), ('2x + 1', [2, 1], False), ('3x + 1', [3, 1], False), ('6x + 1', [6, 1], False),
    ('x²', [1, 0, 0], False), ('x³', [1, 0, 0, 0], False), ('x⁴', [1, 0, 0, 0, 0], False), ('x⁵', [1, 0, 0, 0, 0, 0], False),
    ('x⁶', [1, 0, 0, 0, 0, 0, 0], False), ('x⁷', [1, 0, 0, 0, 0, 0, 0, 0], False),
    ('x² + 1', [1, 0, 1], False), ('x² + x', [1, 1, 0], False), ('x² + x + 1', [1, 1, 1], False), ('x² + x + 41', [1, 1, 41], False),
    ('2x² + 1', [2, 0, 1], False), ('2x² + x', [2, 1, 0], False), ('3x² + x', [3, 1, 0], False), ('6x² + x', [6, 1, 0], False),
    ('x³ + x', [1, 0, 1, 0], False), ('x³ − x', [1, 0, -1, 0], False), ('x³ + x + 1', [1, 0, 1, 1], False), ('x³ + x² + x + 1', [1, 1, 1, 1], False),
    ('2x³ + x', [2, 0, 1, 0], False), ('3x³ + x', [3, 0, 1, 0], False), ('6x³ + x', [6, 0, 1, 0], False),
    ('x⁴ + x', [1, 0, 0, 1, 0], False), ('x⁵ + x', [1, 0, 0, 0, 1, 0], False), ('x⁵ − x', [1, 0, 0, 0, -1, 0], False), ('30x⁵ + x', [30, 0, 0, 0, 1, 0], False),
    ('x with flipping signs (1 − 2 + 3 − 4)', [1, 0], True), ('x² with flipping signs', [1, 0, 0], True), ('x³ with flipping signs', [1, 0, 0, 0], True),
    ('x² + x + 1 with flipping signs', [1, 1, 1], True), ('x³ + x with flipping signs', [1, 0, 1, 0], True),
]


def laps(co, flip):
    d = 1
    for k, c in enumerate(reversed(co)):
        if c: d = math.lcm(d, FAUL[k])
    return d * (2 if flip else 1)


def run(co, flip):
    out = []; L = laps(co, flip)
    for N in range(2, NMAX + 1):
        x = np.arange(1, L * N + 1, dtype=np.int64)
        xm = x % N; r = np.zeros(L * N, dtype=np.int64)
        for c in co: r = (r * xm + c) % N
        if flip: r = np.where(x % 2 == 1, r, (N - r) % N)
        seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
        seen[:] = False; seen[np.cumsum(r) % N] = True
        out.append((l / N, int(seen.sum()) / N))
    return np.array(out)


res = [(name, run(co, flip)) for name, co, flip in ROWS]
print('circle sizes tested:', NMAX - 1)
print('total out of 200 | cumulative average, literal average | sizes filled: cumulative, literal, both | first sizes where both circles fill')
for name, a in sorted(res, key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())):
    both = [N for N in range(2, NMAX + 1) if a[N - 2, 0] == 1 and a[N - 2, 1] == 1]
    print('%-40s %6.1f | %5.1f %5.1f | %4d %4d %4d | %s' % (name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), len(both), ' '.join(map(str, both[:12]))))
d = dict(res)
print('--- at 360 marks: cumulative then literal')
for name in ('x²', 'x³', 'x⁴', 'x⁵', 'x⁶', 'x⁷', 'x³ + x', 'x² + x + 41'):
    print('%-14s %3d %3d' % (name, round(d[name][358, 1] * 360), round(d[name][358, 0] * 360)))
