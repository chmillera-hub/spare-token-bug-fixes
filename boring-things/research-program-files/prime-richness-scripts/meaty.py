# Well-known "interesting" prime recipes from the published record lists, tested for long-run prime rate.
# A repeated prime counts once. Needs gmpy2 and mpmath. Run: python3 meaty.py
import math, json, itertools, sys
from gmpy2 import mpz, is_prime, next_prime, log, gcd, isqrt
import mpmath as mp
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
out=[]
def run(group,label,vals,note=''):
    seen=set(); ex=0.0; t=0
    for v in vals:
        v=abs(int(v)); t+=1
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),10): seen.add(v)
    pct=round((len(seen)/ex-1)*100) if ex>0 else -100
    out.append(dict(group=group,label=label,tested=t,primes=len(seen),expected=ex,pct=pct,note=note))
    print('%-58s tested %6d primes %6d chance %9.1f %+6d%%'%(label[:58],t,len(seen),ex,pct),flush=True)
N=300000
R=lambda f:(f(n) for n in range(1,N+1))
G='Equations famous for a long unbroken run of primes'
run(G,'36n² − 810n + 2753',R(lambda n:36*n*n-810*n+2753))
run(G,'47n² − 1701n + 10181',R(lambda n:47*n*n-1701*n+10181))
run(G,'103n² − 4707n + 50383',R(lambda n:103*n*n-4707*n+50383))
run(G,'8n² − 488n + 7243',R(lambda n:8*n*n-488*n+7243))
run(G,'43n² − 537n + 2971',R(lambda n:43*n*n-537*n+2971))
run(G,'2n² − 108n + 1259',R(lambda n:2*n*n-108*n+1259))
run(G,'3n³ − 183n² + 3318n − 18757',R(lambda n:3*n**3-183*n*n+3318*n-18757))
run(G,'−66n³ + 3845n² − 60897n + 251831',R(lambda n:-66*n**3+3845*n*n-60897*n+251831))
run(G,'45n⁴ − 3416n³ + 96738n² − 1212769n + 5692031',R(lambda n:45*n**4-3416*n**3+96738*n*n-1212769*n+5692031))
run(G,'6n⁴ − 558n³ + 19354n² − 296370n + 1688311',R(lambda n:6*n**4-558*n**3+19354*n*n-296370*n+1688311))
G='Equations from the published richness record lists'
run(G,'249582n² + 1',R(lambda n:249582*n*n+1))
run(G,'452042n² − 1',R(lambda n:452042*n*n-1))
run(G,'n² + 2751n + 1',R(lambda n:n*n+2751*n+1))
run(G,'n² + n − 501229',R(lambda n:n*n+n-501229))
G='Equations famous for very few primes'
run(G,'n⁶ + 1091',R(lambda n:n**6+1091))
run(G,'n¹² + 488669',R(lambda n:n**12+488669))
run(G,'n⁶ + 29450922301244534',R(lambda n:n**6+29450922301244534))
G='Powers of n plus 1 and related equations'
run(G,'n⁸ + 1',R(lambda n:n**8+1))
run(G,'n¹⁶ + 1',R(lambda n:n**16+1))
run(G,'n³² + 1',R(lambda n:n**32+1))
run(G,'n⁴ + n³ + n² + n + 1',R(lambda n:n**4+n**3+n*n+n+1))
run(G,'n⁶ + n⁵ + n⁴ + n³ + n² + n + 1',R(lambda n:(n**7-1)//(n-1) if n>1 else 7))
run(G,'n⁴ − n² + 1',R(lambda n:n**4-n*n+1))
G='Recipes that start from the nth prime'
def primes():
    p=mpz(2)
    while True: yield int(p); p=next_prime(p)
P=list(itertools.islice(primes(),N+1))
note='the recipe needs the list of primes'
for k in (2,4,6,30,210,2310,30030):
    run(G,'the nth prime + %d'%k,(p+k for p in P[:N]),note)
run(G,'2 × the nth prime + 1',(2*p+1 for p in P[:N]),note)
run(G,'(the nth prime)² − 2',(p*p-2 for p in P[:N]),note)
run(G,'(the nth prime)² + 4',(p*p+4 for p in P[:N]),note)
run(G,'the nth prime × the next prime + 2',(P[i]*P[i+1]+2 for i in range(N)),note)
run(G,'the nth prime × the next prime − 2',(P[i]*P[i+1]-2 for i in range(N)),note)
G='Famous number lists'
CAP=10**300
def upto(gen):
    for v in gen:
        if v>CAP: return
        yield v
def lucas():
    a,b=2,1
    while True: yield a; a,b=b,a+b
def pell():
    a,b=0,1
    while True: yield b; a,b=b,2*b+a
def perrin():
    a,b,c=3,0,2
    while True: yield a; a,b,c=b,c,a+b
def partitions(M):
    p=[1]
    for n in range(1,M+1):
        s=0;k=1
        while True:
            g1=k*(3*k-1)//2
            if g1>n: break
            sg=1 if k%2 else -1
            s+=sg*p[n-g1]
            g2=k*(3*k+1)//2
            if g2<=n: s+=sg*p[n-g2]
            k+=1
        p.append(s); yield s
def catalan():
    c=1
    for n in itertools.count(0):
        yield c; c=c*2*(2*n+1)//(n+2)
def bell():
    row=[1]
    while True:
        yield row[0]
        new=[row[-1]]
        for x in row: new.append(new[-1]+x)
        row=new
rough='outputs up to 300 digits'
run(G,'the Lucas numbers (2 then 1 then 3 then 4 then 7 and so on)',upto(lucas()),rough)
run(G,'the Pell numbers (1 then 2 then 5 then 12 then 29 and so on)',upto(pell()),rough)
run(G,'the Perrin numbers (3 then 0 then 2 then 3 then 2 then 5 and so on)',upto(perrin()),rough)
run(G,'the partition numbers (the count of ways to split n into a sum)',partitions(20000),'outputs up to 152 digits')
run(G,'the Catalan numbers',upto(catalan()),rough)
run(G,'the Bell numbers',upto(bell()),rough)
run(G,'(2ⁿ − 1)² − 2',upto(((2**n-1)**2-2 for n in itertools.count(1))),rough)
run(G,'(2ⁿ + 1)² − 2',upto(((2**n+1)**2-2 for n in itertools.count(1))),rough)
run(G,'2 to the power of the nth prime then minus 1',upto((2**p-1 for p in P)),rough+' and the recipe needs the list of primes')
run(G,'(2 to the power of the nth prime then plus 1) ÷ 3',upto(((2**p+1)//3 for p in P[1:])),rough+' and the recipe needs the list of primes')
run(G,'78557 × 2ⁿ + 1',upto((78557*2**n+1 for n in itertools.count(1))),rough)
run(G,'509203 × 2ⁿ − 1',upto((509203*2**n-1 for n in itertools.count(1))),rough)
run(G,'3 × 2ⁿ + 1',upto((3*2**n+1 for n in itertools.count(1))),rough)
def concat():
    s=''
    for n in itertools.count(1):
        s+=str(n); yield int(s)
def concat_primes():
    s=''
    for p in P:
        s+=str(p); yield int(s)
run(G,'the whole numbers written side by side (1 then 12 then 123 and so on)',upto(concat()),rough)
run(G,'the primes written side by side (2 then 23 then 235 then 2357 and so on)',upto(concat_primes()),rough+' and the recipe needs the list of primes')
def fortunate(M):
    pr=mpz(1); p=mpz(1)
    for _ in range(M):
        p=next_prime(p); pr*=p
        yield int(next_prime(pr+1)-pr)
run(G,'the gap from (the product of the first n primes) to the next prime after that product plus 1',fortunate(150),'150 outputs tested')
mp.mp.dps=40
run(G,'e to the power (π × √n) with decimals dropped',(int(mp.floor(mp.exp(mp.pi*mp.sqrt(n)))) for n in range(1,3001)),'3000 outputs tested')
run(G,'n to the power π with decimals dropped',R(lambda n:int(n**math.pi)) if False else (int(mp.floor(mp.mpf(n)**mp.pi)) for n in range(1,60001)),'60000 outputs tested')
# Rowland recurrence
a=7; ones=0; ps=set(); nonp=0
for n in range(2,3000001):
    g=int(gcd(n,a)); a+=g
    if g==1: ones+=1
    elif is_prime(g): ps.add(g)
    else: nonp+=1
print('ROWLAND steps 2999999 ones',ones,'distinct primes',len(ps),'non-prime jumps',nonp,'largest',max(ps),sorted(ps)[:12])
json.dump(out,open('meaty_results.json','w'),ensure_ascii=False,indent=1)
