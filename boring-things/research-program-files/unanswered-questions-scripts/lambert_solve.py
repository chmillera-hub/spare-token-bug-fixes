# Solves a*log(r) + r = y for r with the Lambert W function and checks the answer (SageMath board question 85789)
import sympy as sp, mpmath as mp
a, r, y = sp.symbols("a r y", positive=True)
sol = sp.solve(sp.Eq(a * sp.log(r) + r, y), r)
print("sympy solution:", sol)
closed = a * sp.LambertW(sp.exp(y / a) / a)
print("matches a*LambertW(exp(y/a)/a):", sp.simplify(sol[0] - closed) == 0)
mp.mp.dps = 30
for av, yv in ((2, 5), (0.5, 3), (7, 1), (1, 0.1), (-2, -1), (-2, 3)):
    arg = mp.e ** (mp.mpf(yv) / av) / av
    branches = [0] if arg >= 0 else [0, -1]
    for k in branches:
        if arg < -1 / mp.e: print(f"a = {av}, y = {yv}: no real solution because the argument {mp.nstr(arg, 6)} is below -1/e"); break
        rv = av * mp.lambertw(arg, k)
        print(f"a = {av}, y = {yv}, branch {k}: r = {mp.nstr(rv.real, 15)} | a*log(r) + r - y = {mp.nstr(abs(av * mp.log(rv) + rv - yv), 3)}")
