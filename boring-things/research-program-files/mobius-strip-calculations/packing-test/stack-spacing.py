from shapes import *
H=0.565
for name in ['flat ring','untwisted loop (hoop)','Mobius strip (1 half twist)','loop with 2 half twists','loop with 3 half twists']:
    P=SH[name]; P=P-P.mean(0)
    h=0.065 if name=='flat ring' else H
    col=np.vstack([P+[0,0,k*h] for k in range(-3,4)]); tr=cKDTree(col)
    ds=[]
    for th in np.linspace(0,np.pi,13)[:-1]:
        d=np.array([np.cos(th),np.sin(th),0])
        best=None
        for zshift in (0,h/2):
            for s in np.arange(0.3,3.2,0.02):
                dd,_=tr.query(P+s*d+[0,0,zshift],k=1,distance_upper_bound=2*RAD)
                if not np.isfinite(dd).any():
                    # make sure larger steps stay free (no nesting gaps counted wrongly): accept first free step
                    best=s if best is None else min(best,s); break
        ds.append(best)
    ds=np.array(ds); dm=ds.mean()
    print(f'{name:30s} column spacing min {ds.min():.2f} mean {dm:.2f} max {ds.max():.2f}  volume per piece about {0.866*dm*dm*h:.2f}')
print('straight flat strip volume per piece when tiled and stacked',round(L*W*0.065,2))
