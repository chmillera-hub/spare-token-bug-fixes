# Hybrid test: take a prime-rich equation n^2 + n + A and feed it inputs that are multiples of P,
# where P is the product of every prime up to a limit that CAN divide an output.
# Then none of those primes can divide an output either. Needs gmpy2.
import random, time, json, math
from gmpy2 import mpz, is_prime, log
random.seed(8)
A=26853927251
def primes_upto(N):
    s=bytearray([1])*(N+1); s[0]=s[1]=0
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
PR=primes_upto(20000)
D=1-4*A
def bad(q): 
    if q==2: return A%2==0
    d=D%q
    return d==0 or pow(d,(q-1)//2,q)==1
out=[]
for limit,samples in ((0,100000),(300,100000),(1000,100000)):
    B=[q for q in PR if q<=limit and bad(q)]
    P=mpz(1)
    for q in B: P*=q
    pred=1.0
    for q in PR:
        w=0 if (q<=limit or not bad(q)) else (1 if D%q==0 else 2)
        pred*=(1-w/q)/(1-1/q)
    t=time.time(); pr=0; ex=0.0
    for _ in range(samples):
        n=P*random.randrange(1,10**6+1); v=n*n+n+A; ex+=1/float(log(v))
        if is_prime(v,1): pr+=1
    digits=len(str(P*10**6))*2
    out.append(dict(limit=limit,blocked=len(B),digits=digits,samples=samples,primes=pr,chance=ex,pct=round((pr/ex-1)*100),pred=round((pred-1)*100)))
    print('limit %5d | primes folded in %3d | outputs about %4d digits | tested %6d | primes %5d | chance %7.1f | measured %+5d%% | predicted %+5d%% | %.0fs'%(limit,len(B),digits,samples,pr,ex,round((pr/ex-1)*100),round((pred-1)*100),time.time()-t),flush=True)
json.dump(out,open('hybrid_results.json','w'))
