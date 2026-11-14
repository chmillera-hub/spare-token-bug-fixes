/* word-level evolution: strings are lists of whole words and every paste may add or swap or change one whole word and never deletes */
function makeWorld(D){
  const W={};const vocab=new Map();const words=[];const freq=[];
  const Q=D.p.map(q=>q.split(' ').map(w=>{let id=vocab.get(w);if(id===undefined){id=words.length;vocab.set(w,id);words.push(w);freq.push(0);}freq[id]++;return id;}));
  const cum=[];let tot=0;for(const f of freq){tot+=f;cum.push(tot);}
  W.words=words;W.Q=Q;W.D=D;W.N=Q.length;
  W.pick=r=>{const x=r*tot;let lo=0,hi=cum.length-1;while(lo<hi){const m=(lo+hi)>>1;if(cum[m]>x)hi=m;else lo=m+1;}return lo;};
  const kids=[new Map()],term=[-1],minLen=[1e9];
  Q.forEach((q,qi)=>{let n=0;if(q.length<minLen[0])minLen[0]=q.length;for(const w of q){let k=kids[n].get(w);if(k===undefined){k=kids.length;kids.push(new Map());term.push(-1);minLen.push(1e9);kids[n].set(w,k);}n=k;if(q.length<minLen[n])minLen[n]=q.length;}term[n]=qi;});
  W.kids=kids;W.term=term;W.minLen=minLen;W.scale=Math.max(20,W.N/20);
  W.parse=function(t){const found=[],seen=new Set(),cls=new Array(t.length).fill('j');let partial=0,junk=0,best=0;
    const flush=()=>{partial+=best;best=0;};
    for(let i=0;i<t.length;){let n=0,bj=-1,bid=-1,k=0,deep=0;
      for(let j=i;j<t.length;j++){const q=kids[n].get(t[j]);if(q===undefined)break;n=q;k++;deep=n;if(term[n]>=0){bj=j;bid=term[n];}}
      if(bj>=0){flush();if(!seen.has(bid)){seen.add(bid);found.push(bid);for(let j=i;j<=bj;j++)cls[j]='c';}else{for(let j=i;j<=bj;j++)cls[j]='r';junk+=bj-i+1;}i=bj+1;}
      else{if(k>0){const c=k/minLen[deep];if(c*c>best)best=c*c;}junk++;i++;}}
    flush();return {found,cls,partial,junk};};
  W.fit=function(t,S){const p=W.parse(t);let base=0;const ws=new Set();
    for(const i of p.found){base+=Q[i].length/3;if(S.uniq>0)for(const w of Q[i])ws.add(w);}
    let coh=0;if(S.near>0&&p.found.length>1){const rk=p.found.slice().sort((a,b)=>a-b);for(let i=1;i<rk.length;i++)coh+=S.near*Math.exp(-(rk[i]-rk[i-1])/W.scale);}
    return base+coh+S.uniq*ws.size+0.9*p.partial-S.junk*p.junk;};
  W.text=t=>t.map(i=>words[i]).join(' ');
  W.info=function(t){const p=W.parse(t);const ids=p.found.slice().sort((a,b)=>a-b);const all=[];for(const i of p.found)for(const w of Q[i])all.push(w);
    return {n:ids.length,story:ids.map(i=>({c:D.p[i],scene:D.s[D.i[i]]})),scenes:new Set(ids.map(i=>D.i[i])).size,uniqShare:all.length?Math.round(100*new Set(all).size/all.length):0,cls:p.cls};};
  return W;}
function makeRun(W,S,seed){
  let sd=seed;const rnd=()=>{sd|=0;sd=sd+0x6D2B79F5|0;let t=Math.imul(sd^sd>>>15,1|sd);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};const ri=n=>Math.floor(rnd()*n);
  const R={pop:[],fit:[],pastes:0};
  R.restart=()=>{R.pop=[];R.fit=[];R.pastes=0;for(let i=0;i<S.pool*S.agents;i++){const t=[W.pick(rnd())];R.pop.push(t);R.fit.push(S.pick<=1?0:W.fit(t,S));}};
  const mutate=t=>{const r=rnd()*100;
    if(r<S.add){if(t.length>=S.maxWords)return t;const i=ri(t.length+1);const u=t.slice();u.splice(i,0,W.pick(rnd()));return u;}
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
if(typeof module!=='undefined')module.exports={makeWorld,makeRun};
