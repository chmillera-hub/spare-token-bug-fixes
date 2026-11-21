# Adds up 1 divided by each Fibonacci prime. Needs gmpy2 and mpmath. Run: python3 fib_prime_sum.py
from gmpy2 import mpz, is_prime
import mpmath as mp
mp.mp.dps=60
a,b=mpz(0),mpz(1); total=mp.mpf(0); found=[]
for n in range(1,3001):
    a,b=b,a+b            # a is the nth Fibonacci number
    if a>1 and is_prime(a,30):
        found.append(n); total+=mp.mpf(1)/mp.mpf(int(a))
print('positions of the Fibonacci primes up to position 3000:',found)
print('sum of 1 over each Fibonacci prime:',mp.nstr(total,45))
