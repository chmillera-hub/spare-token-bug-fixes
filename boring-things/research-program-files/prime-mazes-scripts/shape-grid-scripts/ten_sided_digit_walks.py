# Two walks on ten sided rooms worked out from the door directions alone.
# Part 1: whole primes (the door is the last digit). Part 2: the digits of the golden ratio against random digits.
from math import isqrt,sqrt
import random
v={0:(0,-1),1:(1,-1),2:(1,-1),3:(1,0),4:(1,1),5:(0,1),6:(-1,1),7:(-1,1),8:(-1,0),9:(-1,-1)}  # x to the right and y downward in room widths
def primes(n):
    b=bytearray([1])*(n+1);b[0]=b[1]=0
    for k in range(2,int(n**.5)+1):
        if b[k]: b[k*k::k]=bytearray(len(b[k*k::k]))
    return [k for k in range(n+1) if b[k]]
P=primes(40000)[:3600]
x=y=0;xs=[];c={};opp=0;prev=None
for p in P:
    d=p%10;c[d]=c.get(d,0)+1;x+=v[d][0];y+=v[d][1];xs.append(x)
    if prev is not None and {prev,d}=={1,7}: opp+=1
    prev=d
print('whole primes: last digit counts',c,'final x',x,'rooms up',-y,'x range',min(xs),max(xs),'neighbors ending in 1 and 7:',opp)
N=3481
sc=10**(N+6); r=(isqrt(5*sc*sc)+sc)//2; d=[int(ch) for ch in str(r)[:N]]
def walk(d):
    x=y=0;pts=[(0,0)]
    for k in d: x+=v[k][0];y+=v[k][1];pts.append((x,y))
    return pts
pts=walk(d);x,y=pts[-1]
print('golden ratio digit counts',[d.count(k) for k in range(10)],'end: right',x,'up',-y,'distance %.1f'%sqrt(x*x+y*y),'different large rooms',len(set(pts)))
u=[(a-b)/sqrt(2) for a,b in pts]; w=[(a+b)/sqrt(2) for a,b in pts]
print('extent along the lower left to upper right diagonal %.1f and across %.1f'%(max(u)-min(u),max(w)-min(w)))
random.seed(1); far=0;eu=0;ew=0
for t in range(2000):
    p=walk([random.randrange(10) for _ in range(N)]);a,b=p[-1]
    if sqrt(a*a+b*b)>sqrt(x*x+y*y): far+=1
    uu=[(a-b)/sqrt(2) for a,b in p]; ww=[(a+b)/sqrt(2) for a,b in p]; eu+=max(uu)-min(uu); ew+=max(ww)-min(ww)
print('share of 2000 random walks that end farther away: %.1f%%'%(100*far/2000),'average random extent along %.1f and across %.1f'%(eu/2000,ew/2000))
