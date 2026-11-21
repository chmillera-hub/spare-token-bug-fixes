# Compares each equation's prime percentage on small outputs with the percentage on 100-digit outputs.
import random, math, json
from gmpy2 import mpz, is_prime, log
random.seed(77)
EQ=[('n',1,lambda n:n),('2n + 1',1,lambda n:2*n+1),('6n + 1',1,lambda n:6*n+1),('30n + 1',1,lambda n:30*n+1),('210n + 1',1,lambda n:210*n+1),('510510n + 1',1,lambda n:510510*n+1),
('n² + 1',2,lambda n:n*n+1),('n² + n + 1',2,lambda n:n*n+n+1),('n² − n − 1',2,lambda n:n*n-n-1),('n² − 2',2,lambda n:n*n-2),('n² + 3',2,lambda n:n*n+3),('2n² − 1',2,lambda n:2*n*n-1),('4n² + 1',2,lambda n:4*n*n+1),('3n² + 3n + 1',2,lambda n:3*n*n+3*n+1),
('n² + n + 17',2,lambda n:n*n+n+17),('2n² + 29',2,lambda n:2*n*n+29),('n² + n + 41',2,lambda n:n*n+n+41),('n² + n + 27941',2,lambda n:n*n+n+27941),('n² + n + 247757',2,lambda n:n*n+n+247757),('n² + n + 26853927251',2,lambda n:n*n+n+26853927251),
('36n² − 810n + 2753',2,lambda n:36*n*n-810*n+2753),('103n² − 4707n + 50383',2,lambda n:103*n*n-4707*n+50383),('249582n² + 1',2,lambda n:249582*n*n+1),('n² + n − 501229',2,lambda n:abs(n*n+n-501229)),
('n³ + 2',3,lambda n:n**3+2),('n³ + n + 1',3,lambda n:n**3+n+1),('n³ − n + 1',3,lambda n:n**3-n+1),('3n³ − 183n² + 3318n − 18757',3,lambda n:abs(3*n**3-183*n*n+3318*n-18757)),('−66n³ + 3845n² − 60897n + 251831',3,lambda n:abs(-66*n**3+3845*n*n-60897*n+251831)),
('n⁴ + 1',4,lambda n:n**4+1),('n⁴ + n + 1',4,lambda n:n**4+n+1),('n⁴ − n² + 1',4,lambda n:n**4-n*n+1),('n⁴ + n³ + n² + n + 1',4,lambda n:n**4+n**3+n*n+n+1),('n⁵ + 2',5,lambda n:n**5+2),('n⁶ + 1091',6,lambda n:n**6+1091),('n⁸ + 1',8,lambda n:n**8+1),('n¹⁶ + 1',16,lambda n:n**16+1)]
def rate(vals):
    pr=0;ex=0.0
    for v in vals:
        v=mpz(v)
        if v<3: continue
        ex+=1/float(log(v))
        if is_prime(v,1): pr+=1
    return pr/ex
rows=[]
for label,deg,f in EQ:
    lo=rate(f(n) for n in range(1,100001))
    d=max(2,100//deg)
    hi=rate(f(random.randrange(10**(d-1),10**d)) for _ in range(40000))
    rows.append((label,lo,hi)); print('%-36s small %+5d%%   100 digits %+5d%%'%(label,round((lo-1)*100),round((hi-1)*100)),flush=True)
xs=[r[1] for r in rows]; ys=[r[2] for r in rows]; n=len(rows)
mx=sum(xs)/n; my=sum(ys)/n
r=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys))
def ranks(v):
    o=sorted(range(n),key=lambda i:v[i]); rk=[0]*n
    for k,i in enumerate(o): rk[i]=k
    return rk
rx,ry=ranks(xs),ranks(ys); m=(n-1)/2
rs=sum((a-m)*(b-m) for a,b in zip(rx,ry))/math.sqrt(sum((a-m)**2 for a in rx)*sum((b-m)**2 for b in ry))
print('equations',n,'correlation %.3f'%r,'rank correlation %.3f'%rs,'largest gap in points',max(abs(x-y)*100 for x,y in zip(xs,ys)))
json.dump(rows,open('low_high_results.json','w'),ensure_ascii=False)
# first 20 inputs only versus 100 digits
first=[rate(f(n) for n in range(1,21)) for label,deg,f in EQ]
mf=sum(first)/n
rf=sum((x-mf)*(y-my) for x,y in zip(first,ys))/math.sqrt(sum((x-mf)**2 for x in first)*sum((y-my)**2 for y in ys))
print('correlation using the first 20 inputs only %.3f'%rf)
