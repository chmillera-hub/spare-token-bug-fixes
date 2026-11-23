# Rows built from the Collatz rule (an even number is halved and an odd number n becomes 3n + 1) under the cumulative rule and the literal rule.
# Every circle size from 2 to 5000 marks is tested with at most 30 steps for each mark. A single path stops when the path reaches 1.
# Run with: python3 collatz_rows.py   (needs the free Python package numpy)
import sys
import numpy as np

NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER


def path(n):
    out = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        out.append(n)
    return out


steps = np.zeros(K + 1, dtype=np.int64); peak = np.zeros(K + 1, dtype=np.int64); odd = np.zeros(K + 1, dtype=np.int64)
for s in range(1, K + 1):
    n, c, o, m = s, 0, 0, s
    while n != 1:
        if n % 2: n = 3 * n + 1; o += 1
        else: n //= 2
        c += 1
        if n > m: m = n
    steps[s], peak[s], odd[s] = c, m, o
joined = []
s = 2
while len(joined) < K:
    joined += path(s); s += 1
joined = np.array(joined[:K], dtype=np.int64)
print('joined paths use the starts 2 to', s - 1, ' largest peak', int(peak.max()), ' longest path', int(steps.max()), 'steps at start', int(steps.argmax()))

rows = {
    'number of steps for each start to reach 1 (0 + 1 + 7 + 2 + 5 + 8 + 16)': steps[1:],
    'number of odd steps for each start (0 + 0 + 2 + 0 + 1 + 2 + 5)': odd[1:],
    'highest number each start reaches (1 + 2 + 16 + 4 + 16 + 16 + 52)': peak[1:],
    'all paths joined in a line (2 + 1 + 3 + 10 + 5 + 16 + 8 + 4 + 2 + 1 + 4 + 2 + 1)': joined,
}
singles = {}
for st in (27, 871, 6171, 837799, 63728127):
    singles['the single path from %d' % st] = path(st)
big = path(2 ** 3000 - 1)
singles['the single path from 2 to the power 3000 minus 1'] = big
for k, v in singles.items(): print(k, ': terms', len(v), ' digits in the largest term', len(str(max(v))))


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


res = {}
for name, t in rows.items():
    res[name] = np.array([cover(t[:PER * N] % N, N) for N in range(2, NMAX + 1)])
for name, t in singles.items():
    obj = np.array(t, dtype=object)
    res[name] = np.array([cover((obj[:PER * N] % N).astype(np.int64), N) for N in range(2, NMAX + 1)])
print('circle sizes tested:', NMAX - 1)
print('total out of 200 | cumulative average, literal average | sizes filled: cumulative, literal, both | on 360 marks: cumulative, literal')
for name, a in sorted(res.items(), key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())):
    print('%-82s %6.1f | %5.1f %5.1f | %4d %4d %4d | %3d %3d' % (name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
          int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum()), round(a[358, 1] * 360), round(a[358, 0] * 360)))
print('--- multiples of 3 inside the paths')
for name, t in singles.items():
    print(name, ': terms that are multiples of 3:', sum(1 for v in t if v % 3 == 0), 'of', len(t))
print('joined paths: share of terms that are multiples of 3:', float((joined % 3 == 0).mean()), ' even:', float((joined % 2 == 0).mean()))
a = res['all paths joined in a line (2 + 1 + 3 + 10 + 5 + 16 + 8 + 4 + 2 + 1 + 4 + 2 + 1)']
print('joined paths: literal circle not full on', int((a[:, 0] < 1).sum()), 'sizes; first few', [N for N in range(2, NMAX + 1) if a[N - 2, 0] < 1][:10])
b = res['the single path from 2 to the power 3000 minus 1']
for N in (12, 60, 360, 997, 1000):
    print('big single path on %4d marks: cumulative %5.1f%% literal %5.1f%%' % (N, 100 * b[N - 2, 1], 100 * b[N - 2, 0]))
print('big path: literal circle full on', int((b[:, 0] == 1).sum()), 'sizes; largest such size', max([N for N in range(2, NMAX + 1) if b[N - 2, 0] == 1] or [0]),
      ' sizes that are multiples of 3 among them', sum(1 for N in range(2, NMAX + 1) if b[N - 2, 0] == 1 and N % 3 == 0))
