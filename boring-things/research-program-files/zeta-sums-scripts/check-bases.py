import re,sys,json
from mpmath import *
import re
mp.dps=260
def root(coef,guess): return findroot(lambda t: polyval(coef,t),guess)
B={"plastic":root([1,1,0,-1],0.75),"supergold":root([1,0,1,-1],0.68),"pisot4":root([1,0,0,1,-1],0.72),
"pisot5":root([1,0,-1,1,1,-1],0.69),"pisot5b":root([1,1,1,1,0,-1],0.65),"pisot6":root([1,0,-1,0,1,1,-1],0.67),"tribo":root([1,1,1,-1],0.54),
"r23":2-sqrt(3),"third":mpf(1)/3,"silver":sqrt(2)-1,"r15":4-sqrt(15),"r6":5-2*sqrt(6),"r21":(5-sqrt(21))/2,"half":mpf(1)/2}
def parse(line):
    d={}
    for c,n in re.findall(r"([+-]\d+)\*((?:zeta\(\d+\))|(?:pi\^\d+ L\^\d+)|(?:F\(x\^\d+\)))",line): d[n]=int(c)
    return d
def rows(base,s,kind):
    t=open('out_%s.txt'%base).read().split('\n'); out=[]
    for i,l in enumerate(t):
        if (" s=%d %s"%(s,kind)) in l:
            j=i+1
            while j<len(t) and t[j].startswith('      '): out.append(parse(t[j])); j+=1
    return out
def Fsum(x,k,s):
    y=x**k; t=mpf(1); tot=mpf(0); n=0
    while True:
        n+=1; t*=y; tot+=t/mpf(n)**s
        if t<mpf(10)**(-265): return tot
def val(name,x,s):
    L=-log(x)
    if name.startswith('zeta'): return zeta(s)
    m=re.match(r"pi\^(\d+) L\^(\d+)",name)
    if m: return pi**int(m.group(1))*L**int(m.group(2))
    return Fsum(x,int(re.match(r"F\(x\^(\d+)\)",name).group(1)),s)
def fmt(d,s):
    z='zeta(%d)'%s; a=d.get(z,0)
    sign=1 if a>0 else -1
    parts=[]
    def key(n):
        if n.startswith('pi'): m=re.match(r"pi\^(\d+) L\^(\d+)",n); return (0,int(m.group(1)))
        return (1,int(n[4:-1]))
    for n in sorted([n for n in d if n!=z],key=key):
        c=-sign*d[n]
        if n.startswith('pi'):
            m=re.match(r"pi\^(\d+) L\^(\d+)",n); p,q=int(m.group(1)),int(m.group(2))
            nm=("L^%d"%q if q>1 else "L") if p==0 else ("pi^%d × "%p+("L^%d"%q if q>1 else "L"))
        else:
            k=int(n[4:-1]); nm="F(x^%d)"%k if k>1 else "F(x)"
        co="" if abs(c)==1 and not n.startswith('pi') else "%d × "%abs(c)
        parts.append(("+ " if c>0 else "- ")+co+nm)
    rhs=" ".join(parts)
    rhs=rhs[2:] if rhs.startswith("+ ") else "-"+rhs[2:]
    lhs=("%d × zeta(%d)"%(abs(a),s) if abs(a)!=1 else "zeta(%d)"%s) if a else "0"
    return lhs+" = "+rhs
def check(base,d,s):
    x=B[base]; return abs(fsum(c*val(n,x,s) for n,c in d.items()))
out={}
def take(tag,base,s,kind,idx=0,need_zeta=True):
    rs=rows(base,s,kind)
    rs=[r for r in rs if (('zeta(%d)'%s) in r)==need_zeta] if need_zeta else rs
    d=rs[idx]; e=check(base,d,s)
    assert e<mpf(10)**(-240),(tag,e)
    out[tag]=fmt(d,s); print(tag,"ok",nstr(e,3)); print("   ",out[tag])
take("plastic3","plastic",3,"PURE"); take("plastic5","plastic",5,"PURE"); take("plastic9","plastic",9,"mode1")
take("super3","supergold",3,"PURE"); take("super5","supergold",5,"mode1")
take("p4_3","pisot4",3,"PURE"); take("p4_5","pisot4",5,"mode1"); take("p5_3","pisot5",3,"PURE"); take("p5b_3","pisot5b",3,"PURE",1)
take("p6_3","pisot6",3,"mode1"); take("tribo3a","tribo",3,"mode1",0); take("tribo3b","tribo",3,"mode1",1)
take("r23_3","r23",3,"mode1"); take("r23_5","r23",5,"mode1")
for b in ("third","silver","r15","r6","r21"): take(b+"3",b,3,"mode1")
take("half3","half",3,"mode1",1); take("half5","half",5,"mode1")
json.dump(out,open('formulas.json','w'),indent=1)
# plastic zeta(7) single leftover (from plastic.py output) verify
import subprocess
