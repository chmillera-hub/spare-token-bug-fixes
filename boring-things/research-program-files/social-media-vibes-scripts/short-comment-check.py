import re,csv,glob,os,collections,sys,importlib.util,random
spec=importlib.util.spec_from_file_location('g','generic_phrase_filter.py'); g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
rows=[]
for f in sorted(glob.glob("data/rd/*.csv")):
    name=os.path.basename(f)[:-4]; meta=name.split("_")[0]; seen=set()
    for row in csv.reader(open(f,newline='',encoding='utf-8',errors='ignore')):
        if meta not in row: continue
        j=row.index(meta)
        if j<3 or row[j-2] in seen: continue
        seen.add(row[j-2]); t=g.norm(row[j-3])
        if not t or t in("deleted","removed"): continue
        rows.append(t)
n=len(rows); L=[len(t.split()) for t in rows]
for k in (1,2,3,5,8,10,15,20): print('<=',k,sum(l<=k for l in L),round(100*sum(l<=k for l in L)/n,1))
words=sum(L); sw=sum(l for l in L if l<=5); print('share of all words inside short rows',round(100*sw/words,2))
short=[t for t in rows if len(t.split())<=5]
c=collections.Counter(short); print('distinct short',len(c),'top',c.most_common(25))
print('short rows that repeat (appear 2+ times)',sum(v for v in c.values() if v>1))
random.seed(5); print(random.sample(short,70))
qs=sum(t.split()[0] in ('what','why','how','who','where','when','is','are','do','does','did','can','could','would','should','any','anyone') for t in short); print('short rows starting with a question word',qs,round(100*qs/len(short),1))
