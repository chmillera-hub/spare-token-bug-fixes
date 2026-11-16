import random
PAY={('K','K'):(3,3),('K','H'):(-10,5),('H','K'):(5,-10),('H','H'):(1,1)}
L=20; BUDGET=20000; SEARCH=1; TRIAL=0.1
# name: (trial move, real move fn, wants trial?, leaves after n harms in real game or None)
kind=lambda their:'K'; harm=lambda their:'H'; mirror=lambda their:'K' if not their else their[-1]
S={
 'always kind, no sample game, never leaves':('K',kind,False,None),
 'mirror the partner, no sample game, never leaves':('K',mirror,False,None),
 'kind, no sample game, leaves after 1 harm':('K',kind,False,1),
 'kind, sample game first, never leaves the real game':('K',kind,True,None),
 'kind, sample game first, leaves after 1 harm':('K',kind,True,1),
 'open harmer (harms in the sample game too)':('H',harm,False,None),
 'disguised harmer (kind in the sample game, harms in the real game)':('K',harm,False,None),
}
def play(a,b):
    ta,fa,wa,ra=S[a]; tb,fb,wb,rb=S[b]; pa=0.0; n=0
    if wa or wb:                      # one sample turn at 10 percent stakes if either side asks for one
        pa+=PAY[(ta,tb)][0]*TRIAL; n+=1
        if (wa and tb=='H') or (wb and ta=='H'): return pa,n
    ha=[];hb=[]
    for _ in range(L):
        ma=fa(hb); mb=fb(ha); ha.append(ma); hb.append(mb); pa+=PAY[(ma,mb)][0]; n+=1
        if (ra and hb[-ra:]==['H']*ra) or (rb and ha[-rb:]==['H']*rb): break
    return pa,n
KINDS=[s for s in S if 'harmer' not in s]
def run(share,open_frac,seed):
    random.seed(seed)
    nh=int(share*100); no=int(nh*open_frac)
    pop=['open harmer (harms in the sample game too)']*no+['disguised harmer (kind in the sample game, harms in the real game)']*(nh-no)+[KINDS[i%len(KINDS)] for i in range(100-nh)]
    res={}
    for s in S:
        tot=0;used=0
        while used<BUDGET:
            p,n=play(s,random.choice(pop)); tot+=p; used+=n+SEARCH
        res[s]=tot/used
    return res
for label,of in (('all harmers are open',1.0),('half open and half disguised',0.5),('all harmers are disguised',0.0)):
    for sh in (0.1,0.5):
        acc={s:0 for s in S}
        for seed in range(5):
            r=run(sh,of,seed)
            for s in S: acc[s]+=r[s]/5
        print('\n%s | share of harmers %.1f'%(label,sh))
        for k,v in sorted(acc.items(),key=lambda x:-x[1]):
            if (of==1.0 and 'disguised' in k) or (of==0.0 and 'open' in k): continue
            print('   %.2f  %s'%(v,k))
