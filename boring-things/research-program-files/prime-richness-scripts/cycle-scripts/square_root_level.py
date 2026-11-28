# Checks behind sqrt-level-questions.md in the prime-richness folder.
import numpy as np
from mpmath import mp,zeta,log,mpf
mp.dps=30
mu=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,0,1,1,-1,0,0,1,0,0,-1,-1,-1,0,1,1,1,0,-1,1,1,0]
print('sum of 1 over p squared by the zeta formula:',sum(mpf(mu[k])/k*log(zeta(2*k)) for k in range(1,41)))
N=10**7
s=np.ones(N+1,dtype=bool);s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0].astype(float);L=np.log(P);R=1/np.sqrt(P)
c=np.cumsum(1/P**2)
for k in (10,100,10000,len(P)): print('first',k,'primes: sum of 1 over p squared = %.10f'%c[k-1])
tot=0.4522474200410655
print('share of the sum from 2 3 5 7:',[round(100/(p*p)/tot,1) for p in (2,3,5,7)])
for X in (10**3,10**5,10**7):
    m=P<=X
    print('primes up to',X,': sum 1/p^2 = %.4f, sum 1/p = %.4f, sum 1/sqrt(p) = %.1f'%(np.sum(1/P[m]**2),np.sum(1/P[m]),np.sum(R[m])))
m=P<=10**5
zeros=[14.134725,21.022040,25.010858,30.424876]
print('sum of cos(t ln p)/sqrt(p) for primes up to 100000 at the first four zeros:',[round(float(np.sum(R[m]*np.cos(t*L[m]))),2) for t in zeros])
ts=np.linspace(10,40,601);vals=np.array([np.sum(R[m]*np.cos(t*L[m])) for t in ts])
print('over heights 10 to 40: mean %.2f, lowest %.2f at height %.2f'%(vals.mean(),vals.min(),ts[vals.argmin()]))
for n in (60,61,62,63): print(n,'squared =',n*n,'| added over the square before:',2*n-1,'| percent more steps than the square before: %.2f'%(100*(2*n-1)/((n-1)**2)))
