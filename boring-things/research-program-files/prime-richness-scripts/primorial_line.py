# Counts primes among (product of the primes up to p) x n + 1 for random n from 1 to 1 million.
# Needs gmpy2. Run: python3 primorial_line.py
import math, random, time
from gmpy2 import mpz, is_prime, next_prime, log
random.seed(9)
def run(p,samples,top=10**6,bump=False,skip=()):
    a=mpz(1); pred=1.0; q=mpz(2)
    while q<=p:
        if int(q) not in skip: a*=q; pred*=int(q)/(int(q)-1)
        q=next_prime(q)
    t=time.time(); pr=0; ex=0.0
    for _ in range(samples):
        v=a*random.randrange(1,top+1)+1
        if bump:
            d=int(v%10); v=v-d+{0:1,2:3,4:7,5:7,6:7,8:9}.get(d,d)
        ex+=1/float(log(v))
        if is_prime(v,5): pr+=1
    print('p = %5d | digits in the multiplier %4d | tested %6d | primes %6d | chance predicts %7.1f | measured %+5d%% | predicted %+5d%% | %.0fs'%(p,len(str(a)),samples,pr,ex,round((pr/ex-1)*100),round((pred-1)*100),time.time()-t),('bump' if bump else ''),('skip 2 and 5' if skip else ''),flush=True)
run(17,300000,top=1900000)
run(97,300000)
run(541,300000)
run(1009,300000)
run(17,300000,bump=True,skip=(2,5))
