# Does the prime percentage of an equation hold when the outputs have 100 or 300 or 1000 digits?
# Random inputs are drawn so the outputs have about the target count of digits. Needs gmpy2.
import random, time, json
from gmpy2 import mpz, is_prime, log
random.seed(101)
EQ=[('n',1,lambda n:n),
    ('2n + 1',1,lambda n:2*n+1),
    ('510510 × n + 1',1,lambda n:510510*n+1),
    ('n² + n + 41',2,lambda n:n*n+n+41),
    ('36n² − 810n + 2753',2,lambda n:36*n*n-810*n+2753),
    ('n² + n + 26853927251',2,lambda n:n*n+n+26853927251),
    ('−66n³ + 3845n² − 60897n + 251831',3,lambda n:abs(-66*n**3+3845*n*n-60897*n+251831)),
    ('n⁶ + 1091',6,lambda n:n**6+1091)]
out=[]
def go(label,deg,f,digits,samples):
    t=time.time(); d=max(2,digits//deg); pr=0; ex=0.0
    for _ in range(samples):
        v=mpz(f(random.randrange(10**(d-1),10**d))); ex+=1/float(log(v))
        if is_prime(v,1): pr+=1
    pct=round((pr/ex-1)*100)
    out.append(dict(label=label,digits=digits,samples=samples,primes=pr,chance=ex,pct=pct))
    print('%-34s about %4d digits | tested %6d | primes %5d | chance %7.1f | %+5d%% | share prime %.2f%% | %.0fs'%(label,digits,samples,pr,ex,pct,100*pr/samples,time.time()-t),flush=True)
for label,deg,f in EQ: go(label,deg,f,100,40000)
for label,deg,f in EQ: go(label,deg,f,300,20000)
go('n² + n + 26853927251',2,EQ[5][2],1000,2500)
json.dump(out,open('big_digits_results.json','w'),ensure_ascii=False,indent=1)
