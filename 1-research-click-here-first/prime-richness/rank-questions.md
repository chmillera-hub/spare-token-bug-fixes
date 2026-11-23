# Questions about ranking sums that fill a circle under two rules

> **About this page:** One AI model (Claude) wrote this page on 23 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the thirteen earlier question pages in this folder (the last one is [term-questions.md](term-questions.md)). The author proposed the ranking on this page and each way of scoring: rank many sums by how well each sum fills a circle under both rules and reward a sum that does well on many circle sizes. The scores are measurements from the programs both_rules_ranking.py and digit_rows.py in the folder boring-things/research-program-files/prime-richness-scripts/rank-scripts. The page claims no new result and no other person has reviewed the page yet.

## The two rules and the test

Under the "cumulative" rule each term of a sum moves the arrow that many marks so the arrow shows the running total. Under the "literal" rule the arrow lands on the mark with the same number as the term after full turns are removed. A term with a minus sign moves the arrow backward under the cumulative rule and lands on the mark that many steps back from mark 0 under the literal rule.

The test ran 32 sums on every circle size from 2 marks to 5000 marks which is 4999 sizes. Each sum got 30 steps for each mark on the circle so a circle of 360 marks got 10800 steps and a circle of 5000 marks got 150000 steps. Terms with decimals had the decimals dropped with no rounding.

The file [spin-animation.html](spin-animation.html) in this folder shows both rules as two circles side by side with the share filled in the corner of each circle.

## Question: which sums fill both circles?

Five sums filled every mark on all 4999 circle sizes under both rules:

- 1 − 2 + 3 − 4 (the counting numbers with flipping signs). The running totals are 1 and −1 and 2 and −2 and 3 so the arrow swings one mark wider on each side. On 1000 marks this sum filled the literal circle in 1000 steps and the cumulative circle in 1999 steps which was the fastest of the 32 sums.
- 4 + 6 + 8 + 9 (the composite numbers) and the same sum with flipping signs. On 1000 marks the composite numbers needed 2567 steps on the literal circle and 8202 steps on the cumulative circle.
- 0 + 1 + 3 + 5 + 8 + 10 (the whole part of n times the natural logarithm of n).
- 1 + 2 + 5 + 8 + 11 (the whole part of n times the root of n).

A sum fills both circles when the terms reach every remainder and the running totals also reach every remainder. Flipping the signs repaired the counting numbers because the backward moves stop the running total from locking into the triangular numbers. Flipping the signs did not repair the primes because a sign cannot move a prime onto a blocked mark.

## List 1: the two percentages added together (out of 200)

Each percentage is the share of marks a sum reached averaged over all 4999 circle sizes. The brackets show the cumulative circle and then the literal circle. A sum that covers all of both circles scores 200.

1. 1 − 2 + 3 − 4 (counting numbers with flipping signs): 200.0 (100.0 and 100.0)
2. 4 + 6 + 8 + 9 (composite numbers): 200.0 (100.0 and 100.0)
3. 4 − 6 + 8 − 9 (composite numbers with flipping signs): 200.0 (100.0 and 100.0)
4. 0 + 1 + 3 + 5 + 8 + 10 (whole part of n times the natural logarithm of n): 200.0 (100.0 and 100.0)
5. 1 + 2 + 5 + 8 + 11 (whole part of n times the root of n): 200.0 (100.0 and 100.0)
6. 1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2): 199.8 (100.0 and 99.8)
7. 1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio): 199.7 (100.0 and 99.7)
8. 1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece): 192.4 (100.0 and 92.4)
9. 1 − 3 + 5 − 7 (odd numbers with flipping signs): 168.7 (100.0 and 68.7)
10. 2 + 3 + 5 + 7 (primes): 161.1 (100.0 and 61.1)
11. 2 − 3 + 5 − 7 (primes with flipping signs): 161.1 (100.0 and 61.1)
12. 1 + 2 + 3 + 4 (counting numbers): 133.6 (33.6 and 100.0)
13. 1 + 2 + 4 + 5 + 7 + 8 (numbers that are not multiples of 3): 128.4 (39.5 and 88.9)
14. 1 + 2 + 2 + 3 + 3 + 3 (each number n repeated n times): 120.7 (100.0 and 20.7)
15. 1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n): 104.6 (100.0 and 4.6)
16. 1 + 3 + 5 + 7 (odd numbers): 102.8 (27.8 and 75.0)
17. 1 + 4 + 1 + 5 + 9 (digits of pi): 101.4 (100.0 and 1.4)
18. 1 + 1 + 1 + 1 (steady 1): 100.2 (100.0 and 0.2)
19. 2 + 4 + 6 + 8 (even numbers): 99.7 (24.7 and 75.0)
20. 1 − 3 + 6 − 10 (triangular numbers with flipping signs): 97.9 (43.4 and 54.5)
21. 1 − 4 + 9 − 16 (squares with flipping signs): 92.6 (54.5 and 38.1)
22. 1 + 3 + 6 + 10 (triangular numbers): 88.7 (55.2 and 33.6)
23. 7 + 7 + 7 + 7 (steady 7): 87.9 (87.8 and 0.2)
24. 1 + 4 + 9 + 16 (squares): 83.0 (55.2 and 27.8)
25. 1 + 16 + 81 + 256 (fourth powers): 76.2 (57.2 and 19.0)
26. 43 + 47 + 53 + 61 (the recipe n² + n + 41): 75.8 (51.1 and 24.7)
27. 1 + 8 + 27 + 64 (cubes): 68.4 (18.9 and 49.5)
28. 1 + 2 + 2 + 4 (gaps between neighboring primes): 65.1 (61.0 and 4.1)
29. 1 + 1 + 2 + 3 + 5 + 8 (Fibonacci numbers): 62.5 (31.3 and 31.3)
30. 1 + 2 + 4 + 8 + 16 (doublings): 39.9 (19.9 and 20.0)
31. 1 + 2 + 6 + 24 + 120 (1 and 1 × 2 and 1 × 2 × 3): 30.8 (15.3 and 15.5)
32. 1 − 1 + 1 − 1 (steady 1 with flipping signs): 0.6 (0.3 and 0.3)

The steady sum 1 + 1 + 1 + 1 sits in the middle of this list at about 100 because the running total walks onto every mark of the cumulative circle while the arrow on the literal circle stays on mark 1.

## List 2: circle sizes filled on the cumulative circle plus circle sizes filled on the literal circle (out of 9998)

A size counts on a circle only when the sum reached every mark of that circle. The brackets show the cumulative count and then the literal count.

1. 1 − 2 + 3 − 4 (counting numbers with flipping signs): 9998 (4999 and 4999)
2. 4 + 6 + 8 + 9 (composite numbers): 9998 (4999 and 4999)
3. 4 − 6 + 8 − 9 (composite numbers with flipping signs): 9998 (4999 and 4999)
4. 0 + 1 + 3 + 5 + 8 + 10 (whole part of n times the natural logarithm of n): 9998 (4999 and 4999)
5. 1 + 2 + 5 + 8 + 11 (whole part of n times the root of n): 9998 (4999 and 4999)
6. 1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2): 9927 (4999 and 4928)
7. 1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio): 9918 (4999 and 4919)
8. 1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece): 8040 (4999 and 3041)
9. 1 − 3 + 5 − 7 (odd numbers with flipping signs): 7498 (4999 and 2499)
10. 2 + 3 + 5 + 7 (primes): 5668 (4999 and 669)
11. 2 − 3 + 5 − 7 (primes with flipping signs): 5668 (4999 and 669)
12. 1 + 2 + 2 + 3 + 3 + 3 (each number n repeated n times): 5058 (4999 and 59)
13. 1 + 2 + 3 + 4 (counting numbers): 5011 (12 and 4999)
14. 1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n): 5008 (4999 and 9)
15. 1 + 4 + 1 + 5 + 9 (digits of pi): 5008 (4999 and 9)
16. 1 + 1 + 1 + 1 (steady 1): 4999 (4999 and 0)
17. 7 + 7 + 7 + 7 (steady 7): 4285 (4285 and 0)
18. 1 + 2 + 4 + 5 + 7 + 8 (numbers that are not multiples of 3): 3335 (2 and 3333)
19. 1 + 3 + 5 + 7 (odd numbers): 2500 (1 and 2499)
20. 2 + 4 + 6 + 8 (even numbers): 2499 (0 and 2499)
21. 1 + 8 + 27 + 64 (cubes): 1171 (1 and 1170)
22. 1 + 2 + 2 + 4 (gaps between neighboring primes): 675 (668 and 7)
23. 1 − 4 + 9 − 16 (squares with flipping signs): 373 (33 and 340)
24. 1 + 16 + 81 + 256 (fourth powers): 144 (143 and 1)
25. 1 + 1 + 2 + 3 + 5 + 8 (Fibonacci numbers): 100 (50 and 50)
26. 1 + 3 + 6 + 10 (triangular numbers): 69 (57 and 12)
27. 1 + 4 + 9 + 16 (squares): 58 (57 and 1)
28. 1 − 3 + 6 − 10 (triangular numbers with flipping signs): 34 (1 and 33)
29. 43 + 47 + 53 + 61 (the recipe n² + n + 41): 15 (15 and 0)
30. 1 + 2 + 6 + 24 + 120 (1 and 1 × 2 and 1 × 2 × 3): 2 (0 and 2)
31. 1 − 1 + 1 − 1 (steady 1 with flipping signs): 1 (1 and 0)
32. 1 + 2 + 4 + 8 + 16 (doublings): 1 (0 and 1)

## List 3: circle sizes where both circles were filled at once (out of 4999)

1. 1 − 2 + 3 − 4 (counting numbers with flipping signs): 4999
2. 4 + 6 + 8 + 9 (composite numbers): 4999
3. 4 − 6 + 8 − 9 (composite numbers with flipping signs): 4999
4. 0 + 1 + 3 + 5 + 8 + 10 (whole part of n times the natural logarithm of n): 4999
5. 1 + 2 + 5 + 8 + 11 (whole part of n times the root of n): 4999
6. 1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2): 4928
7. 1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio): 4919
8. 1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece): 3041
9. 1 − 3 + 5 − 7 (odd numbers with flipping signs): 2499
10. 2 + 3 + 5 + 7 (primes): 669
11. 2 − 3 + 5 − 7 (primes with flipping signs): 669
12. 1 + 2 + 2 + 3 + 3 + 3 (each number n repeated n times): 59
13. 1 + 1 + 2 + 3 + 5 + 8 (Fibonacci numbers): 50
14. 1 + 2 + 3 + 4 (counting numbers): 12
15. 1 + 3 + 6 + 10 (triangular numbers): 12
16. 1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n): 9
17. 1 + 4 + 1 + 5 + 9 (digits of pi): 9
18. 1 + 2 + 2 + 4 (gaps between neighboring primes): 5
19. 1 − 4 + 9 − 16 (squares with flipping signs): 2
20. 1 + 2 + 4 + 5 + 7 + 8 (numbers that are not multiples of 3): 2
21. 1 − 3 + 6 − 10 (triangular numbers with flipping signs): 1
22. 1 + 4 + 9 + 16 (squares): 1
23. 1 + 8 + 27 + 64 (cubes): 1
24. 1 + 16 + 81 + 256 (fourth powers): 1
25. 1 + 1 + 1 + 1 (steady 1): 0
26. 7 + 7 + 7 + 7 (steady 7): 0
27. 1 − 1 + 1 − 1 (steady 1 with flipping signs): 0
28. 1 + 3 + 5 + 7 (odd numbers): 0
29. 2 + 4 + 6 + 8 (even numbers): 0
30. 43 + 47 + 53 + 61 (the recipe n² + n + 41): 0
31. 1 + 2 + 4 + 8 + 16 (doublings): 0
32. 1 + 2 + 6 + 24 + 120 (1 and 1 × 2 and 1 × 2 × 3): 0

Sums with the same count are tied.

## List 4: the lower of the two percentages (out of 100)

For each circle size the score takes the lower of the two shares and then averages over all 4999 sizes. The brackets show the literal average and then the cumulative average.

1. 1 − 2 + 3 − 4 (counting numbers with flipping signs): 100.0 (100.0 and 100.0)
2. 4 + 6 + 8 + 9 (composite numbers): 100.0 (100.0 and 100.0)
3. 4 − 6 + 8 − 9 (composite numbers with flipping signs): 100.0 (100.0 and 100.0)
4. 0 + 1 + 3 + 5 + 8 + 10 (whole part of n times the natural logarithm of n): 100.0 (100.0 and 100.0)
5. 1 + 2 + 5 + 8 + 11 (whole part of n times the root of n): 100.0 (100.0 and 100.0)
6. 1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2): 99.8 (99.8 and 100.0)
7. 1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio): 99.7 (99.7 and 100.0)
8. 1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece): 92.4 (92.4 and 100.0)
9. 1 − 3 + 5 − 7 (odd numbers with flipping signs): 68.7 (68.7 and 100.0)
10. 2 + 3 + 5 + 7 (primes): 61.1 (61.1 and 100.0)
11. 2 − 3 + 5 − 7 (primes with flipping signs): 61.1 (61.1 and 100.0)
12. 1 − 3 + 6 − 10 (triangular numbers with flipping signs): 43.2 (54.5 and 43.4)
13. 1 + 2 + 4 + 5 + 7 + 8 (numbers that are not multiples of 3): 39.5 (88.9 and 39.5)
14. 1 − 4 + 9 − 16 (squares with flipping signs): 35.0 (38.1 and 54.5)
15. 1 + 2 + 3 + 4 (counting numbers): 33.6 (100.0 and 33.6)
16. 1 + 3 + 6 + 10 (triangular numbers): 33.6 (33.6 and 55.2)
17. 1 + 1 + 2 + 3 + 5 + 8 (Fibonacci numbers): 31.3 (31.3 and 31.3)
18. 1 + 4 + 9 + 16 (squares): 27.8 (27.8 and 55.2)
19. 1 + 3 + 5 + 7 (odd numbers): 27.8 (75.0 and 27.8)
20. 2 + 4 + 6 + 8 (even numbers): 24.7 (75.0 and 24.7)
21. 43 + 47 + 53 + 61 (the recipe n² + n + 41): 24.7 (24.7 and 51.1)
22. 1 + 2 + 2 + 3 + 3 + 3 (each number n repeated n times): 20.7 (20.7 and 100.0)
23. 1 + 2 + 4 + 8 + 16 (doublings): 19.9 (20.0 and 19.9)
24. 1 + 16 + 81 + 256 (fourth powers): 19.0 (19.0 and 57.2)
25. 1 + 8 + 27 + 64 (cubes): 18.4 (49.5 and 18.9)
26. 1 + 2 + 6 + 24 + 120 (1 and 1 × 2 and 1 × 2 × 3): 15.1 (15.5 and 15.3)
27. 1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n): 4.6 (4.6 and 100.0)
28. 1 + 2 + 2 + 4 (gaps between neighboring primes): 4.1 (4.1 and 61.0)
29. 1 + 4 + 1 + 5 + 9 (digits of pi): 1.4 (1.4 and 100.0)
30. 1 − 1 + 1 − 1 (steady 1 with flipping signs): 0.3 (0.3 and 0.3)
31. 1 + 1 + 1 + 1 (steady 1): 0.2 (0.2 and 100.0)
32. 7 + 7 + 7 + 7 (steady 7): 0.2 (0.2 and 87.8)

## Question: what do the counts in the lists match?

- The primes filled both circles on 669 sizes and there are 669 primes up to 5000. The page before this one shows that the primes fill the literal circle only when the number of marks is a prime.
- The counting numbers filled the cumulative circle on 12 sizes and there are 12 powers of 2 from 2 to 4096. The running totals of the counting numbers fill a circle only when the number of marks is a power of 2.
- The numbers with no repeated prime piece filled the literal circle on 3041 sizes and those are exactly the 3041 circle sizes from 2 to 5000 that themselves have no repeated prime piece. The program compared the sizes one by one.
- The odd numbers with flipping signs filled the literal circle on 2499 sizes and those are exactly the 2499 odd sizes from 3 to 4999.
- The steady sum 7 + 7 + 7 + 7 filled the cumulative circle on 4285 sizes which is every size that 7 does not divide.

## Question: does the whole part of n times the natural logarithm of n need decimals?

Yes in the middle of the calculation. The recipe multiplies n by the natural logarithm of n and then drops everything after the decimal point. So 2 gives 1.386 and the term is 1. Then 3 gives 3.296 and the term is 3. Then 4 gives 5.545 and the term is 5. Then 5 gives 8.047 and the term is 8.

The n-th prime is close to n times the natural logarithm of n which is a proven fact about how the primes thin out. So this sum is a smooth imitation of the primes that grows at the pace of the primes. The imitation filled the literal circle on all 4999 sizes and the primes filled the literal circle on 669 sizes. The imitation is free to land on even marks and a prime above 2 is not. So the gap between 4999 and 669 belongs to the sieve and not to how fast the primes grow.

## Question: did dropping the decimals create a randomness as good as the primes?

The chopped sum covered the marks as well as the primes on the cumulative circle and better than the primes on the literal circle. But the chopped sum is not random. The gaps between neighboring terms are 1 and 2 and 2 and 3 and 2 and 3 and the gaps creep upward slowly. So the arrow sweeps around the circle at a speed that changes a tiny bit on each lap and each lap lands slightly offset from the lap before. Anyone can work out the millionth term with a calculator.

On 1000 marks the chopped sum filled the cumulative circle in 5850 steps and the primes needed 8348 steps and random drops would need about 6908.

So "fills every circle" is a weak test of randomness because a fully predictable sum passes the test. The tests on the earlier pages where the primes looked special were the sharp pitches and the last digits of neighboring primes.

The chatbot recalls that mathematicians have proven that the whole parts of smooth slowly bending recipes of this kind spread evenly over the marks of any circle but the chatbot did not look up a source for this exact recipe.

## Question: what does "30 steps for each mark" mean and which sums does the limit treat unfairly?

A sum such as the primes never ends so the program has to stop somewhere and count. One step is one term used once. Each sum got 30 times as many steps as the circle has marks. Random drops need about "the natural logarithm of the number of marks" steps for each mark which is about 8.5 for 5000 marks so 30 is more than three times what random drops need. The number 30 is the chatbot's choice and not a standard.

The limit lowers the literal scores of sums whose terms grow slowly because the arrow on the literal circle cannot reach a mark larger than the largest term seen so far. The sum 1 + 2 + 2 + 3 + 3 + 3 reaches only the term 547 after 150000 steps so that sum cannot land on marks 548 to 4999 of a circle with 5000 marks inside the limit. The digits of pi and the number of divisors of n are held back the same way. The two sums built from the root of 2 and the golden ratio missed a few marks on 71 and 80 sizes and more steps might fill those sizes.

The limit makes no difference for sums that repeat on a circle such as the counting numbers and the squares and the cubes and the Fibonacci numbers and the doublings.

## Question: how do the digits of e and the golden ratio and square roots score?

The test used the digits after the decimal point of pi and e and the golden ratio and the roots of 2 and 3 and 5 and 7 and the natural logarithm of 2. Each constant was used two ways.

**One digit at a time.** Every one of the eight constants scored the same: 100.0 on the cumulative circle and 1.4 on the literal circle for a total of 101.4 out of 200. A digit is 0 to 9 so the arrow on the literal circle can reach at most 10 marks and the literal circle was filled only on the 9 sizes from 2 to 10. Digits from a random number generator scored the same 101.4.

**Four digits at a time.** The digits were cut into blocks of four so e gives 7182 and 8182 and 8459. Every one of the eight constants filled both circles on all 4999 sizes for a total of 200.0. Blocks from a random number generator scored the same 200.0.

Two controls:

- 1 divided by 7 has the repeating digits 142857. One digit at a time scored 95.5 (the cumulative circle was filled on 4444 sizes). Four digits at a time scored 79.0 because the blocks repeat after three blocks.
- The counting numbers written in a line (123456789101112) scored 101.4 one digit at a time and 200.0 four digits at a time though the cumulative circle was left unfilled on 86 sizes.

So the digits of these constants behaved like random digits in this test and no constant stood out from another. The test cannot tell e from the golden ratio or from a random number generator. What decides the score is how large the terms are allowed to be and not which constant the digits belong to.

## Question: what stands out so far?

**The literal circle works like a mirror.** A sum fills the literal circle on the circle sizes that are the same kind of number as the terms of the sum. The primes filled exactly the circles with a prime number of marks. The numbers with no repeated prime piece filled exactly the circles whose size has no repeated prime piece. The odd numbers with flipping signs filled exactly the circles with an odd number of marks. The program compared these size by size from 2 to 5000 and found no exception. The reason is the sieve: a circle size blocks the marks that share a forbidden piece with the size so only a size free of that piece leaves every mark open.

**Filling a circle measures steady drift and not randomness.** A sum that anyone can predict with a calculator (the whole part of n times the natural logarithm of n) filled every circle under both rules and the primes did not. So a full circle says the terms keep shifting their remainders and says nothing about whether the terms are unpredictable.

**The two rules are one rule a level apart.** The running totals of one sum are the terms of another sum. That is the same ladder as the earlier pages where a logarithm takes multiplying down to adding and where dividing each term by the running total takes a sum down one rung.

**Flipping signs repairs the counting numbers.** 1 + 2 + 3 + 4 fills the cumulative circle only on powers of 2 and 1 − 2 + 3 − 4 fills every circle under both rules and was the fastest sum tested. On the earlier pages the same flipped sum was the one that settles to 1/4 while the unflipped sum needs the −1/12 treatment. The chatbot sees a resemblance there (backward steps cancel the pile-up in both settings) and has not shown that the two facts are linked by a proof.

**The digits of the constants could not be told apart.** Pi and e and the golden ratio and four square roots and the natural logarithm of 2 gave the same scores as a random number generator. Mathematicians widely expect the digits of these constants to behave like random digits and nobody has proven that for any of these eight constants. This test agrees with the expectation and does not prove the expectation.

**What the tests did not find.** Nothing here gives a shortcut for predicting the next prime. The circle tests show where the primes cannot land (the sieve) and show that the running total of the primes drifts as freely as many predictable sums do.

## How the questions tie back to the lists

- The recipe n² + n + 41 ranks high for primes on the master lists and scored 75.8 out of 200 here and filled both circles on no size. Being rich in primes and filling a circle are separate properties.
- The primes scored 161.1 out of 200: a full cumulative circle and a literal circle held to 61.1% on average by the sieve.

## Numbers that this page adds to the list in Part 7

56. 161.1 out of 200 is the score of the primes when the average share of the cumulative circle (100.0%) and the literal circle (61.1%) are added over circle sizes 2 to 5000.
57. 30 is the number of steps for each mark that the ranking test allowed.
58. 101.4 out of 200 is the score of the digits of every tested constant taken one digit at a time.
