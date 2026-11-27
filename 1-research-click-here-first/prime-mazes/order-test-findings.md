# Five follow up tests on the door walks: shuffled order and Fibonacci cousins and prime door counts and wider loops and hat tiles that never block

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026. The author of this repository asked whether anything stood out in the door walk experiments and the chatbot named five tests the chatbot wanted to run. The author said to run the tests and upload the results. So the choice of tests on this page is the chatbot's choice and the experiments rest on rules the author set on the earlier pages in this folder. The numbers are measurements from the programs in the folder boring-things/research-program-files/prime-mazes-scripts/shape-grid-scripts. The facts about last digits and about primes are standard mathematics and the page claims no new result. No other person has reviewed the page yet.

## The setup in brief

A walk starts in one room. Each number picks a door. A new room appears when the space behind the door is empty and the walk steps into the old room when a room is already there. On ten sided rooms the door is the last digit of the number. The score is the number of rooms placed plus the longest walk that never enters a room twice. The page [ten-sided-ranking.md](ten-sided-ranking.md) has the full rules and a ranking of 32 sequences.

## Test 1: does the order of the numbers matter or only how often each door is picked?

Each of the 32 sequences ran once in true order with 3600 numbers and then 10 times with the same numbers shuffled. Shuffling keeps how often each door is picked and destroys the order. A true score far from the shuffled scores means the order carries structure.

A gauge for luck: one run of random digits scored 2222 while shuffled copies of the same digits averaged 2808 with a spread of 198. So a gap of about 3 spreads can happen by luck alone and the page treats only larger gaps as a finding.

**Sequences where the true order scores far above the shuffled order on ten sided rooms**

- Digits of the primes written in one row: 5447 against 3959 shuffled which is 14.5 spreads above. The cause is the first digit that stays the same for long stretches.
- Running totals of the primes: 4401 against 2680 shuffled which is 8.0 spreads above.
- Collatz step counts: 4441 against 2655 shuffled which is 7.4 spreads above. The cause is the runs of neighbors with equal step counts.
- x squared minus x plus 1 and x squared plus x plus 41: about 9360 against about 7190 shuffled because the true order never steps back.

**Sequences where the order makes no measurable difference**

- Whole primes: 5943 against 6016 shuffled which is 0.2 spreads below. The ribbon of the primes on ten sided rooms comes from which last digits primes have and not from the order of the primes.
- Divisor counts: 6296 against 6214 shuffled.
- Digits of the golden ratio: 3089 against 3045 shuffled.
- Digits of pi and e and the square root of 2 and the prime gaps and the partition numbers all sit within 2 spreads of their shuffled scores.

**Sequences where the true order scores far below the shuffled order**

- Every closed loop: the counting numbers (26 against 2818 shuffled) and the square numbers (16 against 2952) and the Fibonacci numbers (97 against 2879) and five more. The same doors in shuffled order wander like random digits. So a freeze is caused by the order and not by which doors are used.
- The Recaman sequence (806 against 2682) and the whole part of n times the natural logarithm of n (641 against 2664). Both keep walking back over old rooms because neighbors in these sequences have related last digits.
- 2 times x squared minus 1 (5043 against 5991) because the ladder spends two of every five numbers on returns.

## Test 2: is the closed loop of the Fibonacci numbers on ten sided rooms luck?

Partly. A cousin of the Fibonacci numbers starts from a different pair of numbers and follows the same adding rule. The last digits of a cousin depend only on the starting pair of last digits so there are 100 starting pairs. The pairs fall into 6 cycles.

- The cycle of 60 last digits (the Fibonacci numbers and 59 other pairs) closes: one lap moves the walk 0 rooms right and 0 rooms down.
- The cycle of 20 last digits (pairs such as 0 then 2) also closes.
- The cycle of 12 last digits drifts 1 room up for each lap. This cycle holds the Lucas numbers 1 then 3 then 4 then 7 then 11.
- The cycle of 4 last digits drifts 1 room down for each lap and the cycle of 3 drifts 1 room down and the pair 0 then 0 goes straight up.
- So 80 of the 100 starting pairs make a closed loop on ten sided rooms.

The sideways part has a reason. The last digit of a Fibonacci number 30 places later is 10 minus the last digit now. Door d and door 10 minus d always cancel sideways on a ten sided room: door 1 goes up and right and door 9 goes up and left. So the sideways move is zero for every one of the six cycles.

The up and down part has no such reason that the chatbot could find. The pairs of doors leave moves of 2 up or 1 up or 1 down or 2 down and for the cycle of 60 these happen to add to zero. For the cycle of 12 the same sum leaves 1 room.

On eight sided rooms none of the 8 cycles close. Every starting pair drifts.

## Test 3: what do the primes do in a room with a prime number of doors?

No flat grid has rooms with 7 or 11 neighbors each. So this test is a free walk: the doors are spread evenly around a circle with door 0 pointing up and each prime moves the walk one unit toward the door for its remainder.

A prime larger than 7 never leaves remainder 0 when divided by 7. So door 0 is the one forbidden door and the other 6 doors are used about equally. The 7 directions cancel as a full set so the 6 used directions add up to a push straight away from door 0. The prediction is a march straight down by one sixth of a unit for each prime.

- 7 doors and the first 100000 primes: the door counts run from 16630 to 16685. The walk ended 16628.8 units down (predicted 16666.7) and 5.8 units left.
- 11 doors and the first 100000 primes: the walk ended 10049.1 units down (predicted 10000.0) and 18.5 units right.
- 13 doors and the first 100000 primes: the walk ended 8362.5 units down (predicted 8333.3) and 168.3 units left.

The march is far straighter than random picks from the same doors would give. Random picks from doors 1 to 6 spread about 251 units sideways after 100000 steps and the primes with 7 doors ended 5.8 units off. The reason is that two primes in a row share a remainder much less often than an even split would give: 7.78% of the time with 7 doors where an even split gives 16.67% and 3.14% with 11 doors where an even split gives 10.00% and 1.67% with 13 doors where an even split gives 8.33%. This avoidance is a known effect and the page only measures the effect.

## Test 4: do the primes with 5 digits trace a loop about 8 times wider?

Yes. The page [shape-grids-findings.md](shape-grids-findings.md) predicted a loop about 8 times wider for the digits of the primes with 5 digits because there are 8363 such primes against 1061 primes with 4 digits. This run read all 46534 digits of the primes below 100000.

- Primes with 2 digits: the loop is 13 rooms wide and 9 rooms tall.
- Primes with 3 digits: 73 rooms wide and 56 rooms tall.
- Primes with 4 digits: 555 rooms wide and 389 rooms tall.
- Primes with 5 digits: 4351 rooms wide and 2964 rooms tall.
- The loop for 5 digits is 7.84 times as wide and 7.62 times as tall as the loop for 4 digits.

The drift for each prime with 5 digits matches the earlier prediction closely: 1.03 right and 1.25 up for first digit 1 (predicted 1.00 and 1.25) and 0.97 right and 0.75 down for first digit 4 (predicted 1.00 and 0.75) and 0.99 left and 1.28 up for first digit 9 (predicted 1.00 and 1.25).

No loop closes. The end of the loop for 5 digits sits 436 rooms right and 1404 rooms above the start of that loop because more primes start with a low digit than with a high digit and because the last digit adds a steady upward push.

The picture [loops-of-prime-digits.png](loops-of-prime-digits.png) shows the three loops: red for 3 digits and blue for 4 digits and green for 5 digits. Each loop has a small knot where the first digit changes.

## Test 5: does any sequence grow hat tiles with no blocked step?

A blocked step is a number that picks a door where no hat fits without overlap. Six of the 32 sequences had zero blocked steps in 3600 numbers.

- Doubling numbers placed 3301 hats and scored 6302.
- Tripling numbers placed 3001 hats and scored 5402.
- Factorials placed 3598 hats and scored 7195 because every factorial from the 14th onward picks door 0.
- x squared plus 1 and x to the power 4 and x to the power 5 also had zero blocked steps and these three freeze into loops of 10 and 8 and 13 hats.

Most sequences block often: random numbers block about 700 times in 3600 numbers and the square numbers block 1021 times.

## How does this connect to food and shelter and deep human connection?

None of these counts feeds or houses a person. The tie is the habit behind the page: one person looked at pictures and said what stood out and asked what else might be worth checking and every result went into public view for free. A reader who has the same questions can skip the cost of redoing the work and put those hours toward a meal or a home or toward learning what is in another person's heart and mind.

## What was not checked

- No other person has rerun the programs.
- Each shuffled average uses 10 shuffles so each spread is a rough figure.
- The longest walk in each score is a lower bound on pictures with many loops.
- The free walk with 7 or 11 or 13 doors is not a grid of rooms so rooms and scores do not apply to that test.
- The chatbot did not find out why the doubling numbers never block on hat tiles.
