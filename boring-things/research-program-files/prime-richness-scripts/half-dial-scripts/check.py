# Recheck every figure in half-dial-questions.txt against saved program output.
import json, math, numpy as np, mpmath
from mpmath import mpc, pi
from zfun import *
from scipy.special import loggamma
txt = open('half-dial-questions.txt', encoding='utf-8').read()
bad = []
def need(st, why=''):
    if st not in txt:
        bad.append((st, why))
def sgn(x, d):  # signed with unicode minus
    r = ('%.' + str(d) + 'f') % abs(x)
    return ('+' if x > 0 else '−') + r
# --- Q1 averages
p2 = {k: json.load(open('p2_%s.json' % k)) for k in ['2','1.5','1','0.9','0.8','0.75','0.7','0.6','0.55','0.5','0.4','0.25','0']}
need('At the dial setting 2 the average is ' + sgn(p2['2']['mean_ln'], 5)[0:] )
need('At 1 the average is ' + sgn(p2['1']['mean_ln'], 5))
need('At 0.75 the average is ' + sgn(p2['0.75']['mean_ln'], 5))
need('At 0.6 the average is ' + sgn(p2['0.6']['mean_ln'], 6))
need('At 0.55 the average is ' + sgn(p2['0.55']['mean_ln'], 6))
need('At 0.5 the average is ' + sgn(p2['0.5']['mean_ln'], 5))
for k in ['0.4', '0.25', '0']:
    need('the average is %.4f' % p2[k]['mean_ln'], k)
m = p2['1']['mean_ln_t2pi']
need('is %.4f. So the ramp' % m)
need('0.1 × 5.3157 = %.4f' % (0.1*m)); need('0.25 × 5.3157 = %.4f' % (0.25*m)); need('0.5 × 5.3157 = %.4f' % (0.5*m))
need('= %.3f zeros for each unit of pitch' % (m/(2*math.pi)))
nz = json.load(open('p6.json'))['nz']
need('is %d which is %.3f for each unit' % (nz[1]-nz[0], (nz[1]-nz[0])/3000))
th = np.linspace(0, 2*np.pi, 200001)[:-1]
v = 1/np.abs(1 - 2**(-0.75)*np.exp(-1j*th))
need('a length of %.3f and a length of %.3f' % (v.min(), v.max()))
# --- Q2 piles
p6 = json.load(open('p6.json'))
for k, lab in [('2','Dial 2'),('1.5','Dial 1.5'),('1','Dial 1'),('0.9','Dial 0.9'),('0.8','Dial 0.8'),('0.75','Dial 0.75'),('0.7','Dial 0.7'),('0.6','Dial 0.6'),('0.55','Dial 0.55')]:
    lamps = float(mpmath.primezeta(2*float(k)))
    line = [l for l in txt.split('\n') if l.startswith('- ' + lab + ': the prime lamps total')]
    assert len(line) == 1, lab
    l = line[0]
    for val in ['%.4f' % lamps, '%.4f' % p6['V' + k], '%.4f' % p2[k]['var_ln']]:
        if val not in l: bad.append((val, lab))
need('the measured pile is %.3f.' % p2['0.5']['var_ln'])
h = {k: json.load(open('p5_%s.json' % k)) for k in ['1e+06', '1e+09', '1e+12']}
need('the pile is %.3f on the dial setting 1/2 and %.4f on 0.75 and %.4f on 1.' % (p2['0.5']['var_ln'], p2['0.75']['var_ln'], p2['1']['var_ln']))
for k, lab in [('1e+06', 'one million'), ('1e+09', 'one billion'), ('1e+12', 'one trillion')]:
    r = h[k]
    need('starting at %s: %.3f on 1/2 and %.4f on 0.75 and %.4f on 1.' % (lab, r['sig0.5']['var_ln'], r['sig0.75']['var_ln'], r['sig1.0']['var_ln']), lab)
    need('A stretch of %d starting at %s' % (r['L'], lab))
vs = [p2['0.5']['var_ln']] + [h[k]['sig0.5']['var_ln'] for k in ['1e+06', '1e+09', '1e+12']]
need('gained %.3f and then %.3f and then %.3f' % (vs[1]-vs[0], vs[2]-vs[1], vs[3]-vs[2]))
ll = [0.5*math.log(m), 0.5*math.log(math.log((1e6+7500)/(2*math.pi))), 0.5*math.log(math.log((1e9+5000)/(2*math.pi))), 0.5*math.log(math.log((1e12+750)/(2*math.pi)))]
need('is %.3f and %.3f and %.3f. The stretch' % (ll[1]-ll[0], ll[2]-ll[1], ll[3]-ll[2]))
# --- Q3 baseline
p3 = json.load(open('p3.json'))
need(' and '.join('%.2f' % x for x in p3['base'][:8]))
need(' and '.join('%.2f' % x for x in p3['true'][:8]))
def chi(s): return 2**s*pi**(s-1)*mpmath.sin(pi*s/2)*mpmath.gamma(1-s)
c = [float(abs(chi(mpc(0.7, t)))) for t in (14.52, 100, 1000)]
need('%.3f times as loud at the pitch 14.52 and %.3f times as loud at 100 and %.3f times as loud at 1000' % tuple(c))
tr = np.array(p3['true'])
def miss(lst): return math.sqrt(((np.array(lst)-tr)**2).mean())
need('- No primes: ' + ' and '.join('%.2f' % x for x in p3['base'][:5]) + '. The typical miss is %.2f.' % miss(p3['base']))
for X, lab in [(2, 'The prime 2'), (13, 'The primes up to 13'), (31, 'The primes up to 31')]:
    lst = [x[1] for x in p3['X%d' % X]]
    need('- ' + lab + ': ' + ' and '.join('%.2f' % x for x in lst[:5]) + '. The typical miss is %.2f.' % miss(lst), lab)
for X in [3, 7]:
    need('- The primes up to %d: the typical miss is %.2f.' % (X, miss([x[1] for x in p3['X%d' % X]])))
need('average %.2f so the primes' % ((tr[-1]-tr[0])/11))
f = lambda x: x/(2*math.pi)*(math.log(x/(2*math.pi))-1)+7/8
need('(%.1f at 14.52 and %.1f at 20.65 and %.1f at 25.49)' % tuple(f(x) for x in p3['base'][:3]))
# --- Q4 pair
p4 = json.load(open('p4.json'))
need('Zeros sit at %.4f and at %.4f' % (p4['z'][1], p4['z'][2]))
need('The gap is %.4f where the average gap at that height is %.4f so the two zeros are %.1f%% of an average gap apart' % (p4['gap'], p4['avg'], 100*p4['gap']/p4['avg']))
need('rises to +%.5f' % p4['Ztm'])
ex = p4['ext']; av = sorted(abs(b) for a, b in ex)
need('The %d humps between the pitches 6995 and 7015 have a middle size of %.2f' % (len(ex), av[len(av)//2]))
i = min(range(len(ex)), key=lambda j: abs(ex[j][1]))
need('reach −%.2f and −%.2f' % (abs(ex[i-1][1]), abs(ex[i+1][1])))
# --- Q5 blend
need('1 and %.4f and −%.4f and −1 and 0' % (KAPPA, KAPPA))
need('is −%.4f while the weight at 6 is 1' % (KAPPA*KAPPA))
sh = (1-1j*KAPPA)/2
need('a length of %.2f and the two shares are turned %.1f degrees' % (abs(sh), abs(math.degrees(np.angle(sh)))))
p1a = json.load(open('p1a.json')); p1b = json.load(open('p1b.json'))
assert max(p1a['mirror_rule_rel_err']) < 1e-26
need('to 27 digits at four test settings')
on = len(p1a['on_line_zeros']); off = p1b['offline']
need('The blended row has %d zeros. %d sit on 1/2 and %d sit to the right and %d sit to the left' % (on+2*len(off), on, len(off), len(off)))
assert abs(p1b['winding'] - len(off)) < 1e-6
for z in off:
    need('- Dial %.4f at the pitch %.3f.' % (z[0], z[1]))
def pure(s, N=400, conj=False):
    s = np.asarray(s, dtype=np.complex128); j = -1j if conj else 1j
    return np.exp(-s*np.log(5.0))*(hurwitz(s,0.2,N=N)+j*hurwitz(s,0.4,N=N)-j*hurwitz(s,0.6,N=N)-hurwitz(s,0.8,N=N))
tt = np.arange(0.005, 200, 0.005)
cnt = []
for cj in (False, True):
    w = np.exp(1j*(loggamma(0.75+0.5j*tt).imag + 0.5*tt*np.log(5/np.pi)))*pure(0.5+1j*tt, conj=cj)
    w = (w*np.exp(-1j*np.angle(w[1000]))).real
    cnt.append(int((np.sign(w[1:]) != np.sign(w[:-1])).sum()))
need('The quarter turn row has %d zeros and all %d sit' % (cnt[0], cnt[0]))
need('The swapped quarter turn row has %d zeros and all %d sit' % (cnt[1], cnt[1]))
need('gives %.1f.' % (200/(2*math.pi)*math.log(5*200/(2*math.pi*math.e))))
d = np.load('W_line.npy'); tl, wr = d
tv = []
for z in off:
    mk = (tl > z[1]-0.4) & (tl < z[1]+0.4); st, sw = tl[mk], wr[mk]
    e = [i for i in range(1, len(sw)-1) if (sw[i]-sw[i-1])*(sw[i+1]-sw[i]) <= 0]
    b = min(e, key=lambda i: abs(st[i]-z[1])); tv.append((st[b], sw[b]))
need('at %s near %.2f and at %s near %.2f and at %s near %.2f and at %s near %.2f' % (sgn(tv[0][1],3), tv[0][0], sgn(tv[1][1],3), tv[1][0], sgn(tv[2][1],3), tv[2][0], sgn(tv[3][1],3), tv[3][0]))
onz = p1a['on_line_zeros']; z = off[0][1]
lo = max(x for x in onz if x < z); hi = min(x for x in onz if x > z)
need('(%.2f near 85.70 where the average gap is %.2f)' % (hi-lo, 2*math.pi/math.log(5*z/(2*math.pi))))
p8 = json.load(open('p8.json'))
r = {row[0]: row for row in p8}
need('Dial 0.9: the blended row averages +%.4f and the counting rule predicts 0.' % r[0.9][3])
need('Dial 0.75: the blended row averages %.4f and the counting rule predicts %.4f.' % (r[0.75][3], r[0.75][4]))
for k in [0.65, 0.6, 0.55, 0.51]:
    need('- Dial %s: %.4f against a predicted %.4f.' % (k, r[k][3], r[k][4]), str(k))
lo8 = min(min(row[1], row[2]) for row in p8 if row[0] <= 0.9); hi8 = max(max(row[1], row[2]) for row in p8 if row[0] <= 0.9)
need('stayed between −%.4f and +%.4f' % (abs(lo8), hi8))
# --- Q6 minima
for k, lab in [('2','Dial 2'),('1.5','Dial 1.5'),('1','Dial 1'),('0.9','Dial 0.9'),('0.8','Dial 0.8'),('0.75','Dial 0.75'),('0.7','Dial 0.7'),('0.6','Dial 0.6'),('0.55','Dial 0.55')]:
    need('- %s: %.3f.' % (lab, p6['min' + k][0]), lab)
need('exactly 0 at %d pitches' % (nz[1]-nz[0]))
need('about %.2f in the stretch at one million and about %.2f in the stretch at one billion and about %.2f in the shorter stretch at one trillion' % tuple(h[k]['sig0.75']['min_abs'] for k in ['1e+06', '1e+09', '1e+12']))
need('about %.2f and %.2f and %.2f.' % tuple(h[k]['sig1.0']['min_abs'] for k in ['1e+06', '1e+09', '1e+12']))
print('minimum pitches', [round(p6['min' + k][1], 2) for k in ['0.8','0.75','0.7','0.6','0.55']])
# --- numbered list
need('36. 5.3157'); need('37. 0.846'); need('38. 0.2368'); need('40. 0.00397'); need('41. 0.2841'); need('42. 0.8085 and 85.699')
print('commas:', txt.count(','))
print('MISMATCHES:', len(bad))
for b in bad: print('  ', b)
