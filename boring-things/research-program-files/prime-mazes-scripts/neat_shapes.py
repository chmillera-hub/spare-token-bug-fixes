import os; os.environ["MAZE_RULE"]="zero-north"
from grid_tools import *
import itertools
N_,E_,S_,W_=0,1,2,3
def ring_dirs(k):
    d=[[None]*k for _ in range(k)]
    for L in range(k//2):
        a,b=L,k-1-L
        for c in range(a,b): d[a][c]=E_
        for r in range(a,b): d[r][b]=S_
        for c in range(b,a,-1): d[b][c]=W_
        for r in range(b,a,-1): d[r][a]=N_
    if k%2: d[k//2][k//2]=N_
    return [x for row in d for x in row]
def spiral_dirs(k):
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
        if i+1<len(path): nr,nc=path[i+1]
        else: nr,nc=path[i-1]
        d[r*k+c]=DR.index((nr-r,nc-c))
    return d
pats={
 "rows (every room opens east)": lambda k:[E_]*(k*k),
 "columns (every room opens south and the last room opens east)": lambda k:[S_]*(k*k-1)+[E_],
 "nested rings (each layer of rooms is a clockwise loop)": ring_dirs,
 "spiral (one hallway that winds into the center)": spiral_dirs,
 "staircases (east then south then east then south)": lambda k:[E_ if (i//k+i%k)%2==0 else S_ for i in range(k*k)],
 "comb (left column opens south and every other room opens west)": lambda k:[S_ if i%k==0 else W_ for i in range(k*k)],
 "bricks (pairs of rooms that open toward each other)": lambda k:[E_ if (i%k)%2==0 else W_ for i in range(k*k)] if k%2==0 else None,
 "zigzag (rows open east then west in turn and the row ends open south)": lambda k:[ (S_ if (i%k==k-1 and (i//k)%2==0) or (i%k==0 and (i//k)%2==1) else (E_ if (i//k)%2==0 else W_)) for i in range(k*k)],
}
def smallest_prime(dirs):
    opts=[OPTS[d] for d in dirs]; opts[0]=opts[0].replace("0","")
    if not set(opts[-1])&set("1379"): return None
    cnt=0
    for t in itertools.product(*opts):
        if t[-1] not in "1379": continue
        cnt+=1
        if gmpy2.is_prime(int("".join(t)),30): return "".join(t)
        if cnt>3_000_000: return None
    return None
out=[]
for name,f in pats.items():
    for k in (2,3,4,5,6):
        dirs=f(k)
        if dirs is None: continue
        p=smallest_prime(dirs)
        if p is None: print(name,k,"none"); continue
        adj=build(digits_to_dirs(p),k); comp,sizes=regions(adj); tb,lr=crossings(adj,k); lw=longest_walk(adj)
        out.append({"pattern":name,"k":k,"prime":p,"regions":len(sizes),"largest":max(sizes),"longest":lw,"tb":tb,"lr":lr})
        print(name,k,p,len(sizes),max(sizes),lw,tb,lr,flush=True)
json.dump(out,open("neat_shapes_results.json","w"),indent=1)
