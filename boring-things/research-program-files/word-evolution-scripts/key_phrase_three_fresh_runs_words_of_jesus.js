const fs=require('fs');const {makeWorldP,makeRunP}=require('./pengine.js');
const W=makeWorldP(JSON.parse(fs.readFileSync('ph_red.json','utf8')),['and']);
for(const seed of [101,202,303]){const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,pair:1,same:0.15,uniq:0.05,junk:0.05,dup:0.5,maxPhrases:22,bridge:0,join:0.2};
  const R=makeRunP(W,S,seed);R.restart();while(R.pastes<5000000)R.step();
  for(let a=0;a<2;a++){const t=R.pop[R.agentBest(a)];let out='';for(let i=0;i<t.length;i++){const linked=i>0&&W.scan([t[i-1],t[i]]).np>0;out+=(i?(linked?' ':' | '):'')+W.u[t[i]];}
  console.log('seed '+seed+' agent '+(a+1)+': '+out+'\n');}}
