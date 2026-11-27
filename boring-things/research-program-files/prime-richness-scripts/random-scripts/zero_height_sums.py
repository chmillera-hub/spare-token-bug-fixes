# Sums over the heights of the zeta zeros on the critical line (the heights are 14.13 and 21.02 and 25.01 and onward).
# The zeros are found as sign changes of the standard real-valued zeta formula on the critical line (main sum plus the first correction term).
# Run with: python3 zero_height_sums.py   (needs the free Python package numpy)
import math
import numpy as np

TMAX = 5000.0


def theta(t):
    return t / 2 * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def Z(t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    a = np.sqrt(t / (2 * np.pi)); n = np.floor(a); p = a - n
    th = theta(t); out = np.zeros_like(t)
    for k in range(1, int(n.max()) + 1):
        m = n >= k
        out[m] += np.cos(th[m] - t[m] * math.log(k)) / math.sqrt(k)
    out *= 2
    c0 = np.cos(2 * np.pi * (p * p - p - 1 / 16)) / np.cos(2 * np.pi * p)
    return out + (-1) ** (n.astype(int) - 1) * (t / (2 * np.pi)) ** -0.25 * c0


grid = np.arange(10.0, TMAX, 0.005)
z = Z(grid)
idx = np.flatnonzero(np.sign(z[:-1]) * np.sign(z[1:]) < 0)
lo = grid[idx].copy(); hi = grid[idx + 1].copy(); flo = z[idx].copy()
for _ in range(40):
    mid = (lo + hi) / 2; fm = Z(mid)
    left = np.sign(fm) == np.sign(flo)
    lo = np.where(left, mid, lo); flo = np.where(left, fm, flo); hi = np.where(left, hi, mid)
g = (lo + hi) / 2
T = TMAX
expect = T / (2 * math.pi) * math.log(T / (2 * math.pi * math.e)) + 7 / 8
print('zeros found below height', T, ':', len(g), ' the counting formula predicts about', round(expect, 1))
print('first heights', [round(float(x), 4) for x in g[:8]])
s1 = np.cumsum(1 / g); s2 = np.cumsum(1 / g ** 2); s3 = np.cumsum(1 / (0.25 + g ** 2))
for n in (1, 10, 100, 1000, 2000, len(g)):
    Tn = float(g[n - 1]); sm = math.log(Tn / (2 * math.pi)) ** 2 / (4 * math.pi)
    print('first %4d zeros (up to height %8.2f): sum of 1/height = %.5f | (ln(height/2pi))^2/(4pi) = %.5f | difference %.5f | sum of 1/height^2 = %.7f | sum of 1/(1/4 + height^2) = %.7f' % (n, Tn, s1[n - 1], sm, s1[n - 1] - sm, s2[n - 1], s3[n - 1]))
Tl = float(g[-1])
tail = (math.log(Tl / (2 * math.pi)) + 1) / (2 * math.pi * Tl)
print('estimated tail of the squared sums beyond the last zero found:', tail)
print('sum of 1/height^2 with the tail:', float(s2[-1]) + tail)
print('sum of 1/(1/4 + height^2) with the tail:', float(s3[-1]) + tail)
EUL = 0.5772156649015329
print('1 + 0.5772/2 - ln(4 pi)/2 =', 1 + EUL / 2 - math.log(4 * math.pi) / 2)
for target in (5, 10, 20):
    print('height needed for the sum of 1/height to reach %d (from the smooth formula with the measured offset): about 2pi x e^%.1f' % (target, math.sqrt(4 * math.pi * (target - (float(s1[-1]) - math.log(Tl / (2 * math.pi)) ** 2 / (4 * math.pi))))))
print('average spacing between zeros near height 20:', 2 * math.pi / math.log(20 / (2 * math.pi)), ' near height 5000:', 2 * math.pi / math.log(5000 / (2 * math.pi)))
