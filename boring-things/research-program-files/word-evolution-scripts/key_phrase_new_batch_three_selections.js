const fs=require('fs');const {makeWorldP,makeRunP}=require('./pengine.js');
for(const [f,seed] of [['ph_mine.json',411],['ph_charles.json',412],['ph_red.json',413]]){
  const W=makeWorldP(JSON.parse(fs.readFileSync(f,'utf8')),['and']);const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,pair:1,same:0.15,uniq:0.05,junk:0.05,dup:0.5,maxPhrases:22,bridge:0,join:0.2};
  const R=makeRunP(W,S,seed);R.restart();while(R.pastes<5000000)R.step();console.log('=== '+f);
  for(let a=0;a<3;a++){const t=R.pop[R.agentBest(a)];let out='';for(let i=0;i<t.length;i++){const linked=i>0&&W.scan([t[i-1],t[i]]).np>0;out+=(i?(linked?' ':' | '):'')+W.u[t[i]];}
  console.log('agent '+(a+1)+': '+out+'\n');}}
