# Along each dial setting: average of ln|zeta|, spread of ln|zeta|, smallest |zeta|, for pitches 100..3100
import numpy as np, sys, json
from zfun import *
sig = float(sys.argv[1]); step = float(sys.argv[2])
t = np.arange(100.0, 3100.0, step)
vals = []
for part in np.array_split(t, 30):
    vals.append(np.abs(zeta(sig+1j*part, N=3800)))
a = np.concatenate(vals)
la = np.log(a)
i = int(np.argmin(a))
res = dict(sig=sig, step=step, n=len(t), mean_ln=float(la.mean()), var_ln=float(la.var()),
           min_abs=float(a.min()), min_at=float(t[i]), mean_ln_t2pi=float(np.log(t/(2*np.pi)).mean()))
print(json.dumps(res))
open('p2_%s.json' % sys.argv[1], 'w').write(json.dumps(res))
