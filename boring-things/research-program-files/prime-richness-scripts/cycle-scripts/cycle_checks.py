# Small checks behind cycle-questions.md in the prime-richness folder.
from fractions import Fraction as F
from math import pi
# 1. cycle length of each digit position (from the right) for six polynomials
polys={'x squared':lambda x:x*x,'x cubed':lambda x:x**3,'x squared minus x plus 1':lambda x:x*x-x+1,'2 x squared minus 1':lambda x:2*x*x-1,'x to the power 4':lambda x:x**4,'x squared plus x plus 41':lambda x:x*x+x+41}
def period(seq):
    n=len(seq)//2
    for p in range(1,n+1):
        if all(seq[i]==seq[i+p] for i in range(n)): return p
for name,f in polys.items():
    out=[]
    for k in (1,2,3,4):
        m=10**k;out.append(period([(f(x)//(m//10))%10 for x in range(1,2*m+1)]))
    print(name,'cycle of the digit in place 1 2 3 4 from the right:',out,'| different two digit endings:',len(set(f(x)%100 for x in range(1,201))))
lead=[int(str(x*x)[0]) for x in range(1,2001)];runs=[];r=1
for i in range(1,len(lead)):
    if lead[i]==lead[i-1]: r+=1
    else: runs.append((lead[i-1],r));r=1
print('runs of the first digit of x squared:',runs[:30])
# 2. first composite value of prime rich polynomials
def isp(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def fac(n):
    f=[];i=2
    while i*i<=n:
        while n%i==0: f.append(i);n//=i
        i+=1
    if n>1: f.append(n)
    return f
for c in (2,3,5,11,17,41):
    x=0
    while isp(x*x+x+c): x+=1
    print('x squared + x + %d: first composite at x = %d is %d = %s'%(c,x,x*x+x+c,fac(x*x+x+c)))
for c in (3,5,11,29):
    x=0
    while isp(2*x*x+c): x+=1
    print('2 x squared + %d: first composite at x = %d is %d = %s'%(c,x,2*x*x+c,fac(2*x*x+c)))
# 3. numbers each prime is the first to cross off and the share up to a million
N=1000000
spf=list(range(N+1))
for i in range(2,int(N**.5)+1):
    if spf[i]==i:
        for k in range(i*i,N+1,i):
            if spf[k]==k: spf[k]=i
for p in (2,3,5,7,11,13,17,19,23,29,97,101,997):
    own=[n for n in range(p*p,min(N,p*p*40)+1) if spf[n]==p][:8]
    cnt=sum(1 for n in range(2,N+1) if spf[n]==p and n!=p)
    print(p,'first numbers',own,'| share below a million %.3f%%'%(100*cnt/N))
sf=bytearray([1])*(N+1);i=2
while i*i<=N:
    for k in range(i*i,N+1,i*i): sf[k]=0
    i+=1
print('share of numbers up to a million not divisible by any prime squared: %.5f and 6/pi^2 = %.5f'%(sum(sf[1:])/N,6/pi**2))
# 4. the polynomial through the first n primes and what the polynomial gives next
P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def interp(pts):
    n=len(pts);xs=list(range(1,n+1));c=[F(v) for v in pts]
    for j in range(1,n):
        for i in range(n-1,j-1,-1): c[i]=(c[i]-c[i-1])/(xs[i]-xs[i-j])
    def ev(x):
        r=F(0)
        for i in range(n-1,-1,-1): r=r*(x-xs[i])+c[i]
        return r
    return ev
for n in (3,5,10,15):
    ev=interp(P[:n]);print(n,'primes matched:',[int(ev(x)) for x in range(1,n+1)]==P[:n],'| next three outputs:',[str(ev(x)) for x in range(n+1,n+4)])
