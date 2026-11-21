# Recipes that give no primes (or almost none) retested with the last digit of each output bumped.
import math, random, json, itertools
from gmpy2 import mpz, is_prime, log, next_prime
random.seed(5)
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
def rate(vals,b):
    seen=set(); ex=0.0; t=0
    for v in vals:
        v=abs(int(v)); t+=1
        if b: v=bump(v)
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),5): seen.add(v)
    return t,len(seen),ex
out=[]
def run(label,make,note=''):
    a=rate(make(),False); b=rate(make(),True)
    p0=round((a[1]/a[2]-1)*100) if a[2] else -100; p1=round((b[1]/b[2]-1)*100) if b[2] else -100
    out.append(dict(label=label,tested=a[0],plain=p0,bump=p1,primes_plain=a[1],primes_bump=b[1],chance=b[2],note=note))
    print('%-52s tested %6d | plain %+5d%% (%d) | bumped %+5d%% (%d of chance %.1f)'%(label[:52],a[0],p0,a[1],p1,b[1],b[2]),flush=True)
N=300000
R=lambda f,M=N:(lambda:(f(n) for n in range(1,M+1)))
rev=lambda n:int(str(n)[::-1])
P=[];p=mpz(2)
while len(P)<N+2: P.append(int(p)); p=next_prime(p)
def pairs(f,X):
    def g():
        rr=random.Random(9)
        for _ in range(N): yield f(rr.randrange(1,X+1),rr.randrange(1,X+1))
    return g
run('2n',R(lambda n:2*n))
run('6n + 3',R(lambda n:6*n+3))
run('3n²',R(lambda n:3*n*n))
run('n² − 1',R(lambda n:n*n-1))
run('n² + n + 2',R(lambda n:n*n+n+2))
run('n⁴ + 4',R(lambda n:n**4+4))
run('n⁴ + n² + 1',R(lambda n:n**4+n*n+1))
run('n⁶ + 1',R(lambda n:n**6+1))
run('n¹² + 488669',R(lambda n:n**12+488669))
run('n⁶ + 1091',R(lambda n:n**6+1091))
for k in (2,3,4,5,8,12,16): run('n² ÷ %d with decimals dropped'%k,R(lambda n,k=k:n*n//k))
run('n³ ÷ 9 with decimals dropped',R(lambda n:n**3//9))
run('n × (n + 1) ÷ 2 (the totals of 1 + 2 + 3)',R(lambda n:n*(n+1)//2))
run('the totals of 1² + 2² + 3²',R(lambda n:n*(n+1)*(2*n+1)//6))
run('the most pieces from n flat cuts of a cake',R(lambda n:(n**3+5*n+6)//6))
run('n written twice side by side',R(lambda n:int(str(n)*2)))
run('n followed by n written backward',R(lambda n:int(str(n)+str(n)[::-1])))
run('n + (n written backward)',R(lambda n:n+rev(n)))
run('n² combined with n by the exclusive-or rule',R(lambda n:(n*n)^n))
run('n² + (n mod 6)',R(lambda n:n*n+n%6))
run('the halfway point between the nth prime and the next prime',lambda:((P[i]+P[i+1])//2 for i in range(1,N+1)))
run('x × y',pairs(lambda x,y:x*y,10**6))
run('x³ + y³',pairs(lambda x,y:x**3+y**3,10**4))
run('x⁴ + x² × y² + y⁴',pairs(lambda x,y:x**4+x*x*y*y+y**4,1000))
run('x² + y² + x + y',pairs(lambda x,y:x*x+y*y+x+y,10**6))
CAP=10**300
def upto(f):
    def g():
        for n in itertools.count(1):
            v=f(n)
            if v>CAP: return
            yield v
    return g
run('78557 × 2ⁿ + 1',upto(lambda n:78557*2**n+1),'outputs up to 300 digits')
run('509203 × 2ⁿ − 1',upto(lambda n:509203*2**n-1),'outputs up to 300 digits')
run('2ⁿ ÷ 3 with decimals dropped',upto(lambda n:2**n//3),'outputs up to 300 digits')
def cat():
    s=''
    for n in itertools.count(1):
        s+=str(n)
        if len(s)>300: return
        yield int(s)
run('the whole numbers written side by side',cat,'outputs up to 300 digits')
json.dump(out,open('dead_bump_results.json','w'),ensure_ascii=False,indent=1)
