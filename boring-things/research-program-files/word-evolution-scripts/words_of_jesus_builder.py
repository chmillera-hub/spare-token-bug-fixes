import re,json,math,sys
x=open('/home/claude/dl/ob/eng-web.usfx.xml',encoding='utf-8').read()
NAMES={'MAT':'Matthew','MRK':'Mark','LUK':'Luke','JHN':'John'}
def norm(t):
    t=t.replace('’','').replace("'",'').lower();return re.sub(r'[^a-z]+',' ',t).strip()
phr=[];sec=[];names=[];seen=set();book=None;ch=None;words=0;bybook={}
for m in re.finditer(r'<book id="([A-Z0-9]+)"|<c id="(\d+)"|<wj>(.*?)</wj>',x,flags=re.S):
    if m.group(1): book=m.group(1);ch=None;continue
    if m.group(2): ch=int(m.group(2));continue
    if book not in NAMES: continue
    t=m.group(3);t=re.sub(r'<(x|f)\b.*?</\1>',' ',t,flags=re.S);t=re.sub(r'<[^>]+>',' ',t)
    label=f"{NAMES[book]} {ch}"
    if not names or names[-1]!=label: names.append(label)
    si=len(names)-1;words+=len(t.split());bybook[book]=bybook.get(book,0)+len(t.split())
    for clause in re.split(r'[,.;:!?—“”‘"()\[\]]+',t):
        w=norm(clause).split()
        if not w: continue
        L=len(' '.join(w));k=max(1,math.ceil(L/38));target=L/k;pieces=[];cur=[]
        for y in w:
            if cur and len(pieces)<k-1 and len(' '.join(cur+[y]))>target+3: pieces.append(cur);cur=[]
            cur.append(y)
        if cur: pieces.append(cur)
        for pc in pieces:
            s=' '.join(pc)
            if len(pc)<3 or len(s)<12 or len(s)>44 or s in seen: continue
            seen.add(s);phr.append(s);sec.append(si)
json.dump({'p':phr,'i':sec,'s':names},open('red.json','w'))
print('words of Jesus',words,bybook,'quotes',len(phr),'sections',len(names),file=sys.stderr)
import random;random.seed(2)
for i in sorted(random.sample(range(len(phr)),10)): print(' ',names[sec[i]],'|',phr[i],file=sys.stderr)
