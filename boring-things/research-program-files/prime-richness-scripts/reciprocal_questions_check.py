# Rechecks the figures on the page reciprocal-questions.md in the prime-richness folder.
# Run with: python3 reciprocal_questions_check.py   (needs the free Python package mpmath)
from mpmath import mp, mpf, e, pi, exp, ln, li, sqrt, zeta, nsum, inf

mp.dps = 20


def primes_up_to(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


P = primes_up_to(10 ** 6)

print('--- reciprocal realm')
for a, b in ((3, 6), (4, 12), (10, 10), (2, 1000), (6, 6), (3, 3)):
    print('times', a, b, ' together', 1 / (mpf(1) / a + mpf(1) / b), ' product over sum', mpf(a * b) / (a + b))
print('three painters 2 3 6', 1 / (mpf(1) / 2 + mpf(1) / 3 + mpf(1) / 6))
print('rate average of 3 and 6', 2 * mpf(3 * 6) / 9, ' of 60 and 30', 2 * mpf(60 * 30) / 90)
print('squaring realm 3 4', sqrt(9 + 16), ' 1/3 - 1/5', mpf(1) / 3 - mpf(1) / 5, ' 2/15', mpf(2) / 15)
print('ln(1 - 1/101)', ln(1 - mpf(1) / 101), ' -1/101', -mpf(1) / 101, ' ln(1/5)', ln(mpf(1) / 5))
print('steps: 1/3 - 1/4', mpf(1) / 3 - mpf(1) / 4, ' ln4 - ln3', ln(4) - ln(3))
print('tail of 1/(k(k+1)) from k = 5', nsum(lambda k: 1 / (k * (k + 1)), [5, inf]))

print('--- painters along the number line')
rates = [1 / ln(t) for t in range(10, 21)]
print('rates 10 to 20', [float(r) for r in rates], ' total', sum(rates), ' true primes', len([p for p in P if 10 <= p <= 20]))
print('stretch over predicted', 11 / sum(rates), ' ln 15', ln(15), 1 / ln(15))
out = [n * n + n + 41 for n in range(10)]
r = [1 / ln(v) for v in out]
print('outputs', out, ' rates', [round(float(v), 3) for v in r], ' total', sum(r), ' ratio', 10 / sum(r))
print('rates 2 to 997', sum(1 / ln(t) for t in range(2, 998)), ' true', len([p for p in P if p <= 997]))
print('smooth estimate at one million', li(10 ** 6) - li(2), ' true', len(P))

print('--- smoothing')
w = [p for p in P if 1000 < p < 1100]
print('primes between 1000 and 1100', len(w), ' 1/ln(1050)', 1 / ln(1050))
s = sum(mpf(1) / p for p in P)
smooth = ln(ln(10 ** 6)) + mpf('0.26149721284764')
print('sum of 1/p to one million', s, ' smooth formula', smooth, ' difference', s - smooth)
print('count minus smooth estimate', li(10 ** 6) - li(2) - len(P), ' as a share', (li(10 ** 6) - li(2) - len(P)) / len(P))

print('--- faded sums')
for N in (10, 100, 1000):
    h = mpf(1) / N
    print('fade scale', N, ' faded 1+2+3', exp(-h) / (1 - exp(-h)) ** 2, ' smooth part', N * N,
          ' faded 1+1+1', 1 / (exp(h) - 1), ' smooth part', N)
for n in (1, 5, 10, 20, 50, 100):
    print('n', n, ' dimmer', exp(-mpf(n) / 10), ' dimmed term', n * exp(-mpf(n) / 10))
print('chopped at 10 and 100', 55, 5050)
print('1/(e-1)', 1 / (e - 1), ' 1 - 1/2 + 1/12 - 1/720', 1 - mpf(1) / 2 + mpf(1) / 12 - mpf(1) / 720)
print('zeta(2)', zeta(2), ' -zeta(2)/(2 pi^2)', -zeta(2) / (2 * pi ** 2), ' -1/12', -mpf(1) / 12,
      ' zeta(-1)', zeta(-1), ' zeta(0)', zeta(0))
