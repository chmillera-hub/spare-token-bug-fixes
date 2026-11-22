import numpy as np, mpmath, json
from mpmath import mp, mpf, mpc
from zfun import *
from scipy.special import loggamma
mp.dps = 25
out = {}
# (a) full pile of squared prime wobble at each dial: V = 1/2 sum_k P(2 k sigma)/k^2
print('--- full pile of squared prime wobble ---')
for sg in [2, 1.5, 1, 0.9, 0.8, 0.75, 0.7, 0.6, 0.55]:
    V = mpf(0); first = mpmath.primezeta(2*sg)
    for kk in range(1, 60):
        V += mpmath.primezeta(2*kk*sg)/kk**2
    out['V%s' % sg] = float(V/2)
    print('dial', sg, ' prime lamp total at fading power', 2*sg, '=', mpmath.nstr(first, 6), ' half of it', mpmath.nstr(first/2, 6), ' full pile', mpmath.nstr(V/2, 6))
# (b) zeros between pitch 100 and 3100
n1, n2 = mpmath.nzeros(100), mpmath.nzeros(3100)
print('zeros below 100:', n1, ' below 3100:', n2, ' between:', n2-n1)
out['nz'] = [int(n1), int(n2)]
# (c) refine minima along dials
from scipy.optimize import minimize_scalar
print('--- smallest leftover length along each dial, pitches 100..3100 ---')
for sg in ['2', '1.5', '1', '0.9', '0.8', '0.75', '0.7', '0.6', '0.55']:
    r = json.load(open('p2_%s.json' % sg))
    t0 = r['min_at']
    f = lambda t: float(abs(mpmath.zeta(mpc(float(sg), t))))
    m = minimize_scalar(f, bounds=(t0-0.05, t0+0.05), method='bounded', options={'xatol': 1e-9})
    print('dial', sg, 'grid min %.5f at %.2f  refined %.5f at %.4f' % (r['min_abs'], t0, m.fun, m.x), ' mean ln %.6f var %.4f' % (r['mean_ln'], r['var_ln']))
    out['min%s' % sg] = [m.fun, m.x]
# zeros near 1329 and near 1083 and 1735
for c in [1329.1, 1083.2, 1735.6]:
    k = int(mpmath.nzeros(c))
    zs = [float(mpmath.im(mpmath.zetazero(j))) for j in range(k-1, k+3)]
    avg = 2*np.pi/np.log(c/(2*np.pi))
    print('zeros around', c, [round(z, 4) for z in zs], ' average gap here %.4f' % avg, ' gaps', [round(zs[i+1]-zs[i], 4) for i in range(3)])
# (e) one prime factor averages to zero on the log scale
th = np.linspace(0, 2*np.pi, 2000001)[:-1]
for p, sg in [(2, 0.75), (2, 0.3), (3, 0.5), (7, 1.0)]:
    v = -np.log(np.abs(1 - p**(-sg)*np.exp(-1j*th)))
    print('prime', p, 'dial', sg, ': average of ln length of factor over a full turn = %.2e' % v.mean(), ' smallest factor %.4f largest %.4f' % (np.exp(v.min()), np.exp(v.max())), ' mean square of ln %.5f' % (v**2).mean())
# (f) rms miss of baseline and prime-steered pitches
r = json.load(open('p3.json'))
tr = np.array(r['true'])
print('baseline rms miss %.3f max %.3f' % (np.sqrt(((np.array(r['base'])-tr)**2).mean()), np.abs(np.array(r['base'])-tr).max()))
for X in [2, 3, 5, 7, 11, 13, 19, 31]:
    s = np.array([x[1] for x in r['X%d' % X]])
    print('primes up to', X, 'count', len(s), 'rms miss %.3f max %.3f' % (np.sqrt(((s-tr)**2).mean()), np.abs(s-tr).max()))
json.dump(out, open('p6.json', 'w'))
