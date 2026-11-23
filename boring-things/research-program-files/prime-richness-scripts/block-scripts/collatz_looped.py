# Single Collatz paths that start over from the first term when the path reaches 1 (looped) under the cumulative rule and the literal rule.
# Every circle size from 2 to 5000 marks is tested with 30 steps for each mark.
# Run with: python3 collatz_looped.py   (needs the free Python package numpy)
import sys, math
import numpy as np

NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30


def path(n):
    out = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        out.append(n)
    return out


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


starts = [('27', 27), ('871', 871), ('6171', 6171), ('837799', 837799), ('63728127', 63728127), ('2 to the power 3000 minus 1', 2 ** 3000 - 1)]
print('circle sizes tested:', NMAX - 1)
print('looped: total out of 200 | cumulative average, literal average | sizes filled: cumulative, literal, both | on 360 marks: cumulative, literal || stopped at 1: total, cumulative average, literal average')
keep = {}
for label, s in starts:
    p = path(s); obj = np.array(p, dtype=object)
    a = []; b = []
    for N in range(2, NMAX + 1):
        base = (obj % N).astype(np.int64)
        a.append(cover(np.resize(base, PER * N), N))
        b.append(cover(base[:PER * N], N))
    a = np.array(a); b = np.array(b); keep[label] = (p, a)
    print('path from %-28s terms %5d | %6.1f | %5.1f %5.1f | %4d %4d %4d | %3d %3d || %6.1f %5.1f %5.1f' % (label, len(p), 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum()), round(a[358, 1] * 360), round(a[358, 0] * 360),
          100 * (b[:, 0].mean() + b[:, 1].mean()), 100 * b[:, 1].mean(), 100 * b[:, 0].mean()))
p, a = keep['27']
S = sum(p)
print('path from 27: sum of one pass', S, '=', ' x '.join(map(str, [2] * 6 + [5, 317])) if 2 ** 6 * 5 * 317 == S else '')
bad = [N for N in range(2, NMAX + 1) if (a[N - 2, 1] == 1) != (math.gcd(S, N) == 1)]
print('sizes where "cumulative circle filled" differs from "the size shares no prime piece with the sum of one pass":', len(bad), bad[:15])
print('sizes sharing no prime piece with the sum:', sum(1 for N in range(2, NMAX + 1) if math.gcd(S, N) == 1))
for N in (12, 60, 360, 361, 1000, 4999, 5000):
    print('path from 27 looped on %4d marks: cumulative %4d  literal %4d' % (N, round(a[N - 2, 1] * N), round(a[N - 2, 0] * N)))
