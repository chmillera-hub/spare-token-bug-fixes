import json, math, random, re, subprocess
from gmpy2 import mpz, is_prime, isqrt
random.seed(23)
E=[]   # (label, pct, tested, primes, chance, note)
def add(label,pct,tested,primes,chance,note=''):
    E.append(dict(label=label,pct=pct,tested=tested,primes=primes,chance=chance,note=note))
seen=set()
def norm(s): return s.replace(' ','')
# three recipes from the first table that repeat outputs: recount with each prime counted once
def distinct(f,nmax):
    s=set(); ex=0.0
    for n in range(2,300002):
        v=f(n)
        if v<2: continue
        ex+=min(1.0,1/math.log(v))
        if is_prime(mpz(v)): s.add(v)
    return len(s),ex
over={}
for lab,f,nm in (('n ÷ 2',lambda n:n//2,2*10**12),('√n',lambda n:int(isqrt(mpz(n))),10**12),('n ÷ ln(n)',lambda n:int(n/math.log(n)),3*10**10)):
    p,ex=distinct(f,nm); over[lab]=(p,ex)
R=json.load(open('equation_table_results.json')); RB=json.load(open('equation_table_bump_results.json'))
FAST='Fast-growing equations (tested on outputs up to 300 digits)'
for r in R:
    lab=r['label']; note=''
    if r['group']==FAST: note='outputs up to 300 digits'
    if lab in over:
        p,ex=over[lab]; add(lab,round((p/ex-1)*100),300000,p,ex,'inputs 2 to 300001 in order with repeated primes counted once'); 
    else: add(lab,round((r['score']-1)*100),r['tested'],r['primes'],r['expected'],note)
    seen.add(norm(lab))
for r in RB:
    note='outputs up to 300 digits' if r['group']==FAST else ''
    if r['label'] in over: continue
    add(r['label']+' then bump the last digit',round((r['score']-1)*100),r['tested'],r['primes'],r['expected'],note)
txt=subprocess.run(['python3','divide_table.py'],capture_output=True,text=True).stdout
for m in re.finditer(r'n\^(\d) / +(\d+) : +(\d+) primes where chance predicts +(\d+) : +([+-]\d+)%',txt):
    lab='n%s ÷ %s'%('²' if m.group(1)=='2' else '³',m.group(2))
    if norm(lab) in seen: continue
    add(lab,int(m.group(5)),300000 if m.group(1)=='2' else None,int(m.group(3)),float(m.group(4)))
for A,pct,p,ex in ((26853927251,859,116748,12173),(21425625701,842,115251,12237),(379580297267,840,105451,11221),(5384581877,830,116789,12554),(247757,725,107471,13030),(72491,640,96507,13034),(27941,630,95140,13036)):
    add('n² + n + %d'%A,pct,300000,p,ex)
add('n² + n + 3399714628553118047',972,300000,75368,7031,'outputs have 19 digits')
add('510510 × n + 1 (510510 is 2 × 3 × 5 × 7 × 11 × 13 × 17)',457,300000,62894,11295.3)
add('(the product of every prime up to 97) × n + 1',726,300000,25674,3107.7,'outputs have about 43 digits')
add('(the product of every prime up to 541) × n + 1',1030,300000,6534,578.4,'outputs have about 226 digits')
add('(the product of every prime up to 1009) × n + 1',1108,300000,3713,307.4,'outputs have about 425 digits')
add('51051 × n + 1 then bump the last digit (51051 is 3 × 7 × 11 × 13 × 17)',400,300000,63523,12706.5)
for r in json.load(open('wild_batch_results.json')):
    lab=r['label']
    if lab.endswith('with decimals dropped') and lab.startswith('n² ÷'): continue
    if lab=='sin(e to the n) ÷ ln(n)': r['note']='every output is 0 or −1'
    add(lab,r['pct'],r['tested'],r['primes'],r['expected'],r.get('note','') or ('repeated primes counted once' if r['repeats'] else ''))
C=(('π',4,3.98,8,3.98),('e',4,4.09,11,4.00),('φ (the golden ratio)',4,3.20,7,3.19),('√2',3,3.23,7,3.21),('√3',6,3.19,10,3.19),('ln 2',2,3.50,7,3.46))
for nm,p0,e0,p1,e1 in C:
    add('the leading digits of %s (first 1 digit then first 2 digits and so on)'%nm,round((p0/e0-1)*100),1200,p0,e0,'1200 numbers tested')
    add('the leading digits of %s then bump the last digit'%nm,round((p1/e1-1)*100),1200,p1,e1,'1200 numbers tested')
E.sort(key=lambda e:(-e['pct'],e['label']))
json.dump(E,open('master_list_data.json','w'),ensure_ascii=False,indent=0)
print(len(E)); 
for e in E[:12]+E[-3:]: print(e['pct'],e['label'],e['note'])
print(over)
