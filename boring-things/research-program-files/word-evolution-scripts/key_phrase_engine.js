/* phrase-level evolution: strings are lists of whole key phrases plus single joining words and every paste may add or swap or change one piece and never deletes */
function makeWorldP(D,bridges){
  const W={D:D,N:D.u.length,u:D.u,B:bridges||[]};const N=W.N;
  const pairs=new Set();const secOf=new Int32Array(N).fill(-1);const posOf=new Int32Array(N).fill(-1);
  const first=new Array(N),last=new Array(N);for(let k=0;k<N;k++){const w=D.u[k].split(' ');first[k]=w[0];last[k]=w[w.length-1];}
  /* every pair of neighboring words in the source text is remembered so that a joining word can be checked against the source */
  const big=new Set();let prevWord=null,prevSec=-1;
  for(let i=0;i<D.seq.length;i++){const a=D.seq[i];if(secOf[a]<0){secOf[a]=D.sec[i];posOf[a]=i;}
    if(i+1<D.seq.length&&D.sec[i+1]===D.sec[i])pairs.add(a*N+D.seq[i+1]);
    const ws=D.u[a].split(' ');if(D.sec[i]!==prevSec)prevWord=null;for(const w of ws){if(prevWord!==null)big.add(prevWord+' '+w);prevWord=w;}prevSec=D.sec[i];}
  W.secOf=secOf;W.posOf=posOf;W.pairs=pairs;W.big=big;
  W.pick=r=>D.seq[Math.floor(r*D.seq.length)];
  W.pickBridge=r=>N+Math.floor(r*W.B.length);
  W.isB=k=>k>=N;
  W.word=k=>k>=N?W.B[k-N]:D.u[k];
  const fw=k=>k>=N?W.B[k-N]:first[k],lw=k=>k>=N?W.B[k-N]:last[k];
  /* the reader gives one point for every pair of neighboring phrases that are also neighbors in the Bible and a smaller credit for a joining word that fits the words on both sides */
  W.scan=function(t){const n=t.length;const link=new Array(Math.max(0,n-1)).fill(0);let np=0,ns=0;
    for(let i=0;i+1<n;i++){if(t[i]>=N||t[i+1]>=N)continue;if(pairs.has(t[i]*N+t[i+1])){link[i]=2;np++;}else if(secOf[t[i]]===secOf[t[i+1]]&&t[i]!==t[i+1]){link[i]=1;ns++;}}
    const cls=new Array(n);let junk=0,bfit=0,bhalf=0,bbad=0,run=0;
    for(let i=0;i<n;i++){
      if(t[i]>=N){run++;const l=i>0&&big.has(lw(t[i-1])+' '+W.B[t[i]-N]),r=i<n-1&&big.has(W.B[t[i]-N]+' '+fw(t[i+1]));
        if(run>2||i===0||i===n-1){cls[i]='x';bbad++;}else if(l&&r){cls[i]='b';bfit++;}else if(l||r){cls[i]='h';bhalf++;}else{cls[i]='x';bbad++;}}
      else{run=0;cls[i]=((i>0&&link[i-1]===2)||(i<n-1&&link[i]===2))?'c':'j';if(cls[i]==='j')junk++;}}
    return {link,np,ns,cls,junk,bfit,bhalf,bbad};};
  W.fit=function(t,S){const s=W.scan(t);const d=new Set(t.filter(k=>k<N));let ph=0;for(const k of t)if(k<N)ph++;
    return S.pair*s.np+S.same*s.ns+S.uniq*d.size-S.junk*(s.junk+s.bbad)-S.dup*(ph-d.size)+S.join*s.bfit+0.3*S.join*s.bhalf;};
  W.runs=function(t){const s=W.scan(t);const out=[];let i=0;
    while(i<t.length){if(t[i]>=N){i++;continue;}let j=i;while(j<t.length-1&&s.link[j]===2)j++;if(j>i)out.push({text:t.slice(i,j+1).map(k=>D.u[k]).join(' '),n:j-i+1,scene:D.s[secOf[t[i]]],pos:posOf[t[i]]});i=j+1;}
    out.sort((a,b)=>a.pos-b.pos);return out;};
  W.text=t=>t.map(k=>k>=N?'*'+W.B[k-N]+'*':D.u[k]).join(' ');
  return W;}
function makeRunP(W,S,seed){
  let sd=seed;const rnd=()=>{sd|=0;sd=sd+0x6D2B79F5|0;let t=Math.imul(sd^sd>>>15,1|sd);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};const ri=n=>Math.floor(rnd()*n);
  const R={pop:[],fit:[],pastes:0};
  const piece=()=>(W.B.length&&rnd()*100<S.bridge)?W.pickBridge(rnd()):W.pick(rnd());
  R.restart=()=>{R.pop=[];R.fit=[];R.pastes=0;for(let i=0;i<S.pool*S.agents;i++){const t=[W.pick(rnd())];R.pop.push(t);R.fit.push(S.pick<=1?0:W.fit(t,S));}};
  const mutate=t=>{const r=rnd()*100;
    if(r<S.add){if(t.length>=S.maxPhrases)return t;const i=ri(t.length+1);const u=t.slice();u.splice(i,0,piece());return u;}
    if(r<S.add+S.swap){if(t.length<2)return t;const i=ri(t.length-1);const u=t.slice();const x=u[i];u[i]=u[i+1];u[i+1]=x;return u;}
    if(r<S.add+S.swap+S.change){const u=t.slice();u[ri(t.length)]=piece();return u;}
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
