import sys,time
sys.setrecursionlimit(100000)
N=int(sys.argv[1])
a=[1,2]
def run(coins,lo,j):
    memo={}
    def cover(lo,k,j):
        # largest h with [lo,h) inside N(k,j); coins[0..k-1]
        if j<0: return lo
        if k==1: return j+1 if lo<=j else lo
        key=(lo,k,j)
        if key in memo: return memo[key]
        c=coins[k-1]; p=lo
        while True:
            best=p
            for t in range(min(j,p//c),-1,-1):
                if p-t*c>(j-t)*coins[k-2]: break
                q=t*c+cover(p-t*c,k-1,j-t)
                if q>best: best=q
            if best==p: break
            p=best
        memo[key]=p
        return p
    return cover(lo,len(coins),j),len(memo)
t0=time.time()
for n in range(3,N+1):
    m=n-1
    coins=[x-1 for x in a[1:]]
    lo=a[-1]+1-m
    h,sz=run(coins,lo,m)
    a.append(h+m)
    print(n,a[-1],sz,round(time.time()-t0,1),flush=True)
