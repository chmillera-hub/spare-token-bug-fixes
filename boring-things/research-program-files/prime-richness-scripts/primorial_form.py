# The form at the top of the ranked list: (product of the first n primes) x 30030 - 1 and + 1,
# counted over every such number up to 1200 digits. Needs gmpy2.
import math, time
from gmpy2 import mpz, is_prime, next_prime, log
t=time.time()
for sign in (-1,1):
    P=mpz(1); q=mpz(1); pr=0; ex=0.0; n=0; pred=0.0; hits=[]; g=1.0
    while True:
        q=next_prime(q); P*=q; g*=int(q)/(int(q)-1)
        v=P*30030+sign
        if len(str(v))>1200: break
        n+=1; c=1/float(log(v)); ex+=c; pred+=c*g
        if is_prime(v,1): pr+=1; hits.append(n)
    print('sign %+d | tested %d | primes %d | chance %.2f | the blocking formula predicts %.1f | %+d%% | positions %s | %.0fs'%(sign,n,pr,ex,pred,round((pr/ex-1)*100),hits,time.time()-t),flush=True)
