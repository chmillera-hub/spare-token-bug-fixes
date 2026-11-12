import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
a=[1,2,5,10,28,56,112,326,652,1304,2608,7712,15424,30848,61696,182480,364960,729920,1459840,2919680,8697344,17394688,34789376,69578752,139157504,414552832,829105664,1658211328,3316422656,6632845312]
X=2*a[-1]; m=30
coins=[x-1 for x in a[1:]]
@lru_cache(None)
def f(y,k,j):
    if y==0: return ()
    if j<=0: return None
    if k==1: return (1,)*y if y<=j else None
    c=coins[k-1]
    for t in range(min(j,y//c),-1,-1):
        if y-t*c>(j-t)*coins[k-2]: break
        r=f(y-t*c,k-1,j-t)
        if r is not None: return (c,)*t+r
    return None
r=f(X-m,len(coins),m)
terms=[c+1 for c in r]+[1]*(m-len(r))
print(sorted(terms,reverse=True)); print(len(terms),sum(terms),X,sum(terms)==X, all(t in a for t in terms))
