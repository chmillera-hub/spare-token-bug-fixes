import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':390,'height':844})
        await pg.goto('file://'+os.path.abspath('shapes-animation.html')+'')
        for src in ('counting','triangular'):
          for kind in ('ten','oct','hex','sq'):
            r=await pg.evaluate('''([k,src])=>{var Wd=newGrowWorld(k,numbersFor(src,3600,""),(k==="ten"||k==="oct")?"vanish":""),out=[],marks=[10,20,40,60,100,200,1000,3600],ret=[];for(var i=1;i<=3600;i++){stepGrow(Wd);if(Wd.cur===0&&ret.length<6)ret.push(i);if(marks.indexOf(i)>=0){var c=Wd.tiles[Wd.cur].c,big=0,mv=0;Wd.tiles.forEach(function(t){if(t.e.length>=Wd.bigDoors)big++;if(t.visits>mv)mv=t.visits;});out.push(i+": rooms "+Wd.tiles.length+" large "+big+" doors "+Wd.doors+" at ("+c[0].toFixed(1)+" "+c[1].toFixed(1)+") max visits "+mv);}}return [ret,out];}''',[kind,src])
            print(src,kind,'returns to start at',r[0]); [print('   ',x) for x in r[1]]
        await b.close()
asyncio.run(main())
