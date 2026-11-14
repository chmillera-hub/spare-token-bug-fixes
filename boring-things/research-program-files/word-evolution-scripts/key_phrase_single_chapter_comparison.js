const fs=require('fs');const {makeWorldP,makeRunP}=require('./pengine.js');
const GENERIC='and because so then when but for while if with from in on to of the a those these them they he him his you your here there who that this others all not'.split(' ');
for(const f of ['ph_john10.json','ph_psalm88.json']){
  const W=makeWorldP(JSON.parse(fs.readFileSync(f,'utf8')),GENERIC);const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,pair:1,same:0.15,uniq:0.05,junk:0.05,dup:0.5,maxPhrases:32,bridge:20,join:0.2};
  const R=makeRunP(W,S,5);R.restart();
  for(const stop of [20000,200000,3000000]){while(R.pastes<stop)R.step();
    let longest=0,sum=0;for(let a=0;a<S.agents;a++){const t=R.pop[R.agentBest(a)];const runs=W.runs(t);longest=Math.max(longest,runs.reduce((m,r)=>Math.max(m,r.n),0));sum+=runs.reduce((m,r)=>m+r.n,0);}
    console.log(`\n=== ${f} ${W.N} phrases | ${stop} pastes | longest ${longest} | avg rebuilt ${(sum/S.agents).toFixed(1)}`);
    for(let a=0;a<2;a++){const t=R.pop[R.agentBest(a)];console.log(`Agent ${a+1} (${t.length} pieces, ${W.runs(t).length} stretches): `+W.text(t));}}
}
