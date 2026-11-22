# Rechecks the figures on the page strip-questions.md in the prime-richness folder.
# Run with: python3 strip_questions_check.py   (needs the free Python package mpmath)
from mpmath import mp, mpf, mpc, e, pi, exp, ln, sqrt, zeta, siegelz, nzeros, cos, sin, degrees

mp.dps = 15

print('--- e to the power 1/n against 1 + 1/n')
for n in (1000, 100, 10, 5, 2, 1):
    true = exp(mpf(1) / n)
    miss = true - (1 + mpf(1) / n)
    print('n', n, ' true', true, ' miss', miss, ' rule 1/(2 n n)', mpf(1) / (2 * n * n), ' miss as a share of 1/n', miss * n)

print('--- the 1/12 three ways')
print('1/4 - 1/6', mpf(1) / 4 - mpf(1) / 6, ' zeta(2)/(2 pi^2)', zeta(2) / (2 * pi ** 2), ' 2 pi^2', 2 * pi ** 2)
print('lap shares', [1 / (2 * (pi * k) ** 2) for k in (1, 2, 3)], [2 * (pi * k) ** 2 for k in (1, 2, 3)])
print('lamp with brightness 1/12 sits at', sqrt(12), ' pi sqrt 2', pi * sqrt(2), ' 0.7797 * that', sqrt(6) / pi * pi * sqrt(2))

print('--- lamps against strips')
tail = zeta(2) - sum(mpf(1) / n ** 2 for n in range(1, 10))
print('lamps from 10 outward', tail, ' strip', mpf(1) / 10, ' half lamp', mpf(1) / 200, ' tax', mpf(2) / 12 / 1000, ' sum', mpf(1) / 10 + mpf(1) / 200 + mpf(2) / 12 / 1000)
for n in (1, 2, 3, 10):
    print('centered strip piece at', n, 1 / (mpf(n) ** 2 - mpf(1) / 4), ' lamp', mpf(1) / n ** 2)
print('strip from one half outward', 1 / mpf('0.5'), ' lamps', zeta(2))
for n in (3, 5):
    print('half strength piece around odd lamp', n, 1 / (mpf(n) ** 2 - 1), ' lamp', mpf(1) / n ** 2)
odd = pi ** 2 / 8
print('odd lamps from 3 outward', odd - 1, ' half strength strip from 2', mpf(1) / 4)
odd11 = odd - sum(mpf(1) / n ** 2 for n in (1, 3, 5, 7, 9))
print('odd lamps from 11 outward', odd11, ' pieces', mpf(1) / 22, mpf(1) / 242, mpf(1) / (3 * 1331), ' sum', mpf(1) / 22 + mpf(1) / 242 + mpf(1) / (3 * 1331))

print('--- the leftover along the dial (lamps minus the strip from 1 outward)')
for s in ('2', '1.5', '1.1', '1.01', '1.001', '0.5', '0'):
    s = mpf(s)
    print('dial', s, ' lamps', zeta(s), ' leftover', zeta(s) - 1 / (s - 1))
print('corner pieces for 1/n', [float(mpf(1) / n - ln(mpf(n + 1) / n)) for n in range(1, 5)])
print('corner pieces for 1/n^2', [float(mpf(1) / (n * n * (n + 1))) for n in range(1, 5)], ' 0.6449 - 0.5772', zeta(2) - 1 - mp.euler)

print('--- how the totals are computed')
s = mpf('1.01')
for N in (10 ** 3, 10 ** 6):
    d = sum(mpf(n) ** -s for n in range(1, N + 1))
    print('first', N, 'lamps', d, ' still to add', zeta(s) - d)


def pieces(s, N):
    return (sum(mpf(n) ** -s for n in range(1, N)), mpf(N) ** (1 - s) / (s - 1), mpf(N) ** -s / 2, s / 12 * mpf(N) ** (-s - 1))


for s in (mpf('1.01'), mpf('1.001'), mpf('0.5')):
    N = 10 if s > 1 else 30
    p = pieces(s, N)
    print('dial', s, ' lamps below', N, p[0], ' strip', p[1], ' half lamp', p[2], ' tax', p[3], ' total', sum(p), ' true', zeta(s))

print('--- arrows on the critical line')
for t in ('14.134725', '21.022040', '10', '18'):
    s = mpc(0.5, mpf(t))
    p = pieces(s, 30)
    print('pitch', t, ' lamps 1 to 29', p[0], ' strip and corrections', p[1] + p[2] + p[3], ' leftover length', abs(sum(p)), ' true', abs(zeta(s)))
t = mpf('14.134725')
pos = mpc(0, 0)
for n in (1, 2, 3, 4):
    a = mpf(n) ** mpc(-0.5, -t)
    pos += a
    print('speaker', n, ' length', abs(a), ' arrow', a, ' running position', pos)
for t in (10, 14.134725, 18, 21.02204, 23, 25.010858, 28, 30.424876, 31.7):
    print('pitch', t, ' value on the line', float(siegelz(t)))
print('smallest leftover near the first zero with the dial at 0.7', min(abs(zeta(mpc(0.7, 14 + k * mpf('0.01')))) for k in range(40)))
print('zeros below 100 and 1000 and one million', nzeros(100), nzeros(1000), nzeros(10 ** 6))
print('others at dial 2', zeta(2) - 1)

print('--- growth at the dial setting 1/2')
tot = mpf(0)
for n in range(1, 10001):
    tot += 1 / sqrt(n)
    if n in (100, 10000):
        print('sum of 1/sqrt(n) to', n, tot, ' minus 2 sqrt', tot - 2 * sqrt(n))
for h in ('0.5', '0.1', '0.01', '0.0001'):
    h = mpf(h)
    print('h', h, ' (100^h - 1)/h', (mpf(100) ** h - 1) / h)
print('ln 100', ln(100))
