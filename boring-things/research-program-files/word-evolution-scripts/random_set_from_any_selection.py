# Draws N random key phrases from a phrase file and prints them in one random order with no sorting.
# Usage: python3 random_set.py ph_red.json 8 5
import json,random,sys
f,N,seed=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
D=json.load(open(f));u=D['u'];seq=D['seq'];sec=D['sec'];names=D['s']
random.seed(seed);pick=random.sample(range(len(seq)),N);random.shuffle(pick)
print(f,'ORDER: '+' | '.join(u[seq[i]] for i in pick));print('   sources: '+', '.join(names[sec[i]] for i in pick))
