"""Search simple equations a(n) whose outputs fill door grids of every size (0 opens north; door = a(n) mod 4; n counts rooms from 0).
For each equation: total three part score on grids 2 by 2 to 10 by 10 (highest possible 984) and points = grid sizes from 2 to 12 that are maxed."""
import os; os.environ["MAZE_RULE"]="zero-north"
import math, json, time, multiprocessing as mp
from multi_size_scores import score_dirs, SIZES
import max_score_points as mpnt
N=144
def evaluate(item):
    name,seq=item; d=[x%4 for x in seq]
    sc=[score_dirs(d[:k*k],k) for k in SIZES]; pts=[k for k in mpnt.SIZES if mpnt.maxed(d[:k*k],k)]
    return name,sum(sc),sc,pts
def families():
    out=[]
    for m in range(2,15):
        for a in range(m):
            for b in range(m):
                for c in range(m):
                    if a==0: continue
                    out.append(("(%d*n*n + %d*n + %d) mod %d"%(a,b,c,m),[(a*n*n+b*n+c)%m for n in range(N)]))
    for q in range(2,41):
        for p in range(1,3*q+1):
            if math.gcd(p,q)==1: out.append(("floor(%d*n / %d)"%(p,q),[(p*n)//q for n in range(N)]))
    for q in range(2,80):
        for p in range(1,8): 
            if math.gcd(p,q)==1: out.append(("floor(%d*n*n / %d)"%(p,q),[(p*n*n)//q for n in range(N)]))
    for a in range(1,400): out.append(("floor(sqrt(%d*n))"%a,[math.isqrt(a*n) for n in range(N)]))
    for q in range(1,40): out.append(("floor(n*sqrt(n) / %d)"%q,[int(n*math.sqrt(n)/q) for n in range(N)]))
    for a in range(2,12):
        for m in range(3,60): out.append(("%d^n mod %d"%(a,m),[pow(a,n,m) for n in range(N)]))
    for q in range(1,30): out.append(("n*(n+1)/2 divided by %d and rounded down"%q,[(n*(n+1)//2)//q for n in range(N)]))
    for a in range(1,60):
        for b in range(a+1,60): out.append(("floor(n/%d) + floor(n/%d)"%(a,b),[n//a+n//b for n in range(N)]))
    return out
if __name__=="__main__":
    F=families(); t0=time.time(); print(len(F),"equations",flush=True)
    with mp.Pool(2) as pool: res=pool.map(evaluate,F,chunksize=100)
    print(round(time.time()-t0),"seconds")
    by_total=sorted(res,key=lambda x:-x[1]); by_pts=sorted(res,key=lambda x:(-len(x[3]),-x[1]))
    out={"equations_tested":len(F),"top_by_total":[{"equation":n,"total":t,"scores":sc,"maxed":p} for n,t,sc,p in by_total[:40]],
         "top_by_points":[{"equation":n,"total":t,"scores":sc,"maxed":p} for n,t,sc,p in by_pts[:40]]}
    fam={}
    for n,t,sc,p in by_total:
        key=n.split("(")[0]+("sqrt" if "sqrt" in n else "")+("mod" if "mod" in n else "")+("^" if "^" in n else "")+("nn" if "n*n" in n else "")+("+" if "+ floor" in n else "")+("tri" if "n+1" in n else "")
        fam.setdefault(key,[]).append({"equation":n,"total":t,"scores":sc,"maxed":p})
    out["best_in_each_family"]=[v[0] for v in fam.values()]
    for x in out["top_by_total"][:15]: print(x)
    print("--- by points"); [print(x) for x in out["top_by_points"][:10]]
    print("--- families"); [print(x) for x in out["best_in_each_family"]]
    json.dump(out,open("equation_search_results.json","w"),indent=1)
