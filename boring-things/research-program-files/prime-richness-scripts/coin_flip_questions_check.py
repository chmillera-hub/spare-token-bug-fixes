# Rechecks the figures on the page coin-flip-questions.md in the prime-richness folder.
# Run with: python3 coin_flip_questions_check.py   (needs the free Python packages numpy and mpmath)
import math
import numpy as np
from mpmath import mp, li, sqrt

N = 10 ** 7
sieve = np.ones(N + 1, dtype=bool)
sieve[:2] = False
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
primes = np.nonzero(sieve)[0]

print('--- lap lengths')


def lap(a, n):
    out, v = [], a % n
    while True:
        out.append(v)
        if v == 1:
            return out
        v = v * a % n


for a, n in ((7, 15), (3, 7), (2, 7), (6, 7), (2, 5), (2, 21), (14, 15), (4, 15)):
    print('powers of', a, 'with remainders after dividing by', n, lap(a, n))
print('7*7 leaves', 49 % 15, ' shared pieces', math.gcd(4 - 1, 15), math.gcd(4 + 1, 15), ' for 21:', math.gcd(8 - 1, 21), math.gcd(8 + 1, 21))
print('step numbers for 7 with base 3', {v: k + 1 for k, v in enumerate(lap(3, 7))}, ' 2*6 leaves', 12 % 7)
for p in (7, 11, 13, 17, 37):
    print('repeat length of 1 over', p, len(lap(10, p)))
print('squarings needed for a power of one million', math.log2(10 ** 6))
print('count of 1024 bit primes is about 10 to the power', (1023 * math.log(2) - math.log(1024 * math.log(2))) / math.log(10))

print('--- numbers with no repeated prime piece and the plus and minus tally')
sign = np.ones(N + 1, dtype=np.int8)
count = np.zeros(N + 1, dtype=np.int8)
for p in primes:
    sign[p::p] *= -1
    count[p::p] += 1
    if p * p <= N:
        sign[p * p::p * p] = 0
sign[0] = 0
lead = np.cumsum(sign.astype(np.int64))
for x in (10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
    plus = int((sign[1:x + 1] == 1).sum())
    minus = int((sign[1:x + 1] == -1).sum())
    print('up to', x, ' no repeats', plus + minus, ' predicted', 6 * x / math.pi ** 2, ' plus', plus, ' minus', minus,
          ' lead', int(lead[x]), ' square root', math.sqrt(x))
M = 10 ** 6
ok = sign[:M + 1] != 0
print('breakdown by piece count up to one million', np.bincount(count[:M + 1][ok]))
print('up to 30: in', [n for n in range(1, 31) if sign[n] != 0], ' out', [n for n in range(1, 31) if sign[n] == 0])
pr = 1.0
for p in (2, 3, 5, 7):
    pr *= 1 - 1 / p ** 2
    print('share left after removing multiples of', p * p, pr)
print('heights at one million: power 0.25', 10 ** 1.5, ' power 0.4', 10 ** 2.4, ' power 0.8', 10 ** 4.8, ' at ten million power 0.8', 10 ** 5.6)

print('--- the fence for the prime count if the critical line claim holds')
pc = np.cumsum(sieve)
for x in (10 ** 6, 10 ** 7):
    print('x', x, ' primes', int(pc[x]), ' miss', float(li(x) - li(2)) - int(pc[x]), ' fence', math.sqrt(x) * math.log(x) / (8 * math.pi))

print('--- square roots')
print('perfect squares up to one million', int(math.isqrt(10 ** 6)))
mp.dps = 100010
d = str(sqrt(2))[2:100002]
c = [d.count(str(i)) for i in range(10)]
even = sum(c[0::2])
print('digit counts of the square root of 2', c, ' largest miss', max(abs(v - 10000) for v in c), ' typical wobble', math.sqrt(100000 * 0.1 * 0.9))
print('even digits', even, ' odd digits', 100000 - even, ' typical wobble', math.sqrt(100000) / 2)
