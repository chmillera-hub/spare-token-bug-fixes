# Questions about spinning arrows and circles cut into sections

> **About this page:** One AI model (Claude) wrote this page on 23 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the eleven earlier question pages in this folder (the last one is [sky-questions.md](sky-questions.md)). The author proposed each test on this page: putting a sum on a circle so the sum spins and cutting a circle into sections and asking which sections a sum ever reaches. The underlying facts are standard mathematics so the page claims no new result. The counts for circles with up to 5000 sections are measurements from programs and the page marks which statements are proven and which are only measured. The programs are in the folder boring-things/research-program-files/prime-richness-scripts/spin-scripts. No other person has reviewed the page yet.

## The picture the page uses

An arrow has a length and a direction. A sum of sizes can only pile up along a line. A sum of arrows can cancel because arrows can point in different directions. "Putting a number next to pi" on this page means using the number as an angle: the number sets how far an arrow is turned.

## Question: what happens to 1 + 4 + 9 + 16 + … when the squares are used as turns?

Each term becomes an arrow of length 1 turned by an angle set by the square. The plain sum runs off to infinity and a sum of arrows of length 1 cannot run off that way.

- With a turn of pi times each square the arrows point right and left and right and left so the sum reads 1 − 1 + 1 − 1 and never settles.
- Split a full turn into N equal steps and turn the arrow for each n by n squared steps (n from 0 to N − 1). For N = 5 the arrows add up to 2.2361 = the root of 5 pointing right. For N = 7 the total is 2.6458 = the root of 7 pointing straight up. For N = 11 the total is the root of 11 pointing up. For N = 13 and N = 17 the totals are the roots of 13 and 17 pointing right.

So N arrows of length 1 combine to a length of exactly the root of N (proven for odd N). A prime that leaves a remainder of 1 when divided by 4 gives a total pointing right and a remainder of 3 gives a total pointing up.

For a turn that is not a tidy fraction (the root of 2 of a full turn per unit) the running total wanders: 7.6 from the start after 100 arrows and 98.6 after 10000 and 853 after one million against square roots of 10 and 100 and 1000.

## Question: what about the reciprocal version such as 1 over e to the power 4 pi?

The sum 1/e^pi + 1/e^(4 pi) + 1/e^(9 pi) + … settles at 0.0432174 because the terms are 0.0432 and 0.0000035 and then smaller than a trillionth.

Count the squares on both sides of zero and include zero and put a strength t beside the pi. Call the result the glow at strength t.

- The glow at strength 4 is 1.000007 and the glow at strength 1/4 is 2.000014 which is 2 times as much.
- The glow at strength 9 is 1.000000000001 and the glow at strength 1/9 is 3.000000000003 which is 3 times as much.
- The glow at strength 2 is 1.003735 and the glow at strength 1/2 is 1.419495 which is the root of 2 times as much.

Flipping the strength t to 1 over t multiplies the glow by exactly the root of t. That flip rule is proven and the mirror rule that pairs the zeta dial setting s with 1 − s is derived from the flip rule. The square root in the flip is where the center of the mirror at 1/2 originates.

## Question: how does spinning keep a sum from reaching infinity?

The spinning does not shrink any term. The spinning makes the terms point in different directions so the terms cancel and what is left is the net imbalance.

- **Steady spinning traps the total.** Arrows of length 1 with a quarter turn each visit four spots and return to the start forever. A turn of 10 degrees per arrow traps the total on a circle of radius 5.7.
- **The zeta row.** At the dial setting 1 with no spin the row 1 + 1/2 + 1/3 + … goes to infinity. With a pitch of 10 the running total circles a fixed spot at a distance of 0.100 (measured at 10 and 100 and 1000 and 10000 and 100000 terms). The center has a length of 1.39 and is the value of the zeta function there. The radius is 1 divided by the pitch.

Spinning does not always cage the total. If the arrows keep growing the swings grow (1 − 2 + 3 − 4 + … has running totals 1 and −1 and 2 and −2). If the turns are scrambled the total wanders at a square root pace. If every turn is a whole number of full turns nothing cancels.

Even a swinging row has a center. The row 1 − 2 + 3 − 4 + … faded with a gentle dimmer settles at 0.2494 and then 0.24999 and then 0.2499999 so the center is 1/4. Multiplying 1 + 2 + 3 + 4 + … by 4 and subtracting from the row itself leaves 1 − 2 + 3 − 4 + … so minus 3 times the leftover constant of 1 + 2 + 3 + … equals 1/4 which gives −1/12.

Spinning has three outcomes. Partial cancelling leaves a finite center. Perfect cancelling leaves nothing which is a zero. No cancelling gives a blow-up.

## Question: does spinning help find primes? (Two tests.)

**Test 1: spin the primes and look for the pitches.** Each prime up to one million became an arrow of length (natural logarithm of the prime) divided by (root of the prime) with a gentle fade. The angle was the pitch times the natural logarithm of the prime. The pitch ran from 8 to 52.

- The ten deepest dips of the left-right total sat at 14.13 and 21.02 and 25.02 and 30.43 and 32.94 and 37.57 and 40.91 and 43.31 and 48.03 and 49.78.
- The first ten true pitches of the zeta zeros are 14.13 and 21.02 and 25.01 and 30.42 and 32.94 and 37.59 and 40.92 and 43.33 and 48.01 and 49.77.
- At the pitches the total sat between −3.5 and −4.6. Away from a pitch the total sat between about 0.1 and 1.1.

A first try with the primes cut off dead at one million failed. That try showed false dips every 0.455 which is 2 × pi divided by the natural logarithm of one million. The abrupt edge made its own ripple.

**Test 2: spin the pitches and look for the primes.** Each of the first 100 pitches became an arrow of length 1 with an angle of the pitch times the natural logarithm of x. The total (sign flipped) was read as x ran from 1.5 to 60.

- At the primes 2 and 3 and 5 and 7 and 11 and 13 and 17 and 19 and 23 the total stood at 17.4 and 23.2 and 26.5 and 26.2 and 26.1 and 26.7 and 26.2 and 24.5 and 22.4.
- At the composite numbers 6 and 10 and 12 and 14 and 15 and 18 and 20 and 21 and 22 the total stood between −4.8 and 0.7.
- At 4 and 9 and 25 the total stood at 11.8 and 12.5 and 10.1 (about half a prime). At 8 and 27 the total stood at 8.2 and 4.0.

Past about 40 the peaks drift (40.95 and 42.95 and 47.1 and 52.95 for the primes 41 and 43 and 47 and 53) because one hundred pitches resolve only so finely.

The spiral is an exact translation between the primes and the pitches and not a shortcut. Finding primes that way needs the pitches first and a plain sieve is much faster.

## Question: does the −1/12 show up when 1 + 2 + 3 + 4 is run through e and pi?

In three places.

1. The sum 1/e^pi + 2/e^(2 pi) + 3/e^(3 pi) + … settles at 0.047206. The total breaks into pieces: 1 over pi squared = 0.101321 and then −1/12 (running total 0.017988) and then pi squared over 240 (running total 0.059111) and then pieces that bring the running total to 0.043005 and 0.048569.
2. The sum of n divided by (e to the power 2 pi n minus 1) equals exactly 1/24 minus 1 over (8 × pi). Both sides are 0.0018779309. The 1/24 is half of 1/12 with the sign flipped. The formula is proven.
3. Give each term of 1 + 2 + 3 + … a fixed turn. For a turn of 10 degrees the center of the swinging is −32.9115. The blow-up part is −1 over the turn squared = −32.8281. The leftover is −0.0835. For a turn of 5 degrees the leftover is −0.08337 and for 1 degree −0.083335. The leftover closes in on −1/12.

The −1/12 survives every version because the −1/12 belongs to the row 1 + 2 + 3 + … and not to the method used to tame the row.

## Question: one arrow is turned a full turn and then half a turn more and then a third of a turn more. Where does the arrow end up?

The total turning after n steps is 1 + 1/2 + … + 1/n full turns. The arrow points at 0 degrees after 1 step and 180 after 2 and 300 after 3 and 30 after 4 and then 102 and 162 and 213 and 258 and 298 and 334 and then 7 degrees after 11 steps.

- The arrow circles forever and each lap takes e times as many steps. Laps finish at steps 4 and 11 and 31 and 83 and 227 and 616 and 1674 and 4550 and 12367 and 33617 and 91380. The ratios run 2.75 and 2.82 and 2.68 and 2.73 and 2.714 and then 2.718.
- After the first step the arrow never lands exactly on the start again because 1 + 1/2 + … + 1/n is never a whole number after n = 1 (proven).
- The arrow lingers late in each lap. In the lap from step 4550 to step 12367 the first tenth of the circle held 478 steps and the last tenth held 1177 which is a ratio of 2.46 = e to the power 0.9.
- After n steps the arrow has turned by the natural logarithm of n plus 0.5772 turns so the gap constant is a head start of about 208 degrees.

A second reading: each term is its own arrow of length 1/n tilted at one n-th of a turn and the arrows are laid tip to tail. The left-right total grows like the natural logarithm (running 1.6178 behind the logarithm) and the up-down total settles at 1.7897. The later arrows barely tilt so the spinning tames only the up-down part.

## Question: what if the moves are 1 pi and then 2 pi and then 3 pi?

A turn of pi is half a circle so the arrow can point only right or left. The running totals 1 and 3 and 6 and 10 and 15 and 21 and 28 and 36 are odd and odd and even and even so the arrow points left and left and right and right over and over.

With a full circle split into N stops and moves of 1 stop and then 2 and then 3:

- With 4 stops the arrow visits 1 and 3 and 2 and 2 and 3 and 1 and 0 and 0 and reaches all 4.
- With 5 stops the arrow reaches only 0 and 1 and 3.
- With 7 stops and with 9 stops the arrow reaches only 0 and 1 and 3 and 6.
- With 8 stops and 16 and 32 the arrow reaches every stop.
- With 10 stops the arrow reaches 6.

The arrow reaches every stop exactly when the number of stops is a power of 2 (proven). The pattern always repeats and each cycle reads the same forwards and backwards.

## Question: how can the numbers be converted so the arrow can land anywhere on the circle?

Pick a turning unit that is not a tidy fraction of a full circle. Three choices: the plain number as the angle (one unit is 57.3 degrees) or the golden angle of 137.5 degrees or the root of 2 of a full turn.

With the golden angle and moves of 1 and 2 and 3 units the arrow points at 137.5 and 52.5 and 105.0 and 295.1 and 262.6 and 7.7 and 250.2 and 270.3 and 67.8 and 2.9 and 75.5 and 285.6 degrees.

Over 10000 steps with the circle split into 10 slices (1000 each for a perfectly even spread) the golden angle gave 989 and 1043 and 1034 and 987 and 954 and 1001 and 1017 and 988 and 998 and 989. The plain number gave between 934 and 1067. The root of 2 gave between 974 and 1025. Even coverage is proven for every unit that is not a fraction of a full turn. The arrow never points the same way twice.

## Question: with 360 degrees and moves of 1 degree and then 2 and then 3 are there patterns?

- The arrow sits at 1 and 3 and 6 and 10 and 15 and 21 and 28 and 36 and 45 and 55 and so on. At step 26 the arrow is at 351 and step 27 carries the arrow past the start to 18.
- Only 96 of the 360 marks are ever reached. 360 is 8 × 9 × 5. All 8 remainders for the piece 8 are reached and 4 of 9 (0 and 1 and 3 and 6) and 3 of 5 (0 and 1 and 3). 8 × 4 × 3 = 96.
- The sequence repeats every 720 steps and the first 718 positions read the same forwards and backwards.
- Laps finish at steps 27 and 38 and 46 and 54 and 60 and 66 and 71.
- The arrow lands exactly on 0 at steps 80 and 144 and 224 and 495 and 575 and 639 and 719 and 720 in each cycle.
- In one cycle 16 marks get 12 visits each and 48 marks get 8 and 8 marks get 6 and 24 marks get 4.

## Question: what do other sums do on the 360 degree circle?

Each line gives the moves and the number of marks reached and the cycle.

- Odd numbers: 36 marks and a cycle of 180 steps (the arrow lands on the square numbers).
- Multiples of 3: 48 marks and a cycle of 240.
- Counting numbers: 96 marks and a cycle of 720.
- Squares: 216 marks and a cycle of 2160.
- Cubes: 18 marks and a cycle of 120.
- Fibonacci numbers: 75 marks and a cycle of 120.
- Doublings 1 and 2 and 4 and 8: 14 marks and a cycle of 12.
- The row 1 and 1 × 2 and 1 × 2 × 3 and so on: the arrow visits 1 and 3 and 9 and 33 and 153 and then stays at 153 because every later move is a whole number of full turns.
- Primes: all 360 marks with no cycle found. Over the first 100000 primes each mark got between 227 and 324 visits against 278 for an even spread.

Fractions below one behave in two ways. A row that settles brings the arrow to rest at the sum: moves of 1/2 and 1/4 and 1/8 of a degree rest at 1 degree and moves of 360 divided by each square rest at 232.2 degrees after one full lap. A row that does not settle crawls forever: with moves of 1 and 1/2 and 1/3 of a degree the arrow has turned 16.7 degrees after ten million steps and one lap would take about 10 to the power 156 steps.

## Question: how many sections should a circle have so that every section gets hit?

Every number of sections from 2 to 5000 was tested.

- **Counting moves.** Every section is hit exactly when the number of sections is a power of 2 (up to 4096 in the test). 1000 sections score 424.
- **Square moves.** Every section is hit for 57 counts up to 5000 and each one is built only from 2s and 3s. The largest are 3888 and 4096 and 4374 and 4608. 360 scores 216 and 1000 scores 600.
- **Fibonacci moves.** Every section is hit for 50 counts up to 5000: a power of 5 or a power of 5 times 2 or 4 or 6 or 7 or 14 or a power of 5 times a power of 3. The largest are 3125 and 3375 and 3645 and 3750 and 4375. 1000 scores 750.
- **Prime moves.** Every section was hit for every count from 2 to 5000 using the first 200000 primes.
- **Doubling moves.** No count above 1 reaches 100%. The best are certain primes where the arrow misses one section (4986 of 4987).
- **Odd-number moves.** The only full score is 2 sections. The best large counts sit near 50.1% at twice a prime.
- **Cube moves.** The only full score is 2 sections. The best large counts sit near 37.7%.

Each row has favorite primes: 2 for counting moves and 2 and 3 for square moves and 5 for Fibonacci moves. The rules for counting moves and for Fibonacci moves match known proven results. The rule for square moves and the prime result are measurements from the test.

## Question: does the percentage rise and fall in a pattern as the number of sections grows?

The percentage is a jagged comb. For counting moves and 1 through 30 sections the percentages are 100 and 100 and 67 and 100 and 60 and 67 and 57 and 100 and 44 and 60 and 55 and 67 and 54 and 57 and 40 and 100 and 53 and 44 and 53 and 60 and 38 and 55 and 52 and 67 and 44 and 54 and 41 and 57 and 52 and 40.

- The spikes to 100% sit at the powers of 2 so the gaps between spikes double.
- Doubling the number of sections never changes the percentage (66.7% for 3 and 6 and 12 and 12.5% for 1155 and 2310 and 4620).
- Each different odd prime in the section count cuts the percentage roughly in half: an average of 50.0% with one odd prime piece and 28.3% with two and 17.3% with three and 11.5% with four.
- A prime number of sections scores 66.7% for 3 and 60% for 5 and 57.1% for 7 and 54.5% for 11 and 50.5% for 101 and 50.0% for 4999.
- The average drifts down: 75.5 for 1 to 10 sections and 47.9 for 11 to 100 and 37.1 for 101 to 1000 and 32.3 for 1001 to 5000.
- The lowest scores are 8.2% at 4095 (3 × 3 × 5 × 7 × 13) and 8.3% at 3465.

For square moves each prime above 3 cuts the percentage to about two thirds (60% for 5 and 71.4% for 7 and 66.7% for 997) and the lowest score is 24.7% at 935.

So the wave of percentages is a picture of how each section count breaks into primes.

## Question: do the primes always hit every section?

With the first two million primes every section was hit for every circle tested from 10 sections up to 100000 sections. The chatbot knows of no proof for every circle size.

Random drops would need about N times the natural logarithm of N drops to fill N sections. The primes needed 35 for 10 sections (against 23) and 774 for 100 (against 461) and 1960 for 360 (against 2119) and 8348 for 1000 (against 6908) and 36620 for 5000 (against 42586) and 102551 for 10000 (against 92103) and 502272 for 50000 (against 540989) and 1495882 for 100000 (against 1151293).

On an evenness score where 1.0 means "as even as random drops" a circle of 360 scored 0.93 and 1000 scored 0.89 and 2310 scored 0.98. Small circles show structure: 2 sections alternate perfectly because every prime after 2 is odd and 3 sections scored 0.02 and 4 scored 0.19 and 5 scored 0.39 and 6 scored 2.04.

## Question: which sums that are not trivial hit all 360 marks?

- 1 + 61 + 121 + 181 + … (each move 60 more than the last) lands on all 360 marks in exactly 360 steps with no mark hit twice. The row 31 + 91 + 151 + … does the same.
- 1 + 16 + 31 + 46 + … (each move 15 more) reaches all 360 marks in 675 steps.
- The fourth powers 1 and 16 and 81 and 256 reach all 360 marks after 2427 steps.
- The primes reach all 360 after 1960 steps. The squares of the primes after 2200. The first members of twin prime pairs after 2421. The composite numbers after 2147.
- The digits of pi reach all 360 after 1795 steps. The digits of e after 2480. The digits of the root of 2 after 2197.
- The whole part of n times the root of 2 reaches all 360 after 2003 steps. The whole part of n times the golden ratio after 2117. The number of divisors of n after 1681.

Rows that fail: twice each odd prime reaches 180 marks. The recipe n² + n + 41 reaches 162. The powers of 7 reach 36 and the powers of 11 reach 60.

Two kinds of rows hit everything: a tidy row whose growth is tuned to 8 and 9 and 5 and a row irregular enough to act like random drops which takes about 2000 steps (360 times the natural logarithm of 360 is 2119).

## Question: does this mean primes are truly random and cannot be predicted before being discovered?

No. The primes are fixed and anyone can compute them. What the tests show is that the primes pass many tests of randomness when viewed in bulk.

**Where the primes looked random on this page.** The running total of the primes filled every circle tested at the pace random drops would. The spread across sections matched random drops for circles of moderate and large size.

**Where the primes did not look random.**

- A prime after 2 is never even so the arrow on 2 sections alternates perfectly.
- The pitches in Test 1 are sharp: the primes carry a chord of exact tones which a random list would not.
- The last digits of neighboring primes avoid repeating. Over two million primes a prime ending in 1 was followed by a prime ending in 1 only 17.4% of the time and a prime ending in 9 was followed by a prime ending in 1 33.5% of the time. A fair draw would give 25% for each.

**What "predict" can mean.**

- Testing whether a given number is prime is fast even for numbers with thousands of digits and a fast method is proven to exist.
- Finding the next prime after a given number is also fast because only about "the natural logarithm of the number" candidates need testing on average.
- The count of primes below a number has been computed for numbers with more than 25 digits without listing the primes.
- What nobody has is a short formula that hands over the n-th prime directly. No proof says such a formula cannot exist.

So the primes are a fixed list that imitates randomness in bulk and keeps a few rigid habits and can be computed to any length but not from a shortcut formula that anyone knows.

## How the questions tie back to the lists

- The recipe n² + n + 41 ranks high for primes on the master lists and reaches only 162 of 360 marks as moves. Being rich in primes and spreading evenly around a circle are separate properties.
- The lists compare each recipe with random-like behavior of the number line and this page shows the number line's primes behaving like random drops on a circle in bulk.

## Numbers that this page adds to the list in Part 7

49. 0.0432174 is the sum of 1 over e to the power (pi times each square).
50. 0.047206 is the sum of n over e to the power (n pi) and 0.0018779 is 1/24 minus 1 over (8 × pi).
51. 96 is the number of marks out of 360 reached by moves of 1 and 2 and 3 degrees.
52. 2119 is 360 times the natural logarithm of 360 which is the number of random drops expected to fill 360 marks.
