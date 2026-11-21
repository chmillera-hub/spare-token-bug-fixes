# Hunts for prime-rich running sums of the shape: start at c then add 2a + 4a + 6a and so on.
# The total after n steps is a*n*n + a*n + c. Needs numpy and gmpy2.
# Run: python3 sum_search.py 15     (the number is a)
import numpy as np, math, time, sys
from gmpy2 import mpz, is_prime
a=int(sys.argv[1]); CMAX=int(float(sys.argv[2])) if len(sys.argv)>2 else 2*10**11
t0=time.time()
def primes_upto(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
PR=primes_upto(100000)
def roots(c,q): return sum(1 for x in range(q) if (a*x*x+a*x+c)%q==0)
TOP=53
ok={q:np.array([roots(r,q)==0 for r in range(q)]) for q in PR if q<=TOP}
M=510510; res=np.arange(M); keep=np.ones(M,bool)
for q in (2,3,5,7,11,13,17): keep&=ok[q][res%q]
res=res[keep]
K=CMAX//M+1; ks=np.arange(K,dtype=np.int64)
SV=[q for q in PR if 17<q<=TOP]; kmod={q:(ks%q).astype(np.int16) for q in SV}
out=[]
for r in res:
    idx=None
    for q in SV:
        km=kmod[q] if idx is None else kmod[q][idx]
        good=ok[q][(int(r)%q+(M%q)*km)%q]
        idx=np.nonzero(good)[0] if idx is None else idx[good]
    if len(idx): out.append(int(r)+M*idx.astype(np.int64))
C=np.concatenate(out); C=C[(C>1)&(C<=CMAX)]
score=np.zeros(len(C))
for q in PR:
    if q<=TOP: continue
    if q>500: break
    tbl=np.array([math.log((1-roots(r,q)/q)/(1-1/q)) for r in range(q)])
    score+=tbl[C%q]
top=C[np.argsort(-score)[:30]]
def full(c):
    D=a*a-4*a*c; s=1.0
    for q in PR:
        if q==2: w=roots(c,2)
        elif a%q==0: w=q if c%q==0 else 0
        else:
            d=D%q; w=1 if d==0 else (2 if pow(d,(q-1)//2,q)==1 else 0)
        s*=(1-w/q)/(1-1/q)
    return s
cands=sorted(((full(int(c)),int(c)) for c in top),reverse=True)[:3]
print('a =',a,'survivors',len(C),'search time %.0fs'%(time.time()-t0),flush=True)
for s,c in cands:
    pr=0;ex=0.0
    for n in range(1,300001):
        v=a*n*n+a*n+c; ex+=1/math.log(v)
        if is_prime(mpz(v)): pr+=1
    small=next(q for q in PR if (q==2 and roots(c,2)) or (q>2 and (c%q==0 if a%q==0 else pow((a*a-4*a*c)%q,(q-1)//2,q)<=1)))
    print('RESULT a=%d c=%d predicted %+d%% measured %+d%% primes %d chance %.1f share %.1f%% smallest prime that can divide a total %d largest total %d'%(a,c,round((s-1)*100),round((pr/ex-1)*100),pr,ex,100*pr/300000,small,a*300000*300001+c),flush=True)
