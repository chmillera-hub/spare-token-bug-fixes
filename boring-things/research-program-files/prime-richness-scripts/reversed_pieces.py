import random
from gmpy2 import is_prime
random.seed(21)
PI=[0,4,25,168,1229,9592,78498,664579,5761455,50847534,455052511,4118054813,37607912018]
dens={k:(PI[k]-PI[k-1])/(9*10**(k-1)) for k in range(1,13)}
def pieces(n):
    s=str(n); out=[]
    for k in range(1,len(s)+1):
        t=s[:k][::-1]
        if t[0]=='0': continue
        out.append((k,int(t)))
    return out
def show(n):
    ps=pieces(n); c=sum(1 for k,v in ps if is_prime(v)); e=sum(dens[k] for k,v in ps)
    print(n,'prime' if is_prime(n) else 'not prime','|',c,'of',len(ps),'| chance',round(e,2),'| pct',round((c/e-1)*100),'|',' '.join(f"{v}{'*' if is_prime(v) else ''}" for k,v in ps))
for n in [123456789,2147483647,999999937,1234567891,7654321,3916589,1000000007]: show(n)
N=200000; primes=[]
while len(primes)<N:
    n=random.randrange(10**11,10**12)
    if is_prime(n): primes.append(n)
byd={d:[0,0.0,0,0.0] for d in range(1,10)}  # partial primes, exp ; full primes, exp
bylen={k:[0,0.0] for k in range(1,13)}
dist={}
for p in primes:
    d=int(str(p)[0]); c=0
    for k,v in pieces(p):
        ip=is_prime(v); c+=ip
        bylen[k][0]+=ip; bylen[k][1]+=dens[k]
        if k<12: byd[d][0]+=ip; byd[d][1]+=dens[k]
        else: byd[d][2]+=ip; byd[d][3]+=dens[k]
    dist[c]=dist.get(c,0)+1
tp=sum(b[0] for b in bylen.values()); te=sum(b[1] for b in bylen.values())
print('overall pct',round((tp/te-1)*100))
print('by length',' '.join(f'{k}:{round((a/e-1)*100):+d}%' for k,(a,e) in bylen.items()))
for d,(a,e,fa,fe) in byd.items(): print('lead',d,'partial pct',round((a/e-1)*100),'full reversal pct',round((fa/fe-1)*100) if fe else None)
print('dist',sorted(dist.items()))
best=sorted(primes,key=lambda n:-sum(1 for k,v in pieces(n) if is_prime(v)))[:3]
for n in best: show(n)
# champions: left-truncatable primes whose reversal is prime
lvl=[2,3,5,7]; allp=[]
while lvl:
    allp+=lvl; nxt=[]
    for p in lvl:
        m=10**len(str(p))
        for dd in range(1,10):
            q=dd*m+p
            if is_prime(q): nxt.append(q)
    lvl=nxt
ch=[int(str(q)[::-1]) for q in allp if is_prime(int(str(q)[::-1]))]
print('champions',len(ch),'largest',max(ch),'digits',len(str(max(ch))))
show(max(ch))
