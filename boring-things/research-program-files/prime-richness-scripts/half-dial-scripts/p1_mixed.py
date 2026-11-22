# Mixed row: weights repeat 1, kappa, -kappa, -1, 0 with period 5.
import numpy as np, mpmath, json
from mpmath import mp, mpf, mpc
from zfun import *
mp.dps = 30
k = (mpmath.sqrt(10-2*mpmath.sqrt(5))-2)/(mpmath.sqrt(5)-1)
def fm(s):
    return mpf(5)**(-s)*(mpmath.zeta(s,mpf(1)/5)+k*mpmath.zeta(s,mpf(2)/5)-k*mpmath.zeta(s,mpf(3)/5)-mpmath.zeta(s,mpf(4)/5))
out = {'kappa': float(k)}
# 1. mirror rule check: f(s) = 5^(1/2-s) * 2 (2 pi)^(s-1) Gamma(1-s) cos(pi s/2) f(1-s)
chk = []
for s in [mpc(0.3,7.1), mpc(0.8085,85.7), mpc(-0.4,33.3), mpc(0.62,150.2)]:
    lhs = fm(s)
    rhs = mpf(5)**(mpf(1)/2-s)*2*(2*mpmath.pi)**(s-1)*mpmath.gamma(1-s)*mpmath.cos(mpmath.pi*s/2)*fm(1-s)
    chk.append(float(abs(lhs-rhs)/abs(lhs)))
out['mirror_rule_rel_err'] = chk
print('mirror rule relative mismatch', chk)
# 2. real-valued leftover on the half dial
def vartheta(t):
    return float(mpmath.im(mpmath.loggamma(mpc(0.75, t/2))) + (t/2)*mpmath.log(5/mpmath.pi))
def W_mp(t):
    t = mpf(t)
    th = mpmath.im(mpmath.loggamma(mpc(0.75, t/2))) + (t/2)*mpmath.log(5/mpmath.pi)
    return mpmath.exp(1j*th)*fm(mpc(0.5,t))
for t in [3.3, 50.7, 85.7, 160.1]:
    w = W_mp(t); print('W', t, complex(w))
# numpy version
from scipy.special import loggamma
def W_np(t):
    t = np.asarray(t, dtype=float)
    th = loggamma(0.75+0.5j*t).imag + 0.5*t*np.log(5/np.pi)
    return (np.exp(1j*th)*mixed(0.5+1j*t, N=400))
T = 200.0
tt = np.arange(0.005, T, 0.005)
w = W_np(tt)
print('max |imag part| of W on grid', np.abs(w.imag).max())
wr = w.real
sc = np.where(np.sign(wr[1:]) != np.sign(wr[:-1]))[0]
zeros_on = []
for i in sc:
    r = mpmath.findroot(lambda x: mpmath.re(W_mp(x)), (tt[i], tt[i+1]), solver='anderson')
    zeros_on.append(float(r))
print('sign changes on half dial up to', T, ':', len(zeros_on))
print('first few', [round(z,4) for z in zeros_on[:8]])
out['on_line_zeros'] = zeros_on
np.save('W_line.npy', np.vstack([tt, wr]))
json.dump(out, open('p1a.json','w'))
