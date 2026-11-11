import json,re,sys
J='/home/claude/dl/web/package/json/'
# (book file, display name, chapter, first verse, last verse) in Bible order
SEL=[('genesis','Genesis',1,1,31),('genesis','Genesis',2,1,3),('exodus','Exodus',20,1,17),('deuteronomy','Deuteronomy',6,4,9),('ruth','Ruth',1,16,17),
 ('psalms','Psalm',1,1,6),('psalms','Psalm',8,1,9),('psalms','Psalm',19,1,14),('psalms','Psalm',23,1,6),('psalms','Psalm',27,1,14),('psalms','Psalm',34,1,22),('psalms','Psalm',46,1,11),('psalms','Psalm',91,1,16),('psalms','Psalm',100,1,5),('psalms','Psalm',103,1,22),('psalms','Psalm',121,1,8),('psalms','Psalm',139,1,24),
 ('proverbs','Proverbs',3,1,12),('ecclesiastes','Ecclesiastes',3,1,8),('isaiah','Isaiah',40,28,31),('isaiah','Isaiah',55,6,12),('micah','Micah',6,8,8),
 ('matthew','Matthew',5,1,48),('matthew','Matthew',6,1,34),('matthew','Matthew',7,1,29),('matthew','Matthew',22,34,40),('matthew','Matthew',25,31,40),
 ('luke','Luke',10,25,37),('luke','Luke',15,11,32),('john','John',1,1,14),('john','John',13,34,35),('john','John',15,9,17),
 ('romans','Romans',8,31,39),('romans','Romans',12,9,21),('1corinthians','First Corinthians',13,1,13),('galatians','Galatians',5,22,23),('philippians','Philippians',4,4,9),('colossians','Colossians',3,12,17),('james','James',1,19,27),('1john','First John',4,7,21),('revelation','Revelation',21,1,5)]
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
json.dump({'p':phr,'i':sec,'s':names},open('bible_phrases.json','w'))
import random;random.seed(1)
for i in sorted(random.sample(range(len(phr)),14)): print(' ',names[sec[i]],'|',phr[i],file=sys.stderr)
