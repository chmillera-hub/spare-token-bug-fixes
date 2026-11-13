# Which knot comes out when a paper band with n half twists is cut lengthwise down the middle
# (written 12 November 2026 by an AI chatbot for the Mobius strip folder).
# The band: the center line is a circle of radius 2. The band turns n half twists on the way around.
# A cut down the middle of a band with an odd number of half twists leaves one long loop. The middle line of that
# long loop is the curve that runs at one quarter of the band width from the center and goes around twice.
# The program draws that curve as 1200 short straight pieces and measures three things with standard knot arithmetic:
#   crossings   = how many times the curve crosses over itself in a flat picture
#   determinant = a whole number that is 1 for a loop with no knot and 3 for the trefoil knot and 5 and 7 for the next knots
#   polynomial  = the Alexander polynomial at t=2 with powers of 2 removed (1 for no knot and 3 and 11 and 43 for the same knots)
# The same numbers are computed for the edge of the uncut band. Needs only Python with numpy.
import numpy as np
from fractions import Fraction
def curve(n, offset, laps, N=1200, hand=+1):
    th=np.linspace(0, 2*np.pi*laps, N, endpoint=False)
    r=np.stack([np.cos(th),np.sin(th),0*th],1); z=np.array([0,0,1.0])
    w=np.cos(n*th/2)[:,None]*r + hand*np.sin(n*th/2)[:,None]*z      # direction across the band
    return 2*r + offset*w
def crossings(P, rot_seed=1):
    rng=np.random.default_rng(rot_seed); Q,_=np.linalg.qr(rng.normal(size=(3,3))); X=P@Q.T   # look from a random direction
    N=len(X); A=X; B=np.roll(X,-1,0); out=[]
    for i in range(N):
        p=A[i,:2]; r=B[i,:2]-p
        for j in range(i+2,N):
            if i==0 and j==N-1: continue
            q=A[j,:2]; s=B[j,:2]-q; den=r[0]*s[1]-r[1]*s[0]
            if abs(den)<1e-14: continue
            t=((q-p)[0]*s[1]-(q-p)[1]*s[0])/den; u=((q-p)[0]*r[1]-(q-p)[1]*r[0])/den
            if 0<t<1 and 0<u<1:
                zi=A[i,2]+t*(B[i,2]-A[i,2]); zj=A[j,2]+u*(B[j,2]-A[j,2])
                sign=np.sign(den)*(1 if zi>zj else -1)      # +1 or -1 handedness of the crossing
                over,under=((i+t,j+u) if zi>zj else (j+u,i+t))
                out.append((over,under,int(sign)))
    return out
def invariants(P):
    C=crossings(P); k=len(C)
    if k==0: return 0,1,1,0
    unders=sorted(c[1] for c in C)                           # the curve is cut into arcs at every under-pass
    arc=lambda pos: int(np.searchsorted(unders,pos,side='right'))%k
    def matrix(t):
        M=[[Fraction(0)]*k for _ in range(k)]
        for row,(over,under,sign) in enumerate(C):
            a=arc(over); i_in=(arc(under)-1)%k; i_out=arc(under)
            # standard Alexander relation for a crossing (the roles of the two under arcs swap with the handedness)
            x,y=(i_in,i_out) if sign>0 else (i_out,i_in)
            M[row][a]+=1-t; M[row][x]+=t; M[row][y]+=-1
        return M
    def det_minor(M):
        A=[row[:-1] for row in M[:-1]]; n=len(A); d=Fraction(1)
        for c in range(n):
            p=next((r for r in range(c,n) if A[r][c]!=0),None)
            if p is None: return Fraction(0)
            if p!=c: A[c],A[p]=A[p],A[c]; d=-d
            d*=A[c][c]
            for r in range(c+1,n):
                f=A[r][c]/A[c][c]
                if f: A[r]=[a-f*b for a,b in zip(A[r],A[c])]
        return d
    det=abs(det_minor(matrix(Fraction(-1))))
    a2=abs(det_minor(matrix(Fraction(2))))
    while a2!=0 and a2.denominator==1 and a2.numerator%2==0: a2/=2
    while a2!=0 and a2.denominator%2==0: a2*=2
    return k,int(det),a2,sum(c[2] for c in C)
torus={1:(1,1),3:(3,3),5:(5,11),7:(7,43),9:(9,171)}        # known values for the knots named 3_1 5_1 7_1 9_1
names={1:"no knot",3:"trefoil knot (3 crossings)",5:"five-crossing knot",7:"seven-crossing knot",9:"nine-crossing knot"}
print("CUT DOWN THE MIDDLE of a band with an odd number of half twists (one long loop comes out)")
for n in (1,3,5,7,9):
    for hand in (+1,-1):
        k,det,a2,wr=invariants(curve(n,0.25,2,hand=hand))
        ok="matches" if (det,a2)==torus[n] else "DOES NOT MATCH"
        print(f"  {n} half twists twisted {'one way  ' if hand>0 else 'other way'}: crossings {k:2d}  determinant {det}  polynomial {a2}  crossing handedness total {wr:+d}  -> {ok} the {names[n]}")
print("\nEDGE of the uncut band with an odd number of half twists (the edge is one closed curve)")
for n in (1,3,5,7):
    k,det,a2,wr=invariants(curve(n,0.5,2))
    print(f"  {n} half twists: crossings {k:2d}  determinant {det}  polynomial {a2}  -> {'matches' if (det,a2)==torus[n] else 'DOES NOT MATCH'} the {names[n]}")
print("\nSAME CURVE SEEN FROM FIVE OTHER DIRECTIONS (3 half twists): the picture changes and the knot numbers stay")
P=curve(3,0.25,2)
for seed in (2,3,4,5,6):
    rng=np.random.default_rng(seed*7); Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    k,det,a2,wr=invariants(P@Q.T); print(f"  direction {seed}: crossings {k:2d}  determinant {det}  polynomial {a2}")
print("\nCUT OFF CENTER at one third of the width (3 half twists): the long loop that comes off")
k,det,a2,wr=invariants(curve(3,1/3,2)); print(f"  long loop: crossings {k}  determinant {det}  polynomial {a2}")
k,det,a2,wr=invariants(curve(3,0.0,1)); print(f"  center strip middle line: crossings {k}  determinant {det}  polynomial {a2}")
print("\nEVEN NUMBER of half twists cut down the middle gives two loops. Each loop alone:")
for n in (2,4,6):
    k,det,a2,wr=invariants(curve(n,0.25,1)); print(f"  {n} half twists: one loop alone has crossings {k}  determinant {det}  polynomial {a2}")
