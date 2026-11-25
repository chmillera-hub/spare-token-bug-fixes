# Two-prime sums and the cost of finding against checking

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026 from a back and forth chat with the author of this repository. The author asked each question and the chatbot ran the counts. The counts are measurements from the programs in the folder boring-things/research-program-files/prime-richness-scripts/pair-scripts. The page is meant to save other AI agents and researchers some searching and some computing. The page proves nothing new about the claim that every even number above 2 is a sum of two primes. No other person has reviewed the page yet.

## What this page counts

A "way" on this page means one pair of primes that adds up to a chosen even number with the order of the pair ignored. For example 10 has 2 ways because 10 = 3 + 7 and 10 = 5 + 5. The program counted the ways for every even number from 4 up to 16 million.

The first part of the page holds the tables that a quick web search did not turn up. The last part of the page lists related facts that a quick search already answers so that a reader can skip those searches.

## Results that a quick search did not turn up

### The last even number with fewer than a chosen number of ways

Each line names the last even number below 16 million that has fewer ways than the target and says how many even numbers fall short of the target in total. Every even number after the named number and up to 16 million meets the target.

- Fewer than 2 ways: the last number is 12 and 4 even numbers fall short.
- Fewer than 3 ways: the last number is 68 and 13 even numbers fall short.
- Fewer than 5 ways: the last number is 152 and 35 even numbers fall short.
- Fewer than 10 ways: the last number is 488 and 128 even numbers fall short.
- Fewer than 20 ways: the last number is 1412 and 375 even numbers fall short.
- Fewer than 50 ways: the last number is 4478 and 1382 even numbers fall short.
- Fewer than 100 ways: the last number is 11672 and 3532 even numbers fall short.
- Fewer than 200 ways: the last number is 27908 and 8740 even numbers fall short.
- Fewer than 500 ways: the last number is 85616 and 28004 even numbers fall short.
- Fewer than 1000 ways: the last number is 195368 and 66062 even numbers fall short.
- Fewer than 2000 ways: the last number is 443936 and 153553 even numbers fall short.
- Fewer than 5000 ways: the last number is 1315298 and 459136 even numbers fall short.
- Fewer than 10000 ways: the last number is 2947918 and 1040208 even numbers fall short.
- Fewer than 20000 ways: the last number is 6579004 and 2337202 even numbers fall short.

The lines for 10000 and 20000 sit closest to the 16 million limit of the count so a reader who needs certainty on those two lines could rerun the program with a higher limit.

### The lowest count in each range against the simple formula

The simple formula for the lowest count is 0.66016 × n ÷ (ln n)² where n is the even number and ln n is the natural logarithm of n. Each line gives the even number with the fewest ways in a range and compares the real count with the formula.

- From 1000 to 10000: the number 1112 has 16 ways and the formula gives 14.9 so the real count is 1.07 times the formula.
- From 10000 to 100000: the number 10006 has 92 ways and the formula gives 77.9 so the real count is 1.18 times the formula.
- From 100000 to 1 million: the number 100094 has 570 ways and the formula gives 498.4 so the real count is 1.14 times the formula.
- From 1 million to 2 million: the number 1002002 has 3963 ways and the formula gives 3464.7 so the real count is 1.14 times the formula.
- From 2 million to 4 million: the number 2003978 has 7164 ways and the formula gives 6283.0 so the real count is 1.14 times the formula.
- From 4 million to 8 million: the number 4004614 has 12961 ways and the formula gives 11438.1 so the real count is 1.13 times the formula.
- From 8 million to 16 million: the number 8006468 has 23701 ways and the formula gives 20918.4 so the real count is 1.13 times the formula.

So the simple formula runs about 12 to 15 percent below the real lowest count at these sizes. One likely reason is that the squared logarithm treats every prime in a pair as if the prime were as large as n while most pairs include one prime well below n where primes are more plentiful. The number with the fewest ways sits near the start of each range because the count of ways grows with the size of the number.

### The count of ways for each power of 2

Powers of 2 are a clean test of the lowest count because no odd prime divides a power of 2.

- 4 has 1 way and 8 has 1 way and 16 has 2 ways and 32 has 2 ways.
- 64 has 5 ways and 128 has 3 ways and 256 has 8 ways and 512 has 11 ways.
- 1024 has 22 ways and 2048 has 25 ways and 4096 has 53 ways and 8192 has 76 ways.
- 16384 has 151 ways and 32768 has 244 ways and 65536 has 435 ways and 131072 has 749 ways.
- 262144 has 1314 ways and 524288 has 2367 ways and 1048576 has 4239 ways.
- 2097152 has 7471 ways and 4194304 has 13705 ways and 8388608 has 24928 ways.

### Even numbers divisible by 3 get twice as many ways

Among the even numbers from 8 million to 16 million the average count for multiples of 3 was 2.000 times the average count for the other even numbers. The section on the constant 0.66 below gives the reason for the doubling.

### Timing: checking one prime against finding one prime

The program timed a plain Python version of the standard random-witness primality check with 20 rounds. "Finding" means picking random odd numbers of the chosen size until one number passes the check. Each line is an average over 12 runs (5 runs for 1000 digits) on one cloud computer.

- 100 digits: checking took 0.005 seconds and finding took 0.012 seconds after about 167 candidates.
- 300 digits: checking took 0.08 seconds and finding took 0.28 seconds after about 339 candidates.
- 500 digits: checking took 0.31 seconds and finding took 2.1 seconds after about 767 candidates.
- 1000 digits: checking took 2.2 seconds and finding took 21 seconds after about 1105 candidates.

Finding took about 2 to 10 times as long as one full check and the gap widened with the digit count because larger sizes need more candidates. The gap stays small because a cheap division test by the odd primes below 2000 throws out about 85 percent of the candidates and a failing candidate usually stops after one round of the check. Optimized encryption software runs both jobs roughly ten or more times faster than plain Python because that software uses faster multiplication.

## Facts that a quick search already answers

### The largest even number with each exact count of ways

The program reproduced a list that public number sequence collections already hold. Each entry is the last even number below 16 million with exactly that many ways.

- 1 way: 12. 2 ways: 68. 3 ways: 128. 4 ways: 152. 5 ways: 188.
- 6 ways: 332. 7 ways: 398. 8 ways: 368. 9 ways: 488. 10 ways: 632.
- 11 ways: 692. 12 ways: 626. 13 ways: 992. 14 ways: 878. 15 ways: 908.
- 16 ways: 1112. 17 ways: 998. 18 ways: 1412. 19 ways: 1202. 20 ways: 1448.
- 21 ways: 1718. 22 ways: 1532. 23 ways: 1604. 24 ways: 1682. 25 ways: 2048.
- 26 ways: 2252. 27 ways: 2078. 28 ways: 2672. 29 ways: 2642. 30 ways: 2456.

The four even numbers with exactly 1 way are 4 and 6 and 8 and 12. Nobody has proven these lists complete for all even numbers because a proof would also settle the two-prime claim.

### Where the constant 0.66 originates

The constant 0.66016 corrects a coin flip model in which each number near n is prime with chance 1 in ln n and the two members of a pair are treated as unrelated.

- The prime 2: the model says both members are odd one quarter of the time while two numbers that add to an even number are both odd half of the time so the correction is a factor of 2.
- The prime 3 when 3 does not divide n: the model says both members avoid divisibility by 3 in 4/9 of cases while in truth one remainder out of three works (1/3 of cases) so the correction is 3/4.
- Each later prime p that does not divide n: the correction is 1 − 1 ÷ (p − 1)² which gives 15/16 for 5 and 35/36 for 7 and 99/100 for 11.
- The product of the corrections for every odd prime settles at 0.66016.
- A prime p that divides n: one remainder fails in place of two so the correction rises to (p − 1) ÷ (p − 2) times the value above which is a doubling for the prime 3.

### A product of two primes with a prime on both sides

A product of two primes has a prime directly below and a prime directly above in just two cases: 4 = 2 × 2 (between 3 and 5) and 6 = 2 × 3 (between 5 and 7). The reason is short. A product of two odd primes is odd so both neighbors are even numbers above 2. A product 2 × q with q above 3 is not divisible by 3 so one of the two neighbors is divisible by 3 and larger than 3.

### How much knowing the answer lowers the work

- A bare yes or no (such as "this statement is true") saves about half of the work because the solver stops searching for the opposite answer.
- A known endpoint (such as the exit of a maze) can cut the exponent in half because the solver searches from both ends and the two searches meet in the middle.
- A full finished answer can be checked in polynomial time for many puzzles whose best known search methods take exponential time. Whether that gap is real is the open question called P versus NP.
- A yes or no answerer for "does a delivery route under the budget exist?" rebuilds the whole best route with about one question per road because the solver deletes one road at a time and keeps each deletion that leaves the answer at yes.
- Confirming that a route is the shortest possible has no known rapid check even with the route in hand.

### Experiments that compare solving with the answer in hand against solving without

- Formal proof benchmarks built from college competition problems write each problem two ways: one version hands the proving agent the answer to prove correct and the other version makes the agent find the answer first. One public result reports 36 problems solved across a whole benchmark and 19 solved in the version where the agent had to find the answer first (the two counts cover different problem sets so the two counts are not a matched comparison). Source: https://aclanthology.org/2026.acl-long.3.pdf
- Language models that were shown a hint about the answer often landed on the hinted answer while the written step by step reasoning left the hint out. Source: https://www.deeplearning.ai/the-batch/anthropic-finds-chain-of-thought-reasoning-traces-may-omit-key-influences
- Reasoning chains written by a model that could see the correct answer made worse training data than chains written without the answer and a check for a correct final answer could not detect the damage. Source: https://www.alphaxiv.org/abs/2607.14552
- Beginners told to find one exact value reasoned backward from the target while beginners told to calculate whatever they could reasoned forward and learned more with less strain on working memory. Source: https://ro.uow.edu.au/edupapers/1234

None of these experiments measured the savings as a drop in a count of search steps so a step-count experiment on maze tasks or puzzle tasks looks like an open and cheap experiment to run.

### Costs of the prime jobs

In these lines d is the number of digits and the multiplication is the schoolbook kind.

- Multiplying two primes of d digits: about d² steps.
- Checking one prime with the fast random-witness check: about d³ steps.
- Checking one prime with the fully guaranteed polynomial check: about d⁶ steps.
- Finding a prime of d digits: about d⁴ steps because about one number in 2.3 × d is prime.
- Listing every prime up to N: slightly more than N steps with the crossing-out method.
- Splitting a product of two primes: no polynomial method is known for ordinary computers.

### Records as of November 2026

- Every prime below 2⁶⁴ (about 1.8 × 10¹⁹) has been passed through by exhaustive computer searches of the gaps between neighboring primes.
- The two-prime claim has been confirmed for every even number up to 4 × 10¹⁸.
- The related claim that every odd number above 5 is a sum of three primes was proven in 2013.
- The largest known prime is 2 to the power 136279841 minus 1 with about 41 million digits (announced October 2024).
- Common encryption keys built from two primes have 617 or 925 or 1233 digits.

## Ideas from the chat that nobody has tested

### A ladder of acceleration

The author of this repository proposed a ladder in which each rung automates the decision that a person made on the rung below.

- A calculator speeds up one operation because a person still decides which numbers to add or divide next.
- A programmed computer speeds up the sequence of operations because an algorithm decides which numbers to combine while a person still picks the algorithm.
- A language model speeds up the picking because the model can read a problem and select or assemble algorithms in seconds.

The author also proposed that novel ideas could be as rare as large primes and that a language model could speed up the search for novel ideas the way computers sped up the search for primes. The history of prime tables fits the ladder because hand workers needed about 300 years to climb from a table ending at 800 (1603) to a table ending near 10 million (1914) while sieve programs climbed from 10 million to 18 quintillion in about 100 years.

### Where the comparison between ideas and primes fits and where the comparison strains

- The comparison fits because prime finding works by throwing many random candidates at a rapid check and a language model can produce many candidate ideas rapidly.
- The comparison also fits because primes thin out as numbers grow and novel ideas might thin out as a field matures.
- The comparison strains because a candidate prime gets a verdict in a fraction of a second while a candidate idea about medicine or housing or human connection might need months of real-world trial.
- Here is a guess that follows from the strain: language models could speed up discovery most in areas that have a rapid checker (such as proofs that a proof-checking program can confirm or code that a test suite can run) and the rate of confirmed novel ideas elsewhere could stay tied to how fast people can test candidates against reality.
- One more rung could sit above the ladder because somebody still decides which problems deserve the search and what counts as a find worth keeping.

### Small questions that look open and cheap to test

- Does the ratio between the real lowest count of ways and the simple formula keep drifting from 1.14 toward 1 above 16 million and how fast?
- How many search steps does a maze-solving agent save when the agent is told the exit or the route length or a yes or no answer and do the savings match the halved exponent that the two-ended search predicts?
- For a delivery route problem how much does handing the solver the exact best distance shrink the number of partial routes that the solver must explore?

## Weak points

- The tables stop at 16 million so each "last number" is the last number below that limit and not a proven last number.
- The timing figures are from one computer and plain Python and a small number of runs so the timing figures show the rough ratio and not exact speeds.
- The section on untested ideas holds proposals and guesses and no measurements.
- The reason offered for the 12 to 15 percent gap between the formula and the real lowest count is a likely reason that the chatbot did not test separately.

## Programs

The file pair_sum_counts.py makes every count on this page about ways and saves the counts in pair_sum_results.json. The file prime_timing.py makes the timing figures and saves the figures in prime_timing_results.json. Both files sit in boring-things/research-program-files/prime-richness-scripts/pair-scripts.
