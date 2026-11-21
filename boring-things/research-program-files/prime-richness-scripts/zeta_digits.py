# Digits taken from the zeta sum 1/1^s + 1/2^s + 1/3^s and so on.
# Reading A: at position n take the first n decimal digits of the single piece 1/n^s.
# Reading B: at position n take the first n digits of the running total up to 1/n^s.
# Each number is tested for primes plain and with the last digit bumped. Needs gmpy2.
import math, time
from fractions import Fraction
from gmpy2 import mpz, is_prime, log
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
N=2000
def report(name,vals):
    for mode in ('plain','bump'):
        seen=set(); ex=0.0; where=[]
        for n,v in vals:
            if mode=='bump': v=bump(v)
            if v<2: continue
            ex+=chance(v)
            if v not in seen and is_prime(mpz(v),10): seen.add(v); where.append(n)
        print('%-44s %-5s primes %2d chance %5.2f %+5d%% positions %s'%(name,mode,len(seen),ex,round((len(seen)/ex-1)*100),where),flush=True)
for s in (1,2,3):
    report('piece 1/n^%d first n decimal digits'%s,[(n,10**n//n**s) for n in range(1,N+1)])
    tot=Fraction(0); vals=[]
    for n in range(1,N+1):
        tot+=Fraction(1,n**s)
        whole=len(str(tot.numerator//tot.denominator))
        vals.append((n,tot.numerator*10**(n-whole)//tot.denominator if n>=whole else tot.numerator//tot.denominator))
    report('running total for s = %d first n digits'%s,vals)
print('samples piece s=2:',[10**n//n**2 for n in range(1,9)])
tot=Fraction(0);sm=[]
for n in range(1,9):
    tot+=Fraction(1,n*n); sm.append(tot.numerator*10**(n-1)//tot.denominator)
print('samples total s=2:',sm)
