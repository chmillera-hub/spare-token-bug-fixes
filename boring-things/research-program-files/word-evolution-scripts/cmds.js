// build 10000 sensible commands from action words paired only with things the action fits
const G=[
 {v:'love hug kiss hold carry comfort protect thank help greet visit call teach trust forgive welcome invite praise respect hear feed thank bless guide follow answer'.split(' '),
  s:'farmer baker mother father sister brother neighbor friend son daughter wife husband grandmother grandfather guest stranger elder family aunt uncle cousin teacher boy girl'.split(' '),p:'farmers bakers parents neighbors friends guests elders sisters brothers'.split(' ')},
 {v:'open close lock fix paint clean hold'.split(' '),s:'door window gate box lid drawer bag book jar'.split(' '),p:'doors windows boxes bags jars'.split(' ')},
 {v:'wash dry clean wipe'.split(' '),s:'face cup plate bowl spoon floor table window car dog pot pan'.split(' '),p:'hands feet dishes clothes cups plates bowls spoons'.split(' ')},
 {v:['pick up','put down','bring','carry','take','hold','pass','find','move','lift','fetch','hand me'],s:'cup book ball toy spoon bag box bowl plate coat hat basket blanket pillow chair lamp bottle letter pen key'.split(' '),p:'shoes keys toys books cups bags boxes'.split(' ')},
 {v:'eat cook share taste cut serve bring buy warm'.split(' '),s:'bread apple egg soup rice fish meal fruit cheese cake pie'.split(' '),p:'beans eggs apples carrots'.split(' ')},
 {v:'drink pour boil bring share warm'.split(' '),s:'water milk tea juice coffee soup'.split(' '),p:[]},
 {v:['water','plant','pick','smell','grow','tend','weed'],s:'tree garden rose flower herb'.split(' '),p:'flowers seeds tomatoes beans roses herbs trees'.split(' ')},
 {v:['feed','walk','pet','brush','wash','call','water'],s:'dog cat horse cow goat rabbit bird pony lamb'.split(' '),p:'dogs cats horses cows sheep hens goats rabbits birds'.split(' ')},
 {v:['read','write','tell','share','hear','sing','learn','finish'],s:'book story letter poem song word lesson name note prayer'.split(' '),p:'books stories letters songs words'.split(' ')},
 {v:['light','watch','tend','build'],s:'fire candle lamp'.split(' '),p:'candles lamps'.split(' ')},
 {v:['make','fold','change','warm','shake out'],s:'bed blanket sheet towel'.split(' '),p:'beds blankets sheets towels'.split(' ')},
 {v:['sweep','mop','scrub','tidy'],s:'floor room kitchen porch yard house'.split(' '),p:'floors rooms stairs'.split(' ')}
];
const base=[],seen=new Set();const META=new Map();let gi=-1;
function add(c,arr){if(!seen.has(c)){seen.add(c);arr.push(c);}}
G.forEach((g,gidx)=>{for(const v of g.v){
 g.s.forEach((n,ni)=>{['the','your','my','our','this','that'].forEach((d,di)=>{const c=v+' '+d+' '+n;if(!META.has(c))META.set(c,{g:gidx,v:v,n:n,ni:ni,di:di});add(c,base);});});
 g.p.forEach((n,ni)=>{['the','your','my','our','these','those'].forEach((d,di)=>{const c=v+' '+d+' '+n;if(!META.has(c))META.set(c,{g:gidx,v:v,n:n,ni:100+ni,di:di});add(c,base);});});
}});
// deterministic shuffle so the 10000 mix plain commands and commands with one extra word
let sd=42;function r(){sd=(sd*1103515245+12345)&0x7fffffff;return sd/0x7fffffff;}
const ext=[];const tails=[' now',' today',' again',' gently',' slowly',' with care',' every day',' together'];
for(const c of base){const m=META.get(c);const e='please '+c;ext.push(e);if(!META.has(e))META.set(e,m);for(const t of tails){ext.push(c+t);if(!META.has(c+t))META.set(c+t,m);}}
for(let i=ext.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[ext[i],ext[j]]=[ext[j],ext[i]];}
for(let i=base.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[base[i],base[j]]=[base[j],base[i]];}
const CMDS=base.slice(0,8500);for(const c of ext){if(CMDS.length>=10000)break;if(!seen.has(c)){seen.add(c);CMDS.push(c);}}
// story of one day: each command gets a scene and a place inside the scene
const SCENES=['waking up','washing','caring for the animals','morning drinks','caring for people','working in the garden','cleaning the house','fetching things','making and eating the meal','evening by the fire with stories','closing the house for the night'];
const BODY=new Set(['face','hands','feet']);
const ORDER={0:'greet welcome call visit invite hear answer hug kiss hold carry feed comfort help guide teach protect follow trust respect praise thank forgive bless love'.split(' '),
 3:['find','fetch','pick up','lift','take','hold','carry','bring','hand me','pass','move','put down'],4:'buy bring cut cook warm serve share taste eat'.split(' '),5:'bring boil warm pour share drink'.split(' '),
 6:['plant','water','weed','tend','grow','pick','smell'],7:['call','feed','water','walk','brush','wash','pet'],8:['learn','read','write','finish','tell','share','hear','sing'],9:['build','light','tend','watch'],11:['tidy','sweep','mop','scrub']};
function scene(m){
  if(m.g===10)return (m.v==='fold'||m.v==='warm')?10:0;
  if(m.g===1)return m.v==='open'?0:((m.v==='close'||m.v==='lock'||m.v==='hold')?10:6);
  if(m.g===2)return BODY.has(m.n)?1:6;
  return {7:2,5:3,0:4,6:5,11:6,3:7,4:8,9:9,8:9}[m.g];
}
function key(c){const m=META.get(c);const sc=scene(m);const o=ORDER[m.g];const vi=o?Math.max(0,o.indexOf(m.v)):0;return [sc,m.g,vi,m.ni,m.di,c.length];}
const sorted=CMDS.slice().sort((a,b)=>{const x=key(a),y=key(b);for(let i=0;i<x.length;i++)if(x[i]!==y[i])return x[i]-y[i];return a<b?-1:1;});
const RANK=new Map();sorted.forEach((c,i)=>RANK.set(c,i));
const sceneOf=c=>scene(META.get(c));
module.exports={CMDS,baseCount:base.length,RANK,SCENES,sceneOf,STORY:sorted};
if(require.main===module){console.log('base',base.length,'total',CMDS.length);for(let i=0;i<12;i++)console.log(' ',CMDS[Math.floor(r()*CMDS.length)]);}
