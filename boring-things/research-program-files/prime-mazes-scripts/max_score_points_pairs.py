import time, json, sys
import max_score_points as m
DR=m.DR
def extend(prefix,k,deadline):
    n=k*k; dirs=list(prefix)+[None]*(n-len(prefix)); deg=[0]*n; edges=set()
    def add(i,d):
        r,c=divmod(i,k); a,b=r+DR[d][0],c+DR[d][1]
        if not(0<=a<k and 0<=b<k): return None
        j=a*k+b; e=(min(i,j),max(i,j))
        if e in edges: return ()
        if deg[i]>=3 or deg[j]>=3: return False
        edges.add(e); deg[i]+=1; deg[j]+=1; return e
    def undo(e):
        if e: edges.discard(e); deg[e[0]]-=1; deg[e[1]]-=1
    for i,d in enumerate(prefix):
        if add(i,d) is False: return
    def go(i):
        if time.time()>deadline: return
        if i==n:
            if m.maxed(dirs,k): yield list(dirs)
            return
        for d in range(4):
            e=add(i,d)
            if e is False: continue
            dirs[i]=d; ok=True; r=i//k
            if i%k==k-1 and r>=1:
                for j in range((r-1)*k,r*k):
                    if deg[j]==0: ok=False; break
            if ok: yield from go(i+1)
            undo(e)
    yield from go(len(prefix))
t0=time.time(); res={}
# how many door patterns max out each small grid
for k in (2,3,4):
    c=sum(1 for _ in extend([],k,time.time()+600)); res["maxers_%d"%k]=c; print("maxers",k,c,round(time.time()-t0,1),flush=True)
# which pairs of sizes can one sequence max out (first k*k numbers fill each grid)
pairs={}
for a in (2,3,4):
    for b in range(a+1,7):
        found=None; dl=time.time()+40; n=0
        for sa in extend([],a,dl):
            n+=1
            for sb in extend(sa,b,dl): found=sb; break
            if found or time.time()>dl: break
        done=time.time()<dl
        pairs["%d,%d"%(a,b)]={"found":"".join(map(str,found)) if found else None,"search_finished":done or bool(found)}
        print(a,b,pairs["%d,%d"%(a,b)],round(time.time()-t0,1),flush=True)
res["pairs"]=pairs
json.dump(res,open("max_score_points_pairs_results.json","w"),indent=1)
