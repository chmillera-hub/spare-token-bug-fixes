# Running totals tested for primes three ways: the plain total, the total with the last digit bumped,
# and the total bumped and then carried into the next addition. A repeated prime counts once.
# Needs gmpy2 and mpmath. Run: python3 running_sums.py
import math, json, itertools
from gmpy2 import mpz, is_prime, next_prime
import mpmath as mp
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def chance(v):
    if v<2: return 0.0
    return min(1.0,1/(math.log(v) if v<10**300 else float(mp.log(v))))
def run(terms,start=0,steps=300000,cap=10**300):
    res=[]
    for mode in ('plain','bump','carry'):
        s=start; seen=set(); ex=0.0; n=0
        for t in itertools.islice(terms(),steps):
            s+=t
            if s>cap: break
            v=s
            if mode=='bump': v=bump(s)
            if mode=='carry': s=v=bump(s)
            n+=1
            if v<2: continue
            ex+=chance(v)
            if is_prime(mpz(v),10): seen.add(v)
        res.append((n,len(seen),ex,round((len(seen)/ex-1)*100) if ex else -100))
    return res
def nat():
    n=0
    while True: n+=1; yield n
def mapn(f): return lambda:(f(n) for n in nat())
def const(c): return lambda:itertools.repeat(c)
def primes():
    p=mpz(2)
    while True: yield int(p); p=next_prime(p)
def fib():
    a,b=1,1
    while True: yield a; a,b=b,a+b
def facts():
    f=1
    for n in nat(): f*=n; yield f
mp.mp.dps=100010
PI=mp.nstr(mp.pi,100005,strip_zeros=False).replace('.','')[:100000]
mp.mp.dps=30
R=[
 ('1 + 2 + 3 + 4 and so on',nat,0),
 ('1 + 3 + 5 + 7 and so on (odd numbers)',mapn(lambda n:2*n-1),0),
 ('2 + 4 + 6 + 8 and so on (even numbers)',mapn(lambda n:2*n),0),
 ('start at 41 then add 2 + 4 + 6 + 8 and so on',mapn(lambda n:2*n),41),
 ('start at 26853927251 then add 2 + 4 + 6 + 8 and so on',mapn(lambda n:2*n),26853927251),
 ('1 + 4 + 9 + 16 and so on (squares)',mapn(lambda n:n*n),0),
 ('1 + 8 + 27 + 64 and so on (cubes)',mapn(lambda n:n**3),0),
 ('1 + 3 + 6 + 10 and so on (triangle numbers)',mapn(lambda n:n*(n+1)//2),0),
 ('2 + 3 + 5 + 7 and so on (primes)',primes,0),
 ('6 + 12 + 18 + 24 and so on (multiples of 6)',mapn(lambda n:6*n),0),
 ('start at 1 then add 30 + 60 + 90 and so on (multiples of 30)',mapn(lambda n:30*n),1),
 ('start at 1 then add 210 + 420 + 630 and so on (multiples of 210)',mapn(lambda n:210*n),1),
 ('start at 1 then add 2310 + 4620 + 6930 and so on (multiples of 2310)',mapn(lambda n:2310*n),1),
 ('1 + 1 + 1 + 1 and so on',const(1),0),
 ('2 + 2 + 2 + 2 and so on',const(2),0),
 ('3 + 3 + 3 + 3 and so on',const(3),0),
 ('6 + 6 + 6 + 6 and so on',const(6),0),
 ('7 + 7 + 7 + 7 and so on',const(7),0),
 ('start at 1 then add 10 + 10 + 10 and so on',const(10),1),
 ('start at 1 then add 30 + 30 + 30 and so on',const(30),1),
 ('start at 1 then add 210 + 210 + 210 and so on',const(210),1),
 ('start at 1 then add 30030 + 30030 + 30030 and so on',const(30030),1),
 ('n × π with decimals dropped added up',mapn(lambda n:int(n*math.pi)),0),
 ('√n with decimals dropped added up',mapn(lambda n:math.isqrt(n)),0),
 ('n × ln(n) with decimals dropped added up',mapn(lambda n:int(n*math.log(n))),0),
 ('n² + n + 41 added up',mapn(lambda n:n*n+n+41),0),
 ('the digits of π added up (3 + 1 + 4 + 1 + 5 and so on)',lambda:(int(c) for c in PI),0),
 ('1 + 2 + 4 + 8 and so on (powers of 2)',mapn(lambda n:2**(n-1)),0),
 ('1 + 3 + 9 + 27 and so on (powers of 3)',mapn(lambda n:3**(n-1)),0),
 ('1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers)',fib,0),
 ('1 + 2 + 6 + 24 and so on (factorials)',facts,0),
]
out=[]
for label,terms,start in R:
    r=run(terms,start)
    out.append(dict(label=label,steps=r[0][0],plain=r[0][3],bump=r[1][3],carry=r[2][3],primes=[x[1] for x in r],chance=[round(x[2],1) for x in r]))
    print('%-62s steps %6d | plain %+5d%% (%d) | bump %+5d%% (%d) | bump and carry %+5d%% (%d of chance %.1f)'%(label,r[0][0],r[0][3],r[0][1],r[1][3],r[1][1],r[2][3],r[2][1],r[2][2]),flush=True)
json.dump(out,open('running_sums_results.json','w'),ensure_ascii=False,indent=1)
