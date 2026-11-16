import random
from collections import deque
PAY={('K','K'):(3,3),('K','H'):(0,5),('H','K'):(5,0),('H','H'):(1,1)}
L=20; THR=0.5; MINOBS=5; WINDOW=20
KIND=['always kind, no record check, never leaves',
      'always kind, checks the record and declines a partner who mostly harms, never leaves',
      'kind, no record check, leaves after 1 harm',
      'kind, checks the record and declines, also leaves after 1 harm']
HARM=['open harmer (always harms)',
      'careful harmer (harms 4 turns in 10 to keep a passable record)',
      'selfish learner (harms until declined 3 times and then plays kind)']
class A:
    def __init__(s,name): s.name=name; s.hist=deque(maxlen=WINDOW); s.pay=0.0; s.used=0; s.declined=0
    def move(s):
        n=s.name
        if n.startswith('open'): return 'H'
        if n.startswith('careful'): return 'H' if random.random()<0.4 else 'K'
        if n.startswith('selfish'): return 'K' if s.declined>=3 else 'H'
        return 'K'
    def accepts(s,o):
        if 'checks the record' not in s.name or len(o.hist)<MINOBS: return True
        return sum(1 for m in o.hist if m=='H')/len(o.hist) <= THR
    def leaves(s,their): return 'leaves after 1 harm' in s.name and their=='H'
def run(share,seed,matches=150000):
    random.seed(seed); nh=int(share*100)
    ag=[A(HARM[i%3]) for i in range(nh)]+[A(KIND[i%4]) for i in range(100-nh)]
    for _ in range(matches):
        a,b=random.sample(ag,2); a.used+=1; b.used+=1
        okA=a.accepts(b); okB=b.accepts(a)
        if not okA: b.declined+=1
        if not okB: a.declined+=1
        if not (okA and okB): continue
        for _ in range(L):
            ma=a.move(); mb=b.move(); a.hist.append(ma); b.hist.append(mb)
            pa,pb=PAY[(ma,mb)]; a.pay+=pa; b.pay+=pb; a.used+=1; b.used+=1
            if a.leaves(mb) or b.leaves(ma): break
    out={}
    for n in KIND+HARM:
        g=[x for x in ag if x.name==n]
        out[n]=sum(x.pay for x in g)/max(1,sum(x.used for x in g))
    return out
for sh in (0.1,0.5,0.8):
    acc={}
    for seed in range(5):
        for k,v in run(sh,seed).items(): acc[k]=acc.get(k,0)+v/5
    print('\nshare of harmers %.1f'%sh)
    for k,v in sorted(acc.items(),key=lambda x:-x[1]): print('   %.2f  %s'%(v,k))
