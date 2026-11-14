import numpy as np
rng=np.random.default_rng(7); N=400000
def local_model(a,b):
    # each pair gets one shared hidden twist axis at the moment of the pinch; each detector reports
    # +1 if its direction is within 90 degrees of the local strip's axis, else -1; partner strip is opposite
    lam=rng.uniform(0,2*np.pi,N)
    A=np.sign(np.cos(a-lam)); B=-np.sign(np.cos(b-lam))
    return A,B
def whole_ribbon_model(a,b):
    # nothing is fixed before measurement; the first measurement (at A along a) sets the twist axis for the
    # whole ribbon, A's result is 50/50, B's strip is opposite about axis a; B measured along b agrees with
    # its own axis with probability cos^2(theta/2) (half-angle rule, assumed, echoing the two-lap property)
    A=rng.choice([-1,1],N)
    th=b-a
    same=rng.random(N)<np.cos(th/2)**2
    B=np.where(same,-A,A)
    return A,B
def E(model,a,b):
    A,B=model(a,b); return np.mean(A*B), np.mean(B)
print("angle  quantum(-cos)  local-pinch  whole-ribbon")
for deg in [0,22.5,45,67.5,90,135,180]:
    th=np.radians(deg)
    print(f"{deg:6.1f}  {-np.cos(th):+.3f}        {E(local_model,0,th)[0]:+.3f}       {E(whole_ribbon_model,0,th)[0]:+.3f}")
def chsh(model):
    a,a2,b,b2=0,np.pi/2,np.pi/4,3*np.pi/4
    return abs(E(model,a,b)[0]-E(model,a,b2)[0]+E(model,a2,b)[0]+E(model,a2,b2)[0])
print("combined test score (limit 2.000 for any pre-set model; quantum 2.828):")
print("  local-pinch :",round(chsh(local_model),3))
print("  whole-ribbon:",round(chsh(whole_ribbon_model),3))
print("can A send a message? average of B results for different A settings (whole-ribbon):",
      [round(E(whole_ribbon_model,x,1.0)[1],3) for x in (0,0.7,1.9,3.0)])
