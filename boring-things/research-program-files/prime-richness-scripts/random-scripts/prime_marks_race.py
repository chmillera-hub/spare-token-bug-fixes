# Two prime patterns on the literal circle (the arrow lands on each prime with full turns removed).
# 1. The race: do some open marks collect more primes than others?
# 2. Repeats: how often do two primes in a row land on the same mark compared with an even share?
# Uses every prime below 100 million. Run with: python3 prime_marks_race.py   (needs the free Python package numpy)
import math
import numpy as np

LIM = 10 ** 8
s = np.ones(LIM // 2, dtype=bool)          # odd numbers only: index i stands for 2i + 1
s[0] = False
for i in range(1, int(LIM ** 0.5) // 2 + 1):
    if s[i]: s[2 * i * (i + 1)::2 * i + 1] = False
P = np.concatenate(([2], 2 * np.flatnonzero(s) + 1)).astype(np.int64)
print('primes below 100 million:', len(P))

print('--- 1. the race between marks')
for N, a, b in ((4, 3, 1), (3, 2, 1), (10, 3, 1), (10, 7, 9), (8, 3, 1), (8, 5, 1), (8, 7, 1), (12, 5, 1), (12, 7, 1), (12, 11, 1)):
    r = P % N
    ca = np.cumsum(r == a); cb = np.cumsum(r == b)
    lead = float((ca > cb).mean()); tie = float((ca == cb).mean())
    print('%2d marks: mark %2d against mark %2d: final counts %d and %d (difference %d)  mark %d ahead after %.2f%% of the primes  tied %.3f%%' % (N, a, b, ca[-1], cb[-1], ca[-1] - cb[-1], a, 100 * lead, 100 * tie))
for N in (360, 1000):
    r = P % N
    cnt = np.bincount(r, minlength=N)
    opn = [m for m in range(N) if math.gcd(m, N) == 1]
    sq = {(x * x) % N for x in range(N) if math.gcd(x, N) == 1}
    a = np.array([cnt[m] for m in opn if m in sq]); b = np.array([cnt[m] for m in opn if m not in sq])
    print('%4d marks: %d open marks; %d of them are squares of an open mark with full turns removed; average primes on a square mark %.1f and on a non-square mark %.1f (difference %.1f); spread among all open marks from %d to %d' % (
        N, len(opn), len(a), a.mean(), b.mean(), b.mean() - a.mean(), min(cnt[m] for m in opn), max(cnt[m] for m in opn)))
print('root of 100 million divided by its natural logarithm:', LIM ** 0.5 / math.log(LIM))

print('--- 2. two primes in a row on the same mark')
for N in (3, 4, 5, 6, 10, 12, 30, 360):
    Q = P[P > N]
    r = Q % N
    same = float((r[1:] == r[:-1]).mean())
    opn = sum(1 for m in range(N) if math.gcd(m, N) == 1)
    print('%3d marks: %2d open marks: an even share of repeats would be %.2f%% and the primes repeat %.2f%% of the time (%.0f%% of the even share)' % (N, opn, 100 / opn, 100 * same, 100 * same * opn))
r = P[P > 10] % 10
print('10 marks, where the arrow goes next from mark 1:', {int(b): round(100 * float(((r[:-1] == 1) & (r[1:] == b)).sum()) / float((r[:-1] == 1).sum()), 2) for b in (1, 3, 7, 9)})
print('10 marks, where the arrow goes next from mark 9:', {int(b): round(100 * float(((r[:-1] == 9) & (r[1:] == b)).sum()) / float((r[:-1] == 9).sum()), 2) for b in (1, 3, 7, 9)})
for lim in (10 ** 4, 10 ** 6, 10 ** 8):
    Q = P[(P > 10) & (P < lim)]; r = Q % 10
    print('10 marks using primes below %d: repeats %.2f%% (even share 25%%)' % (lim, 100 * float((r[1:] == r[:-1]).mean())))
