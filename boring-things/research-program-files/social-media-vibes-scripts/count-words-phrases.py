import re,sys,collections,json,glob
src=sys.argv[1]; out=sys.argv[2]
c=[]
for f in sorted(glob.glob(src+'/part-*.txt')):
    p=re.split(r'===== Comment (\d+) =====\n',open(f,encoding='utf-8').read())
    c+=[p[i+1].lower().replace('’',"'") for i in range(1,len(p)-1,2)]
N=len(c)
wstop=set("""a about above after again against all am an and any are aren't as at be because been before being below between both but by can can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves just like also even get got going go one will might may maybe much many really thing things something someone anything make made way want know think see say said says saying using use used well yeah okay oh im dont thats name removed don lot still back every now else kind sort actually instead without within toward towards another around mean means meant people person need needs feel feeling help time""".split())
pstop=set("a an and the of to in on at for from with by as is are was were be been being am it its it's this that these those i you he she we they me my your our their them his her so or but if then than not no do does did have has had can could would should will just like also very more most some any all what which who how when where why because about into out up down over there here i'm you're don't that's can't might may maybe s t u name removed one get got going go really lot kind own".split())
w=collections.Counter(); wd=collections.Counter(); ph=collections.Counter(); pd=collections.Counter()
for x in c:
    ws=[k.strip("'") for k in re.findall(r"[a-z][a-z'\-]+",x)]
    ws=[k for k in ws if k not in wstop and len(k)>2]
    w.update(ws); wd.update(set(ws))
    seen=set()
    for seg in re.split(r"[.!?\n,;:()\"“”…\[\]]+",x):
        t=re.findall(r"[a-z][a-z'\-]*",seg)
        for n in (2,3,4,5):
            for i in range(len(t)-n+1):
                g=t[i:i+n]
                if g[0] in pstop or g[-1] in pstop: continue
                if n==2 and (len(g[0])<3 or len(g[1])<3): continue
                s=' '.join(g); ph[s]+=1; seen.add(s)
    pd.update(seen)
words=[(k,v,wd[k]) for k,v in w.most_common(25)]
cand=ph.most_common(600)
drop={"other people","right now","each other","make sure","too much","better understand","someone else","every time","someone says","other person","another human"}
phr=[]
for k,v in cand:
    if k in drop: continue
    if any(k!=k2 and (' '+k+' ') in (' '+k2+' ') and v2>=0.6*v for k2,v2 in cand): continue
    phr.append((k,v,pd[k]))
print(N); print(words); print(phr[:32])
json.dump({'N':N,'words':words,'phr':phr[:32]},open(out,'w'))
