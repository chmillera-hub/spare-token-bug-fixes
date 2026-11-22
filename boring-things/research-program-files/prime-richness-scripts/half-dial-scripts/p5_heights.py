# Spread of ln|zeta| at great pitch heights for dials 0.5, 0.75, 1 using the
# "short row plus mirrored short row plus first remainder term" formula.
import numpy as np, sys, json, mpmath, time
from mpmath import mp, mpf, mpc
t0 = float(sys.argv[1]); L = float(sys.argv[2]); step = float(sys.argv[3])
LD = np.longdouble
TWO_PI = LD(2)*np.arctan(LD(1))*LD(4)
def theta_ld(t):
    t = t.astype(LD)
    return (t/2)*np.log(t/TWO_PI) - t/2 - TWO_PI/16 + 1/(48*t) + 7/(5760*t**3)
def psi(p):
    den = np.cos(2*np.pi*p)
    bad = np.abs(den) < 1e-6
    p2 = np.where(bad, p+1e-5, p)
    return np.cos(2*np.pi*(p2*p2 - p2 - 1/16))/np.cos(2*np.pi*p2)
sigs = [0.5, 0.75, 1.0]
def zeta_block(t):
    """t: float64 array (all with same N). returns dict sigma -> complex zeta"""
    a = t/(2*np.pi)
    N = int(np.floor(np.sqrt(a.min())))
    assert int(np.floor(np.sqrt(a.max()))) == N
    n = np.arange(1, N+1)
    ln_n = np.log(n.astype(LD))
    th = theta_ld(t)
    th64 = np.fmod(th, TWO_PI).astype(np.float64)
    p = np.sqrt(a) - N
    out = {s: np.zeros(t.shape, dtype=np.complex128) for s in sigs}
    D = {s: np.zeros(t.shape, dtype=np.complex128) for s in sigs}
    Dm = {s: np.zeros(t.shape, dtype=np.complex128) for s in sigs}
    tl = t.astype(LD)
    chunk = max(1, int(3e6 // len(t)))
    for i in range(0, N, chunk):
        ph = np.fmod(np.outer(tl, ln_n[i:i+chunk]), TWO_PI).astype(np.float64)
        E = np.exp(-1j*ph)
        nn = n[i:i+chunk].astype(np.float64)
        for s in sigs:
            D[s] += E @ nn**(-s)
            Dm[s] += np.conj(E) @ nn**(s-1)
    for s in sigs:
        chi = a**(0.5-s)*np.exp(-2j*th64)
        rem = (-1)**(N-1)*a**(-s/2)*np.exp(-1j*th64)*psi(p)
        out[s] = D[s] + chi*Dm[s] + rem
    return out
if __name__ == '__main__':
    mp.dps = 30
    # validation
    rng = np.random.default_rng(3)
    tv = t0 + np.sort(rng.uniform(0, min(L, 50), 6))
    Nv = np.floor(np.sqrt(tv/(2*np.pi)))
    tv = tv[Nv == Nv[0]]
    got = zeta_block(tv)
    worst = 0
    for s in sigs:
        for j, x in enumerate(tv):
            ex = complex(mpmath.zeta(mpc(s, mpf(float(x)))))
            worst = max(worst, abs(got[s][j]-ex))
    print('validation: worst absolute error vs mpmath', worst, flush=True)
    t = t0 + np.arange(0, L, step)
    Ns = np.floor(np.sqrt(t/(2*np.pi))).astype(int)
    res = {s: [] for s in sigs}
    st = time.time()
    for Nval in np.unique(Ns):
        tb = t[Ns == Nval]
        for part in np.array_split(tb, max(1, len(tb)//20000)):
            o = zeta_block(part)
            for s in sigs: res[s].append(np.abs(o[s]))
    out = {'t0': t0, 'L': L, 'step': step, 'n': len(t), 'valid_err': float(worst), 'secs': time.time()-st}
    for s in sigs:
        a = np.concatenate(res[s]); la = np.log(a)
        out['sig%s' % s] = dict(mean_ln=float(la.mean()), var_ln=float(la.var()), min_abs=float(a.min()))
    print(json.dumps(out))
    open('p5_%g.json' % t0, 'w').write(json.dumps(out))
