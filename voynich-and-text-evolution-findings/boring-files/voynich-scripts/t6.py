import sys;sys.path.insert(0,".")
from t4 import *
def spearman(x,y):
    rx=np.argsort(np.argsort(x));ry=np.argsort(np.argsort(y));return float(np.corrcoef(rx,ry)[0,1])
def analyse(fn,group,mode='tri',top=300):
    a=A(fn,1,mode)
    P=[p for p in a.order if re.fullmatch(r'f\d+[rv]',p) and a.key(p)==group and len(a.pages[p]['lines'])>=4]
    sheets=collections.defaultdict(list)
    for p in P: sheets[(a.M(p)['Q'],a.M(p)['B'])].append(p)
    sk=sorted(sheets,key=lambda k:min(a.fol(p) for p in sheets[k]))
    def fv(lines): return feat(words(lines),mode)
    full={p:fv(a.pages[p]['lines']) for p in P}
    tot=collections.Counter()
    for p in P: tot.update(full[p])
    vocab=[w for w,_ in tot.most_common(top)]
    def vec(c):
        v=np.array([c.get(w,0) for w in vocab],float);s=v.sum();return np.sqrt(v/s) if s else v
    def pc1(X):
        Xc=X-X.mean(0);u,s,vt=np.linalg.svd(Xc,full_matrices=False);return Xc@vt[0],vt[0],X.mean(0),(s[0]**2/(s**2).sum())
    def sheetvec(k,sel):
        c=collections.Counter()
        for p in sheets[k]:
            L=a.pages[p]['lines'];c.update(fv([l for i,l in enumerate(L) if sel(i)]))
        return vec(c)
    Xo=np.array([sheetvec(k,lambda i:i%2==0) for k in sk]);Xe=np.array([sheetvec(k,lambda i:i%2==1) for k in sk])
    so,_,_,_=pc1(Xo);se,_,_,_=pc1(Xe)
    Xa=np.array([sheetvec(k,lambda i:True) for k in sk]);sa,axis,mu,ev=pc1(Xa)
    print(f"{fn[:2]} group {group}: sheets={len(sk)} pages={len(P)}  split-half PC1 agreement |rho|={abs(spearman(so,se)):.2f}  PC1 share={ev:.2f}")
    # bound order correlation
    print(f"   PC1 vs bound position rho={spearman(sa,np.arange(len(sk))):+.2f}")
    # within-sheet direction: project pages on axis
    proj={p:float((vec(full[p])-mu)@axis) for p in P}
    d12=[];d23=[];d34=[];d14=[]
    for k in sk:
        ps=sorted(sheets[k],key=lambda p:(a.fol(p),p[-1]))
        fs=sorted({a.fol(p) for p in ps})
        if len(fs)!=2: continue
        g=lambda f,s: proj.get('f%d%s'%(f,s))
        p1,p2,p3,p4=g(fs[0],'r'),g(fs[0],'v'),g(fs[1],'r'),g(fs[1],'v')
        if None not in(p1,p2): d12.append(p2-p1)
        if None not in(p2,p3): d23.append(p3-p2)
        if None not in(p3,p4): d34.append(p4-p3)
        if None not in(p1,p4): d14.append(p4-p1)
    for nm,d in (('p1->p2',d12),('p2->p3',d23),('p3->p4',d34),('p1->p4',d14)):
        d=np.array(d);print(f"   {nm}: n={len(d)} mean step={d.mean():+.4f} positive {int((d>0).sum())}/{len(d)}")
    # page-level distance decay within sheet vs between
    sd=np.std(list(proj.values()))
    print('   sd of page scores',round(float(sd),4))
    return a,sk,sa,sheets
for fn in ('ZL3b-n.txt','IT2a-n.txt'):
    for g in (('1','A','H'),('2','B','B'),('3','B','S'),('2','B','H')):
        try: r=analyse(fn,g)
        except Exception as e: print(fn,g,'ERR',e)
        if fn=='ZL3b-n.txt' and g==('1','A','H'):
            a,sk,sa,sheets=r;o=np.argsort(sa)
            print('   seriated sheets (leaf pairs), one end to the other:',' | '.join('-'.join(str(f) for f in sorted({a.fol(p) for p in sheets[sk[i]]})) for i in o))
