"""Make original background music from scratch for the shelf video.

Usage: python3 tools/video_music.py SECONDS OUTPUT.wav

Soft pad chords plus a gentle plucked pattern. No existing recording is used.
Needs NumPy.
"""
import numpy as np, wave, sys
sr=44100; total=float(sys.argv[1]); bpm=72; beat=60/bpm; bar=4*beat
rng=np.random.default_rng(7)
def hz(m): return 440*2**((m-69)/12)
prog=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,66],[57,60,64,67],[53,57,60,65],[50,53,57,60],[52,55,59,62]]  # Am7 Fmaj7 Cmaj7 Gmaj7 Am7 F6 Dm7 Em7
n=int(total*sr); L=np.zeros(n); R=np.zeros(n)
def add(buf_l,buf_r,start,sig,pan):
    a=int(start*sr); b=min(n,a+len(sig))
    if a>=n: return
    buf_l[a:b]+=sig[:b-a]*(1-pan); buf_r[a:b]+=sig[:b-a]*pan
bars=int(total/bar)+1
for k in range(bars):
    ch=prog[k%len(prog)]; t0=k*bar
    # pad: slow swell, two detuned sines per note
    dur=bar*1.25; t=np.arange(int(dur*sr))/sr
    env=np.minimum(t/1.2,1)*np.minimum((dur-t)/1.4,1)
    pad=sum(np.sin(2*np.pi*hz(m-12)*t)+0.6*np.sin(2*np.pi*hz(m)*1.003*t)+0.3*np.sin(2*np.pi*hz(m)*0.997*t) for m in ch)
    add(L,R,t0,0.035*pad*env,0.5)
    # bass
    tb=np.arange(int(bar*sr))/sr
    add(L,R,t0,0.11*np.sin(2*np.pi*hz(ch[0]-24)*tb)*np.minimum(tb/0.05,1)*np.exp(-tb/2.2),0.5)
    # pluck pattern: eighth notes with a little variation
    order=[0,2,1,3,2,1,3,2] if k%4!=3 else [0,1,2,3,3,2,1,0]
    for j,idx in enumerate(order):
        if k%8==7 and j%2==1: continue
        m=ch[idx]+12+(12 if (j==4 and k%2==0) else 0)
        tp=np.arange(int(1.6*sr))/sr
        tone=(np.sin(2*np.pi*hz(m)*tp)+0.35*np.sin(2*np.pi*2*hz(m)*tp)*np.exp(-tp/0.25))*np.exp(-tp/0.55)*np.minimum(tp/0.004,1)
        add(L,R,t0+j*beat/2,0.07*tone,0.3+0.4*((j*37)%10)/10)
# gentle shimmer every 8 bars
for k in range(0,bars,8):
    ts=np.arange(int(6*sr))/sr
    add(L,R,k*bar,0.02*np.sin(2*np.pi*hz(88)*ts)*np.minimum(ts/2,1)*np.exp(-ts/3),0.7)
# simple echo
d=int(0.375*sr)
for buf in (L,R):
    buf[d:]+=0.28*buf[:-d]; buf[2*d:]+=0.1*buf[:-2*d]
# master: fade in 1.5 s, fade out 5 s, normalise softly
t=np.arange(n)/sr; fade=np.minimum(t/1.5,1)*np.minimum((total-t)/5,1)
st=np.stack([L,R],1)*fade[:,None]; st=np.tanh(st*1.4); st*=0.5/np.max(np.abs(st))
w=wave.open(sys.argv[2],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
print('music seconds',total)
