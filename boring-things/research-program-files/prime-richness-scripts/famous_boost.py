# Takes well-known number lists and hunts for the rule that makes the most primes out of each one.
# Rules tried: add or subtract a number up to 50, the bump, a fixed last digit, a stronger bump
# (move up to the nearest number that shares no factor with 30 or 210 or 2310 or 30030) and
# multiply by 2 or 6 or 30 or 210 or 2310 or 30030 and then add or subtract 1.
# The winner is picked on one stretch of the list and then confirmed on a fresh later stretch.
import math, json, itertools, sys
from gmpy2 import mpz, is_prime, log, gcd
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def wheel(W):
    def f(v):
        while gcd(v,W)!=1: v+=1
        return v
    return f
RULES=[('no rule',lambda v:v),('bump the last digit',bump)]
for d in (1,3,7,9): RULES.append(('change the last digit to %d'%d,lambda v,d=d:v-v%10+d))
for W in (30,210,2310,30030): RULES.append(('move up to the nearest number that shares no factor with %d'%W,wheel(W)))
for k in range(1,51):
    RULES.append(('add %d'%k,lambda v,k=k:v+k)); RULES.append(('subtract %d'%k,lambda v,k=k:v-k))
for a in (2,6,30,210,2310,30030):
    RULES.append(('multiply by %d then add 1'%a,lambda v,a=a:a*v+1)); RULES.append(('multiply by %d then subtract 1'%a,lambda v,a=a:a*v-1))
def rate(terms,rule):
    seen=set(); ex=0.0
    for t in terms:
        v=rule(t)
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),1): seen.add(v)
    return len(seen),ex
def fibs(a,b):
    while True: yield a; a,b=b,a+b
def pell():
    a,b=0,1
    while True: yield b; a,b=b,2*b+a
def facts():
    f=1
    for n in itertools.count(1): f*=n; yield f
def catalan():
    c=1
    for n in itertools.count(0):
        yield c; c=c*2*(2*n+1)//(n+2)
def primorials():
    from gmpy2 import next_prime
    p=mpz(1); q=mpz(1)
    while True: q=next_prime(q); p*=q; yield int(p)
def partitions():
    p=[1]
    for n in itertools.count(1):
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
def poly(f): return lambda:(f(n) for n in itertools.count(1))
SEQ=[
 ('the triangle numbers n × (n + 1) ÷ 2',poly(lambda n:n*(n+1)//2),'poly'),
 ('the squares n²',poly(lambda n:n*n),'poly'),
 ('the cubes n³',poly(lambda n:n**3),'poly'),
 ('the fourth powers n⁴',poly(lambda n:n**4),'poly'),
 ('the pentagon numbers n × (3n − 1) ÷ 2',poly(lambda n:n*(3*n-1)//2),'poly'),
 ('n × (n + 1)',poly(lambda n:n*(n+1)),'poly'),
 ('the pyramid numbers n × (n + 1) × (n + 2) ÷ 6',poly(lambda n:n*(n+1)*(n+2)//6),'poly'),
 ('the totals of 1² + 2² + 3² up to n²',poly(lambda n:n*(n+1)*(2*n+1)//6),'poly'),
 ('the Fibonacci numbers',lambda:fibs(1,2),'fast'),
 ('the list 2 then 1 then 3 then 4 then 7 where each number is the two before added up',lambda:fibs(2,1),'fast'),
 ('the list 1 then 2 then 5 then 12 then 29 where each number is twice the one before plus the one before that',pell,'fast'),
 ('the powers of 2',poly(lambda n:2**n),'fast'),
 ('the powers of 3',poly(lambda n:3**n),'fast'),
 ('the powers of 10',poly(lambda n:10**n),'fast'),
 ('the factorials 1 × 2 × 3 up to n',facts,'fast'),
 ('the products of the first n primes',primorials,'fast'),
 ('the count of ways to pair up n sets of brackets',catalan,'fast'),
 ('the numbers 1 then 11 then 111 then 1111',poly(lambda n:(10**n-1)//9),'fast'),
 ('n to the power n',poly(lambda n:n**n),'fast'),
 ('the partition numbers',partitions,'part'),
]
out=[]
for name,gen,kind in SEQ:
    if kind=='poly':
        terms=list(itertools.islice(gen(),350000)); A=terms[:50000]; B=terms[50000:]
    elif kind=='part':
        terms=list(itertools.islice(gen(),20000)); A=terms[:5000]; B=terms[5000:]
    else:
        A=[];B=[]
        for t in gen():
            if t<10**150: A.append(t)
            elif t<10**450: B.append(t)
            else: break
    sc=[]
    for rn,rf in RULES:
        p,ex=rate(A,rf)
        sc.append(((p/ex) if ex>0 else 0,p,ex,rn,rf))
    plainA=[s for s in sc if s[3]=='no rule'][0]
    sc.sort(key=lambda s:-s[0])
    res=dict(name=name,screen_terms=len(A),confirm_terms=len(B),top=[])
    pp,pex=rate(B,RULES[0][1]); res['plain_confirm']=dict(primes=pp,chance=pex,pct=round((pp/pex-1)*100) if pex else -100)
    for s in sc[:3]:
        p,ex=rate(B,s[4])
        res['top'].append(dict(rule=s[3],screen_pct=round((s[0]-1)*100),screen_primes=s[1],confirm_primes=p,confirm_chance=ex,confirm_pct=round((p/ex-1)*100) if ex else -100))
    out.append(res)
    print(name[:44],'| no rule on the confirming stretch %+d%% (%d of %.1f)'%(res['plain_confirm']['pct'],pp,pex),flush=True)
    for t in res['top']: print('     %-62s picked at %+5d%% | confirmed at %+5d%% (%d primes where chance predicts %.1f)'%(t['rule'],t['screen_pct'],t['confirm_pct'],t['confirm_primes'],t['confirm_chance']),flush=True)
    json.dump(out,open('famous_boost_results.json','w'),ensure_ascii=False,indent=1)
