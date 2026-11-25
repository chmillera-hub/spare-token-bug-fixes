import time, json, os
os.environ["MAZE_RULE"]="zero-north"
import max_score_points as m, importlib.util, sys
src=open('max_score_points_pairs.py').read().split("t0=time.time(); res={}")[0]; exec(src)
out={}
# every pair of sequences that maxes 3 by 3 and 4 by 4, then try to extend to 5 by 5
t0=time.time(); pairs34=[]; dl=time.time()+60
for sa in extend([],3,dl):
    for sb in extend(sa,4,dl): pairs34.append(sb)
print("sequences that max 3 and 4:",len(pairs34),"finished",time.time()<dl,round(time.time()-t0,1),flush=True)
found5=None; dl=time.time()+150; tried=0
for sb in pairs34:
    tried+=1
    for sc in extend(sb,5,dl): found5=sc; break
    if found5 or time.time()>dl: break
print("extend to 5:",found5,"tried",tried,"of",len(pairs34),"finished",time.time()<dl,flush=True)
out["max_3_and_4"]={"count":len(pairs34),"examples":["".join(map(str,x)) for x in pairs34[:5]]}
out["max_3_4_5"]={"found":"".join(map(str,found5)) if found5 else None,"tried":tried,"finished":time.time()<dl}
# 2 and 4 from the 46 sequences that max 2 by 2
c24=[]; dl=time.time()+90
import itertools
for sa in extend([],2,dl):
    for sb in extend(sa,4,dl): c24.append(sb); break
print("2 and 4:",len(c24),time.time()<dl,flush=True)
out["max_2_and_4"]={"count_of_2_by_2_starts_that_extend":len(c24),"examples":["".join(map(str,x)) for x in c24[:5]],"finished":time.time()<dl}
# well known sequences: points on sizes 2 to 12
import numpy as np, mpmath; mpmath.mp.dps=170
s=np.ones(4000,dtype=bool); s[:2]=False
for i in range(2,64):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0][:160].tolist(); pdig=[int(c) for c in "".join(map(str,P))]
dg=lambda x:[int(c) for c in mpmath.nstr(x,160,strip_zeros=False).replace(".","")][:144]
fib=[1,1]
while len(fib)<144: fib.append(fib[-1]+fib[-2])
NAT={"digits of the primes written in one row":pdig,"digits of pi":dg(mpmath.pi),"digits of e":dg(mpmath.e),"digits of the square root of 2":dg(mpmath.sqrt(2)),
 "digits of the counting numbers written in one row":[int(c) for c in "".join(str(i) for i in range(1,120))],"counting numbers with one whole number in each room":list(range(1,145)),
 "one whole prime in each room":P,"Fibonacci numbers with one whole number in each room":fib,"square numbers with one whole number in each room":[i*i for i in range(1,145)]}
out["natural"]={n:[k for k in m.SIZES if m.maxed([x%4 for x in q[:k*k]],k)] for n,q in NAT.items()}
print(out["natural"])
json.dump(out,open("max_score_points_triples_results.json","w"),indent=1)
