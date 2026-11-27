import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file://'+os.path.abspath('shapes-animation.html'))
        srcs=await pg.evaluate('()=>Array.from(el("src").options).map(o=>[o.value,o.textContent]).filter(o=>o[0]!=="own")')
        rows=[]
        for v,label in srcs:
            reps=5 if v=='random' else 1
            acc=[]
            for _ in range(reps):
                r=await pg.evaluate('''v=>{var N=3600,nums=numbersFor(v,N,""),Wd=newGrowWorld("ten",nums,"vanish"),lastNew=0,ret=0,L=2.414213562;
                  for(var i=1;i<=N;i++){var t=Wd.tiles.length;stepGrow(Wd);if(Wd.tiles.length>t)lastNew=i;if(Wd.cur===0)ret++;}
                  var g=growScore(Wd),big=0,mv=0,x0=1e9,x1=-1e9,y0=1e9,y1=-1e9;Wd.tiles.forEach(function(t){if(t.e.length>=Wd.bigDoors)big++;if(t.visits>mv)mv=t.visits;if(t.c[0]<x0)x0=t.c[0];if(t.c[0]>x1)x1=t.c[0];if(t.c[1]<y0)y0=t.c[1];if(t.c[1]>y1)y1=t.c[1];});
                  return {score:g.score,region:g.big,walk:g.len,cut:g.cut,large:big,back:Wd.back,maxv:mv,w:Math.round((x1-x0)/L)+1,h:Math.round((y1-y0)/L)+1,lastNew:lastNew,ret:ret};}''',v)
                acc.append(r)
            r=acc[0]
            if reps>1:
                for k in ('score','region','walk','large','back','maxv','w','h','lastNew','ret'): r[k]=round(sum(a[k] for a in acc)/reps)
            r['v']=v;r['label']=label;rows.append(r)
        rows.sort(key=lambda r:-r['score'])
        json.dump(rows,open('ten_sided_ranking_results.json','w'))
        for i,r in enumerate(rows): print(i+1,r['v'],'|',r['score'],'+' if r['cut'] else '','reg',r['region'],'walk',r['walk'],'large',r['large'],'back',r['back'],'maxv',r['maxv'],'%dx%d'%(r['w'],r['h']),'lastNew',r['lastNew'],'ret',r['ret'])
        await b.close()
asyncio.run(main())
