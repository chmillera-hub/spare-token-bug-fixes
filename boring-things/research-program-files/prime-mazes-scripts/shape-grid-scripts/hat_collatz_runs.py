import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio
from playwright.async_api import async_playwright
def steps(n):
    c=0
    while n!=1: n=3*n+1 if n%2 else n//2; c+=1
    return c
S=[steps(i) for i in range(1,3601)]
eq=sum(1 for i in range(1,3600) if S[i]==S[i-1]); print('consecutive equal pairs',eq,'of 3599 = %.1f%%'%(100*eq/3599))
runs=[];r=1
for i in range(1,3600):
    if S[i]==S[i-1]: r+=1
    else: runs.append(r); r=1
runs.append(r); print('longest run of equal step counts',max(runs),'runs of 3 or more',sum(1 for x in runs if x>=3))
from collections import Counter
m=Counter(x%14 for x in S); print('share by remainder mod 14',[round(100*m[k]/3600,1) for k in range(14)])
print('max step count',max(S),'distinct values',len(set(S)))
d=Counter((S[i]-S[i-1])%14 for i in range(1,3600)); print('change in door between neighbors',[round(100*d[k]/3599,1) for k in range(14)])
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page()
        await pg.goto('file://'+os.path.abspath('shapes-animation.html'))
        r=await pg.evaluate('''()=>{function run(nums){var Wd=newHatWorld(nums),bl=0,blSame=0,sameTot=0,sameNew=0,sameBack=0,prevKind="";for(var i=0;i<nums.length;i++){var same=i>0&&nums[i]===nums[i-1],res=stepHat(Wd);if(same){sameTot++;if(res.kind==="blocked")blSame++;else if(res.kind==="new")sameNew++;else sameBack++;}if(res.kind==="blocked")bl++;}var s=hatSummary(Wd);s.blSame=blSame;s.sameTot=sameTot;s.sameNew=sameNew;s.sameBack=sameBack;return s;}
          var c=numbersFor("collatz",3600,""),out={collatz:run(c)};
          // shuffled copy of the same values
          var acc={tiles:0,blocked:0,back:0,loops:0};for(var t=0;t<20;t++){var sh=c.slice();for(var i=sh.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=sh[i];sh[i]=sh[j];sh[j]=x;}var r=run(sh);for(var k in acc)acc[k]+=r[k]/20;}
          out.shuffled=acc;return out;}''')
        print(r)
        await b.close()
asyncio.run(main())
