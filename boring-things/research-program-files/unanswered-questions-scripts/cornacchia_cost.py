# Measures where the time goes in the algorithm of Cornacchia for x^2 + y^2 = N   (SageMath board question 85618)
import time, random, sympy
from math import isqrt
from sympy.ntheory import sqrt_mod, randprime
print("sympy", sympy.__version__)
random.seed(1)

def euclid_step(N, r):
    a, b = N, r
    while b * b > N:
        a, b = b, a % b
    y2 = N - b * b
    y = isqrt(y2)
    return (b, y) if y * y == y2 else None

def timed(f, *args):
    t = time.perf_counter(); out = f(*args); return out, time.perf_counter() - t

print("check with the example in the question: N = 725 ->", euclid_step(725, max(r for r in sqrt_mod(-1, 725, all_roots=True) if euclid_step(725, r))))
print("\nN prime (N = 1 mod 4):")
for bits in (64, 256, 1024, 2048):
    while True:
        p = randprime(2 ** (bits - 1), 2 ** bits)
        if p % 4 == 1: break
    r, t_root = timed(sqrt_mod, -1, p)
    sol, t_euclid = timed(euclid_step, p, r)
    print(f"  {bits} bits | square root of -1 mod N: {t_root * 1000:.3f} ms | Euclid step: {t_euclid * 1000:.3f} ms | x^2 + y^2 = N holds: {sol[0]**2 + sol[1]**2 == p}")
print("\nN = p*q with two primes of equal size (both 1 mod 4), factors not given to the program:")
for bits in (20, 26, 32, 36):
    ps = []
    while len(ps) < 2:
        p = randprime(2 ** (bits - 1), 2 ** bits)
        if p % 4 == 1 and p not in ps: ps.append(p)
    N = ps[0] * ps[1]
    r, t_root = timed(sqrt_mod, -1, N)
    sol, t_euclid = timed(euclid_step, N, r)
    print(f"  N has {N.bit_length()} bits | square root of -1 mod N: {t_root * 1000:.1f} ms | Euclid step: {t_euclid * 1000:.3f} ms")
# two different square roots of -1 mod N reveal the factors
p, q = 1000033, 1000037
N = p * q
roots = sqrt_mod(-1, N, all_roots=True)
r1 = roots[0]; r2 = next(r for r in roots if r not in (r1, N - r1))
from math import gcd
print("\ntwo unrelated square roots of -1 mod N give a factor through gcd(r1 - r2, N):", gcd(r1 - r2, N), "| true factors:", p, q)
