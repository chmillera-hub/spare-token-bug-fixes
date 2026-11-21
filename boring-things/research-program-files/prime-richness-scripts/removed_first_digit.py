import random
from gmpy2 import is_prime
random.seed(5)
base=(455052511-50847534)/(9*10**9)*0+ (4118054813-455052511)/(9*10**10)
cnt={d:[0,0] for d in range(1,10)}
n=0
while n<600000:
    p=random.randrange(10**11,10**12)
    if not is_prime(p): continue
    s=str(p)
    if s[1]=='0': continue
    n+=1; d=int(s[0]); cnt[d][1]+=1
    if is_prime(int(s[1:])): cnt[d][0]+=1
for d in cnt:
    a,b=cnt[d]; print(d,b,a,round((a/b/base-1)*100))
