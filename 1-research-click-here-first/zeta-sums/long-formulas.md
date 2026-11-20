# Written-out sum formulas for zeta(5) and zeta(7) and zeta(9) plus the search records

> **About this page:** One AI model (Claude) ran a computer search on 20 November 2026 and wrote this page. The same day a second run recomputed every formula on this page independently. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer.

## What this page holds and what this page leaves out

This page holds only the parts of the search that a reader could not find with a quick web search on 20 November 2026 which means the four formulas with their exact whole-number coefficients and the three near-miss coincidences and the list of searches that found nothing.

This page leaves out the well-known formulas for these numbers because standard reference pages already print those formulas.

The formulas below are not new theorems because formulas of this ladder shape belong to families that are already in the published mathematical record. What appears to be missing from easy-to-find sources is each formula written out in full with every coefficient so that a reader can type the formula straight into a program.

The page named zeta3-golden.md in this folder holds a follow-up search that found shorter formulas for zeta(5) and zeta(7) and two formulas for zeta(3).

## Notation

zeta(5) means 1/1^5 + 1/2^5 + 1/3^5 and so on forever and zeta(7) and zeta(9) use the powers 7 and 9 in the same way.

phi = (1 + sqrt(5))/2 which is the golden ratio near 1.618.

r = 1/phi which is near 0.618.

l = ln(phi) which is the natural logarithm of the golden ratio.

F(x) means the sum of x^n/n^s for n = 1 and 2 and 3 and so on forever. The number s is 5 inside a zeta(5) formula and 7 inside a zeta(7) formula and 9 inside a zeta(9) formula.

The sign × means multiplication.

## Formula 1: zeta(5) with the golden ratio

268 × zeta(5) = 432 × F(r^2) - 675 × F(r^4) + 1216 × F(r^6) - 648 × F(r^8) - 144 × F(r^10) - 136 × F(r^12) + 9 × F(r^20) + 4 × F(r^24) + 4 × pi^4 × l - 32 × pi^2 × l^3 + 192 × l^5

## Formula 2: zeta(7) with the golden ratio

698535 × zeta(7) = 1881360 × F(r^2) - 2467260 × F(r^4) + 1825920 × F(r^6) - 459270 × F(r^8) - 69120 × F(r^10) - 45900 × F(r^12) + 1080 × F(r^20) + 315 × F(r^24) + 93504 × l^7 - 19392 × pi^2 × l^5 + 832 × pi^4 × l^3 + 536 × pi^6 × l

## Formula 3: zeta(9) with the golden ratio

125596001790 × zeta(9) = 220857840000 × F(r^2) - 143129581875 × F(r^4) + 58302720000 × F(r^6) - 9300217500 × F(r^8) - 855671040 × F(r^10) - 393750000 × F(r^12) + 3342465 × F(r^20) + 708750 × F(r^24) + 2364192000 × l^9 - 1022976000 × pi^2 × l^7 + 258249600 × pi^4 × l^5 - 55329600 × pi^6 × l^3 + 14149132 × pi^8 × l

## Formula 4: zeta(5) with powers of one half

403 × zeta(5) = 576 × F(1/2) - 162 × F(1/4) - 16 × F(1/8) + F(1/64) + (8/3) × pi^4 × ln(2) - 4 × pi^2 × ln(2)^3 + 6 × ln(2)^5

The same powers-of-one-half search found no formula for zeta(7) so the golden ratio family reached further than the one-half family in these runs.

## How well the four formulas were checked

The second run computed the left side and the right side of each of the four formulas with 1560 digits of working precision and the two sides agreed to more than 1500 digits in every case.

A match of 1500 digits is overwhelming numerical evidence but a numerical match is not a written proof.

## How fast the sums shrink

Each sum F shrinks fast because each sum is built from powers of a number smaller than 1.

As a measured example 40 terms of each sum in Formula 1 give a value that differs from zeta(5) by about 1.5 × 10^-25 which means 24 decimal places match.

## Three near misses that are coincidences

gamma below is the constant near 0.5772 that measures the gap between the harmonic series and the natural logarithm. G below is the constant near 0.9160 that equals 1 - 1/9 + 1/25 - 1/49 and so on.

63/(19 × pi^2 × gamma^2) lands within 0.000000014 of zeta(7) and the match breaks at the 8th decimal so the guess is a coincidence.

(55/78) × e^2 × gamma^3 lands within 0.00000004 of zeta(9) and the match breaks at the 8th decimal so the guess is a coincidence.

(100/51) × G/sqrt(3) lands within 0.0000003 of zeta(5) and the match breaks at the 7th decimal so the guess is a coincidence.

The second run measured the three gaps again and found the same sizes.

## Searches that found nothing

The method was an integer relation search which is a procedure that takes a list of numbers and hunts for whole-number coefficients that make the weighted total equal exactly zero. The second run did not repeat the searches in this section because each search covers an enormous number of coefficient combinations which means this section rests on the first run alone.

zeta(3) and zeta(5) and zeta(7) and zeta(9) are not equal to a fraction times the matching power of pi for whole numbers up to one trillion.

zeta(5) and zeta(7) and zeta(9) are not roots of a polynomial up to degree 12 with whole-number coefficients up to one million.

No product of powers of pi and e and 2 and 3 and 5 and 7 and gamma and ln(2) and phi and zeta(3) and G and the gamma function at 1/4 and the gamma function at 1/3 equals zeta(5) or zeta(7) or zeta(9) with exponents up to 10000.

zeta(5) is not a sum of pairwise products of pi and e and gamma and ln(2) and zeta(3) and G and sqrt(2) with coefficients up to 2000.

No mix of e^pi and e^(-pi) and pi × e^pi and e^(2 × pi) and e^(-2 × pi) and pi and sqrt(2) and sqrt(3) and sqrt(5) matched zeta(5) with coefficients up to one million.

zeta(9) is not a mix of zeta(7) × pi^2 and zeta(5) × pi^4 and zeta(3) × pi^6 and zeta(3)^3 and pi^9 with coefficients up to ten billion.

zeta(5) is not a mix of zeta(3) × pi^2 and zeta(3) and zeta(3)^2 and powers of pi from pi^1 to pi^5 with coefficients up to one hundred million.

zeta(5) is not a mix of F(1/2) with s = 5 and F(1/2) with s = 4 times ln(2) and zeta(3) × ln(2)^2 and zeta(3) × pi^2 and pi^4 × ln(2) and pi^2 × ln(2)^3 and ln(2)^5 with coefficients up to ten billion.

A search does not prove that a finite closed form is impossible because a formula could use ingredients that were not included in the test.

## Where the families are published

A 1998 paper builds ladders of this kind from powers of one half and reaches zeta(11): https://arxiv.org/abs/math/9803067

A 2000 paper describes a golden ratio ladder that reaches zeta(9): https://arxiv.org/abs/hep-th/0004153

A reading of both papers on 20 November 2026 did not find the exact coefficients of the four formulas above printed in either paper. That reading was done by an automated summary of long documents which could have missed a formula.
