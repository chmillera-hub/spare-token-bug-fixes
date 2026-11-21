import math, random, json, time
import gmpy2
from gmpy2 import mpz, isqrt, is_prime
import mpmath as mp
mp.mp.dps=60
random.seed(7)
L12=10**12
PHI=(1+mp.sqrt(5))/2; PI=mp.pi; E=mp.e
def fl(x): return int(mp.floor(x))
def safe(fun_float, fun_mp):
    # exact floor: use float fast path, fall back to mpmath when near an integer
    def f(n):
        x=fun_float(n)
        fr=x-math.floor(x)
        if x<1e11 and 1e-3<fr<1-1e-3: return int(math.floor(x))
        return fl(fun_mp(n))
    return f
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
F=[]  # (group, label, func, mode, note)
def add(g,label,f,note='',mode='poly'): F.append((g,label,f,mode,note))
G1='Straight-line equations'
add(G1,'n',lambda n:n,'the plain number line used as the baseline')
add(G1,'2n',lambda n:2*n,'every output is even')
add(G1,'2n + 1',lambda n:2*n+1,'every output is odd so the prime 2 never divides an output')
add(G1,'4n + 3',lambda n:4*n+3,'every output is odd so the prime 2 never divides an output')
add(G1,'6n + 1',lambda n:6*n+1,'the primes 2 and 3 never divide an output')
add(G1,'6n + 3',lambda n:6*n+3,'every output is a multiple of 3')
add(G1,'10n + 1',lambda n:10*n+1,'the primes 2 and 5 never divide an output')
add(G1,'30n + 1',lambda n:30*n+1,'the primes 2 and 3 and 5 never divide an output')
add(G1,'210n + 1',lambda n:210*n+1,'the primes 2 and 3 and 5 and 7 never divide an output')
G2='Squared equations'
add(G2,'n² + 1',lambda n:n*n+1,'2 divides every second output and 5 divides two of every five outputs')
add(G2,'n² + n + 1',lambda n:n*n+n+1,'every output is odd')
add(G2,'n² − n − 1',lambda n:n*n-n-1,'the golden ratio equation where 2 and every prime ending in 3 or 7 never divide an output')
add(G2,'n² − 2',lambda n:n*n-2,'')
add(G2,'n² + 3',lambda n:n*n+3,'')
add(G2,'2n² − 1',lambda n:2*n*n-1,'every output is odd')
add(G2,'4n² + 1',lambda n:4*n*n+1,'every output is odd and 3 never divides an output')
add(G2,'3n² + 3n + 1',lambda n:3*n*n+3*n+1,'the gap between two neighboring cubes where 2 and 3 and 5 never divide an output')
add(G2,'n² + n + 17',lambda n:n*n+n+17,'no prime below 17 ever divides an output')
add(G2,'2n² + 29',lambda n:2*n*n+29,'no prime below 29 ever divides an output')
add(G2,'n² + n + 41',lambda n:n*n+n+41,'no prime below 41 ever divides an output')
add(G2,'n² − 79n + 1601',lambda n:n*n-79*n+1601,'the same outputs as n² + n + 41 with the inputs shifted by 40')
add(G2,'n² − 1',lambda n:n*n-1,'the equation splits into (n − 1) × (n + 1)')
add(G2,'n² + n + 2',lambda n:n*n+n+2,'every output is even')
add(G2,'n² + 5n + 6',lambda n:n*n+5*n+6,'the equation splits into (n + 2) × (n + 3)')
G3='Cubes and higher powers'
add(G3,'n³ + 2',lambda n:n**3+2,'')
add(G3,'n³ + n + 1',lambda n:n**3+n+1,'every output is odd')
add(G3,'n³ + n² + 1',lambda n:n**3+n*n+1,'every output is odd')
add(G3,'n³ − n + 1',lambda n:n**3-n+1,'2 and 3 never divide an output')
add(G3,'n⁴ + 1',lambda n:n**4+1,'')
add(G3,'n⁴ + n + 1',lambda n:n**4+n+1,'every output is odd')
add(G3,'n⁵ + 2',lambda n:n**5+2,'')
add(G3,'n⁴ + 4',lambda n:n**4+4,'the equation secretly splits into (n² + 2n + 2) × (n² − 2n + 2)')
add(G3,'n⁴ + n² + 1',lambda n:n**4+n*n+1,'the equation secretly splits into (n² + n + 1) × (n² − n + 1)')
add(G3,'n⁶ + 1',lambda n:n**6+1,'the equation secretly splits into (n² + 1) × (n⁴ − n² + 1)')
G4='Division with the decimal places dropped'
add(G4,'n ÷ 2',lambda n:n//2,'each whole number shows up twice in a row so the outputs are the plain number line repeated')
add(G4,'n² ÷ 2',lambda n:n*n//2,'')
add(G4,'n² ÷ 3',lambda n:n*n//3,'')
add(G4,'n² ÷ 4',lambda n:n*n//4,'for even n the output is a perfect square and for odd n the output is two neighboring numbers multiplied')
add(G4,'n² ÷ 5',lambda n:n*n//5,'')
add(G4,'n² ÷ 7',lambda n:n*n//7,'')
add(G4,'n² ÷ 10',lambda n:n*n//10,'')
add(G4,'(n² + 1) ÷ 3',lambda n:(n*n+1)//3,'')
add(G4,'n³ ÷ 2',lambda n:n**3//2,'')
add(G4,'n³ ÷ 7',lambda n:n**3//7,'')
add(G4,'n × (n + 1) ÷ 2',lambda n:n*(n+1)//2,'the division is always exact and the output is two numbers multiplied')
add(G4,'n² ÷ (n + 1)',lambda n:n*n//(n+1),'dropping the decimals always leaves n − 1 so the outputs are the plain number line')
add(G4,'n³ ÷ (n + 1)',lambda n:n**3//(n+1),'dropping the decimals always leaves n² − n which is always even')
add(G4,'(n³ + 5) ÷ (n + 1)',lambda n:(n**3+5)//(n+1),'')
add(G4,'n⁴ ÷ (n² + 1)',lambda n:n**4//(n*n+1),'dropping the decimals always leaves n² − 1 which splits into (n − 1) × (n + 1)')
G5='Square roots and special multipliers with the decimal places dropped'
add(G5,'n × √2',lambda n:int(isqrt(mpz(2*n*n))),'')
add(G5,'n × φ (the golden ratio)',lambda n:int((n+isqrt(mpz(5*n*n)))//2),'')
add(G5,'n × π',safe(lambda n:n*math.pi,lambda n:n*PI),'')
add(G5,'n × e',safe(lambda n:n*math.e,lambda n:n*E),'')
add(G5,'n² × √2',lambda n:int(isqrt(mpz(2*n**4))),'')
add(G5,'n² × φ (the golden ratio)',lambda n:int((n*n+isqrt(mpz(5*n**4)))//2),'')
add(G5,'n² × π',safe(lambda n:n*n*math.pi,lambda n:n*n*PI),'')
add(G5,'n to the power 1.5',lambda n:int(isqrt(mpz(n**3))),'')
add(G5,'n to the power 2.5',lambda n:int(isqrt(mpz(n**5))),'')
add(G5,'√n',lambda n:int(isqrt(mpz(n))),'each whole number repeats many times in a row so the outputs are the plain number line repeated')
G6='Logarithms with the decimal places dropped'
add(G6,'n × ln(n)',safe(lambda n:n*math.log(n),lambda n:n*mp.log(n)),'the output is close to the size of the nth prime number')
add(G6,'n × log₂(n)',safe(lambda n:n*math.log2(n),lambda n:n*mp.log(n,2)),'')
add(G6,'n × log₁₀(n)',safe(lambda n:n*math.log10(n),lambda n:n*mp.log10(n)),'')
add(G6,'n × ln(n) × ln(n)',safe(lambda n:n*math.log(n)**2,lambda n:n*mp.log(n)**2),'')
add(G6,'n² × ln(n)',safe(lambda n:n*n*math.log(n),lambda n:n*n*mp.log(n)),'')
add(G6,'n² ÷ ln(n)',safe(lambda n:n*n/math.log(n),lambda n:n*n/mp.log(n)),'')
add(G6,'n ÷ ln(n)',safe(lambda n:n/math.log(n),lambda n:n/mp.log(n)),'the output is close to the count of primes below n')
G7='Fast-growing equations (tested on outputs up to 300 digits)'
E300=10**300
add(G7,'2ⁿ − 1',lambda n:2**n-1,'the output can be prime only when n is prime','exp')
add(G7,'2ⁿ + 1',lambda n:2**n+1,'the output can be prime only when n is a power of 2 and the known primes stop at n = 16','exp')
add(G7,'2ⁿ + 3',lambda n:2**n+3,'','exp')
add(G7,'2ⁿ − 3',lambda n:2**n-3,'','exp')
add(G7,'2ⁿ + n',lambda n:2**n+n,'','exp')
add(G7,'3ⁿ − 2',lambda n:3**n-2,'','exp')
add(G7,'3ⁿ + 2',lambda n:3**n+2,'','exp')
add(G7,'10ⁿ + 1',lambda n:10**n+1,'','exp')
add(G7,'10ⁿ + 7',lambda n:10**n+7,'','exp')
add(G7,'n × 2ⁿ + 1',lambda n:n*2**n+1,'','exp')
add(G7,'n! + 1 (1 × 2 × 3 up to n then add 1)',lambda n:math.factorial(n)+1,'no prime up to n divides the output','exp')
add(G7,'n! − 1',lambda n:math.factorial(n)-1,'no prime up to n divides the output','exp')
add(G7,'nⁿ + 1',lambda n:n**n+1,'','exp')
add(G7,'the nth Fibonacci number',fib,'the output can be prime only when n is prime or n = 4','exp')
add(G7,'1.5ⁿ with decimals dropped',lambda n:3**n//2**n,'','exp')
add(G7,'φⁿ with decimals dropped',lambda n:fl(PHI**n),'','exp')
add(G7,'eⁿ with decimals dropped',lambda n:fl(E**n),'','exp')
add(G7,'πⁿ with decimals dropped',lambda n:fl(PI**n),'','exp')
add(G7,'2ⁿ ÷ n with decimals dropped',lambda n:2**n//n,'','exp')
add(G7,'2ⁿ ÷ 3 with decimals dropped',lambda n:2**n//3,'for odd n the output is even and for even n the output splits into two factors','exp')
def lnv(v):
    return math.log(v) if v<10**300 else float(mp.log(v))
out=[]
for g,label,f,mode,note in F:
    t=time.time()
    if mode=='exp':
        mp.mp.dps=400
        tested=primes=0;exp=0.0;n=1
        while True:
            v=f(n)
            if v>E300: break
            n+=1
            if v<3:
                continue
            tested+=1;exp+=1/lnv(v)
            if is_prime(mpz(v),25): primes+=1
        how='every input whose output has 300 digits or fewer'
        mp.mp.dps=60
    else:
        # largest input with output <= 10^12
        hi=2
        while f(hi)<=L12: hi*=2
        lo=hi//2
        while hi-lo>1:
            m=(lo+hi)//2
            if f(m)<=L12: lo=m
            else: hi=m
        nmax=lo
        if nmax<=300000:
            ns=range(2,nmax+1); how='every input whose output stays under 1 trillion'
        else:
            ns=(random.randrange(2,nmax+1) for _ in range(300000)); how='300000 random inputs whose outputs stay under 1 trillion'
        tested=primes=0;exp=0.0
        for n in ns:
            v=f(n)
            if v<3: continue
            tested+=1;exp+=1/math.log(v)
            if is_prime(mpz(v),15): primes+=1
    score=primes/exp if exp>0 else 0
    out.append(dict(group=g,label=label,note=note,tested=tested,primes=primes,expected=exp,score=score,how=how))
    print(f'{label:38s} tested {tested:7d} primes {primes:6d} exp {exp:9.1f} score {score:6.3f} pct {round((score-1)*100):+5d}%  {time.time()-t:.1f}s',flush=True)
json.dump(out,open('results.json','w'),ensure_ascii=False,indent=1)
