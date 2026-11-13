#!/bin/bash
# Runs the many-commands reader under four settings with five starting points each (20 runs and four at a time).
# plain = no bonus; story = bonus for closeness in the story; fresh = bonus for words that are not repeats; both = both bonuses.
cd "$(dirname "$0")"
job() { # setting seed
  case $1 in plain) B=0;U=0;; story) B=1;U=0;; fresh) B=0;U=0.4;; both) B=1;U=0.4;; esac
  BONUS=$B UNIQ=$U node many_commands_story_order.js A $2 > out_$1_$2.txt 2>&1
}
export -f job
for s in 31 32 33 34 35; do for c in plain story fresh both; do echo "$c $s"; done; done | xargs -P 4 -L 1 bash -c 'job $0 $1'
echo ALLDONE > done.txt
