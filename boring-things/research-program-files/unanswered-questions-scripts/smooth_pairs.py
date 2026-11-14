# Finds all pairs (A, B) with A - B = 1 or 2 where A and B are built only from primes in a given set.
# Method 1: brute force over every such number up to 10^60.
# Method 2: the Pell equation method of Stormer and Lehmer, which gives a complete list (per their theorems).
import sys
from math import isqrt
from itertools import combinations

def smooth_numbers(primes, bound):
    nums = [1]
    for p in primes:
        new = []
        for n in nums:
            while n <= bound:
                new.append(n); n *= p
        nums = new
    return sorted(nums)

def brute(primes, bound):
    nums = smooth_numbers(primes, bound); s = set(nums)
    return sorted((n + d, n) for n in nums for d in (1, 2) if n + d in s)

def is_smooth(n, primes):
    for p in primes:
        while n % p == 0: n //= p
    return n == 1

def pell_fundamental(D):
    a0 = isqrt(D); m, d, a = 0, 1, a0
    h1, h0, k1, k0 = a0, 1, 1, 0
    while h1 * h1 - D * k1 * k1 != 1:
        m = d * a - m; d = (D - m * m) // d; a = (a0 + m) // d
        h1, h0 = a * h1 + h0, h1; k1, k0 = a * k1 + k0, k1
    return h1, k1

def pell(primes):
    count = max(3, (max(primes) + 1) // 2)
    found = set()
    squarefree = [1]
    for r in range(1, len(primes) + 1):
        for c in combinations(primes, r):
            q = 1
            for p in c: q *= p
            squarefree.append(q)
    for q in squarefree:
        for D, kind in ((2 * q, 1), (q, 2)):
            if isqrt(D) ** 2 == D: continue
            x1, y1 = pell_fundamental(D); x, y = x1, y1
            for _ in range(count):
                if kind == 1 and x % 2 == 1:
                    a, b = (x + 1) // 2, (x - 1) // 2
                    if is_smooth(a, primes) and is_smooth(b, primes): found.add((a, b))
                if kind == 2:
                    a, b = x + 1, x - 1
                    if is_smooth(a, primes) and is_smooth(b, primes): found.add((a, b))
                x, y = x1 * x + D * y1 * y, x1 * y + y1 * x
    # every even pair with difference 2 is a doubled pair with difference 1
    found |= {(2 * a, 2 * b) for a, b in found if a - b == 1 and 2 in primes}
    return sorted(found)

expected = {
    (2, 31): [(2, 1), (4, 2), (32, 31), (64, 62)],
    (2, 3, 11): [(2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (6, 4), (8, 6), (9, 8), (11, 9), (12, 11), (18, 16), (24, 22), (33, 32), (66, 64), (243, 242), (486, 484)],
}
for primes, want in expected.items():
    b = brute(list(primes), 10 ** 60); p = pell(list(primes))
    print("primes", primes)
    print("  brute force up to 10^60:", b)
    print("  Pell method:            ", p)
    print("  brute force equals list in the question:", b == sorted(want), "| Pell method equals list in the question:", p == sorted(want))
extra = (2, 3, 5, 7)
b = brute(list(extra), 10 ** 60); p = pell(list(extra))
print("extra test primes", extra, "| brute force equals Pell method:", b == p, "| number of pairs:", len(b), "| largest pair:", b[-1])
