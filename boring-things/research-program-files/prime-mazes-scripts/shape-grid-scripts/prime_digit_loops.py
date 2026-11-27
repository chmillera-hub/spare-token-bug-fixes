import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file://'+os.path.abspath('shapes-animation.html')+'')
        for src in ('primedigits','wholeprime','lastdigit','gap','primesums'):
            r=await pg.evaluate('s=>growRun("ten",s,3600,"vanish")',src); print(src,r['tiles'],r['back'],r['width'],r['height'])
        r=await pg.evaluate('''()=>{var nums=numbersFor("primedigits",3600,""),Wd=newGrowWorld("ten",nums,"vanish"),pos=[[0,0]],tl=[1],bk=[0];
          for(var i=0;i<3600;i++){stepGrow(Wd);var c=Wd.tiles[Wd.cur].c;pos.push([c[0],c[1]]);tl.push(Wd.tiles.length);bk.push(Wd.back);}
          // unit step vectors of each door from the template
          var G=growTemplate("ten"),t=G.tab[G.start],dv=t.e.map(function(ed){var sm=G.tab[ed.sig].e.length<t.e.length;return [ed.off[0]*(sm?2:1),ed.off[1]*(sm?2:1)];});
          return {pos:pos,tl:tl,bk:bk,dv:dv};}''')
        pos=r['pos'];dv=r['dv'];L=2.414213562
        print('door vectors in room widths (x right, y down):',[(round(v[0]/L,2),round(v[1]/L,2)) for v in dv])
        # primes and digit index
        def primes(n):
            s=bytearray([1])*(n+1);s[0]=s[1]=0
            for i in range(2,int(n**.5)+1):
                if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
            return [i for i in range(n+1) if s[i]]
        P=primes(20000); idx=0; segs={}
        order=[]
        for q in P:
            d=str(q)
            if idx+len(d)>3600: break
            key=(len(d),d[0])
            if key not in segs: segs[key]=[idx,idx,0]; order.append(key)
            segs[key][1]=idx+len(d); segs[key][2]+=1
            idx+=len(d)
        print('digits used',idx,'last prime',q)
        for key in order:
            a,bb,cnt=segs[key]
            dx=(pos[bb][0]-pos[a][0])/L; dy=(pos[bb][1]-pos[a][1])/L
            # predicted: sum of door vectors of the digits
            print('primes with %d digits starting with %s: %4d primes, digits %4d-%4d, moved right %7.1f down %7.1f rooms, per prime (%.2f, %.2f), new rooms %d, steps back %d'%(key[0],key[1],cnt,a,bb,dx,dy,dx/cnt,dy/cnt,r['tl'][bb]-r['tl'][a],r['bk'][bb]-r['bk'][a]))
        # predicted drift per prime for 4-digit primes with lead digit a: lead vector + avg of middle digits (uniform 0-9) *2 + avg last (1,3,7,9)
        avg=[sum(v[0] for v in dv)/10/L,sum(v[1] for v in dv)/10/L]; last=[sum(dv[d][0] for d in (1,3,7,9))/4/L,sum(dv[d][1] for d in (1,3,7,9))/4/L]
        print('average of all ten doors',avg,'average of doors 1 3 7 9',last)
        for a in range(1,10): print('predicted per prime for 4 digits starting with',a,(round(dv[a][0]/L+2*avg[0]+last[0],2),round(dv[a][1]/L+2*avg[1]+last[1],2)))
        await b.close()
asyncio.run(main())
