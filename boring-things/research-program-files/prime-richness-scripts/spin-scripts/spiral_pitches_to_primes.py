# Spins the pitches to find the primes (Test 2 on the page spin-questions.md).
# The first block is the first try at Test 1 with no fade. That try gave false dips every 0.455 and is kept here to show the failure.
# Needs numpy and mpmath.
import numpy as np, math
from mpmath import zetazero
N=10**6
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,1001):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0].astype(np.float64)
lp=np.log(P); w=lp/np.sqrt(P)
# Test 1: spin the primes. arrow for prime p: length ln p / sqrt p, angle t ln p. look at the left-right part.
ts=np.arange(10,52,0.01)
vals=np.array([np.sum(w*np.cos(t*lp)) for t in ts])
# local minima (deep dips)
dips=[(vals[i],ts[i]) for i in range(1,len(ts)-1) if vals[i]<vals[i-1] and vals[i]<vals[i+1]]
dips.sort()
print('TEST 1 deepest dips (value, pitch):')
for v,t in sorted(dips[:12],key=lambda z:z[1]): print(round(t,2), round(v,1))
print('typical size of the curve away from dips: median', np.median(vals), 'min', vals.min())
Z=[float(zetazero(k).imag) for k in range(1,101)]
print('true pitches', [round(z,2) for z in Z[:12]])
# Test 2: spin the pitches. f(x) = - sum cos(gamma ln x)
G=np.array(Z)
xs=np.arange(1.5,60.05,0.05)
f=np.array([-np.sum(np.cos(G*math.log(x))) for x in xs])
peaks=[(f[i],xs[i]) for i in range(1,len(xs)-1) if f[i]>f[i-1] and f[i]>f[i+1]]
peaks.sort(reverse=True)
print('TEST 2 highest peaks (place, height):')
for v,x in sorted(peaks[:24],key=lambda z:z[1]): print(round(x,2), round(v,1))
print('value at whole numbers 2..30:', [(n, round(float(-np.sum(np.cos(G*math.log(n)))),1)) for n in range(2,31)])
