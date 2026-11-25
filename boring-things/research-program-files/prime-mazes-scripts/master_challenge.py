"""Master challenge: one sequence of whole numbers scored on the two circle test and on the maze test.
Circle part (out of 200): for every circle size from 2 to 200 marks the sequence gets 30 steps for each mark; the cumulative circle
uses the running total and the literal circle uses the term itself; the score adds the two average shares of marks reached.
Maze part (out of 984): one whole number in each room (door = number mod 4 with 0 north) on grids 2 by 2 to 10 by 10; three part score."""
import os; os.environ["MAZE_RULE"]="zero-north"
import math, json, time, multiprocessing as mp
import numpy as np
from multi_size_scores import score_dirs, SIZES
import equation_search as equations
NMAX=200; PER=30; K=NMAX*PER
def circle(seq):
    a=np.array(seq[:K],dtype=object)
    try: a=np.array(seq[:K],dtype=np.int64)
    except OverflowError: pass
    cum=lit=0.0
    for N in range(2,NMAX+1):
        t=a[:PER*N]
        if a.dtype==object: r=np.array([int(x)%N for x in t],dtype=np.int64)
        else: r=np.mod(t,N)
        lit+=len(np.unique(r))/N; cum+=len(np.unique(np.mod(np.cumsum(r),N)))/N
    c=NMAX-1; return 100*cum/c,100*lit/c
def maze(seq): return [score_dirs([int(x)%4 for x in seq[:k*k]],k) for k in SIZES]
def evaluate(item):
    name,seq=item; cu,li=circle(seq); mz=maze(seq); cp=(cu+li)/2; mpct=100*sum(mz)/984
    return {"name":name,"cumulative":round(cu,1),"literal":round(li,1),"circle_out_of_200":round(cu+li,1),"maze_total":sum(mz),"maze_percent":round(mpct,1),
            "average_percent":round((cp+mpct)/2,1),"lower_percent":round(min(cp,mpct),1)}
def named():
    n=np.arange(1,K+1,dtype=np.int64); sign=np.where(n%2==1,1,-1)
    s=np.ones(25*K,dtype=bool); s[:2]=False
    for i in range(2,int((25*K)**.5)+1):
        if s[i]: s[i*i::i]=False
    primes=np.flatnonzero(s)[:K]; comps=np.flatnonzero(~s)[2:][:K]
    sqf=np.ones(2*K+100,dtype=bool); sqf[0]=False
    for q in range(2,int((2*K+100)**.5)+1): sqf[q*q::q*q]=False
    div=np.zeros(K+1,dtype=np.int64)
    for d in range(1,K+1): div[d::d]+=1
    import mpmath; mpmath.mp.dps=K+20; pid=[int(c) for c in mpmath.nstr(mpmath.pi,K+5)[2:K+2]]
    fib=[1,1]
    while len(fib)<K: fib.append(fib[-1]+fib[-2])
    L=lambda x:[int(v) for v in x]
    return [("1 + 1 + 1 + 1 (steady 1)",[1]*K),("1 + 2 + 3 + 4 (counting numbers)",L(n)),("1 - 2 + 3 - 4 (counting numbers with flipping signs)",L(n*sign)),
     ("1 + 3 + 5 + 7 (odd numbers)",L(2*n-1)),("1 - 3 + 5 - 7 (odd numbers with flipping signs)",L((2*n-1)*sign)),("2 + 4 + 6 + 8 (even numbers)",L(2*n)),
     ("1 + 3 + 6 + 10 (triangular numbers)",L(n*(n+1)//2)),("1 + 4 + 9 + 16 (squares)",L(n*n)),("1 - 4 + 9 - 16 (squares with flipping signs)",L(n*n*sign)),("1 + 8 + 27 + 64 (cubes)",L(n**3)),
     ("2 + 3 + 5 + 7 (primes)",L(primes)),("2 - 3 + 5 - 7 (primes with flipping signs)",L(primes*sign)),("4 + 6 + 8 + 9 (composite numbers)",L(comps)),("4 - 6 + 8 - 9 (composite numbers with flipping signs)",L(comps*sign)),
     ("1 + 2 + 2 + 4 (gaps between neighboring primes)",L(np.diff(np.flatnonzero(s))[:K])),("1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece)",L(np.flatnonzero(sqf)[:K])),
     ("1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n)",L(div[1:])),("1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2)",[math.isqrt(2*k*k) for k in range(1,K+1)]),
     ("1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio)",[(k+math.isqrt(5*k*k))//2 for k in range(1,K+1)]),
     ("0 + 1 + 3 + 5 + 8 (whole part of n times the natural logarithm of n)",[int(k*math.log(k)) for k in range(1,K+1)]),("1 + 2 + 5 + 8 + 11 (whole part of n times the root of n)",[int(k*math.sqrt(k)) for k in range(1,K+1)]),
     ("1 + 4 + 1 + 5 + 9 (digits of pi after the decimal point)",pid),("1 + 1 + 2 + 3 + 5 (Fibonacci numbers)",fib),
     ("repeating block 0 3 3 0 1 0 0 (best short block from the maze test)",[[0,3,3,0,1,0,0][i%7] for i in range(K)]),
     ("repeating block 1 5 9 0 3 7 2 6 4 8 (best block with equal digits from the maze test)",[int("1590372648"[i%10]) for i in range(K)])]
if __name__=="__main__":
    t0=time.time(); out={}
    out["named"]=sorted([evaluate(x) for x in named()],key=lambda r:-r["average_percent"])
    for r in out["named"]: print(r,flush=True)
    equations.N=K; F=equations.families(); print(len(F),"equations",round(time.time()-t0),flush=True)
    with mp.Pool(2) as pool: res=pool.map(evaluate,F,chunksize=50)
    out["equations_tested"]=len(F)
    out["top_average"]=sorted(res,key=lambda r:-r["average_percent"])[:30]; out["top_lower"]=sorted(res,key=lambda r:-r["lower_percent"])[:30]
    print("--- top by average"); [print(r) for r in out["top_average"][:12]]
    print("--- top by lower"); [print(r) for r in out["top_lower"][:12]]
    json.dump(out,open("master_challenge_results.json","w"),indent=1); print(round(time.time()-t0),"seconds")
