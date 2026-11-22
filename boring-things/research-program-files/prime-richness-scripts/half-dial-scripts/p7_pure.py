# Pure prime-product row with the pattern of five: weights 1, i, -i, -1, 0  (i = quarter turn)
import numpy as np, mpmath, json
from mpmath import mp, mpf, mpc
from zfun import *
from scipy.special import loggamma
def pure(s, N=400, conj=False):
    s = np.asarray(s, dtype=np.complex128)
    j = -1j if conj else 1j
    return np.exp(-s*np.log(5.0))*(hurwitz(s,0.2,N=N)+j*hurwitz(s,0.4,N=N)-j*hurwitz(s,0.6,N=N)-hurwitz(s,0.8,N=N))
# blend check: mixed = (1 - i k)/2 * pure + (1 + i k)/2 * pure_conj
s = np.array([0.3+7j, 0.8+85.7j, 1.2+33j])
b = (1-1j*KAPPA)/2*pure(s) + (1+1j*KAPPA)/2*pure(s, conj=True)
print('blend mismatch', np.abs(b - mixed(s, N=400)).max())
print('blend shares: length of each share', abs((1-1j*KAPPA)/2), ' turn in degrees', np.degrees(np.angle((1-1j*KAPPA)/2)))
# weights multiply? pure: w(2)*w(3) vs w(6); mixed: same
wp = {0:0, 1:1, 2:1j, 3:-1j, 4:-1}
wm = {0:0, 1:1, 2:KAPPA, 3:-KAPPA, 4:-1}
print('pure:  w(2)*w(3) =', wp[2]*wp[3], ' w(6) =', wp[6%5], '; w(2)*w(2) =', wp[2]*wp[2], ' w(4) =', wp[4])
print('mixed: w(2)*w(3) =', wm[2]*wm[3], ' w(6) =', wm[6%5], '; w(2)*w(2) =', wm[2]*wm[2], ' w(4) =', wm[4])
T = 200.0
tt = np.arange(0.005, T, 0.005)
res = {}
for conj in [False, True]:
    th = loggamma(0.75+0.5j*tt).imag + 0.5*tt*np.log(5/np.pi)
    w = np.exp(1j*th)*pure(0.5+1j*tt, conj=conj)
    # fixed turn that makes it real
    ang = np.angle(w[1000]); 
    # w = e^{i a} * real  -> remove angle a (mod pi)
    w2 = w*np.exp(-1j*ang)
    print('conj' if conj else 'pure', ' fixed turn removed (degrees) %.4f' % np.degrees(ang), ' max |imag| after', np.abs(w2.imag).max())
    wr = w2.real
    sc = np.where(np.sign(wr[1:]) != np.sign(wr[:-1]))[0]
    print('  sign changes on the half dial below pitch 200:', len(sc), ' first few', [round(float(tt[i]), 3) for i in sc[:6]])
    # winding number right of dial 0.505
    def path(a, b, n): return a + (b-a)*np.linspace(0, 1, n)
    c1, c2, t1, t2 = 0.505, 4.0, 0.5, T
    pts = np.concatenate([path(complex(c1,t1), complex(c2,t1), 20000), path(complex(c2,t1), complex(c2,t2), 200000),
                          path(complex(c2,t2), complex(c1,t2), 20000), path(complex(c1,t2), complex(c1,t1), 800000)])
    vals = np.concatenate([pure(p, conj=conj) for p in np.array_split(pts, 40)])
    a = np.unwrap(np.angle(vals))
    print('  winding number right of dial 0.505:', (a[-1]-a[0])/(2*np.pi), ' max step', np.abs(np.diff(a)).max())
    # winding number left of dial 0.495 down to -0.0? (zeros between dial 0 and 0.495)
    c1, c2 = 0.02, 0.495
    pts = np.concatenate([path(complex(c1,t1), complex(c2,t1), 20000), path(complex(c2,t1), complex(c2,t2), 800000),
                          path(complex(c2,t2), complex(c1,t2), 20000), path(complex(c1,t2), complex(c1,t1), 400000)])
    vals = np.concatenate([pure(p, conj=conj) for p in np.array_split(pts, 40)])
    a = np.unwrap(np.angle(vals))
    print('  winding number between dial 0.02 and 0.495:', (a[-1]-a[0])/(2*np.pi), ' max step', np.abs(np.diff(a)).max())
    res['conj' if conj else 'pure'] = int(len(sc))
print('count formula (T/2pi) ln(5T/(2 pi e)) at T=200:', T/(2*np.pi)*np.log(5*T/(2*np.pi*np.e)))
# mixed row: kind of turning point near each off-line zero
d = np.load('W_line.npy'); tl, wr = d
for z in [85.699348, 114.163343, 166.479306, 176.702461]:
    m = (tl > z-0.4) & (tl < z+0.4)
    st, sw = tl[m], wr[m]
    ext = [i for i in range(1, len(sw)-1) if (sw[i]-sw[i-1])*(sw[i+1]-sw[i]) <= 0]
    b = min(ext, key=lambda i: abs(st[i]-z))
    kind = 'peak' if sw[b] > sw[b-1] else 'valley'
    print('pitch %.3f: %s at %.3f with value %+.4f' % (z, kind, st[b], sw[b]))
# nearest on-line zeros around each off-line pitch
on = json.load(open('p1a.json'))['on_line_zeros']
for z in [85.699348, 114.163343, 166.479306, 176.702461]:
    lo = max(x for x in on if x < z); hi = min(x for x in on if x > z)
    print('off-line pitch %.3f sits between half-dial silences at %.3f and %.3f (gap %.3f)' % (z, lo, hi, hi-lo))
print('average gap of the mixed row near pitch 100: %.3f' % (2*np.pi/np.log(5*100/(2*np.pi))))
