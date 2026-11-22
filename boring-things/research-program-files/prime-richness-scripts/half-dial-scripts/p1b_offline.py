import numpy as np, mpmath, json
from mpmath import mp, mpf, mpc
from zfun import *
mp.dps = 30
k = (mpmath.sqrt(10-2*mpmath.sqrt(5))-2)/(mpmath.sqrt(5)-1)
def fm(s):
    return mpf(5)**(-s)*(mpmath.zeta(s,mpf(1)/5)+k*mpmath.zeta(s,mpf(2)/5)-k*mpmath.zeta(s,mpf(3)/5)-mpmath.zeta(s,mpf(4)/5))
T = 200.0
sig = np.arange(0.51, 2.51, 0.02)
tt = np.arange(0.5, T, 0.05)
S, TT = np.meshgrid(sig, tt, indexing='ij')
A = np.abs(mixed(S+1j*TT, N=400))
cands = []
for i in range(1, A.shape[0]-1):
    for j in range(1, A.shape[1]-1):
        a = A[i,j]
        if a < 0.2 and a <= A[i-1:i+2, j-1:j+2].min():
            cands.append((sig[i], tt[j], a))
print('candidates', len(cands))
found = []
for s0, t0, a in cands:
    try:
        r = mpmath.findroot(fm, mpc(s0, t0))
        if abs(fm(r)) < mpf(10)**-20 and mpmath.re(r) > 0.5001 and 0 < mpmath.im(r) < T:
            z = (float(mpmath.re(r)), float(mpmath.im(r)))
            if not any(abs(z[0]-q[0])<1e-6 and abs(z[1]-q[1])<1e-6 for q in found):
                found.append(z)
    except Exception as e:
        pass
found.sort(key=lambda z: z[1])
print('zeros right of the half dial with pitch below', T)
for z in found: print('  dial %.6f  pitch %.6f' % z)
# argument principle count on rectangle [0.505, 4] x [0.5, 200]
def path(a, b, n):
    return a + (b-a)*np.linspace(0, 1, n)
c1, c2, t1, t2 = 0.505, 4.0, 0.5, T
pts = np.concatenate([path(complex(c1,t1), complex(c2,t1), 20000),
                      path(complex(c2,t1), complex(c2,t2), 200000),
                      path(complex(c2,t2), complex(c1,t2), 20000),
                      path(complex(c1,t2), complex(c1,t1), 800000)])
vals = np.concatenate([mixed(p, N=400) for p in np.array_split(pts, 40)])
ang = np.unwrap(np.angle(vals))
wind = (ang[-1]-ang[0])/(2*np.pi)
print('winding number (zeros with dial > 0.505, pitch 0.5..200):', wind, 'max step', np.abs(np.diff(ang)).max())
json.dump({'offline': found, 'winding': float(wind)}, open('p1b.json','w'))
# leftover on the half dial near each off-line zero
d = np.load('W_line.npy'); tl, wr = d
for z in found:
    m = (tl > z[1]-0.6) & (tl < z[1]+0.6)
    seg_t, seg_w = tl[m], wr[m]
    # local extremum of |W| closest to the pitch (non crossing)
    ext = [i for i in range(1, len(seg_w)-1) if (seg_w[i]-seg_w[i-1])*(seg_w[i+1]-seg_w[i]) <= 0]
    best = min(ext, key=lambda i: abs(seg_t[i]-z[1]))
    print('near pitch %.3f: leftover on half dial turns around at pitch %.3f with value %+.4f' % (z[1], seg_t[best], seg_w[best]))
