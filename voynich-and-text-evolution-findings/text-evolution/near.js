const {CMDS}=require('./cmds.js');
const AL='abcdefghijklmnopqrstuvwxyz ';
// trie
const kids=[new Map()],term=[-1];
CMDS.forEach((c,ci)=>{let n=0;for(const ch of c){let k=kids[n].get(ch);if(k===undefined){k=kids.length;kids.push(new Map());term.push(-1);kids[n].set(ch,k);}n=k;}term[n]=ci;});
const rows=[];for(let i=0;i<64;i++)rows.push(new Int16Array(700));
let best,bestC,X,L;
function dfs(n,depth){
  const prev=rows[depth-1],row=rows[depth];
  for(const [ch,k] of kids[n]){
    row[0]=depth;let mn=depth;
    for(let j=1;j<=L;j++){const c=prev[j-1]+(X.charCodeAt(j-1)===ch.charCodeAt(0)?0:1);const a=prev[j]+1,b=row[j-1]+1;const v=c<a?(c<b?c:b):(a<b?a:b);row[j]=v;if(v<mn)mn=v;}
    if(term[k]>=0&&row[L]<best){best=row[L];bestC=term[k];}
    if(mn<best)dfs(k,depth+1);
  }
}
function nearest(x,bound){X=x;L=x.length;best=bound+1;bestC=-1;for(let j=0;j<=L;j++)rows[0][j]=j;dfs(0,1);return {d:best,c:bestC};}
// experiment
let seed=1;function rnd(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;}
const ri=n=>Math.floor(rnd()*n);const tidy=x=>x.replace(/ +/g,' ');
function mutate(x){const r=rnd()*100;
  if(r<30){const i=ri(x.length+1);return tidy(x.slice(0,i)+AL[ri(27)]+x.slice(i));}
  if(r<40){if(x.length<2)return x;const i=ri(x.length-1);return x.slice(0,i)+x[i+1]+x[i]+x.slice(i+2);}
  if(r<50){const i=ri(x.length);return tidy(x.slice(0,i)+AL[ri(27)]+x.slice(i+1));}
  return x;}
function run(name,cfg,total,sd){
  seed=sd;const P=300,pick=cfg.pick;let pop=[],D=[],Cc=[],F=[];
  const score=(x,bound)=>{const t=x.trim();if(!t.length)return {d:99,c:-1,f:0};let r=nearest(t,bound);if(r.c<0)r=nearest(t,60);return {d:r.d,c:r.c,f:1-r.d/Math.max(t.length,CMDS[r.c].length)};};
  for(let i=0;i<P;i++){const x=AL[ri(26)];const s=score(x,60);pop.push(x);D.push(s.d);Cc.push(s.c);F.push(s.f);}
  let firstExact=-1;const t0=Date.now();const log=[];
  for(let n=1;n<=total;n++){
    let p=ri(P);for(let k=1;k<pick;k++){const j=ri(P);if(F[j]>F[p])p=j;}
    const ch=mutate(pop[p]);const s=ch===pop[p]?{d:D[p],c:Cc[p],f:F[p]}:score(ch,D[p]+2);
    let w=ri(P);for(let k=1;k<pick;k++){const j=ri(P);if(F[j]<F[w])w=j;}
    pop[w]=ch;D[w]=s.d;Cc[w]=s.c;F[w]=s.f;
    if(s.d===0&&firstExact<0)firstExact=n;
    if(cfg.force&&n%(cfg.force*10)===0){for(let i=0;i<P;i++){const x=pop[i],k=ri(x.length+1);pop[i]=x.slice(0,k)+AL[ri(26)]+x.slice(k);const q=score(pop[i],D[i]+1);D[i]=q.d;Cc[i]=q.c;F[i]=q.f;}}
    if(cfg.marks.includes(n)){
      const exact=D.filter(d=>d===0).length,distinct=new Set(pop.filter((_,i)=>D[i]===0).map(x=>x.trim())).size;
      const ms=F.reduce((a,b)=>a+b,0)/P,ml=pop.reduce((a,b)=>a+b.length,0)/P;let b=0;for(let i=1;i<P;i++)if(F[i]>F[b])b=i;
      const ex=[...new Set(pop.map(x=>x.trim()))].slice(0,4);
      console.log(`[${name} seed ${sd}] pastes=${n} (~${Math.round(n/600)} min) exact commands in pool=${exact}/300 distinct exact=${distinct} mean closeness=${ms.toFixed(2)} mean length=${ml.toFixed(0)} first exact at paste ${firstExact} | best "${pop[b].trim()}" nearest "${CMDS[Cc[b]]}" | others: ${ex.map(e=>'"'+e+'"').join(' ; ')} | ${Date.now()-t0} ms`);
    }
  }
}
module.exports={run,CMDS};

if(require.main===module){
  const a=process.argv[2];const M=[3000,30000,150000,300000];
  if(a==='A') for(const sd of [5,6]) run('closeness reader no forcing',{pick:3,force:0,marks:M},300000,sd);
  if(a==='B') for(const sd of [5,6]) run('closeness reader forced every 5 min',{pick:3,force:300,marks:M},300000,sd);
  if(a==='C') run('closeness reader forced every 60 s',{pick:3,force:60,marks:[30000,90000,150000]},150000,5);
  if(a==='D') run('closeness reader forced every 20 min',{pick:3,force:1200,marks:[150000,300000,600000]},600000,5);
}
