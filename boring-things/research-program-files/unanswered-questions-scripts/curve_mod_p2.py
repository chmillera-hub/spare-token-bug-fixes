# Computes q*P on an elliptic curve over the whole numbers modulo p^2 with division-free formulas (SageMath board question 83276)
import sys, time
from math import gcd
p = 115792089237316195423570985008687907853269984665640564039457584007913129639747
a, b = -3, 2697448053935541741976221051345108825177671050689533270507
N = p * p

def add(P, Q, n):
    # complete projective addition for y^2 = x^3 + a*x + b (formulas of Renes, Costello and Batina): no division anywhere
    X1, Y1, Z1 = P; X2, Y2, Z2 = Q; b3 = 3 * b % n
    t0 = X1*X2 % n; t1 = Y1*Y2 % n; t2 = Z1*Z2 % n
    t3 = (X1+Y1)*(X2+Y2) % n; t4 = (t0+t1) % n; t3 = (t3-t4) % n
    t4 = (X1+Z1)*(X2+Z2) % n; t5 = (t0+t2) % n; t4 = (t4-t5) % n
    t5 = (Y1+Z1)*(Y2+Z2) % n; X3 = (t1+t2) % n; t5 = (t5-X3) % n
    Z3 = a*t4 % n; X3 = b3*t2 % n; Z3 = (X3+Z3) % n
    X3 = (t1-Z3) % n; Z3 = (t1+Z3) % n; Y3 = X3*Z3 % n
    t1 = (t0+t0) % n; t1 = (t1+t0) % n; t2 = a*t2 % n
    t4 = b3*t4 % n; t1 = (t1+t2) % n; t2 = (t0-t2) % n
    t2 = a*t2 % n; t4 = (t4+t2) % n; t0 = t1*t4 % n
    Y3 = (Y3+t0) % n; t0 = t5*t4 % n; X3 = t3*X3 % n
    X3 = (X3-t0) % n; t0 = t3*t1 % n; Z3 = t5*Z3 % n
    Z3 = (Z3+t0) % n
    return (X3, Y3, Z3)

def mul(k, P, n):
    R = (0, 1, 0)                         # the neutral point
    for bit in bin(k)[2:]:
        R = add(R, R, n)
        if bit == "1": R = add(R, P, n)
    return R

def on_curve(P, n):
    X, Y, Z = P; return (Y*Y*Z - X**3 - a*X*Z*Z - b*Z**3) % n == 0

def lift_x(c):
    # a point with x = c modulo p^2: square root modulo p (p = 3 mod 4), then one Hensel step up to p^2
    rhs = (c**3 + a*c + b)
    y = pow(rhs % p, (p + 1) // 4, p)
    assert y*y % p == rhs % p, "no point with this x"
    y = (y - (y*y - rhs) * pow(2*y, -1, p)) % N
    return (c % N, y, 1)

if __name__ == "__main__":
    print("Python", sys.version.split()[0], "| p mod 4 =", p % 4)
    from cypari import pari
    pari.allocatemem(2 * 10**9)
    t = time.time(); q = int(pari.ellcard(pari.ellinit([a, b], p))); print(f"number of points over the field with p elements (PARI ellcard, {time.time()-t:.0f} s): q = {q}")
    print("q differs from p:", q != p, "| q and p share no factor:", gcd(q, p) == 1)
    P = lift_x(12010)
    print("P lies on the curve modulo p^2:", on_curve(P, N))
    Q = mul(q, P, N)
    print("q*P lies on the curve modulo p^2:", on_curve(Q, N))
    print("q*P reduces to the neutral point modulo p (X and Z divisible by p):", Q[0] % p == 0 and Q[2] % p == 0 and Q[1] % p != 0)
    print("q*P is NOT the neutral point modulo p^2:", not (Q[0] % N == 0 and Q[2] % N == 0))
    R = mul(p, Q, N)
    print("p*(q*P) IS the neutral point modulo p^2 (X = 0 and Z = 0, Y a unit):", R[0] % N == 0 and R[2] % N == 0 and gcd(R[1], N) == 1)
    Yinv = pow(Q[1], -1, N)
    print("q*P scaled to Y = 1: X/Y =", Q[0] * Yinv % N // p, "times p | Z/Y =", Q[2] * Yinv % N // p, "times p")
