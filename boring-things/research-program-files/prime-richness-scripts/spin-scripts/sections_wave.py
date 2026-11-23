# How the share of sections reached rises and falls with the number of sections. Needs numpy.
import numpy as np, math
MAXN=5000
def odd_primes(n):
    c=0; 
    while n%2==0: n//=2
    p=3
    while p*p<=n:
        if n%p==0:
            c+=1
            while n%p==0: n//=p
        p+=2
    if n>1: c+=1
    return c
def cov_poly(fn,mult):
    return {N: np.unique(fn(np.arange(0,mult*N+1,dtype=np.int64))%N).size/N*100 for N in range(1,MAXN+1)}
c=cov_poly(lambda n:n*(n+1)//2,2)
print('counting moves, sections 1..30:',[round(c[N]) for N in range(1,31)])
for lo,hi in ((1,10),(11,100),(101,1000),(1001,5000)):
    print('average share', lo,hi, round(np.mean([c[N] for N in range(lo,hi+1)]),1))
for k in range(0,5):
    v=[c[N] for N in range(1,MAXN+1) if odd_primes(N)==k]; print('distinct odd prime pieces',k,'count',len(v),'average',round(np.mean(v),1),'range',round(min(v),1),round(max(v),1))
print('primes:',[(p,round(c[p],1)) for p in (3,5,7,11,13,101,997,4999)])
print('prime powers:',[(q,round(c[q],1)) for q in (9,27,81,25,125,49)])
print('doubling keeps the share:',[(N,round(c[N],1),round(c[2*N],1),round(c[4*N],1)) for N in (3,5,15,45,105,1155)])
lowest=sorted((c[N],N) for N in range(2,MAXN+1))[:5]; print('lowest',[(N,round(s,1)) for s,N in lowest])
s=cov_poly(lambda n:n*(n+1)*(2*n+1)//6,6)
print('square moves, sections 1..30:',[round(s[N]) for N in range(1,31)])
print('primes:',[(p,round(s[p],1)) for p in (5,7,11,13,17,19,23,101,997)])
for lo,hi in ((1,10),(11,100),(101,1000),(1001,5000)):
    print('average share', lo,hi, round(np.mean([s[N] for N in range(lo,hi+1)]),1))
print('lowest',[(N,round(v,1)) for v,N in sorted((s[N],N) for N in range(2,MAXN+1))[:4]])
