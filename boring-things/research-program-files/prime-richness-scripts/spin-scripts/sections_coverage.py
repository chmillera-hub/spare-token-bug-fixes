# For each number of sections from 2 to 5000: how many sections each kind of move ever reaches. Needs numpy. Takes a few minutes.
import numpy as np, math
MAXN=5000
def report(name, cov):
    full=[N for N in range(2,MAXN+1) if cov[N]==N]
    best=sorted(((cov[N]/N,N) for N in range(1000,MAXN+1)),reverse=True)[:5]
    print(name,'| full coverage count',len(full),'| first',full[:14],'| largest',full[-6:] if full else None)
    print('    best share for 1000 or more sections:',[(N,round(100*s,2)) for s,N in best], '| 360:',cov[360],'| 1000:',cov[1000])
def poly_cov(fn, mult):
    cov={}
    for N in range(2,MAXN+1):
        n=np.arange(0,mult*N+1,dtype=np.int64)
        cov[N]=np.unique(fn(n)%N).size
    return cov
report('counting numbers', poly_cov(lambda n:n*(n+1)//2,2))
report('odd numbers', poly_cov(lambda n:n*n,1))
report('squares', poly_cov(lambda n:n*(n+1)*(2*n+1)//6,6))
def cubes(n):
    t=n*(n+1)//2
    return t  # squared below with care
cov={}
for N in range(2,MAXN+1):
    n=np.arange(0,2*N+1,dtype=np.int64); t=(n*(n+1)//2)%N
    cov[N]=np.unique((t*t)%N).size
report('cubes',cov)
cov={}
for N in range(2,MAXN+1):
    a,b=1%N,1%N; pos=0; seen=set(); start=(a,b); k=0
    while True:
        pos=(pos+a)%N; seen.add(pos); a,b=b,(a+b)%N; k+=1
        if (a,b)==start: break
    cov[N]=len(seen)
report('fibonacci',cov)
cov={}
for N in range(2,MAXN+1):
    x=1%N; pos=0; seen=set(); states=set()
    while (x,pos) not in states:
        states.add((x,pos)); pos=(pos+x)%N; seen.add(pos); x=(2*x)%N
    cov[N]=len(seen)
report('doublings',cov)
s=np.ones(3000001,dtype=bool); s[:2]=False
for i in range(2,1733):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0][:200000].astype(np.int64); cs=np.cumsum(P)
cov={}
for N in range(2,MAXN+1): cov[N]=np.unique(cs%N).size
report('primes (first 200000)',cov)
print('primes: smallest share', min((cov[N]/N,N) for N in range(2,MAXN+1)))
