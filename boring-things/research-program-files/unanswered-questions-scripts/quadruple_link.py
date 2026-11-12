# Links the two parametrizations of the special Pythagorean quadruples and lists the whole-number solutions for N = 65
# (SageMath board question 85649)
import sympy as sp
from itertools import product
m, n = sp.symbols("m n")
d = 36*m**2 + 18*m + 4*n**2 + 2*n + 3
a = 24*m*n + 6*m + 6*n + 1
b = 2*(3*m + n + 1)*(6*m - 2*n + 1)
c = 2*(3*m + n + 1)
print("a^2 + b^2 + c^2 = d^2 for every m and n:", sp.expand(a**2 + b**2 + c**2 - d**2) == 0)
print("d + a = c^2 for every m and n:", sp.expand(d + a - c**2) == 0)
N = sp.symbols("N")
print("a = 3*(3N-3)/6 + 1 turns into N =", sp.factor(sp.solve(sp.Eq(3*(3*N - 3)/6 + 1, a), N)[0]))

def solutions_for(Nval, box=40):
    out = []
    for f in sp.divisors(Nval):
        for sign in (1, -1):
            p, q = sign * f, sign * (Nval // f)
            if (p - 1) % 4 == 0 and (q - 1) % 4 == 0:
                mv, nv = (p - 1) // 4, (q - 1) // 4
                vals = [int(e.subs({m: mv, n: nv})) for e in (a, b, c, d)]
                out.append((mv, nv, vals))
    return out

for mv, nv, (av, bv, cv, dv) in solutions_for(65):
    # u^2 + v^2 = (d + a)/2 and s^2 + t^2 = (d - a)/2, then b and c pick out the matching combinations
    found = []
    hi = int(((dv + av) // 2) ** 0.5) + 1; lo = int(((dv - av) // 2) ** 0.5) + 1
    for u, v in product(range(-hi, hi + 1), repeat=2):
        if u*u + v*v != (dv + av) // 2: continue
        for s, t in product(range(-lo, lo + 1), repeat=2):
            if s*s + t*t == (dv - av) // 2 and 2*(u*t + v*s) == bv and 2*(v*t - u*s) == cv:
                found.append((u, v, s, t))
    print(f"m = {mv}, n = {nv}: a = {av}, b = {bv}, c = {cv}, d = {dv} | checks: {av*av + bv*bv + cv*cv == dv*dv}, {dv + av == cv*cv} | whole-number (u, v, s, t): {len(found)} found, for example {found[:2]}")
