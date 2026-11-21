import random
from gmpy2 import is_prime
random.seed(33)
PI=[0,4,25,168,1229,9592,78498,664579,5761455,50847534,455052511,4118054813,37607912018]
dens={k:(PI[k]-PI[k-1])/(9*10**(k-1)) for k in range(1,13)}
B={'0':'1','1':'1','2':'3','3':'3','4':'7','5':'7','6':'7','7':'7','8':'9','9':'9'}
def pieces(n):
    s=str(n); s=B[s[0]]+s[1:]; out=[]
    for k in range(1,len(s)+1):
        t=s[:k][::-1]
        if t[0]=='0': continue
        out.append((k,int(t)))
    return out
def fair(k): return 0.5 if k==1 else 2.5*dens[k]
def show(n):
    ps=pieces(n); c=sum(1 for k,v in ps if is_prime(v)); e=sum(dens[k] for k,v in ps); f=sum(fair(k) for k,v in ps)
    print(n,'|',c,'of',len(ps),'| line',round(e,2),round((c/e-1)*100),'| fair',round(f,2),round((c/f-1)*100),'|',' '.join(f"{v}{'*' if is_prime(v) else ''}" for k,v in ps))
for n in [98765,123456789,2147483647,999999937,1234567891,8675309]: show(n)
N=200000; primes=[]
while len(primes)<N:
    n=random.randrange(10**11,10**12)
    if is_prime(n): primes.append(n)
byd={d:[0,0.0,0.0,0,0.0] for d in range(1,10)}
bylen={k:[0,0.0,0.0] for k in range(1,13)}
dist={}
for p in primes:
    d=int(str(p)[0]); c=0
    for k,v in pieces(p):
        ip=is_prime(v); c+=ip
        bylen[k][0]+=ip; bylen[k][1]+=dens[k]; bylen[k][2]+=fair(k)
        if k<12: byd[d][0]+=ip; byd[d][1]+=dens[k]; byd[d][2]+=fair(k)
        else: byd[d][3]+=ip; byd[d][4]+=fair(k)
    dist[c]=dist.get(c,0)+1
tp=sum(b[0] for b in bylen.values()); te=sum(b[1] for b in bylen.values()); tf=sum(b[2] for b in bylen.values())
print('overall vs line',round((tp/te-1)*100),'vs fair',round((tp/tf-1)*100))
print('by length vs line',' '.join(f'{k}:{round((a/e-1)*100):+d}%' for k,(a,e,f) in bylen.items()))
print('by length vs fair',' '.join(f'{k}:{round((a/f-1)*100):+d}%' for k,(a,e,f) in bylen.items()))
for d,(a,e,f,fa,ff) in byd.items(): print('orig lead',d,'partial vs line',round((a/e-1)*100),'vs fair',round((a/f-1)*100),'| full vs fair',round((fa/ff-1)*100))
print('dist',sorted(dist.items()))
best=sorted(primes,key=lambda n:-sum(1 for k,v in pieces(n) if is_prime(v)))[:3]
for n in best: show(n)
