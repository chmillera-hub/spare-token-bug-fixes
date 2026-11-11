const fs=require('fs');const {makeWorld,makeRun}=require('./word_level_engine.js');
const sets={'Claude selection (41 passages)':'bible_phrases.json','Charles selection (13 whole books)':'sel13.json','Words of Jesus (red letters)':'red.json'};
const total=+process.argv[2]||600000;
for(const [name,f] of Object.entries(sets)){
  const W=makeWorld(JSON.parse(fs.readFileSync(f,'utf8')));const S={agents:10,pool:60,pick:3,add:30,swap:10,change:10,uniq:0.2,near:0,junk:0.02,maxWords:60};
  const R=makeRun(W,S,11);R.restart();const t0=Date.now();while(R.pastes<total)R.step();
  console.log(`\n=== ${name}: ${W.N} quotes, ${W.words.length} different words | ${total} pastes = ${R.minutes().toFixed(0)} min of experiment time | ${Math.round(total/((Date.now()-t0)/1000))} pastes per second`);
  const cnt=new Map();let nq=0,nw=0;
  for(let a=0;a<S.agents;a++){const t=R.pop[R.agentBest(a)];const inf=W.info(t);nq+=inf.n;
    for(const o of inf.story)for(const w of o.c.split(' ')){cnt.set(w,(cnt.get(w)||0)+1);nw++;}
    if(a<4)console.log(`Agent ${a+1} (${inf.n} quotes, ${inf.scenes} passages): `+inf.story.map(o=>o.c).join(' / '));}
  const share=(m,tot,ws)=>Math.round(100*ws.reduce((x,w)=>x+(m.get(w)||0),0)/tot);
  const src=new Map();let sw=0;for(const q of W.D.p)for(const w of q.split(' ')){src.set(w,(src.get(w)||0)+1);sw++;}
  const G={'you/your':['you','your','yours','yourselves'],'i/me/my':['i','me','my','mine'],'he/him/they/them':['he','him','his','they','them','their'],'father':['father'],'love':['love','loved','loves'],'will/shall':['will','shall'],'dont/not/no':['dont','not','no','neither','nor'],'yahweh/god/lord':['yahweh','god','lord']};
  console.log('word shares in evolved quotes vs in the whole source list: '+Object.entries(G).map(([k,ws])=>k+' '+share(cnt,nw,ws)+'% vs '+share(src,sw,ws)+'%').join(' | '));
  const stop=new Set('and the of to in a is that for it with as be on not this but by from or an at are was were his her their they them he him you your i me my we our us who which what will shall have has had do does did so if all no nor then there when one out up into dont also may can let more than those these its am been being about over after before because'.split(' '));
  console.log('most used content words:',[...cnt.entries()].filter(e=>!stop.has(e[0])).sort((a,b)=>b[1]-a[1]).slice(0,22).map(e=>e[0]+' '+e[1]).join(', '));
  console.log('average quotes per agent',(nq/S.agents).toFixed(1),'| most used words in the quotes of all 10 agents:',[...cnt.entries()].sort((a,b)=>b[1]-a[1]).slice(0,25).map(e=>e[0]+' '+e[1]).join(', '));
}
