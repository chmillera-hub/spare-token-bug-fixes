# Do prime-rich equations stay prime-rich at hundreds of digits

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each result comes from a computer count and not from a written proof unless the section says a proof exists.

## What the page answers

A percentage measured on small outputs could in principle fall apart on long outputs. The page tests whether an equation that beats the number line on outputs of about 12 digits still beats the number line by the same factor on outputs of 100 and 300 and 1000 digits. The short answer from the tests below is yes for equations in n.

## The test at 100 and 300 digits

Each equation was fed random inputs sized so the outputs have about 100 digits (40000 tests) and about 300 digits (20000 tests). The share is the share of the tested outputs that were prime.

- n: +10% at about 100 digits (191 primes in 40000 tests which is a share of 0.48%) and +10% at about 300 digits (32 primes in 20000 tests which is a share of 0.16%)
- 2n + 1: +108% at about 100 digits (361 primes in 40000 tests which is a share of 0.90%) and +104% at about 300 digits (59 primes in 20000 tests which is a share of 0.29%)
- 510510 × n + 1: +467% at about 100 digits (934 primes in 40000 tests which is a share of 2.33%) and +434% at about 300 digits (152 primes in 20000 tests which is a share of 0.76%)
- n² + n + 41: +593% at about 100 digits (1212 primes in 40000 tests which is a share of 3.03%) and +538% at about 300 digits (185 primes in 20000 tests which is a share of 0.93%)
- 36n² − 810n + 2753: +680% at about 100 digits (1342 primes in 40000 tests which is a share of 3.35%) and +676% at about 300 digits (224 primes in 20000 tests which is a share of 1.12%)
- n² + n + 26853927251: +829% at about 100 digits (1625 primes in 40000 tests which is a share of 4.06%) and +800% at about 300 digits (261 primes in 20000 tests which is a share of 1.30%) and +1097% at about 1000 digits (13 primes in 2500 tests which is a share of 0.52%)
- −66n³ + 3845n² − 60897n + 251831: +769% at about 100 digits (1512 primes in 40000 tests which is a share of 3.78%) and +794% at about 300 digits (258 primes in 20000 tests which is a share of 1.29%)
- n⁶ + 1091: −94% at about 100 digits (12 primes in 40000 tests which is a share of 0.03%) and −100% at about 300 digits (0 primes in 20000 tests which is a share of 0.00%)

The wobble from luck is about 25 points at 100 digits for the top equations and about 55 points at 300 digits so the small shifts between the two sizes are inside the wobble. The plain number line itself measured +10% at both sizes which shows how far luck alone can move a line. The single test at 1000 digits found 13 primes where chance predicts 1.1 which is rough and fits the +800% to +860% measured at the smaller sizes.

## The match between small outputs and 100-digit outputs for 37 equations

Each line gives the percentage on the first 100000 inputs and then the percentage on 40000 random inputs with outputs of about 100 digits.

- n: 0% small and −1% at 100 digits
- 2n + 1: +99% small and +84% at 100 digits
- 6n + 1: +199% small and +208% at 100 digits
- 30n + 1: +274% small and +281% at 100 digits
- 210n + 1: +336% small and +325% at 100 digits
- 510510n + 1: +454% small and +464% at 100 digits
- n² + 1: +38% small and +45% at 100 digits
- n² + n + 1: +123% small and +127% at 100 digits
- n² − n − 1: +255% small and +277% at 100 digits
- n² − 2: +85% small and +81% at 100 digits
- n² + 3: +13% small and +5% at 100 digits
- 2n² − 1: +269% small and +260% at 100 digits
- 4n² + 1: +175% small and +171% at 100 digits
- 3n² + 3n + 1: +234% small and +230% at 100 digits
- n² + n + 17: +318% small and +300% at 100 digits
- 2n² + 29: +492% small and +504% at 100 digits
- n² + n + 41: +564% small and +578% at 100 digits
- n² + n + 27941: +631% small and +663% at 100 digits
- n² + n + 247757: +728% small and +733% at 100 digits
- n² + n + 26853927251: +859% small and +837% at 100 digits
- 36n² − 810n + 2753: +684% small and +710% at 100 digits
- 103n² − 4707n + 50383: +703% small and +692% at 100 digits
- 249582n² + 1: +694% small and +697% at 100 digits
- n² + n − 501229: +698% small and +661% at 100 digits
- n³ + 2: +26% small and +28% at 100 digits
- n³ + n + 1: +208% small and +215% at 100 digits
- n³ − n + 1: +248% small and +255% at 100 digits
- 3n³ − 183n² + 3318n − 18757: +616% small and +626% at 100 digits
- −66n³ + 3845n² − 60897n + 251831: +748% small and +738% at 100 digits
- n⁴ + 1: +166% small and +165% at 100 digits
- n⁴ + n + 1: +154% small and +162% at 100 digits
- n⁴ − n² + 1: +367% small and +347% at 100 digits
- n⁴ + n³ + n² + n + 1: +191% small and +185% at 100 digits
- n⁵ + 2: +17% small and +20% at 100 digits
- n⁶ + 1091: −97% small and −95% at 100 digits
- n⁸ + 1: +108% small and +110% at 100 digits
- n¹⁶ + 1: +265% small and +293% at 100 digits

The correlation between the two columns is 0.999 on a scale where 1.000 is a perfect match and the rank correlation is 0.996. The largest gap among the 37 equations is 37 points.

Scoring each equation on the first 20 inputs alone drops the correlation with the 100-digit result to 0.88 because 20 inputs leave too much room for luck.

## Why the match is tight

The percentage of an equation is set by which small primes can divide the outputs. For example 6n + 1 is never a multiple of 2 or 3 whether n has 2 digits or 200 digits. The match is a standard prediction in number theory that has no proof yet and the tables above are one more check of the prediction.

## How far small-prime blocking can go

Multiplying n by the product of every prime up to p and adding 1 blocks every prime up to p. The measured factors were 5.6 times the number line for p = 17 and 8.3 times for p = 97 and 11.3 times for p = 541 and 12.1 times for p = 1009 (300000 tests each). The factor grows like 1.78 times the natural logarithm of p which predicts about 25 times for p near 1 million and about 37 times for p near 1 billion. Reaching 100 times the number line would need every prime blocked up to a number of about 24 digits and no multiplier that long can be written down.

## Program files

The files big_digits.py and low_high.py and primorial_line.py in the folder boring-things/research-program-files/prime-richness-scripts rerun every count on this page.
