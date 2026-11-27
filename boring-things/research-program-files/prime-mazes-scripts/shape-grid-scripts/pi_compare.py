# Digits of pi (3 1 4 1 5 9 ...) on the square door grid and the hexagon door grid at the same sizes with the three part score.
# Run with: python3 pi_compare.py   (needs the free Python package mpmath)
import sys, json
sys.setrecursionlimit(100000)
from mpmath import mp
from hex_compare import build, score
mp.dps = 3700
digs = [int(c) for c in mp.nstr(mp.pi, 3650).replace('.', '')[:3600]]
out = {}
print('size | squares: score of max (percent) = largest + walk + door | hexagons: score of max (percent) = largest + walk + door')
for k in (12, 16, 20, 24, 30, 36, 40, 48, 60):
    row = []
    for hexa in (False, True):
        s = score(build(digs, k, hexa), k); row.append(s)
    mx = 2 * k * k + 4 * k; out[k] = row
    print('%2d by %2d | %4d of %4d (%4.1f%%) = %3d + %3d + %2d, regions %3d | %4d of %4d (%4.1f%%) = %3d + %3d + %2d, regions %3d' % (
        k, k, row[0]['three'], mx, 100 * row[0]['three'] / mx, row[0]['big'], row[0]['walk'], row[0]['door'], row[0]['regions'],
        row[1]['three'], mx, 100 * row[1]['three'] / mx, row[1]['big'], row[1]['walk'], row[1]['door'], row[1]['regions']))
json.dump({str(k): [[r['big'], r['walk'], r['door']] for r in v] for k, v in out.items()}, open('pi_ref.json', 'w'))
from collections import Counter
for name, mod in (('square doors', 4), ('hexagon doors', 6)):
    c = Counter(d % mod for d in digs); print(name, 'share of the first 3600 digits opening each door:', [round(100 * c[i] / 3600, 1) for i in range(mod)])
