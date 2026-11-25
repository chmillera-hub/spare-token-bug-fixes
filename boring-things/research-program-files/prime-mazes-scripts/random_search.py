import os, sys, time; os.environ["MAZE_RULE"]="zero-north"
from grid_tools import *
def score_digits(s,k):
    dirs=[int(ch)%4 for ch in s]; adj=build(dirs,k); comp,sizes=regions(adj)
    top={comp[c] for c in range(k)}; bot={comp[(k-1)*k+c] for c in range(k)}; left={comp[r*k] for r in range(k)}; right={comp[r*k+k-1] for r in range(k)}
    door=sum(comp[c] in bot for c in range(k))+sum(comp[(k-1)*k+c] in top for c in range(k))+sum(comp[r*k] in right for r in range(k))+sum(comp[r*k+k-1] in left for r in range(k))
    big=max(sizes); lw=longest_walk(adj); return big+lw+door,big,lw,door
out={}
rng=random.Random(2026)
for k,n in ((4,200000),(5,150000),(6,80000),(8,25000),(10,10000)):
    t0=time.time(); best=None; hist={}; marks=[]
    for i in range(1,n+1):
        s=str(rng.randrange(1,10))+"".join(str(rng.randrange(10)) for _ in range(k*k-1)); sc=score_digits(s,k)
        if best is None or sc[0]>best[1][0]: best=(s,sc); marks.append((i,sc[0]))
    # hill climb from the best random number: change one digit at a time and keep any change that does not lower the score
    s,sc=best; cur=list(s); curs=sc; steps=0; r2=random.Random(k)
    for _ in range(40000):
        i=r2.randrange(k*k); old=cur[i]; cur[i]=str(r2.randrange(1 if i==0 else 0,10))
        ns=score_digits("".join(cur),k)
        if ns[0]>=curs[0]:
            if ns[0]>curs[0]: steps+=1
            curs=ns
        else: cur[i]=old
        if curs[0]==2*k*k+4*k: break
    out[k]={"samples":n,"max":2*k*k+4*k,"best_random":best[0],"best_random_score":best[1],"improvement_marks":marks,"climbed":"".join(cur),"climbed_score":curs,"climb_improvements":steps,"seconds":round(time.time()-t0,1)}
    print(k,out[k],flush=True)
json.dump(out,open("random_search_results.json","w"),indent=1)
