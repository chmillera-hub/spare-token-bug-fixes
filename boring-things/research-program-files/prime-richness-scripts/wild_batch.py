# Prime rate for recipes built from trig functions, custom rounding rules, modulus, sums, calculus
# and the digits of constants. A prime that shows up more than once counts once.
# Needs gmpy2 and mpmath. Run: python3 wild_batch.py
import math, random, json, time
from gmpy2 import mpz, is_prime, isqrt
import mpmath as mp
random.seed(17)
L=10**12
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def chance(v):
    return 0.0 if v<2 else min(1.0,1/math.log(v))
def measure(f,nmax,samples=300000):
    if nmax<=samples: ns=range(1,nmax+1)
    elif nmax<=10**7: ns=random.sample(range(1,nmax+1),samples)
    else: ns=(random.randrange(1,nmax+1) for _ in range(samples))
    seen=set(); ex=0.0; t=0; reps=0
    for n in ns:
        v=f(n); t+=1
        if v<2: continue
        ex+=chance(v)
        if is_prime(mpz(v),15):
            if v in seen: reps+=1
            else: seen.add(v)
    return t,len(seen),reps,ex
def top_input(f,limit=L):
    hi=2
    while f(hi)<=limit: hi*=2
    lo=hi//2
    while hi-lo>1:
        m=(lo+hi)//2
        if f(m)<=limit: lo=m
        else: hi=m
    return lo
def rnd(x,t):          # custom rounding: decimals at or above t go up, decimals below t go down
    fl=math.floor(x); return fl+(1 if x-fl>=t and x!=fl else 0)
out=[]
def run(group,label,f,nmax=None,samples=300000):
    if nmax is None: nmax=top_input(f)
    t,p,r,ex=measure(f,nmax,samples)
    pct=round((p/ex-1)*100) if ex>0 else -100
    out.append(dict(group=group,label=label,tested=t,primes=p,repeats=r,expected=ex,pct=pct))
    print('%-58s tested %6d distinct primes %6d repeats %6d chance %8.1f  %+5d%%'%(label,t,p,r,ex,pct),flush=True)
s,c,a=math.sin,math.cos,abs
G='Trig functions with decimals dropped'
run(G,'n × |sin(n)|',lambda n:int(n*a(s(n))),10**12)
run(G,'n² × |sin(n)|',lambda n:int(n*n*a(s(n))),10**6)
run(G,'n × (2 + sin(n))',lambda n:int(n*(2+s(n))),3*10**11)
run(G,'n + 1000 × sin(n)',lambda n:int(math.floor(n+1000*s(n))),10**12)
run(G,'n × cos(n)²',lambda n:int(n*c(n)**2),10**12)
run(G,'n × |tan(n)|',lambda n:int(min(n*a(math.tan(n)),10**15)),10**10)
run(G,'n ÷ |sin(n)|',lambda n:int(min(n/a(s(n)),10**15)),10**10)
run(G,'n² × sin(1 ÷ n)',lambda n:int(math.floor(n*n*s(1/n))),10**7)
run(G,'1000000 × |sin(n)|',lambda n:int(10**6*a(s(n))),10**12)
run(G,'sin(e to the n) ÷ ln(n)',lambda n:int(math.floor(s(math.exp(n))/math.log(n))) if n>1 else 0,700)
run(G,'n² + n + 41 + 10 × sin(n)',lambda n:int(math.floor(n*n+n+41+10*s(n))),10**6-1)
run(G,'n² + n + 41 + 2 × the whole part of 5 × sin(n)',lambda n:n*n+n+41+2*int(math.floor(5*s(n))),10**6-1)
G='Rounding rules on n² ÷ k'
for k in range(2,13):
    nm=int(math.isqrt(L*k))-2
    for name,t in (('decimals dropped',2.0),('decimals of 0.3 or more go up',0.3),('decimals of 0.5 or more go up',0.5),('any decimals go up',1e-12)):
        if t>1: f=lambda n,k=k:n*n//k
        elif t<1e-6: f=lambda n,k=k:-((-n*n)//k)
        else: f=lambda n,k=k,t=t:(n*n//k)+(1 if (n*n%k)>=t*k else 0)
        run(G,'n² ÷ %d with %s'%(k,name),f,nm)
G='Rounding rules on a scrambled recipe'
for name,t in (('decimals dropped',2.0),('decimals of 0.3 or more go up',0.3),('any decimals go up',1e-12)):
    run(G,'n × π with %s'%name,lambda n,t=t:rnd(n*math.pi,t),3*10**11)
G='Modulus (the remainder after division)'
run(G,'2 to the power n mod n',lambda n:pow(2,n,n),10**12)
run(G,'3 to the power n mod (2n + 1)',lambda n:pow(3,n,2*n+1),4*10**11)
run(G,'n² mod 1000003',lambda n:n*n%1000003,10**12)
run(G,'n² + (n mod 6)',lambda n:n*n+n%6,10**6-1)
run(G,'n × (n mod 7) + 1',lambda n:n*(n%7)+1,10**11)
run(G,'2 + (2 × n!) mod (n + 1)',lambda n:(n+1) if is_prime(n+1) else 2,300000)
run(G,'n² + n + 41 mod 1000000007',lambda n:(n*n+n+41)%1000000007,10**12)
G='Sums'
def sieve(N):
    sv=bytearray([1])*(N+1); sv[0]=sv[1]=0
    for i in range(2,int(N**.5)+1):
        if sv[i]: sv[i*i::i]=bytearray(len(sv[i*i::i]))
    return [i for i in range(N+1) if sv[i]]
P=sieve(4400000)[:300000]; PS=[0]
for q in P: PS.append(PS[-1]+q)
run(G,'the first n primes added up',lambda n:PS[n],300000)
run(G,'the first n primes added up then plus 1 for even totals',lambda n:PS[n]+(1 if PS[n]%2==0 else 0),300000)
run(G,'1 + 2 + 3 up to n',lambda n:n*(n+1)//2)
run(G,'1² + 2² + 3² up to n²',lambda n:n*(n+1)*(2*n+1)//6)
run(G,'1² + 2² + 3² up to n² then plus 1',lambda n:n*(n+1)*(2*n+1)//6+1)
N=300000; dv=[0]*(N+1)
for i in range(1,N+1):
    for j in range(i,N+1,i): dv[j]+=1
DS=[0]
for i in range(1,N+1): DS.append(DS[-1]+dv[i])
run(G,'n÷1 + n÷2 + n÷3 up to n÷n with decimals dropped in each piece',lambda n:DS[n],300000)
H=[0.0]
for i in range(1,N+1): H.append(H[-1]+1/i)
run(G,'n × (1 + 1/2 + 1/3 up to 1/n) with decimals dropped',lambda n:int(n*H[n]),300000)
SQ=[0]
for i in range(1,N+1): SQ.append(SQ[-1]+math.isqrt(i))
run(G,'√1 + √2 + √3 up to √n with decimals dropped in each piece',lambda n:SQ[n],300000)
G='Calculus'
run(G,'slope of n² + n + 41 which is 2n + 1',lambda n:2*n+1)
run(G,'slope of n³ + 2 which is 3n²',lambda n:3*n*n)
run(G,'area under x² + x + 41 from 0 to n with decimals dropped',lambda n:(2*n**3+3*n*n+246*n)//6)
run(G,'area under ln(x) from 1 to n with decimals dropped',lambda n:int(n*math.log(n)-n+1),3*10**10)
run(G,'area under x × sin(x)² from 0 to n with decimals dropped',lambda n:int(n*n/4-n*s(2*n)/4-c(2*n)/8+0.125),10**6)
run(G,'area under 1 ÷ ln(x) from 2 to n with decimals dropped',lambda n:int(mp.li(n)-mp.li(2)),10**7,samples=20000)
json.dump(out,open('wild_batch_results.json','w'),ensure_ascii=False,indent=1)
# digits of constants
mp.mp.dps=1300
print('--- leading digits of constants (3 then 31 then 314 and so on) up to 1200 digits')
for name,val in (('π',mp.pi),('e',mp.e),('φ',(1+mp.sqrt(5))/2),('√2',mp.sqrt(2)),('√3',mp.sqrt(3)),('ln 2',mp.log(2)*10)):
    digs=mp.nstr(val,1260,strip_zeros=False).replace('.','')[:1200]
    for mode in ('plain','bump'):
        pr=[];ex=0.0
        for k in range(1,1201):
            v=int(digs[:k])
            if mode=='bump': v=bump(v)
            if v<2: continue
            ex+=chance(v)
            if is_prime(mpz(v),10): pr.append(k)
        print('%-5s %-5s primes %2d chance %5.2f  digit counts of the primes: %s'%(name,mode,len(pr),ex,pr),flush=True)
