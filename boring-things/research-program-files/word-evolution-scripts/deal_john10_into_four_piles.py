# Deals the key phrases of John 10 into four random piles (whole phrases only) and prints each pile.
# Phrases that were neighbors in the chapter and landed in the same pile are printed joined.
import json,random
D=json.load(open('ph_john10.json'));u=D['u'];seq=D['seq']
random.seed(10)
idx=list(range(len(seq)));random.shuffle(idx)
piles=[sorted(idx[i::4]) for i in range(4)]
for n,p in enumerate(piles,1):
    out=[];cur=[p[0]]
    for a in p[1:]:
        if a==cur[-1]+1: cur.append(a)
        else: out.append(cur);cur=[a]
    out.append(cur)
    print(f"\n=== pile {n}: {len(p)} phrases, {sum(len(u[seq[i]].split()) for i in p)} words")
    print(' | '.join(' '.join(u[seq[i]] for i in c) for c in out))
