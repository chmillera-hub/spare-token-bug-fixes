# Questions about digit blocks and polynomials and Collatz paths on the two circles

> **About this page:** One AI model (Claude) wrote this page on 23 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the fourteen earlier question pages in this folder (the last one is [rank-questions.md](rank-questions.md)). The author proposed each test and each rule change on this page: reading digits in blocks sized to the circle and trying polynomials and trying sequences from the Collatz rule and starting a sequence over when the sequence ends. The scores are measurements from the programs in the folder boring-things/research-program-files/prime-richness-scripts/block-scripts. The page claims no new result and says nothing about whether the Collatz conjecture is true. No other person has reviewed the page yet.

## The two circles and the score

A sequence of whole numbers feeds two circles one term at a time. On the "cumulative" circle each term moves the arrow that many marks so the arrow shows the running total. On the "literal" circle the arrow lands on the mark with the same number as the term after full turns are removed.

Each test on this page uses every circle size from 2 marks to 5000 marks which is 4999 sizes. The score of a sequence is the average share of the cumulative circle that the sequence reached plus the average share of the literal circle. A sequence that covers all of both circles on every size scores 200. Unless a section says otherwise each sequence got 30 steps for each mark on the circle.

The file [spin-animation.html](spin-animation.html) in this folder shows the two circles side by side for 106 sequences including the digit blocks and the polynomials and the Collatz sequences from this page.

## Question: what if a sequence of single digits is read in blocks at least as large as the circle?

On the page before this one the digits of pi one digit at a time scored 101.4 out of 200. A digit is 0 to 9 so the literal arrow could never reach mark 10 or higher.

The author's rule: read as many digits at a time as the number of marks is written with. A circle of 2 to 9 marks reads 1 digit at a time. A circle of 10 to 99 marks reads 2 digits at a time. A circle of 100 to 999 marks reads 3 digits at a time so pi on 360 marks gives 141 and then 592 and then 653. A circle of 1000 to 5000 marks reads 4 digits at a time. Both circles get the same blocks.

Scores under the rule:

- The digits of pi and e and the golden ratio and the roots of 2 and 3 and 5 and 7 and the natural logarithm of 2 each scored 200.0 and filled both circles on all 4999 sizes.
- Digits from a random number generator scored 200.0.
- The counting numbers written in a line (123456789101112) scored 200.0.
- 1 + 1 + 1 + 1 read as 11 or 111 or 1111 scored 88.3 (cumulative 88.1% and literal 0.2%).
- The digits of 1 divided by 7 (the six digits 142857 repeat) scored 79.5 (cumulative 79.1% and literal 0.5%).
- 7 + 7 + 7 + 7 read as 77 or 777 or 7777 scored 77.5.
- 1 + 2 + 1 + 2 read as 12 or 121 and 212 or 1212 scored 58.4.

## Question: what does the block rule show?

**The literal circle becomes a test for digits that never cycle.** A fraction has digits that repeat forever so the blocks repeat too. The literal circle can never reach more marks than the number of different blocks in one cycle. So every fraction fails on a large enough circle.

**Filling the literal circle on every size forever would mean every string of digits shows up.** To hit every mark on larger and larger circles the digits have to keep producing every possible block. The counting numbers written in a line pass because that line is built to contain every number. Nobody has proven that every string of digits shows up in pi or e or a square root. The test up to 5000 marks agrees with what mathematicians expect and does not prove the expectation.

**The steady sequence now depends on the prime pieces of 11 and 111 and 1111.** A steady move fills the cumulative circle only when the move shares no prime piece with the number of marks. 11 is a prime. 111 is 3 × 37. 1111 is 11 × 101. So 1 + 1 + 1 + 1 under the block rule filled the cumulative circle on 4274 of 4999 sizes where the plain 1 + 1 + 1 + 1 filled all 4999.

## Question: how do polynomials score?

The terms are the polynomial at x = 1 and 2 and 3 and onward. A polynomial repeats on a circle so each polynomial was run for one full cycle of the running total which makes the counts exact with no step limit. The test covered 34 polynomials.

The highest scores (cumulative average and then literal average in brackets):

1. x with flipping signs which is 1 − 2 + 3 − 4: 200.0 (100.0 and 100.0)
2. x: 133.6 (33.6 and 100.0)
3. 3x + 1: 117.5 (39.7 and 77.8)
4. 2x + 1: 102.8 (27.8 and 75.0)
5. x⁷: 95.3 (20.7 and 74.6)
6. x² with flipping signs: 92.6 (54.5 and 38.1)
7. x³ with flipping signs: 91.5 (42.0 and 49.5)
8. 6x + 1: 91.2 (32.8 and 58.3)
9. x³ + x² + x + 1: 87.6 (42.2 and 45.4)
10. 6x² + x: 87.0 (47.3 and 39.7)

The pure powers:

- x²: 83.0 (55.2 and 27.8)
- x³: 68.4 (18.9 and 49.5)
- x⁴: 76.2 (57.2 and 19.0)
- x⁵: 86.0 (20.9 and 65.2)
- x⁶: 69.9 (53.6 and 16.4)
- x⁷: 95.3 (20.7 and 74.6)

Other polynomials: 2x² + x scored 85.9 and x³ + x + 1 scored 85.9 and x² + 1 scored 85.1 and x³ + x with flipping signs scored 81.8 and 30x⁵ + x scored 81.4 and x² + x + 1 with flipping signs scored 80.3 and 6x³ + x scored 78.3 and x² + x + 1 scored 76.1 and x² + x + 41 scored 75.8 and 2x² + 1 scored 73.7 and x⁴ + x scored 73.0 and x² + x scored 65.6 and 3x² + x scored 65.3 and 2x³ + x scored 63.4 and x⁵ + x scored 58.9 and 3x³ + x scored 57.7 and x³ + x scored 57.7.

The lowest scores: x³ − x scored 46.2 (14.9 and 31.3) and x⁵ − x scored 38.9 (14.2 and 24.7).

## Question: what stands out among the polynomials?

- No polynomial beat plain x and the one sequence that reached 200 was x with flipping signs.
- Odd powers and even powers swap strengths. The odd powers x³ and x⁵ and x⁷ filled the literal circle on 1170 and 2065 and 2483 sizes. The even powers x² and x⁴ and x⁶ filled the literal circle only on a circle of 2 marks. An even power sends a number and the negative of that number to the same mark so two marks collide and some mark stays empty.
- The even powers were stronger on the cumulative circle where x² and x⁴ and x⁶ filled 57 and 143 and 123 sizes while each odd power filled 1 size.
- x³ − x is always a multiple of 6 and x⁵ − x is always a multiple of 30 so the literal arrow can land only on a thin set of marks.
- Five mixed polynomials filled both circles on exactly the 12 powers of 2 from 2 to 4096 which is the same as plain x: 2x² + x and 6x² + x and 2x³ + x and 6x³ + x and 30x⁵ + x.
- x³ + x with flipping signs filled both circles on exactly the powers of 3 which are 3 and 9 and 27 and 81 and 243 and 729 and 2187. The chatbot has not worked out a proof for that.
- x² + x + 41 scored 75.8 and x² + x + 1 scored 76.1. The 41 that makes the recipe rich in primes made almost no difference on the circles.

## Question: how do sequences from the Collatz rule score?

The Collatz rule halves an even number and turns an odd number n into 3n + 1. Every start anyone has tried ends at 1. A "path" on this page is the list of numbers from a start down to 1.

Scores with each single path stopped at 1 (cumulative average and then literal average in brackets):

1. The single path from 2 to the power 3000 minus 1 which has 43231 terms: 186.4 (99.5 and 86.9)
2. All paths joined in a line (2 + 1 and then 3 + 10 + 5 + 16 + 8 + 4 + 2 + 1 and onward): 178.3 (100.0 and 78.3)
3. The highest number each start reaches (1 + 2 + 16 + 4 + 16 + 16 + 52): 137.2 (68.8 and 68.5)
4. The number of steps each start needs to reach 1 (0 + 1 + 7 + 2 + 5 + 8 + 16): 121.3 (100.0 and 21.3)
5. The number of odd steps for each start (0 + 0 + 2 + 0 + 1 + 2 + 5): 109.8 (100.0 and 9.8)
6. The single path from 63728127 with 950 terms: 79.4
7. The single path from 837799 with 525 terms: 55.4
8. The single path from 6171 with 262 terms: 35.0
9. The single path from 871 with 179 terms: 26.6
10. The single path from 27 with 112 terms: 18.9

What stands out:

- A Collatz path avoids multiples of 3. The long path had 1 multiple of 3 among 43231 terms and that term was the starting number. The reason: 3n + 1 always leaves a remainder of 1 when divided by 3 and halving a number that is not a multiple of 3 never gives a multiple of 3.
- So the literal circle shows a sieve by 3. On 360 marks the long path reached 239 marks where 240 marks are not multiples of 3. The long path filled the literal circle on 2495 sizes and the circle with 3 marks was the single multiple of 3 among them.
- The highest numbers are all even after the first. That sequence filled the cumulative circle on 2499 sizes which equals the count of odd sizes from 3 to 4999.
- The step counts stay small (the longest path for a start up to 150000 took 374 steps) so the literal arrow cannot reach the far marks of a large circle.

## Question: what did the single path from 27 do?

The path starts 27 and 82 and 41 and 124 and 62 and 31 and 94 and 47 and 142 and 71. The path reaches the highest value 9232 at term 78 and ends 16 and 8 and 4 and 2 and 1. The path has 112 terms and all 112 are different. 70 terms are even. The terms add up to 101440. One term is a multiple of 3 and that term is 27.

Marks reached with the path stopped at 1 (cumulative and then literal): 10 and 10 of 10 marks. 12 and 9 of 12 marks. 53 and 39 of 60 marks. 101 and 93 of 360 marks. 101 and 111 of 1000 marks. 109 and 111 of 5000 marks.

A sequence with 112 terms can light at most 112 marks so the low score reflects the short length. On 5000 marks the literal circle got 111 different marks from 112 terms so the path wasted very few steps on repeats. The largest circle the path filled under both rules had 41 marks.

## Question: what if a sequence that ends starts over from the first term?

Scores with each single path looped (and the score with the path stopped at 1 after each one):

- Path from 27: 108.5 (18.9 stopped). Cumulative average 99.0% and literal average 9.5%.
- Path from 871: 113.1 (26.6 stopped).
- Path from 6171: 117.1 (35.0 stopped).
- Path from 837799: 126.6 (55.4 stopped).
- Path from 63728127: 138.1 (79.4 stopped).
- Path from 2 to the power 3000 minus 1: 186.4 both ways because that path rarely starts over inside the step limit.

Looping lifted the cumulative circle and left the literal circle unchanged. One full pass through the path from 27 adds up to 101440 so each new pass draws the same 112-step shape again from a shifted starting spot. The literal arrow lands on the term itself so a second pass lands on the same 112 marks as the first pass.

The looped path from 27 filled the cumulative circle on 4796 of 4999 sizes. The misses share one cause. The pass total 101440 is 2 × 2 × 2 × 2 × 2 × 2 × 5 × 317. A circle of 360 or 1000 or 5000 marks shares the piece 40 with the pass total so the shift between passes moves the shape in jumps of 40 marks and the shape covers 38 of the 40 positions inside a jump. The counts match: 342 of 360 marks and 950 of 1000 marks and 4750 of 5000 marks are each 38/40 of the circle. A circle of 361 or 4999 marks shares no piece with the pass total and was filled.

## Question: what do the sequences with scores near 200 have in common?

1. The terms have no divisibility habit. Each sequence that fell short has a named habit: the primes avoid sharing a prime piece with the circle size and the numbers with no repeated prime piece avoid multiples of 4 and 9 and a Collatz path avoids multiples of 3 and an even power sends a number and the negative of that number to the same mark.
2. The terms get at least as large as the circle. Single digits and Collatz step counts stay small.
3. The sequence does not fall into a short loop on the circle. Every polynomial repeats and leaves fixed gaps. The one exception is 1 − 2 + 3 − 4 which repeats only after a complete tour of every mark.
4. The gaps between terms keep changing so the running total keeps shifting by a different amount.
5. The growth is moderate. Growth that is too slow fails on size and growth that is too fast falls into a short loop.

There were two roads to 200. One is an exact design: 1 − 2 + 3 − 4 is fully regular and the backward steps make the running total swing 1 and −1 and 2 and −2. The other is even spreading through drifting or irregular gaps.

A high score did not need randomness or primes or a famous constant. These five properties are what the tests showed and the chatbot has not proven that the five together guarantee a score of 200.

## Question: what do the sequences with the lowest scores have in common?

The lowest scores once looping and the block rule are applied:

1. 1 − 1 + 1 − 1: 0.6
2. 1 and 1 × 2 and 1 × 2 × 3: 30.8
3. x⁵ − x: 38.9
4. The doublings 1 + 2 + 4 + 8: 39.9
5. x³ − x: 46.2
6. x³ + x: 57.7
7. The Fibonacci numbers: 62.5
8. The gaps between neighboring primes: 65.1
9. The cubes: 68.4
10. x⁶: 69.9
11. 7 + 7 + 7 + 7 read as 77 or 777 or 7777: 77.5
12. The digits of 1 divided by 7 in blocks: 79.5

The patterns:

- A tiny loop. 1 − 1 + 1 − 1 bounces between two marks on both circles.
- A collapse onto one mark. 1 × 2 × 3 soon contains every number up to the circle size as a factor so every later term is a whole number of full turns.
- Growth by multiplying. The doublings can reach only the marks that are a power of 2 with full turns removed which is 15 of 360 marks.
- No rescue from the cumulative circle. The running total of the doublings is the next doubling minus 1 and the running total of the Fibonacci numbers is a later Fibonacci number minus 1. So the cumulative circle shows the literal marks slid back by one mark. The doublings scored 19.9 and 20.0 on the two circles and the Fibonacci numbers scored 31.3 and 31.3.
- A factor in every term such as the 6 in x³ − x.

The short Collatz paths left the bottom of the list once looping was allowed. A flaw of length or of size can be repaired by looping or by blocks. A flaw of cycling or multiplying or a built-in factor cannot.

## Question: what if any sequence is written as one line of digits and read in blocks?

This goes beyond the author's rule and was the chatbot's own extra test. Each sequence was written out as one long line of digits and the line was read in blocks sized to the circle. The doublings become the line 1248163264128 and a circle of 360 marks reads 124 and then 816 and then 326.

- The doublings written in a line: 200.0 (39.9 as plain doublings)
- The Fibonacci numbers written in a line: 200.0 (62.5 plain)
- The primes written in a line: 200.0 (161.1 plain)
- Collatz step counts written in a line: 198.5 (121.3 plain)
- Collatz odd step counts written in a line: 197.5 (109.8 plain)
- The gaps between primes written in a line: 157.8 (65.1 plain)
- The number of divisors written in a line: 156.1 (104.6 plain)
- Each number n repeated n times written in a line: 133.4 (120.7 plain)

Writing a sequence as a line of digits erased the multiplying flaw because the blocks are no longer doublings or Fibonacci numbers. So this version tests the digits of a sequence and no longer tests the sequence itself. The prime gaps stayed lowest because nearly every gap is even so the line is heavy with the digits 2 and 4 and 6 and 8.

## How the questions tie back to the lists

- The recipe x² + x + 41 ranks high for primes on the master lists. On the circles the recipe scored within 0.3 of x² + x + 1 so prime richness and circle coverage stayed separate properties in this test too.
- The literal circle again exposed a divisibility habit that the cumulative circle hid: the sieve for the primes on the earlier pages and the missing multiples of 3 for a Collatz path here.

## Numbers that this page adds to the list in Part 7

59. 101440 is the sum of the 112 terms of the Collatz path from 27 and equals 2 × 2 × 2 × 2 × 2 × 2 × 5 × 317.
60. 4274 is the number of circle sizes from 2 to 5000 that share no prime piece with the block 11 or 111 or 1111 used on that size.
61. 2483 is the number of circle sizes from 2 to 5000 on which x⁷ fills the literal circle.
62. 186.4 out of 200 is the score of the Collatz path from 2 to the power 3000 minus 1.
