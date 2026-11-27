# Counts how the first 3600 primes split between remainder 1 and remainder 5 when divided by 6.
# On growing hexagons a prime with remainder 1 picks the upper right door and remainder 5 picks the upper left door.
def primes(n):
    b=bytearray([1])*(n+1);b[0]=b[1]=0
    for k in range(2,int(n**.5)+1):
        if b[k]: b[k*k::k]=bytearray(len(b[k*k::k]))
    return [k for k in range(n+1) if b[k]]
P=primes(40000)[:3600]
x=0;mn=mx=0;rep=0;c1=c5=0;prev=None
for p in P[2:]:
    r=p%6
    if r==1: x+=1;c1+=1
    else: x-=1;c5+=1
    mn=min(mn,x);mx=max(mx,x)
    if prev==r: rep+=1
    prev=r
print('last prime',P[-1],'count 1 mod 6',c1,'count 5 mod 6',c5,'final offset',x,'range',mn,mx,'same door twice in a row %.1f%%'%(100*rep/(len(P)-3)))
