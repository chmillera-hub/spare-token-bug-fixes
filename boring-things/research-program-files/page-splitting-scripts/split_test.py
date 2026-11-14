import re,math,collections,random,sys
import numpy as np
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=t.find('*** START');e=t.find('*** END')
if s>0: t=t[t.find('\n',s):e if e>0 else None]
W=t.split();N=1000;L=len(W)//N
pages=[W[i*L:(i+1)*L] for i in range(N)]
print('words',len(W),'words per page',L)
ends_mid=sum(1 for p in pages[:-1] if not re.search(r'[.!?]["\')]*$',p[-1]));print('pages that end in the middle of a sentence',ends_mid)
tok=[[w for w in re.findall(r"[a-z]+",' '.join(p).lower()) if len(w)>3] for p in pages]
df=collections.Counter()
for d in tok:
    for w in set(d): df[w]+=1
vocab={w:i for i,w in enumerate(w for w,c in df.items() if 2<=c<=N*0.2)}
X=np.zeros((N,len(vocab)),np.float32)
for i,d in enumerate(tok):
    for w,c in collections.Counter(d).items():
        if w in vocab: X[i,vocab[w]]=(1+math.log(c))*math.log(N/df[w])
X/=np.linalg.norm(X,axis=1,keepdims=True)+1e-9
S=X@X.T;np.fill_diagonal(S,-1)
nn=np.argsort(-S,axis=1)[:,:8]
terms=[w for w,c in df.items() if 4<=c<=12 and len(w)>=7]
tpages={w:[i for i,d in enumerate(tok) if w in set(d)] for w in terms}
print('rare technical terms tracked',len(terms),'e.g.',sorted(terms,key=lambda w:-df[w])[:8])
def metrics(a):
    a=np.asarray(a);out=[]
    for k in range(4):
        idx=np.where(a==k)[0];st=set(idx.tolist())
        keep=np.mean([(i+1) in st for i in idx if i<N-1])
        run=best=0;prev=-5
        for i in idx:
            run=run+1 if i==prev+1 else 1;best=max(best,run);prev=i
        rel=np.mean([np.mean(a[nn[i,:5]]==k) for i in idx])
        out.append((keep,best,rel))
    tm=np.mean([max(collections.Counter(a[p].tolist()).values())/len(p) for p in tpages.values()])
    th=np.mean([max(collections.Counter(a[p].tolist()).values())/len(p)>=0.5 for p in tpages.values()])
    o=np.array(out);return o[:,0].max(),o[:,1].max(),o[:,2].max(),tm,th
def per(name,a):
    a=np.asarray(a);row=[]
    for k in range(4):
        idx=np.where(a==k)[0];st=set(idx.tolist())
        keep=100*np.mean([(i+1) in st for i in idx if i<N-1]);rel=100*np.mean([np.mean(a[nn[i,:5]]==k) for i in idx])
        tm=100*np.mean([np.sum(a[p]==k)/len(p) for p in tpages.values()])
        row.append((keep,rel,tm,100-(keep+rel+tm)/3))
    print(name,' | '.join(f'pile {k+1}: next {r[0]:.0f} related {r[1]:.0f} term {r[2]:.0f} confusion {r[3]:.0f}' for k,r in enumerate(row)))
def show(name,m): print(f"{name:28s} next page in same pile {m[0]*100:5.1f}% | longest unbroken run {m[1]:6.1f} pages | related pages together {m[2]*100:5.1f}% | biggest share of a rare term in one pile {m[3]*100:5.1f}% | terms with half or more in one pile {m[4]*100:5.1f}%")
per('quarters',[i*4//N for i in range(N)])
rng=random.Random(1);R=[]
for _ in range(20):
    a=[i%4 for i in range(N)];rng.shuffle(a);R.append(metrics(a))
per('random',a)
rr=[i%4 for i in range(N)];per('turns',rr)
# optimised
Wt=collections.defaultdict(float)
for i in range(N):
    for j in nn[i]:
        k=(min(i,int(j)),max(i,int(j)));Wt[k]=max(Wt[k],float(S[i,j]))
    for d,w in ((1,5.0),):
        if i+d<N: Wt[(i,i+d)]+=w
adj=collections.defaultdict(list)
for (i,j),w in Wt.items(): adj[i].append((j,w));adj[j].append((i,w))
a=rr[:]
def cost(i,k): return sum(w for j,w in adj[i] if a[j]==k)
rng=random.Random(7)
for it in range(1500000):
    i,j=rng.randrange(N),rng.randrange(N)
    if a[i]==a[j]: continue
    ki,kj=a[i],a[j]
    before=cost(i,ki)+cost(j,kj)
    a[i],a[j]=kj,ki
    after=cost(i,kj)+cost(j,ki)
    if after>before or (after==before and rng.random()<0.5): a[i],a[j]=ki,kj
per('tuned',a)
print('pile sizes',collections.Counter(a))
