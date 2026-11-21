# Equations with no numbers in them: several variables joined by plus and times and powers,
# then one-variable equations whose every coefficient is 1 (with a lone + 1 at the end).
# A repeated prime counts once. Needs numpy and gmpy2.
import math, random, json, itertools, time
import numpy as np
from gmpy2 import mpz, is_prime, log
random.seed(2026)
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
out=[]
def run(group,label,vals,note=''):
    seen=set(); ex=0.0; t=0
    for v in vals:
        v=abs(int(v)); t+=1
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),5): seen.add(v)
    pct=round((len(seen)/ex-1)*100) if ex>0 else -100
    out.append(dict(group=group,label=label,tested=t,primes=len(seen),expected=ex,pct=pct,note=note))
    print('%-46s tested %6d primes %6d chance %9.1f %+6d%%  %s'%(label[:46],t,len(seen),ex,pct,note),flush=True)
S=300000
def pairs(X,Y=None):
    Y=Y or X
    for _ in range(S):
        x=random.randrange(1,X+1); y=random.randrange(1,Y+1)
        yield x,y
def triples(X):
    for _ in range(S): yield random.randrange(1,X+1),random.randrange(1,X+1),random.randrange(1,X+1)
G='Two variables and no numbers'
M=10**6
run(G,'x + y',(x+y for x,y in pairs(M)))
run(G,'x × y',(x*y for x,y in pairs(M)))
run(G,'x × y + x + y',(x*y+x+y for x,y in pairs(M)))
run(G,'x² + y²',(x*x+y*y for x,y in pairs(M)))
run(G,'x² + x × y + y²',(x*x+x*y+y*y for x,y in pairs(M)))
run(G,'x² − x × y + y²',(x*x-x*y+y*y for x,y in pairs(M)))
run(G,'x² + y² + x × y + x + y',(x*x+y*y+x*y+x+y for x,y in pairs(M)))
run(G,'x² + y² + x + y',(x*x+y*y+x+y for x,y in pairs(M)))
run(G,'x³ + y²',(x**3+y*y for x,y in pairs(10**4,M)))
run(G,'x³ + y³',(x**3+y**3 for x,y in pairs(10**4)))
run(G,'x³ + x × y + y³',(x**3+x*y+y**3 for x,y in pairs(10**4)))
run(G,'x³ + x² × y + y³',(x**3+x*x*y+y**3 for x,y in pairs(10**4)))
run(G,'x⁴ + y²',(x**4+y*y for x,y in pairs(1000,M)))
run(G,'x⁴ + y⁴',(x**4+y**4 for x,y in pairs(1000)),'the inputs go up to 1000 so many pairs repeat')
run(G,'x⁴ + x² × y² + y⁴',(x**4+x*x*y*y+y**4 for x,y in pairs(1000)))
run(G,'x⁸ + y⁸',(x**8+y**8 for x,y in pairs(10**5)))
run(G,'x¹⁶ + y¹⁶',(x**16+y**16 for x,y in pairs(10**5)))
CAP=10**150
def powpairs(f,cap=CAP,sym=True):
    x=2
    while True:
        y=x+1 if sym else 2; any_=False
        while True:
            v=f(x,y)
            if abs(v)>cap: break
            any_=True; yield v; y+=1
        if (not any_ and sym) or (not sym and x>=300): return
        x+=1
rough='outputs up to 150 digits'
rough2='x from 2 to 300 and outputs up to 150 digits'
run(G,'x to the power y + y to the power x',powpairs(lambda x,y:x**y+y**x),rough)
run(G,'x to the power y − y to the power x',powpairs(lambda x,y:x**y-y**x),rough)
run(G,'x to the power y + y',powpairs(lambda x,y:x**y+y,sym=False),rough2)
run(G,'x to the power y + x + y',powpairs(lambda x,y:x**y+x+y,sym=False),rough2)
run(G,'x to the power y + x × y',powpairs(lambda x,y:x**y+x*y,sym=False),rough2)
run(G,'x to the power x + y to the power y',powpairs(lambda x,y:x**x+y**y,cap=10**300),'outputs up to 300 digits')
run(G,'x to the power x + y',((x**x+y for x in range(2,61) for y in range(1,5001))),'x up to 60 and y up to 5000')
G='Three variables and no numbers'
run(G,'x² + y² + z²',(x*x+y*y+z*z for x,y,z in triples(M)))
run(G,'x × y + y × z + z × x',(x*y+y*z+z*x for x,y,z in triples(M)))
run(G,'x × y × z + x + y + z',(x*y*z+x+y+z for x,y,z in triples(10**4)))
run(G,'x² + y² + z² + x × y + y × z + z × x',(x*x+y*y+z*z+x*y+y*z+z*x for x,y,z in triples(M)))
run(G,'x³ + y³ + z³',(x**3+y**3+z**3 for x,y,z in triples(10**4)))
run(G,'x⁴ + y⁴ + z⁴',(x**4+y**4+z**4 for x,y,z in triples(1000)))
run(G,'x × y + z',(x*y+z for x,y,z in triples(M)))
json.dump(out,open('no_numbers_results.json','w'),ensure_ascii=False,indent=1)
# one variable: every coefficient is 0 or 1 and the equation ends in + 1; degree up to 16
def sieve(K):
    s=bytearray([1])*(K+1); s[0]=s[1]=0
    for i in range(2,int(K**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(K+1) if s[i]]
PR=sieve(400); DEG=16
masks=np.arange(1,2**(DEG+1),2,dtype=np.int64)            # bit 0 set: the lone + 1
C=((masks[:,None]>>np.arange(DEG+1))&1).astype(np.int64)  # rows of coefficients
logscore=np.zeros(len(masks)); sumw=np.zeros(len(masks))
for p in PR:
    X=np.array([[pow(x,k,p) for k in range(DEG+1)] for x in range(p)],dtype=np.int64)
    w=((C@X.T)%p==0).sum(axis=1)
    sumw+=w
    with np.errstate(divide='ignore'): logscore+=np.log(np.maximum(1-w/p,1e-300))-math.log(1-1/p)
meanw=sumw/len(PR)
ok=(meanw<1.45)&(masks>1)
order=np.argsort(-np.where(ok,logscore,-1e9))[:14]
def name(mask):
    sup='⁰¹²³⁴⁵⁶⁷⁸⁹'; t=[]
    for k in range(DEG,0,-1):
        if mask>>k&1: t.append('x'+(''.join(sup[int(c)] for c in str(k)) if k>1 else ''))
    return ' + '.join(t+['1'])
def f(mask,n): return sum(n**k for k in range(DEG+1) if mask>>k&1)
G='One variable with every coefficient equal to 1'
res=[]
for i in order:
    m=int(masks[i]); pr=0; ex=0.0
    for n in range(1,20001):
        v=f(m,n); ex+=chance(v)
        if is_prime(mpz(v),5): pr+=1
    res.append((pr/ex,m,math.exp(logscore[i])))
    print('screen %-60s predicted %+5d%% measured on 20000 inputs %+5d%%'%(name(m),round((math.exp(logscore[i])-1)*100),round((pr/ex-1)*100)),flush=True)
res.sort(reverse=True)
for sc,m,pred in res[:6]:
    run(G,name(m),(f(m,n) for n in range(1,S+1)))
for m in (0b11,0b101,0b111,0b1011,0b1101,0b10011,0b11111,0b1111111,(1<<16)|1,(1<<8)|1):
    run(G,name(m),(f(m,n) for n in range(1,S+1)))
json.dump(out,open('no_numbers_results.json','w'),ensure_ascii=False,indent=1)
