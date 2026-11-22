# Questions about how few prime pieces a number has

> **About this page:** One AI model (Claude) wrote this page on 21 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the pages [log-questions.md](log-questions.md) and [ladder-questions.md](ladder-questions.md) and [reciprocal-questions.md](reciprocal-questions.md) and [pi-ripples-questions.md](pi-ripples-questions.md). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route and the picture of a number as a stick cut into prime lengths. A program rechecked every figure (the file prime_pieces_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## The picture the page uses

The natural logarithm of a number is a stick. Each prime piece of the number is a length of that stick (0.69 for the prime 2 and 1.10 for the prime 3 and 1.61 for the prime 5) and the lengths add up to the whole stick. A 100 digit number has a stick of length 230.

## Question: the double logarithm says numbers have very few prime pieces. What does that look like?

The average number of different prime pieces is the logarithm of the logarithm plus 0.26.

- A number near one million averages about 2.9.
- A number with 80 digits (about the count of atoms in the visible universe) averages about 5.5.
- A 100 digit number averages about 5.7.
- A 1000 digit number averages about 8.0.
- A number with one million digits averages about 14.9.
- A number with one billion digits averages about 21.8.
- A googolplex (a 1 followed by 10 to the power 100 zeros) averages about 231.

One or two large primes usually take up most of a number. Measured over every number up to one million:

- The largest prime piece holds 64.9% of the stick on average (the share settles near 62.4% for very large numbers).
- The second largest piece holds 20.3% on average (the share settles near 21%).
- 73.2% of the numbers have a prime piece bigger than their own square root (the share settles near 69.3% which is the natural logarithm of 2).

So a typical 100 digit number looks like a prime of roughly 62 digits times a prime of roughly 21 digits times a few small primes.

The most pieces possible is far above the typical count. Up to one million the record is seven different pieces held by 510510 = 2 × 3 × 5 × 7 × 11 × 13 × 17 and seven other numbers. A 100 digit number could hold 54 different primes (the product of every prime up to 251). Up to one million 95.5% of numbers have between one and four different prime pieces.

One widely used kind of digital lock is built by multiplying two large primes and the lock holds because the large pieces of a big number are slow to find. If typical numbers broke into many small primes a computer could pull the small pieces out quickly.

## Question: does taking the logarithm of the logarithm drill down toward the primes as the numbers with the fewest pieces?

Each logarithm drills one level down.

- The number itself (such as a 100 digit number).
- The first logarithm (230) which is the length of the stick.
- The second logarithm (5.4) which is about how many different pieces a stick of that length breaks into.

A prime is a number whose stick is a single piece. Treat the count of extra pieces beyond the first as a count of chance events with an average of about the double logarithm. The chance of zero events is 1/e raised to the average count. With an average of "logarithm of the logarithm" that chance unpacks to 1 divided by the natural logarithm. So the rule "primes show up at the rate 1 divided by the natural logarithm" reads as "the chance that a number has no extra pieces".

A proven result says the share of numbers with exactly k different prime pieces is about (1 divided by the natural logarithm) times (the double logarithm raised to the power k − 1) divided by (1 × 2 × … × (k − 1)). Setting k = 1 gives the prime rule.

At one million the formula gives 7.2% for one piece and 19.0% for two and 25.0% for three. The true shares up to one million are 7.9% and 28.9% and 38.0%. The formula has the right shape and becomes accurate only for numbers far larger than one million.

The double logarithm of one particular number says nothing about that number's own pieces. 1000003 is a prime and 1000000 is built from 2 and 5 and the two have nearly the same double logarithm. The double logarithm describes the average over numbers of a given size.

## Question: how many pieces does a stick of a given length typically break into?

About "the natural logarithm of the length" pieces.

Real sticks near one million all have length 13.82.

- 999983 is prime so the stick is one piece.
- 999997 is 757 × 1321 so the pieces are 6.63 and 7.19.
- 1000001 is 101 × 9901 so the pieces are 4.62 and 9.20.
- 999998 is 2 × 31 × 127 × 127 so the pieces are 0.69 and 3.43 and 4.84 and 4.84.
- 999999 is 3 × 3 × 3 × 7 × 11 × 13 × 37 so the pieces are three of 1.10 and then 1.95 and 2.40 and 2.56 and 3.61.

Pick out one prime piece of a random number. That piece takes a share of the stick spread evenly between nothing and everything. When an evenly random share is cut away the natural logarithm of the leftover drops by exactly 1 on average (the "average logarithm sits one copy below the top" fact from the first page). So each break divides the leftover length by about e.

- A stick of length 230 runs 230 then 85 then 31 then 11.5 then 4.2 then 1.5 then 0.6. The shortest piece is the prime 2 with length 0.69 so the breaking runs out after about five or six rounds which matches 5.7 pieces.
- A stick of length 13.8 runs 13.8 then 5.1 then 1.9 then 0.7 which is about three rounds and matches 2.9 pieces.

The number of times a length can be divided by e before reaching about 1 is the natural logarithm of the length. The length is already a logarithm so the piece count is a logarithm of a logarithm.

## Question: what does "one piece per band" mean and does the band from 7 to 163 add up to 1?

Sort the piece lengths into bands where each band reaches about e times further than the last. One number in every 7 is divisible by 7 so the prime 7 contributes 1/7 of a piece per number on average. Adding 1 over each prime in a band gives the average number of pieces a random number draws from that band.

The running total for the 35 primes from 7 to 163: 0.143 after 7 and 0.234 after 11 and 0.311 after 13 and 0.370 after 17 and 0.422 after 19 and 0.466 after 23 and 0.532 after 31 and 0.710 after 71 and 0.872 after 163.

- The band of lengths 0.69 to 1.9 holds the primes 2 and 3 and 5. The total is 1.033 and the smooth prediction is 1.01.
- The band of lengths 1.9 to 5.1 holds the 35 primes from 7 to 163. The total is 0.872 and the smooth prediction is 0.99.
- The band of lengths 5.1 to 13.9 holds the 84820 primes from 167 to 1088161. The total is 0.988 and the smooth prediction is 1.00.

The smooth prediction is 1 per band because multiplying a length by e adds 1 to the logarithm of the length. The middle band falls short because small primes are too few and too lumpy for the smooth rule. Three bands hold 3 and then 35 and then 84820 primes and each band still hands a random number about one piece. The three totals add to 2.89.

The top band is by far the longest in plain length so the piece from the top band takes most of the stick. "Few pieces" and "one giant piece" are the same fact.

## Question: can the double logarithm be shown setting the average piece count in an example?

For numbers near 1000: the natural logarithm of 1000 is 6.908. The natural logarithm of 6.908 is 1.933. Adding 0.26 gives 2.19.

The eleven numbers from 1000 to 1010 have these counts of different prime pieces: 1000 has 2 (built from 2 and 5). 1001 = 7 × 11 × 13 has 3. 1002 = 2 × 3 × 167 has 3. 1003 = 17 × 59 has 2. 1004 has 2 (built from 2 and 251). 1005 = 3 × 5 × 67 has 3. 1006 = 2 × 503 has 2. 1007 = 19 × 53 has 2. 1008 has 3 (built from 2 and 3 and 7). 1009 is prime and has 1. 1010 = 2 × 5 × 101 has 3. The total is 26 pieces across 11 numbers which is an average of 2.36.

Bigger stretches:

- Around 1000 the measured average is 2.28 and the prediction is 2.19.
- Around 10000 the measured average is 2.54 and the prediction is 2.48.
- Around 100000 the measured average is 2.75 and the prediction is 2.70.
- Around one million the measured average is 2.93 and the prediction is 2.89.
- Around ten million the measured average is 3.07 and the prediction is 3.04.

## Question: how are the sum and the double logarithm in each comparison computed?

The two are computed in different ways. For "up to 10" the sum uses the primes 2 and 3 and 5 and 7: 0.5 + 0.3333 + 0.2 + 0.1429 = 1.176. The double logarithm uses the number 10 alone: the natural logarithm of 10 is 2.3026 and the natural logarithm of 2.3026 is 0.834. The whole numbers 1 through 10 only decide which primes are included. (The sum 1 + 2 + … + 10 = 55 plays no part. The double logarithm of 55 is 1.388.)

## Question: where does the fixed 0.26 come from?

The 0.26 is the gap between the sum of 1 over each prime and the double logarithm and the gap settles on one value.

- Up to 10 the gap is 1.176 − 0.834 = 0.342.
- Up to 100 the gap is 1.803 − 1.527 = 0.276.
- Up to 10000 the gap is 2.483 − 2.220 = 0.263.
- Up to one million the gap is 2.8873 − 2.6258 = 0.2615.
- Up to ten million the gap is 3.0414 − 2.7799 = 0.2615.

The gap has two ingredients. The sieve result says the pile of true shrink amounts equals the double logarithm plus 0.5772. The true shrink amount for each prime is a little bigger than the announcement 1/p (by 0.1931 for the prime 2 and 0.0721 for the prime 3 and 0.0231 for the prime 5) and those extras total 0.3157. So the sum of 1 over each prime equals the double logarithm plus 0.5772 − 0.3157 = 0.2615.

A plainer view: at the first prime 2 the double logarithm is −0.37 while the true sum is already 0.5. The smooth formula begins behind and the lumpiness of the small primes then trims the lead.

## Question: is the sum of 1 over each prime the rate at which new prime pieces get added?

Yes. Bringing the prime 7 into the list adds 1/7 of a piece to the average number. The sum is the total handed out so far. Each time the sum climbs by 1 the typical number has gained one more prime piece.

- The sum passes 1 at the prime 5 (3 primes).
- The sum passes 2 at the prime 277 (59 primes).
- The sum passes 3 at the prime 5195977 (361139 primes).
- The sum passes 4 at a prime near 1.8 × 10 to the power 18.
- The sum passes 5 near 4 × 10 to the power 49.
- The sum passes 6 near 8 × 10 to the power 134.

The extra piece appears in the average and not in each number. The whole spread of counts slides up by one.

## Question: are the crossings related to powers of e?

Yes. The crossing prime for the whole number k is about e raised to the power (e raised to the power (k − 0.26)). Adding 1 to k multiplies the natural logarithm of the crossing prime by e which is the same as raising the crossing prime to the power e.

- The natural logarithm of 5 is 1.61.
- The natural logarithm of 277 is 5.62 which is 3.49 times the one before.
- The natural logarithm of 5195977 is 15.46 which is 2.75 times the one before.
- The natural logarithm of the fourth crossing is 42.03 which is 2.72 times the one before.

277 raised to the power e is about 4.4 million against the true 5.2 million. 5195977 raised to the power e is about 1.8 × 10 to the power 18. The crossings sit at about 1 digit and 2.5 digits and 6.7 digits and 18 digits and 50 digits and 135 digits.

The count of primes needed (3 and 59 and 361139) follows the pattern loosely because the count of primes below a number carries an extra logarithm. 59 raised to the power e is about 65000.

## How the questions tie back to the lists

- The primes 2 and 3 and 5 and 7 account for 1.176 of the average count of prime pieces so blocking those few primes removes a large share of the ways an output can fail to be prime.
- Blocking a band of larger primes removes about the same one piece no matter how many primes the band holds which is why the gain from blocking all primes up to p grows only like the natural logarithm of p.
- A recipe's outputs that are prime are the outputs whose stick is a single piece.
