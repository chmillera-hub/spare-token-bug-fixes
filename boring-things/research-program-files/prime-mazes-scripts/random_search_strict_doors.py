import os, time; os.environ["MAZE_RULE"]="zero-north"
from grid_tools import *
def score_digits(s,k,per):
    adj=[set() for _ in range(k*k)]; outs=[]
    for i in range(k*k):
        r,c=divmod(i,k)
        for t in range(per):
            d=int(s[i*per+t])%4; a,b=r+DR[d][0],c+DR[d][1]
            if 0<=a<k and 0<=b<k: adj[i].add(a*k+b); adj[a*k+b].add(i)
            else: outs.append((i,d))
    comp,sizes=regions(adj); have={}
    for i,d in set(outs): have.setdefault(comp[i],[0,0,0,0])[d]+=1
    door=sum((o[0]+o[2] if o[0] and o[2] else 0)+(o[1]+o[3] if o[1] and o[3] else 0) for o in have.values())
    big=max(sizes); lw=longest_walk(adj); return big+lw+door,big,lw,door
out={}
rng=random.Random(2027)
for per,k,n in ((1,4,150000),(1,5,150000),(1,6,80000),(1,8,25000),(1,10,10000),(2,3,60000),(2,4,25000)):
    t0=time.time(); best=None; marks=[]; anydoor=0
    for i in range(1,n+1):
        s=str(rng.randrange(1,10))+"".join(str(rng.randrange(10)) for _ in range(k*k*per-1)); sc=score_digits(s,k,per); anydoor+=sc[3]>0
        if best is None or sc[0]>best[1][0]: best=(s,sc); marks.append((i,sc[0]))
    out["%d_%d"%(per,k)]={"per":per,"k":k,"samples":n,"best":best[0],"score":best[1],"marks":marks,"share_with_door_points":anydoor/n,"seconds":round(time.time()-t0,1)}
    print(per,k,out["%d_%d"%(per,k)],flush=True)
json.dump(out,open("random_search_strict_doors_results.json","w"),indent=1)
