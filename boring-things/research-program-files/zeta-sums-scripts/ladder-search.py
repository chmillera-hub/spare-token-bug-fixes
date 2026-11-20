import sys, json, math
from mpmath import *
from flint import fmpz_mat
from fractions import Fraction
def mobius(n):
    r=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0: return 0
            r=-r
        p+=1
    if n>1: r=-r
    return r
POLY={
 "lehmer":[1,1,0,-1,-1,-1,-1,-1,0,1,1],"salem10b":[1,0,0,0,-1,-1,-1,0,0,0,1],"salem8":[1,0,0,-1,-1,-1,0,0,1],
 "salem6":[1,0,-1,-1,-1,0,1],"salem4":[1,-1,-1,-1,1],"golden":[1,1,-1],"plastic":[1,1,0,-1],
 "omega7":[1,2,-1,-1],"theta9":[1,0,-3,1],"supergold":[1,0,1,-1]}
name=sys.argv[1]; D=int(sys.argv[2]); K=int(sys.argv[3]); SMAX=int(sys.argv[4])
coef=POLY[name]
mp.dps=400
rts=polyroots(coef,maxsteps=2000,extraprec=2000)
real=[r.real for r in rts if abs(r.imag)<mpf(10)**-300 and 0<r.real<1]
x0=min(real) if name not in("omega7",) else max(real)
def phi_at(a,d):
    v=mpc(1)
    for e in range(1,d+1):
        if d%e==0:
            m=mobius(d//e)
            if m: v*=(a**e-1)**m
    return v
norms={}
for d in range(1,K+1):
    nrm=mpf(1)
    for a in rts: nrm*=phi_at(a,d)
    n=int(nint(abs(nrm)))
    norms[d]=n
def primes(n):
    out=set();p=2
    while p*p<=n and p<200000:
        while n%p==0: out.add(p); n//=p
        p+=1
    if n>1: out.add(n)
    return out
pf={d:primes(n) for d,n in norms.items()}
alive=set(norms)
while True:
    cnt={}
    for d in alive:
        for p in pf[d]: cnt[p]=cnt.get(p,0)+1
    drop={d for d in alive if any(cnt[p]<2 for p in pf[d])}
    if not drop: break
    alive-=drop
ds=sorted(alive)
print(name,"base",nstr(x0,12),"candidate cyclotomic indices",len(ds),ds,flush=True)
# weight-1 lattice
D1=max(300,30*(len(ds)+1))
mp.dps=D1+60
x=findroot(lambda t: polyval(coef,t), x0)
vals=[log(x)]+[log(abs(phi_at(x,d).real)) for d in ds]
n=len(vals); Kk=mpf(10)**D1
M=[[0]*(n+1) for _ in range(n)]
for i,v in enumerate(vals):
    M[i][i]=1; M[i][n]=int(nint(v*Kk))
R=fmpz_mat(M).lll()
E=[]
for i in range(n):
    row=[int(R[i,j]) for j in range(n)]
    res=abs(fsum(c*v for c,v in zip(row,vals)))
    if res<mpf(10)**(-(D1-30)) and max(map(abs,row))<10**6 and any(row[1:]): E.append(row)
print("weight-1 relations:",len(E),"max entry",max(max(map(abs,r)) for r in E),flush=True)
used=sorted({ds[j-1] for r in E for j in range(1,n) if r[j]})
print("cyclotomic indices used:",used,flush=True)
# c_k vectors
C=[]
for r in E:
    e={ds[j-1]:r[j] for j in range(1,n) if r[j]}
    c={}
    for d,ed in e.items():
        for k in range(1,d+1):
            if d%k==0:
                m=mobius(d//k)
                if m: c[k]=c.get(k,0)+m*ed
    C.append({k:v for k,v in c.items() if v})
ks=sorted({k for c in C for k in c})
print("powers needed:",len(ks),ks,flush=True)
mp.dps=D+120
x=findroot(lambda t: polyval(coef,t), x0); L=-log(x)
SMIN=int(sys.argv[5]) if len(sys.argv)>5 else 3
S=list(range(SMIN,SMAX+1,2)); eps=mpf(10)**(-(D+110)); F={}
for k in ks:
    y=x**k; t=mpf(1); acc=[mpf(0)]*len(S); nn=0
    while True:
        nn+=1; t*=y
        if t<eps: break
        w=mpf(nn); p=w**S[0]; q=w*w
        for i in range(len(S)):
            acc[i]+=t/p; p*=q
    for i,s in enumerate(S): F[(k,s)]=acc[i]
print("sums done",flush=True)
def lattice(vals):
    n=len(vals); Kk=mpf(10)**D
    M=[[0]*(n+1) for _ in range(n)]
    for i,v in enumerate(vals):
        M[i][i]=1; M[i][n]=int(nint(v*Kk))
    R=fmpz_mat(M).lll(); out=[]
    bound=10**int(D/(2.0*n))
    for i in range(n):
        row=[int(R[i,j]) for j in range(n)]
        res=abs(fsum(c*v for c,v in zip(row,vals)))
        if res<mpf(10)**(-(D-20)) and 0<max(map(abs,row))<bound: out.append(row)
    return out,int(D/(2.0*n))
def expand(row,off,s):
    # row over [zeta, (leftovers), Y_j...] -> integer coefficients on zeta, leftovers, F(x^k)
    co={}
    for j,c in enumerate(C):
        a=row[off+j]
        if a:
            for k,v in c.items(): co[k]=co.get(k,Fraction(0))+Fraction(a*v*SC[s],k**(s-1))
    return {k:v for k,v in co.items() if v}
res={}
SC={}
for s in S:
    lc=1
    for k in ks: lc=lc*k**(s-1)//math.gcd(lc,k**(s-1))
    SC[s]=1
    Y=[fsum(v*F[(k,s)]/mpf(k)**(s-1) for k,v in c.items()) for c in C]
    # rescale each Y_j by lcm of its own k^(s-1) so entries are integer combos
    scal=[]
    for c in C:
        l=1
        for k in c: l=l*k**(s-1)//math.gcd(l,k**(s-1))
        scal.append(l)
    scal=[1]*len(C)
    pure,b=lattice([zeta(s)]+Y)
    pz=[r for r in pure if r[0]]
    left=[pi**(2*j)*L**(s-2*j) for j in range(0,(s-1)//2+1)]
    full,b2=lattice([zeta(s)]+left+Y)
    fz=[r for r in full if r[0]]
    print("s=%d: with leftovers %d relations (%d with zeta) bound 1e%d | no leftovers %d relations (%d with zeta) bound 1e%d"%(s,len(full),len(fz),b2,len(pure),len(pz),b),flush=True)
    def tofk(row,off):
        co={}
        for j,c in enumerate(C):
            a=row[off+j]
            if a:
                for k,v in c.items(): co[k]=co.get(k,Fraction(0))+Fraction(a*v*scal[j],k**(s-1))
        den=1
        for v in co.values(): den=den*v.denominator//math.gcd(den,v.denominator)
        return den,{k:int(v*den) for k,v in co.items() if v}
    # exact elimination of leftover terms from the full relations
    def nullcombos(rows,ncols_off,ncols):
        A=[[Fraction(r[ncols_off+j]) for j in range(ncols)] for r in rows]
        m=len(rows); T=[[Fraction(int(i==j)) for j in range(m)] for i in range(m)]
        rk=0
        for col in range(ncols):
            piv=None
            for i in range(rk,m):
                if A[i][col]!=0: piv=i;break
            if piv is None: continue
            A[rk],A[piv]=A[piv],A[rk]; T[rk],T[piv]=T[piv],T[rk]
            for i in range(m):
                if i!=rk and A[i][col]!=0:
                    f=A[i][col]/A[rk][col]
                    A[i]=[a-f*b for a,b in zip(A[i],A[rk])]; T[i]=[a-f*b for a,b in zip(T[i],T[rk])]
            rk+=1
        return rk,T[rk:]
    rk,combos=nullcombos(full,1,len(left))
    elim=[]
    for t in combos:
        den=1
        for v in t: den=den*v.denominator//math.gcd(den,v.denominator)
        ti=[int(v*den) for v in t]
        row=[sum(a*r[i] for a,r in zip(ti,full)) for i in range(len(full[0]))]
        g=0
        for v in row: g=math.gcd(g,abs(v))
        row=[v//g for v in row]
        assert all(v==0 for v in row[1:1+len(left)])
        row=[row[0]]+row[1+len(left):]
        rr=abs(fsum(c*v for c,v in zip(row,[zeta(s)]+Y)))
        elim.append(row)
        print("   elimination gives a no-leftover relation: zeta coef digits %d residual %s"%(len(str(abs(row[0]))),nstr(rr,3)),flush=True)
    print("   leftover rank %d so exact count of no-leftover relations = %d (with zeta: %d)"%(rk,len(elim),sum(1 for r in elim if r[0])),flush=True)
    if not pz: pz=[r for r in elim if r[0]]
    out=[]
    for r in pz[:2]:
        den,co=tofk(r,1)
        g=math.gcd(r[0]*den, *co.values()) if co else 1
        out.append({"zeta":r[0]*den//g,"F":{str(k):v//g for k,v in co.items()}})
    outf=[]
    for r in fz[:1]:
        den,co=tofk(r,1+len(left))
        outf.append({"zeta":r[0]*den,"left":[c*den for c in r[1:1+len(left)]],"F":{str(k):v for k,v in co.items()}})
    res[s]={"npure":len(pure),"npurez":len(pz),"nfull":len(full),"pure":out,"full":outf,"nelim":len(elim)}
    if out: print("   simplest no-leftover formula: zeta coefficient",out[0]["zeta"],"terms",len(out[0]["F"]),"largest coefficient digits",len(str(max(map(abs,out[0]["F"].values())))),flush=True)
json.dump({"x":str(x)[:60],"ks":ks,"res":res},open("lad_%s_%d_%d.json"%(name,D,S[0]),"w"))
