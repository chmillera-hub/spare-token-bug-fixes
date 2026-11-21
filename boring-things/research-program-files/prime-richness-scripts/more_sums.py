# More running totals (plain, bumped, bumped and carried) plus a hunt for the best starting number
# for the carried sum 1 + 2 + 3 + 4. Needs gmpy2 and mpmath and the file running_sums.py beside it.
import math, json, itertools, sys, io
_o=sys.stdout; sys.stdout=io.StringIO()
import running_sums as rs          # reuses run() and the helpers (its own table prints are muted)
sys.stdout=_o
from gmpy2 import mpz, is_prime, next_prime
nat,mapn,run,bump=rs.nat,rs.mapn,rs.run,rs.bump
def primes(): return rs.primes()
def gaps():
    p=2
    for q in itertools.islice(primes(),1,None): yield q-p; p=q
def digsum(): return (sum(map(int,str(n))) for n in nat())
R=[
 ('start at 2 then add the gaps between neighboring primes (circular because the recipe needs the list of primes)',gaps,2),
 ('the gaps between neighboring primes added up',gaps,0),
 ('4 + 9 + 25 + 49 and so on (squares of primes)',lambda:(p*p for p in primes()),0),
 ('2 + 5 + 11 + 17 and so on (every second prime)',lambda:itertools.islice(primes(),0,None,2),0),
 ('1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime)',lambda:(n*p for n,p in zip(nat(),primes())),0),
 ('1 + 16 + 81 + 256 and so on (fourth powers)',mapn(lambda n:n**4),0),
 ('2 + 6 + 12 + 20 and so on (n times n + 1)',mapn(lambda n:n*(n+1)),0),
 ('1 + 9 + 25 + 49 and so on (odd squares)',mapn(lambda n:(2*n-1)**2),0),
 ('start at 1 then add 4 + 8 + 12 + 16 and so on',mapn(lambda n:4*n),1),
 ('start at 29 then add 2 + 6 + 10 + 14 and so on',mapn(lambda n:4*n-2),29),
 ('start at 1 then add 6 + 12 + 18 + 24 and so on',mapn(lambda n:6*n),1),
 ('start at 5660169547 then add 30 + 60 + 90 and so on',mapn(lambda n:30*n),5660169547),
 ('start at 29717281333 then add 6 + 12 + 18 and so on',mapn(lambda n:6*n),29717281333),
 ('start at 100800448037 then add 210 + 420 + 630 and so on',mapn(lambda n:210*n),100800448037),
 ('the digit totals of 1 and 2 and 3 and so on added up',digsum,0),
 ('1 + 11 + 111 + 1111 and so on',mapn(lambda n:(10**n-1)//9),0),
]
out=[]
for label,terms,start in R:
    r=run(terms,start)
    out.append(dict(label=label,steps=r[0][0],plain=r[0][3],bump=r[1][3],carry=r[2][3],primes=[x[1] for x in r],chance=[round(x[2],1) for x in r]))
    print('%-64s steps %6d | plain %+5d%% (%d) | bump %+5d%% (%d) | carry %+5d%% (%d of %.1f)'%(label[:64],r[0][0],r[0][3],r[0][1],r[1][3],r[1][1],r[2][3],r[2][1],r[2][2]),flush=True)
# best starting number for the carried sum 1 + 2 + 3 + 4
best=[]
for s0 in range(0,601):
    s=s0; pr=0; ex=0.0
    for n in range(1,20001):
        s=bump(s+n); ex+=rs.chance(s)
        if is_prime(mpz(s)): pr+=1
    best.append((pr/ex,s0))
best.sort(reverse=True)
print('best starts (20000 steps):',[(s0,round((x-1)*100)) for x,s0 in best[:6]],'worst:',[(s0,round((x-1)*100)) for x,s0 in best[-3:]])
for x,s0 in best[:3]:
    r=run(nat,s0)
    lab='start at %d then add 1 + 2 + 3 + 4 and so on'%s0
    out.append(dict(label=lab,steps=r[0][0],plain=r[0][3],bump=r[1][3],carry=r[2][3],primes=[x[1] for x in r],chance=[round(x[2],1) for x in r]))
    print('%-64s | plain %+5d%% | bump %+5d%% | carry %+5d%% (%d of %.1f)'%(lab,r[0][3],r[1][3],r[2][3],r[2][1],r[2][2]),flush=True)
json.dump(out,open('more_sums_results.json','w'),ensure_ascii=False,indent=1)
