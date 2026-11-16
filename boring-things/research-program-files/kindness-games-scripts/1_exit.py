import random
random.seed(7)
PAY={('K','K'):(3,3),('K','H'):(0,5),('H','K'):(5,0),('H','H'):(1,1)}
L=20; BUDGET=2000; SEARCH=1
# strategy = (move function, retreat rule: number of partner harms in a row before leaving; None = never)
def kind(my,their): return 'K'
def harm(my,their): return 'H'
def mirror(my,their): return 'K' if not their else their[-1]
S={'always kind, never leaves':(kind,None),'always harm':(harm,None),'mirror the partner, never leaves':(mirror,None),
   'kind, leaves after 1 harm':(kind,1),'kind, leaves after 2 harms':(kind,2),'kind, leaves after 3 harms':(kind,3)}
def play(a,b):
    fa,ra=S[a]; fb,rb=S[b]; ha=[];hb=[]; pa=0; n=0
    for _ in range(L):
        ma=fa(ha,hb); mb=fb(hb,ha); ha.append(ma); hb.append(mb); pa+=PAY[(ma,mb)][0]; n+=1
        def streak(h):
            c=0
            for x in reversed(h):
                if x=='H': c+=1
                else: break
            return c
        if (ra and streak(hb)>=ra) or (rb and streak(ha)>=rb): break
    return pa,n
def run(share_harm):
    others=[s for s in S if s!='always harm']
    pop=['always harm']*int(share_harm*100)+[random.choice(others) for _ in range(100-int(share_harm*100))]
    res={}
    for s in S:
        tot=0;used=0
        while used<BUDGET:
            p,n=play(s,random.choice(pop)); tot+=p; used+=n+SEARCH
        res[s]=tot/used
    return res
for sh in (0.1,0.3,0.5,0.7):
    r=run(sh); print('share of always-harm players:',sh)
    for k,v in sorted(r.items(),key=lambda x:-x[1]): print('   %.2f  %s'%(v,k))
