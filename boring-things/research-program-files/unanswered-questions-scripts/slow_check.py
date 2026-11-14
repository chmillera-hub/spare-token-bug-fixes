# Slow brute-force check of OEIS A394252 (run: python3 slow_check.py 17)
import numpy as np,sys
N=int(sys.argv[1])
a=[1]
for n in range(2,N+1):
    m=n-1
    B=[x-1 for x in a[1:]]
    L=3*a[-1]+5
    f=np.arange(L+1,dtype=np.int32)  # fewest coins to make y (coin 1 always exists once n>2)
    if not B: f=np.where(np.arange(L+1)==0,0,10**6).astype(np.int32)
    for c in B:
        if c==1: continue
        for s in range(c,L+1,c):
            e=min(s+c,L+1)
            np.minimum(f[s:e],f[s-c:e-c]+1,out=f[s:e])
    a.append(next(y+m for y in range(a[-1]+1-m,L+1-m) if f[y]>m))
    print(n,a[-1])
