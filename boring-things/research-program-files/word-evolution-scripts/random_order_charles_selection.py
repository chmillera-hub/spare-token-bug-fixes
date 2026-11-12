# Draws one random set of 16 key phrases from the Charles selection and prints the set in three random orders.
# No sorting is applied: each order is a plain shuffle.
import json,random
D=json.load(open('ph_charles.json'));u=D['u'];seq=D['seq'];sec=D['sec'];names=D['s']
import sys
N=int(sys.argv[1]) if len(sys.argv)>1 else 16
random.seed(int(sys.argv[2]) if len(sys.argv)>2 else 77)
pick=random.sample(range(len(seq)),N)
print('SET (with source chapter):')
for i in pick: print('  ',u[seq[i]],'  [',names[sec[i]],']')
for k in (1,2,3):
    o=pick[:];random.shuffle(o)
    print(f'\nORDER {k}: '+' | '.join(u[seq[i]] for i in o))
