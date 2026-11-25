"""One pattern or one sequence scored on every grid size from 2 by 2 to 10 by 10 rooms (0 opens north).
three part score = largest region + longest walk + door points (every edge room has an outside door the player can open)."""
import os; os.environ["MAZE_RULE"]="zero-north"
from grid_tools import *
import itertools, multiprocessing as mp
SIZES=list(range(2,11)); MAXT=sum(2*k*k+4*k for k in SIZES)
def score_dirs(dirs,k):
    adj=build(dirs,k); comp,sizes=regions(adj)
    top={comp[c] for c in range(k)}; bot={comp[(k-1)*k+c] for c in range(k)}; left={comp[r*k] for r in range(k)}; right={comp[r*k+k-1] for r in range(k)}
    door=sum(comp[c] in bot for c in range(k))+sum(comp[(k-1)*k+c] in top for c in range(k))+sum(comp[r*k] in right for r in range(k))+sum(comp[r*k+k-1] in left for r in range(k))
    return max(sizes)+longest_walk(adj)+door
N_,E_,S_,W_=0,1,2,3
def spiral(k):
    path=[]; a,b=0,k-1
    while a<=b:
        for c in range(a,b+1): path.append((a,c))
        for r in range(a+1,b+1): path.append((r,b))
        if a<b:
            for c in range(b-1,a-1,-1): path.append((b,c))
            for r in range(b-1,a,-1): path.append((r,a))
        a+=1;b-=1
    d=[None]*(k*k)
    for i,(r,c) in enumerate(path):
        nr,nc=path[i+1] if i+1<len(path) else path[i-1]; d[r*k+c]=DR.index((nr-r,nc-c))
    return d
def rings(k):
    d=[[None]*k for _ in range(k)]
    for L in range(k//2):
        a,b=L,k-1-L
        for c in range(a,b): d[a][c]=E_
        for r in range(a,b): d[r][b]=S_
        for c in range(b,a,-1): d[b][c]=W_
        for r in range(b,a,-1): d[r][a]=N_
    if k%2: d[k//2][k//2]=N_
    return [x for row in d for x in row]
SHAPES={
 "spiral (one hallway that winds into the center)": spiral,
 "zigzag (one hallway that snakes back and forth)": lambda k:[(S_ if (i%k==k-1 and (i//k)%2==0) or (i%k==0 and (i//k)%2==1) else (E_ if (i//k)%2==0 else W_)) for i in range(k*k)],
 "comb (left column opens south and every other room opens west)": lambda k:[S_ if i%k==0 else W_ for i in range(k*k)],
 "nested rings (each layer of rooms is a clockwise loop)": rings,
 "staircases (east then south over and over)": lambda k:[E_ if (i//k+i%k)%2==0 else S_ for i in range(k*k)],
 "rows (every room opens east)": lambda k:[E_]*(k*k),
 "columns (every room opens south)": lambda k:[S_]*(k*k),
 "bricks (pairs of rooms that open toward each other)": lambda k:[E_ if (i%k)%2==0 else W_ for i in range(k*k)],
}
def seq_scores(digs):   # digs: function k -> list of k*k numbers read row by row
    return [score_dirs([d%4 for d in digs(k)],k) for k in SIZES]
def block_total(block):
    L=len(block); sc=[score_dirs([block[i%L] for i in range(k*k)],k) for k in SIZES]; return sum(sc),block,sc
if __name__=="__main__":
    out={"sizes":SIZES,"max_total":MAXT,"max_each":[2*k*k+4*k for k in SIZES]}
    out["shapes"]=[{"name":n,"scores":[score_dirs(f(k),k) for k in SIZES]} for n,f in SHAPES.items()]
    for s in out["shapes"]: s["total"]=sum(s["scores"]); print(s["name"],s["total"],s["scores"],flush=True)
    # natural sequences: the first k*k numbers fill the grid
    def small_primes(n):
        s=np.ones(4000,dtype=bool); s[:2]=False
        for i in range(2,64):
            if s[i]: s[i*i::i]=False
        return np.nonzero(s)[0][:n].tolist()
    P=small_primes(120); pdig=[int(c) for c in "".join(map(str,P))]
    import mpmath; mpmath.mp.dps=130
    def digs_of(x): return [int(c) for c in mpmath.nstr(x,120,strip_zeros=False).replace(".","")][:100]
    cnt=[int(c) for c in "".join(str(i) for i in range(1,80))]
    fib=[1,1]
    while len(fib)<100: fib.append(fib[-1]+fib[-2])
    NAT={"digits of the primes written in one row (2 3 5 7 1 1 1 3 ...)":pdig,"digits of pi (3 1 4 1 5 9 ...)":digs_of(mpmath.pi),"digits of e (2 7 1 8 2 8 ...)":digs_of(mpmath.e),
         "digits of the square root of 2 (1 4 1 4 2 1 ...)":digs_of(mpmath.sqrt(2)),"digits of the counting numbers written in one row (1 2 3 ... 9 1 0 1 1 ...)":cnt,
         "counting numbers with one whole number in each room (1 then 2 then 3 ...)":list(range(1,101)),"one whole prime in each room (2 then 3 then 5 ...)":P,
         "Fibonacci numbers with one whole number in each room (1 1 2 3 5 8 ...)":fib,"square numbers with one whole number in each room (1 4 9 16 ...)":[i*i for i in range(1,101)]}
    out["natural"]=[]
    for n,seq in NAT.items():
        sc=seq_scores(lambda k:seq[:k*k]); out["natural"].append({"name":n,"scores":sc,"total":sum(sc),"start":seq[:12]}); print(n,sum(sc),sc,flush=True)
    r=random.Random(11); tot=[sum(seq_scores(lambda k:[r.randrange(10) for _ in range(k*k)])) for _ in range(300)]
    out["random_average_total"]=sum(tot)/len(tot); out["random_best_total_of_300"]=max(tot); print("random",out["random_average_total"],max(tot))
    # every repeating block of doors up to 7 long
    blocks=[b for L in range(1,8) for b in itertools.product(range(4),repeat=L)]
    with mp.Pool(2) as pool: res=pool.map(block_total,blocks,chunksize=200)
    best={}
    for t,b,sc in res:
        # keep the shortest block for each repeated pattern
        key=tuple(b[i%len(b)] for i in range(420))
        if key not in best or len(b)<len(best[key][1]): best[key]=(t,b,sc)
    ranked=sorted(best.values(),key=lambda x:(-x[0],len(x[1]),x[1]))
    out["blocks_tested"]=len(blocks); out["distinct_patterns"]=len(ranked)
    out["top_blocks"]=[{"doors":list(b),"total":t,"scores":sc} for t,b,sc in ranked[:40]]
    out["best_by_length"]={str(L):[{"doors":list(b),"total":t,"scores":sc} for t,b,sc in ranked if len(b)==L][:3] for L in range(1,8)}
    for x in out["top_blocks"][:12]: print(x)
    json.dump(out,open("multi_size_scores_results.json","w"),indent=1)
