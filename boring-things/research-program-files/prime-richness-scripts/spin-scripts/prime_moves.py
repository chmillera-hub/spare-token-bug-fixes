# Moves equal to the primes: how many primes fill a circle and how evenly. Needs numpy.
import numpy as np, math
LIM=33*10**6
s=np.ones(LIM+1,dtype=bool); s[:2]=False
for i in range(2,int(LIM**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0][:2000000].astype(np.int64); cs=np.cumsum(P)
print('primes used',len(P),'largest',P[-1])
print('cover time (primes needed to hit every section) against N ln N:')
for N in (10,36,100,360,1000,2310,5000,10000,30030,50000,100000):
    u,idx=np.unique(cs%N,return_index=True)
    if u.size==N: print(N, int(idx.max())+1, round(N*math.log(N)), round((idx.max()+1)/(N*math.log(N)),2))
    else: print(N,'not all hit: reached',u.size)
print('evenness after 2 million primes (1.0 means as even as random dropping):')
for N in (2,3,4,5,6,7,8,9,10,12,30,36,100,210,360,1000,2310):
    c=np.bincount(cs%N,minlength=N); e=len(cs)/N
    chi=((c-e)**2/e).sum()/(N-1)
    print(N, round(chi,2), int(c.min()), int(c.max()), round(e))
print('N=2 pattern first 12:',list(cs[:12]%2),' N=3 counts',np.bincount(cs%3),' N=4 counts',np.bincount(cs%4),' N=6 counts',np.bincount(cs%6))
# step by step evenness for small N at early times
for N in (10,360):
    for k in (1000,10000,100000):
        c=np.bincount(cs[:k]%N,minlength=N); print('N',N,'after',k,'primes min max',int(c.min()),int(c.max()),'expected',round(k/N,1))
