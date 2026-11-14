# Reads the World English Bible PDF and writes one verse per line (reference, tab, verse text).
# Usage: python3 make-verses-file.py world-english-bible.pdf bible-verses.txt  (needs the pymupdf package)
import pymupdf,re,sys,collections
d=pymupdf.open(sys.argv[1])
hdr=re.compile(r'^(.+?) (?:(\d+):)?(\d+)$')
verses=collections.OrderedDict()
book=None;ch=None;v=None
def add(txt):
    if book is None or v is None: return
    k=(book,ch,v); verses[k]=verses.get(k,'')+txt
for pn in range(len(d)):
    spans=[]
    for b in d[pn].get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            y=l['bbox'][1]
            first=True
            for s in l['spans']:
                spans.append((s,first)); first=False
    heads=[s for s,_ in spans if abs(s['size']-8)<0.3 and s['bbox'][1]<65]
    hb=None
    for s in heads:
        m=hdr.match(s['text'].strip())
        if m: hb=m; break
    if not hb: continue
    if hb.group(1)!=book:
        book=hb.group(1); ch=int(hb.group(2) or 1); v=None
        if int(hb.group(3))!=1 or ch!=1: print('book start odd',book,hb.group(0),file=sys.stderr)
    foot=False
    for s,first in spans:
        t=s['text']; sz=s['size']; f=s['font']
        if s['bbox'][1]<65 and abs(sz-8)<0.3: continue
        if foot: continue
        if sz>16 and 'Bold' in f and t.strip().isdigit():
            ch=int(t.strip()); v=None; continue
        if abs(sz-9)<0.4:
            if 'Bold' in f: foot=True; continue
            if f.startswith('NotoSerif-Regular') and t.strip().isdigit():
                v=int(t.strip()); continue
            if s['bbox'][1]>700 and not t.strip().isdigit() and f.startswith('Noto'): foot=True; continue
            continue  # footnote marks
        if abs(sz-12)<0.6:
            if first and (book,ch,v) in verses and not verses[(book,ch,v)].endswith((' ','-')): add(' ')
            add(t)
        # other sizes (titles) skipped
out=open(sys.argv[2],'w')
n=0
for (b,c,vv),t in verses.items():
    t=re.sub(r'[*§]','',t); t=re.sub(r'\s+',' ',t).strip()
    t=re.sub(r'\s+([,.;:?!”’])',r'\1',t); t=re.sub(r'([“‘])\s+',r'\1',t)
    if t: out.write(f'{b} {c}:{vv}\t{t}\n'); n+=1
print(n)
