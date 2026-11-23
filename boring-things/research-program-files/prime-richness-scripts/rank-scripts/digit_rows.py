# Rows made from the digits of constants tested under the moving rule and the landing rule.
# Each constant is used two ways: one digit at a time and four digits at a time (blocks such as 1415 then 9265).
# Every circle size from 2 to 5000 marks is tested with 30 steps for each mark.
# Run with: python3 digit_rows.py   (needs the free Python packages numpy and mpmath)
import sys
import numpy as np
from mpmath import mp

NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER
mp.dps = 4 * K + 50


def digits(x):
    s = mp.nstr(x, 4 * K + 20)
    s = s.split('.')[1][:4 * K]
    return np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int64) - 48


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


champ = np.frombuffer(''.join(str(i) for i in range(1, 140000)).encode(), dtype=np.uint8).astype(np.int64)[:4 * K] - 48
sev = np.resize(np.array([1, 4, 2, 8, 5, 7], dtype=np.int64), 4 * K)
rng = np.random.default_rng(1)
src = {
    'pi': digits(mp.pi), 'e': digits(mp.e), 'the golden ratio': digits(mp.phi),
    'the root of 2': digits(mp.sqrt(2)), 'the root of 3': digits(mp.sqrt(3)), 'the root of 5': digits(mp.sqrt(5)),
    'the root of 7': digits(mp.sqrt(7)), 'the natural logarithm of 2': digits(mp.log(2)),
    '1 divided by 7 (repeats 142857)': sev,
    'the counting numbers written in a line (123456789101112)': champ,
    'a random number generator': rng.integers(0, 10, 4 * K),
}
res = {}
for name, d in src.items():
    assert len(d) >= 4 * K, (name, len(d))
    one = d[:K]
    four = d[:4 * K].reshape(-1, 4) @ np.array([1000, 100, 10, 1])
    for tag, t in (('one digit at a time', one), ('four digits at a time', four)):
        a = np.array([cover(np.mod(t[:PER * N], N), N) for N in range(2, NMAX + 1)])
        res[(name, tag)] = a
print('circle sizes tested:', NMAX - 1)
print('digit check: e', ''.join(map(str, src['e'][:12])), ' golden ratio', ''.join(map(str, src['the golden ratio'][:12])), ' root of 2', ''.join(map(str, src['the root of 2'][:12])))
for tag in ('four digits at a time', 'one digit at a time'):
    print('---', tag, ': total out of 200 | moving average, landing average | sizes filled: moving, landing, both')
    for (name, tg), a in sorted(res.items(), key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())):
        if tg != tag: continue
        print('%-58s %6.1f | %5.1f %5.1f | %4d %4d %4d' % (name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean(),
              int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum())))
a = res[('e', 'four digits at a time')]
miss = [N for N in range(2, NMAX + 1) if a[N - 2, 0] < 1]
print('e in blocks of four: smallest size where the landing circle is not full', miss[:1], ' landing share at 5000 marks', a[-1, 0] if NMAX >= 5000 else None)
import math
print('random drops expected to leave empty at 5000 marks after 150000 drops:', 5000 * math.exp(-30), ' and for landing with values 0 to 9999 folded onto 5000 marks the same')
