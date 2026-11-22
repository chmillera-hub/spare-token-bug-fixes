# Rechecks the figures on the page lamp-questions.md in the prime-richness folder.
# Run with: python3 lamp_questions_check.py   (uses only the Python standard library)
import math
from math import gcd, pi, e, log, exp, sqrt


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


P = primes_up_to(10 ** 6)

print('--- square times a number with no repeated prime piece')
def no_repeat(n):
    return all(n % (p * p) for p in range(2, int(n ** 0.5) + 1))
def count(x):
    return sum(1 for n in range(1, x + 1) if no_repeat(n))
groups = [(k * k, count(100 // (k * k))) for k in range(1, 11)]
print(groups, ' total', sum(c for _, c in groups))
for N in (10, 100, 1000):
    print('orchard patch', N, ' visible trees', sum(1 for a in range(1, N + 1) for b in range(1, N + 1) if gcd(a, b) == 1), ' of', N * N)
print('1 over the sum of 1/n^2', 6 / pi ** 2)

print('--- products of (1 - 1/n^2)')
run = 1.0
for n in range(2, 6):
    run *= 1 - 1 / n ** 2
    print('every square through', n * n, run)
run = 1.0
for n in range(2, 100000):
    run *= 1 - 1 / n ** 2
print('every square: product heads to', run)
run = 1.0
for p in (2, 3, 5, 7):
    run *= 1 - 1 / p ** 2
    print('prime squares through', p * p, run, ' factor splits as', 1 - 1 / p, 1 + 1 / p)

print('--- prime lamps')
pile = sum(1 / p ** 2 for p in P) + 1 / (10 ** 6 * log(10 ** 6))
print('brightness of lamps at the primes', pile)
t = 0.0
for p in (2, 3, 5, 7):
    t += 1 / p ** 2
    print('through the lamp at', p, t)
print('rest', pile - t, ' share from the lamp at 2', 0.25 / pile, ' share of lamps from 2 upward', pile / (pi ** 2 / 6 - 1))
print('estimates of the share left: subtraction', 1 - pile, ' smooth', exp(-pile), ' true', 6 / pi ** 2, ' ratio', (6 / pi ** 2) / exp(-pile))
miss = [-log(1 - 1 / p ** 2) - 1 / p ** 2 for p in (2, 3, 5, 7)]
total_miss = sum(-log(1 - 1 / p ** 2) - 1 / p ** 2 for p in P)
print('chunk misses', miss, ' total', total_miss, ' real pile', pile + total_miss, ' share from the prime 2', miss[0] / total_miss)
for name, b in (('every whole number', pi ** 2 / 6), ('from 2 upward', pi ** 2 / 6 - 1), ('primes one side', pile), ('primes both sides', 2 * pile),
                ('odd lamps both sides', pi ** 2 / 4)):
    print(name, ' brightness', b, ' matching distance', 1 / sqrt(b))

print('--- lamp arithmetic')
print('2/pi', 2 / pi, ' pi^2/4', pi ** 2 / 4, ' pi^2/8', pi ** 2 / 8, ' times 4/3', pi ** 2 / 8 * 4 / 3, ' pi/2', pi / 2)
print('lamp at half a unit', 1 / 0.5 ** 2, ' distance for brightness 2', 1 / sqrt(2), ' 0.9003/0.6366', 0.9003163 / 0.6366198)
print('1/4 + 1/16 + ...', sum(0.25 ** k for k in range(1, 60)), ' with a leading 1', sum(0.25 ** k for k in range(0, 60)))

print('--- base e and other bases')
print('powers for a 1% growth', log(1.01), math.log10(1.01), math.log2(1.01))
print('pile in base 10 and base 2', pile / log(10), pile / log(2), ' checks', 10 ** (-pile / log(10)), 2 ** (-pile / log(2)))
print('100 digit number', 100 * log(10), 100 * log(10) / log(2))
print('zero events with 2 expected', exp(-2), 2 / log(10), 2 / log(2), ' half-life for an average wait of 10', 10 * log(2))
print('steady 5% for 10 years', exp(0.5), 0.5 / log(10))
print('tax numbers', log(10), 1 / log(10), log(2), 1 / log(2))
for top in (1009, 10 ** 6):
    theta = sum(log(p) for p in P if p <= top)
    print('primes up to', top, ' root of the product', exp(theta / top))
print('split 10 into equal parts', [(k, (10 / k) ** k) for k in (3, 4, 5)])
