from mpmath import *
from flint import fmpz_mat
D=1500
mp.dps=D+80
phi=(1+sqrt(5))/2; r=1/phi; l=log(phi)
C=[1,2,3,4,6,8,10,12,20,24]
def lattice(names,vals):
    n=len(vals); K=mpf(10)**D
    M=[[0]*(n+1) for _ in range(n)]
    for i,v in enumerate(vals):
        M[i][i]=1; M[i][n]=int(nint(v*K))
    R=fmpz_mat(M).lll(); out=[]
    for i in range(n):
        row=[int(R[i,j]) for j in range(n)]
        res=abs(fsum(c*v for c,v in zip(row,vals)))
        if res<mpf(10)**(-(D-10)) and max(map(abs,row))<10**40:
            out.append(row)
    return out
def show(names,row):
    if row[0]<0: row=[-c for c in row]
    lhs="%d %s"%(row[0],names[0]) if row[0] else "0"
    rhs=" ".join("%+d %s"%(-c,n) for c,n in zip(row[1:],names[1:]) if c)
    return lhs+" = "+rhs
def P(s): return ['F(r^%d)'%k for k in C],[polylog(s,r**k) for k in C]
for s,cs in ((3,[('zeta(3)',zeta(3))]),(3,[('pi^2 l',pi**2*l)]),(3,[('l^3',l**3)]),(3,[]),
             (5,[('zeta(5)',zeta(5)),('l^5',l**5)]),(5,[('zeta(5)',zeta(5)),('pi^2 l^3',pi**2*l**3)]),(5,[('zeta(5)',zeta(5)),('pi^4 l',pi**4*l)]),
             (5,[('pi^4 l',pi**4*l),('pi^2 l^3',pi**2*l**3)]),(5,[('l^5',l**5),('pi^2 l^3',pi**2*l**3)]),(5,[('l^5',l**5),('pi^4 l',pi**4*l)]),
             (7,[('zeta(7)',zeta(7)),('l^7',l**7),('pi^2 l^5',pi**2*l**5),('pi^4 l^3',pi**4*l**3)]),
             (7,[('zeta(7)',zeta(7)),('l^7',l**7),('pi^2 l^5',pi**2*l**5),('pi^6 l',pi**6*l)]),
             (7,[('zeta(7)',zeta(7)),('l^7',l**7),('pi^4 l^3',pi**4*l**3),('pi^6 l',pi**6*l)]),
             (7,[('zeta(7)',zeta(7)),('pi^2 l^5',pi**2*l**5),('pi^4 l^3',pi**4*l**3),('pi^6 l',pi**6*l)]),
             ):
    pn,pv=P(s)
    names=[c[0] for c in cs]+pn; vals=[c[1] for c in cs]+pv
    L=lattice(names,vals)
    print("s=%d consts=%s : %d relation(s)"%(s,[c[0] for c in cs],len(L)))
    for row in L: print("    ",show(names,row))
