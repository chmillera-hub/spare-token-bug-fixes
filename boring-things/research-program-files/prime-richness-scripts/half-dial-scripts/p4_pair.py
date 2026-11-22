import mpmath, json
from mpmath import mp, mpf
mp.dps = 25
Z = mpmath.siegelz
z1 = mpmath.im(mpmath.zetazero(6709)); z2 = mpmath.im(mpmath.zetazero(6710))
z0 = mpmath.im(mpmath.zetazero(6708)); z3 = mpmath.im(mpmath.zetazero(6711))
print('zeros 6708..6711:', [mpmath.nstr(x, 10) for x in (z0, z1, z2, z3)])
gap = z2 - z1
avg = 2*mpmath.pi/mpmath.log(z1/(2*mpmath.pi))
print('gap', mpmath.nstr(gap, 6), 'average gap at this height', mpmath.nstr(avg, 6), 'ratio', mpmath.nstr(gap/avg, 4))
# extremum between the pair
tm = mpmath.findroot(lambda t: mpmath.diff(Z, t), (z1+z2)/2)
print('turning point at', mpmath.nstr(tm, 10), 'value', mpmath.nstr(Z(tm), 6))
# neighbouring humps for comparison
import numpy as np
ts = np.arange(6995, 7015, 0.002)
vals = np.array([float(Z(mpf(x))) for x in ts])
ext = [(ts[i], vals[i]) for i in range(1, len(ts)-1) if (vals[i]-vals[i-1])*(vals[i+1]-vals[i]) < 0]
print('turning values of the signed leftover between pitch 6995 and 7015:')
print([ (round(a,3), round(b,4)) for a,b in ext])
absv = [abs(b) for a,b in ext]
print('count', len(ext), 'median |turning value|', float(np.median(absv)), 'smallest', min(absv))
json.dump({'z':[float(z0),float(z1),float(z2),float(z3)], 'gap':float(gap), 'avg':float(avg), 'tm':float(tm), 'Ztm':float(Z(tm)),
           'ext':ext}, open('p4.json','w'))
