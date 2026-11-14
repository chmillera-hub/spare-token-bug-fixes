import numpy as np
from scipy.spatial import cKDTree, ConvexHull
L=2*np.pi; W=0.5; R=1.0; SP=0.035; RAD=0.03   # strip length, width, loop radius, point spacing, half thickness
def band(k):
    # closed band with k half twists; k=0 gives a hoop (untwisted loop standing like a bracelet)
    nu=int(L/SP); nv=int(W/SP)+1
    u=np.linspace(0,2*np.pi,nu,endpoint=False); v=np.linspace(-W/2,W/2,nv)
    U,V=np.meshgrid(u,v,indexing='ij'); a=k*U/2
    x=(R+V*np.sin(a))*np.cos(U); y=(R+V*np.sin(a))*np.sin(U); z=V*np.cos(a)
    return np.c_[x.ravel(),y.ravel(),z.ravel()]
def flat_ring():
    nu=int(L/SP); nv=int(W/SP)+1
    u=np.linspace(0,2*np.pi,nu,endpoint=False); v=np.linspace(-W/2,W/2,nv)
    U,V=np.meshgrid(u,v,indexing='ij')
    return np.c_[((R+V)*np.cos(U)).ravel(),((R+V)*np.sin(U)).ravel(),np.zeros(U.size)]
def straight():
    nu=int(L/SP); nv=int(W/SP)+1
    U,V=np.meshgrid(np.linspace(-L/2,L/2,nu),np.linspace(-W/2,W/2,nv),indexing='ij')
    return np.c_[U.ravel(),V.ravel(),np.zeros(U.size)]
SH={'straight flat strip':straight(),'flat ring':flat_ring(),'untwisted loop (hoop)':band(0),'Mobius strip (1 half twist)':band(1),'loop with 2 half twists':band(2),'loop with 3 half twists':band(3)}
def rot(rng):
    q=rng.normal(size=4); q/=np.linalg.norm(q); a,b,c,d=q
    return np.array([[a*a+b*b-c*c-d*d,2*(b*c-a*d),2*(b*d+a*c)],[2*(b*c+a*d),a*a-b*b+c*c-d*d,2*(c*d-a*b)],[2*(b*d-a*c),2*(c*d+a*b),a*a-b*b-c*c+d*d]])
