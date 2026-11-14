import re,glob,sys
sys.argv=['x','none']
src=open('write.py').read(); exec(src[:src.index("if sys.argv[1]=='gen'")])
print('=== A new openings')
A=["i feel","when someone dismisses me i","the meaning of life is","a job is","money is","love is","my emotions are","the chatbot said","jesus said","people who are lonely","the universe is","if you are suffering then","a boundary is","the lizard brain","peace is","work is"]
for p in A: print('>>',gen(p,n=60,seed=5)); print()
print('=== B temperature')
for t in (0.3,0.8,1.3): print(t,'>>',gen("loneliness is",n=55,temp=t,seed=9)); print()
print('=== C pull test')
P=["the weather today is","my favorite food is","the car was","yesterday i went to","the movie was about","video games are","the president","a dog is","the internet is","school is","my phone","the best way to cook","music is","sports are","the ocean is"]
Q=["anger is","society is","god is","ai is","my job","money is","people are","my fear","a therapist","conversation is","power is","the brain","loneliness is","boredom is","truth is"]
import collections
def run(L):
    outs=[]
    for p in L:
        for s in range(5): outs.append((p,gen(p,n=70,seed=100+s)))
    return outs
on=run(P); oq=run(Q)
keys={'suffering':r'suffer','well-being':r'well-being','emotion':r'emotion','mean to you':r'mean to you|means to you','meaning/meaningful':r'meaning','humanity/human':r'human'}
for name,o in (('neutral openings',on),('theme openings',oq)):
    print(name,len(o),{k:sum(bool(re.search(r,x)) for _,x in o) for k,r in keys.items()})
for p,x in on[::5][:8]: print('>>',x); print()
print('=== D copy check')
c=[]
for f in sorted(glob.glob('../../../../1-research-click-here-first/social-media-vibes/owner-comments-full/part-*.txt')):
    pp=re.split(r'===== Comment (\d+) =====\n',open(f,encoding='utf-8').read())
    c+=[pp[i+1].lower().replace('’',"'") for i in range(1,len(pp)-1,2)]
W=lambda s: re.findall(r"[a-z0-9'\-]+",s)
grams={n:set() for n in range(4,16)}
for x in c:
    w=W(x)
    for n in grams:
        for i in range(len(w)-n+1): grams[n].add(' '.join(w[i:i+n]))
def longest(x):
    w=W(x); best=3; ex=''
    for n in range(4,16):
        hit=[' '.join(w[i:i+n]) for i in range(len(w)-n+1) if ' '.join(w[i:i+n]) in grams[n]]
        if hit: best=n; ex=hit[0]
        else: break
    return best,ex
L=sorted(longest(x) for _,x in on+oq)
print('median',L[len(L)//2][0],'max',L[-1],'share>=8',sum(a>=8 for a,_ in L)/len(L),'share>=12',sum(a>=12 for a,_ in L)/len(L))
print('=== E closest words')
E_=F.normalize(m.e.weight.detach(),dim=1)
for w in "love peace meaning truth power work job brain loneliness lonely chatbot humanity emotions meaningless silence family consciousness reddit capitalism death hope".split():
    t=tok.encode(' '+w).ids
    if len(t)!=1: print(w,'(split into pieces)'); continue
    s=E_@E_[t[0]]; print(w,'|',', '.join(tok.decode([j]).strip() for j in s.topk(9).indices[1:].tolist()))
