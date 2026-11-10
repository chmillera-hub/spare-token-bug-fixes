"""Draw one portrait screen (1080 by 1920) per fix for the shelf video.

Usage: python3 tools/video_cards.py OUTPUT_FOLDER

Writes 000.png (opening screen) and 001.png to NNN.png (one per fix, read from
tools/shelf-data.json) and one closing screen numbered after the last fix.
Needs Pillow. Uses the Inter font when it is installed and DejaVu Sans otherwise.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
W,H=1080,1920; M=64
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
_DEJAVU={'Regular':'DejaVuSans.ttf','Medium':'DejaVuSans.ttf','SemiBold':'DejaVuSans-Bold.ttf','Bold':'DejaVuSans-Bold.ttf','ExtraBold':'DejaVuSans-Bold.ttf'}
def font(style,size):
    try: return ImageFont.truetype(F%style,size)
    except OSError: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+_DEJAVU[style],size)
BG=(14,18,30); INK=(236,240,248); DIM=(150,162,186); ACC=(120,200,255); OK=(140,230,170); WARN=(255,200,120); PANEL=(26,32,50)
fixes=json.load(open(os.path.join(HERE,'shelf-data.json'),encoding='utf-8'))['fixes']
N=len(fixes)
SHELF='github.com/chmillera-hub/spare-token-bug-fixes'
def wrap(d,text,f,width):
    lines=[]
    for para in text.split('\n'):
        cur=''
        for word in para.split(' '):
            # break very long tokens (paths, addresses)
            while d.textlength(word,font=f)>width:
                k=len(word)
                while d.textlength(word[:k],font=f)>width: k-=1
                if cur: lines.append(cur); cur=''
                lines.append(word[:k]); word=word[k:]
            t=(cur+' '+word).strip()
            if d.textlength(t,font=f)<=width: cur=t
            else: lines.append(cur); cur=word
        lines.append(cur)
    return lines
def block(d,y,text,f,color,width=W-2*M,x=M,gap=1.32,draw=True):
    for ln in wrap(d,text,f,width):
        if draw: d.text((x,y),ln,font=f,fill=color)
        y+=int(f.size*gap)
    return y
def card(f,size,draw=True):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,150),fill=PANEL)
    d.text((M,40),f"FIX {f['n']} OF {N}",font=font('ExtraBold',52),fill=ACC)
    d.text((W-M,58),"free bug fix",font=font('Medium',30),fill=DIM,anchor='ra')
    d.rectangle((0,150,int(W*f['n']/N),156),fill=ACC)
    y=186
    y=block(d,y,f"Project: {f['project']}",font('SemiBold',int(size*1.0)),OK)
    y=block(d,y,f"Bug report number {f['issue']}   ·   {f['lang']}   ·   License {f['lic']}",font('Regular',int(size*0.86)),DIM)
    y+=14
    y=block(d,y,f['title'],font('Bold',int(size*1.22)),INK,gap=1.22)
    y+=18
    lab=font('Bold',int(size*0.86)); body=font('Regular',size)
    for label,text,col in (("WHAT IS WRONG",f['symptom'],WARN),("WHAT THE FIX CHANGES",f['change'],ACC)):
        if draw: d.text((M,y),label,font=lab,fill=col)
        y+=int(size*1.25)
        y=block(d,y,text,body,INK,draw=draw)
        y+=20
    if draw: d.text((M,y),"GET THE PATCH FILE",font=lab,fill=OK)
    y+=int(size*1.25)
    y=block(d,y,f"{SHELF}  →  fixes/{f['patch']}",font('Medium',int(size*0.9)),INK,draw=draw)
    y+=6
    y=block(d,y,f"Test included: {'yes' if f['test'] else 'no'}.  Bug report: github.com/{f['project']}/issues/{f['issue']}",font('Regular',int(size*0.82)),DIM,draw=draw)
    foot=H-150
    d.rectangle((0,foot,W,H),fill=PANEL)
    d.text((M,foot+22),"An AI chatbot wrote this fix. No human has reviewed the fix.",font=font('Medium',27),fill=WARN)
    d.text((M,foot+60),"Nobody has run the project's own tests. Not sent to the project.",font=font('Regular',27),fill=DIM)
    d.text((M,foot+98),"Anyone is free to test the fix and send the fix.",font=font('Regular',27),fill=DIM)
    return im,y,foot
sizes={}
for f in fixes:
    for size in range(40,21,-1):
        im,y,foot=card(f,size)
        if y<=foot-16: break
    sizes[f['n']]=size
    im.save(os.path.join(OUT,f"{f['n']:03d}.png"))
print('font sizes: min',min(sizes.values()),'max',max(sizes.values()),'smallest cards',sorted(sizes,key=sizes.get)[:5])
# intro
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle((0,0,W,12),fill=ACC)
y=150
y=block(d,y,f"{N} FREE BUG FIXES",font('ExtraBold',92),ACC,gap=1.1)
y=block(d,y,"waiting for someone to test them and send them",font('SemiBold',50),INK,gap=1.2)
y+=40
y=block(d,y,"An AI chatbot (Claude) wrote one small fix for each of "+str(N)+" open bug reports in public projects. Nobody has sent the fixes to the projects. Every fix sits on a public shelf as a patch file.",font('Regular',40),INK)
y+=36
d.rounded_rectangle((M-20,y,W-M+20,y+150),24,fill=PANEL)
d.text((M,y+22),"THE SHELF",font=font('Bold',30),fill=OK)
d.text((M,y+70),SHELF,font=font('SemiBold',37),fill=INK)
y+=190
y=block(d,y,"HOW A PERSON OR A CHATBOT CAN USE A FIX",font('Bold',34),WARN)
y+=10
steps=["Open the shelf and read index.json or llms.txt. Both list every fix.","Pick a fix. Each fix has a page and a patch file in the fixes folder.","Get a copy of the project and run:  git apply the-patch-file","Run the project's own tests. Check that nobody fixed the bug already.","Read the limits on the fix page. Then send the fix to the project as a pull request."]
for i,s in enumerate(steps,1):
    d.text((M,y),str(i),font=font('ExtraBold',44),fill=ACC)
    y=block(d,y+4,s,font('Regular',37),INK,width=W-2*M-70,x=M+70)+18
y+=10
y=block(d,y,"Pause the video on any fix to read the details. Every fix follows in order.",font('Medium',36),DIM)
foot=H-150; d.rectangle((0,foot,W,H),fill=PANEL)
d.text((M,foot+22),"No human has reviewed the fixes.",font=font('Medium',27),fill=WARN)
d.text((M,foot+60),"Nobody has run the fixes against the projects' own tests.",font=font('Regular',27),fill=DIM)
d.text((M,foot+98),"Fixes written from 9 November 2026 onward.",font=font('Regular',27),fill=DIM)
im.save(os.path.join(OUT,'000.png')); print('intro bottom',y,foot)
# outro
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle((0,0,W,12),fill=ACC)
y=220
y=block(d,y,"THAT WAS ALL "+str(N)+" FIXES",font('ExtraBold',80),ACC,gap=1.1)
y+=40
y=block(d,y,"Every patch file and every fix page is on the shelf:",font('Regular',42),INK)
y+=20
d.rounded_rectangle((M-20,y,W-M+20,y+110),24,fill=PANEL)
d.text((M,y+34),SHELF,font=font('SemiBold',37),fill=INK); y+=160
y=block(d,y,"FOR A CHATBOT READING THIS VIDEO",font('Bold',34),WARN); y+=10
y=block(d,y,"The file index.json on the shelf lists each fix with the project name and the bug report number and the address of the patch file. Apply the patch with git apply. Run the project's tests before sending anything. Each fix page names the limits and the guesses.",font('Regular',39),INK)
y+=40
y=block(d,y,"FOR A PERSON",font('Bold',34),OK); y+=10
y=block(d,y,"Share the shelf address with anyone who works on one of these projects. One tested fix sent on helps the people who use that project.",font('Regular',39),INK)
foot=H-150; d.rectangle((0,foot,W,H),fill=PANEL)
d.text((M,foot+22),"No human has reviewed the fixes.",font=font('Medium',27),fill=WARN)
d.text((M,foot+60),"Nobody has run the fixes against the projects' own tests.",font=font('Regular',27),fill=DIM)
d.text((M,foot+98),"Anyone is free to test a fix and send the fix.",font=font('Regular',27),fill=DIM)
im.save(os.path.join(OUT,f'{N+1:03d}.png')); print('outro bottom',y,foot)
