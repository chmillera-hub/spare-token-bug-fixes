import json,re,sys
J='/home/claude/dl/web/package/json/'
# (book file, display name, chapter, first verse, last verse) in Bible order
import sys
BOOKS={'genesis':'Genesis','psalms':'Psalm','proverbs':'Proverbs','ecclesiastes':'Ecclesiastes','isaiah':'Isaiah','jeremiah':'Jeremiah','matthew':'Matthew','mark':'Mark','luke':'Luke','john':'John','romans':'Romans','galatians':'Galatians','hebrews':'Hebrews'}
want=sys.argv[1].split(',');OUT=sys.argv[2]
SEL=[]
for bk in want:
    d=json.load(open(J+bk+'.json',encoding='utf-8'))
    chs=sorted({x['chapterNumber'] for x in d if 'chapterNumber' in x})
    for ch in chs: SEL.append((bk,BOOKS[bk],ch,1,999))
def norm(t):
    t=t.replace('’','').replace("'",'').lower()
    return re.sub(r'[^a-z]+',' ',t).strip()
phr=[];sec=[];names=[];seen=set();total=0;rawtotal=0
for bk,name,ch,v1,v2 in SEL:
    d=json.load(open(J+bk+'.json',encoding='utf-8'))
    txt=' '.join(x['value'] for x in d if 'value' in x and x.get('chapterNumber')==ch and v1<=x.get('verseNumber',0)<=v2)
    rawtotal+=len(txt.split())
    label=f"{name} {ch}";names.append(label);si=len(names)-1
    for clause in re.split(r'[,.;:!?—“”"()\[\]]+',txt):
        w=norm(clause).split()
        if not w: continue
        # cut long clauses into pieces of at most 38 letters at word boundaries
        # cut a long clause into pieces of roughly equal size so that no tiny leftover piece appears
        import math
        L=len(' '.join(w));k=max(1,math.ceil(L/38));target=L/k
        pieces=[];cur=[]
        for x in w:
            if cur and len(pieces)<k-1 and len(' '.join(cur+[x]))>target+3: pieces.append(cur);cur=[]
            cur.append(x)
        if cur: pieces.append(cur)
        for pc in pieces:
            s=' '.join(pc)
            if len(pc)<3 or len(s)<12 or len(s)>44 or s in seen: continue
            seen.add(s);phr.append(s);sec.append(si);total+=len(pc)
print('sections',len(names),'words in chosen passages',rawtotal,'phrases',len(phr),'words in phrases',total,'avg letters',sum(map(len,phr))/len(phr),file=sys.stderr)
json.dump({'p':phr,'i':sec,'s':names},open(OUT,'w'))
import random;random.seed(1)
for i in sorted(random.sample(range(len(phr)),14)): print(' ',names[sec[i]],'|',phr[i],file=sys.stderr)
