# Invented recipes that mix digit tricks, bit tricks, prime lists, counting functions, geometry,
# step-by-step rules and fractions. A repeated prime counts once. Needs numpy, gmpy2 and mpmath.
import math, json, itertools
import numpy as np
from fractions import Fraction
from gmpy2 import mpz, is_prime, next_prime, log, gcd, isqrt, comb
import mpmath as mp
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
out=[]
def run(group,label,vals,note=''):
    seen=set(); ex=0.0; t=0
    for v in vals:
        v=abs(int(v)); t+=1
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),10): seen.add(v)
    pct=round((len(seen)/ex-1)*100) if ex>0 else -100
    out.append(dict(group=group,label=label,tested=t,primes=len(seen),expected=ex,pct=pct,note=note))
    print('%-66s tested %6d primes %6d chance %9.1f %+6d%%'%(label[:66],t,len(seen),ex,pct),flush=True)
N=300000
R=lambda f,M=N:(f(n) for n in range(1,M+1))
rev=lambda n:int(str(n)[::-1])
ds=lambda n:sum(map(int,str(n)))
CAP=10**300
def upto(gen):
    for v in gen:
        if abs(v)>CAP: return
        yield v
G='Digit tricks'
run(G,'n + (n written backward)',R(lambda n:n+rev(n)))
run(G,'n × (n written backward) + 1',R(lambda n:n*rev(n)+1))
run(G,'n written twice side by side',R(lambda n:int(str(n)*2)))
run(G,'n followed by n written backward',R(lambda n:int(str(n)+str(n)[::-1])))
run(G,'n followed by n written backward with the middle digit shared',R(lambda n:int(str(n)+str(n)[-2::-1])))
run(G,'n² written backward',R(lambda n:rev(n*n)))
run(G,'n written in base 2 and then read as a base 10 number',R(lambda n:int(bin(n)[2:])))
run(G,'n written in base 3 and then read as a base 10 number',R(lambda n:int(np.base_repr(n,3))))
run(G,'the digits of n read as a base 11 number',R(lambda n:int(str(n),11)))
run(G,'n × (the digit total of n) + 1',R(lambda n:n*ds(n)+1))
run(G,'n followed by n + 1',R(lambda n:int(str(n)+str(n+1))))
run(G,'the digit 1 then n then the digit 1',R(lambda n:int('1'+str(n)+'1')))
run(G,'n followed by the digit total of n',R(lambda n:int(str(n)+str(ds(n)))))
run(G,'n² + (the digit total of n)²',R(lambda n:n*n+ds(n)**2))
G='Bit tricks'
run(G,'n combined with half of n by the exclusive-or rule (Gray code)',R(lambda n:n^(n>>1)))
run(G,'the binary digits of n written backward',R(lambda n:int(bin(n)[:1:-1],2)))
run(G,'n² combined with n by the exclusive-or rule',R(lambda n:(n*n)^n))
run(G,'n + (2ⁿ mod n)',R(lambda n:n+pow(2,n,n)))
run(G,'n² + (2ⁿ mod n)',R(lambda n:n*n+pow(2,n,n)))
G='Mixed operations'
run(G,'(n × π with decimals dropped) × (n × e with decimals dropped) + 1',R(lambda n:int(n*math.pi)*int(n*math.e)+1))
run(G,'(n × √2 with decimals dropped)² + (n × √3 with decimals dropped)²',R(lambda n:int(isqrt(2*n*n))**2+int(isqrt(3*n*n))**2))
f41=lambda n:n*n+n+41
run(G,'n² + n + 41 fed back into itself',R(lambda n:f41(f41(n))))
def strip25(v):
    while v%2==0: v//=2
    while v%5==0: v//=5
    return v
run(G,'n² + 1 with every factor of 2 and 5 divided out',R(lambda n:strip25(n*n+1)))
M=100000; arr=np.arange(1,M+1,dtype=np.int64)**2+1; big=np.ones(M,dtype=np.int64)
def sieve(K):
    s=bytearray([1])*(K+1); s[0]=s[1]=0
    for i in range(2,int(K**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(K+1) if s[i]]
for p in sieve(M):
    if p!=2 and p%4!=1: continue
    while True:
        m=arr%p==0
        if not m.any(): break
        arr[m]//=p; big[m]=p
big=np.where(arr>1,arr,big)
run(G,'the largest prime that divides n² + 1',(int(x) for x in big),'100000 inputs and the recipe needs factoring')
run(G,'(2n choose n) + 1',upto((int(comb(2*n,n))+1 for n in itertools.count(1))),'outputs up to 300 digits')
run(G,'(2n choose n) − 1',upto((int(comb(2*n,n))-1 for n in itertools.count(1))),'outputs up to 300 digits')
def harm(s):
    t=Fraction(0)
    for n in itertools.count(1):
        t+=Fraction(1,n**s); yield t.numerator
run(G,'the top number of the fraction 1 + 1/2 + 1/3 up to 1/n',upto(harm(1)),'outputs up to 300 digits')
run(G,'the top number of the fraction 1 + 1/4 + 1/9 up to 1/n²',upto(harm(2)),'outputs up to 300 digits')
G='Recipes built from the list of primes'
P=[];p=mpz(2)
while len(P)<N+3: P.append(int(p)); p=next_prime(p)
need='the recipe needs the list of primes'
run(G,'the halfway point between the nth prime and the next prime',((P[i]+P[i+1])//2 for i in range(1,N+1)),need)
run(G,'the nth prime + the next prime + 1',(P[i]+P[i+1]+1 for i in range(N)),need)
run(G,'three neighboring primes added up',(P[i]+P[i+1]+P[i+2] for i in range(N)),need)
run(G,'n × the nth prime + 1',((i+1)*P[i]+1 for i in range(N)),need)
run(G,'the nth prime + n',(P[i]+i+1 for i in range(N)),need)
run(G,'the nth prime − n',(P[i]-i-1 for i in range(N)),need)
run(G,'(the nth prime)² + the nth prime + 41',(f41(P[i]) for i in range(N)),need)
run(G,'the nth prime written backward',(rev(P[i]) for i in range(N)),need)
sv=np.ones(N+1,bool); sv[:2]=False
for i in range(2,int(N**.5)+1):
    if sv[i]: sv[i*i::i]=False
pi=np.cumsum(sv)
run(G,'n + the count of primes up to n',R(lambda n:n+int(pi[n])),need)
run(G,'n × the count of primes up to n + 1',R(lambda n:n*int(pi[n])+1),need)
G='Counting functions'
phi=np.arange(N+1,dtype=np.int64)
for q in np.nonzero(sv)[0]: phi[q::q]-=phi[q::q]//q
sig=np.zeros(N+1,dtype=np.int64)
for d in range(1,N+1): sig[d::d]+=d
run(G,'n + the count of numbers below n that share no factor with n',R(lambda n:n+int(phi[n])))
run(G,'n × the count of numbers below n that share no factor with n + 1',R(lambda n:n*int(phi[n])+1))
run(G,'the total of the divisors of n then plus 1',R(lambda n:int(sig[n])+1))
run(G,'the total of the divisors of n then plus n',R(lambda n:int(sig[n])+n))
G='Geometry'
def circle(n):
    x=np.arange(1,n+1,dtype=np.int64); v=n*n-x*x; y=np.floor(np.sqrt(v.astype(np.float64))).astype(np.int64)
    y[(y+1)*(y+1)<=v]+=1; y[y*y>v]-=1
    return int(2*(2*y+1).sum()+2*n+1)
run(G,'the count of grid points inside a circle of radius n',(circle(n) for n in range(1,20001)),'20000 inputs tested')
run(G,'the most pieces from n straight cuts of a pizza',R(lambda n:(n*n+n+2)//2))
run(G,'the most pieces from n flat cuts of a cake',R(lambda n:(n**3+5*n+6)//6))
run(G,'the star numbers 6 × n × (n − 1) + 1',R(lambda n:6*n*(n-1)+1))
G='Step-by-step rules'
def steps(start,rule,M=N):
    a=start
    for n in range(1,M+1):
        a=rule(a,n); yield a
def smallest_nondivisor(a):
    q=2
    while a%q==0: q=int(next_prime(q))
    return q
run(G,'start at 1 and keep adding the digit total of the current number',steps(1,lambda a,n:a+ds(a)))
run(G,'start at 1 and keep adding the largest digit of the current number',steps(1,lambda a,n:a+int(max(str(a)))))
run(G,'start at 1 and keep adding the smallest prime that does not divide the current number',steps(1,lambda a,n:a+smallest_nondivisor(a)))
run(G,'start at 1 and keep adding the count of 1s in the binary form of the current number',steps(1,lambda a,n:a+bin(a).count('1')))
run(G,'start at 1 and keep adding the current number written backward',upto(steps(1,lambda a,n:a+rev(a),5000)),'outputs up to 300 digits')
mp.mp.dps=700
def conv(x):
    h0,h1=1,int(mp.floor(x)); k0,k1=0,1; yield h1
    for _ in range(560):
        x=1/(x-mp.floor(x)); a=int(mp.floor(x)); h0,h1=h1,a*h1+h0; yield h1
G='Best fractions'
run(G,'the top numbers of the best fractions for π (3 then 22 then 333 then 355 and so on)',upto(conv(mp.pi)),'outputs up to 300 digits')
run(G,'the top numbers of the best fractions for e',upto(conv(mp.e)),'outputs up to 300 digits')
run(G,'the top numbers of the best fractions for √2 (1 then 3 then 7 then 17 and so on)',upto(conv(mp.sqrt(2))),'outputs up to 300 digits')
json.dump(out,open('weird_results.json','w'),ensure_ascii=False,indent=1)
