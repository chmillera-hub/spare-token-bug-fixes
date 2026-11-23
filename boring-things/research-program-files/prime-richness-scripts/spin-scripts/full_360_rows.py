# Which rows of moves reach all 360 marks. Needs mpmath.
import math
from mpmath import mp
def cover(moves, limit=10**6):
    pos=0; seen=set(); k=0
    for m in moves:
        pos=(pos+m)%360; seen.add(pos); k+=1
        if len(seen)==360: return (360,k)
        if k>=limit: break
    return (len(seen),k)
def gen(f,N=200000):
    for n in range(1,N+1): yield f(n)
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
P=primes(3*10**6)
tests={
 'primes':P, 'primes squared':[p*p for p in P[:100000]], 'odd primes times 2':[2*p for p in P[1:100000]],
 'composites':[n for n in range(4,200000) if n not in set()][:0],
}
tests.pop('composites')
ps=set(P)
tests['composite numbers']=[n for n in range(4,300000) if n not in ps]
tests['twin prime first members']=[p for p in P if p+2 in ps]
tests['numbers with two prime pieces']=[n for n in range(4,300000) if sum(1 for _ in [0])][:0]
tests.pop('numbers with two prime pieces')
for name,f in (('fourth powers',lambda n:n**4),('fifth powers',lambda n:n**5),('n(n+1) pronic',lambda n:n*(n+1)),('triangular numbers',lambda n:n*(n+1)//2),
               ('n squared plus 1',lambda n:n*n+1),('n squared plus n plus 41',lambda n:n*n+n+41),('2n squared',lambda n:2*n*n),('powers of 7',lambda n:pow(7,n,360)),('powers of 11',lambda n:pow(11,n,360)),
               ('60n minus 29',lambda n:60*n-29),('n cubed plus n',lambda n:n**3+n),('floor of n times root 2',lambda n:math.isqrt(2*n*n)),('floor of n times the golden ratio',lambda n:int(n*(1+5**.5)/2)),
               ('floor of n ln n',lambda n:int(n*math.log(n))), ('number of divisors of n',lambda n:sum(1 for d in range(1,int(n**.5)+1) if n%d==0)*2-(1 if int(n**.5)**2==n else 0))):
    tests[name]=list(gen(f,60000))
mp.dps=60010
tests['digits of pi']=[int(ch) for ch in str(mp.pi)[2:60002]]
tests['digits of e']=[int(ch) for ch in str(mp.e)[2:60002]]
tests['digits of root 2']=[int(ch) for ch in str(mp.sqrt(2))[2:60002]]
for name,mv in tests.items():
    print(name, cover(mv), mv[:8])
# arithmetic rows a, a+d, a+2d: smallest d with a full score
best=[]
for d in range(1,361):
    for a in range(1,361):
        r=cover((a+d*(n-1) for n in range(1,721)))
        if r[0]==360: best.append((d,a,r[1])); break
print('arithmetic rows with a full score: smallest steps d and first a:',best[:8], len(best))
