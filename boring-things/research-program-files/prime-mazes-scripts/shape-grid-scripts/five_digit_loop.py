# The digits of the primes written in one row on ten sided rooms: does the loop of the primes with 5 digits
# measure about 8 times the loop of the primes with 4 digits?  Positions are large room positions in room widths.
from PIL import Image,ImageDraw
v={0:(0,-1),1:(1,-1),2:(1,-1),3:(1,0),4:(1,1),5:(0,1),6:(-1,1),7:(-1,1),8:(-1,0),9:(-1,-1)}
def primes(n):
    b=bytearray([1])*(n+1);b[0]=b[1]=0
    for k in range(2,int(n**.5)+1):
        if b[k]: b[k*k::k]=bytearray(len(b[k*k::k]))
    return [k for k in range(n+1) if b[k]]
P=primes(99999)
x=y=0;pts=[(0,0)];seg={};lead={}
for p in P:
    s=str(p);k=len(s);a=len(pts)-1
    for ch in s: x+=v[int(ch)][0];y+=v[int(ch)][1];pts.append((x,y))
    seg.setdefault(k,[a,a])[1]=len(pts)-1
    lead.setdefault((k,s[0]),[a,a,0]);lead[(k,s[0])][1]=len(pts)-1;lead[(k,s[0])][2]+=1
print('digits used',len(pts)-1)
size={}
for k,(a,b) in seg.items():
    xs=[q[0] for q in pts[a:b+1]];ys=[q[1] for q in pts[a:b+1]]
    size[k]=(max(xs)-min(xs),max(ys)-min(ys))
    print('primes with %d digits: digits %d to %d, loop is %d rooms wide and %d rooms tall, start to end gap (%d, %d)'%(k,a,b,size[k][0],size[k][1],pts[b][0]-pts[a][0],pts[b][1]-pts[a][1]))
for k in (3,4,5):
    print('ratio of loop width for %d digits to %d digits: %.2f and of height: %.2f'%(k,k-1,size[k][0]/size[k-1][0],size[k][1]/size[k-1][1]))
for d in '123456789':
    a,b,c=lead[(5,d)];print('5 digits starting with %s: %d primes, per prime right %.2f down %.2f'%(d,c,(pts[b][0]-pts[a][0])/c,(pts[b][1]-pts[a][1])/c))
xs=[q[0] for q in pts];ys=[q[1] for q in pts];W=1000;pad=30
sc=(W-2*pad)/max(max(xs)-min(xs),max(ys)-min(ys))
im=Image.new('RGB',(W,W),'white');d=ImageDraw.Draw(im)
col={1:(0,0,0),2:(0,0,0),3:(200,60,60),4:(40,120,200),5:(60,150,80)}
for k,(a,b) in seg.items():
    d.line([(pad+(q[0]-min(xs))*sc,pad+(q[1]-min(ys))*sc) for q in pts[a:b+1:3]],fill=col[k],width=3 if k<5 else 2)
im.save('loops-of-prime-digits.png')
