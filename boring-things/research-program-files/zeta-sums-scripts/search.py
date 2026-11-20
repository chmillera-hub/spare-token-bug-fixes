from mpmath import *
from flint import fmpz_mat
import itertools, sys
def lattice(vals, D):
    n=len(vals); K=mpf(10)**D
    M=[[0]*(n+1) for _ in range(n)]
    for i,v in enumerate(vals):
        M[i][i]=1; M[i][n]=int(nint(v*K))
    R=fmpz_mat(M).lll()
    out=[]
    for i in range(n):
        row=[int(R[i,j]) for j in range(n+1)]
        mx=max(abs(c) for c in row[:n])
        res=abs(fsum(c*v for c,v in zip(row[:n],vals)))
        if mx>0 and res < mpf(10)**(-(D-10)) and mx < 10**int(D/(2.0*n)):
            out.append((row[:n],mx))
    return out
def consts(s,mode):
    phi=(1+sqrt(5))/2; l=log(phi)
    out=[('zeta(%d)'%s,zeta(s))]
    if mode>=1:
        for j in range(0,(s-1)//2+1): out.append(('pi^%d l^%d'%(2*j,s-2*j),pi**(2*j)*l**(s-2*j)))
    if mode>=2:
        # products zeta(m)*pi^(2a)*l^b , m odd 3..s-2, plus zeta(3)^2*..., weight s
        for m in range(3,s-1,2):
            w=s-m
            for a in range(0,w//2+1):
                b=w-2*a
                out.append(('zeta(%d) pi^%d l^%d'%(m,2*a,b),zeta(m)*pi**(2*a)*l**b))
        if s>=7:
            w=s-6
            for a in range(0,w//2+1):
                out.append(('zeta(3)^2 pi^%d l^%d'%(2*a,w-2*a),zeta(3)**2*pi**(2*a)*l**(w-2*a)))
        if s>=9:
            out.append(('zeta(3)^3',zeta(3)**3))
            out.append(('zeta(3) zeta(5) l',zeta(3)*zeta(5)*l))
    return out
D=int(sys.argv[1]); 
C=[1,2,3,4,6,8,10,12,20,24]
sets={"C":C,"1..40":list(range(1,41)),"1..24+30,36,40,48,60":list(range(1,25))+[30,36,40,48,60]}
for s in (3,5,7,9):
    for mode in (0,1,2):
        for lab,ks in sets.items():
            mp.dps=D+80
            phi=(1+sqrt(5))/2; r=1/phi
            cs=consts(s,mode)
            names=[c[0] for c in cs]+['F(r^%d)'%k for k in ks]
            vals=[c[1] for c in cs]+[polylog(s,r**k) for k in ks]
            L=lattice(vals,D)
            nz=sum(1 for R,mx in L if R[0]!=0)
            used=sorted({names[i] for R,mx in L for i,c in enumerate(R) if c})
            print("s=%d consts=%d(mode%d) ks=%s n=%d: relations=%d (zeta nonzero in %d) maxcoef=%s bound=1e%d"%(s,len(cs),mode,lab,len(vals),len(L),nz,max([mx for R,mx in L],default=0),int(D/(2.0*len(vals)))),flush=True)
            if L and lab!="C": print("    terms used:",used)
