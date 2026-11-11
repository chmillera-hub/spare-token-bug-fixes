/* phrase-level evolution: strings are lists of whole key phrases and every paste may add or swap or change one whole phrase and never deletes */
function makeWorldP(D){
  const W={D:D,N:D.u.length,u:D.u};const N=W.N;
  const pairs=new Set();const secOf=new Int32Array(N).fill(-1);const posOf=new Int32Array(N).fill(-1);
  for(let i=0;i<D.seq.length;i++){const a=D.seq[i];if(secOf[a]<0){secOf[a]=D.sec[i];posOf[a]=i;}
    if(i+1<D.seq.length&&D.sec[i+1]===D.sec[i])pairs.add(a*N+D.seq[i+1]);}
  W.secOf=secOf;W.posOf=posOf;W.pairs=pairs;
  W.pick=r=>D.seq[Math.floor(r*D.seq.length)];
  /* the reader gives one point for every pair of neighboring phrases that are also neighbors in the Bible */
  W.scan=function(t){const link=new Array(Math.max(0,t.length-1));let np=0,ns=0;
    for(let i=0;i+1<t.length;i++){if(pairs.has(t[i]*N+t[i+1])){link[i]=2;np++;}else if(secOf[t[i]]===secOf[t[i+1]]&&t[i]!==t[i+1]){link[i]=1;ns++;}else link[i]=0;}
    const cls=t.map((_,i)=>((i>0&&link[i-1]===2)||(i<t.length-1&&link[i]===2))?'c':'j');let junk=0;for(const c of cls)if(c==='j')junk++;
    return {link,np,ns,cls,junk};};
  W.fit=function(t,S){const s=W.scan(t);const d=new Set(t).size;return S.pair*s.np+S.same*s.ns+S.uniq*d-S.junk*s.junk-S.dup*(t.length-d);};
  W.runs=function(t){const s=W.scan(t);const out=[];let i=0;
    while(i<t.length){let j=i;while(j<t.length-1&&s.link[j]===2)j++;if(j>i)out.push({ids:t.slice(i,j+1),text:t.slice(i,j+1).map(k=>D.u[k]).join(' '),n:j-i+1,scene:D.s[secOf[t[i]]],pos:posOf[t[i]]});i=j+1;}
    out.sort((a,b)=>a.pos-b.pos);return out;};
  W.text=t=>t.map(k=>D.u[k]).join(' / ');
  return W;}
function makeRunP(W,S,seed){
  let sd=seed;const rnd=()=>{sd|=0;sd=sd+0x6D2B79F5|0;let t=Math.imul(sd^sd>>>15,1|sd);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};const ri=n=>Math.floor(rnd()*n);
  const R={pop:[],fit:[],pastes:0};
  R.restart=()=>{R.pop=[];R.fit=[];R.pastes=0;for(let i=0;i<S.pool*S.agents;i++){const t=[W.pick(rnd())];R.pop.push(t);R.fit.push(S.pick<=1?0:W.fit(t,S));}};
  const mutate=t=>{const r=rnd()*100;
    if(r<S.add){if(t.length>=S.maxPhrases)return t;const i=ri(t.length+1);const u=t.slice();u.splice(i,0,W.pick(rnd()));return u;}
    if(r<S.add+S.swap){if(t.length<2)return t;const i=ri(t.length-1);const u=t.slice();const x=u[i];u[i]=u[i+1];u[i+1]=x;return u;}
    if(r<S.add+S.swap+S.change){const u=t.slice();u[ri(t.length)]=W.pick(rnd());return u;}
    return t;};
  R.step=()=>{const a=R.pastes%S.agents,o=a*S.pool;let p=o+ri(S.pool);for(let k=1;k<S.pick;k++){const j=o+ri(S.pool);if(R.fit[j]>R.fit[p])p=j;}
    const ch=mutate(R.pop[p]);const f=ch===R.pop[p]?R.fit[p]:(S.pick<=1?0:W.fit(ch,S));
    let w=o+ri(S.pool);for(let k=1;k<S.pick;k++){const j=o+ri(S.pool);if(R.fit[j]<R.fit[w])w=j;}
    R.pop[w]=ch;R.fit[w]=f;R.pastes++;};
  R.rescore=()=>{for(let i=0;i<R.pop.length;i++)R.fit[i]=S.pick<=1?0:W.fit(R.pop[i],S);};
  R.agentBest=a=>{const o=a*S.pool;let b=o;for(let i=o+1;i<o+S.pool;i++)if(R.fit[i]>R.fit[b])b=i;return b;};
  R.minutes=()=>R.pastes/(600*S.agents);
  return R;}
if(typeof module!=='undefined')module.exports={makeWorldP,makeRunP};
