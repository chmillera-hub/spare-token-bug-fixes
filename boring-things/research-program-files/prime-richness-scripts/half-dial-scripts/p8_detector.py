import numpy as np, json
from zfun import *
def pure(s, N=400, conj=False):
    s = np.asarray(s, dtype=np.complex128)
    j = -1j if conj else 1j
    return np.exp(-s*np.log(5.0))*(hurwitz(s,0.2,N=N)+j*hurwitz(s,0.4,N=N)-j*hurwitz(s,0.6,N=N)-hurwitz(s,0.8,N=N))
T = 200.0
off = [(0.808517, 85.699348), (0.650830, 114.163343), (0.574356, 166.479306), (0.724258, 176.702461)]
tt = np.arange(0.0005, T, 0.001)
print('dial   pure row avg   mirror-pattern pure row avg   blended row avg   counting-rule prediction for blended')
rows = []
for sg in [1.5, 1.0, 0.9, 0.75, 0.65, 0.6, 0.55, 0.51]:
    a = np.log(np.abs(pure(sg+1j*tt))).mean()
    b = np.log(np.abs(pure(sg+1j*tt, conj=True))).mean()
    c = np.log(np.abs(mixed(sg+1j*tt, N=400))).mean()
    pred = 2*np.pi*sum(max(0, be-sg) for be, ga in off)/T
    rows.append((sg, a, b, c, pred))
    print('%.2f   %+.5f   %+.5f   %+.5f   %.5f' % (sg, a, b, c, pred))
json.dump(rows, open('p8.json', 'w'))
# total zero counts by winding number on rectangle dial 0.02..4, pitch 0.5..200
def path(a, b, n): return a + (b-a)*np.linspace(0, 1, n)
c1, c2, t1, t2 = 0.02, 4.0, 0.5, T
pts = np.concatenate([path(complex(c1,t1), complex(c2,t1), 40000), path(complex(c2,t1), complex(c2,t2), 200000),
                      path(complex(c2,t2), complex(c1,t2), 40000), path(complex(c1,t2), complex(c1,t1), 400000)])
for name, f in [('pure', lambda p: pure(p)), ('mirror-pattern pure', lambda p: pure(p, conj=True)), ('blended', lambda p: mixed(p, N=400))]:
    vals = np.concatenate([f(p) for p in np.array_split(pts, 40)])
    a = np.unwrap(np.angle(vals))
    print(name, 'total zeros with dial between 0.02 and 4 and pitch 0.5..200:', (a[-1]-a[0])/(2*np.pi), ' max step', np.abs(np.diff(a)).max())
