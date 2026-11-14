import re,sys,math,collections,itertools,numpy as np
from math import comb
D='data/'
def load(F):
    pages={};order=[]
    for ln in open(F,encoding='utf-8',errors='replace'):
        ln=ln.rstrip('\n')
        m=re.match(r'^<(f\d+[rv]\d*)>\s+<!(.*)>',ln)
        if m:
            pages[m.group(1)]={'meta':dict(re.findall(r'\$(\w)=(\w+)',m.group(2))),'lines':[]};order.append(m.group(1));continue
        m=re.match(r'^<(f\d+[rv]\d*)\.(\d+),([^>]*)>\s+(.*)',ln)
        if m and 'P' in m.group(3) and m.group(1) in pages:
            t=m.group(4);t=re.sub(r'<[^>]*>','',t);t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t);t=re.sub(r'[{}]','',t);t=re.sub(r'@\d+;','?',t)
            pages[m.group(1)]['lines'].append(t)
    return pages,order
def words(lines):
    out=[]
    for t in lines:
        out+=[w for w in t.replace(',','.').split('.') if w and re.fullmatch(r"[a-z']+",w)]
    return out
def feat(ws,mode):
    g=collections.Counter()
    if mode=='word':
        g.update(ws);return g
    n=3 if mode=='tri' else 2
    for w in ws:
        s='^'+w+'$'
        for i in range(len(s)-n+1): g[s[i:i+n]]+=1
    return g
def cos(a,b):
    if not a or not b: return 0.0
    d=sum(v*b.get(k,0) for k,v in a.items())
    return d/math.sqrt(sum(v*v for v in a.values())*sum(v*v for v in b.values()))
def binom_p(k,n,p): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
class A:
    def __init__(s,fn,K=4,mode='tri'):
        s.pages,s.order=load(D+fn);s.K=K
        s.simple=[p for p in s.order if re.fullmatch(r'f\d+[rv]',p) and len(s.pages[p]['lines'])>=2*K]
        s.S=set(s.simple)
        s.bot={p:feat(words(s.pages[p]['lines'][-K:]),mode) for p in s.simple}
        s.top={p:feat(words(s.pages[p]['lines'][:K]),mode) for p in s.simple}
    def M(s,p): return s.pages[p]['meta']
    def key(s,p): return tuple(s.M(p).get(k) for k in 'HLI')
    @staticmethod
    def fol(p): return int(re.match(r'f(\d+)',p).group(1))
    def partner(s,p):
        n=s.fol(p);m=s.M(p)
        c=[q for q in s.order if re.fullmatch(r'f\d+[rv]',q) and q[-1]=='r' and s.M(q).get('Q')==m.get('Q') and s.M(q).get('B')==m.get('B') and s.fol(q)!=n]
        return s.fol(c[0]) if c else None
    def rank(s,src,true,cands):
        sc=sorted(cands,key=lambda c:-cos(s.bot[src],s.top[c]))
        r=sc.index(true);return 1-r/(len(sc)-1),r==0,1/len(sc),sc
    def transitions(s):
        out=collections.defaultdict(list)
        for p in s.simple:
            n=s.fol(p);g=s.key(p)
            if p[-1]=='r':
                V=[q for q in s.simple if q[-1]=='v' and s.key(q)==g]
                if 'f%dv'%n in V and len(V)>=6: out['flip'].append((p,)+s.rank(p,'f%dv'%n,V)[:3])
                continue
            R=[q for q in s.simple if q[-1]=='r' and s.key(q)==g and s.fol(q)!=n]
            if len(R)<6: continue
            pn=s.partner(p);face='f%dr'%(n+1)
            central=(pn==n+1)
            if face in R: out['facing_central' if central else 'facing_noncentral'].append((p,)+s.rank(p,face,R)[:3])
            if pn and not central and 'f%dr'%pn in R:
                out['partner_fwd' if pn>n else 'partner_bwd'].append((p,)+s.rank(p,'f%dr'%pn,R)[:3])
        return out
def line(name,rows):
    if not rows: return f"{name}: n=0"
    a=np.array([r[1] for r in rows]);n=len(a);z=(a.mean()-0.5)/math.sqrt(1/12/n)
    k=sum(r[2] for r in rows);pc=float(np.mean([r[3] for r in rows]))
    return f"{name}: n={n} meanpct={a.mean():.3f} z={z:+.1f} top1={k}/{n} (chance {pc*n:.1f}, p={binom_p(k,n,pc):.1e})"
if __name__=='__main__':
    print("=== main: ZL, K=4, trigram")
    a=A('ZL3b-n.txt');T=a.transitions()
    for k in ('flip','facing_central','facing_noncentral','partner_fwd','partner_bwd'): print(' ',line(k,T[k]))
    print("  per scribe/section, partner_fwd:")
    by=collections.defaultdict(list)
    for r in T['partner_fwd']: by[a.key(r[0])].append(r)
    for g,v in sorted(by.items()): print('   ',g,line('',v))
    print('  partner_fwd detail:',' '.join(f"{r[0]}:{r[1]:.2f}" for r in T['partner_fwd']))
    print("=== robustness grid (partner_fwd | partner_bwd | facing_noncentral | flip) meanpct(n)")
    for fn in ('ZL3b-n.txt','IT2a-n.txt','RF1b-e.txt'):
        for mode in ('tri','bi','word'):
            for K in (3,4,5,6):
                T=A(fn,K,mode).transitions()
                f=lambda k:(f"{np.mean([r[1] for r in T[k]]):.2f}({len(T[k])})" if T[k] else 'na')
                print(f"  {fn[:2]} {mode:4} K={K}: {f('partner_fwd')} | {f('partner_bwd')} | {f('facing_noncentral')} | {f('flip')}")
