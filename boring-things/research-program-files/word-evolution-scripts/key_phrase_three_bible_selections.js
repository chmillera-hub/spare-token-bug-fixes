const fs=require('fs');const {makeWorldP,makeRunP}=require('./pengine.js');
const GENERIC='and because so then when but for while if with from in on to of the a those these them they he him his you your here there who that this others all not'.split(' ');
const SPECIAL={mine:'god yahweh love earth father time day heaven man light son heart made give know tell saw see keep heard called seek put make good evil blessed right great holy wicked righteous secret perfect living new'.split(' '),charles:'yahweh god man jesus son people lord day king house land heart says know tell give see say made make take heard hear answered good evil great wicked righteous holy high right wise blessed dead poor'.split(' '),red:'father man son god kingdom lord heaven world house life day earth love seed jesus christ yahweh tell see know give sent say hear take believe enter receive made good evil little great blessed greater dead eternal last righteous right full'.split(' ')};
const sets={'Claude selection (41 passages)':'ph_mine.json','Charles selection (10 whole books)':'ph_charles.json','Words of Jesus (four gospels)':'ph_red.json'};
const total=+process.argv[2]||6000000,seed=+process.argv[3]||11;
for(const [name,f] of Object.entries(sets)){
  const W=makeWorldP(JSON.parse(fs.readFileSync(f,'utf8')),GENERIC.concat(SPECIAL[name]));const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,pair:1,same:0.15,uniq:0.05,junk:0.05,dup:0.5,maxPhrases:32,bridge:20,join:0.2};
  const R=makeRunP(W,S,seed);R.restart();const t0=Date.now();while(R.pastes<total)R.step();
  console.log(`\n=== ${name}: ${W.N} different key phrases | ${total} pastes = ${R.minutes().toFixed(0)} min of experiment time | ${Math.round(total/((Date.now()-t0)/1000))} pastes per second`);
  let longest=0,sum=0;
  for(let a=0;a<S.agents;a++){const t=R.pop[R.agentBest(a)];const runs=W.runs(t);const mx=runs.reduce((m,r)=>Math.max(m,r.n),0);longest=Math.max(longest,mx);sum+=runs.reduce((m,r)=>m+r.n,0);
    if(a<2)console.log(`Agent ${a+1} (${t.length} pieces, ${runs.length} rebuilt stretches):\n   `+W.text(t));}
  console.log('longest rebuilt stretch in phrases',longest,'| average phrases inside rebuilt stretches per agent',(sum/S.agents).toFixed(1));
}
