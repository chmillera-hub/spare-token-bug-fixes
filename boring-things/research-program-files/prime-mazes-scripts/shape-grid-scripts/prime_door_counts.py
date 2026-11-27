# Whole primes on a room with a prime number of doors (7 or 11 or 13).
# No flat grid has rooms with 7 or 11 neighbors each so this is a free walk: each number moves one unit
# in the direction of its door and the doors are spread evenly around a circle with door 0 pointing up.
import math,random
def primes(n):
    b=bytearray([1])*(n+1);b[0]=b[1]=0
    for k in range(2,int(n**.5)+1):
        if b[k]: b[k*k::k]=bytearray(len(b[k*k::k]))
    return [k for k in range(n+1) if b[k]]
P=primes(2000000)
random.seed(3)
for m in (7,11,13):
    for N in (3600,100000):
        Q=P[:N];x=y=0;cnt=[0]*m;rep=0;prev=None
        for p in Q:
            d=p%m;cnt[d]+=1;a=2*math.pi*d/m;x+=math.sin(a);y+=math.cos(a)
            if d==prev: rep+=1
            prev=d
        # random walk using the same doors 1..m-1 with equal chance
        rd=[]
        for t in range(200):
            rx=ry=0
            for i in range(N):
                d=random.randrange(1,m);a=2*math.pi*d/m;rx+=math.sin(a);ry+=math.cos(a)
            rd.append((rx,ry))
        mx=sum(r[0] for r in rd)/200;my=sum(r[1] for r in rd)/200
        sx=(sum((r[0]-mx)**2 for r in rd)/200)**.5
        print('%d doors, first %d primes: door counts %s'%(m,N,cnt))
        print('   end point: %.1f right and %.1f up (predicted up: %.1f). Random doors 1 to %d: sideways spread %.1f. Same door twice in a row %.2f%% (even share %.2f%%)'%(x,y,-N/(m-1),m-1,sx,100*rep/(N-1),100/(m-1)))
