# Copies the verses file and leaves out genealogies and long lists of names.
# Usage: python3 make-outputs-file.py bible-verses.txt bible-verses-for-outputs.txt
import re,sys,collections
src,dst=sys.argv[1],sys.argv[2]
V=[l.rstrip('\n').split('\t') for l in open(src)]
def parse(ref):
    m=re.match(r'(.+) (\d+):(\d+)$',ref); return m.group(1),int(m.group(2)),int(m.group(3))
# known genealogy and name-list sections: (book, chapter, first verse, last verse)
R=[('Genesis',5,1,32),('Genesis',10,1,32),('Genesis',11,10,32),('Genesis',22,20,24),('Genesis',25,1,4),('Genesis',25,12,18),('Genesis',35,22,26),('Genesis',36,1,43),('Genesis',46,8,27),
('Exodus',1,1,5),('Exodus',6,14,25),('Numbers',1,5,46),('Numbers',2,1,34),('Numbers',3,14,39),('Numbers',7,12,88),('Numbers',10,14,28),('Numbers',13,4,16),('Numbers',26,5,62),('Numbers',33,5,49),('Numbers',34,16,29),
('Joshua',12,7,24),('Joshua',15,1,63),('Joshua',16,1,10),('Joshua',17,1,11),('Joshua',18,11,28),('Joshua',19,1,51),('Joshua',21,1,42),
('Ruth',4,18,22),('2 Samuel',23,24,39),('1 Kings',4,1,19),
('1 Chronicles',1,1,54),('1 Chronicles',2,1,55),('1 Chronicles',3,1,24),('1 Chronicles',4,1,43),('1 Chronicles',5,1,26),('1 Chronicles',6,1,81),('1 Chronicles',7,1,40),('1 Chronicles',8,1,40),('1 Chronicles',9,1,44),('1 Chronicles',11,26,47),('1 Chronicles',12,1,37),('1 Chronicles',15,4,24),('1 Chronicles',23,6,24),('1 Chronicles',24,1,31),('1 Chronicles',25,1,31),('1 Chronicles',26,1,32),('1 Chronicles',27,1,34),
('Ezra',2,1,70),('Ezra',8,1,20),('Ezra',10,18,44),('Nehemiah',3,1,32),('Nehemiah',7,6,73),('Nehemiah',10,1,27),('Nehemiah',11,3,36),('Nehemiah',12,1,26),
('Matthew',1,1,17),('Luke',3,23,38)]
def known(b,c,v): return any(b==B and c==C and a<=v<=z for B,C,a,z in R)
SKIP=set('God Yahweh Lord LORD Jesus Christ I Israel Father Spirit Holy Son Man Good News Kingdom Behold Amen Jerusalem Judah Egypt Zion'.split())
def score(t):
    w=re.findall(r"[A-Za-z’']+",t)
    if len(w)<6: return 0,0
    names=[x for i,x in enumerate(w) if x[0].isupper() and x not in SKIP and i>0 and not re.search(r'[.?!”“:]\s*[“‘]?$', t[:t.find(x)] ) ]
    return len(names),len(names)/len(w)
flag=[]
for ref,t in V:
    b,c,v=parse(ref); n,r=score(t)
    pat=len(re.findall(r'became the father of|the sons? of [A-Z]|son of [A-Z]|daughter of [A-Z]|were born|, and [A-Z][a-z]+, and [A-Z]',t))
    h=(n>=5 and r>=0.30) or (pat>=3 and r>=0.22) or ('became the father of' in t and r>=0.15)
    flag.append([known(b,c,v),h])
# heuristic verses only count when at least 3 flagged verses sit within a window of 4 in the same chapter
N=len(V); keep=[]; dropped=collections.Counter(); extra=[]
for i,(ref,t) in enumerate(V):
    k,h=flag[i]
    run=False
    if h and not k:
        b,c,_=parse(ref)
        near=[j for j in range(max(0,i-3),min(N,i+4)) if parse(V[j][0])[:2]==(b,c) and flag[j][1] and not flag[j][0]]
        run=len(near)>=3
    if k or run:
        dropped[parse(ref)[0]]+=1
        if run and not k: extra.append(ref+'  '+t[:110])
    else: keep.append(ref+'\t'+t)
open(dst,'w').write('\n'.join(keep)+'\n')
print('kept',len(keep),'dropped',N-len(keep),'heuristic-only',len(extra))
print(dict(dropped))

