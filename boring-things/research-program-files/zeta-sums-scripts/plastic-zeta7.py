from mpmath import *
from flint import fmpz_mat
D=2200; mp.dps=D+80
x=findroot(lambda t:t**3+t**2-1,0.75); L=-log(x)
ks=[1,2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,28,30,42]
def lattice(vals):
    n=len(vals); K=mpf(10)**D
    M=[[0]*(n+1) for _ in range(n)]
    for i,v in enumerate(vals):
        M[i][i]=1; M[i][n]=int(nint(v*K))
    R=fmpz_mat(M).lll(); out=[]
    for i in range(n):
        row=[int(R[i,j]) for j in range(n)]
        res=abs(fsum(c*v for c,v in zip(row,vals)))
        if res<mpf(10)**(-(D-15)) and 0<max(map(abs,row))<10**40: out.append(row)
    return out
def show(names,row):
    if row[0]<0: row=[-c for c in row]
    return "%d %s = "%(row[0],names[0])+" ".join("%+d %s"%(-c,n) for c,n in zip(row[1:],names[1:]) if c)
s=7
pv=[polylog(s,x**k) for k in ks]; pn=['F(x^%d)'%k for k in ks]
for nm,val in (('L^7',L**7),('pi^2 L^5',pi**2*L**5),('pi^4 L^3',pi**4*L**3),('pi^6 L',pi**6*L)):
    names=['zeta(7)',nm]+pn
    for r in lattice([zeta(7),val]+pv): print(show(names,r))
