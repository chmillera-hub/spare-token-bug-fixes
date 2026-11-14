from shapes import *
BOX=8.0
for name,P0 in SH.items():
    P0=P0-P0.mean(0); res=[]
    for seed in (1,2):
        rng=np.random.default_rng(seed); pts=np.empty((0,3)); tree=None; n=0; fails=0; att=0
        while fails<500 and att<7000:
            att+=1
            Q=(P0@rot(rng).T+rng.uniform(0,BOX,3))%BOX
            ok=True
            if tree is not None:
                d,_=tree.query(Q,k=1,distance_upper_bound=2*RAD); ok=not np.isfinite(d).any()
            if ok:
                pts=np.vstack([pts,Q]); tree=cKDTree(pts,boxsize=BOX); n+=1; fails=0
            else: fails+=1
        res.append(n)
    print(f'{name:30s} placed {res}  mean {np.mean(res):.1f}',flush=True)
