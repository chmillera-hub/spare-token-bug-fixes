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
    s='%s: %s (%s). Tested %d outputs and found %d %s where chance predicts %s. Luck odds: %s.'%(e['label'],pc(e['pct']),wob,e['tested'],k,'prime' if k==1 else 'primes',('%.0f'%lam if lam>=100 else '%.1f'%lam),odds(p))
    if e['note']: s+=' Note: '+e['note']+'.'
    e['line']=s
E.sort(key=lambda e:(-e['pct'],e['label']))
json.dump(E,open('master.json','w'),ensure_ascii=False,indent=0)
print(len(E)); print(sum(1 for e in E if e['p'] is not None and e['p']>=0.095),'lines where the gap could be luck')
for e in E[:4]+[x for x in E if 'n! − 1' in x['label']][:1]+[x for x in E if x['label']=='n × π'][:1]+E[-2:]: print(e['line'])
