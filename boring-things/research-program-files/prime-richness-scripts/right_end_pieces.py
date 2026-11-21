import random, math
from gmpy2 import mpz, is_prime
random.seed(11)
PI=[0,4,25,168,1229,9592,78498,664579,5761455,50847534,455052511,4118054813,37607912018]
dens={k:(PI[k]-PI[k-1])/(9*10**(k-1)) for k in range(1,13)}
def suffixes(n):
    s=str(n); out=[]
    for k in range(1,len(s)):
        t=s[-k:]
        if t[0]=='0': continue
        out.append((k,int(t)))
    return out
def stats(nums,name):
    by={k:[0,0] for k in range(1,12)}; dist={}
    tot=0;exp=0.0
    for n in nums:
        c=0
        for k,v in suffixes(n):
            by[k][1]+=1; exp+=dens[k]; tot+=1
            if is_prime(v): by[k][0]+=1; c+=1
        dist[c]=dist.get(c,0)+1
    P=sum(b[0] for b in by.values())
    print(name,'suffixes',tot,'primes',P,'expected',round(exp),'pct',round((P/exp-1)*100))
    print('  by length:',' '.join(f'{k}:{round((by[k][0]/by[k][1]/dens[k]-1)*100):+d}%' for k in by))
    print('  dist:',sorted(dist.items()))
    return by
N=200000
primes=[]
while len(primes)<N:
    n=random.randrange(10**11,10**12)
    if is_prime(n): primes.append(n)
stats(primes,'12-digit primes')
stats([random.randrange(10**10,10**11)*10+random.choice([1,3,7,9]) for _ in range(N)],'12-digit numbers ending 1 3 7 9')
stats([random.randrange(10**11,10**12) for _ in range(N)],'12-digit ordinary numbers')
# best in sample
best=sorted(primes,key=lambda n:-sum(1 for k,v in suffixes(n) if is_prime(v)))[:5]
for n in best: print('best',n,[(v,bool(is_prime(v))) for k,v in suffixes(n)])
def show(n):
    sf=suffixes(n); c=sum(1 for k,v in sf if is_prime(v)); e=sum(dens[k] for k,v in sf if k in dens)
    print(n,'prime' if is_prime(n) else 'not prime','| prime suffixes',c,'of',len(sf),'| chance',round(e,2),'| pct',round((c/e-1)*100) if e else None,'|',' '.join(f"{v}{'*' if is_prime(v) else ''}" for k,v in sf))
for n in [123456789,1234567891,2147483647,1000000007,999999937,987654323,739391133,6666666667 if False else 9999999967, 357686312646216567629137]:
    try: show(n)
    except Exception as ex: print(n,ex)
# left-truncatable primes
lvl=[2,3,5,7]; total=0; big=0
while lvl:
    total+=len(lvl); big=max(lvl)
    nxt=[]
    for p in lvl:
        m=10**len(str(p))
        for d in range(1,10):
            q=d*m+p
            if is_prime(q): nxt.append(q)
    lvl=nxt
print('left-truncatable total',total,'largest',big)
