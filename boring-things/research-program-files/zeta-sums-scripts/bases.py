from mpmath import *
from flint import fmpz_mat
import sys
D=int(sys.argv[1]); which=sys.argv[2]; KMAX=int(sys.argv[3])
mp.dps=D+100
BASES={"half":(mpf(1)/2,"1/2"),"third":(mpf(1)/3,"1/3"),"silver":(sqrt(2)-1,"sqrt(2)-1"),"r23":(2-sqrt(3),"2-sqrt(3)"),"golden":((sqrt(5)-1)/2,"1/phi")}
def root(coef,guess): return findroot(lambda t: polyval(coef,t),guess)
BASES.update({
 "omega7":(root([1,2,-1,-1],0.8),"root of x^3+2x^2-x-1 near 0.802"),
 "theta9":(root([1,0,-3,1],0.35),"root of x^3-3x+1 near 0.347"),
 "plastic":(root([1,1,0,-1],0.75),"root of x^3+x^2-1 near 0.755"),
 "supergold":(root([1,0,1,-1],0.68),"root of x^3+x-1 near 0.682"),
 "tribo":(root([1,1,1,-1],0.54),"root of x^3+x^2+x-1 near 0.544"),
 "pisot4":(root([1,0,0,1,-1],0.72),"root of x^4+x-1 near 0.724"),
 "pisot5":(root([1,0,-1,1,1,-1],0.69),"root of x^5-x^3+x^2+x-1 near 0.693"),
 "pisot6":(root([1,0,-1,0,1,1,-1],0.67),"root of x^6-x^4+x^2+x-1 near 0.666"),
 "pisot5b":(root([1,1,1,1,0,-1],0.65),"root of x^5+x^4+x^3+x^2-1 near 0.652"),
 "r13":((sqrt(13)-3)/2,"(sqrt(13)-3)/2"),
 "r15":(4-sqrt(15),"4-sqrt(15)"),
 "r6":(5-2*sqrt(6),"5-2sqrt(6)"),
 "r7":(8-3*sqrt(7),"8-3sqrt(7)"),
 "fifth":(mpf(1)/5,"1/5"),"seventh":(mpf(1)/7,"1/7"),
 "r17":(sqrt(17)-4,"sqrt(17)-4"),
 "r3m1":((sqrt(3)-1)/2,"(sqrt(3)-1)/2"),
 "r21":((5-sqrt(21))/2,"(5-sqrt(21))/2"),
})
x,label=BASES[which]; L=-log(x)
def lattice(vals):
    n=len(vals); K=mpf(10)**D
    M=[[0]*(n+1) for _ in range(n)]
    for i,v in enumerate(vals):
        M[i][i]=1; M[i][n]=int(nint(v*K))
    R=fmpz_mat(M).lll(); out=[]
    bound=10**int(D/(2.0*n))
    for i in range(n):
        row=[int(R[i,j]) for j in range(n)]
        res=abs(fsum(c*v for c,v in zip(row,vals)))
        if res<mpf(10)**(-(D-15)) and 0<max(map(abs,row))<bound: out.append(row)
    return out,int(D/(2.0*n))
def consts(s,mode):
    out=[('zeta(%d)'%s,zeta(s))]
    for j in range(0,(s-1)//2+1): out.append(('pi^%d L^%d'%(2*j,s-2*j),pi**(2*j)*L**(s-2*j)))
    if mode==2:
        for m in range(3,s-1,2):
            w=s-m
            for a in range(0,w//2+1): out.append(('zeta(%d) pi^%d L^%d'%(m,2*a,w-2*a),zeta(m)*pi**(2*a)*L**(w-2*a)))
        if s>=7:
            w=s-6
            for a in range(0,w//2+1): out.append(('zeta(3)^2 pi^%d L^%d'%(2*a,w-2*a),zeta(3)**2*pi**(2*a)*L**(w-2*a)))
    return out
def show(names,row):
    return " ".join("%+d*%s"%(c,n) for c,n in zip(row,names) if c)
ks=list(range(1,KMAX+1))
for s in (3,5,7,9,11):
    pv=[polylog(s,x**k) for k in ks]; pn=['F(x^%d)'%k for k in ks]
    # pure
    cs=[('zeta(%d)'%s,zeta(s))]
    rel,b=lattice([c[1] for c in cs]+pv)
    nz=[r for r in rel if r[0]]
    print("BASE %s s=%d PURE: relations=%d zeta-nonzero=%d bound=1e%d"%(label,s,len(rel),len(nz),b),flush=True)
    for r in rel[:4]: print("     ",show([c[0] for c in cs]+pn,r),flush=True)
    for mode in ((1,2) if s<=7 else (1,)):
        cs=consts(s,mode)
        rel,b=lattice([c[1] for c in cs]+pv)
        nz=[r for r in rel if r[0]]
        names=[c[0] for c in cs]+pn
        used=sorted({names[i] for r in rel for i,c in enumerate(r) if c and i>=len(cs)},key=lambda t:int(t[4:-1]))
        usedc=sorted({names[i] for r in rel for i,c in enumerate(r) if c and i<len(cs)})
        print("BASE %s s=%d mode%d: relations=%d zeta-nonzero=%d maxcoef=%s bound=1e%d powers=%s consts=%s"%(label,s,mode,len(rel),len(nz),max([max(map(abs,r)) for r in rel],default=0),b,[u[4:-1] for u in used],usedc),flush=True)
        if mode==1:
            for r in rel[:6]: print("     ",show(names,r),flush=True)
