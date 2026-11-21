# Lists every prime where each reversed piece is prime (the first digit, then the first two digits
# written backward, and so on up to the whole number written backward). Needs gmpy2.
from gmpy2 import is_prime
level=[2,3,5,7]; chain=[]
while level:
    chain+=level; nxt=[]
    for p in level:
        m=10**len(str(p))
        for d in range(1,10):
            q=d*m+p
            if is_prime(q): nxt.append(q)
    level=nxt
print('primes where every right-end piece is prime:',len(chain),'largest',max(chain))
champs=sorted(int(str(q)[::-1]) for q in chain if is_prime(int(str(q)[::-1])))
print('primes where every reversed piece is prime:',len(champs),'largest',max(champs))
by={}
for c in champs: by[len(str(c))]=by.get(len(str(c)),0)+1
print('count by number of digits:',sorted(by.items()))
open('champions.txt','w').write('\n'.join(str(c) for c in champs)+'\n')
