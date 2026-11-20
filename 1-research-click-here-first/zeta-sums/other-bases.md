# Sum formulas for zeta(3) and zeta(5) and zeta(7) and zeta(9) in 23 different bases

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 20 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. The formulas were checked by number matching and not by a written proof.

## What this page answers

The page named zeta3-golden.md in this folder shows that zeta(3) can be written purely as sums over powers of 1/phi where phi is the golden ratio. This page asks the next question which is whether other simple numbers work as a base in the same way and how far up each base reaches.

The main finding is that the base x near 0.7549 that solves x^3 + x^2 = 1 gives a formula for zeta(5) with no leftover terms at all. The search found no such formula for zeta(5) in the golden ratio base or in any of the other 21 bases tested.

The base near 0.7549 is 1 divided by the number called the plastic ratio (the number p near 1.3247 that solves p^3 = p + 1). Ladders of sums in this base were studied in a 1987 journal article that sits behind a paywall (https://link.springer.com/article/10.1007/BF01836149) which means the formulas below are very likely consequences of published mathematics. A free web search on 20 November 2026 did not turn up the formulas written out with their coefficients.

## Notation

zeta(3) means 1/1^3 + 1/2^3 + 1/3^3 and so on forever and zeta(5) and zeta(7) and zeta(9) use the powers 5 and 7 and 9 in the same way.

x is the base which is a number between 0 and 1 that each section names.

L = ln(1/x) which is the natural logarithm of 1 divided by the base.

F(y) means the sum of y^n/n^s for n = 1 and 2 and 3 and so on forever. The number s is 3 inside a zeta(3) formula and 5 inside a zeta(5) formula and 7 inside a zeta(7) formula and 9 inside a zeta(9) formula.

The sign × means multiplication.

A leftover term on this page means an extra piece such as pi^2 × L or L^3 that sits beside the sums in a formula. A formula with no leftover terms is built from the sums alone.

## The base near 0.7549 (1 divided by the plastic ratio)

x is the number near 0.754877666 that solves x^3 + x^2 = 1.

zeta(3) with no leftover terms:

zeta(3) = 2 × F(x) + F(x^2) - 2 × F(x^4) - 6 × F(x^5) - F(x^6) + 8 × F(x^7) + 5 × F(x^8) - 4 × F(x^9) - 2 × F(x^12) - F(x^14) + F(x^18)

zeta(5) with no leftover terms:

15 × zeta(5) = -144 × F(x) + 663 × F(x^2) - 512 × F(x^3) - 402 × F(x^4) - 48 × F(x^5) + 519 × F(x^6) + 320 × F(x^7) - 164 × F(x^8) - 17 × F(x^10) - 647 × F(x^12) + 236 × F(x^14) + 240 × F(x^15) + 77 × F(x^20) - 64 × F(x^21) - 17 × F(x^28) - 15 × F(x^30) + 4 × F(x^42)

The search found no formula with no leftover terms for zeta(7) in this base. Four independent formulas for zeta(7) exist with leftover terms allowed and four kinds of leftover term exist for zeta(7) which means three kinds can be cancelled at once. The zeta(7) formula that keeps only the L^7 leftover term is:

49334395572 × zeta(7) = -127108628880 × L^7 + 1019977983360 × F(x) - 3832713139500 × F(x^2) + 4424724528000 × F(x^3) + 429949097235 × F(x^4) - 1308137427072 × F(x^5) - 3885234820460 × F(x^6) + 2612156140800 × F(x^7) + 411381140310 × F(x^8) + 1390253177600 × F(x^9) - 207653038992 × F(x^10) - 1730769403265 × F(x^12) + 384077377980 × F(x^14) + 368160328704 × F(x^15) - 21722705900 × F(x^18) + 68769207549 × F(x^20) - 59940527360 × F(x^21) - 7769425860 × F(x^28) - 5752505136 × F(x^30) + 936570740 × F(x^42)

Only one formula showed up for zeta(9) in this base and the formula keeps all five kinds of leftover term:

13310700154200 × zeta(9) = -10334024827000 × L^9 + 1360103529120 × pi^2 × L^7 - 83179291440 × pi^4 × L^5 - 51456160 × pi^6 × L^3 + 1326333632 × pi^8 × L - 1428712992000 × F(x) + 26229777989625 × F(x^2) + 7578801619200 × F(x^3) - 21920398732575 × F(x^4) - 13022008312320 × F(x^5) + 10079503971075 × F(x^6) + 11189037254400 × F(x^7) - 967513802850 × F(x^8) - 3760850822400 × F(x^9) - 530066022570 × F(x^10) - 710864470575 × F(x^12) + 413520068025 × F(x^14) + 141913658880 × F(x^15) + 14690823525 × F(x^18) + 16277960475 × F(x^20) - 6484780800 × F(x^21) - 1350189000 × F(x^28) - 554350230 × F(x^30) + 25331175 × F(x^42)

The search found no formula for zeta(11) in this base.

The sums in this base shrink slowly because the slowest sum uses powers of 0.7549. With 100 terms of each sum the zeta(5) formula missed zeta(5) by about 1.5 × 10^-21 and with 200 terms the miss was about 3.2 × 10^-35.

## The base near 0.6823 (solves x^3 + x = 1)

x is 1 divided by the number near 1.4656 that solves p^3 = p^2 + 1.

zeta(3) with no leftover terms:

5 × zeta(3) = 18 × F(x) - 13 × F(x^2) - 2 × F(x^3) - 7 × F(x^4) + 5 × F(x^6) + 8 × F(x^7) - F(x^14)

The search found three independent formulas for zeta(5) in this base and each formula needs leftover terms. One of the three is:

2100 × zeta(5) = 600 × L^5 - 160 × pi^2 × L^3 + 30 × pi^4 × L + 1251 × F(x^2) + 2064 × F(x^3) + 1719 × F(x^4) - 2880 × F(x^5) - 390 × F(x^6) - 1152 × F(x^7) + 972 × F(x^8) + 336 × F(x^9) + 180 × F(x^10) + 96 × F(x^12) + 36 × F(x^14) - 21 × F(x^18) - 6 × F(x^24)

## Three more bases that give zeta(3) with no leftover terms

The base near 0.7245 that solves x^4 + x = 1:

3 × zeta(3) = 6 × F(x) + 12 × F(x^2) - 20 × F(x^3) - 15 × F(x^4) + 12 × F(x^5) + 12 × F(x^6) + 8 × F(x^9) - 9 × F(x^10) - 8 × F(x^15) + F(x^30)

The same base gives two formulas for zeta(5) with leftover terms and one of the two is:

5040 × zeta(5) = 1782 × L^5 - 180 × pi^2 × L^3 + 38 × pi^4 × L + 6480 × F(x) + 945 × F(x^2) - 6720 × F(x^3) + 6345 × F(x^4) - 2160 × F(x^5) - 795 × F(x^6) + 2160 × F(x^7) - 1215 × F(x^8) + 240 × F(x^9) - 240 × F(x^12) - 135 × F(x^14) + 15 × F(x^24)

The base near 0.6929 that solves x^5 - x^3 + x^2 + x = 1:

24 × zeta(3) = 57 × F(x) + 51 × F(x^2) - 190 × F(x^3) + 141 × F(x^4) - 45 × F(x^5) - 52 × F(x^6) + 57 × F(x^7) - 12 × F(x^8) - 55 × F(x^9) + 84 × F(x^10) + 48 × F(x^12) + 5 × F(x^15) - 21 × F(x^20)

The base near 0.6518 that solves x^5 + x^4 + x^3 + x^2 = 1:

12 × zeta(3) = 189 × F(x^2) - 378 × F(x^3) + 210 × F(x^4) - 42 × F(x^5) + 70 × F(x^6) - 6 × F(x^7) - 112 × F(x^9) + 63 × F(x^10) + 63 × F(x^12) + 9 × F(x^14) + 28 × F(x^15) + 4 × F(x^21) - 7 × F(x^30) - F(x^42)

## The base 2 - sqrt(3) which reaches zeta(5) and shrinks fast

x = 2 - sqrt(3) which is near 0.2679 and L = ln(2 + sqrt(3)).

23 × zeta(3) = -2 × L^3 + 2 × pi^2 × L + 12 × F(x) + 39 × F(x^2) + 4 × F(x^3) - 3 × F(x^4) - F(x^6)

50430 × zeta(5) = 144 × L^5 - 240 × pi^2 × L^3 + 286 × pi^4 × L + 86400 × F(x) - 39960 × F(x^2) - 1920 × F(x^3) + 675 × F(x^4) + 120 × F(x^6)

The zeta(5) formula in this base shrinks faster than the golden ratio formulas because every sum uses powers of a number near 0.268. With 20 terms of each sum the formula missed zeta(5) by about 5.2 × 10^-19 and with 40 terms the miss was about 6.9 × 10^-32.

## Shorter results in other bases

Each formula in this section is for zeta(3) and each base reached no further than zeta(3) in the search.

The base 1/3:

26 × zeta(3) = -2 × L^3 + 2 × pi^2 × L + 36 × F(x) - 3 × F(x^2)

The base sqrt(2) - 1 near 0.4142:

33 × zeta(3) = -8 × L^3 + 4 × pi^2 × L + 60 × F(x^2) - 6 × F(x^4)

The base 4 - sqrt(15) near 0.1270:

179 × zeta(3) = -4 × L^3 + 10 × pi^2 × L + 360 × F(x) + 12 × F(x^2) - 8 × F(x^3) - 3 × F(x^4)

The base 5 - 2 × sqrt(6) near 0.1010:

116 × zeta(3) = -2 × L^3 + 6 × pi^2 × L + 276 × F(x) - 45 × F(x^2) - 4 × F(x^3) + F(x^6)

The base (5 - sqrt(21))/2 near 0.2087:

154 × zeta(3) = -6 × L^3 + 10 × pi^2 × L + 252 × F(x) - 9 × F(x^2) - 12 × F(x^3) + F(x^6)

The base near 0.5437 that solves x^3 + x^2 + x = 1 (two formulas):

12 × zeta(3) = -8 × L^3 + 2 × pi^2 × L + 6 × F(x^2) + 16 × F(x^3) - 3 × F(x^4)

9 × zeta(3) = 4 × L^3 + 24 × F(x) - 12 × F(x^2) + 8 × F(x^3) - 21 × F(x^4) + 3 × F(x^8)

The base near 0.6662 that solves x^6 - x^4 + x^2 + x = 1:

24 × zeta(3) = -32 × L^3 + 4 × pi^2 × L + 24 × F(x) - 24 × F(x^2) + 24 × F(x^3) + 18 × F(x^4) - 24 × F(x^5) + 12 × F(x^6) - 24 × F(x^7) + 21 × F(x^8) + 18 × F(x^10) - 3 × F(x^12) + 6 × F(x^14) - 3 × F(x^20)

## The base 1/2 for comparison

The base 1/2 gives two independent formulas for zeta(3) and one formula for zeta(5) and both kinds are already in print. The versions the search returned are:

7 × zeta(3) = 2 × L^3 + 24 × F(x) - 18 × F(x^2) - 4 × F(x^3) + F(x^6)

1209 × zeta(5) = 18 × L^5 - 12 × pi^2 × L^3 + 8 × pi^4 × L + 1728 × F(x) - 486 × F(x^2) - 48 × F(x^3) + 3 × F(x^6)

The search found no formula for zeta(7) or zeta(9) or zeta(11) built from F(1/2) through F(1/2^30) with leftover terms made from pi and ln(2). Published formulas for those numbers in the base 1/2 use sums with complex numbers inside which this search did not include.

## How many independent formulas each base gave

Each line gives the count of independent formulas for zeta(3) and zeta(5) and zeta(7) and zeta(9) and zeta(11) in that order with leftover terms allowed. A count of 0 means the search found nothing.

- The base near 0.7549 that solves x^3 + x^2 = 1 gave 10 and 7 and 4 and 1 and 0.
- The base 1/phi near 0.6180 (the golden ratio base) gave 5 and 3 and 2 and 1 and 0.
- The base near 0.6823 that solves x^3 + x = 1 gave 6 and 3 and 0 and 0 and 0.
- The base near 0.7245 that solves x^4 + x = 1 gave 6 and 2 and 0 and 0 and 0.
- The base 1/2 gave 2 and 1 and 0 and 0 and 0.
- The base 2 - sqrt(3) gave 2 and 1 and 0 and 0 and 0.
- The base near 0.6929 that solves x^5 - x^3 + x^2 + x = 1 gave 4 and 0 and 0 and 0 and 0.
- The base near 0.6518 that solves x^5 + x^4 + x^3 + x^2 = 1 gave 4 and 0 and 0 and 0 and 0.
- The base near 0.6662 that solves x^6 - x^4 + x^2 + x = 1 gave 2 and 0 and 0 and 0 and 0.
- The base near 0.5437 that solves x^3 + x^2 + x = 1 gave 2 and 0 and 0 and 0 and 0.
- The bases 1/3 and sqrt(2) - 1 and 4 - sqrt(15) and 5 - 2 × sqrt(6) and (5 - sqrt(21))/2 gave 1 and 0 and 0 and 0 and 0 each.
- The bases 1/5 and 1/7 and (sqrt(13) - 3)/2 and sqrt(17) - 4 and (sqrt(3) - 1)/2 and 8 - 3 × sqrt(7) gave 0 at every step.
- The base near 0.8019 that solves x^3 + 2 × x^2 - x = 1 and the base near 0.3473 that solves x^3 - 3 × x + 1 = 0 gave 0 at every step.

A formula with no leftover terms showed up for zeta(3) in six bases (the golden ratio base and the five bases named in the sections above) and for zeta(5) in one base (the base near 0.7549).

## Limits of the search

The search used the sums F(x) through F(x^30) for bases built from square roots and whole numbers and F(x) through F(x^45) or F(x^50) for the other bases. A formula that needs a higher power would be missed.

The only leftover terms allowed were products of powers of pi and powers of L. A base whose formulas need a different leftover piece (such as the logarithm of a second number) would show a count of 0 on this page even if formulas exist. That limit is the most likely reason for a count of 0 in the last two lines of the list.

The search worked with 3000 digits and accepted a formula only when the whole-number coefficients stayed far below the size that a chance match would need (below 10^28 in the largest runs).

A search does not prove that a formula is impossible because a formula could use ingredients that were not included in the test.

## How the formulas were checked

Every formula printed on this page was checked a second time by adding up each sum term by term with 260 digits and both sides agreed to more than 240 digits in every case.

The program files sit in the boring-things folder of this repository in research-program-files/zeta-sums-scripts (the file bases.py runs the search for one base and the file check-bases.py repeats the term by term check).

## Sources

The paywalled 1987 article on ladders in the base that solves x^3 + x^2 = 1: https://link.springer.com/article/10.1007/BF01836149

A 2015 paper that states the counts for the golden ratio base: https://arxiv.org/abs/1504.05303

A 1998 paper on ladders in the base 1/2 up to zeta(11): https://arxiv.org/abs/math/9803067
