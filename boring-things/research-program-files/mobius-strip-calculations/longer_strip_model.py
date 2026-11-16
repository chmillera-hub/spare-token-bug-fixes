# Sample calculation: mass stored along the length of the strip (base energy per length)
# instead of mass coming only from circulation.
# Energy per length used: 0.91 GeV per femtometer, the measured energy stored per length
# in the stretched strong-force field between quarks.
import math
c=299792458.0; T=0.91  # GeV per fm
amu=0.9315 # GeV per nucleon (average)
atoms=[("hydrogen",1,0.9383),("helium",4,3.7274),("carbon",12,11.175),("iron",56,52.09),("uranium",238,221.7)]
Rp=0.84 # fm measured proton radius
f_first_p=4.537e23
for n,A,m in atoms:
    L=m/T                       # strip length in fm
    lap_open=c/(L*1e-15)        # one big loop, edge at light speed
    turns=L/(2*math.pi*0.1655)  # coiled around a loop the size hydrogen's strip makes
    print(f"{n}: mass {m} GeV | strip length {L:.1f} fm | one big loop: radius {L/(2*math.pi):.2f} fm, {lap_open:.2e} laps/s | coiled on hydrogen-size loop: {turns:.1f} turns, {c/(0.9383/T*1e-15):.2e} laps/s | first model (shrinking loop): {f_first_p*m/0.9383:.2e} laps/s")
    print("    spin if every turn circulates same way (units of hydrogen loop spin):", round(turns,1), "| big loop spin grows as mass squared:", round((m/0.9383)**2,1))
print("nuclear radius formula 1.2*A^(1/3) fm: iron", 1.2*56**(1/3), "uranium", 1.2*238**(1/3))
