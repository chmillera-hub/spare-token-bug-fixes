"""Sequences that use the ten digits 0 to 9 equally often (0 opens north; door = digit mod 4).
Part 1: every repeating block of 10 digits that uses each digit once, scored on grids 2 by 2 to 10 by 10 and for maxed sizes 2 to 12.
Part 2: for each grid size the best grid found whose digits are spread as equally as possible, by swapping two digits at a time."""
import os; os.environ["MAZE_RULE"]="zero-north"
import itertools, json, random, time, multiprocessing as mp
from multi_size_scores import score_dirs, SIZES
import max_score_points as m
DIGITS={0:"048",1:"159",2:"26",3:"37"}
def to_digits(doors):
    use={k:list(v) for k,v in DIGITS.items()}; return "".join(use[d].pop(0) for d in doors)
def block_eval(b):
    sc=[score_dirs([b[i%10] for i in range(k*k)],k) for k in SIZES]; pts=[k for k in m.SIZES if m.maxed([b[i%10] for i in range(k*k)],k)]
    return sum(sc),b,sc,pts
def climb(k,seconds,seed):
    r=random.Random(seed); n=k*k; base=[i%10 for i in range(n)]
    extra=n%10
    if extra: base=[i%10 for i in range(n-extra)]+r.sample(range(10),extra)
    best=None; t0=time.time(); restarts=0
    while time.time()-t0<seconds:
        cur=base[:]; r.shuffle(cur)
        while cur[0]==0: r.shuffle(cur)
        cs=score_dirs([x%4 for x in cur],k); stale=0; restarts+=1
        while stale<6000 and time.time()-t0<seconds:
            i,j=r.randrange(n),r.randrange(n)
            if cur[i]%4==cur[j]%4 or (i==0 and cur[j]==0) or (j==0 and cur[i]==0): continue
            cur[i],cur[j]=cur[j],cur[i]; ns=score_dirs([x%4 for x in cur],k)
            if ns>=cs:
                stale=0 if ns>cs else stale+1; cs=ns
            else: cur[i],cur[j]=cur[j],cur[i]; stale+=1
            if cs==2*n+4*k: break
        if best is None or cs>best[0]: best=(cs,"".join(map(str,cur)))
        if cs==2*n+4*k: break
    cnt=[best[1].count(str(d)) for d in range(10)]
    return {"k":k,"score":best[0],"max":2*n+4*k,"digits":best[1],"count_of_each_digit":cnt,"restarts":restarts}
if __name__=="__main__":
    out={}
    blocks=sorted(set(itertools.permutations([0,0,0,1,1,1,2,2,3,3])))
    print(len(blocks),"door blocks",flush=True); t0=time.time()
    with mp.Pool(2) as pool:
        res=pool.map(block_eval,blocks,chunksize=200)
        print("blocks done",round(time.time()-t0),flush=True)
        cl=pool.starmap(climb,[(k,45 if k<8 else 110,k) for k in (4,5,6,7,8,9,10,12)])
    by_total=sorted(res,key=lambda x:-x[0]); by_pts=sorted(res,key=lambda x:(-len(x[3]),-x[0]))
    fmt=lambda x:{"doors":"".join(map(str,x[1])),"digits":to_digits(x[1]),"total":x[0],"scores":x[2],"maxed":x[3]}
    out["blocks_tested"]=len(blocks); out["top_by_total"]=[fmt(x) for x in by_total[:25]]; out["top_by_points"]=[fmt(x) for x in by_pts[:15]]
    out["points_tally"]={}
    for x in res:
        key=",".join(map(str,x[3])) or "none"; out["points_tally"][key]=out["points_tally"].get(key,0)+1
    out["average_total"]=sum(x[0] for x in res)/len(res); out["lowest_total"]=min(x[0] for x in res)
    # the counting block 0123456789 and the linear equations (a*n + b) mod 10
    lin=[]
    for a in (1,3,7,9):
        for b in range(10):
            blk=tuple(((a*n+b)%10)%4 for n in range(10)); e=block_eval(blk); lin.append({"equation":"(%d*n + %d) mod 10"%(a,b),"digits":"".join(str((a*n+b)%10) for n in range(10)),"total":e[0],"scores":e[2],"maxed":e[3]})
    out["linear_equations"]=sorted(lin,key=lambda x:-x["total"])
    out["climb"]=cl
    for x in out["top_by_total"][:8]: print(x)
    print("points",out["points_tally"],"avg",out["average_total"]); [print(x) for x in out["top_by_points"][:4]]
    [print(x) for x in out["linear_equations"][:5]]
    [print(x) for x in cl]
    json.dump(out,open("equal_digits_search_results.json","w"),indent=1)
