const {CMDS,RANK,SCENES,sceneOf}=require('./cmds.js');
const AL='abcdefghijklmnopqrstuvwxyz ';const MAXLEN=300;
const kids=[new Map()],term=[-1];
CMDS.forEach((c,ci)=>{let n=0;for(const ch of c){let k=kids[n].get(ch);if(k===undefined){k=kids.length;kids.push(new Map());term.push(-1);kids[n].set(ch,k);}n=k;}term[n]=ci;});
const rows=[];for(let i=0;i<64;i++)rows.push(new Int16Array(64));
let best,bestC,X,L;
function dfs(n,depth){const prev=rows[depth-1],row=rows[depth];
  for(const [ch,k] of kids[n]){row[0]=depth;let mn=depth;const cc=ch.charCodeAt(0);
    for(let j=1;j<=L;j++){const c=prev[j-1]+(X.charCodeAt(j-1)===cc?0:1);const a=prev[j]+1,b=row[j-1]+1;const v=c<a?(c<b?c:b):(a<b?a:b);row[j]=v;if(v<mn)mn=v;}
    if(term[k]>=0&&row[L]<best){best=row[L];bestC=term[k];}
    if(mn<best&&depth<62)dfs(k,depth+1);}}
const cache=new Map();
function sim(r){ // closeness of a leftover stretch to the nearest command (0 to 1)
  if(r.length>40)return {v:0,c:-1};let v=cache.get(r);if(v!==undefined)return v;
  X=r;L=r.length;best=13;bestC=-1;for(let j=0;j<=L;j++)rows[0][j]=j;dfs(0,1);
  v=bestC<0?{v:0,c:-1}:{v:1-best/Math.max(L,CMDS[bestC].length),c:bestC};if(cache.size>400000)cache.clear();cache.set(r,v);return v;}
function parse(x){const t=x.trim().split(' ').filter(Boolean);const found=new Set();const junk=[];let cur=[];let inside=0;
  for(let i=0;i<t.length;){let n=0,bj=-1,bid=-1,ok=true;
    for(let j=i;j<t.length&&ok;j++){const s=(j>i?' ':'')+t[j];for(const ch of s){const k=kids[n].get(ch);if(k===undefined){ok=false;break;}n=k;}if(ok&&term[n]>=0){bj=j;bid=term[n];}}
    if(bj>=0){if(cur.length){junk.push(cur.join(' '));cur=[];}if(!found.has(bid)){found.add(bid);for(let j=i;j<=bj;j++)inside+=t[j].length+1;}i=bj+1;}else{cur.push(t[i]);i++;}}
  if(cur.length)junk.push(cur.join(' '));return {found,junk,inside};}
const BONUS=process.env.BONUS==='1';const UNIQ=+(process.env.UNIQ||0);const CW=CMDS.map(c=>c.split(' '));const RK=CMDS.map(c=>RANK.get(c));
function fitness(x){const p=parse(x);let m=0,jl=0,coh=0;const rk=[];p.found.forEach(i=>rk.push(RK[i]));rk.sort((a,b)=>a-b);
  if(BONUS)for(let i=1;i<rk.length;i++)coh+=0.5*Math.exp(-(rk[i]-rk[i-1])/500);
  const ws=new Set();if(UNIQ>0)p.found.forEach(i=>{for(const w of CW[i])ws.add(w);});
  for(const r of p.junk){const s=sim(r);let w=1;
    if(UNIQ>0&&s.c>=0){let nw=0;for(const q of CW[s.c])if(!ws.has(q))nw++;w*=0.5+0.5*nw/CW[s.c].length;}
    if(BONUS&&rk.length&&s.c>=0){let g=1e9;const q=RK[s.c];for(const k of rk){const d=Math.abs(k-q);if(d<g)g=d;}w=0.5+0.5*Math.exp(-g/500);}
    m+=s.v*s.v*w;jl+=r.length;}
  return {f:p.found.size+coh+UNIQ*ws.size+0.9*m-0.004*jl,n:p.found.size,inside:p.inside};}
let seed=1;function rnd(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;}
const ri=n=>Math.floor(rnd()*n);const tidy=x=>x.replace(/ +/g,' ');
function mutate(x,noSpaceLoophole){const r=rnd()*100;
  if(r<30){if(x.length>=MAXLEN)return x;const i=ri(x.length+1);return tidy(x.slice(0,i)+AL[ri(27)]+x.slice(i));}
  if(r<40){if(x.length<2)return x;const i=ri(x.length-1);return tidy(x.slice(0,i)+x[i+1]+x[i]+x.slice(i+2));}
  if(r<50){const i=ri(x.length);const y=x.slice(0,i)+AL[ri(27)]+x.slice(i+1);const z=tidy(y);return (noSpaceLoophole&&z.length<x.length)?x:z;}
  return x;}
function run(name,cfg,total,sd,marks){seed=sd;cache.clear();const P=300,pick=3;let pop=[],F=[],N=[];
  for(let i=0;i<P;i++){pop.push(AL[ri(26)]);const s=fitness(pop[i]);F.push(s.f);N.push(s.n);}
  const t0=Date.now();
  for(let n=1;n<=total;n++){
    let p=ri(P);for(let k=1;k<pick;k++){const j=ri(P);if(F[j]>F[p])p=j;}
    const ch=mutate(pop[p],true);const s=ch===pop[p]?{f:F[p],n:N[p]}:fitness(ch);
    let w=ri(P);for(let k=1;k<pick;k++){const j=ri(P);if(F[j]<F[w])w=j;}
    pop[w]=ch;F[w]=s.f;N[w]=s.n;
    if(cfg.force&&n%(cfg.force*10)===0){for(let i=0;i<P;i++){const x=pop[i];if(x.length<MAXLEN){const k=ri(x.length+1);pop[i]=x.slice(0,k)+AL[ri(26)]+x.slice(k);const q=fitness(pop[i]);F[i]=q.f;N[i]=q.n;}}}
    if(marks.includes(n)){let b=0;for(let i=1;i<P;i++)if(F[i]>F[b])b=i;const q=fitness(pop[b]);const all=new Set();for(const x of pop)parse(x).found.forEach(v=>all.add(v));
      console.log(`[${name} seed ${sd}] pastes=${n} (~${Math.round(n/600)} min) best string holds ${q.n} different commands | pool average ${(N.reduce((a,b)=>a+b,0)/P).toFixed(1)} | different commands anywhere in pool ${all.size} | best length ${pop[b].length} | letters inside commands ${Math.round(100*q.inside/Math.max(1,pop[b].trim().length+1))}% | ${Date.now()-t0} ms\n    "${pop[b]}"`);if(n===total)story(pop[b]);}
  }}
function story(x){const ids=[];const t=x.trim().split(' ').filter(Boolean);const seen=new Set();
  for(let i=0;i<t.length;){let n=0,bj=-1,bid=-1,ok=true;for(let j=i;j<t.length&&ok;j++){const s=(j>i?' ':'')+t[j];for(const ch of s){const k=kids[n].get(ch);if(k===undefined){ok=false;break;}n=k;}if(ok&&term[n]>=0){bj=j;bid=term[n];}}
    if(bj>=0){if(!seen.has(bid)){seen.add(bid);ids.push(bid);}i=bj+1;}else i++;}
  const ev=ids.map(i=>CMDS[i]);const st=ev.slice().sort((a,b)=>RANK.get(a)-RANK.get(b));
  const allw=ev.join(' ').split(' ').filter(Boolean);console.log('    words inside commands '+allw.length+' | different words '+new Set(allw).size+' | share of words that are not repeats '+Math.round(100*new Set(allw).size/Math.max(1,allw.length))+'%');
  const rk=st.map(c=>RANK.get(c));let gs=0;for(let i=1;i<rk.length;i++)gs+=rk[i]-rk[i-1];console.log('    commands '+ev.length+' | scenes covered '+new Set(st.map(sceneOf)).size+' | average gap between neighbors in the 10000-command story '+(rk.length>1?Math.round(gs/(rk.length-1)):0)+' places');
  const sw=l=>{let s=0;for(let i=1;i<l.length;i++)if(sceneOf(l[i])!==sceneOf(l[i-1]))s++;return s;};
  console.log('    evolved order ('+sw(ev)+' scene changes): '+ev.join(' / '));
  console.log('    story order   ('+sw(st)+' scene changes): '+st.map(c=>c+' ['+SCENES[sceneOf(c)]+']').join(' / '));}
const a=process.argv[2];
if(a==='S'){for(const x of process.argv.slice(3))story(x);}
if(a==='A')run('no forcing',{force:0},900000,+process.argv[3],[600000,900000]);
if(a==='B')run('forced every 5 min',{force:300},600000,5,[60000,300000,600000]);
if(a==='C')run('forced every 60 s',{force:60},600000,5,[60000,300000,600000]);
