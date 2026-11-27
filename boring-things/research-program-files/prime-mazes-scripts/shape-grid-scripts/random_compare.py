# Random digit sequences on the square door grid and the hexagon door grid at the same sizes.
# Each trial puts the same random digits on both grids and counts the three part score (largest region + longest walk + door points).
# A second test gives every door the same chance (a random door for each room) to separate the shape from the digit rule.
# Run with: python3 random_compare.py
import random, sys
sys.setrecursionlimit(100000)
from hex_compare import build, score, SQ, NBE, NBO

random.seed(11)


def trial(k, fair):
    n = k * k
    if fair:
        a = [random.randrange(4) for _ in range(n)]; b = [random.randrange(6) for _ in range(n)]
    else:
        a = b = [random.randrange(10) for _ in range(n)]
    return score(build(a, k, False), k), score(build(b, k, True), k)


for fair in (False, True):
    print('--- ' + ('every door has the same chance' if fair else 'random digits 0 to 9 with the digit rule'))
    for k, T in ((12, 1500), (16, 1000), (20, 600), (24, 400), (30, 250), (40, 120), (60, 40)):
        tot = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]; win = tie = 0; anydoor = [0, 0]; best = [0, 0]
        for _ in range(T):
            s, h = trial(k, fair)
            for i, x in enumerate((s, h)):
                tot[i][0] += x['three']; tot[i][1] += x['big']; tot[i][2] += x['walk']; tot[i][3] += x['door']; tot[i][4] += x['regions']
                anydoor[i] += x['door'] > 0; best[i] = max(best[i], x['three'])
            win += h['three'] > s['three']; tie += h['three'] == s['three']
        mx = 2 * k * k + 4 * k
        f = lambda v: v / T
        print('%2d by %2d (%4d trials): squares avg %6.1f (%4.1f%%) = %5.1f + %5.1f + %4.2f, regions %6.1f, best %3d | hexagons avg %6.1f (%4.1f%%) = %5.1f + %5.1f + %4.2f, regions %6.1f, best %3d | hexagons higher in %4.1f%% of trials, tied %3.1f%% | any door point: squares %4.1f%% hexagons %4.1f%%' % (
            k, k, T, f(tot[0][0]), 100 * f(tot[0][0]) / mx, f(tot[0][1]), f(tot[0][2]), f(tot[0][3]), f(tot[0][4]), best[0],
            f(tot[1][0]), 100 * f(tot[1][0]) / mx, f(tot[1][1]), f(tot[1][2]), f(tot[1][3]), f(tot[1][4]), best[1], 100 * win / T, 100 * tie / T, 100 * anydoor[0] / T, 100 * anydoor[1] / T))
