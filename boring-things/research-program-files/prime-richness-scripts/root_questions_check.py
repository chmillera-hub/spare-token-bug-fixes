# Rechecks the figures on the page root-questions.md in the prime-richness folder.
# Run with: python3 root_questions_check.py   (needs the free Python package mpmath)
import math
from mpmath import mp, mpf, sqrt, factorial, primezeta, zeta, pi, e, ln, exp

mp.dps = 20

print('--- the source row for the dial setting 1/2')
for n in (1, 2, 3, 4, 5, 6, 9, 100):
    print('source', n, ' strength', 1 / math.sqrt(n), ' position on the logarithm ruler', math.log(n))
print('strength lost per unit of position', math.exp(-0.5), ' 0.707 * 0.577', (1 / math.sqrt(2)) * (1 / math.sqrt(3)), ' 1/sqrt(6)', 1 / math.sqrt(6))

print('--- patterns in square roots')
r = [math.sqrt(n) for n in range(10, 16)]
print('roots of 10 to 15', [round(v, 3) for v in r], ' steps', [round(b - a, 3) for a, b in zip(r, r[1:])])
print('root of 107', math.sqrt(107), ' shortcut', 10 + 7 / 20, ' 99/70', 99 / 70, ' root of 2', math.sqrt(2))


def tower(n):
    a0 = math.isqrt(n)
    if a0 * a0 == n:
        return a0, []
    m, d, a, block = 0, 1, a0, []
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        block.append(a)
        if a == 2 * a0:
            return a0, block


for n in (2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 19, 21, 23, 26, 29):
    a0, block = tower(n)
    print('root of', n, ' whole part', a0, ' repeating block', block, ' length', len(block))
print('root 2 * root 3', math.sqrt(2) * math.sqrt(3), ' root 6', math.sqrt(6), ' root 12', math.sqrt(12), ' 2 root 3', 2 * math.sqrt(3))

print('--- precision')
print('1.414 * 1.732', 1.414 * 1.732, ' true', math.sqrt(6), ' off by', math.sqrt(6) - 1.414 * 1.732,
      ' relative errors', (math.sqrt(2) - 1.414) / math.sqrt(2), (math.sqrt(3) - 1.732) / math.sqrt(3), (math.sqrt(6) - 1.414 * 1.732) / math.sqrt(6))
g = 2.5
for i in range(3):
    g = (g + 6 / g) / 2
    print('guess and average round', i + 1, g)
print('2.449 * 2.449', 2.449 * 2.449)

print('--- sums with roots on the bottom')
s = 0.0
for n in range(1, 10 ** 6 + 1):
    s += 1 / math.sqrt(n * (n + 1))
    if n in (1, 2, 3, 4, 10, 100, 10 ** 4, 10 ** 6):
        print('terms', n, ' total', s, ' minus ln', s - math.log(n))
print('root of 3*4', math.sqrt(12))
t = 0.0
for n in range(1, 100):
    t += 1 / (math.sqrt(n) + math.sqrt(n + 1))
    if n in (3, 8, 99):
        print('adding roots on the bottom: terms', n, ' total', t)
tot = mpf(0)
for n in range(1, 40):
    term = 1 / sqrt(factorial(n))
    tot += term
    if n <= 10:
        print('n', n, ' term', term, ' running total', tot)
print('sum of 1/sqrt(n!)', tot, ' with a term for n = 0', tot + 1, ' pi^2/4', pi ** 2 / 4, ' e - 1', e - 1)

print('--- lamps at the roots of the primes')
for total, label in ((1 / 2 + 1 / 3 + 1 / 5, 'through 5'), (1 / 2 + 1 / 3 + 1 / 5 + 1 / 7, 'through 7'), (2, 'sum 2'), (3, 'sum 3'), (4, 'sum 4')):
    print(label, ' sum', total, ' height', 1 / math.sqrt(total), ' painter minutes', 60 / total)
print('roots', [round(math.sqrt(p), 3) for p in (2, 3, 5, 7)])

print('--- the boundary at the square root')
for a in ('1', '0.9', '0.75', '0.6', '0.55', '0.505', '0.5005'):
    a = mpf(a)
    print('power', a, ' prime lamps', primezeta(2 * a), ' whole number lamps', zeta(2 * a))
print('ln 10', ln(10))

print('--- the square root as a midpoint')
print('factor pairs of 36', [(d, 36 // d) for d in range(1, 7) if 36 % d == 0], ' root of 997', math.sqrt(997))
for t in (1000, 10 ** 6):
    print('pitch', t, ' sources needed', math.sqrt(t / (2 * math.pi)), ' whole sources', math.floor(math.sqrt(t / (2 * math.pi))))
