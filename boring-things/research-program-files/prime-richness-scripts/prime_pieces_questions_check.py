# Rechecks the figures on the page prime-pieces-questions.md in the prime-richness folder.
# Run with: python3 prime_pieces_questions_check.py   (needs the free Python package numpy)
import math
import numpy as np

N = 10 ** 7
sieve = np.ones(N + 1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
primes = np.nonzero(sieve)[0]

pieces = np.zeros(N + 1, dtype=np.int8)      # count of different prime pieces
largest = np.zeros(N + 1, dtype=np.int64)    # largest prime piece
for p in primes:
    pieces[p::p] += 1
    largest[p::p] = p

print('--- average count of different prime pieces by size')
for d in (6, 80, 100, 1000, 10 ** 6, 10 ** 9):
    print('digits', d, ' average', math.log(d * math.log(10)) + 0.2615)
print('googolplex', math.log(10.0 ** 100 * math.log(10)) + 0.2615)
for lo, hi in ((900, 1100), (9000, 11000), (90000, 110000), (900000, 1100000), (9000000, 10000000)):
    mid = (lo + hi) / 2
    print('band', lo, hi, ' measured', pieces[lo:hi + 1].mean(), ' predicted', math.log(math.log(mid)) + 0.2615)
print('1000 to 1010', [int(v) for v in pieces[1000:1011]], ' total', int(pieces[1000:1011].sum()),
      ' double log of 1000', math.log(math.log(1000)), ' ln 1000', math.log(1000))

print('--- how the stick is cut (numbers up to one million)')
M = 10 ** 6
n = np.arange(2, M + 1)
L = largest[2:M + 1]
rest = n // L
second = np.where(rest > 1, largest[rest], 1)
print('share of length in largest piece', (np.log(L) / np.log(n)).mean(), ' second', (np.log(second) / np.log(n)).mean())
print('share with a prime piece above the square root', (L.astype(float) ** 2 > n).mean(), ' ln 2', math.log(2))
cnt = np.bincount(pieces[2:M + 1])
print('shares by piece count', cnt / (M - 1), ' one to four', cnt[1:5].sum() / (M - 1), ' numbers with seven', int(cnt[7]))
print('first number with seven pieces', 2 * 3 * 5 * 7 * 11 * 13 * 17)
theta = 0.0
k = 0
for p in primes:
    theta += math.log(p)
    k += 1
    if theta / math.log(10) >= 100:
        print('product of the first', k, 'primes (up to', int(p), ') reaches 100 digits')
        break
for v, f in ((999983, '999983'), (999997, '757*1321'), (1000001, '101*9901'), (999998, '2*31*127*127'), (999999, '3*3*3*7*11*13*37')):
    print(v, f, eval(f) == v, [round(math.log(int(t)), 2) for t in f.split('*')], round(math.log(v), 2))
print('stick of 230 divided by e again and again', [round(230 / math.e ** j, 1) for j in range(7)],
      ' stick of 13.8', [round(13.8 / math.e ** j, 1) for j in range(4)])

print('--- formula for exactly k pieces at one million')
a, b = math.log(M), math.log(math.log(M))
print([round(100 * b ** (j - 1) / math.factorial(j - 1) / a, 2) for j in (1, 2, 3)])

print('--- bands of piece length')
recip = 1 / primes.astype(np.float64)
for lo, hi in ((0.69, 1.9), (1.9, 5.1), (5.1, 13.9)):
    sel = (primes > math.exp(lo)) & (primes <= math.exp(hi)) if lo > 0.69 else primes <= 5
    q = primes[sel]
    print('lengths', lo, hi, ' primes', len(q), int(q[0]), int(q[-1]), ' total', recip[sel].sum(), ' smooth', math.log(hi / lo))
run = 0.0
for p in primes[3:]:
    run += 1 / p
    if p in (7, 11, 13, 17, 19, 23, 31, 71, 163):
        print('running total from 7 through', int(p), run)
    if p > 163:
        break

print('--- the gap and the crossings')
csum = np.cumsum(recip)
for top in (10, 100, 10 ** 4, 10 ** 6, 10 ** 7):
    kk = np.searchsorted(primes, top, side='right')
    print('top', top, ' sum', csum[kk - 1], ' double log', math.log(math.log(top)), ' gap', csum[kk - 1] - math.log(math.log(top)))
print('double log of 2', math.log(math.log(2)), ' double log of 55', math.log(math.log(55)), ' 0.5772 - 0.3157', 0.5772157 - 0.3157185)
target = 1
for kk, p in enumerate(primes):
    if csum[kk] >= target:
        print('sum passes', target, 'at the prime', int(p), ' primes used', kk + 1, ' ln', math.log(p))
        target += 1
for t in (4, 5, 6):
    print('predicted crossing for', t, math.exp(math.exp(t - 0.2615)), ' digits', math.exp(t - 0.2615) / math.log(10))
print('277 to the power e', 277 ** math.e, ' 5195977 to the power e', 5195977 ** math.e, ' 59 to the power e', 59 ** math.e)
print('ratios of ln', math.log(277) / math.log(5), math.log(5195977) / math.log(277), math.exp(4 - 0.2615) / math.log(5195977))
