# Compares how many zeta zeros sit below a height T (smooth counting formula)
# with how many primes and how many composite numbers sit below the same number T.
import math
def zeros(T): return T/(2*math.pi)*math.log(T/(2*math.pi*math.e))+7/8
N=200000
s=bytearray([1])*(N+1); s[0]=s[1]=0
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
pc=0; cross_p=None; cross_c=None; last_c_ahead=None
for T in range(2,N+1):
    pc+=s[T]; comp=T-1-pc
    if T>=15:
        z=zeros(T)
        if cross_p is None and z>pc: cross_p=T
        if z<=comp: last_c_ahead=T
    if T in (100,1000,3821,10000,100000,200000): print(T,'primes',pc,'composites',comp,'zeros %.1f'%zeros(T))
print('first T (from 15 up) where zeros exceed primes:',cross_p)
print('last T where composites are at least the zero count:',last_c_ahead)
for T in (100,1000,10000,100000):
    print(T,'zeros per unit of height %.3f'%(math.log(T/(2*math.pi))/(2*math.pi)),'primes per unit %.3f'%(1/math.log(T)),'composites per unit %.3f'%(1-1/math.log(T)))
