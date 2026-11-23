# Questions about a circle where the arrow lands on the term itself

> **About this page:** One AI model (Claude) wrote this page on 23 November 2026 from a back and forth chat with the author of this repository. The question is the author's question with the wording tidied and the answers are the chatbot's answers shortened. The page continues the twelve earlier question pages in this folder (the last one is [spin-questions.md](spin-questions.md)). The author proposed the test on this page: point the arrow at each term of a sum directly and remove full turns from any term larger than the circle. The underlying facts are standard mathematics so the page claims no new result. The counts are measurements from the program term_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts and the page marks which statements are proven and which are only measured. No other person has reviewed the page yet.

## The two rules side by side

The page before this one used a "moving" rule: each term of a sum moves the arrow that many marks so the arrow shows the running total of the sum.

This page uses a "landing" rule: the arrow points at the mark with the same number as the term. A term larger than the number of marks has full turns removed first. With 360 marks the term 367 lands on mark 7 and the term 720 lands on mark 0.

The file [spin-animation.html](spin-animation.html) in this folder shows the two rules as two circles side by side.

## Question: what changes when the arrow lands on the term itself?

The landing rule looks only at what is left of each term after full turns are removed. The running total plays no part. So the rows trade places.

Marks reached out of 360 under the landing rule (with the count under the moving rule after each one):

- The counting numbers 1 and 2 and 3 reach all 360 marks (96 under the moving rule).
- The composite numbers 4 and 6 and 8 and 9 reach all 360 marks (360 under the moving rule).
- The odd numbers reach 180 marks because an odd number stays odd after 360 is removed (36 under the moving rule).
- The primes reach 99 marks which is 27.5% (360 under the moving rule).
- The triangular numbers 1 and 3 and 6 and 10 reach 96 marks (216 under the moving rule).
- The cubes reach 75 marks (18 under the moving rule).
- The Fibonacci numbers reach 75 marks (75 under the moving rule).
- The recipe n² + n + 41 reaches 48 marks (162 under the moving rule).
- The squares reach 36 marks (216 under the moving rule).
- The fourth powers reach 16 marks (360 under the moving rule).
- The doublings 1 and 2 and 4 and 8 reach 15 marks (14 under the moving rule). The marks are 1 and 2 and 4 and 8 and 16 and 32 and 64 and 128 and 136 and 152 and 184 and 248 and 256 and 272 and 304. After 1 and 2 and 4 the arrow circles through the other 12 marks.
- The row 1 and 61 and 121 where each term is 60 more reaches 6 marks which are 1 and 61 and 121 and 181 and 241 and 301 (360 under the moving rule).
- The row 1 and 1 × 2 and 1 × 2 × 3 reaches 6 marks which are 1 and 2 and 6 and 24 and 120 and 0 (5 under the moving rule). The term 1 × 2 × 3 × 4 × 5 × 6 is 720 which is two full turns so that term and every later term lands on mark 0.
- The same term 7 over and over reaches 1 mark (360 under the moving rule).

A steady row such as 1 + 1 + 1 is the worst row under the landing rule and one of the best under the moving rule. The counting numbers are the best row under the landing rule and a middling row under the moving rule.

## Question: are the two rules related?

Yes. The two rules are one rule shifted by a level. The running totals of one row are the terms of another row. So moving the arrow by the first row gives the same marks as landing the arrow on the second row.

- The running totals of the odd numbers are the squares (1 and 1 + 3 = 4 and 1 + 3 + 5 = 9). The odd numbers under the moving rule reach 36 marks and the squares under the landing rule reach the same 36 marks.
- The running totals of the counting numbers are the triangular numbers (1 and 1 + 2 = 3 and 1 + 2 + 3 = 6). The counting numbers under the moving rule reach 96 marks and the triangular numbers under the landing rule reach the same 96 marks.
- The running totals of a steady 1 + 1 + 1 are the counting numbers. A steady move of 1 fills the circle under the moving rule and the counting numbers fill the circle under the landing rule.

The Fibonacci numbers score 75 under both rules because the running total of the Fibonacci numbers is a later Fibonacci number minus 1. So the moving rule gives the landing marks slid back by one mark.

## Question: why do the primes reach only 99 of 360 marks?

The number 360 is built from the primes 2 and 3 and 5. A prime above 5 shares no prime piece with 360. Removing 360 from a number does not change whether the number is even or a multiple of 3 or a multiple of 5. So a prime above 5 can never land on an even mark or a mark that is a multiple of 3 or a multiple of 5.

Exactly 96 of the 360 marks share no prime piece with 360. The primes 2 and 3 and 5 land on their own marks once each. That gives 96 + 3 = 99 marks.

The first 279 primes were enough to reach all 99 marks (the 279th prime is 1801).

A proven theorem says each of the 96 open marks holds infinitely many primes and the primes spread evenly among those marks in the long run. In the measurement the first 200000 primes visited each of the 96 marks between 2036 and 2130 times where an even share is 2083.

The 96 marks open to the primes and the 96 marks reached by the triangular numbers are different sets that have the same size. The two sets share 8 marks.

## Question: which circle sizes do the primes fill under the landing rule?

Marks reached by the primes for a few circle sizes:

- 2 marks: 2 reached (100%)
- 3 marks: 3 reached (100%)
- 4 marks: 3 reached (75%)
- 6 marks: 4 reached (66.7%)
- 10 marks: 6 reached (60%)
- 12 marks: 6 reached (50%)
- 30 marks: 11 reached (36.7%)
- 60 marks: 19 reached (31.7%)
- 100 marks: 42 reached (42%)
- 210 marks: 52 reached (24.8%)
- 256 marks: 129 reached (50.4%)
- 360 marks: 99 reached (27.5%)
- 997 marks: 997 reached (100%)
- 1000 marks: 402 reached (40.2%)
- 2310 marks: 485 reached (21%)

The rule behind the table: the number of marks reached is the number of marks that share no prime piece with the circle size plus the number of different primes that divide the circle size. The program found no exception for any circle size from 2 to 5000. The rule follows from the proven theorem in the answer above.

The primes fill a circle exactly when the number of marks is itself a prime. All 669 circle sizes from 2 to 5000 that were filled are primes and all 669 primes up to 5000 were filled. On a circle with a prime number of marks no mark is blocked except mark 0 and the circle's own prime lands on mark 0.

A circle size with many different small prime pieces blocks the most marks. The lowest share from 2 to 5000 marks was 20.9% at 4620 marks (4620 is 2 × 2 × 3 × 5 × 7 × 11).

## Question: how does the blocked share tie back to the sieve?

The share of marks open to the primes on a circle of 360 is 96/360 which is 26.7%. That share is (1 − 1/2) × (1 − 1/3) × (1 − 1/5) which is the sieve product from the first pages taken over the primes 2 and 3 and 5.

So a circle whose size is built from the first few primes shows the sieve as a picture. Each prime piece of the circle size switches off the marks that are multiples of that prime. The marks left lit are the only places a later prime can land.

Under the moving rule the primes looked random because the running total mixes the terms together. Under the landing rule the primes show one of their rigid habits: a prime never shares a prime piece with a number the prime does not divide.

## How the question ties back to the lists

- The recipe n² + n + 41 ranks high for primes on the master lists and lands on only 48 of 360 marks. Every output of the recipe is odd and the outputs avoid many marks so a row can be rich in primes while reaching a small part of a circle.
- The master lists compare each recipe with the plain number line. The plain number line fills every circle under the landing rule and the primes inside the number line fill only circles with a prime number of marks.

## Numbers that this page adds to the list in Part 7

53. 99 is the number of marks out of 360 that the primes land on which is 27.5%.
54. 26.7% is 96/360 which is (1 − 1/2) × (1 − 1/3) × (1 − 1/5) and is the share of marks on a circle of 360 that are open to primes above 5.
55. 669 is the number of primes up to 5000 and is also the number of circle sizes up to 5000 that the primes fill under the landing rule.
