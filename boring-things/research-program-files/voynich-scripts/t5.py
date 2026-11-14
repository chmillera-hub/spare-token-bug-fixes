import sys;sys.path.insert(0,".");from t4 import *
a=A('ZL3b-n.txt',4,'tri')
def pctl(src,cands,targets):
    sc=sorted(cands,key=lambda c:-cos(a.bot[src],a.top[c]));n=len(sc)
    return [1-sc.index(t)/(n-1) for t in targets]
def rep(name,v):
    v=np.array(v)
    print(f"{name}: n={len(v)} meanpct={v.mean():.3f} se={v.std()/math.sqrt(max(len(v),1)):.3f}" if len(v) else name+': n=0')
# control: same quire, other sheet
ctl_fwd=[];ctl_any=[];other=[];flip1=[];flip2=[]
sheets={}
for p in a.simple:
    n=a.fol(p);g=a.key(p);m=a.M(p)
    pn=a.partner(p)
    if p[-1]=='r':
        V=[q for q in a.simple if q[-1]=='v' and a.key(q)==g]
        if 'f%dv'%n in V and len(V)>=6 and pn:
            (flip1 if pn>n else flip2).append(a.rank(p,'f%dv'%n,V)[0])
        continue
    R=[q for q in a.simple if q[-1]=='r' and a.key(q)==g and a.fol(q)!=n]
    if len(R)<6 or not pn: continue
    sameQ=[q for q in R if a.M(q).get('Q')==m.get('Q') and a.fol(q) not in (pn,n+1)]
    if pn>n:
        t=[q for q in sameQ if a.partner(q) and a.partner(q)<a.fol(q)]  # second-half rectos of other sheets
        ctl_fwd+=pctl(p,R,t)
    ctl_any+=pctl(p,R,sameQ)
rep('control: first-half verso -> second-half recto of a DIFFERENT sheet, same quire',ctl_fwd)
rep('control: any verso -> any non-partner non-facing recto in same quire',ctl_any)
rep('flip on first leaf of sheet (p1->p2)',flip1);rep('flip on second leaf of sheet (p3->p4)',flip2)
# sheet chain: exit = second-leaf verso bottom ; entry = first-leaf recto top
ex=[];en=[]
for p in a.simple:
    pn=a.partner(p);n=a.fol(p)
    if not pn: continue
    if p[-1]=='v' and pn<n: ex.append(p)
    if p[-1]=='r' and pn>n: en.append(p)
H=collections.defaultdict(list);lead=[]
qs=sorted({a.M(p).get('Q') for p in a.simple})
for p in ex:
    g=a.key(p);m=a.M(p);C=[q for q in en if a.key(q)==g and a.partner(q)!=a.fol(p) and not (a.M(q).get('Q')==m.get('Q') and a.M(q).get('B')==m.get('B'))]
    if len(C)<5: continue
    sc=sorted(C,key=lambda c:-cos(a.bot[p],a.top[c]));n=len(sc)
    for q in C:
        mq=a.M(q);pc=1-sc.index(q)/(n-1)
        same=mq.get('Q')==m.get('Q');db=int(mq.get('B'))-int(m.get('B'))
        if same: H['same quire, any other sheet'].append(pc)
        if same and db==1: H['same quire, next sheet inward (B+1)'].append(pc)
        if same and db==-1: H['same quire, next sheet outward (B-1)'].append(pc)
        if not same and qs.index(mq.get('Q'))-qs.index(m.get('Q'))==1: H['next quire, any sheet'].append(pc)
        if not same and qs.index(mq.get('Q'))-qs.index(m.get('Q'))==-1: H['previous quire, any sheet'].append(pc)
    lead.append((cos(a.bot[p],a.top[sc[0]])-cos(a.bot[p],a.top[sc[1]]),p,sc[0],n,g))
print('--- sheet-to-sheet (end of one sheet -> start of another), units:',len(lead))
for k,v in H.items(): rep('  '+k,v)
# mutual best among sheets
predbest={}
for q in en:
    C=[p for p in ex if a.key(p)==a.key(q) and a.partner(q)!=a.fol(p) and not (a.M(q).get('Q')==a.M(p).get('Q') and a.M(q).get('B')==a.M(p).get('B'))]
    if len(C)>=5: predbest[q]=max(C,key=lambda p:cos(a.bot[p],a.top[q]))
print('--- mutual-best sheet links (end page -> start page):')
for mar,p,q,n,g in sorted(lead,reverse=True):
    if predbest.get(q)==p:
        print(f"   {p} (quire {a.M(p)['Q']} sheet {a.M(p)['B']}) -> {q} (quire {a.M(q)['Q']} sheet {a.M(q)['B']}) scribe {g[0]} sec {g[2]} cands {n} margin {mar:.3f}")
