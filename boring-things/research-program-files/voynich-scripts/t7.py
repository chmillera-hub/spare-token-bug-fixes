import sys;sys.path.insert(0,".")
from t4 import *
a=A('ZL3b-n.txt',1,'tri');g=('1','A','H')
P=[p for p in a.order if re.fullmatch(r'f\d+[rv]',p) and a.key(p)==g and len(a.pages[p]['lines'])>=4]
sheets=collections.defaultdict(list)
for p in P: sheets[(a.M(p)['Q'],a.M(p)['B'])].append(p)
sk=sorted(sheets,key=lambda k:min(a.fol(p) for p in sheets[k]))
tot=collections.Counter();full={}
for p in P: full[p]=feat(words(a.pages[p]['lines']),'tri');tot.update(full[p])
vocab=[w for w,_ in tot.most_common(300)]
def vec(c):
    v=np.array([c.get(w,0) for w in vocab],float);return np.sqrt(v/v.sum())
def sv(k):
    c=collections.Counter()
    for p in sheets[k]: c.update(full[p])
    return vec(c)
X=np.array([sv(k) for k in sk]);mu=X.mean(0);u,s,vt=np.linalg.svd(X-mu,full_matrices=False);sc=(X-mu)@vt[0]
o=np.argsort(vt[0]);print('negative end trigrams:',[vocab[i] for i in o[:12]]);print('positive end trigrams:',[vocab[i] for i in o[-12:]])
# word-level contrast between extreme sheets
lo=[sk[i] for i in np.argsort(sc)[:6]];hi=[sk[i] for i in np.argsort(sc)[-6:]]
def wc(ks):
    c=collections.Counter()
    for k in ks:
        for p in sheets[k]: c.update(words(a.pages[p]['lines']))
    return c
cl,ch=wc(lo),wc(hi);nl,nh=sum(cl.values()),sum(ch.values())
ws=[w for w in set(cl)|set(ch) if cl[w]+ch[w]>=12]
r=sorted(ws,key=lambda w:(cl[w]+.5)/nl/((ch[w]+.5)/nh))
print('words favored at positive end:',[(w,cl[w],ch[w]) for w in r[:10]]);print('words favored at negative end:',[(w,cl[w],ch[w]) for w in r[-10:]],'totals',nl,nh)
# quire clustering permutation
Q=[k[0] for k in sk];rng=np.random.default_rng(0)
def within(q): return sum(np.var(sc[[i for i,x in enumerate(q) if x==u]])*sum(1 for x in q if x==u) for u in set(q))
obs=within(Q);perm=[within(list(rng.permutation(Q))) for _ in range(20000)]
print('quire clustering: within-quire variance obs',round(obs,4),'perm mean',round(float(np.mean(perm)),4),'p=',np.mean(np.array(perm)<=obs))
for q in sorted(set(Q)): print('  quire',q,[round(float(sc[i]),2) for i,x in enumerate(Q) if x==q])
# plant drawing? pages with $I all H. chol/chor share per sheet
