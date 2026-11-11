const fs=require('fs');const {makeWorldP,makeRunP}=require('./key_phrase_engine.js');
const sets={'Claude selection (41 passages)':'ph_mine.json','Charles selection (10 whole books)':'ph_charles.json','Words of Jesus (four gospels)':'ph_red.json'};
const total=+process.argv[2]||6000000,seed=+process.argv[3]||11;
for(const [name,f] of Object.entries(sets)){
  const W=makeWorldP(JSON.parse(fs.readFileSync(f,'utf8')));const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,pair:1,same:0.15,uniq:0.05,junk:0.05,dup:0.5,maxPhrases:24};
  const R=makeRunP(W,S,seed);R.restart();const t0=Date.now();while(R.pastes<total)R.step();
  console.log(`\n=== ${name}: ${W.N} different key phrases | ${total} pastes = ${R.minutes().toFixed(0)} min of experiment time | ${Math.round(total/((Date.now()-t0)/1000))} pastes per second`);
  let longest=0,sum=0;
  for(let a=0;a<S.agents;a++){const t=R.pop[R.agentBest(a)];const runs=W.runs(t);const mx=runs.reduce((m,r)=>Math.max(m,r.n),0);longest=Math.max(longest,mx);sum+=runs.reduce((m,r)=>m+r.n,0);
    if(a<4)console.log(`Agent ${a+1} (${t.length} phrases, ${runs.length} rebuilt stretches):\n   `+runs.map(r=>'['+r.scene+'] '+r.text).join('\n   '));}
  console.log('longest rebuilt stretch in phrases',longest,'| average phrases inside rebuilt stretches per agent',(sum/S.agents).toFixed(1));
}
