# Counts how many pages with running text end exactly where a paragraph ends (written 12 November 2026 by an AI chatbot).
# In the typed copy the mark <$> closes a paragraph and a text line of running paragraph text has the letter P in the line tag.
import re,collections
last={};nl=collections.Counter()
for ln in open('data/ZL3b-n.txt',encoding='latin-1'):
    m=re.match(r'<(f\d+[rv]\d*)\.\d+[a-z]?,([^>]*)>\s*(.*)',ln.rstrip())
    if m and re.search(r'P[0-9a-z]',m.group(2)):       # any kind of paragraph text line (running or centred or right-justified or title)
        last[m.group(1)]=m.group(3); nl[m.group(1)]+=1
pages=[p for p in last if nl[p]>=2]
ends=[p for p in pages if '<$>' in last[p]]
print("pages with at least two lines of paragraph text:",len(pages))
print("pages whose last paragraph-text line closes a paragraph:",len(ends))
print("pages that end in the middle of a paragraph:",sorted(set(pages)-set(ends)))
for p in sorted(set(pages)-set(ends)): print("   ",p,last[p][-60:])
# Second check that does not trust the <$> marks: a line that ends a paragraph usually stops short of the right margin.
# The check compares the length in letters of three kinds of line with the middle length of the lines on the same page.
import statistics
pg=collections.defaultdict(list)
for ln in open('data/ZL3b-n.txt',encoding='latin-1'):
    m=re.match(r'<(f\d+[rv])\.\d+[a-z]?,([^>]*)>\s*(.*)',ln.rstrip())
    if m and re.search(r'P[0-9a-z]',m.group(2)):
        t=m.group(3); end='<$>' in t
        t=re.sub(r'<[^>]*>','',t); t=re.sub(r'\[([^:\]]*)(:[^\]]*)?\]',r'\1',t); t=re.sub(r'[^a-z?]','',t)
        pg[m.group(1)].append((len(t),end,bool(re.search(r'P0',m.group(2)))))
last=[];midend=[];midrun=[]
for p,L in pg.items():
    if len(L)<6: continue
    med=statistics.median(l for l,_,_ in L)
    for i,(l,e,run) in enumerate(L):
        r=l/med
        if i==len(L)-1: last.append(r)
        elif e: midend.append(r)
        else: midrun.append(r)
def show(name,v): print(f"   {name}: {len(v)} lines  middle value {statistics.median(v):.2f} of the usual line length  share shorter than 0.8 of the usual length {sum(x<0.8 for x in v)/len(v):.2f}")
print("line length check on ordinary pages with at least six lines of paragraph text")
show("last line of a page",last); show("line that ends a paragraph in the middle of a page",midend); show("line inside a paragraph",midrun)
