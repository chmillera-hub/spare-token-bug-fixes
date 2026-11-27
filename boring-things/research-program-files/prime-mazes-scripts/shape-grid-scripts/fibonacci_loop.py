import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page()
        await pg.goto('file://'+os.path.abspath('shapes-animation.html')+'')
        for kind in ('oct','ten'):
            r=await pg.evaluate('''k=>{var Wd=newGrowWorld(k,numbersFor("fib",3600,""),"vanish"),out=[],doors=[];for(var i=1;i<=3600;i++){var r=stepGrow(Wd);if(i<=120)doors.push(r.door);if(i%60===0&&i<=600||i===144||i===3600){var c=Wd.tiles[Wd.cur].c,big=0,mv=0;Wd.tiles.forEach(function(t){if(t.e.length>=8)big++;if(t.visits>mv)mv=t.visits;});out.push([i,Wd.tiles.length,big,Wd.doors,Math.round(c[0]*100)/100,Math.round(c[1]*100)/100,mv]);}}return {out:out,d1:doors.slice(0,60).join(""),same:doors.slice(0,60).join("")===doors.slice(60).join("")};}''',kind)
            print(kind,r['same'],r['d1']); [print(x) for x in r['out']]
        await b.close()
asyncio.run(main())
