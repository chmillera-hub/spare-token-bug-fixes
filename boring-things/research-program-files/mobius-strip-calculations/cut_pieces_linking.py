import numpy as np
def band_curve(n,s,R=3.0,N=1500):
    laps = 2 if (n%2==1 and abs(s)>1e-12) else 1
    t=np.linspace(0,2*np.pi*laps,N*laps,endpoint=False)
    r=R+s*np.cos(n*t/2)
    return np.stack([r*np.cos(t),r*np.sin(t),s*np.sin(n*t/2)],1)
def gauss(A,B):
    dA=np.roll(A,-1,0)-A; dB=np.roll(B,-1,0)-B
    mA=A+dA/2; mB=B+dB/2
    tot=0.0
    for i in range(len(mA)):
        r=mA[i]-mB
        d=np.linalg.norm(r,axis=1)**3
        tot+=np.sum(np.einsum('j,ij->i',dA[i],np.cross(dB,r))/d)
    return tot/(4*np.pi)
w=1.0
print("n  m  pieces: (inner,outer offsets) ; core-core linking ; edge-edge linking of each two-sided piece")
for n in [1,-1,2,3,4]:
    for m in [2,3,4,5]:
        # cut lines at offsets
        cuts=[-w+2*w*k/m for k in range(m+1)]
        if n%2:  # odd: pieces by |offset| intervals
            a=sorted(set(round(abs(c),9) for c in cuts))
            pieces=[(a[i],a[i+1]) for i in range(len(a)-1)]
            if abs(a[0])>1e-9: pieces=[(0.0,a[0])]+pieces  # central Mobius (core at 0)
            cores=[]
            for (lo,hi) in pieces:
                cores.append(0.0 if lo==0.0 and (m%2==1) else (lo+hi)/2)
        else:
            pieces=[(cuts[i],cuts[i+1]) for i in range(m)]
            cores=[(lo+hi)/2 for lo,hi in pieces]
        C=[band_curve(n,c) for c in cores]
        L=[[round(gauss(C[i],C[j]),2) for j in range(len(C)) if j>i] for i in range(len(C))]
        E=[]
        for (lo,hi),c in zip(pieces,cores):
            if n%2 and c==0.0:
                E.append(('mobius core-edge',round(gauss(band_curve(n,0.0),band_curve(n,hi)),2)))
            else:
                lo2=lo if abs(lo)>1e-9 else 1e-3
                E.append(('edges',round(gauss(band_curve(n,lo2),band_curve(n,hi)),2)))
        print(n,m,len(pieces),'pieces | core links',L,'| twist measure',E)
