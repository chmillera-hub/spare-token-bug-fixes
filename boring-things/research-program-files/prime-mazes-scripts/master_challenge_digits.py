"""Digit sequences on both tests. Circle part uses the block rule (read as many digits at a time as the circle size is written with),
circle sizes 2 to 1000 with 30 steps for each mark. Maze part: one digit in each room on grids 2 by 2 to 12 by 12."""
import os; os.environ["MAZE_RULE"]="zero-north"
import json, numpy as np, mpmath
from multi_size_scores import score_dirs
import max_score_points as m
NMAX=1000; PER=30; W=3; L=W*NMAX*PER
mpmath.mp.dps=L+50
def digs(x): return [int(c) for c in mpmath.nstr(x,L+20).split('.')[1][:L]]
PI=digs(mpmath.pi)
def circle(d):
    d=np.array(d[:L],dtype=np.int64); cum=lit=0.0; fc=fl=0
    for N in range(2,NMAX+1):
        w=len(str(N)); b=d[:(L//w)*w].reshape(-1,w)@(10**np.arange(w-1,-1,-1)); r=b[:PER*N]%N
        l=len(np.unique(r))/N; c=len(np.unique(np.cumsum(r)%N))/N; lit+=l; cum+=c; fl+=l==1; fc+=c==1
    n=NMAX-1; return round(100*cum/n,1),round(100*lit/n,1),int(fc),int(fl)
def maze(d):
    sc={k:score_dirs([x%4 for x in d[:k*k]],k) for k in range(2,11)}; pts=[k for k in range(2,13) if m.maxed([x%4 for x in d[:k*k]],k)]
    return sum(sc.values()),sc,pts
E=json.load(open('equal_digits_search_results.json')); B=json.load(open('large_grid_sequences_results.json'))
eq={c["k"]:c["digits"] for c in E["climb"]}
cands={
 "digits of pi alone":PI,
 "perfect 8 by 8 grid with equal digits and then the digits of pi":[int(c) for c in eq[8]]+PI,
 "perfect 6 by 6 grid with equal digits and then the digits of pi":[int(c) for c in eq[6]]+PI,
 "perfect 10 by 10 grid (random number improved digit by digit) and then the digits of pi":[int(c) for c in B["climb_10"][0]]+PI,
 "perfect 12 by 12 spiral and then the digits of pi":[int(c) for c in B["spiral_12"][0]]+PI,
 "16 digits that max 3 by 3 and 4 by 4 rooms (2332120331120333) and then the digits of pi":[int(c) for c in "2332120331120333"]+PI,
 "9 digits that max 2 by 2 and 3 by 3 rooms (150492837) and then the digits of pi":[int(c) for c in "150492837"]+PI,
 "repeating block 1590372648":[int("1590372648"[i%10]) for i in range(L)],
 "counting numbers written in a line (123456789101112)":[int(c) for c in "".join(str(i) for i in range(1,30000))][:L],
}
out=[]
for name,d in cands.items():
    cu,li,fc,fl=circle(d); tot,sc,pts=maze(d)
    out.append({"name":name,"cumulative":cu,"literal":li,"circle_out_of_200":round(cu+li,1),"circle_sizes_filled_cumulative":fc,"circle_sizes_filled_literal":fl,"maze_total_2_to_10":tot,"maze_scores":sc,"maze_sizes_maxed":pts,"first_digits":"".join(map(str,d[:30]))})
    print(out[-1],flush=True)
json.dump(out,open("master_challenge_digits_results.json","w"),indent=1)
