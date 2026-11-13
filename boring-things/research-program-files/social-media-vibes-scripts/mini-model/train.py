import re,glob,time,math,sys,torch,torch.nn as nn,torch.nn.functional as F
from tokenizers import Tokenizer,models,trainers,pre_tokenizers,decoders
torch.manual_seed(0); torch.set_num_threads(2)
src='../../../../1-research-click-here-first/social-media-vibes/owner-comments-full'
c=[]
for f in sorted(glob.glob(src+'/part-*.txt')):
    p=re.split(r'===== Comment (\d+) =====\n',open(f,encoding='utf-8').read())
    c+=[re.sub(r'\s+',' ',p[i+1].lower().replace('’',"'").replace('“','"').replace('”','"')).strip() for i in range(1,len(p)-1,2)]
tok=Tokenizer(models.BPE(unk_token='<unk>')); tok.pre_tokenizer=pre_tokenizers.ByteLevel(add_prefix_space=True); tok.decoder=decoders.ByteLevel()
tok.train_from_iterator(c,trainers.BpeTrainer(vocab_size=4096,special_tokens=['<unk>','<eot>'],initial_alphabet=pre_tokenizers.ByteLevel.alphabet()))
tok.save('word-pieces.json'); eot=tok.token_to_id('<eot>')
ids=[]
for x in c: ids+=tok.encode(x).ids+[eot]
data=torch.tensor(ids); n=int(len(data)*0.97); tr,va=data[:n],data[n:]
print('tokens',len(data),flush=True)
V,C,D,H,L,B=4096,128,192,4,4,32
class Blk(nn.Module):
    def __init__(s):
        super().__init__(); s.l1=nn.LayerNorm(D); s.l2=nn.LayerNorm(D); s.a=nn.MultiheadAttention(D,H,batch_first=True); s.m=nn.Sequential(nn.Linear(D,4*D),nn.GELU(),nn.Linear(4*D,D))
    def forward(s,x,mask):
        h=s.l1(x); x=x+s.a(h,h,h,attn_mask=mask,need_weights=False)[0]; return x+s.m(s.l2(x))
class G(nn.Module):
    def __init__(s):
        super().__init__(); s.e=nn.Embedding(V,D); s.p=nn.Embedding(C,D); s.b=nn.ModuleList(Blk() for _ in range(L)); s.n=nn.LayerNorm(D); s.o=nn.Linear(D,V,bias=False); s.o.weight=s.e.weight
    def forward(s,x):
        T=x.shape[1]; mask=torch.triu(torch.ones(T,T,dtype=torch.bool),1)
        h=s.e(x)+s.p(torch.arange(T))
        for b in s.b: h=b(h,mask)
        return s.o(s.n(h))
m=G(); nn.init.normal_(m.e.weight,std=0.02); nn.init.normal_(m.p.weight,std=0.02); print('params',sum(p.numel() for p in m.parameters()),flush=True)
opt=torch.optim.AdamW(m.parameters(),lr=1e-3,weight_decay=0.01)
def batch(d):
    i=torch.randint(len(d)-C-1,(B,)); return torch.stack([d[j:j+C] for j in i]),torch.stack([d[j+1:j+C+1] for j in i])
budget=float(sys.argv[1]); t0=time.time(); it=0
while time.time()-t0<budget:
    fr=(time.time()-t0)/budget
    for g in opt.param_groups: g['lr']=1e-3*min(1,it/100)*(0.5*(1+math.cos(math.pi*fr)))+1e-5
    x,y=batch(tr); loss=F.cross_entropy(m(x).view(-1,V),y.view(-1)); opt.zero_grad(); loss.backward(); nn.utils.clip_grad_norm_(m.parameters(),1.0); opt.step(); it+=1
    if it%100==0:
        m.eval()
        with torch.no_grad(): vl=sum(F.cross_entropy(m(a).view(-1,V),b.view(-1)).item() for a,b in [batch(va) for _ in range(4)])/4
        m.train(); print(it,round(time.time()-t0),round(loss.item(),3),round(vl,3),flush=True); torch.save(m.state_dict(),'model.pt')
torch.save(m.state_dict(),'model.pt'); print('done',it,flush=True)
