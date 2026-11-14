import numpy as np
from cut_pieces_linking import gauss
def ribbon(center, phi, s, laps=1, N=1500):
    # center(t) planar closed curve, frame angle phi(t) measured from in-plane normal toward z
    t=np.linspace(0,2*np.pi*laps,N*laps,endpoint=False)
    c=center(t); eps=1e-5
    tan=(center(t+eps)-center(t-eps)); tan/=np.linalg.norm(tan,axis=1)[:,None]
    nrm=np.stack([tan[:,1],-tan[:,0],0*t],1); z=np.array([0,0,1.0])
    ph=phi(t)
    return c+s*(np.cos(ph)[:,None]*nrm+np.sin(ph)[:,None]*z)
circle=lambda R,cx:(lambda t:np.stack([cx+R*np.cos(t),R*np.sin(t),0*t],1))
# parent: one loop holding a right-handed half twist then a left-handed half twist (net zero)
tm=lambda t:np.mod(t,2*np.pi)
bump=lambda t:np.where(tm(t)<np.pi, tm(t), 2*np.pi-tm(t))   # 0 -> pi -> 0
par=circle(3.0,0)
print("parent loop, linking of its two edges:", round(gauss(ribbon(par,bump,0.4),ribbon(par,bump,-0.4)),2))
# daughters after pinch-off: each closes on itself keeping its own half twist
up=lambda t:t/2      # +pi per lap
dn=lambda t:-t/2     # -pi per lap
A=circle(1.5,-2); B=circle(1.5,2)
print("daughter A core-to-edge linking:", round(gauss(ribbon(A,up,0.0),ribbon(A,up,0.4,laps=2)),2))
print("daughter B core-to-edge linking:", round(gauss(ribbon(B,dn,0.0),ribbon(B,dn,0.4,laps=2)),2))
