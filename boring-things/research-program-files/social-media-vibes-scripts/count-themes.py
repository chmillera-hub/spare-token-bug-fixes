import re,sys,collections,glob,math,json
c=[]
for f in sorted(glob.glob(sys.argv[1]+'/part-*.txt')):
    p=re.split(r'===== Comment (\d+) =====\n',open(f,encoding='utf-8').read())
    c+=[p[i+1].strip() for i in range(1,len(p)-1,2)]
N=len(c)
th={'emotions':r"\bemotion",'suffering':r"\bsuffer",'ai':r"\b(ai|chatbot|chat bot|llm)\b",'god':r"\b(god|jesus|christ|lord|scripture|bible|psalm)\b",'society/power':r"\b(society|societal|power structures?|capitalism)\b",'gaslight/dehuman':r"gasligh|dehumaniz",'mean to you':r"mean to you",'lonel':r"\blonel",'profanity':r"\b(fuck|shit)",'pro-human':r"pro-?human",'lizard':r"lizard brain",'emo family':r"emotional family"}
D=10; res={k:[] for k in th}; low=[]; med=[]
for d in range(D):
    s=c[d*N//D:(d+1)*N//D]
    for k,r in th.items(): res[k].append(round(100*sum(bool(re.search(r,x.lower())) for x in s)/len(s)))
    low.append(round(100*sum(x[:1].islower() for x in s)/len(s)))
    L=sorted(len(x.split()) for x in s); med.append(L[len(L)//2])
for k in res: print(f'{k:18}',res[k])
print(f'{"lowercase start":18}',low); print(f'{"median words":18}',med)
json.dump({'res':res,'low':low,'med':med},open('themes.json','w'))
emo="anger fear boredom loneliness doubt guilt sadness annoyance shame overwhelm tiredness grief joy envy frustration".split()
stop=set("the a an and or of to in on at for from with by as is are was were be been being am it its this that these those i you he she we they me my your our their them so but if then than not no do does did have has had can could would should will just like also very more most some any all what which who how when where why because about into out up down over there here might may maybe one get got going go really when s t don't i'm it's that's emotion emotions emotional".split())
win={e:collections.Counter() for e in emo}; cc=collections.Counter(); tot=collections.Counter()
co=collections.Counter()
for x in c:
    t=re.findall(r"[a-z][a-z'\-]+",x.lower().replace('’',"'"))
    pres=set(e for e in emo if e in t); cc.update(pres)
    for a in pres:
        for b in pres:
            if a<b: co[(a,b)]+=1
    for i,w in enumerate(t):
        if w in win:
            for u in t[max(0,i-7):i+8]:
                if u not in stop and u not in emo and len(u)>2: win[w][u]+=1
for e in emo: tot.update(win[e])
T=sum(tot.values())
print()
for e in emo:
    n=sum(win[e].values())
    sc=[(math.log((v/n)/((tot[u]-v+1)/(T-n+1))),u,v) for u,v in win[e].items() if v>=max(8,cc[e]//25)]
    print(f'{e:12}{cc[e]:5} |',', '.join(f'{u}({v})' for _,u,v in sorted(sc,reverse=True)[:10]))
print(co.most_common(8))
