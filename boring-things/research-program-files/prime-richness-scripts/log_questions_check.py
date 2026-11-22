# Rechecks the figures on the page log-questions.md in the prime-richness folder.
# Run with: python3 log_questions_check.py   (needs the free Python package mpmath)
from mpmath import mp, mpf, e, pi, euler, exp, ln, log10, sqrt, harmonic, lambertw

mp.dps = 20


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


P = primes_up_to(10 ** 6)

print('log10(5)/2', log10(5) / 2, ' log10(5/2)', log10(mpf(5) / 2), ' sqrt(5)', sqrt(5))
print('log10(997)', log10(997), ' log10(998)', log10(998), ' ln(10)', ln(10))

for n in (10, 100, 1000):
    print('n', n, ' (1+1/n)^n', (1 + mpf(1) / n) ** n, ' (1-1/n)^n', (1 - mpf(1) / n) ** n,
          ' exact 1/n step', exp(-mpf(1) / n))
print('half step', exp(-mpf(1) / 2), ' 1/7 step', exp(-mpf(1) / 7), ' 1/101 step', exp(-mpf(1) / 101))

share = mpf(1)
for p in (2, 3, 5, 7, 11):
    share *= 1 - mpf(1) / p
    print('share left after prime', p, share)

for n in (10, 100, 1000, 10 ** 6):
    print('n', n, ' sum', harmonic(n), ' ln', ln(n), ' gap', harmonic(n) - ln(n))
corners = [mpf(1) / k - ln(mpf(k + 1) / k) for k in range(1, 5)]
print('corner pieces', corners, ' total', sum(corners))

s = sum(mpf(1) / p for p in P if p <= 997)
print('sum of 1/p up to 997', s, ' ln ln 997', ln(ln(997)), ' gap', s - ln(ln(997)))

g = euler
om = lambertw(1).real
print('gap constant', g, ' sieve constant', exp(-g), ' doubled', 2 * exp(-g))
print('1/(e-1)', 1 / (e - 1), ' 1/sqrt(pi)', 1 / sqrt(pi), ' ln(pi)/2', ln(pi) / 2)
print('Omega', om, ' Omega squared', om ** 2, ' twice Omega', 2 * om)
x = g
for i in range(4):
    x = exp(-x)
    print('chain from 0.5772', x)
x = mpf(0)
for i in range(8):
    x = exp(-x)
    print('chain from 0', x)

print('bell curve heights', exp(-mpf(1) / 2), exp(-2), exp(-mpf(9) / 2))

L = ln(997)
print('primes up to 997', len([p for p in P if p <= 997]), ' primes up to one million', len(P))
print('997/ln', 997 / L, ' 997/(ln-1)', 997 / (L - 1), ' 997/e', 997 / e, ' 997/ln(499)', 997 / ln(499))
L6 = ln(10 ** 6)
print('million/(ln-1)', 10 ** 6 / (L6 - 1), ' million/(ln-1.08366)', 10 ** 6 / (L6 - mpf('1.08366')))

for n in (10, 100, 997):
    a = sum(ln(k) for k in range(1, n + 1)) / n
    print('n', n, ' average ln', a, ' ln(n)-1', ln(n) - 1, ' multiplying average', exp(a))
print('bands', 1 - 1 / e, 1 / e - 1 / e ** 2, 1 / e ** 2 - 1 / e ** 3, 1 / e ** 3)
print('band edges', 997 / e, 997 / e ** 2, 997 / e ** 3)

theta = sum(ln(p) for p in P if p <= 1009)
print('ln of product of primes up to 1009', theta, ' digits', theta / ln(10))
