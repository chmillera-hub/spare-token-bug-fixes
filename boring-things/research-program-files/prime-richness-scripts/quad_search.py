# Hunts for the equation n^2 + n + A (A under 900 billion) whose outputs contain the most primes.
# Step 1 keeps every A where no prime up to 47 can divide an output.
# Step 2 scores the survivors by which larger primes can divide an output.
# Step 3 counts primes for the best ones on every input from 1 to 300000.
# Needs numpy and gmpy2. Run: python3 quad_search.py
import numpy as np, math, time, sys
from gmpy2 import mpz, is_prime
t0=time.time()
def primes_upto(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
PR=primes_upto(200000)
def roots(A,q): return sum(1 for x in range(q) if (x*x+x+A)%q==0)
AMAX=9*10**11
WHEEL=[2,3,5,7,11,13,17]; M=510510
ok={q:np.array([roots(a,q)==0 for a in range(q)]) for q in PR if q<=47}
res=np.arange(M)
keep=np.ones(M,bool)
for q in WHEEL: keep&=ok[q][res%q]
res=res[keep]
K=AMAX//M+1
ks=np.arange(K,dtype=np.int64)
SIEVE=[q for q in PR if 17<q<=47]
kmod={q:(ks%q).astype(np.int16) for q in SIEVE}
out=[]
for r in res:
    idx=None
    for q in SIEVE:
        km=kmod[q] if idx is None else kmod[q][idx]
        good=ok[q][(int(r)%q+(M%q)*km)%q]
        idx=np.nonzero(good)[0] if idx is None else idx[good]
    out.append(int(r)+M*idx.astype(np.int64))
A=np.concatenate(out); A=A[(A>1)&(A<=AMAX)]
print('survivors with no prime up to 47 dividing any output:',len(A),'time %.0fs'%(time.time()-t0),flush=True)
score=np.zeros(len(A))
for q in PR:
    if q<=47: continue
    if q>600: break
    tbl=np.array([math.log((1-roots(a,q)/q)/(1-1/q)) for a in range(q)])
    score+=tbl[A%q]
top=A[np.argsort(-score)[:40]]
def full_score(a):
    D=1-4*a; s=1.0
    for q in PR:
        if q==2: w=0 if a%2 else 2
        else:
            d=D%q
            w=1 if d==0 else (2 if pow(d,(q-1)//2,q)==1 else 0)
        s*=(1-w/q)/(1-1/q)
    return s
cands=sorted(((full_score(int(a)),int(a)) for a in top),reverse=True)
print('time %.0fs'%(time.time()-t0)); 
for s,a in cands[:12]: print('A =',a,'predicted %+d%%'%round((s-1)*100))
def measure(a,N=300000):
    pr=0;ex=0.0
    for n in range(1,N+1):
        v=n*n+n+a; ex+=1/math.log(v)
        if is_prime(mpz(v)): pr+=1
    return pr,ex
for a in [41,27941,72491,247757]+[c[1] for c in cands[:4]]+[3399714628553118047]:
    pr,ex=measure(a)
    print('n^2 + n +',a,': predicted %+d%% | measured %+d%% (%d primes where chance predicts %.0f) | first input with a non-prime output: %d'%(round((full_score(a)-1)*100),round((pr/ex-1)*100),pr,ex,next(n for n in range(0,10**6) if not is_prime(mpz(n*n+n+a)))),flush=True)
