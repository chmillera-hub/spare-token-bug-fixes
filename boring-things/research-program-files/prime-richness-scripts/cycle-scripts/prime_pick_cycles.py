# Does any rule that picks primes by position (every a-th prime or the prime in position n squared and so on)
# give last digits that repeat in a cycle?  For each picked list the program tries every cycle length and reports
# the best share of places where the last digit equals the last digit one cycle later.  A true cycle would give 100%.
# Four digits used equally and independently would give about 25%.
import numpy as np
N=20000000
s=np.ones(N+1,dtype=bool);s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0];D=(P%10).astype(np.int8)
print('primes found',len(P))
def best(seq,maxp,skip=5):
    seq=seq[skip:];L=len(seq);b=(0,0)
    for p in range(1,min(maxp,L//3)+1):
        m=float(np.mean(seq[:-p]==seq[p:]))
        if m>b[0]: b=(m,p)
    return b,L
worst=(0,None)
for a in range(1,61):
    for off in range(a):
        seq=D[off::a][:20000]
        (m,p),L=best(seq,400)
        if m>worst[0]: worst=(m,(a,off,p,L))
print('every a-th prime for a = 1 to 60 and every offset: highest match share %.2f%% at (a, offset, cycle length, list length) %s'%(100*worst[0],worst[1]))
rules={'position n squared':lambda n:n*n,'position n cubed':lambda n:n**3,'position n(n+1)/2':lambda n:n*(n+1)//2,'position n squared plus n plus 41':lambda n:n*n+n+41,'position 2 n squared minus 1':lambda n:2*n*n-1,'position 1000 n plus 7':lambda n:1000*n+7}
for name,f in rules.items():
    idx=[];n=1
    while f(n)<=len(P): idx.append(f(n)-1);n+=1
    seq=D[np.array(idx)]
    (m,p),L=best(seq,min(300,len(seq)//3))
    cnt=[int(np.sum(seq==d)) for d in (1,3,7,9)]
    # chance level for the best of that many cycle lengths: simulate
    rng=np.random.default_rng(1);sim=[]
    for t in range(200):
        r=rng.choice([1,3,7,9],size=len(seq));sim.append(best(r,min(300,len(seq)//3),0)[0][0])
    print('%s: %d primes picked, digit counts 1 3 7 9 = %s, highest match share %.2f%% at cycle length %d, random lists of the same length reach %.2f%% on average and %.2f%% at most'%(name,L,cnt,100*m,p,100*np.mean(sim),100*max(sim)))
# primes that are values of a polynomial: last digits of the primes of the form n squared plus 1
vals=[n*n+1 for n in range(1,400000)]
isp=[v for v in vals if v<=N and s[v]]
seq=np.array([v%10 for v in isp],dtype=np.int8)
(m,p),L=best(seq,300)
print('primes of the form n squared plus 1 below 20 million: %d primes, last digits used %s, highest match share %.2f%% at cycle length %d (two digits used equally would give 50%%)'%(L,sorted(set(seq.tolist())),100*m,p))
