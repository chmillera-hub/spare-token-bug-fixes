# A golden ratio sum for zeta(3) with no leftover terms

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 20 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. The formulas were checked by number matching and not by a written proof.

## Link to the original question

https://arxiv.org/abs/2508.03743

A 2025 paper at that link asks whether formulas built purely from sums over powers of the golden ratio exist for numbers beyond pi^2. The paper reports that an experimental search for a pure formula of that kind for zeta(3) did not succeed and the paper gives a formula that multiplies several sums together as a replacement.

This page reports two pure formulas for zeta(3) that a computer search found on 20 November 2026 so any reader is free to carry the formulas over to people who work on that question.

## Notation

zeta(3) means 1/1^3 + 1/2^3 + 1/3^3 and so on forever which is a number near 1.2020569.

phi = (1 + sqrt(5))/2 which is the golden ratio near 1.618.

r = 1/phi which is near 0.618.

l = ln(phi) which is the natural logarithm of the golden ratio.

F(x) means the sum of x^n/n^3 for n = 1 and 2 and 3 and so on forever. Further down the page the same letter F is used with the power 5 or 7 in place of 3 and the page says so at that spot.

The sign × means multiplication.

A leftover term on this page means an extra piece such as pi^2 × l or l^3 that sits beside the sums in a formula. The classic golden ratio formula for zeta(3) has two leftover terms because the classic formula reads zeta(3) = (5/4) × F(r^2) + (1/6) × pi^2 × l - (5/6) × l^3.

## The two formulas with no leftover terms

Formula A:

3 × zeta(3) = 12 × F(r) - 6 × F(r^2) - 16 × F(r^3) + 9 × F(r^4) + 8 × F(r^6) - F(r^12)

Formula B:

zeta(3) = 8 × F(r^2) - 15 × F(r^4) - 4 × F(r^6) + 18 × F(r^8) + 4 × F(r^10) + 6 × F(r^12) - F(r^20) - F(r^24)

Each side of Formula A and of Formula B agreed to more than 1500 digits in one computation and to more than 400 digits in a second computation that added up every sum term by term without a library routine for F.

## Formula A written as one single sum

Formula A can be folded into one sum because every F in Formula A is a sum over powers of 1/phi.

3 × zeta(3) = the sum of a(n)/(phi^n × n^3) for n = 1 and 2 and 3 and so on forever

The whole numbers a(n) repeat with a period of 12 and the twelve values in order are 12 and -36 and -420 and 540 and 12 and 1260 and 12 and 540 and -420 and -36 and 12 and 108.

The single sum agreed with 3 × zeta(3) to 320 digits.

## How fast the formulas shrink

Formula B shrinks faster than Formula A because the slowest sum in Formula B uses powers of r^2 near 0.382 while the slowest sum in Formula A uses powers of r near 0.618.

With 40 terms of each sum Formula B missed zeta(3) by about 1.3 × 10^-21 and Formula A missed zeta(3) by about 3.7 × 10^-13.

With 80 terms of each sum Formula B missed zeta(3) by about 3.9 × 10^-31 and Formula A missed zeta(3) by about 2.2 × 10^-22.

## The same trick works for the two leftover terms

The search also found sums with no leftover terms for each of the two leftover pieces which means all three ingredients of the classic formula can be written purely as golden ratio sums.

2 × l^3 = 6 × F(r) - 9 × F(r^2) - 8 × F(r^3) + 9 × F(r^4) + 7 × F(r^6) - F(r^12)

2 × pi^2 × l = 66 × F(r) - 54 × F(r^2) - 88 × F(r^3) + 27 × F(r^4) + 47 × F(r^6) + 54 × F(r^8) + 12 × F(r^10) + 10 × F(r^12) - 3 × F(r^20) - 3 × F(r^24)

Both formulas agreed to more than 400 digits in the term by term computation.

## Two combinations of the sums that equal exactly zero

Formula A and Formula B are not the only correct formulas because two combinations of the sums add up to zero and a reader may add any multiple of a zero combination to a formula.

0 = 2 × F(r^2) - 15 × F(r^4) + 34 × F(r^6) - 18 × F(r^8) - 8 × F(r^10) - 11 × F(r^12) + 2 × F(r^20) + F(r^24)

0 = 12 × F(r) - 32 × F(r^2) - 16 × F(r^3) + 69 × F(r^4) - 14 × F(r^6) - 36 × F(r^8) - 4 × F(r^10) - 8 × F(r^12) + F(r^20) + 2 × F(r^24)

The search found no third zero combination among the powers r^1 through r^40.

## Why the formulas probably exist

Published work on golden ratio ladders states that five independent combinations of these sums reduce to zeta(3) plus leftover terms. Only two kinds of leftover term exist for zeta(3) which are pi^2 × l and l^3. Five combinations with two kinds of leftover term leave room to cancel both leftover terms and still keep three combinations which matches what the search found (one formula for zeta(3) plus two zero combinations).

That reasoning means the formulas on this page are very likely consequences of mathematics that is already published and are not new theorems. What a search of the web on 20 November 2026 could not find is the formulas written out with their coefficients.

## What the search found for zeta(5) and zeta(7) and zeta(9)

In this section F uses the power 5 inside a zeta(5) formula and the power 7 inside a zeta(7) formula.

The search found no formula without leftover terms for zeta(5) or zeta(7) or zeta(9) among the powers r^1 through r^40 with whole-number coefficients up to 10^29. A search does not prove that no such formula exists because a formula could use ingredients that were not included in the test.

The count of independent formulas with leftover terms allowed was 5 for zeta(3) and 3 for zeta(5) and 2 for zeta(7) and 1 for zeta(9). Those four counts match the counts in the published record which is a sign that the search worked correctly.

Three independent formulas for zeta(5) with three kinds of leftover term mean that two kinds can be cancelled at once. The search found the three formulas for zeta(5) that keep only one leftover term each:

2881 × zeta(5) = 1584 × l^5 + 23400 × F(r^2) - 70605 × F(r^4) + 90400 × F(r^6) - 33210 × F(r^8) - 8496 × F(r^10) - 8140 × F(r^12) + 531 × F(r^20) + 205 × F(r^24)

1943 × zeta(5) = 96 × pi^2 × l^3 + 13104 × F(r^2) - 34695 × F(r^4) + 40352 × F(r^6) - 13446 × F(r^8) - 3600 × F(r^10) - 3452 × F(r^12) + 225 × F(r^20) + 83 × F(r^24)

6231 × zeta(5) = 44 × pi^4 × l + 21600 × F(r^2) - 40500 × F(r^4) + 40800 × F(r^6) - 12150 × F(r^8) - 3456 × F(r^10) - 3300 × F(r^12) + 216 × F(r^20) + 75 × F(r^24)

Two independent formulas for zeta(7) with four kinds of leftover term mean that one kind can be cancelled. The zeta(7) formula with the smallest coefficients that drops the pi^6 × l term is:

187256115 × zeta(7) = 98740416 × l^7 - 23794368 × pi^2 × l^5 + 2458528 × pi^4 × l^3 + 886699440 × F(r^2) - 1652579415 × F(r^4) + 1397911680 × F(r^6) - 380734830 × F(r^8) - 55563840 × F(r^10) - 36845100 × F(r^12) + 868185 × F(r^20) + 261135 × F(r^24)

Only one formula exists for zeta(9) in this family as far as the search could tell which means no leftover term of the zeta(9) formula can be cancelled. The page named long-formulas.md in this folder prints that zeta(9) formula.

The four formulas in this section agreed to more than 400 digits in the term by term computation.

## How the search worked

The method was an integer relation search which is a procedure that takes a list of numbers and hunts for whole-number coefficients that make the weighted total equal exactly zero. The search worked with 2400 digits and a true formula shows up as coefficients of a few digits while a false match would need coefficients of dozens of digits.

The program file sits in the boring-things folder of this repository at research-program-files/zeta-sums-scripts/search.py so any person or AI model can rerun the search.

## Sources

The 2025 paper that reports the unsuccessful search for a pure zeta(3) formula: https://arxiv.org/abs/2508.03743

A 2015 paper that states the counts of independent golden ratio combinations: https://arxiv.org/abs/1504.05303

A 2000 paper that describes the golden ratio ladder up to zeta(9): https://arxiv.org/abs/hep-th/0004153
