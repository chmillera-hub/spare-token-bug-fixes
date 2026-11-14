# Tests whether the half-angle rule for entangled pairs can come from geometry instead of being assumed.
# Rule tested: the far strip has a twist axis n. The detector points along b. A hidden direction u is
# drawn evenly from all directions in a space with d dimensions. The far strip "agrees" with the detector
# when u sits lower along b than the twist axis n does (u.b < n.b). Quantum physics needs cos^2(angle/2).
import numpy as np
from math import gamma, pi
rng=np.random.default_rng(11); N=1_000_000
def random_directions(d,n):
    v=rng.normal(size=(n,d)); return v/np.linalg.norm(v,axis=1,keepdims=True)
def agree_rate_sim(d,theta):
    u=random_directions(d,N); return np.mean(u[:,0]<np.cos(theta))      # b is the first axis
def agree_rate_exact(d,theta,steps=200001):
    if d==2:                                                                # a circle: the share falls in a straight line
        return 1-theta/pi
    x=np.linspace(-1,1,steps); w=(1-x**2)**((d-3)/2) if d!=3 else np.ones_like(x)
    c=np.cumsum((w[1:]+w[:-1])/2)*(x[1]-x[0]); c=np.concatenate([[0],c]); c/=c[-1]
    return float(np.interp(np.cos(theta),x,c))
def E_exact(d,theta): return -(2*agree_rate_exact(d,theta)-1)             # average of (result A times result B)
angles=[0,22.5,45,67.5,90,112.5,135,157.5,180]
print("share of pairs where the far strip agrees with its own twist axis")
print("angle   quantum   "+"   ".join(f"d={d} exact/sim" for d in (2,3,4,5)))
for deg in angles:
    th=np.radians(deg); row=f"{deg:6.1f}  {np.cos(th/2)**2:.4f}   "
    row+="   ".join(f"{agree_rate_exact(d,th):.4f}/{agree_rate_sim(d,th):.4f}" for d in (2,3,4,5)); print(row)
print("\nlargest gap from the quantum rule over all angles:")
grid=np.radians(np.linspace(0,180,721))
for d in (2,3,4,5,6,10):
    print(f"  d={d}: {max(abs(agree_rate_exact(d,t)-np.cos(t/2)**2) for t in grid):.4f}")
def chsh_std(d):
    a,a2,b,b2=0,pi/2,pi/4,3*pi/4; e=lambda x,y:E_exact(d,abs(x-y))
    return abs(e(a,b)-e(a,b2)+e(a2,b)+e(a2,b2))
def chsh_best(d):
    best=0
    for t in np.radians(np.linspace(1,89,353)):                          # detector directions 0, 2t, t, 3t
        e=lambda x:E_exact(d,x); best=max(best,abs(3*e(t)-e(3*t)))
    return best
print("\ncombined test score (pre-set models cannot pass 2.000; quantum physics tops out at 2.828):")
for d in (2,3,4,5,6,10,50):
    print(f"  d={d}: standard angles {chsh_std(d):.3f}   best angles {chsh_best(d):.3f}")
# full pair simulation in three dimensions with detector directions anywhere in space
def pair_3d(a,b,n=N):
    A=rng.choice([-1,1],n)                       # first result is an even coin flip
    axis=-A[:,None]*a[None,:]                    # the far strip gets the opposite twist axis for the whole ribbon
    u=random_directions(3,n)
    agree=(u@b)<(axis@b); B=np.where(agree,1,-1)
    return A,B
def unit(v): v=np.array(v,float); return v/np.linalg.norm(v)
print("\nfull pair run in three dimensions with detectors pointing anywhere in space:")
for a,b in [((0,0,1),(0,0,1)),((0,0,1),(1,0,1)),((1,2,2),(2,-1,0.5)),((0,0,1),(0,1,0)),((1,0,0),(-1,0.2,0))]:
    a,b=unit(a),unit(b); A,B=pair_3d(a,b)
    print(f"  angle {np.degrees(np.arccos(a@b)):6.1f}  quantum {-(a@b):+.4f}  simulated {np.mean(A*B):+.4f}  far-end average {np.mean(B):+.4f}")
