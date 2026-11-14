from shapes import *
import sys
rng=np.random.default_rng(1)
print('points per shape',{k:len(v) for k,v in SH.items()})
for name,P in SH.items():
    P=P-P.mean(0); tr=cKDTree(P); ext=np.linalg.norm(P,axis=1).max()
    hull=ConvexHull(np.vstack([P+[0,0,RAD],P-[0,0,RAD]]),qhull_options='QJ').volume
    B=2*ext+2*RAD; n=6000; hit=0
    for _ in range(n):
        Q=P@rot(rng).T+rng.uniform(-B,B,3)
        d,_=tr.query(Q,k=1,distance_upper_bound=2*RAD)
        hit+=np.isfinite(d).any()
    ex=hit/n*(2*B)**3
    print(f'{name:30s} reach {ext:.2f}  hull volume {hull:.2f}  pair excluded volume {ex:.2f}')
