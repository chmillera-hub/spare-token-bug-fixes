"""Generic phrase filter. Reads the phrase list and a folder of comment tables and counts matches.
Usage: put generic-phrases-10000.txt beside this file and put the public comment tables in data/rd then run python3 generic_phrase_filter.py"""
import re,csv,sys,glob,collections,os,json
csv.field_size_limit(10**9)
def norm(s):
    s=s.lower().replace("’","'")
    s=re.sub(r"[^a-z0-9' ]+"," ",s); s=s.replace("'","")
    return re.sub(r"\s+"," ",s).strip()
def load_list(p="generic-phrases-10000.txt"):
    P=set(); body=False
    for l in open(p):
        l=l.rstrip("\n")
        if l.startswith("==="): body=True; continue
        if not body or not l.strip() or re.search(r" - \d+ phrases$",l): continue
        n=norm(l)
        if n and not n.replace(" ","").isdigit(): P.add(n)
    return P
csv.field_size_limit(10**9)
P=load_list(); P2=[p for p in P if len(p.split())>=2]
P2set=set(P2); maxlen=max(len(p.split()) for p in P2)
def tier(t):
    w=t.split()
    if t in P: return 1
    if len(w)<=8:
        for i in range(len(w)):
            for L in range(2,min(maxlen,len(w)-i)+1):
                if " ".join(w[i:i+L]) in P2set: return 2
    return 0
if __name__=="__main__":
    tot=collections.Counter(); per={}
    for f in sorted(glob.glob("data/rd/*.csv")):
        name=os.path.basename(f)[:-4]; meta=name.split("_")[0]; seen=set(); c=collections.Counter()
        for row in csv.reader(open(f,newline='',encoding='utf-8',errors='ignore')):
            if meta not in row: continue
            j=row.index(meta)
            if j<3 or row[j-2] in seen: continue
            seen.add(row[j-2]); t=norm(row[j-3])
            if not t or t in("deleted","removed"): continue
            c["n"]+=1; k=tier(t)
            if k==1: c["exact"]+=1
            if k==2: c["contains"]+=1
            if len(t.split())<=5: c["short"]+=1
        per[name]=dict(c); tot.update(c)
    json.dump({"tot":tot,"per":per},open("rd2.json","w"))
    n=tot["n"]; print(tot,{k:round(v/n*100,2) for k,v in tot.items()})
