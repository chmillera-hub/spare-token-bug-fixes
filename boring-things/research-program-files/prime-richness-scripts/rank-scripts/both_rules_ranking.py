# Ranks rows of whole numbers by how much of a circle each row reaches under two rules.
# Moving rule: each term moves the arrow that many marks (the arrow shows the running total).
# Landing rule: the arrow lands on the term itself with full turns removed.
# A negative term moves the arrow the other way around the circle.
# Every circle size from 2 to 5000 marks is tested (a different top size can be given after the file name) with 30 steps for each mark on the circle.
# Run with: python3 both_rules_ranking.py   (needs the free Python packages numpy and mpmath)
import math
import numpy as np
from mpmath import mp

import sys
NMAX, PER = (int(sys.argv[1]) if len(sys.argv) > 1 else 5000), 30
K = NMAX * PER
n = np.arange(1, K + 1, dtype=np.int64)
sign = np.where(n % 2 == 1, 1, -1).astype(np.int64)


def sieve(m):
    s = np.ones(m + 1, dtype=bool); s[:2] = False
    for i in range(2, int(m ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return s


S = sieve(22 * K)
primes = np.flatnonzero(S)[:K].astype(np.int64)
comps = np.flatnonzero(~S)[2:][:K].astype(np.int64)
mp.dps = K + 20
pid = np.array([int(c) for c in mp.nstr(mp.pi, K + 5)[2:K + 2]], dtype=np.int64)
div = np.zeros(K + 1, dtype=np.int64)
for d in range(1, K + 1): div[d::d] += 1
sqf = np.ones(2 * K + 100, dtype=bool); sqf[0] = False
for q in range(2, int((2 * K + 100) ** 0.5) + 1): sqf[q * q::q * q] = False
isq = np.array([math.isqrt(2 * k * k) for k in range(1, K + 1)], dtype=np.int64)
gold = np.array([(k + math.isqrt(5 * k * k)) // 2 for k in range(1, K + 1)], dtype=np.int64)

rows = {
 '1 + 1 + 1 + 1 (steady 1)': np.ones(K, dtype=np.int64),
 '7 + 7 + 7 + 7 (steady 7)': np.full(K, 7, dtype=np.int64),
 '1 - 1 + 1 - 1 (steady 1 with flipping signs)': sign.copy(),
 '1 + 2 + 3 + 4 (counting numbers)': n,
 '1 - 2 + 3 - 4 (counting numbers with flipping signs)': n * sign,
 '1 + 3 + 5 + 7 (odd numbers)': 2 * n - 1,
 '1 - 3 + 5 - 7 (odd numbers with flipping signs)': (2 * n - 1) * sign,
 '2 + 4 + 6 + 8 (even numbers)': 2 * n,
 '1 + 3 + 6 + 10 (triangular numbers)': n * (n + 1) // 2,
 '1 - 3 + 6 - 10 (triangular numbers with flipping signs)': n * (n + 1) // 2 * sign,
 '1 + 4 + 9 + 16 (squares)': n * n,
 '1 - 4 + 9 - 16 (squares with flipping signs)': n * n * sign,
 '1 + 8 + 27 + 64 (cubes)': n ** 3,
 '43 + 47 + 53 + 61 (the recipe n*n + n + 41)': n * n + n + 41,
 '2 + 3 + 5 + 7 (primes)': primes,
 '2 - 3 + 5 - 7 (primes with flipping signs)': primes * sign,
 '4 + 6 + 8 + 9 (composite numbers)': comps,
 '4 - 6 + 8 - 9 (composite numbers with flipping signs)': comps * sign,
 '1 + 2 + 2 + 4 (gaps between neighboring primes)': np.diff(np.flatnonzero(S))[:K].astype(np.int64),
 '1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece)': np.flatnonzero(sqf)[:K].astype(np.int64),
 '1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n)': div[1:],
 '1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2)': isq,
 '1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio)': gold,
 '1 + 4 + 1 + 5 + 9 (digits of pi)': pid,
 '1 + 2 + 4 + 5 + 7 + 8 (numbers that are not multiples of 3)': (3 * n - 1) // 2,
 '1 + 2 + 2 + 3 + 3 + 3 (each number n repeated n times)': np.floor(0.5 + np.sqrt(2.0 * n)).astype(np.int64),
 '0 + 1 + 3 + 5 + 8 + 10 (whole part of n times the natural logarithm of n)': np.floor(n * np.log(n)).astype(np.int64),
 '1 + 2 + 5 + 8 + 11 (whole part of n times the root of n)': np.array([math.isqrt(k ** 3) for k in range(1, K + 1)], dtype=np.int64),
}


def cover(r, N):
    seen = np.zeros(N, dtype=bool); seen[r] = True; l = int(seen.sum())
    seen[:] = False; seen[np.cumsum(r) % N] = True
    return l / N, int(seen.sum()) / N


def recur(kind):
    out = []
    for N in range(2, NMAX + 1):
        steps = PER * N; seq = []
        if kind == 'fib':
            a, b = 1 % N, 1 % N
            while len(seq) < steps:
                seq.append(a); a, b = b, (a + b) % N
                if a == 1 % N and b == 1 % N: break
            r = np.resize(np.array(seq, dtype=np.int64), steps)
        elif kind == 'dbl':
            a = 1 % N; first = {}
            while a not in first and len(seq) < steps:
                first[a] = len(seq); seq.append(a); a = 2 * a % N
            pre = first.get(a, len(seq)); cyc = seq[pre:] or [0]
            r = np.concatenate([np.array(seq[:pre], dtype=np.int64), np.resize(np.array(cyc, dtype=np.int64), max(steps - pre, 0))])[:steps]
        else:
            a, k = 1 % N, 1
            while len(seq) < steps:
                seq.append(a)
                if a == 0: break
                k += 1; a = a * (k % N) % N
            r = np.concatenate([np.array(seq, dtype=np.int64), np.zeros(steps - len(seq), dtype=np.int64)])
        out.append(cover(r, N))
    return np.array(out)


res = {}
for name, t in rows.items():
    assert len(t) >= K, name
    res[name] = np.array([cover(np.mod(t[:PER * N], N), N) for N in range(2, NMAX + 1)])
out = []
for N in range(2, NMAX + 1):
    r = n[:PER * N] % N; r = r * r % N; r = r * r % N
    out.append(cover(r, N))
res['1 + 16 + 81 + 256 (fourth powers)'] = np.array(out)
res['1 + 1 + 2 + 3 + 5 + 8 (Fibonacci numbers)'] = recur('fib')
res['1 + 2 + 4 + 8 + 16 (doublings)'] = recur('dbl')
res['1 + 2 + 6 + 24 + 120 (1 and 1*2 and 1*2*3)'] = recur('fact')


def first_full(t, N, cap):
    r = np.mod(t[:cap], N)
    def when(v):
        _, idx = np.unique(v, return_index=True)
        return int(idx.max()) + 1 if idx.size == N else None
    return when(r), when(np.cumsum(r) % N)


T = NMAX - 1
print('circle sizes tested:', T, ' steps for each mark:', PER)
rank = sorted(res.items(), key=lambda kv: -np.minimum(kv[1][:, 0], kv[1][:, 1]).mean())
print('--- ranking 1: average over all sizes of the lower of the two percentages (then landing average and moving average)')
for i, (name, a) in enumerate(rank, 1):
    print('%2d. %-74s %5.1f | land %5.1f move %5.1f' % (i, name, 100 * np.minimum(a[:, 0], a[:, 1]).mean(), 100 * a[:, 0].mean(), 100 * a[:, 1].mean()))
cnt = {k: (int((a[:, 1] == 1).sum()), int((a[:, 0] == 1).sum()), int(((a[:, 0] == 1) & (a[:, 1] == 1)).sum())) for k, a in res.items()}
print('--- ranking 2: number of sizes filled under both rules at once')
for i, (name, c) in enumerate(sorted(cnt.items(), key=lambda kv: -kv[1][2]), 1):
    print('%2d. %-74s %4d' % (i, name, c[2]))
print('--- ranking 3: sizes filled on the moving circle plus sizes filled on the landing circle')
for i, (name, c) in enumerate(sorted(cnt.items(), key=lambda kv: -(kv[1][0] + kv[1][1])), 1):
    print('%2d. %-74s %5d | moving %4d landing %4d' % (i, name, c[0] + c[1], c[0], c[1]))
print('--- ranking 4: moving average percentage plus landing average percentage (out of 200)')
for i, (name, a) in enumerate(sorted(res.items(), key=lambda kv: -(kv[1][:, 0].mean() + kv[1][:, 1].mean())), 1):
    print('%2d. %-74s %5.1f | moving %5.1f landing %5.1f' % (i, name, 100 * (a[:, 0].mean() + a[:, 1].mean()), 100 * a[:, 1].mean(), 100 * a[:, 0].mean()))
print('--- steps needed to fill 1000 marks: landing circle then moving circle')
for name in rows:
    if any(w in name for w in ('1 - 2 + 3 - 4', '4 + 6 + 8 + 9', 'natural logarithm', '2 + 3 + 5 + 7')):
        print('%-74s' % name, first_full(rows[name], 1000, min(K, 30000)))
print('--- which sizes get a full landing circle')
lp = res['2 + 3 + 5 + 7 (primes)'][:, 0] == 1
ls = res['1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece)'][:, 0] == 1
lo = res['1 - 3 + 5 - 7 (odd numbers with flipping signs)'][:, 0] == 1
lt = res['1 + 3 + 6 + 10 (triangular numbers)'][:, 0] == 1
sizes = range(2, NMAX + 1)
print('primes: differs from "the size is a prime" on', sum(1 for N, f in zip(sizes, lp) if f != bool(S[N])), 'sizes')
print('numbers with no repeated prime piece: differs from "the size has no repeated prime piece" on', sum(1 for N, f in zip(sizes, ls) if f != bool(sqf[N])), 'sizes')
print('odd numbers with flipping signs: differs from "the size is odd" on', sum(1 for N, f in zip(sizes, lo) if f != (N % 2 == 1)), 'sizes')
print('triangular numbers: differs from "the size is a power of 2" on', sum(1 for N, f in zip(sizes, lt) if f != (N & (N - 1) == 0)), 'sizes')
