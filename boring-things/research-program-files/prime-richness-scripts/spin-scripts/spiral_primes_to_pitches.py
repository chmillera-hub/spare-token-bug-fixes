# Spins the primes with a gentle fade to find the pitches (Test 1 on the page spin-questions.md). Needs numpy.
import numpy as np, math
N=10**6
s=np.ones(N+1,dtype=bool); s[:2]=False
for i in range(2,1001):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0].astype(np.float64)
lp=np.log(P); L=math.log(N)
w=lp/np.sqrt(P)*(1-lp/L)**2     # gentle fade so the far primes die away smoothly
ts=np.arange(8,52,0.01)
vals=np.array([np.sum(w*np.cos(t*lp)) for t in ts])
dips=[(vals[i],ts[i]) for i in range(1,len(ts)-1) if vals[i]<vals[i-1] and vals[i]<vals[i+1]]
dips.sort()
print('deepest dips (pitch, value):')
for v,t in sorted(dips[:10],key=lambda z:z[1]): print(round(t,2), round(v,2))
print('median', round(float(np.median(vals)),2), 'max', round(float(vals.max()),2))
true=[14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.01,49.77]
for z in true:
    i=int(round((z-8)/0.01)); print('value at true pitch', z, round(float(vals[i]),2))
for t in (10,12,17,19,23,28,35,46): 
    i=int(round((t-8)/0.01)); print('value away from a pitch', t, round(float(vals[i]),2))
