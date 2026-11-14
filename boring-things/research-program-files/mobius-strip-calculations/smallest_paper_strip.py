# Checks the folded-triangle Mobius strip: a paper strip of width 1 and length sqrt(3) folded flat along
# three slanted creases. The check confirms that the two short ends of the strip land on the same line with
# one end flipped, which is the join that makes a Mobius strip, and that every piece keeps its true size.
import numpy as np
L=np.sqrt(3); h=1/np.sqrt(3)                       # h = how far each crease leans along the strip
creases=[((0,0),(h,1)),((h,1),(2*h,0)),((2*h,0),(3*h,1))]
def reflect_across(p,a,b):
    a=np.array(a,float); b=np.array(b,float); d=(b-a)/np.linalg.norm(b-a); v=np.array(p,float)-a
    return a+2*(v@d)*d-v
def piece_index(p):                                # which of the four pieces a point of the strip lies in
    x,y=p; k=0
    for (a,b) in creases:
        a=np.array(a);b=np.array(b); xc=a[0]+(b[0]-a[0])*(y-a[1])/(b[1]-a[1])
        if x>xc: k+=1
    return k
def folded(p):                                     # where a point of the flat strip ends up after folding
    k=piece_index(p); q=np.array(p,float)
    for i in range(k-1,-1,-1): q=reflect_across(q,*creases[i])   # undo folds from the nearest crease outward
    return q
ys=np.linspace(0,1,11)
left=[folded((0,y)) for y in ys]; right=[folded((L,y)) for y in ys]
gap_flip=max(np.linalg.norm(l-r) for l,r in zip(left,right[::-1]))
gap_same=max(np.linalg.norm(l-r) for l,r in zip(left,right))
print("length divided by width:",round(L,4))
print("largest distance between the left end and the flipped right end after folding:",round(gap_flip,12))
print("largest distance between the left end and the unflipped right end after folding:",round(gap_same,4))
rng=np.random.default_rng(3); worst=0
for _ in range(20000):                             # folding must not stretch the paper inside any one piece
    p=rng.uniform([0,0],[L,1]); q=p+rng.normal(scale=1e-4,size=2)
    if 0<=q[0]<=L and 0<=q[1]<=1 and piece_index(p)==piece_index(q):
        worst=max(worst,abs(np.linalg.norm(folded(p)-folded(q))-np.linalg.norm(p-q)))
print("largest change in distance between nearby points inside one piece:",worst)
corners=np.array([folded(p) for p in [(0,0),(0,1),(h,1),(2*h,0),(3*h,1),(L,0)]])
print("folded shape corner points:",np.round(np.unique(np.round(corners,6),axis=0),4).tolist())
pts=np.array([folded(p) for p in rng.uniform([0,0],[L,1],size=(20000,2))])
print("folded shape fits inside a box of size:",np.round(pts.max(0)-pts.min(0),4).tolist(),"(an equilateral triangle with height 1 has side",round(2/np.sqrt(3),4),")")
