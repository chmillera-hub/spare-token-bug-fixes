# Rechecks the figures on the page pi-ripples-questions.md in the prime-richness folder.
# Run with: python3 pi_ripples_questions_check.py
# Needs the free Python packages mpmath and numpy. The 200 zeros take a minute or two.
import math
import random
import statistics
import numpy as np
from mpmath import mp, mpf, mpc, e, pi, exp, ln, log, sqrt, zeta, zetazero, atan, tan, radians, degrees, sin

mp.dps = 20

print('--- pieces of 1/(e-1)')
run = mpf(1)
for sign, bottom in ((-1, 2), (1, 12), (-1, 720), (1, 30240), (-1, 1209600), (1, 47900160)):
    run += mpf(sign) / bottom
    print('piece 1/%d' % bottom, ' running', run)
print('target', 1 / (e - 1), ' ratios', 720 / 12, 30240 / 720, 1209600 / 30240, 47900160 / 1209600, ' (2 pi)^2', (2 * pi) ** 2)
print('leftover constants: cubes', zeta(-3), ' fifth powers', zeta(-5), ' squares', zeta(-2), ' fourth powers', zeta(-4))

print('--- lap points')
shares = [2 / (2 * pi * k) ** 2 for k in (1, 2, 3)]
print('shares', shares, ' first share of 1/12', shares[0] * 12, ' total', sum(2 / (2 * pi * k) ** 2 for k in range(1, 200000)))
print('one sideways unit in degrees', degrees(1), ' 2 pi', 2 * pi)

print('--- the 12')
print('2 pi^2', 2 * pi ** 2, ' over 1.645', 2 * pi ** 2 / mpf('1.645'), ' over zeta(2)', 2 * pi ** 2 / zeta(2), ' zeta(2)', zeta(2))
print('zeta(4)', zeta(4), ' pi^4/90', pi ** 4 / 90, ' zeta(4)*6/(8 pi^4)', zeta(4) * 6 / (8 * pi ** 4), ' 1/120', mpf(1) / 120)
t = 0.0
for n in range(1, 1001):
    t += 1 / n ** 2
    if n in (1, 2, 3, 4, 5, 1000):
        print('sum of 1/n^2 after', n, t)

print('--- lamps')
print('across', 2 / pi, ' brightness', 1 / (2 / pi) ** 2, ' pi^2/4', pi ** 2 / 4, ' pi^2/8', pi ** 2 / 8, ' times 4/3', pi ** 2 / 8 * 4 / 3)
for around in (4, 8, 16, 1024):
    R = around / (2 * pi)
    lamps = [2 * R * sin((mpf(k) / R) / 2) for k in range(1, around // 2, 2)]
    print('around', around, ' nearest straight distances', [float(v) for v in lamps[:2]], ' total brightness', 2 * sum(1 / v ** 2 for v in lamps))
t = 0.0
for k in range(4):
    t += 2 / (2 * k + 1) ** 2
    print('row of odd lamps running total', t)
print('even lamps', zeta(2) / 4)

print('--- no repeated prime piece')
N = 10 ** 6
sf = bytearray([1]) * (N + 1)
i = 2
while i * i <= N:
    sf[i * i::i * i] = bytearray(len(sf[i * i::i * i]))
    i += 1
print('count up to one million', sum(sf) - 1, ' 6/pi^2', 6 / pi ** 2)
random.seed(1)
print('pairs sharing no prime out of one million', sum(math.gcd(random.randrange(1, 10 ** 9), random.randrange(1, 10 ** 9)) == 1 for _ in range(10 ** 6)))
pr = 1.0
for p in (2, 3, 5, 7, 11, 13):
    pr *= 1 - 1 / p ** 2
    print('after removing multiples of', p * p, pr)

print('--- primes up to one hundred million')
M = 10 ** 8
s = np.ones(M + 1, dtype=bool)
s[:2] = False
for i in range(2, int(M ** 0.5) + 1):
    if s[i]:
        s[i * i::i] = False
p = np.nonzero(s)[0]
c = np.cumsum(1 / p.astype(np.float64))
print('sum of 1/p^2', float(np.sum(1 / p.astype(np.float64) ** 2)))
for top in (10, 100, 10 ** 4, 10 ** 6, 10 ** 8):
    k = np.searchsorted(p, top, side='right')
    print('top', top, ' primes', k, ' sum of 1/p', c[k - 1], ' formula', math.log(math.log(top)) + 0.2614972128)
T = 10 ** 6
om = np.zeros(T + 1, dtype=np.int8)
for q in p[p <= T]:
    om[q::q] += 1
print('average count of different prime pieces up to one million', om[2:].mean(), ' shares', np.bincount(om[2:]) / (T - 1), np.bincount(om[2:]))
print('100 digit number', math.log(math.log(10.0 ** 100)) + 0.2615)

print('--- the staircase of prime weights')
small = [int(v) for v in p[p <= 10 ** 6]]


def stair(x):
    t = 0.0
    for q in small:
        if q > x:
            break
        r = q
        while r <= x:
            t += math.log(q)
            r *= q
    return t


for x in (10 ** 4, 10 ** 5, 10 ** 6):
    print('x', x, ' staircase', stair(x), ' minus ramp over square root', (stair(x) - x) / math.sqrt(x))
print('ripple heights at one million for dials 0.5 0.9 1:', 0.1414 * 10 ** 3, 0.1414 * 10 ** 5.4, 0.1414 * 10 ** 6)
print('dial 0.6 extra loudness at one million', 10 ** 0.6)

print('--- dial at 1/2')
t = 0.0
for n in range(1, 10001):
    t += 1 / math.sqrt(n)
    if n in (100, 10000):
        print('sum of 1/sqrt(n) after', n, t, ' minus 2 sqrt', t - 2 * math.sqrt(n))
print('zeta(1/2)', zeta(0.5), ' 1/sqrt(3)', 1 / sqrt(3), ' exp(-1/sqrt(3))', exp(-1 / sqrt(3)))
print('angles', degrees(atan(mpf('0.577'))), degrees(atan(mpf('0.698'))), ' slope at 30 degrees', tan(radians(30)),
      ' slope change per hundredth of a degree', tan(radians(mpf('29.99'))) - tan(radians(mpf('29.98'))))

print('--- zeros')
Z = [zetazero(k) for k in range(1, 201)]
print('first pitches', [round(float(z.imag), 2) for z in Z[:10]])
for z in Z[:3]:
    print('pitch', float(z.imag), ' loudness', float(2 / abs(z)), ' repeat factor', float(exp(2 * pi / z.imag)))
for x in (8, 10, 12.5, 16, 20, 25, 31, 39, 49, 61):
    x = mpf(x)
    print('x', float(x), ' first three ripples', [round(float(-2 * (x ** r / r).real), 2) for r in Z[:3]])
for x in (mpf('20.5'), mpf('50.5')):
    base = x - ln(2 * pi) - ln(1 - x ** -2) / 2
    print('x', x, ' true', stair(float(x)), ' smooth only', base, ' one ripple', base - 2 * (x ** Z[0] / Z[0]).real,
          ' 200 ripples', base - sum(2 * (x ** z / z).real for z in Z))


def smooth_count(T):
    return T / (2 * pi) * log(T / (2 * pi * e)) + mpf(7) / 8


u = [float(smooth_count(z.imag)) for z in Z]
g = [u[i + 1] - u[i] for i in range(len(u) - 1)]
print('rescaled gaps: mean', statistics.mean(g), ' spread', statistics.pstdev(g), ' min', min(g), ' max', max(g),
      ' share below 0.25', sum(v < 0.25 for v in g) / len(g), ' share below 0.5', sum(v < 0.5 for v in g) / len(g))
print('waiting-time shares below 0.25 and 0.5', 1 - math.exp(-0.25), 1 - math.exp(-0.5))
print('formula at 100', float(smooth_count(100)), ' true', sum(z.imag < 100 for z in Z),
      ' formula at 396', float(smooth_count(396)), ' true', sum(z.imag < 396 for z in Z))
