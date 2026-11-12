# Independent second pass on the Voynich "next page" result (written 12 November 2026 by an AI chatbot).
# This program shares no code with t4.py to t7.py. Every choice below was fixed before the first run:
#   own parser; window = first third and last third of the lines of a page; feature = two-letter chunks inside words;
#   closeness = Jensen-Shannon divergence (smaller means closer); candidates = pages by the same scribe in the same
#   language group and the same section; score = rank of the true page among candidates (0.5 chance and 1.0 top match).
# The typed copy (ZL3b-n.txt and IT2a-n.txt and RF1b-e.txt from voynich.nu) must sit in a folder named data.
import re,sys,math,random,collections
import numpy as np
def parse(path):
    pages={};order=[]
    for ln in open(path,encoding='latin-1'):
        ln=ln.rstrip()
        h=re.match(r'<(f\d+[rv])>\s*<!\s*(.*?)>',ln)
        if h:
            meta={k:v for k,v in re.findall(r'\$([A-Z])=(\S+?)(?=\s|$)',h.group(2))}
            pages[h.group(1)]=dict(meta=meta,lines=[]);order.append(h.group(1));continue
        m=re.match(r'<(f\d+[rv])\.\d+[a-z]?,[^>]*?P[^>]*>\s*(.*)',ln)
        if m and m.group(1) in pages:
            t=m.group(2)
            t=re.sub(r'<[^>]*>','',t)                     # inline comments
            t=re.sub(r'\[([^:\]]*)(:[^\]]*)?\]',r'\1',t)  # first reading of an uncertain spot
            t=re.sub(r'@\d+;','?',t); t=t.replace('{','').replace('}','')
            ws=[w for w in re.split(r'[.,\s]+',t) if w and re.fullmatch(r"[a-z]+",w)]
            if ws: pages[m.group(1)]['lines'].append(ws)
    return pages,order
def chunks(lines):
    c=collections.Counter()
    for ws in lines:
        for w in ws:
            s='<'+w+'>'
            for i in range(len(s)-1): c[s[i:i+2]]+=1
    return c
def jsd(a,b):
    if not a or not b: return 1.0
    na=sum(a.values()); nb=sum(b.values()); out=0.0
    for k in set(a)|set(b):
        p=a.get(k,0)/na; q=b.get(k,0)/nb; m=(p+q)/2
        if p: out+=0.5*p*math.log2(p/m)
        if q: out+=0.5*q*math.log2(q/m)
    return out
def fol(p): return int(re.match(r'f(\d+)',p).group(1))
def run(fn,rng):
    pages,order=parse('data/'+fn)
    ok=[p for p in order if len(pages[p]['lines'])>=6]
    top={};bot={}
    for p in ok:
        L=pages[p]['lines']; k=max(2,len(L)//3); top[p]=chunks(L[:k]); bot[p]=chunks(L[-k:])
    grp=lambda p: tuple(pages[p]['meta'].get(k) for k in 'HLI')
    sheet=lambda p:(pages[p]['meta'].get('Q'),pages[p]['meta'].get('B'))
    partner={}
    bysheet=collections.defaultdict(set)
    for p in order: bysheet[sheet(p)].add(fol(p))
    for p in order:
        o=[f for f in bysheet[sheet(p)] if f!=fol(p)]
        if len(bysheet[sheet(p)])==2: partner[p]=o[0]
    def score(src_feat,true,cands,tgt):
        d=sorted(cands,key=lambda c:jsd(src_feat,tgt[c])); return 1-d.index(true)/(len(d)-1)
    res=collections.defaultdict(list)
    for p in ok:
        n=fol(p); g=grp(p)
        if p.endswith('r'):
            V=[q for q in ok if q.endswith('v') and grp(q)==g]
            t='f%dv'%n
            if t in V and len(V)>=6: res['front of a leaf to the back of the same leaf'].append(score(bot[p],t,V,top))
            continue
        R=[q for q in ok if q.endswith('r') and grp(q)==g and fol(q)!=n]
        if len(R)<6: continue
        pn=partner.get(p)
        f='f%dr'%(n+1)
        if f in R and pn!=n+1: res['facing page in the bound book'].append(score(bot[p],f,R,top))
        if pn and pn!=n+1 and 'f%dr'%pn in R:
            t='f%dr'%pn
            if pn>n:
                res['forward sheet partner'].append(score(bot[p],t,R,top))
                res['forward sheet partner with the wrong ends (top lines to bottom lines)'].append(score(top[p],t,R,bot))
                res['_fwd_sizes'].append(len(R))
            else: res['backward sheet partner'].append(score(bot[p],t,R,top))
    # shuffle test for the forward sheet partner: a randomly chosen candidate takes the place of the true page
    sizes=res.pop('_fwd_sizes'); obs=np.mean(res['forward sheet partner'])
    sims=np.array([np.mean([1-rng.randrange(s)/(s-1) for s in sizes]) for _ in range(100000)])
    p=(np.sum(sims>=obs)+1)/(len(sims)+1)
    return res,p
rng=random.Random(12)
for fn in ('ZL3b-n.txt','IT2a-n.txt','RF1b-e.txt'):
    res,p=run(fn,rng); print(fn)
    for k,v in res.items(): print(f"   {k}: {np.mean(v):.3f} across {len(v)} cases")
    print(f"   shuffle test for the forward sheet partner: chance of a score this high = {p:.6f}")
# Extra numbers added after the first run (the choices above were not changed): how sure the direction result is.
print("\ndirection checks on ZL3b-n.txt")
res,_=run('ZL3b-n.txt',rng)
f=np.array(res['forward sheet partner']); w=np.array(res['forward sheet partner with the wrong ends (top lines to bottom lines)']); b=np.array(res['backward sheet partner'])
nr=np.random.default_rng(12)
d=f-w; flips=np.array([np.mean(d*nr.choice([-1,1],len(d))) for _ in range(100000)])
print(f"   right ends minus wrong ends on the same 30 sheets: mean gap {d.mean():+.3f}  right ends higher on {int((d>0).sum())} and lower on {int((d<0).sum())}  sign-flip chance {(np.sum(flips>=d.mean())+1)/100001:.4f}")
allv=np.concatenate([f,b]); gap=f.mean()-b.mean(); cnt=0
for _ in range(100000):
    nr.shuffle(allv); cnt+= (allv[:len(f)].mean()-allv[len(f):].mean())>=gap
print(f"   forward minus backward: gap {gap:+.3f}  label-shuffle chance {(cnt+1)/100001:.4f}")
for name,v in (('forward',f),('backward',b)):
    bs=[nr.choice(v,len(v)).mean() for _ in range(20000)]
    print(f"   {name}: mean {v.mean():.3f}  95 percent range {np.percentile(bs,2.5):.3f} to {np.percentile(bs,97.5):.3f}")
