# Rechecks the figures on the page ladder-questions.md in the prime-richness folder.
# Run with: python3 ladder_questions_check.py   (needs the free Python package mpmath)
from mpmath import mp, mpf, e, exp, ln, li, loggamma, euler

mp.dps = 20


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


P = primes_up_to(10 ** 7)

print('--- prime lengths')
print('ln 60', ln(60), ' pieces', ln(2), ln(2), ln(3), ln(5), ' ln 7', ln(7), ' ln 6', ln(6), ' ln 12', ln(12))

print('--- bookkeeping up to 997')
x = 997
tot = mpf(0)
for p in P:
    if p > x:
        break
    q, c = p, 0
    while q <= x:
        c += x // q
        q *= p
    tot += c * ln(p)
print('sum of ln n for n up to 997', loggamma(998), ' weight handed out by primes', tot)
for top in (997, 10 ** 6):
    s = sum(ln(p) / p for p in P if p <= top)
    print('top', top, ' sum of ln(p)/p', s, ' ln(top)', ln(top), ' gap', ln(top) - s)
print('sum of 1/ln(t) for t from 2 to 997', sum(1 / ln(t) for t in range(2, 998)))
print('smooth estimate at one million', li(10 ** 6) - li(2), ' true count', len([p for p in P if p <= 10 ** 6]))

print('--- round trips')
print('ln 6 + ln 7', ln(6) + ln(7), ' unpacked', exp(ln(6) + ln(7)))

print('--- powers near zero')
for t in ('1', '0.5', '0.25', '0.125', '0.001', '0.0001'):
    print('e to the', t, exp(mpf(t)))
print('e^3 e^2 e^-1', exp(3), exp(2), exp(-1), ' 10^0.001', mpf(10) ** mpf('0.001'))

print('--- Fibonacci grid')
a, b, c, d = 1, 1, 1, 0
for i in range(9):
    a, b, c, d = a + b, a, c + d, c
print('tenth power of the grid', a, b, c, d)
print('ln ln of a 100 digit number', ln(ln(mpf(10) ** 100)), ' triple', ln(ln(ln(mpf(10) ** 100))),
      ' triple at one million', ln(ln(ln(10 ** 6))))

print('--- shuffles for x^3 - 2 over primes from 5 to ten million')
cnt = {0: 0, 1: 0, 3: 0}
for p in P:
    if p < 5:
        continue
    if p % 3 == 2:
        cnt[1] += 1
    elif pow(2, (p - 1) // 3, p) == 1:
        cnt[3] += 1
    else:
        cnt[0] += 1
N = sum(cnt.values())
print(N, cnt, {k: round(100 * v / N, 2) for k, v in cnt.items()}, ' average', sum(k * v for k, v in cnt.items()) / N)
for p in (5, 7, 11, 13, 31, 43):
    print('prime', p, ' working values for x^3 - 2', [v for v in range(p) if (v ** 3 - 2) % p == 0],
          ' for x^2 + 1', [v for v in range(p) if (v * v + 1) % p == 0])

print('--- ladder')
h, s2, s3 = 1.0, 0.0, 0.0
marks = {}
import math
for n in range(2, 10 ** 6 + 1):
    s2 += (1 / n) / h
    h += 1 / n
    s3 += 1 / (n * math.log(n))
    if n in (5, 1000, 2000, 10 ** 6):
        marks[n] = (h, s2, s3)
        print('n', n, ' first notebook', h, ' second notebook', s2, ' sum of 1/(n ln n)', s3)
for top in (10, 100, 1000, 10 ** 6):
    print('sum of 1/p up to', top, sum(1.0 / p for p in P if p <= top), ' ln ln', math.log(math.log(top)))
print('rise from 1000 to one million: 1/(n ln n)', marks[10 ** 6][2] - marks[1000][2],
      ' primes', sum(1.0 / p for p in P if 1000 < p <= 10 ** 6),
      ' ln ln', math.log(math.log(10 ** 6)) - math.log(math.log(1000)))
print('total 4 needs ln x =', exp(4 - mpf('0.2615')), ' total 10 needs digits', exp(10 - mpf('0.2615')) / ln(10))
pr = mpf(1)
for k in range(1, 11):
    pr *= 1 + mpf(1) / k
print('product of (1+1/k) up to 10', pr, ' sum', sum(mpf(1) / k for k in range(1, 11)), ' ln 11', ln(11))
print('squares: sum of step/total up to 1000th', sum((2.0 * n - 1) / n ** 2 for n in range(1, 1001)), ' ln', math.log(1000.0 ** 2))

print('--- chunks')
for n in (1, 2, 4, 10, 100, 1000):
    print('n', n, ' (1+1/n)^n', (1 + mpf(1) / n) ** n, ' n ln(1+1/n)', n * ln(1 + mpf(1) / n))
for a in ('1', '0.5', '0.1', '0.01'):
    a = mpf(a)
    print('announce', a, ' chunk', 1 + a, ' smooth', exp(a), ' chunk worth', ln(1 + a), ' shrink chunk', 1 - a, ' smooth shrink', exp(-a))
miss = [float(mpf(1) / p + ln(1 - mpf(1) / p)) for p in (2, 3, 5, 7)]
allmiss = sum(1.0 / p + math.log(1 - 1.0 / p) for p in P)
print('prime chunk misses', miss, ' total over primes to ten million', allmiss, ' 0.5772 minus that', float(euler) + allmiss)

print('--- sums that total 1')
print(sum(mpf(1) / 2 ** n for n in range(1, 60)), sum(mpf(2) / 3 ** n for n in range(1, 60)),
      sum(mpf(1) / (n * (n + 1)) for n in range(1, 5)), (e - 1) * sum(exp(-n) for n in range(1, 80)))
f, run = 1, mpf(0)
for n in range(1, 5):
    f *= (n + 1)
    run += mpf(n) / f
    print('n/(n+1)! running total', run)

print('--- slots')
for n in (10, 100, 1000):
    print('slots', n, ' zero', (1 - mpf(1) / n) ** n, ' one', (1 - mpf(1) / n) ** (n - 1))
print('expected 1:', [float(exp(-1) / math.factorial(k)) for k in range(5)], ' expected 2:', float(exp(-2)), float(2 * exp(-2)))
