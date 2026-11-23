import sys, numpy as np
exec(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'random_routes_test.py')).read().split('print("name')[0])
def guided(D,k,mode):
    n=len(D); best=1e18
    for _ in range(k):
        cur=rng.integers(n); vis=np.zeros(n,bool); vis[cur]=True; L=0; s=cur
        for step in range(n-1):
            d=np.where(vis,np.inf,D[cur])
            left=n-1-step
            if mode=='near' or left==1: j=d.argmin()
            elif mode=='top2': j=np.argpartition(d,1)[:2][rng.integers(2)]
            elif mode=='top3':
                m=min(3,left); j=np.argpartition(d,m-1)[:m][rng.integers(m)]
            elif mode=='90':
                c=np.argpartition(d,1)[:2]; c=c[np.argsort(d[c])]; j=c[0] if rng.random()<0.9 else c[1]
            L+=D[cur,j]; vis[j]=True; cur=j
        best=min(best,L+D[cur,s])
    return best
print("name n near top2 top3 p90")
for f,o in [("eil51",426),("berlin52",7542),("kroA100",21282),("ch150",6528),("a280",2579)]:
    D=dm(load(sys.argv[1]+"/"+f+".tsp"),True)
    print(f,len(D),*[f"{(guided(D,10000,m)/o-1)*100:.0f}%" for m in ['near','top2','top3','90']],flush=True)
for n in [12,14]:
    rng=np.random.default_rng(n); D=dm(rng.random((n,2))*100,False); o=hk(D)
    print("random",n,*[f"{(guided(D,10000,m)/o-1)*100:.0f}%" for m in ['near','top2','top3','90']],flush=True)
