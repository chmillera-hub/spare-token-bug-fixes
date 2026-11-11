import re,math,random,collections,sys
t=open('data/origin_of_species_2009.txt',encoding='utf-8',errors='replace').read()
s=t.find('*** START');e=t.find('*** END');t=t[s:e].lower()
t=re.sub(r'[^a-z]+',' ',t)
K=5;C=[collections.Counter() for _ in range(K+1)]
for n in range(1,K+1):
    for i in range(len(t)-n+1): C[n][t[i:i+n]]+=1
tot=len(t);vocab=collections.Counter(t.split());real={w for w,c in vocab.items() if c>=3 and (len(w)>1 or w in 'ai')}
AL='abcdefghijklmnopqrstuvwxyz '
def lp(ctx,c):
    b=0.0
    for n in range(min(K-1,len(ctx)),-1,-1):
        g=ctx[len(ctx)-n:]+c;num=C[n+1].get(g,0)
        den=C[n].get(g[:-1],0) if n>0 else tot
        if num>0: return b+math.log(num/den)
        b+=math.log(0.3)
    return b+math.log(1e-4)
def sense(x):
    y=' '+x.strip()+' ';return sum(lp(y[max(0,i-4):i],y[i]) for i in range(1,len(y)))/(len(y)-1)
def sense_nr(x):
    w=x.split();rep=1-len(set(w))/len(w) if w else 0
    return sense(x)-3.0*rep
def mutate(x,rng):
    r=rng.random();x=list(x)
    if r<0.30: x.insert(rng.randrange(len(x)+1),rng.choice(AL))
    elif r<0.40 and len(x)>1:
        i=rng.randrange(len(x)-1);x[i],x[i+1]=x[i+1],x[i]
    elif r<0.50: x[rng.randrange(len(x))]=rng.choice(AL)
    return re.sub(' +',' ',''.join(x))
def stats(pop):
    L=sum(len(p) for p in pop)/len(pop);ws=[w for p in pop for w in p.split()]
    rw=sum(w in real for w in ws)/max(1,len(ws));rep=sum(1-len(set(p.split()))/max(1,len(p.split())) for p in pop)/len(pop)
    return L,rw,rep

def force(x,rng): return re.sub(' +',' ',x[:(i:=rng.randrange(len(x)+1))]+rng.choice(AL[:26])+x[i:])
def run(name,fit,total,period,P=300,seed=3,marks=()):
    rng=random.Random(seed);pop=[rng.choice(AL.strip()) for _ in range(P)];f=[fit(p) for p in pop]
    for n in range(1,total+1):
        a=rng.sample(range(P),3);par=max(a,key=lambda i:f[i]);ch=mutate(pop[par],rng)
        b=rng.sample(range(P),3);w=min(b,key=lambda i:f[i]);pop[w]=ch;f[w]=fit(ch)
        if n%period==0:
            pop=[force(p,rng) for p in pop];f=[fit(p) for p in pop]
        if n in marks:
            L,rw,rep=stats(pop);i=max(range(P),key=lambda i:f[i])
            print(f"[{name}] pastes={n} (~{n/600:.0f} min) forced letters so far={n//period} mean length={L:.0f} real-word share={rw*100:.0f}% repeated-word share={rep*100:.0f}%\n     \"{pop[i][:170]}\"",flush=True)


def sense_more(x):
    w=x.split();d=len({v for v in w if v in real})
    return sense(x)+1.5*math.log(1+d)
run('forced every 5 min + reader wants more real words',sense_more,300000,3000,marks=(30000,150000,300000))
run('forced every 100 s + reader wants more real words',sense_more,300000,1000,marks=(30000,150000,300000))
