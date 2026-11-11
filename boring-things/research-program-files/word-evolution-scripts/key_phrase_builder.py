import json,re,sys,math
J='/home/claude/dl/web/package/json/'
BOOKS={'psalms':'Psalm','proverbs':'Proverbs','ecclesiastes':'Ecclesiastes','isaiah':'Isaiah','jeremiah':'Jeremiah','matthew':'Matthew','mark':'Mark','luke':'Luke','john':'John','romans':'Romans'}
# a new key phrase may start before one of these linking words
CUT=set('and but or nor for that who whom which because so when where while if unless until as than in on with from by into through before after like at among against without then yet'.split())
def norm(t):
    t=t.replace('’','').replace("'",'').lower();return re.sub(r'[^a-z]+',' ',t).strip()
def chunks(text):
    out=[]
    for clause in re.split(r'[,.;:!?—“”‘"()\[\]]+',text):
        w=norm(clause).split()
        if not w: continue
        parts=[];cur=[]
        for x in w:
            if x in CUT and len(cur)>=2: parts.append(cur);cur=[]
            cur.append(x)
        if cur: parts.append(cur)
        # a piece of one word joins the piece before it or after it because one word alone rarely makes sense
        merged=[]
        for p in parts:
            if merged and (len(p)<2 or len(merged[-1])<2): merged[-1]=merged[-1]+p
            else: merged.append(p)
        for p in merged:
            # very long pieces are cut in the middle
            while len(p)>7: out.append(' '.join(p[:4]));p=p[4:]
            if len(p)>=2 or not out: out.append(' '.join(p))
            else: out[-1]=out[-1]+' '+' '.join(p)
    return out
def pack(sections,outfile):
    uid={};u=[];seq=[];sec=[];names=[]
    for label,text in sections:
        names.append(label);si=len(names)-1
        for c in chunks(text):
            if c not in uid: uid[c]=len(u);u.append(c)
            seq.append(uid[c]);sec.append(si)
    json.dump({'u':u,'seq':seq,'sec':sec,'s':names},open(outfile,'w'))
    print(outfile,'sections',len(names),'phrases in order',len(seq),'different phrases',len(u),'avg words',round(sum(len(x.split()) for x in u)/len(u),2),file=sys.stderr)
    return u
def from_json(sel):
    out=[]
    for bk,name,ch,v1,v2 in sel:
        d=json.load(open(J+bk+'.json',encoding='utf-8'))
        out.append((f"{name} {ch}",' '.join(x['value'] for x in d if 'value' in x and x.get('chapterNumber')==ch and v1<=x.get('verseNumber',0)<=v2)))
    return out
# 1 Claude selection: the same 41 passages as before
src=open('bible_build.py').read();a=src.index('SEL=[');b=src.index(']',src.index("('revelation'"))+1
exec(src[a:b])
u=pack(from_json(SEL),'ph_mine.json')
# 2 Charles selection: ten whole books
sel=[]
for bk in BOOKS:
    d=json.load(open(J+bk+'.json',encoding='utf-8'))
    for ch in sorted({x['chapterNumber'] for x in d if 'chapterNumber' in x}): sel.append((bk,BOOKS[bk],ch,1,999))
pack(from_json(sel),'ph_charles.json')
# 3 words of Jesus in the four gospels
x=open('/home/claude/dl/ob/eng-web.usfx.xml',encoding='utf-8').read();NAMES={'MAT':'Matthew','MRK':'Mark','LUK':'Luke','JHN':'John'}
secs=[];book=None;ch=None
for m in re.finditer(r'<book id="([A-Z0-9]+)"|<c id="(\d+)"|<wj>(.*?)</wj>',x,flags=re.S):
    if m.group(1): book=m.group(1);ch=None;continue
    if m.group(2): ch=int(m.group(2));continue
    if book not in NAMES: continue
    t=re.sub(r'<(x|f)\b.*?</\1>',' ',m.group(3),flags=re.S);t=re.sub(r'<[^>]+>',' ',t);label=f"{NAMES[book]} {ch}"
    if secs and secs[-1][0]==label: secs[-1]=(label,secs[-1][1]+' . '+t)
    else: secs.append((label,t))
pack(secs,'ph_red.json')
import random;random.seed(4)
d=json.load(open('ph_mine.json'));i=d['sec'].index(d['s'].index('Psalm 23'));print(' / '.join(d['u'][k] for k in d['seq'][i:i+22]),file=sys.stderr)
