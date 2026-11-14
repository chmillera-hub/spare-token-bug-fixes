import re,sys,collections,json,glob
c=[]
for f in sorted(glob.glob(sys.argv[1]+'/part-*.txt')):
    p=re.split(r'===== Comment (\d+) =====\n',open(f,encoding='utf-8').read())
    c+=[p[i+1] for i in range(1,len(p)-1,2)]
ids=collections.defaultdict(set); show={}; order={}
for ci,x in enumerate(c):
    for si,s in enumerate(re.split(r"(?<=[.!?])\s+|\n+",x)):
        k=re.sub(r"[^a-z0-9' ]+"," ",s.lower().replace('’',"'")); k=' '.join(k.split())
        if len(k.split())<4: continue
        ids[k].add(ci); show.setdefault(k,collections.Counter())[s.strip()]+=1; order.setdefault(k,si)
ks=sorted([k for k in ids if len(ids[k])>=6],key=lambda k:(-len(ids[k]),order[k]))
blocks=[]
for k in ks:
    for b in blocks:
        a=ids[b['k'][0]]; i=len(a&ids[k])
        if i/len(a|ids[k])>=0.8: b['k'].append(k); break
    else: blocks.append({'k':[k]})
out=[]
for b in blocks[:int(sys.argv[3])]:
    k=b['k'][0]; out.append((show[k].most_common(1)[0][0],len(ids[k]),len(b['k'])))
    print(len(ids[k]),len(b['k']),'|',out[-1][0][:170])
json.dump({'N':len(c),'top':out},open(sys.argv[2],'w'))
