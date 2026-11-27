import os  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
import asyncio,json
from playwright.async_api import async_playwright
# For each number sequence: the growing score in true order against the average score of 10 shuffled copies.
# Shapes: ten sided rooms (squares disappear) and Einstein hat tiles. Also counts hat steps where no tile fits.
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page()
        await pg.goto('file://'+os.path.abspath('shapes-animation.html'))
        srcs=await pg.evaluate('()=>Array.from(el("src").options).map(o=>[o.value,o.textContent]).filter(o=>o[0]!=="own")')
        out=[]
        for v,label in srcs:
            r=await pg.evaluate('''v=>{var N=3600;
              function run(kind,nums){var Wd=kind==="hat"?newHatWorld(nums):newGrowWorld(kind,nums,"vanish");while(!Wd.done)(kind==="hat"?stepHat:stepGrow)(Wd);var g=growScore(Wd);return {score:g.score,tiles:Wd.tiles.length,walk:g.len,back:Wd.back,blocked:Wd.blocked};}
              function shuf(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=a[i];a[i]=a[j];a[j]=x;}return a;}
              var res={};["ten","hat"].forEach(function(kind){var nums=kind==="hat"?hatNumbers(v,N,""):numbersFor(v,N,""),t=run(kind,nums),S=10,acc={score:0,tiles:0,walk:0,back:0,blocked:0},sq=0;
                for(var s=0;s<S;s++){var q=run(kind,shuf(nums));for(var k in acc)acc[k]+=q[k]/S;sq+=q.score*q.score/S;}
                acc.sd=Math.sqrt(Math.max(0,sq-acc.score*acc.score));res[kind]={true:t,shuffled:acc};});return res;}''',v)
            r['v']=v;r['label']=label;out.append(r)
            t=r['ten'];h=r['hat']
            print('%-12s ten true %5d shuffled %7.1f (sd %5.1f) ratio %.2f | hat true %5d shuffled %7.1f ratio %.2f blocked true %4d shuffled %6.1f'%(v,t['true']['score'],t['shuffled']['score'],t['shuffled']['sd'],t['true']['score']/max(1,t['shuffled']['score']),h['true']['score'],h['shuffled']['score'],h['true']['score']/max(1,h['shuffled']['score']),h['true']['blocked'],h['shuffled']['blocked']))
        json.dump(out,open('shuffle_scores_results.json','w'))
        await b.close()
asyncio.run(main())
