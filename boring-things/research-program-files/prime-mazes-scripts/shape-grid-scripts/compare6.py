import asyncio,json,io,base64,os
from playwright.async_api import async_playwright
from PIL import Image,ImageDraw,ImageFont
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':700,'height':900}); await pg.emulate_media(color_scheme='light')
        await pg.goto('file://'+os.path.abspath('shapes-animation.html'))  # a copy of shapes-animation.html from the prime-mazes folder must sit beside this script
        for k,T in ((12,400),(20,200),(30,100)):
            res=await pg.evaluate('''([k,T])=>{var kinds=["tri","sq","pent","hex","oct","ten"],out={};kinds.forEach(function(kind){var n=roomCount(kind,k),s={pct:0,big:0,walk:0,door:0,reg:0,any:0},mx=0;
              for(var t=0;t<T;t++){var d=[];for(var i=0;i<n;i++)d.push(Math.floor(Math.random()*10));var r=fullScore(kind,k,d);mx=r.max;s.pct+=100*r.three/r.max;s.big+=100*r.big/n;s.walk+=100*r.walk/n;s.door+=r.door;s.reg+=r.regions/n;s.any+=r.door>0?1:0;}
              for(var key in s)s[key]=s[key]/T;s.n=n;s.max=mx;out[kind]=s;});return out}''',[k,T])
            print('--- grid size',k,'with',T,'random digit strings for each shape')
            for kind,s in res.items(): print('%-5s rooms %4d | avg score %5.2f%% of max | largest region %5.2f%% of rooms | longest walk %5.2f%% of rooms | regions per room %.3f | any door point in %4.1f%% of trials'%(kind,s['n'],s['pct'],s['big'],s['walk'],s['reg'],100*s['any']))
        imgs={}; sc={}
        names={'tri':'Triangles','sq':'Squares','pent':'Five sided','hex':'Hexagons','oct':'Eight sided + squares','ten':'Ten sided + fillers'}
        for kind in names:
            r=await pg.evaluate('''kind=>{el("grid").value=kind;el("src").value="pi";el("size").value=12;syncBoxes();setup();finishAll();var M=S.M,i=regionInfo(M);return [el("cv").toDataURL("image/png"),i.big,S.walk.len,i.door,2*M.T.n+M.T.doorMax,M.T.n]}''',kind)
            imgs[kind]=Image.open(io.BytesIO(base64.b64decode(r[0].split(',')[1]))).convert('RGB'); sc[kind]=r[1:]
        f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',32); cell=900
        sheet=Image.new('RGB',(2*cell,3*(cell+60)),'white'); d=ImageDraw.Draw(sheet)
        for idx,kind in enumerate(names):
            x=(idx%2)*cell; y=(idx//2)*(cell+60); s=sc[kind]
            d.text((x+24,y+12),'%s: %d of %d (%.1f%%)'%(names[kind],s[0]+s[1]+s[2],s[3],100*(s[0]+s[1]+s[2])/s[3]),fill='black',font=f); sheet.paste(imgs[kind],(x,y+60))
        sheet=sheet.resize((1200,int(sheet.height*1200/sheet.width)),Image.LANCZOS); sheet.save('pi-on-six-grids.png',optimize=True); print(sheet.size, sc)
        await b.close()
asyncio.run(main())
