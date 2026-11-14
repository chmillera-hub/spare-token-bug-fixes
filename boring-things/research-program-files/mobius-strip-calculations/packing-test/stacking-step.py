from shapes import *
rng=np.random.default_rng(5)
D=rng.normal(size=(160,3)); D/=np.linalg.norm(D,axis=1)[:,None]
D=np.vstack([D,np.eye(3)])
S=np.arange(2*RAD+0.005,3.6,0.025)
for name,P in SH.items():
    P=P-P.mean(0); tr=cKDTree(P); best=(9,None)
    for d in D:
        for s in S:
            if s>=best[0]: break
            free=True
            for k in (1,2,3):
                dd,_=tr.query(P+k*s*d,k=1,distance_upper_bound=2*RAD)
                if np.isfinite(dd).any(): free=False;break
            if free: best=(s,d);break
    print(f'{name:30s} smallest stacking step {best[0]:.3f} direction {np.round(best[1],2)}',flush=True)
