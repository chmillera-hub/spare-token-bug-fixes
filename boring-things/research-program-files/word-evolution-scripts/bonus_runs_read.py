# Reads the twenty run files and prints one line per run and the averages per setting.
import re,glob,statistics,collections
rows=collections.defaultdict(dict)
for f in sorted(glob.glob('out_*_*.txt')):
    _,cond,seed=f[:-4].split('_'); t=open(f).read()
    m=re.search(r'commands (\d+) \| scenes covered (\d+) \| average gap.*?story (\d+) places',t)
    w=re.search(r'words inside commands (\d+) \| different words (\d+)',t)
    e=re.search(r'evolved order \((\d+) scene changes\)',t); s=re.search(r'story order\s+\((\d+) scene changes\)',t)
    if not (m and w): continue
    rows[cond][int(seed)]=dict(cmds=int(m.group(1)),scenes=int(m.group(2)),gap=int(m.group(3)),words=int(w.group(1)),diff=int(w.group(2)),ev=int(e.group(1)),st=int(s.group(1)))
for cond in ('plain','story','fresh','both'):
    R=rows.get(cond,{})
    for seed,r in sorted(R.items()):
        print(f"{cond:5} start {seed}: commands {r['cmds']:2d}  scenes {r['scenes']}  scenes per command {r['scenes']/r['cmds']:.2f}  gap {r['gap']:4d}  words not repeats {r['diff']}/{r['words']} = {100*r['diff']/r['words']:.0f}%  scene changes {r['ev']} -> {r['st']}")
    if R:
        v=list(R.values()); mean=lambda k: statistics.mean(x[k] for x in v)
        print(f"  {cond} average over {len(v)} runs: commands {mean('cmds'):.1f}  scenes {mean('scenes'):.1f}  gap {mean('gap'):.0f}  share of words that are not repeats {100*sum(x['diff'] for x in v)/sum(x['words'] for x in v):.0f}%  scenes per command {statistics.mean(x['scenes']/x['cmds'] for x in v):.2f}\n")
print("paired differences against plain (same starting point)")
for cond in ('story','fresh','both'):
    seeds=sorted(set(rows['plain'])&set(rows.get(cond,{})))
    if not seeds: continue
    for k,name in (('cmds','commands'),('scenes','scenes'),('gap','gap')):
        d=[rows[cond][s][k]-rows['plain'][s][k] for s in seeds]; print(f"  {cond} minus plain {name}: {d}  mean {statistics.mean(d):+.1f}")
    d=[100*rows[cond][s]['diff']/rows[cond][s]['words']-100*rows['plain'][s]['diff']/rows['plain'][s]['words'] for s in seeds]
    print(f"  {cond} minus plain share not repeats: {[round(x) for x in d]}  mean {statistics.mean(d):+.1f}")
