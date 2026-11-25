"""One point for each grid size where a sequence earns the highest possible three part score (0 opens north).
The highest score needs one hallway through every room, so the test is: all rooms joined and no room with more than two open walls."""
import os; os.environ["MAZE_RULE"]="zero-north"
import itertools, json, random, time, multiprocessing as mp
DR=((-1,0),(0,1),(1,0),(0,-1))
SIZES=list(range(2,13))
def maxed(dirs,k):
    n=k*k; nb=[[] for _ in range(n)]
    for i in range(n):
        d=dirs[i]; r,c=divmod(i,k); a,b=r+DR[d][0],c+DR[d][1]
        if 0<=a<k and 0<=b<k:
            j=a*k+b
            if j not in nb[i]:
                nb[i].append(j); nb[j].append(i)
                if len(nb[i])>3 or len(nb[j])>3: return False
    seen=[False]*n; st=[0]; seen[0]=True; cnt=1
    while st:
        u=st.pop()
        for v in nb[u]:
            if not seen[v]: seen[v]=True; cnt+=1; st.append(v)
    if cnt!=n: return False
    degs=[len(x) for x in nb]; ends=degs.count(1); threes=degs.count(3)
    if ends>2 or threes>2: return False
    if threes==0: return True
    # a loop with one or two tails: look for one walk through every room starting at a tail end
    starts=[i for i in range(n) if degs[i]==1] or [0]
    used=[False]*n
    def walk(u,left):
        if left==0: return True
        for v in nb[u]:
            if not used[v]:
                used[v]=True
                if walk(v,left-1): return True
                used[v]=False
        return False
    import sys; sys.setrecursionlimit(10000)
    for s0 in starts:
        used=[False]*n; used[s0]=True
        if walk(s0,n-1): return True
    return False
def block_points(block):
    L=len(block); hit=[k for k in SIZES if maxed([block[i%L] for i in range(k*k)],k)]; return len(hit),block,hit
STATS={}
def chain_search(limit_seconds):
    """Longest run of grid sizes starting at 2 by 2 that one sequence can max out when the first k*k numbers fill each grid."""
    best=[[],0]; t0=time.time()
    def extend(prefix,k):
        # fill a grid of k by k rooms whose first len(prefix) rooms are fixed; backtrack with degree pruning
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
            if time.time()-t0>limit_seconds: return
            if i==n:
                if maxed(dirs,k): yield list(dirs)
                return
            for d in range(4):
                e=add(i,d)
                if e is False: continue
                dirs[i]=d
                # a finished room above the current row with no open wall can never be joined later
                r=i//k
                ok=True
                if i%k==k-1 and r>=1:
                    for j in range((r-1)*k,r*k):
                        if deg[j]==0: ok=False; break
                if ok: yield from go(i+1)
                undo(e)
        yield from go(len(prefix))
    def dfs(prefix,k):
        if time.time()-t0>limit_seconds: return
        if k-1>best[1]-0 and len(prefix)==(k-1)*(k-1) and k-1>=2:
            if k-1>best[1]: best[0]=list(prefix); best[1]=k-1; print("chain reaches",k-1,"".join(map(str,prefix)),flush=True)
        for sol in extend(prefix,k):
            STATS[k]=STATS.get(k,0)+1; dfs(sol,k+1)
    dfs([],2); return best
if __name__=="__main__":
    out={"sizes":SIZES}
    blocks=[b for L in range(1,9) for b in itertools.product(range(4),repeat=L)]
    with mp.Pool(2) as pool: res=pool.map(block_points,blocks,chunksize=500)
    best={}
    for p,b,hit in res:
        if p==0: continue
        key=tuple(b[i%len(b)] for i in range(840))
        if key not in best or len(b)<len(best[key][1]): best[key]=(p,b,hit)
    ranked=sorted(best.values(),key=lambda x:(-x[0],len(x[1]),x[1]))
    out["blocks_tested"]=len(blocks); out["blocks_with_points"]=len(ranked)
    out["point_counts"]={str(p):sum(1 for x in ranked if x[0]==p) for p in sorted({x[0] for x in ranked},reverse=True)}
    out["top_blocks"]=[{"doors":"".join(map(str,b)),"points":p,"sizes":hit} for p,b,hit in ranked[:60]]
    out["sizes_ever_maxed_by_a_block"]=sorted({k for x in ranked for k in x[2]})
    print(out["point_counts"],out["sizes_ever_maxed_by_a_block"]); [print(x) for x in out["top_blocks"][:25]]
    json.dump(out,open("max_score_points_results.json","w"),indent=1)
    c=chain_search(420); out["chain"]={"doors":"".join(map(str,c[0])),"reaches":c[1],"solutions_found_by_size":STATS}; print(out["chain"])
    json.dump(out,open("max_score_points_results.json","w"),indent=1)
