# Counts orbits of the symmetric group S_n on k-element collections of vertex pairs with the counting lemma of Burnside
# (SageMath board question 83156) and checks the counts against brute force and against known graph counts
from itertools import combinations, combinations_with_replacement, permutations
from math import factorial
from sympy.utilities.iterables import partitions
from sympy import symbols, Poly, prod, Rational

x = symbols("x")

def cycle_lengths_on_pairs(perm, pairs):
    index = {pr: i for i, pr in enumerate(pairs)}
    seen, out = set(), []
    for pr in pairs:
        if pr in seen: continue
        length, cur = 0, pr
        while cur not in seen:
            seen.add(cur); length += 1
            cur = tuple(sorted(perm[v] for v in cur))
        out.append(length)
    return out

def perm_of_type(part, n):
    perm, start = list(range(n)), 0
    for length, mult in part.items():
        for _ in range(mult):
            for i in range(length): perm[start + i] = start + (i + 1) % length
            start += length
    return perm

def class_size(part, n):
    denom = 1
    for length, mult in part.items(): denom *= length**mult * factorial(mult)
    return factorial(n) // denom

def orbit_counts(n, kmax, loops, repeats):
    # loops: pairs {v, v} allowed.  repeats: the same pair may be chosen several times (a multiset of pairs).
    pairs = list(combinations_with_replacement(range(n), 2)) if loops else list(combinations(range(n), 2))
    total = [Rational(0)] * (kmax + 1)
    for part in partitions(n):
        lens = cycle_lengths_on_pairs(perm_of_type(part, n), pairs)
        series = [1] + [0] * kmax                      # generating function of collections fixed by this permutation
        for L in lens:
            new = series[:]
            if repeats:                                   # factor 1/(1 - x^L)
                for k in range(L, kmax + 1): new[k] += new[k - L]
            else:                                         # factor (1 + x^L)
                for k in range(kmax, L - 1, -1): new[k] = series[k] + series[k - L]
            series = new
        size = class_size(part, n)
        total = [t + size * s for t, s in zip(total, series)]
    return [int(t / factorial(n)) for t in total]

def brute(n, kmax, loops, repeats):
    pairs = list(combinations_with_replacement(range(n), 2)) if loops else list(combinations(range(n), 2))
    choose = combinations_with_replacement if repeats else combinations
    out = []
    for k in range(kmax + 1):
        seen = set()
        for coll in choose(pairs, k):
            canon = min(tuple(sorted(tuple(sorted(pm[v] for v in pr)) for pr in coll)) for pm in permutations(range(n)))
            seen.add(canon)
        out.append(len(seen))
    return out

for n in (3, 4):
    for loops, repeats, name in ((False, False, "simple graphs"), (True, True, "multisets of pairs with loops")):
        kmax = n * (n - 1) // 2 if not repeats else 4
        f, b = orbit_counts(n, kmax, loops, repeats), brute(n, kmax, loops, repeats)
        print(f"n = {n}, {name}: formula {f} | brute force {b} | equal: {f == b}")
for n, known in ((4, 11), (5, 34), (6, 156), (7, 1044)):
    seq = orbit_counts(n, n * (n - 1) // 2, False, False)
    print(f"n = {n}: graphs by number of edges {seq} | total {sum(seq)} (known count {known}) | symmetric: {seq == seq[::-1]}")
print("n = 5, multisets of pairs with loops, k = 0..6:", orbit_counts(5, 6, True, True))
