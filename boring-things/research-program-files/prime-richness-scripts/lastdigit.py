# Rule under test: replace the last digit of every output with one fixed digit (1 or 3 or 7 or 9)
# and compare with the usual bump (move the last digit up to the nearest of 1 3 7 9).
# Also counts the primes below 100 million by last digit. A repeated prime counts once.
import math, json
import numpy as np
from gmpy2 import mpz, is_prime, log
def chance(v): return 0.0 if v<2 else min(1.0,1/float(log(mpz(v))))
BM={0:1,2:3,4:7,5:7,6:7,8:9}
def bump(v):
    d=v%10; return v-d+BM.get(d,d)
def rate(vals,rule):
    seen=set(); ex=0.0; t=0
    for v in vals:
        t+=1
        if rule=='bump': v=bump(v)
        elif rule!='plain': v=v-v%10+rule
        if v<2: continue
        ex+=chance(v)
        if v not in seen and is_prime(mpz(v),5): seen.add(v)
    return t,len(seen),ex
N=300000
EQ=[('n',lambda n:n),('10n',lambda n:10*n),('2n',lambda n:2*n),('6n',lambda n:6*n),('30n',lambda n:30*n),('210n',lambda n:210*n),
('n²',lambda n:n*n),('n² − 1',lambda n:n*n-1),('n² + 1',lambda n:n*n+1),('n² + n',lambda n:n*n+n),('n² + n + 41',lambda n:n*n+n+41),
('n² ÷ 2 with decimals dropped',lambda n:n*n//2),('n × (n + 1) ÷ 2',lambda n:n*(n+1)//2),('n³',lambda n:n**3),('n⁴ + 4',lambda n:n**4+4),
('n × π with decimals dropped',lambda n:int(n*math.pi)),('n² × π with decimals dropped',lambda n:int(n*n*math.pi)),('2ⁿ mod n then plus n²',lambda n:n*n+pow(2,n,n))]
out=[]
for label,f in EQ:
    row=dict(label=label)
    for rule in ('plain','bump',1,3,7,9):
        t,p,ex=rate((f(n) for n in range(1,N+1)),rule)
        row[str(rule)]=dict(tested=t,primes=p,chance=ex,pct=round((p/ex-1)*100) if ex else -100)
    out.append(row)
    print('%-30s plain %+5d%% | bump %+5d%% | to 1 %+5d%% | to 3 %+5d%% | to 7 %+5d%% | to 9 %+5d%%'%(label,*[row[str(r)]['pct'] for r in ('plain','bump',1,3,7,9)]),flush=True)
json.dump(out,open('lastdigit_results.json','w'),ensure_ascii=False,indent=1)
# primes below 100 million by last digit
L=10**8
s=np.ones(L//2,dtype=bool); s[0]=False          # s[i] stands for the odd number 2i+1
for i in range(1,int(L**.5)//2+1):
    if s[i]: s[2*i*(i+1)::2*i+1]=False
odd=2*np.nonzero(s)[0]+1
cnt={d:int((odd%10==d).sum()) for d in (1,3,7,9)}
print('primes below 100 million by last digit',cnt,'total with 2 and 5',len(odd)+1)
json.dump(cnt,open('lastdigit_counts.json','w'))
