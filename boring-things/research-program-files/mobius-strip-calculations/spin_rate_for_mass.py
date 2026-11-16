# Sample calculation: how fast a closed ribbon would need to circulate for
# the energy of the circulation alone to equal the measured mass of a particle.
# Assumptions: the ribbon circulates at the speed of light around a round loop,
# the loop carries the measured spin of one half unit (hbar/2),
# energy = momentum x c for a ribbon moving at light speed.
# Then: radius R = hbar/(2 m c), lap rate = c/(2 pi R) = 2 m c^2 / h,
# and a Mobius strip needs two laps to return right side up so
# full-return rate = m c^2 / h.
import math
hbar=1.054571817e-34; h=2*math.pi*hbar; c=299792458.0; eV=1.602176634e-19
lp=1.616255e-35
parts=[("neutrino (assumed 0.05 eV)",0.05),("electron",0.51099895e6),("muon",105.6583755e6),
       ("proton",938.27208816e6),("tau",1776.86e6),("top quark",172.57e9)]
for n,mev in parts:
    E=mev*eV; m=E/c**2
    R=hbar/(2*m*c); lap=c/(2*math.pi*R); ret=lap/2
    print(f"{n}: mass {m:.3e} kg | radius {R:.3e} m | circumference {2*math.pi*R:.3e} m = {2*math.pi*R/lp:.2e} Planck lengths | laps/s {lap:.3e} | full returns/s {ret:.3e} | max width (circ/1.732) {2*math.pi*R/math.sqrt(3):.3e} m")
# check: return rate equals Compton frequency m c^2/h
m=0.51099895e6*eV/c**2; print("electron Compton frequency", m*c**2/h)
# sub-light wheel check: edge speed needed for a rigid hoop of rest mass m with spin hbar/2 at radius r
for r in (2.8179e-15,1e-18):
    print("electron hoop radius",r,"edge speed / c =",hbar/(2*m*r)/c)
# split: spin supplies fraction x of the mass
for x in (1.0,0.99,0.5,0.01):
    mp=938.27208816e6*eV/c**2
    print("proton spin share",x,"radius",hbar/(2*x*mp*c),"laps/s",x*2*mp*c**2/h)
print("measured proton charge radius 8.41e-16 m ; ratio to single-loop radius", 8.41e-16/(hbar/(2*mp*c)))
