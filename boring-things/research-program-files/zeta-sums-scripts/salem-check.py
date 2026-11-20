import json,sys
from mpmath import *
mp.dps=330
POLY={"salem4":[1,-1,-1,-1,1],"salem6":[1,0,-1,-1,-1,0,1],"salem8":[1,0,0,-1,-1,-1,0,0,1]}
def base(name):
    c=POLY[name]; r=[t.real for t in polyroots(c,maxsteps=2000,extraprec=1500) if abs(t.imag)<mpf(10)**-200 and 0<t.real<1]
    return min(r)
def fmt_pure(A,F,s):
    sg=1 if A>0 else -1
    parts=[]
    for k in sorted(F,key=int):
        c=-sg*F[k]; nm="F(x^%s)"%k if k!="1" else "F(x)"
        parts.append(("+ " if c>0 else "- ")+("%d × "%abs(c) if abs(c)!=1 else "")+nm)
    rhs=" ".join(parts); rhs=rhs[2:] if rhs.startswith("+ ") else "-"+rhs[2:]
    return ("%d × "%abs(A) if abs(A)!=1 else "")+"zeta(%d) = "%s+rhs
def fmt_full(A,left,F,s):
    sg=1 if A>0 else -1
    parts=[]
    for j,c in enumerate(left):
        c=-sg*c
        if c:
            p,q=2*j,s-2*j
            nm=("L^%d"%q if q>1 else "L") if p==0 else ("pi^%d × "%p+("L^%d"%q if q>1 else "L"))
            parts.append(("+ " if c>0 else "- ")+"%d × "%abs(c)+nm)
    for k in sorted(F,key=int):
        c=-sg*F[k]; nm="F(x^%s)"%k if k!="1" else "F(x)"
        parts.append(("+ " if c>0 else "- ")+("%d × "%abs(c) if abs(c)!=1 else "")+nm)
    rhs=" ".join(parts); rhs=rhs[2:] if rhs.startswith("+ ") else "-"+rhs[2:]
    return "%d × zeta(%d) = "%(abs(A),s)+rhs
out={}
for name,fn in (("salem4","lad_salem4.json"),("salem6","lad_salem6.json"),("salem8","lad_salem8.json")):
    J=json.load(open(fn)); x=base(name); L=-log(x)
    for s_,R in J["res"].items():
        s=int(s_)
        if R["pure"]:
            # pick the one with the fewest digits overall
            best=min(R["pure"],key=lambda p: len(str(p["zeta"]))+sum(len(str(v)) for v in p["F"].values()))
            e=abs(best["zeta"]*zeta(s)+fsum(c*polylog(s,x**int(k)) for k,c in best["F"].items()))
            assert e<mpf(10)**-250,(name,s,e)
            out["%s_pure_%d"%(name,s)]=fmt_pure(best["zeta"],best["F"],s)
            print(name,s,"pure ok",nstr(e,3),"terms",len(best["F"]),flush=True)
        elif R["full"]:
            f=R["full"][0]
            e=abs(f["zeta"]*zeta(s)+fsum(c*pi**(2*j)*L**(s-2*j) for j,c in enumerate(f["left"]))+fsum(c*polylog(s,x**int(k)) for k,c in f["F"].items()))
            mx=max(map(abs,list(f["F"].values())+f["left"]+[f["zeta"]])); assert e/mx<mpf(10)**-300,(name,s,e/mx)
            out["%s_full_%d"%(name,s)]=fmt_full(f["zeta"],f["left"],f["F"],s)
            print(name,s,"full ok",nstr(e,3),"terms",len(f["F"]),flush=True)
json.dump(out,open("salem_formulas.json","w"),indent=1)
