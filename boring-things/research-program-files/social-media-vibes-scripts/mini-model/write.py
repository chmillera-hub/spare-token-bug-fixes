import torch,torch.nn.functional as F,sys,re
from tokenizers import Tokenizer
src=open('train.py').read(); src=src[src.index('V,C,D,H,L,B='):src.index("m=G()")]
import torch.nn as nn; exec(src)
tok=Tokenizer.from_file('word-pieces.json'); m=G(); m.load_state_dict(torch.load('model.pt')); m.eval(); eot=tok.token_to_id('<eot>')
def gen(p,n=70,temp=0.8,k=40,seed=0):
    torch.manual_seed(seed); x=[eot]+tok.encode(p).ids
    for _ in range(n):
        with torch.no_grad(): lg=m(torch.tensor([x[-C:]]))[0,-1]/temp
        v,i=lg.topk(k); nx=i[torch.multinomial(F.softmax(v,-1),1)].item()
        if nx==eot: break
        x.append(nx)
    return tok.decode(x[1:]).strip()
if sys.argv[1]=='gen':
    for p in ["loneliness is","my anger tells me","boredom is a signal that","god is","society wants you to","what does","ai is","the reason people smile and nod is","fear and doubt","meaningful conversation is"]:
        for s in (1,2): print('>>',gen(p,seed=s)); print()
else:
    E=F.normalize(m.e.weight.detach(),dim=1)
    for w in "loneliness boredom anger fear doubt god ai society suffering gaslighting money conversation therapist jesus dopamine".split():
        t=tok.encode(' '+w).ids
        if len(t)!=1: print(w,'(split)'); continue
        s=E@E[t[0]]; print(w,'|',', '.join(tok.decode([j]).strip() for j in s.topk(11).indices[1:].tolist()))
