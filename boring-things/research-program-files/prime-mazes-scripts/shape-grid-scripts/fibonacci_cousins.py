# Do all sequences that follow the Fibonacci adding rule close their walk on ten sided rooms?
# A cousin starts from any pair of last digits (a b) and each next last digit is the sum of the two before.
# The door on a ten sided room is the last digit. A diagonal door passes through a square to the diagonal large room.
v10={0:(0,-1),1:(1,-1),2:(1,-1),3:(1,0),4:(1,1),5:(0,1),6:(-1,1),7:(-1,1),8:(-1,0),9:(-1,-1)}  # x right and y down
v8={0:(0,-1),1:(1,-1),2:(1,0),3:(1,1),4:(0,1),5:(-1,1),6:(-1,0),7:(-1,-1)}
def orbits(m):
    seen=set();out=[]
    for a in range(m):
        for b in range(m):
            if (a,b) in seen: continue
            cyc=[];x,y=a,b
            while (x,y) not in seen:
                seen.add((x,y));cyc.append(x);x,y=y,(x+y)%m
            out.append(((a,b),cyc))
    return out
for m,v,name in ((10,v10,'ten sided rooms'),(8,v8,'eight sided rooms')):
    print(name)
    closed=0;pairs_closed=0;total=0
    for (a,b),cyc in orbits(m):
        dx=sum(v[d][0] for d in cyc);dy=sum(v[d][1] for d in cyc)
        rooms=set();x=y=0;rooms.add((0,0))
        for d in cyc: x+=v[d][0];y+=v[d][1];rooms.add((x,y))
        total+=len(cyc)
        if dx==0 and dy==0: closed+=1;pairs_closed+=len(cyc)
        print('  start pair',(a,b),'cycle of',len(cyc),'last digits: net move right',dx,'down',dy,'large rooms in one lap',len(rooms),'CLOSED' if dx==0 and dy==0 else 'drifts')
    print('  cycles that close:',closed,'which hold',pairs_closed,'of the',total,'starting pairs')
# why the sideways part cancels on ten sided rooms
F=[1,1]
while len(F)<60: F.append((F[-1]+F[-2])%10)
print('F(n+30) + F(n) ends in 0 for every n:',all((F[n]+F[n+30])%10==0 for n in range(30)))
print('door d plus door 10-d: net move for d = 0..5:',[(v10[d][0]+v10[(10-d)%10][0],v10[d][1]+v10[(10-d)%10][1]) for d in range(6)])
half=F[:30];print('first 30 last digits',''.join(map(str,half)))
print('net down over the first 30 doors plus their partners:',sum(v10[d][1]+v10[(10-d)%10][1] for d in half))
