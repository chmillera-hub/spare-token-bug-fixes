# Follow-up tests for the half-angle finding page (written 12 November 2026 by an AI chatbot).
# Rule under test: a hidden direction u is evenly random in a space with d dimensions. The far strip has a
# twist arrow n. A detector points along b. The far strip "agrees" when u.b < n.b.
# Test 1: exact formulas for the combined test score (the CHSH score) in each count of dimensions.
# Test 2: a full pair run in d dimensions that checks whether the far-end average stays at zero.
# Test 3: the arrow-averaging test. Two different mixes of twist arrows with the same average arrow are
#         compared. Quantum physics says the two mixes cannot be told apart by any detector.
import numpy as np
from math import gamma, pi, sqrt, asin
rng=np.random.default_rng(2026); N=2_000_000
def dirs(d,n):
    v=rng.normal(size=(n,d)); return v/np.linalg.norm(v,axis=1,keepdims=True)
def F_numeric(d,c,steps=400001):                 # share of random directions with height below c
    if d==2: return 1-np.arccos(np.clip(c,-1,1))/pi
    x=np.linspace(-1,1,steps); w=(1-x**2)**((d-3)/2)
    cs=np.concatenate([[0],np.cumsum((w[1:]+w[:-1])/2)]); cs/=cs[-1]
    return float(np.interp(c,x,cs))
def F_closed(d,c):                                # closed formulas for d = 2 to 5
    if d==2: return 1-np.arccos(c)/pi
    if d==3: return (1+c)/2
    if d==4: return 0.5+(c*sqrt(1-c*c)+asin(c))/pi
    if d==5: return 0.5+(3*c-c**3)/4
print("TEST 1  combined test score at the standard detector angles (0 and 90 degrees against 45 and 135 degrees)")
closed={2:("2",2.0),3:("2 times the square root of 2",2*sqrt(2)),4:("2 plus 4 divided by pi",2+4/pi),5:("5 divided by the square root of 2",5/sqrt(2))}
c=1/sqrt(2)
for d in range(2,13):
    num=4*(2*F_numeric(d,c)-1)
    line=f"  d={d:2d}: numeric {num:.4f}"
    if d in closed: line+=f"   closed formula {closed[d][1]:.4f} ({closed[d][0]})   formula check {4*(2*F_closed(d,c)-1):.4f}"
    print(line)
# large-d limit: height times sqrt(d) tends to a bell curve, so the score tends to 4
for d in (50,200,1000): print(f"  d={d}: numeric {4*(2*F_numeric(d,c,2000001)-1):.4f}")
print("\n  best score over all four-direction layouts in one plane (search over angle step t with directions 0, 2t, t, 3t)")
for d in (2,3,4,5,6):
    E=lambda th: 2*F_numeric(d,np.cos(th),100001)-1
    best=max((abs(3*E(t)-E(3*t)),np.degrees(t)) for t in np.radians(np.linspace(1,89,177)))
    print(f"  d={d}: best {best[0]:.4f} at step {best[1]:.1f} degrees")
print("\nTEST 2  full pair run in d dimensions (first result is an even coin flip and sets the far twist arrow)")
def pair(d,a,b,n=N):
    A=rng.choice([-1,1],n); axis=-A[:,None]*a[None,:]; u=dirs(d,n)
    B=np.where((u@b)<(axis@b),1,-1); return A,B
for d in (2,3,4,5,6):
    out=[]
    for deg in (0,30,45,90,135):
        a=np.zeros(d); a[0]=1; b=np.zeros(d); b[0]=np.cos(np.radians(deg)); b[1]=np.sin(np.radians(deg))
        A,B=pair(d,a,b); out.append(f"{deg}deg corr {np.mean(A*B):+.4f} far avg {np.mean(B):+.4f}")
    print(f"  d={d}: "+" | ".join(out))
print("\nTEST 3  arrow averaging. Mix one: twist arrow 60 degrees left of straight up half the time and 60 degrees right half the time.")
print("        Mix two: twist arrow straight up three quarters of the time and straight down one quarter of the time.")
print("        Both mixes have the same average arrow (half length and straight up). Detector points straight up.")
for d in (2,3,4,5,6,10):
    m1=F_numeric(d,0.5); m2=0.75*F_numeric(d,1.0)+0.25*F_numeric(d,-1.0)
    # simulation of mix one
    u=dirs(d,N); sim1=np.mean(u[:,0]<0.5)
    print(f"  d={d:2d}: mix one agrees {m1:.4f} (simulated {sim1:.4f})   mix two agrees {m2:.4f}   gap {abs(m1-m2):.4f}")
print("\n        same test with the detector tilted 40 degrees away from straight up")
t=np.radians(40)
for d in (2,3,4,5,6):
    h1a=np.cos(np.radians(60)-t); h1b=np.cos(np.radians(60)+t)      # heights of the two mix-one arrows along the detector
    m1=0.5*F_numeric(d,h1a)+0.5*F_numeric(d,h1b); m2=0.75*F_numeric(d,np.cos(t))+0.25*F_numeric(d,-np.cos(t))
    print(f"  d={d}: mix one agrees {m1:.4f}   mix two agrees {m2:.4f}   gap {abs(m1-m2):.4f}")
