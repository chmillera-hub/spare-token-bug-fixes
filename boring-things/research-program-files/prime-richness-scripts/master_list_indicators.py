# Joins every result into one list and adds the sample-size indicators to each line:
# the wobble on the percentage and the odds that plain luck explains the gap from the number line.
import json, math, re
import mpmath as mp
E=json.load(open('master_list_first_version.json'))
for e in E:
    if e['tested'] is None:
        m=re.match(r'n³ ÷ (\d+)',e['label']); e['tested']=int(round((10**12*int(m.group(1)))**(1/3)))-3
def add(label,pct,tested,primes,chance,note=''):
    E.append(dict(label=label,pct=pct,tested=tested,primes=primes,chance=chance,note=note))
have={e['label'] for e in E}
for e in E:
    if e['label']=='n² + n + 3399714628553118047': e['note']='outputs have 19 digits and the equation is a known record from published research'
    if e['label']=='2 + (2 × n!) mod (n + 1)': e['note']='a known formula whose output is 2 for most inputs and repeated primes counted once'
for fn in ('running_sums_results.json','more_sums_results.json'):
    for r in json.load(open(fn)):
        lab=r['label']; note='outputs up to 300 digits' if r['steps']<300000 and 'digits of π' not in lab else ''
        if 'gaps between' in lab: note='circular because the recipe needs the list of primes to begin with'
        p=r['primes']; c=r['chance']
        if p[0]==p[1]==p[2] and r['plain']==r['bump']==r['carry']:
            add(lab,r['plain'],r['steps'],p[0],c[0],(note+' and ' if note else '')+'the bump changes nothing for these totals')
        else:
            add(lab,r['plain'],r['steps'],p[0],c[0],note)
            add(lab+' then bump each total',r['bump'],r['steps'],p[1],c[1],note)
            add(lab+' with the bump carried into the next addition',r['carry'],r['steps'],p[2],c[2],note)
for a,c,pct,pr,ch in ((15,24600021781,861,109706,11415.6),(15,190514189597,862,107017,11128.9),(3,473317155281,846,104947,11092.0),(3,404492439881,838,104578,11146.9)):
    add('start at %d then add %d + %d + %d and so on'%(c,2*a,4*a,6*a),pct,300000,pr,ch)
Z=((1,'piece',4,3.75,12,3.73),(1,'total',4,3.39,6,3.38),(2,'piece',1,4.01,7,3.99),(2,'total',6,3.48,12,3.46),(3,'piece',4,4.39,11,4.35),(3,'total',2,3.51,4,3.51))
sup={1:'',2:'²',3:'³'}
for s,kind,p0,c0,p1,c1 in Z:
    if kind=='piece': lab='the first n decimal digits of the zeta piece 1/n%s'%sup[s]
    else: lab='the first n digits of the zeta running total 1/1%s + 1/2%s + 1/3%s up to 1/n%s'%(sup[s],sup[s],sup[s],sup[s])
    add(lab,round((p0/c0-1)*100),2000,p0,c0,'positions 1 to 2000')
    add(lab+' then bump the last digit',round((p1/c1-1)*100),2000,p1,c1,'positions 1 to 2000')
REL={'the Lucas numbers (2 then 1 then 3 then 4 then 7 and so on)':'the list 2 then 1 then 3 then 4 then 7 where each number is the two before added up',
 'the Pell numbers (1 then 2 then 5 then 12 then 29 and so on)':'the list 1 then 2 then 5 then 12 then 29 where each number is twice the one before plus the one before that',
 'the Perrin numbers (3 then 0 then 2 then 3 then 2 then 5 and so on)':'the list 3 then 0 then 2 then 3 then 2 then 5 where each number is the second and third numbers before added up',
 'the Catalan numbers':'the count of ways to pair up n sets of brackets',
 'the Bell numbers':'the count of ways to sort n objects into groups',
 'n combined with half of n by the exclusive-or rule (Gray code)':'n combined with half of n by the exclusive-or rule'}
GM={'Equations famous for a long unbroken run of primes':'run','Equations from the published richness record lists':'rich','Equations famous for very few primes':'poor','Powers of n plus 1 and related equations':'pow','Recipes that start from the nth prime':'pr','Famous number lists':'lists','Digit tricks':'dig','Bit tricks':'bit','Mixed operations':'mix','Recipes built from the list of primes':'pr','Counting functions':'cnt','Geometry':'geo','Step-by-step rules':'step','Best fractions':'frac'}
for fn in ('meaty_results.json','weird_results.json'):
    for r in json.load(open(fn)):
        if r['label'].startswith('e to the power'): continue
        lab=REL.get(r['label'],r['label'])
        if fn.startswith('meaty') and lab in ('the nth prime + 2',): pass
        add(lab,r['pct'],r['tested'],r['primes'],r['expected'],r.get('note',''))
        E[-1]['g']=GM[r['group']]
labels={e['label'] for e in E}
SKIP1={'x + 1','x² + 1','x² + x + 1','x³ + x + 1','x³ + x² + 1','x⁴ + x + 1','x⁴ + x³ + x² + x + 1','x⁶ + x⁵ + x⁴ + x³ + x² + x + 1','x¹⁶ + 1','x⁸ + 1'}
GN={'Two variables and no numbers':'nv2','Three variables and no numbers':'nv3','One variable with every coefficient equal to 1':'ones'}
for r in json.load(open('no_numbers_results.json')):
    if r['label'] in SKIP1 or r['label'] in labels: continue
    add(r['label'],r['pct'],r['tested'],r['primes'],r['expected'],r.get('note','')); E[-1]['g']=GN[r['group']]; labels.add(r['label'])
gof={e['label']:e.get('g') for e in E}
for r in json.load(open('dead_bump_results.json')):
    base=r['label'].replace(' with decimals dropped','') if r['label'].startswith(('n² ÷','n³ ÷')) else r['label']
    base={'n × (n + 1) ÷ 2 (the totals of 1 + 2 + 3)':'n × (n + 1) ÷ 2'}.get(base,base)
    if base.startswith('the totals of'): continue
    lab=base+' then bump the last digit'
    if lab in labels: continue
    add(lab,r['bump'],r['tested'],r['primes_bump'],r['chance'],r.get('note','')); labels.add(lab)
    g=gof.get(base) or gof.get(base+' with decimals dropped')
    if base in ('2ⁿ ÷ 3','78557 × 2ⁿ + 1','509203 × 2ⁿ − 1','the whole numbers written side by side'): g=gof.get(base,g)
    if base=='3n²': g=None
    if g: E[-1]['g']=g
add('n² + n + 26853927251 fed inputs that are multiples of the 11 primes up to 300 that can divide an output',992,100000,7770,711.4,'outputs have about 62 digits'); E[-1]['g']='sq'
add('n² + n + 26853927251 fed inputs that are multiples of the 52 primes up to 1000 that can divide an output',1167,100000,1900,149.9,'outputs have about 292 digits'); E[-1]['g']='sq'
for r in json.load(open('lastdigit_results.json')):
    for d in ('1','3','7','9'):
        x=r[d]; add(r['label']+' with the last digit changed to '+d,x['pct'],x['tested'],x['primes'],x['chance'],'inputs 1 to 300000 in order'); E[-1]['g']='ld'
for r in json.load(open('famous_boost_results.json')):
    fast=r['screen_terms']<5000
    for t in r['top']:
        if t['confirm_chance']<=0: continue
        note='the rule was picked on an earlier stretch of the list and confirmed on these outputs'+(' which have 150 to 450 digits' if fast else '')
        add(r['name']+' then '+t['rule'],t['confirm_pct'],r['confirm_terms'],t['confirm_primes'],t['confirm_chance'],note); E[-1]['g']='fb'
def outof(s):
    if s<=0: return 'none'
    if s>0.995: return 'every output'
    if s>=0.095:
        best=min(((abs(a/b-s),b,a) for b in range(2,11) for a in range(1,b)),key=lambda t:(round(t[0],4),t[1]))
        return 'about %d of every %d'%(best[2],best[1])
    n=1/s
    if n>=100:
        mag=10**(len(str(int(n)))-2); n=round(n/mag)*mag
    return 'about 1 of every %d'%round(n)
def sh(x):
    x*=100
    return ('%.0f'%x if x>=10 else '%.1f'%x if x>=1 else '%.2f'%x if x>=0.1 else '%.3f'%x)+'%'
def luck(k,lam):
    if lam<=0: return None
    z=(k-lam)/math.sqrt(lam)
    if abs(z)>7: return 0.0
    if k>=lam: return float(mp.gammainc(k,0,lam,regularized=True)) if k>0 else 1.0   # chance of k or more
    return float(mp.gammainc(k+1,lam,mp.inf,regularized=True))                      # chance of k or fewer
def odds(p):
    if p is None: return 'not measurable because every output is below 2'
    if p<1e-9: return 'under 1 in a billion'
    if p>=0.095: return 'about %d in 100 which means the gap could be luck'%round(p*100)
    if p>=0.01: return 'about %d in 100'%max(1,round(p*100))
    n=1/p; mag=10**int(math.floor(math.log10(n))); n=int(round(n/mag))*mag
    return '1 in %d'%n
pc=lambda d:'0%' if d==0 else ('+' if d>0 else '−')+str(abs(d))+'%'
for e in E:
    k,lam=e['primes'],e['chance']
    p=luck(k,lam); e['p']=p
    err=100*math.sqrt(max(k,1))/lam if lam>0 else None
    e['err']=err
    n_=max(1,round(err)) if err is not None else 0; wob=('give or take %d point%s'%(n_,'' if n_==1 else 's')) if err is not None else ''
    s='%s: %s (%s). Tested %d outputs and found %d %s (%s of the outputs which is %s) where chance predicts %s (%s which is %s). Luck odds: %s.'%(e['label'],pc(e['pct']),wob,e['tested'],k,'prime' if k==1 else 'primes',sh(k/e['tested']),outof(k/e['tested']),('%.0f'%lam if lam>=100 else '%.1f'%lam),sh(lam/e['tested']),outof(lam/e['tested']),odds(p))
    if e['note']: s+=' Note: '+e['note'].replace('100000 inputs and the recipe needs factoring','the recipe needs a factoring step').replace('150 outputs tested','the recipe needs a search for the next prime').replace('20000 inputs tested','the count takes long to compute').replace('60000 outputs tested','fewer inputs fit the precision used')+'.'
    e['line']=s
E.sort(key=lambda e:(-e['pct'],e['label']))
json.dump(E,open('master.json','w'),ensure_ascii=False,indent=0)
print(len(E)); print(sum(1 for e in E if e['p'] is not None and e['p']>=0.095),'lines where the gap could be luck')
for e in E[:4]+[x for x in E if 'n! − 1' in x['label']][:1]+[x for x in E if x['label']=='n × π'][:1]+E[-2:]: print(e['line'])
