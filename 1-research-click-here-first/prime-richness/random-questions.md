# Questions about random sequences and the fewest steps and the zeta zeros

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026 from a back and forth chat with the author of this repository that ran from 23 to 27 November 2026. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the fifteen earlier question pages in this folder (the last one is [block-questions.md](block-questions.md)). The scores and counts are measurements from the programs in the folder boring-things/research-program-files/prime-richness-scripts/random-scripts. The facts about the zeta zeros are standard mathematics and the page claims no new result. No other person has reviewed the page yet.

## The two circles and the score

A sequence of whole numbers feeds two circles one term at a time. On the "cumulative" circle each term moves the arrow that many marks so the arrow shows the running total. On the "literal" circle the arrow lands on the mark with the same number as the term after full turns are removed. Each test uses every circle size from 2 marks to 5000 marks. The score is the average share of the cumulative circle reached plus the average share of the literal circle reached so a perfect score is 200. Each sequence got 30 steps for each mark.

## How does a random sequence of numbers do on the two circles?

A random sequence scores 200 when the range of the random numbers is wider than the largest circle. The score falls when the range is narrow because the literal circle can only be hit on marks that the range reaches.

- Random whole numbers from 0 to 9999: 200.0 on each of three runs.
- Random whole numbers from 0 to 999999: 200.0.
- Random primes below 1000000: 160.9 because the primes skip every mark that shares a factor with the circle size.
- Random multiples of 3 from 0 to 999999: 155.6.
- Random whole numbers from 0 to 999: 152.2.
- Random even numbers from 0 to 999998: 150.0.
- Random whole numbers from 0 to 99: 109.8.
- Random whole numbers from 0 to 9: 101.4 because the literal circle only ever sees the marks 0 to 9.
- A random choice of +1 or −1: between 21.3 and 27.7 because the arrow on the cumulative circle wanders back and forth and covers only 13.1% of a circle with 5000 marks in 150000 steps.

Random digits from 0 to 9 reach 200.0 when the digits are read in blocks sized to the circle which is the block rule on [block-questions.md](block-questions.md).

## Is a perfect score on 4999 circle sizes strong evidence that every circle size would be filled?

A perfect score on every size from 2 to 5000 is good evidence for those sizes and weak evidence by itself for every size beyond 5000. A measurement on a finite list of sizes cannot settle a claim about every size because a sequence can have a habit that only shows on a size nobody tested. A claim about every size needs an argument about the rule of the sequence. The next answer has a rule where the reason is visible.

## Which rule fills both circles in the fewest steps?

The sequence 0 + 1 − 2 + 3 − 4 fills both circles in exactly N steps on every even circle size N from 2 to 5000. N steps is the fewest possible because each step can mark at most one new mark on each circle.

- On the literal circle the terms 0 and 1 and −2 and 3 and −4 land on a new mark each time.
- On the cumulative circle the running totals are 0 then 1 then −1 then 2 then −2 so the arrow swings one mark farther out on alternate sides.
- Without the 0 in front the sequence 1 − 2 + 3 − 4 needs 2N − 1 steps on the cumulative circle (19 steps on 10 marks and 719 steps on 360 marks).
- On an odd circle size the sequence with the 0 in front fills the cumulative circle in N steps and takes about one and a half times N steps on the literal circle (17 steps on 11 marks and 542 steps on 361 marks).
- A search of every possible sequence on small circles found that the fewest steps for both circles together is 2 on 2 marks and 4 on 3 marks and 4 on 4 marks and 6 on 5 marks and 6 on 6 marks and 8 on 7 marks. So an odd size N needed N + 1 steps in every case tried.

## Do the primes show patterns on the literal circle?

Yes. Three patterns showed up for the 5761455 primes below 100 million.

**The primes avoid marks that share a factor with the circle size.** On 360 marks only 96 marks can ever be hit by a prime larger than 5.

**Some open marks stay slightly ahead.** A mark that is the square of another open mark gets slightly fewer primes.

- On 4 marks: mark 3 got 2880950 primes and mark 1 got 2880504 and mark 3 was ahead after 99.96% of the primes.
- On 3 marks: mark 2 got 2880937 primes and mark 1 got 2880517.
- On 10 marks: mark 3 beat mark 1 by 176 and mark 7 beat mark 9 by 309.
- On 8 marks: marks 3 and 5 and 7 all beat mark 1 by between 436 and 574.
- On 360 marks: the 6 open marks that are squares averaged 59941.2 primes and the other 90 open marks averaged 60020.1.

This lean is a known effect in the study of primes and the page only measures the effect.

**Two primes in a row avoid landing on the same mark.**

- On 10 marks an even spread would repeat the mark 25.00% of the time and the primes repeat 17.18% of the time.
- On 3 marks an even spread would repeat 50.00% of the time and the primes repeat 43.89% of the time.
- On 30 marks an even spread would repeat 12.50% of the time and the primes repeat 4.43% of the time.
- After a prime that ends in 1 the next prime ends in 1 only 17.7% of the time and ends in 3 in 30.39% and ends in 7 in 31.03% and ends in 9 in 20.87%.
- The avoidance fades slowly as the primes grow: 11.85% repeats for primes below 10000 and 15.35% below 1000000 and 17.18% below 100000000.

This avoidance is also a known effect and the page only measures the effect.

## What is the sum of one over the height of each zero of the zeta function?

The sum of 1 divided by the height of each zero on the critical line grows without limit and grows very slowly. The program found 4520 zeros below height 5000 which matches the standard counting formula (about 4520.3).

- The sum over the first 10 zeros is 0.33655.
- The sum over the first 100 zeros is 1.03114.
- The sum over the first 1000 zeros is 2.32103.
- The sum over all 4520 zeros below height 5000 is 3.53295.
- The sum tracks the square of the natural logarithm of (height divided by 2π) divided by 4π with a steady gap near −0.017.
- By that formula the sum reaches 5 near a height of 2π times e to the power 7.9 and reaches 10 near 2π times e to the power 11.2.

The sum of 1 divided by the square of each height does settle on a limit. The closely related sum of 1 divided by (one quarter plus the height squared) has the known exact value 1 + 0.5772/2 − ln(4π)/2 = 0.0230957 where 0.5772 is the Euler constant. The program reached 0.0230924 from 4520 zeros plus an estimate for the rest.

## How does the number of zeros compare with the number of primes and composites?

The zeros get more crowded with height while the primes get more spread out.

- Near height 20 the average gap between zeros is about 5.43 and near height 5000 the gap is about 0.94.
- The count of zeros below height T is close to the natural logarithm of the factorial of (T divided by 2π).
- Near 1000 there are about 0.807 zeros for each unit of height and about 0.145 primes for each unit of the number line and about 0.855 composite numbers.
- The count of zeros below T passes the count of primes below T at T = 86 and stays ahead.
- The count of zeros below T passes the count of composite numbers below T near T = 3820 (3291 zeros against 3290 composites at T = 3821). The zeros stay ahead after that because the zeros keep getting denser while the composites can never exceed one for each whole number.

The link between the two lists is the known explicit formula: each zero adds one wave to the count of primes and the height of the zero sets how fast that wave wiggles.

## How does this connect to food and shelter and deep human connection?

None of these counts feeds or houses a person. The tie is that the answers sit in public for free so a person who asks the same question does not have to pay for the answer or spend hours finding the answer. The hours saved can go toward a meal or toward rent or toward sitting with another person and hearing what is on that person's heart.

## What was not checked

- No other person has rerun the programs.
- The zeros were found by a fast method that looks for sign changes and the count matches the standard formula. The program did not prove that no zero was missed.
- The two prime effects are named in the research literature and the chatbot did not compare the measured sizes against published predictions.
