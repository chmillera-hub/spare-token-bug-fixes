import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page()
        await pg.goto('file://'+os.path.abspath('shapes-animation.html'))
        r=await pg.evaluate('''()=>{var nums=hatNumbers("counting",3249,""),Wd=newHatWorld(nums),seq=[],lastNew=0,kinds=[];
          for(var i=0;i<nums.length;i++){var t=Wd.tiles.length,res=stepHat(Wd);if(Wd.tiles.length>t)lastNew=i+1;seq.push(Wd.cur);kinds.push(res.kind);}
          // find period of (tile, n mod 14) after lastNew
          var st=seq.map(function(c,i){return c+"_"+(nums[i]%14);}),per=0;
          for(var P=14;P<=2000&&!per;P+=14){var ok=true;for(var j=lastNew+50;j<lastNew+50+2*P&&j+P<st.length;j++)if(st[j]!==st[j+P]){ok=false;break;}if(ok)per=P;}
          var start=lastNew;while(start>0&&start+per<st.length&&st[start-1]===st[start-1+per])start--;
          var cyc=seq.slice(lastNew+100,lastNew+100+per),cnt={},bl=0;cyc.forEach(function(c){cnt[c]=(cnt[c]||0)+1;});for(var q=lastNew+100;q<lastNew+100+per;q++)if(kinds[q]==="blocked")bl++;
          var vis516={};var W2=newHatWorld(nums);for(i=0;i<516;i++)stepHat(W2);var v=W2.tiles.map(function(t){return t.visits;});
          var total=Wd.tiles.map(function(t){return t.visits;});
          return {first:nums[0],lastNew:lastNew,per:per,cycleStartsAtStep:start,tilesInCycle:Object.keys(cnt).length,cnt:cnt,blockedPerCycle:bl,v516:v,vEnd:total,blockedTotal:Wd.blocked};}''')
        for k,v in r.items(): print(k,v)
        await b.close()
asyncio.run(main())
