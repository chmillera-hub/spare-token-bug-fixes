// Rerun of the closeness reader with ten new starting points (written 12 November 2026 by an AI chatbot).
// The engine is near.js unchanged. The earlier page used starting points 5 and 6. This file uses 11 to 20.
// Run with: node closeness_rerun.js
const {run}=require('./near.js');
for(let sd=11;sd<=20;sd++) run('closeness reader no forcing',{pick:3,force:0,marks:[300000]},300000,sd);
