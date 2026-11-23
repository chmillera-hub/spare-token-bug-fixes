# Rechecks the smaller figures on the page spin-questions.md in the prime-richness folder.
# Run with: python3 spin_basics_check.py   (needs the free Python package mpmath)
import cmath, math
from collections import Counter
from mpmath import mp, mpf, pi, exp, sin, nsum, inf, radians, zeta, mpc

mp.dps = 25
print('--- arrows turned by squares')
for N in (5, 7, 11, 13, 17):
    s = sum(cmath.exp(2j * math.pi * n * n / N) for n in range(N))
    print('N', N, ' total', round(s.real, 4), round(s.imag, 4), ' length', abs(s), ' root', math.sqrt(N))
x = math.sqrt(2)
s = 0
for n in range(1, 10 ** 6 + 1):
    s += cmath.exp(2j * math.pi * n * n * x)
    if n in (100, 10 ** 4, 10 ** 6):
        print('root 2 of a turn: arrows', n, ' distance', abs(s), ' root', math.sqrt(n))
glow = lambda t: sum(math.exp(-math.pi * n * n * t) for n in range(-60, 61))
for t in (4, 0.25, 9, 1 / 9, 2, 0.5):
    print('glow at strength', t, glow(t))
print('one sided reciprocal sum', (glow(1) - 1) / 2, ' terms', math.exp(-math.pi), math.exp(-4 * math.pi), math.exp(-9 * math.pi))

print('--- spinning tames a sum')
s = 0
print('quarter turns', [(round((s := s + 1j ** n).real), round(s.imag)) for n in range(8)])
print('radius for a 10 degree turn', 1 / (2 * math.sin(math.radians(5))))
z = complex(zeta(mpc(1, 10)))
s = 0
for n in range(1, 100001):
    s += n ** (-1 - 10j)
    if n in (10, 100, 1000, 10 ** 4, 10 ** 5):
        print('dial 1 pitch 10 after', n, 'terms: distance from the center', abs(s - z))
print('center length', abs(z))
for h in (0.1, 0.01, 0.001):
    print('faded 1 - 2 + 3 - 4 with fade', h, math.exp(-h) / (1 + math.exp(-h)) ** 2)

print('--- the -1/12 from e and pi')
print('sum of n / e^(n pi)', nsum(lambda n: n * exp(-n * pi), [1, inf]))
run = mpf(0)
for p in (1 / pi ** 2, -mpf(1) / 12, pi ** 2 / 240, -pi ** 4 / 6048, pi ** 6 / 172800):
    run += p
    print('piece', p, ' running', run)
print('sum of n / (e^(2 pi n) - 1)', nsum(lambda n: n / (exp(2 * pi * n) - 1), [1, inf]), ' 1/24 - 1/(8 pi)', mpf(1) / 24 - 1 / (8 * pi))
for deg in (10, 5, 1):
    th = radians(deg)
    c = -1 / (4 * sin(th / 2) ** 2)
    print('turn of', deg, 'degrees: center', c, ' blow-up part', -1 / th ** 2, ' leftover', c + 1 / th ** 2)

print('--- one arrow turned by 1 then 1/2 then 1/3 of a turn')
h, nxt, laps, dirs = 0.0, 2, [], []
tenths = Counter()
for n in range(1, 100001):
    h += 1 / n
    if n <= 11:
        dirs.append((n, round((h % 1) * 360, 1)))
    if h >= nxt:
        laps.append(n)
        nxt += 1
    if 9 <= h < 10:
        tenths[int((h - 9) * 10)] += 1
print(dirs)
print('laps finish at', laps, ' ratios', [round(b / a, 3) for a, b in zip(laps, laps[1:])])
print('steps in each tenth of one lap', [tenths[i] for i in range(10)], tenths[9] / tenths[0], math.exp(0.9), ' head start in degrees', 0.5772156649 * 360)
s = 0
for n in range(1, 10 ** 6 + 1):
    s += cmath.exp(2j * math.pi / n) / n
print('arrows of length 1/n tilted one n-th of a turn: left-right minus ln', s.real - math.log(10 ** 6), ' up-down', s.imag)

print('--- moves of 1 then 2 then 3 units')
T = lambda n: n * (n + 1) // 2
print('half turns', [T(n) % 2 for n in range(1, 9)])
for N in (4, 5, 7, 8, 9, 10, 16, 32):
    seq = [T(n) % N for n in range(1, 2 * N + 1)]
    print('stops', N, ' reached', len(set(seq)), sorted(set(seq)) if N < 12 else '', seq[:16] if N in (4, 5, 8) else '')
g = (3 - math.sqrt(5)) / 2
print('golden angle', g * 360, [round((T(n) * g % 1) * 360, 1) for n in range(1, 13)])
print('plain number as the angle', [round((T(n) / (2 * math.pi) % 1) * 360, 1) for n in range(1, 13)])
for name, a in (('golden', g), ('plain number', 1 / (2 * math.pi)), ('root 2', math.sqrt(2) % 1)):
    c = [0] * 10
    for n in range(1, 10001):
        c[int((T(n) * a % 1) * 10)] += 1
    print(name, c)

print('--- 360 marks with moves of 1 then 2 then 3 degrees')
seq = [T(n) % 360 for n in range(1, 721)]
print(seq[:27], ' marks', len(set(seq)), ' returns to 0', [n for n in range(1, 721) if T(n) % 360 == 0])
print('mirror', seq[:718] == seq[:718][::-1], ' cycle 720', all(T(n) % 360 == T(n + 720) % 360 for n in range(1, 2000)))
print('laps finish at', [next(n for n in range(1, 2000) if T(n) >= 360 * k) for k in range(1, 8)])
print('visits', sorted(Counter(Counter(seq).values()).items()), ' remainders reached for 8 and 9 and 5',
      len({v % 8 for v in seq}), sorted({v % 9 for v in seq}), sorted({v % 5 for v in seq}))
S = lambda n: n * (n + 1) * (2 * n + 1) // 6
print('square moves cycle 2160', all(S(n) % 360 == S(n + 2160) % 360 for n in range(1, 5000)), ' marks', len({S(n) % 360 for n in range(1, 2161)}))
print('fractions: 1/n degrees after ten million steps', sum(1 / n for n in range(1, 10 ** 7 + 1)), ' steps for a lap: 10 to the power', (360 - 0.5772) / math.log(10))
print('360/n^2 rests at', (360 * math.pi ** 2 / 6) % 360)
