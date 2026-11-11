// build 10000 sensible commands from action words paired only with things the action fits
const G=[
 {v:'love hug kiss hold carry comfort protect thank help greet visit call teach trust forgive welcome invite praise respect hear feed thank bless guide follow answer'.split(' '),
  s:'baby child mother father sister brother neighbor friend son daughter wife husband grandmother grandfather guest stranger elder family aunt uncle cousin teacher boy girl'.split(' '),p:'children kids parents neighbors friends guests elders sisters brothers'.split(' ')},
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
const base=[],seen=new Set();
function add(c,arr){if(!seen.has(c)){seen.add(c);arr.push(c);}}
for(const g of G)for(const v of g.v){
 for(const n of g.s)for(const d of ['the','your','my','our','this','that'])add(v+' '+d+' '+n,base);
 for(const n of g.p)for(const d of ['the','your','my','our','these','those'])add(v+' '+d+' '+n,base);
}
// deterministic shuffle so the 10000 mix plain commands and commands with one extra word
let sd=42;function r(){sd=(sd*1103515245+12345)&0x7fffffff;return sd/0x7fffffff;}
const ext=[];const tails=[' now',' today',' again',' gently',' slowly',' with care',' every day',' together'];
for(const c of base){ext.push('please '+c);for(const t of tails)ext.push(c+t);}
for(let i=ext.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[ext[i],ext[j]]=[ext[j],ext[i]];}
for(let i=base.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[base[i],base[j]]=[base[j],base[i]];}
const CMDS=base.slice(0,8500);for(const c of ext){if(CMDS.length>=10000)break;if(!seen.has(c)){seen.add(c);CMDS.push(c);}}
module.exports={CMDS,baseCount:base.length};
if(require.main===module){console.log('base',base.length,'total',CMDS.length);for(let i=0;i<12;i++)console.log(' ',CMDS[Math.floor(r()*CMDS.length)]);}
