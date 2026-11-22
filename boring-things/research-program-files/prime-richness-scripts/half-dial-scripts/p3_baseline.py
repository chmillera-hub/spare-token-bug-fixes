# One speaker plus its own mirror image: silent where theta(t) = (n - 3/2) pi.  Then add prime turns.
import mpmath, json
from mpmath import mp, mpf, mpc, pi
mp.dps = 25
theta = mpmath.siegeltheta
true = [mpmath.im(mpmath.zetazero(n)) for n in range(1, 13)]
base = []
for n in range(1, 13):
    g = (true[n-1])
    r = mpmath.findroot(lambda t: theta(t) - (n-mpf(3)/2)*pi, g)
    base.append(r)
print('n   true      one speaker + mirror   miss')
for n in range(12):
    print(n+1, mpmath.nstr(true[n], 7), mpmath.nstr(base[n], 7), mpmath.nstr(base[n]-true[n], 3))
import sympy
def argP(t, X):
    tot = mpf(0)
    for p in sympy.primerange(2, X+1):
        tot -= mpmath.arg(1 - mpf(p)**(-mpc(0.5, t)))
    return tot
res = {'true': [float(x) for x in true], 'base': [float(x) for x in base]}
for X in [2, 3, 5, 7, 11, 13, 19, 31]:
    # all solutions of theta + argP = (n-3/2) pi in [10, 60]
    f = lambda t: theta(t) + argP(t, X)
    import numpy as np
    ts = np.arange(10, 58, 0.01)
    vals = [float(f(mpf(x))) for x in ts]
    sols = []
    for n in range(1, 13):
        target = float((n-1.5)*pi)
        for i in range(len(ts)-1):
            if (vals[i]-target)*(vals[i+1]-target) <= 0:
                r = mpmath.findroot(lambda t: f(t) - target, (ts[i], ts[i+1]), solver='anderson')
                sols.append((n, float(r)))
    res['X%d' % X] = sols
    print('primes up to', X, [round(s[1], 2) for s in sols])
json.dump(res, open('p3.json', 'w'))
# size of the mirror stretch off the half dial
def chi(s):
    return 2**s*pi**(s-1)*mpmath.sin(pi*s/2)*mpmath.gamma(1-s)
for sg in [0.5, 0.6, 0.7, 0.8]:
    print('dial', sg, 'length of mirror factor at pitch 14.52 and 100 and 1000:',
          [mpmath.nstr(abs(chi(mpc(sg, t))), 5) for t in [14.52, 100, 1000]])
