# Prime rate of (n to a power) divided by k with the decimal places dropped, compared with the number line.
# Needs gmpy2. Run: python3 divide_table.py
import math, random
from gmpy2 import mpz, is_prime
random.seed(3)
L=10**12
def rate(f,nmax):
    ns=range(2,nmax+1) if nmax<=300000 else (random.randrange(2,nmax+1) for _ in range(300000))
    pr=0; ex=0.0
    for n in ns:
        v=f(n)
        if v<3: continue
        ex+=1/math.log(v)
        if is_prime(mpz(v),15): pr+=1
    return pr,ex
for power in (2,3):
    for k in range(2,21):
        nmax=int(round((L*k)**(1/power)))-2
        pr,ex=rate(lambda n:n**power//k,nmax)
        print('n^%d / %2d : %6d primes where chance predicts %7.0f : %+4d%%'%(power,k,pr,ex,round((pr/ex-1)*100)))
