import sys, numpy as np, itertools, math
rng=np.random.default_rng(1)
def load(p):
    pts=[];on=False
    for l in open(p):
        l=l.strip()
        if l.startswith('NODE_COORD'): on=True; continue
        if l=='EOF' or not l: continue
        if on:
            a=l.split(); pts.append((float(a[1]),float(a[2])))
    return np.array(pts)
def dm(P,rnd):
    D=np.sqrt(((P[:,None]-P[None])**2).sum(-1))
    return np.rint(D) if rnd else D
def tl(D,t): return D[t,np.roll(t,-1)].sum()
def rand_best(D,k):
    n=len(D); ls=[]
    for _ in range(k):
        ls.append(tl(D,rng.permutation(n)))
    ls=np.array(ls); return ls.min(), ls.mean()
def nn(D):
    n=len(D); best=1e18
    for s in range(min(n,20)):
        seen=[s]; left=set(range(n))-{s}
        while left:
            c=min(left,key=lambda j:D[seen[-1],j]); seen.append(c); left.remove(c)
        best=min(best,tl(D,np.array(seen)))
    return best
def twoopt(D,t):
    n=len(t); t=list(t); imp=True; ev=0
    while imp:
        imp=False
        for i in range(n-1):
            for j in range(i+2,n):
                if i==0 and j==n-1: continue
                a,b,c,d=t[i],t[i+1],t[j],t[(j+1)%n]; ev+=1
                if D[a,c]+D[b,d]<D[a,b]+D[c,d]-1e-9:
                    t[i+1:j+1]=reversed(t[i+1:j+1]); imp=True
    return tl(D,np.array(t)),ev
def hk(D):
    n=len(D); C={}
    for k in range(1,n): C[(1<<k,k)]=D[0,k]
    for s in range(2,n):
        for sub in itertools.combinations(range(1,n),s):
            bits=sum(1<<x for x in sub)
            for k in sub:
                pb=bits&~(1<<k)
                C[(bits,k)]=min(C[(pb,m)]+D[m,k] for m in sub if m!=k)
    full=(1<<n)-2
    return min(C[(full,k)]+D[k,0] for k in range(1,n))
print("name n optimal best_of_10k pct_over avg_random_pct_over NN_pct 2opt_pct 2opt_evals frac_of_all_routes")
def report(name,D,opt):
    n=len(D); b,m=rand_best(D,10000); t2,ev=twoopt(D,rng.permutation(n))
    logtot=math.lgamma(n)-math.log(2)  # (n-1)!/2
    print(name,n,round(opt,1),round(b,1),f"{(b/opt-1)*100:.0f}%",f"{(m/opt-1)*100:.0f}%",f"{(nn(D)/opt-1)*100:.0f}%",f"{(t2/opt-1)*100:.0f}%",ev,f"1e{(math.log(10000)-logtot)/math.log(10):.0f}")
for n in [6,8,10,12,14]:
    D=dm(rng.random((n,2))*100,False); report(f"random{n}",D,hk(D))
for n in [20,30]:
    a=np.linspace(0,2*np.pi,n,endpoint=False); P=np.c_[np.cos(a),np.sin(a)]*100
    D=dm(P,False); report(f"circle{n}",D,n*2*100*math.sin(math.pi/n))
for f,o in [("eil51",426),("berlin52",7542),("kroA100",21282),("ch150",6528),("a280",2579)]:
    report(f,dm(load(sys.argv[1]+"/"+f+".tsp"),True),o)
