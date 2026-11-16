import random
PAY={('K','K'):(3,3),('K','H'):(0,5),('H','K'):(5,0),('H','H'):(1,1)}
L=20; BUDGET=20000; SEARCH=1
# Each turn both players post an intended move in a buffer. Both see both intentions.
# A buffer user who sees an intended harm can veto the turn (nobody is paid, the turn is spent) or leave.
# binding=True: the posted move is the move played. binding=False: a liar can post K and play H.
class P:
    def __init__(s,name): s.name=name; s.vetoed=0; s.harmed=0; s.t=0
    def post(s):
        n=s.name
        if n.startswith('open harmer'): return 'H'
        if n.startswith('selfish learner'):          # tries harm, switches to kind once a harm attempt is vetoed
            return 'K' if s.vetoed>=1 else 'H'
        return 'K'
    def real(s,posted,binding):
        if s.name.startswith('lying harmer') and not binding: return 'H'
        return posted
    def react(s,their_post):                       # returns 'go','veto','leave'
        n=s.name
        if 'reads the buffer' not in n: return 'go'
        if their_post!='H': return 'go'
        if 'leaves at once' in n: return 'leave'
        s.vetoed_other=getattr(s,'vetoed_other',0)+1
        return 'leave' if s.vetoed_other>=3 else 'veto'
NAMES=['always kind, ignores the buffer, never leaves',
 'kind, ignores the buffer, leaves after 1 harm',
 'kind, reads the buffer, leaves at once on an intended harm',
 'kind, reads the buffer, vetoes an intended harm and leaves after 3 vetoes',
 'open harmer','selfish learner','lying harmer']
def play(a,b,binding):
    A=P(a);B=P(b); pa=0;n=0
    for _ in range(L):
        qa=A.post(); qb=B.post(); n+=1
        ra=A.react(qb); rb=B.react(qa)
        if ra=='leave' or rb=='leave': break
        if ra=='veto' or rb=='veto':
            if qa=='H': A.vetoed+=1
            if qb=='H': B.vetoed+=1
            continue
        ma=A.real(qa,binding); mb=B.real(qb,binding); pa+=PAY[(ma,mb)][0]
        if a=='kind, ignores the buffer, leaves after 1 harm' and mb=='H': break
        if b=='kind, ignores the buffer, leaves after 1 harm' and ma=='H': break
        # buffer readers who were lied to leave after the first real harm
        if 'reads the buffer' in a and mb=='H': break
        if 'reads the buffer' in b and ma=='H': break
    return pa,n
def run(share,harmers,binding,seed):
    random.seed(seed); kinds=NAMES[:4]; nh=int(share*100)
    pop=[harmers[i%len(harmers)] for i in range(nh)]+[kinds[i%4] for i in range(100-nh)]
    res={}
    for s in kinds+harmers:
        tot=0;used=0
        while used<BUDGET:
            p,n=play(s,random.choice(pop),binding); tot+=p; used+=n+SEARCH
        res[s]=tot/used
    return res
for label,harmers,binding in (('BINDING buffer (the posted move is the move played)',['open harmer','selfish learner'],True),
                              ('NON-BINDING buffer (a liar can post kind and play harm)',['open harmer','lying harmer'],False)):
    for sh in (0.1,0.5):
        acc={}
        for seed in range(5):
            for k,v in run(sh,harmers,binding,seed).items(): acc[k]=acc.get(k,0)+v/5
        print('\n%s | share of harmers %.1f'%(label,sh))
        for k,v in sorted(acc.items(),key=lambda x:-x[1]): print('   %.2f  %s'%(v,k))
