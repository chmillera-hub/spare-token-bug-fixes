# Shared helpers: vectorized Hurwitz zeta by Euler-Maclaurin (numpy, double precision)
import numpy as np
from math import factorial
B2K = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]

def hurwitz(s, a=1.0, N=None, K=8):
    """zeta(s,a) = sum_{n>=0} (n+a)^-s for complex numpy array s (s != 1)."""
    s = np.asarray(s, dtype=np.complex128)
    if N is None:
        N = int(1.2*np.max(np.abs(s.imag)) + 40)
    out = np.zeros(s.shape, dtype=np.complex128)
    logs = np.log(np.arange(N) + a)
    # chunk over n to bound memory
    flat = s.ravel()
    acc = np.zeros(flat.shape, dtype=np.complex128)
    chunk = max(1, int(4e6 // max(1, flat.size)))
    for i in range(0, N, chunk):
        l = logs[i:i+chunk]
        acc += np.exp(-np.outer(flat, l)).sum(axis=1)
    x = N + a
    lx = np.log(x)
    xs = np.exp(-flat*lx)           # x^-s
    acc += x*xs/(flat-1) + xs/2
    term = flat*xs/x                # s * x^(-s-1)
    for k in range(1, K+1):
        acc += B2K[k-1]/factorial(2*k) * term
        term = term*(flat+2*k-1)*(flat+2*k)/(x*x)
    return acc.reshape(s.shape)

def zeta(s, **kw):
    return hurwitz(s, 1.0, **kw)

KAPPA = (np.sqrt(10-2*np.sqrt(5))-2)/(np.sqrt(5)-1)

def mixed(s, **kw):
    """Row with repeating weights 1, kappa, -kappa, -1, 0 (period 5)."""
    s = np.asarray(s, dtype=np.complex128)
    return np.exp(-s*np.log(5.0))*(hurwitz(s,0.2,**kw)+KAPPA*hurwitz(s,0.4,**kw)
                                   -KAPPA*hurwitz(s,0.6,**kw)-hurwitz(s,0.8,**kw))
