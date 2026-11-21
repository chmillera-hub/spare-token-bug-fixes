# Lists built from the product of the first primes (2 x 3 x 5 x ... x p).
# Needs the free Python package gmpy2. Run: python3 primorial_lists.py
import math
from gmpy2 import mpz, is_prime, next_prime
LIMIT=2000
primes=[]; p=mpz(2)
while p<LIMIT: primes.append(int(p)); p=next_prime(p)
def has_used_factor(r,upto):
    for q in primes:
        if q>upto: break
        if r%q==0: return True
    return False
P=mpz(1); n=0; exact=0; nofac=0; naive=0.0; adj=0.0; hits=[]
print('First entries of (product of primes up to p) divided by (p + 1) with decimals dropped:')
for p in primes:
    P*=p; r=P//(p+1)
    if p<=37: print(' p =',p,' entry =',r)
    if r<2: continue
    n+=1
    ln=float(math.log(int(r))) if r.bit_length()<1000 else r.bit_length()*math.log(2)
    naive+=1/ln
    if P%(p+1)==0: exact+=1
    if not has_used_factor(r,p):
        nofac+=1; adj+=math.log(p)*math.exp(0.5772156649)/ln
    if is_prime(r,40): hits.append((p,len(str(r))))
print('entries tested',n,'| exact divisions',exact,'| entries with no used prime as a factor',nofac)
print('primes that chance predicts for ordinary numbers of the same sizes %.2f'%naive)
print('primes predicted after counting the exact divisions and the blocked small primes %.2f'%adj)
print('entries that passed the prime test (largest prime used, digit count):',hits)
P=mpz(1); s=0
print('Product of primes minus the total of the same primes (OEIS A355590):')
for p in primes[:12]:
    P*=p; s+=p; print(' p =',p,' entry =',P-s,' prime' if is_prime(P-s) else '')
