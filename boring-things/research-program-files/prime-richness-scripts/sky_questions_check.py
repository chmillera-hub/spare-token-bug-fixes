# Rechecks the figures on the page sky-questions.md in the prime-richness folder.
# Run with: python3 sky_questions_check.py   (needs the free Python packages numpy and mpmath)
# Two values on the page are known values that this program does not recompute:
# the sum of 1 over each twin prime (about 1.9) and the sum of 1 over each whole number with no digit 9 (about 22.9).
import math
import numpy as np
from mpmath import zeta, mpf

print('--- doublings pulled in to the whole numbers')
print('1 over the distance: doublings', sum(0.5 ** k for k in range(1, 60)), ' inverse square: doublings', sum(0.25 ** k for k in range(1, 60)),
      ' inverse square whole numbers', float(zeta(2)))
for a in ('2', '1.5', '1.1', '1.01'):
    print('1 over the distance with lamps at n to the power', a, float(zeta(mpf(a))))

print('--- the pull to the square roots under the inverse square rule')
for lo in (1, 2, 3, 10):
    ns = [n for n in range(1, 200) if lo <= math.sqrt(n) < lo + 1]
    print('stretch', lo, 'to', lo + 1, ' lamps', len(ns), ' first and last numbers', ns[0], ns[-1],
          ' light after the pull', sum(1 / n for n in ns), ' light before', 1 / lo ** 2, ' 2/d', 2 / (lo + 0.5))
h = 0.0
for n in range(1, 10 ** 6 + 1):
    h += 1 / n
    if n in (100, 10 ** 4, 10 ** 6):
        print('lamps out to a distance of', math.isqrt(n), ' total', h)
print('out to a distance of one million', math.log(10 ** 12) + 0.5772156649, ' gain for each tenfold step', 2 * math.log(10))
print('halving every distance', 4 * float(zeta(2)))
for a in ('1', '0.9', '0.75', '0.6', '0.55', '0.505', '0.5005'):
    print('power', a, ' total', float(zeta(2 * mpf(a))))

print('--- line and sheet and space')
print('ring of a sheet: lamps per unit of distance', 2 * math.pi, ' shell of space', 4 * math.pi)
tot = 0.0
R = 300
for x in range(-R, R + 1):
    for y in range(-R, R + 1):
        d2 = x * x + y * y
        if 0 < d2 <= R * R:
            tot += 1 / d2
    if x in (-R + 0,):
        pass
print('lamps on a square grid of a sheet out to a distance of 300', tot, ' 2 pi ln 300', 2 * math.pi * math.log(300))

print('--- lamps dropped at random along a line (one lamp per unit on average and 20000 layouts)')
rng = np.random.default_rng(1)
gaps = rng.exponential(1.0, size=(20000, 2000))
pos = np.cumsum(gaps, axis=1)
totals = (1 / pos ** 2).sum(axis=1)
print('median', np.median(totals), ' ninth tenth', np.quantile(totals, 0.9), ' largest', totals.max(), ' average', totals.mean(),
      ' share of the grand total held by the 20 brightest layouts', np.sort(totals)[-20:].sum() / totals.sum())
print('far lamps beyond a distance of 2000 would add about', 1 / 2000)

print('--- groups kept from 1 + 1/2 + 1/3 + ...')
print('first million terms', h, ' squares', float(zeta(2)), ' doublings', 1.0)
print('--- roots that mark the boundary')
for n in (4, 9, 100):
    print('number', n, ' distance', math.sqrt(n), ' brightness', 1 / math.sqrt(n) ** 2)
