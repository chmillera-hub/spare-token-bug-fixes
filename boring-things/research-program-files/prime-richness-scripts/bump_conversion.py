import random
from gmpy2 import is_prime
random.seed(44)
B={0:1,2:3,4:7,5:7,6:7,8:9}
def runA(nums):
    by={d:[0,0] for d in B}
    for n in nums:
        d=n%10
        if d not in B: continue
        by[d][1]+=1
        if is_prime(n-d+B[d]): by[d][0]+=1
    return by
def runB(nums):
    by={d:[0,0] for d in [2,4,5,6,8]}
    for n in nums:
        if is_prime(n): continue
        s=str(n); d=int(s[0])
        if d not in by: continue
        by[d][1]+=1
        if is_prime(int((str(B[d])+s[1:])[::-1])): by[d][0]+=1
    return by
def pr(tag,by):
    a=sum(x[0] for x in by.values()); b=sum(x[1] for x in by.values())
    print(tag,'ALL %.2f%% (%d of %d)'%(100*a/b,a,b),' '.join('%d:%.2f%%'%(d,100*x[0]/x[1]) for d,x in by.items()))
for k in [2,3,4,5,6]:
    nums=range(10**(k-1),10**k)
    pr(f'A {k}-digit',runA(nums)); pr(f'B {k}-digit',runB(nums))
for k in [9,12,18]:
    nums=[random.randrange(10**(k-1),10**k) for _ in range(600000)]
    pr(f'A {k}-digit',runA(nums)); pr(f'B {k}-digit',runB(nums))
# share of nonprimes that get changed, 6 digit
np=[n for n in range(100000,1000000) if not is_prime(n)]
print('share of 6-digit nonprimes with a trivial ending',sum(1 for n in np if n%10 in B)/len(np))
# a few examples
for n in [98765,123456,1000,2024,91,9990]:
    d=n%10; m=n-d+B.get(d,d); print(n,'->',m,bool(is_prime(m)))
