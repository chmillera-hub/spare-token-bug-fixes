# Prime percentages grouped by type of equation

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each percentage comes from a computer count and not from a written proof.

## What the list shows

The list sorts 529 equations and running sums into 30 groups by type and ranks the recipes inside each group from the most primes to the fewest primes. Each percentage compares the recipe with plain counting numbers of the same size so +859% means 859% more primes than the number line and −100% means no primes.

The page [ranked-list.md](ranked-list.md) holds the same lines in one ranking from the highest percentage to the lowest percentage.

## The rules behind every line

An output with decimal places has the decimal places dropped with no rounding (1.99 becomes 1) unless the line names a different rounding rule.

"Bump" means the last digit of a number moves up to the nearest of 1 or 3 or 7 or 9 so 0 becomes 1 and 2 becomes 3 and 4 or 5 or 6 becomes 7 and 8 becomes 9. "Bump carried into the next addition" means a running total is bumped and the next number is added to the bumped total.

A prime that an equation outputs more than once counts once so an equation that keeps repeating the same prime gets a low percentage.

## How to judge how solid a line is

Each line carries three numbers that show how much testing stands behind the percentage because a percentage from 30 tested outputs deserves far less trust than a percentage from 300000 tested outputs.

"Give or take" is the wobble that luck alone puts on the percentage. A line that reads +341% (give or take 128 points) could have landed anywhere from about +210% to about +470% by luck while a line that reads +859% (give or take 3 points) is pinned down tightly.

"Tested" is the count of outputs the computer checked and "found" is the count of different primes among those outputs and "chance predicts" is the count of primes that ordinary numbers of the same sizes would give. The two shares in brackets give the absolute picture: the share of the outputs that were prime and the share that chance predicts. A line can have a high percentage and a low share when the outputs are long because primes are rare among long numbers.

"Luck odds" works like the p-value from science. The luck odds say how often plain luck would produce a gap this large if the equation really had the same prime rate as the number line. Luck odds of 1 in 50000 mean the gap is almost surely real. Luck odds of about 10 in 100 or more mean the gap could be luck and the line says so. 81 of the 529 lines carry that warning.

## The groups compared

Each line gives the highest and the lowest percentage inside one group and the groups run from the group with the highest top percentage to the group with the lowest top percentage.

- Sums and running totals (128 lines): highest +1307% and lowest −100%
- Straight-line equations (a number times n) (23 lines): highest +1108% and lowest −100%
- Equations that start with n² (38 lines): highest +972% and lowest −100%
- Mixed operations (9 lines): highest +796% and lowest +26%
- Equations famous for a long unbroken run of primes (10 lines): highest +747% and lowest +615%
- Equations from published richness record lists (4 lines): highest +701% and lowest +648%
- Recipes that start from the list of primes (22 lines): highest +579% and lowest −100%
- Well-known number lists (17 lines): highest +536% and lowest −100%
- Powers of n plus 1 and related equations (6 lines): highest +363% and lowest +110%
- Factorials and Fibonacci numbers (4 lines): highest +360% and lowest +44%
- Equations with n in the exponent (28 lines): highest +337% and lowest −89%
- Geometry (4 lines): highest +315% and lowest −100%
- Cubes and higher powers (20 lines): highest +262% and lowest −100%
- Digits taken from the zeta sum (12 lines): highest +247% and lowest −75%
- Counting functions (4 lines): highest +213% and lowest −36%
- Square roots and decimal powers (13 lines): highest +213% and lowest −100%
- A square divided by a whole number (60 lines): highest +180% and lowest −100%
- Equations and digits built from e (6 lines): highest +175% and lowest −2%
- Other division equations (32 lines): highest +158% and lowest −100%
- Equations and digits built from π (11 lines): highest +153% and lowest −2%
- Logarithms (15 lines): highest +152% and lowest −92%
- Equations and digits built from φ (the golden ratio) (8 lines): highest +151% and lowest 0%
- Digit tricks (14 lines): highest +150% and lowest −100%
- Modulus (the remainder after division) (7 lines): highest +109% and lowest −100%
- Trig functions (sine and cosine and tangent) (12 lines): highest +108% and lowest −100%
- Calculus (slopes and areas) (6 lines): highest +100% and lowest −100%
- Step-by-step rules (5 lines): highest +100% and lowest −87%
- Best fractions (3 lines): highest +88% and lowest +39%
- Bit tricks (5 lines): highest 0% and lowest −100%
- Equations famous for very few primes (3 lines): highest −97% and lowest −100%

## Sums and running totals

A running total is tested at every step. Sums of whole numbers or squares or cubes produce no primes because the totals split into factors such as n × (n + 1) ÷ 2. Carrying the bump into the next addition breaks the splitting and can lock the totals onto prime-rich equations. A sum that starts at a well-chosen number and adds multiples of 2 or 6 or 30 reaches the highest percentages because the totals form a prime-rich equation such as n² + n + 41.

1. start at 2 then add the gaps between neighboring primes: +1307% (give or take 3 points). Tested 300000 outputs and found 300000 primes (100% of the outputs) where chance predicts 21316 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
2. start at 2 then add the gaps between neighboring primes then bump each total: +1307% (give or take 3 points). Tested 300000 outputs and found 299999 primes (100% of the outputs) where chance predicts 21316 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
3. the gaps between neighboring primes added up with the bump carried into the next addition: +1307% (give or take 3 points). Tested 300000 outputs and found 299999 primes (100% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
4. start at 5660169547 then add 30 + 60 + 90 and so on: +865% (give or take 3 points). Tested 300000 outputs and found 111218 primes (37% of the outputs) where chance predicts 11521 (3.8%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
5. start at 190514189597 then add 30 + 60 + 90 and so on: +862% (give or take 3 points). Tested 300000 outputs and found 107017 primes (36% of the outputs) where chance predicts 11129 (3.7%). Luck odds: under 1 in a billion.
6. start at 24600021781 then add 30 + 60 + 90 and so on: +861% (give or take 3 points). Tested 300000 outputs and found 109706 primes (37% of the outputs) where chance predicts 11416 (3.8%). Luck odds: under 1 in a billion.
7. start at 26853927251 then add 2 + 4 + 6 + 8 and so on: +859% (give or take 3 points). Tested 300000 outputs and found 116748 primes (39% of the outputs) where chance predicts 12173 (4.1%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
8. start at 100800448037 then add 210 + 420 + 630 and so on: +857% (give or take 3 points). Tested 300000 outputs and found 102125 primes (34% of the outputs) where chance predicts 10666 (3.6%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
9. start at 29717281333 then add 6 + 12 + 18 and so on: +854% (give or take 3 points). Tested 300000 outputs and found 113475 primes (38% of the outputs) where chance predicts 11889 (4.0%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
10. start at 473317155281 then add 6 + 12 + 18 and so on: +846% (give or take 3 points). Tested 300000 outputs and found 104947 primes (35% of the outputs) where chance predicts 11092 (3.7%). Luck odds: under 1 in a billion.
11. start at 404492439881 then add 6 + 12 + 18 and so on: +838% (give or take 3 points). Tested 300000 outputs and found 104578 primes (35% of the outputs) where chance predicts 11147 (3.7%). Luck odds: under 1 in a billion.
12. start at 41 then add 2 + 4 + 6 + 8 and so on: +564% (give or take 2 points). Tested 300000 outputs and found 86613 primes (29% of the outputs) where chance predicts 13042 (4.3%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
13. start at 29 then add 2 + 6 + 10 + 14 and so on: +492% (give or take 2 points). Tested 300000 outputs and found 74919 primes (25% of the outputs) where chance predicts 12656 (4.2%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
14. start at 1 then add 30030 + 30030 + 30030 and so on: +422% (give or take 2 points). Tested 300000 outputs and found 71656 primes (24% of the outputs) where chance predicts 13717 (4.6%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
15. start at 1 then add 2310 + 4620 + 6930 and so on (multiples of 2310): +368% (give or take 2 points). Tested 300000 outputs and found 46609 primes (16% of the outputs) where chance predicts 9961 (3.3%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
16. the gaps between neighboring primes added up then bump each total: +341% (give or take 1 point). Tested 300000 outputs and found 93921 primes (31% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
17. start at 1 then add 210 + 210 + 210 and so on: +338% (give or take 2 points). Tested 300000 outputs and found 77774 primes (26% of the outputs) where chance predicts 17762 (5.9%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
18. start at 28 then add 1 + 2 + 3 + 4 and so on with the bump carried into the next addition: +322% (give or take 2 points). Tested 300000 outputs and found 56776 primes (19% of the outputs) where chance predicts 13453 (4.5%). Luck odds: under 1 in a billion.
19. start at 1 then add 210 + 420 + 630 and so on (multiples of 210): +298% (give or take 2 points). Tested 300000 outputs and found 43060 primes (14% of the outputs) where chance predicts 10829 (3.6%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
20. start at 1 then add 30 + 30 + 30 and so on: +275% (give or take 1 point). Tested 300000 outputs and found 75251 primes (25% of the outputs) where chance predicts 20089 (6.7%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
21. 1 + 8 + 27 + 64 and so on (cubes) with the bump carried into the next addition: +274% (give or take 2 points). Tested 300000 outputs and found 25180 primes (8.4% of the outputs) where chance predicts 6727 (2.2%). Luck odds: under 1 in a billion.
22. 6 + 12 + 18 + 24 and so on (multiples of 6) then bump each total: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes (14% of the outputs) where chance predicts 12441 (4.1%). Luck odds: under 1 in a billion.
23. 6 + 12 + 18 + 24 and so on (multiples of 6) with the bump carried into the next addition: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes (14% of the outputs) where chance predicts 12441 (4.1%). Luck odds: under 1 in a billion.
24. start at 1 then add 6 + 12 + 18 + 24 and so on: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes (14% of the outputs) where chance predicts 12441 (4.1%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
25. start at 1 then add 4 + 8 + 12 + 16 and so on then bump each total: +226% (give or take 2 points). Tested 300000 outputs and found 41304 primes (14% of the outputs) where chance predicts 12657 (4.2%). Luck odds: under 1 in a billion.
26. 1 + 2 + 3 + 4 and so on with the bump carried into the next addition: +222% (give or take 2 points). Tested 300000 outputs and found 43383 primes (14% of the outputs) where chance predicts 13454 (4.5%). Luck odds: under 1 in a billion.
27. 2 + 6 + 12 + 20 and so on (n times n + 1) then bump each total: +216% (give or take 2 points). Tested 300000 outputs and found 28438 primes (9.5% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
28. 2 + 6 + 12 + 20 and so on (n times n + 1) with the bump carried into the next addition: +216% (give or take 2 points). Tested 300000 outputs and found 28438 primes (9.5% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
29. start at 28 then add 1 + 2 + 3 + 4 and so on then bump each total: +212% (give or take 2 points). Tested 300000 outputs and found 41933 primes (14% of the outputs) where chance predicts 13453 (4.5%). Luck odds: under 1 in a billion.
30. start at 1 then add 30 + 60 + 90 and so on (multiples of 30): +204% (give or take 2 points). Tested 300000 outputs and found 35456 primes (12% of the outputs) where chance predicts 11655 (3.9%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
31. 6 + 6 + 6 + 6 and so on then bump each total: +200% (give or take 1 point). Tested 300000 outputs and found 67500 primes (22% of the outputs) where chance predicts 22536 (7.5%). Luck odds: under 1 in a billion.
32. 1 + 9 + 25 + 49 and so on (odd squares) with the bump carried into the next addition: +194% (give or take 2 points). Tested 300000 outputs and found 25380 primes (8.5% of the outputs) where chance predicts 8622 (2.9%). Luck odds: under 1 in a billion.
33. 1 + 8 + 27 + 64 and so on (cubes) then bump each total: +185% (give or take 2 points). Tested 300000 outputs and found 19152 primes (6.4% of the outputs) where chance predicts 6727 (2.2%). Luck odds: under 1 in a billion.
34. n! + 1 (1 × 2 × 3 up to n then add 1): +185% (give or take 90 points). Tested 165 outputs and found 10 primes (6.1% of the outputs) where chance predicts 3.5 (2.1%). Luck odds: 1 in 300. Note: outputs up to 300 digits.
35. 1 + 3 + 9 + 27 and so on (powers of 3) then bump each total: +176% (give or take 69 points). Tested 629 outputs and found 16 primes (2.5% of the outputs) where chance predicts 5.8 (0.92%). Luck odds: 1 in 3000. Note: outputs up to 300 digits.
36. start at 1 then add 4 + 8 + 12 + 16 and so on: +173% (give or take 1 point). Tested 300000 outputs and found 34603 primes (12% of the outputs) where chance predicts 12657 (4.2%). Luck odds: under 1 in a billion.
37. 1 + 4 + 9 + 16 and so on (squares) with the bump carried into the next addition: +169% (give or take 2 points). Tested 300000 outputs and found 24179 primes (8.1% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
38. 1 + 11 + 111 + 1111 and so on with the bump carried into the next addition: +163% (give or take 98 points). Tested 300 outputs and found 7 primes (2.3% of the outputs) where chance predicts 2.7 (0.90%). Luck odds: about 2 in 100. Note: outputs up to 300 digits.
39. 1 + 2 + 3 + 4 and so on then bump each total: +159% (give or take 1 point). Tested 300000 outputs and found 34905 primes (12% of the outputs) where chance predicts 13454 (4.5%). Luck odds: under 1 in a billion.
40. start at 1 then add 4 + 8 + 12 + 16 and so on with the bump carried into the next addition: +158% (give or take 1 point). Tested 300000 outputs and found 32609 primes (11% of the outputs) where chance predicts 12657 (4.2%). Luck odds: under 1 in a billion.
41. n × π with decimals dropped added up with the bump carried into the next addition: +156% (give or take 1 point). Tested 300000 outputs and found 32763 primes (11% of the outputs) where chance predicts 12789 (4.3%). Luck odds: under 1 in a billion.
42. n × π with decimals dropped added up then bump each total: +154% (give or take 1 point). Tested 300000 outputs and found 32438 primes (11% of the outputs) where chance predicts 12789 (4.3%). Luck odds: under 1 in a billion.
43. the digit totals of 1 and 2 and 3 and so on added up then bump each total: +154% (give or take 1 point). Tested 300000 outputs and found 52249 primes (17% of the outputs) where chance predicts 20584 (6.9%). Luck odds: under 1 in a billion.
44. √n with decimals dropped added up with the bump carried into the next addition: +154% (give or take 1 point). Tested 300000 outputs and found 45312 primes (15% of the outputs) where chance predicts 17808 (5.9%). Luck odds: under 1 in a billion.
45. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime) then bump each total: +152% (give or take 2 points). Tested 300000 outputs and found 21007 primes (7.0% of the outputs) where chance predicts 8350 (2.8%). Luck odds: under 1 in a billion.
46. 4 + 9 + 25 + 49 and so on (squares of primes) then bump each total: +152% (give or take 2 points). Tested 300000 outputs and found 19635 primes (6.5% of the outputs) where chance predicts 7797 (2.6%). Luck odds: under 1 in a billion.
47. 2 + 5 + 11 + 17 and so on (every second prime) then bump each total: +151% (give or take 1 point). Tested 300000 outputs and found 29409 primes (9.8% of the outputs) where chance predicts 11723 (3.9%). Luck odds: under 1 in a billion.
48. 2 + 5 + 11 + 17 and so on (every second prime) with the bump carried into the next addition: +151% (give or take 1 point). Tested 300000 outputs and found 29383 primes (9.8% of the outputs) where chance predicts 11723 (3.9%). Luck odds: under 1 in a billion.
49. 4 + 9 + 25 + 49 and so on (squares of primes) with the bump carried into the next addition: +151% (give or take 2 points). Tested 300000 outputs and found 19553 primes (6.5% of the outputs) where chance predicts 7797 (2.6%). Luck odds: under 1 in a billion.
50. n × ln(n) with decimals dropped added up then bump each total: +151% (give or take 1 point). Tested 300000 outputs and found 30500 primes (10% of the outputs) where chance predicts 12143 (4.0%). Luck odds: under 1 in a billion.
51. 1 + 1 + 1 + 1 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 60236 primes (20% of the outputs) where chance predicts 24140 (8.0%). Luck odds: under 1 in a billion.
52. 1 + 16 + 81 + 256 and so on (fourth powers) with the bump carried into the next addition: +150% (give or take 2 points). Tested 300000 outputs and found 13409 primes (4.5% of the outputs) where chance predicts 5370 (1.8%). Luck odds: under 1 in a billion.
53. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime) with the bump carried into the next addition: +150% (give or take 2 points). Tested 300000 outputs and found 20849 primes (6.9% of the outputs) where chance predicts 8350 (2.8%). Luck odds: under 1 in a billion.
54. 2 + 2 + 2 + 2 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 60236 primes (20% of the outputs) where chance predicts 24140 (8.0%). Luck odds: under 1 in a billion.
55. 3 + 3 + 3 + 3 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 57097 primes (19% of the outputs) where chance predicts 22853 (7.6%). Luck odds: under 1 in a billion.
56. 6 + 6 + 6 + 6 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 55890 primes (19% of the outputs) where chance predicts 22358 (7.5%). Luck odds: under 1 in a billion.
57. 7 + 7 + 7 + 7 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 54249 primes (18% of the outputs) where chance predicts 21697 (7.2%). Luck odds: under 1 in a billion.
58. n × ln(n) with decimals dropped added up with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 30353 primes (10% of the outputs) where chance predicts 12144 (4.0%). Luck odds: under 1 in a billion.
59. start at 1 then add 10 + 10 + 10 and so on: +150% (give or take 1 point). Tested 300000 outputs and found 54175 primes (18% of the outputs) where chance predicts 21697 (7.2%). Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
60. the digit totals of 1 and 2 and 3 and so on added up with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 51241 primes (17% of the outputs) where chance predicts 20530 (6.8%). Luck odds: under 1 in a billion.
61. 2 + 3 + 5 + 7 and so on (primes) with the bump carried into the next addition: +149% (give or take 1 point). Tested 300000 outputs and found 30117 primes (10% of the outputs) where chance predicts 12083 (4.0%). Luck odds: under 1 in a billion.
62. n! + 1 (1 × 2 × 3 up to n then add 1) then bump the last digit: +149% (give or take 75 points). Tested 166 outputs and found 11 primes (6.6% of the outputs) where chance predicts 4.4 (2.7%). Luck odds: 1 in 200. Note: outputs up to 300 digits.
63. 2 + 3 + 5 + 7 and so on (primes) then bump each total: +148% (give or take 1 point). Tested 300000 outputs and found 29913 primes (10.0% of the outputs) where chance predicts 12083 (4.0%). Luck odds: under 1 in a billion.
64. n² + n + 41 added up with the bump carried into the next addition: +147% (give or take 2 points). Tested 300000 outputs and found 22226 primes (7.4% of the outputs) where chance predicts 8985 (3.0%). Luck odds: under 1 in a billion.
65. 1 + 11 + 111 + 1111 and so on then bump each total: +126% (give or take 91 points). Tested 300 outputs and found 6 primes (2.0% of the outputs) where chance predicts 2.7 (0.90%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
66. 1 + 3 + 9 + 27 and so on (powers of 3) with the bump carried into the next addition: +126% (give or take 62 points). Tested 629 outputs and found 13 primes (2.1% of the outputs) where chance predicts 5.8 (0.92%). Luck odds: 1 in 100. Note: outputs up to 300 digits.
67. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on) with the bump carried into the next addition: +125% (give or take 2 points). Tested 100000 outputs and found 18634 primes (19% of the outputs) where chance predicts 8267 (8.3%). Luck odds: under 1 in a billion.
68. 1 + 3 + 5 + 7 and so on (odd numbers) with the bump carried into the next addition: +123% (give or take 1 point). Tested 300000 outputs and found 29138 primes (9.7% of the outputs) where chance predicts 13043 (4.3%). Luck odds: under 1 in a billion.
69. 2 + 4 + 6 + 8 and so on (even numbers) then bump each total: +123% (give or take 1 point). Tested 300000 outputs and found 29139 primes (9.7% of the outputs) where chance predicts 13044 (4.3%). Luck odds: under 1 in a billion.
70. 2 + 4 + 6 + 8 and so on (even numbers) with the bump carried into the next addition: +123% (give or take 1 point). Tested 300000 outputs and found 29139 primes (9.7% of the outputs) where chance predicts 13044 (4.3%). Luck odds: under 1 in a billion.
71. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on) then bump each total: +103% (give or take 2 points). Tested 100000 outputs and found 17002 primes (17% of the outputs) where chance predicts 8395 (8.4%). Luck odds: under 1 in a billion.
72. 2 + 2 + 2 + 2 and so on then bump each total: +100% (give or take 1 point). Tested 300000 outputs and found 49096 primes (16% of the outputs) where chance predicts 24586 (8.2%). Luck odds: under 1 in a billion.
73. the first n primes added up then plus 1 for even totals: +99% (give or take 1 point). Tested 300000 outputs and found 23995 primes (8.0% of the outputs) where chance predicts 12084 (4.0%). Luck odds: under 1 in a billion.
74. 1 + 3 + 5 + 7 and so on (odd numbers) then bump each total: +96% (give or take 1 point). Tested 300000 outputs and found 25564 primes (8.5% of the outputs) where chance predicts 13043 (4.3%). Luck odds: under 1 in a billion.
75. 3 + 3 + 3 + 3 and so on then bump each total: +87% (give or take 1 point). Tested 300000 outputs and found 44506 primes (15% of the outputs) where chance predicts 23787 (7.9%). Luck odds: under 1 in a billion.
76. n² + n + 41 added up then bump each total: +86% (give or take 1 point). Tested 300000 outputs and found 16708 primes (5.6% of the outputs) where chance predicts 8985 (3.0%). Luck odds: under 1 in a billion.
77. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers) then bump each total: +82% (give or take 36 points). Tested 1435 outputs and found 25 primes (1.7% of the outputs) where chance predicts 13.8 (0.96%). Luck odds: 1 in 200. Note: outputs up to 300 digits.
78. √n with decimals dropped added up then bump each total: +80% (give or take 1 point). Tested 300000 outputs and found 31998 primes (11% of the outputs) where chance predicts 17820 (5.9%). Luck odds: under 1 in a billion.
79. 1 + 2 + 4 + 8 and so on (powers of 2) then bump each total: +78% (give or take 43 points). Tested 996 outputs and found 17 primes (1.7% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: about 2 in 100. Note: outputs up to 300 digits.
80. start at 2 then add the gaps between neighboring primes with the bump carried into the next addition: +76% (give or take 1 point). Tested 300000 outputs and found 37465 primes (12% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
81. 7 + 7 + 7 + 7 and so on then bump each total: +75% (give or take 1 point). Tested 300000 outputs and found 38940 primes (13% of the outputs) where chance predicts 22276 (7.4%). Luck odds: under 1 in a billion.
82. 1 + 3 + 6 + 10 and so on (triangle numbers) with the bump carried into the next addition: +74% (give or take 1 point). Tested 300000 outputs and found 16011 primes (5.3% of the outputs) where chance predicts 9179 (3.1%). Luck odds: under 1 in a billion.
83. start at 28 then add 1 + 2 + 3 + 4 and so on: +56% (give or take 1 point). Tested 300000 outputs and found 21051 primes (7.0% of the outputs) where chance predicts 13453 (4.5%). Luck odds: under 1 in a billion.
84. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers) with the bump carried into the next addition: +47% (give or take 33 points). Tested 1435 outputs and found 20 primes (1.4% of the outputs) where chance predicts 13.6 (0.95%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
85. 1 + 2 + 4 + 8 and so on (powers of 2): +46% (give or take 39 points). Tested 996 outputs and found 14 primes (1.4% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: about 11 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
86. 1 + 9 + 25 + 49 and so on (odd squares) then bump each total: +38% (give or take 1 point). Tested 300000 outputs and found 11857 primes (4.0% of the outputs) where chance predicts 8622 (2.9%). Luck odds: under 1 in a billion.
87. 1 + 2 + 4 + 8 and so on (powers of 2) with the bump carried into the next addition: +36% (give or take 38 points). Tested 996 outputs and found 13 primes (1.3% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: about 17 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
88. 1 + 4 + 9 + 16 and so on (squares) then bump each total: +35% (give or take 1 point). Tested 300000 outputs and found 12173 primes (4.1% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
89. the gaps between neighboring primes added up: +33% (give or take 1 point). Tested 300000 outputs and found 28349 primes (9.4% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
90. n × π with decimals dropped added up: +4% (give or take 1 point). Tested 300000 outputs and found 13352 primes (4.5% of the outputs) where chance predicts 12789 (4.3%). Luck odds: 1 in 3000000.
91. 2 + 5 + 11 + 17 and so on (every second prime): +1% (give or take 1 point). Tested 300000 outputs and found 11845 primes (3.9% of the outputs) where chance predicts 11723 (3.9%). Luck odds: about 13 in 100 which means the gap could be luck.
92. n × ln(n) with decimals dropped added up: +1% (give or take 1 point). Tested 300000 outputs and found 12315 primes (4.1% of the outputs) where chance predicts 12144 (4.0%). Luck odds: about 6 in 100.
93. n÷1 + n÷2 + n÷3 up to n÷n with decimals dropped in each piece: +1% (give or take 1 point). Tested 300000 outputs and found 21800 primes (7.3% of the outputs) where chance predicts 21482 (7.2%). Luck odds: about 2 in 100.
94. 1 + 1 + 1 + 1 and so on: 0% (give or take 1 point). Tested 300000 outputs and found 25997 primes (8.7% of the outputs) where chance predicts 26086 (8.7%). Luck odds: about 29 in 100 which means the gap could be luck.
95. 1 + 1 + 1 + 1 and so on then bump each total: 0% (give or take 1 point). Tested 300000 outputs and found 25995 primes (8.7% of the outputs) where chance predicts 26085 (8.7%). Luck odds: about 29 in 100 which means the gap could be luck.
96. 1 + 3 + 9 + 27 and so on (powers of 3): 0% (give or take 41 points). Tested 629 outputs and found 6 primes (0.95% of the outputs) where chance predicts 6.0 (0.95%). Luck odds: about 55 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
97. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime): 0% (give or take 1 point). Tested 300000 outputs and found 8367 primes (2.8% of the outputs) where chance predicts 8350 (2.8%). Luck odds: about 43 in 100 which means the gap could be luck.
98. n × (1 + 1/2 + 1/3 up to 1/n) with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 21340 primes (7.1% of the outputs) where chance predicts 21425 (7.1%). Luck odds: about 28 in 100 which means the gap could be luck.
99. 1 + 3 + 6 + 10 and so on (triangle numbers) then bump each total: −1% (give or take 1 point). Tested 300000 outputs and found 9080 primes (3.0% of the outputs) where chance predicts 9179 (3.1%). Luck odds: about 15 in 100 which means the gap could be luck.
100. 2 + 3 + 5 + 7 and so on (primes): −1% (give or take 1 point). Tested 300000 outputs and found 12012 primes (4.0% of the outputs) where chance predicts 12084 (4.0%). Luck odds: about 26 in 100 which means the gap could be luck.
101. 4 + 9 + 25 + 49 and so on (squares of primes): −1% (give or take 1 point). Tested 300000 outputs and found 7749 primes (2.6% of the outputs) where chance predicts 7797 (2.6%). Luck odds: about 30 in 100 which means the gap could be luck.
102. the first n primes added up: −1% (give or take 1 point). Tested 300000 outputs and found 12012 primes (4.0% of the outputs) where chance predicts 12084 (4.0%). Luck odds: about 26 in 100 which means the gap could be luck.
103. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on): −11% (give or take 1 point). Tested 100000 outputs and found 7474 primes (7.5% of the outputs) where chance predicts 8395 (8.4%). Luck odds: under 1 in a billion.
104. 1 + 16 + 81 + 256 and so on (fourth powers) then bump each total: −34% (give or take 1 point). Tested 300000 outputs and found 3526 primes (1.2% of the outputs) where chance predicts 5370 (1.8%). Luck odds: under 1 in a billion.
105. the digit totals of 1 and 2 and 3 and so on added up: −60% (give or take 1 point). Tested 300000 outputs and found 8181 primes (2.7% of the outputs) where chance predicts 20584 (6.9%). Luck odds: under 1 in a billion.
106. 1 + 2 + 6 + 24 and so on (factorials): −71% (give or take 29 points). Tested 166 outputs and found 1 prime (0.60% of the outputs) where chance predicts 3.4 (2.0%). Luck odds: about 15 in 100 which means the gap could be luck. Note: outputs up to 300 digits and the bump changes nothing for these totals.
107. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers): −86% (give or take 10 points). Tested 1435 outputs and found 2 primes (0.14% of the outputs) where chance predicts 14.1 (0.98%). Luck odds: 1 in 10000. Note: outputs up to 300 digits.
108. 1 + 11 + 111 + 1111 and so on: −100% (give or take 37 points). Tested 300 outputs and found 0 primes (0.000% of the outputs) where chance predicts 2.7 (0.90%). Luck odds: about 7 in 100. Note: outputs up to 300 digits.
109. 1 + 16 + 81 + 256 and so on (fourth powers): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 5370 (1.8%). Luck odds: under 1 in a billion.
110. 1 + 2 + 3 + 4 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 13455 (4.5%). Luck odds: under 1 in a billion.
111. 1 + 2 + 3 up to n: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
112. 1 + 3 + 5 + 7 and so on (odd numbers): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 13043 (4.3%). Luck odds: under 1 in a billion.
113. 1 + 3 + 6 + 10 and so on (triangle numbers): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 9179 (3.1%). Luck odds: under 1 in a billion.
114. 1 + 4 + 9 + 16 and so on (squares): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
115. 1 + 8 + 27 + 64 and so on (cubes): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 6727 (2.2%). Luck odds: under 1 in a billion.
116. 1 + 9 + 25 + 49 and so on (odd squares): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 8623 (2.9%). Luck odds: under 1 in a billion.
117. 1² + 2² + 3² up to n²: −100% (give or take 1 point). Tested 14421 outputs and found 1 prime (0.007% of the outputs) where chance predicts 599 (4.2%). Luck odds: under 1 in a billion.
118. 1² + 2² + 3² up to n² then plus 1: −100% (give or take 1 point). Tested 14421 outputs and found 2 primes (0.014% of the outputs) where chance predicts 600 (4.2%). Luck odds: under 1 in a billion.
119. 2 + 2 + 2 + 2 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 24586 (8.2%). Luck odds: under 1 in a billion.
120. 2 + 4 + 6 + 8 and so on (even numbers): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 13044 (4.3%). Luck odds: under 1 in a billion.
121. 2 + 6 + 12 + 20 and so on (n times n + 1): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 8986 (3.0%). Luck odds: under 1 in a billion.
122. 3 + 3 + 3 + 3 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 23787 (7.9%). Luck odds: under 1 in a billion.
123. 6 + 12 + 18 + 24 and so on (multiples of 6): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 12441 (4.1%). Luck odds: under 1 in a billion.
124. 6 + 6 + 6 + 6 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 22536 (7.5%). Luck odds: under 1 in a billion.
125. 7 + 7 + 7 + 7 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 22276 (7.4%). Luck odds: under 1 in a billion.
126. n² + n + 41 added up: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 8985 (3.0%). Luck odds: under 1 in a billion.
127. √1 + √2 + √3 up to √n with decimals dropped in each piece: −100% (give or take 1 point). Tested 300000 outputs and found 16 primes (0.005% of the outputs) where chance predicts 17820 (5.9%). Luck odds: under 1 in a billion.
128. √n with decimals dropped added up: −100% (give or take 1 point). Tested 300000 outputs and found 16 primes (0.005% of the outputs) where chance predicts 17820 (5.9%). Luck odds: under 1 in a billion.

## Straight-line equations (a number times n)

Straight-line equations gain primes when the multiplier contains many small primes because the outputs then dodge every one of those primes.

1. (the product of every prime up to 1009) × n + 1: +1108% (give or take 20 points). Tested 300000 outputs and found 3713 primes (1.2% of the outputs) where chance predicts 307 (0.10%). Luck odds: under 1 in a billion. Note: outputs have about 425 digits.
2. (the product of every prime up to 541) × n + 1: +1030% (give or take 14 points). Tested 300000 outputs and found 6534 primes (2.2% of the outputs) where chance predicts 578 (0.19%). Luck odds: under 1 in a billion. Note: outputs have about 226 digits.
3. (the product of every prime up to 97) × n + 1: +726% (give or take 5 points). Tested 300000 outputs and found 25674 primes (8.6% of the outputs) where chance predicts 3108 (1.0%). Luck odds: under 1 in a billion. Note: outputs have about 43 digits.
4. 510510 × n + 1 (510510 is 2 × 3 × 5 × 7 × 11 × 13 × 17): +457% (give or take 2 points). Tested 300000 outputs and found 62894 primes (21% of the outputs) where chance predicts 11295 (3.8%). Luck odds: under 1 in a billion.
5. 51051 × n + 1 then bump the last digit (51051 is 3 × 7 × 11 × 13 × 17): +400% (give or take 2 points). Tested 300000 outputs and found 63523 primes (21% of the outputs) where chance predicts 12706 (4.2%). Luck odds: under 1 in a billion.
6. 210n + 1: +335% (give or take 2 points). Tested 300000 outputs and found 49050 primes (16% of the outputs) where chance predicts 11284 (3.8%). Luck odds: under 1 in a billion.
7. 210n + 1 then bump the last digit: +335% (give or take 2 points). Tested 300000 outputs and found 49050 primes (16% of the outputs) where chance predicts 11284 (3.8%). Luck odds: under 1 in a billion.
8. 30n + 1: +276% (give or take 2 points). Tested 300000 outputs and found 42449 primes (14% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
9. 30n + 1 then bump the last digit: +276% (give or take 2 points). Tested 300000 outputs and found 42449 primes (14% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
10. 6n + 1: +200% (give or take 2 points). Tested 300000 outputs and found 33894 primes (11% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
11. 6n + 1 then bump the last digit: +200% (give or take 2 points). Tested 300000 outputs and found 33894 primes (11% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
12. 4n + 3 then bump the last digit: +153% (give or take 1 point). Tested 300000 outputs and found 28501 primes (9.5% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
13. 2n + 1 then bump the last digit: +152% (give or take 1 point). Tested 300000 outputs and found 28468 primes (9.5% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
14. 10n + 1: +149% (give or take 1 point). Tested 300000 outputs and found 28119 primes (9.4% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
15. 10n + 1 then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28119 primes (9.4% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
16. n then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28088 primes (9.4% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.
17. 2n then bump the last digit: +148% (give or take 1 point). Tested 300000 outputs and found 27930 primes (9.3% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.
18. 4n + 3: +102% (give or take 1 point). Tested 300000 outputs and found 22799 primes (7.6% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
19. 2n + 1: +101% (give or take 1 point). Tested 300000 outputs and found 22670 primes (7.6% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
20. n: −1% (give or take 1 point). Tested 300000 outputs and found 11116 primes (3.7% of the outputs) where chance predicts 11282 (3.8%). Luck odds: about 6 in 100.
21. 6n + 3 then bump the last digit: −25% (give or take 1 point). Tested 300000 outputs and found 8510 primes (2.8% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.
22. 2n: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.
23. 6n + 3: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.

## Equations that start with n²

Squared equations hold the highest percentages under 1 trillion because the added number can be chosen so that no small prime ever divides an output.

1. n² + n + 3399714628553118047: +972% (give or take 4 points). Tested 300000 outputs and found 75368 primes (25% of the outputs) where chance predicts 7031 (2.3%). Luck odds: under 1 in a billion. Note: outputs have 19 digits and the equation is a known record from published research.
2. n² + n + 26853927251: +859% (give or take 3 points). Tested 300000 outputs and found 116748 primes (39% of the outputs) where chance predicts 12173 (4.1%). Luck odds: under 1 in a billion.
3. n² + n + 21425625701: +842% (give or take 3 points). Tested 300000 outputs and found 115251 primes (38% of the outputs) where chance predicts 12237 (4.1%). Luck odds: under 1 in a billion.
4. n² + n + 379580297267: +840% (give or take 3 points). Tested 300000 outputs and found 105451 primes (35% of the outputs) where chance predicts 11221 (3.7%). Luck odds: under 1 in a billion.
5. n² + n + 5384581877: +830% (give or take 3 points). Tested 300000 outputs and found 116789 primes (39% of the outputs) where chance predicts 12554 (4.2%). Luck odds: under 1 in a billion.
6. n² + n + 247757: +725% (give or take 3 points). Tested 300000 outputs and found 107471 primes (36% of the outputs) where chance predicts 13030 (4.3%). Luck odds: under 1 in a billion.
7. n² + n + 72491: +640% (give or take 2 points). Tested 300000 outputs and found 96507 primes (32% of the outputs) where chance predicts 13034 (4.3%). Luck odds: under 1 in a billion.
8. n² + n + 27941: +630% (give or take 2 points). Tested 300000 outputs and found 95140 primes (32% of the outputs) where chance predicts 13036 (4.3%). Luck odds: under 1 in a billion.
9. n² − 79n + 1601: +566% (give or take 2 points). Tested 300000 outputs and found 78597 primes (26% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
10. n² − 79n + 1601 then bump the last digit: +566% (give or take 2 points). Tested 300000 outputs and found 78597 primes (26% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
11. n² + n + 41: +564% (give or take 2 points). Tested 300000 outputs and found 78263 primes (26% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
12. n² + n + 41 then bump the last digit: +564% (give or take 2 points). Tested 300000 outputs and found 78263 primes (26% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
13. 2n² + 29: +491% (give or take 2 points). Tested 300000 outputs and found 69693 primes (23% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
14. 2n² + 29 then bump the last digit: +491% (give or take 2 points). Tested 300000 outputs and found 69693 primes (23% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
15. n² + n + 17: +318% (give or take 2 points). Tested 300000 outputs and found 49315 primes (16% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
16. n² + n + 17 then bump the last digit: +318% (give or take 2 points). Tested 300000 outputs and found 49315 primes (16% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
17. n² − n − 1 then bump the last digit: +298% (give or take 2 points). Tested 300000 outputs and found 46939 primes (16% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
18. 2n² − 1: +267% (give or take 2 points). Tested 300000 outputs and found 43336 primes (14% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
19. 2n² − 1 then bump the last digit: +267% (give or take 2 points). Tested 300000 outputs and found 43336 primes (14% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
20. 4n² + 1 then bump the last digit: +266% (give or take 2 points). Tested 300000 outputs and found 43124 primes (14% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
21. n² − n − 1: +254% (give or take 2 points). Tested 300000 outputs and found 41751 primes (14% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
22. 3n² + 3n + 1: +237% (give or take 2 points). Tested 300000 outputs and found 39763 primes (13% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
23. 3n² + 3n + 1 then bump the last digit: +237% (give or take 2 points). Tested 300000 outputs and found 39763 primes (13% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
24. n² + 3 then bump the last digit: +199% (give or take 2 points). Tested 300000 outputs and found 35271 primes (12% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
25. n² − 2 then bump the last digit: +179% (give or take 2 points). Tested 300000 outputs and found 32890 primes (11% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
26. 4n² + 1: +176% (give or take 2 points). Tested 300000 outputs and found 32527 primes (11% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
27. n² + 1 then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 29573 primes (9.9% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
28. n² + n + 2 then bump the last digit: +126% (give or take 1 point). Tested 300000 outputs and found 26603 primes (8.9% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
29. n² + 5n + 6 then bump the last digit: +124% (give or take 1 point). Tested 300000 outputs and found 26395 primes (8.8% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
30. n² + n + 1: +121% (give or take 1 point). Tested 300000 outputs and found 26026 primes (8.7% of the outputs) where chance predicts 11790 (3.9%). Luck odds: under 1 in a billion.
31. n² + n + 1 then bump the last digit: +121% (give or take 1 point). Tested 300000 outputs and found 26026 primes (8.7% of the outputs) where chance predicts 11790 (3.9%). Luck odds: under 1 in a billion.
32. n² − 2: +87% (give or take 1 point). Tested 300000 outputs and found 22001 primes (7.3% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
33. n² + 1: +36% (give or take 1 point). Tested 300000 outputs and found 16062 primes (5.4% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
34. n² + 3: +12% (give or take 1 point). Tested 300000 outputs and found 13217 primes (4.4% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
35. n² − 1 then bump the last digit: +5% (give or take 1 point). Tested 300000 outputs and found 12439 primes (4.1% of the outputs) where chance predicts 11793 (3.9%). Luck odds: 1 in 500000000.
36. n² + 5n + 6: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
37. n² + n + 2: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
38. n² − 1: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.

## Mixed operations

These recipes combine several operations. A recipe that divides out small factors or keeps the largest prime factor lands high because the leftover number has fewer ways to fail.

1. the largest prime that divides n² + 1: +796% (give or take 3 points). Tested 100000 outputs and found 70780 primes (71% of the outputs) where chance predicts 7897 (7.9%). Luck odds: under 1 in a billion. Note: the recipe needs a factoring step.
2. n² + n + 41 fed back into itself: +569% (give or take 3 points). Tested 300000 outputs and found 43624 primes (15% of the outputs) where chance predicts 6521 (2.2%). Luck odds: under 1 in a billion.
3. n² + 1 with every factor of 2 and 5 divided out: +358% (give or take 2 points). Tested 300000 outputs and found 63095 primes (21% of the outputs) where chance predicts 13787 (4.6%). Luck odds: under 1 in a billion.
4. the top number of the fraction 1 + 1/2 + 1/3 up to 1/n: +333% (give or take 79 points). Tested 682 outputs and found 30 primes (4.4% of the outputs) where chance predicts 6.9 (1.0%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
5. (2n choose n) − 1: +252% (give or take 85 points). Tested 500 outputs and found 17 primes (3.4% of the outputs) where chance predicts 4.8 (0.97%). Luck odds: 1 in 80000. Note: outputs up to 300 digits.
6. (2n choose n) + 1: +238% (give or take 78 points). Tested 500 outputs and found 19 primes (3.8% of the outputs) where chance predicts 5.6 (1.1%). Luck odds: 1 in 100000. Note: outputs up to 300 digits.
7. the top number of the fraction 1 + 1/4 + 1/9 up to 1/n²: +104% (give or take 77 points). Tested 348 outputs and found 7 primes (2.0% of the outputs) where chance predicts 3.4 (0.99%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
8. (n × π with decimals dropped) × (n × e with decimals dropped) + 1: +95% (give or take 1 point). Tested 300000 outputs and found 23297 primes (7.8% of the outputs) where chance predicts 11919 (4.0%). Luck odds: under 1 in a billion.
9. (n × √2 with decimals dropped)² + (n × √3 with decimals dropped)²: +26% (give or take 1 point). Tested 300000 outputs and found 15391 primes (5.1% of the outputs) where chance predicts 12181 (4.1%). Luck odds: under 1 in a billion.

## Equations famous for a long unbroken run of primes

These equations hold records for giving a prime on 40 or more inputs in a row. The long-run percentages are high as well because the same blocked small primes that make the opening run possible keep working at every size.

1. −66n³ + 3845n² − 60897n + 251831: +747% (give or take 3 points). Tested 300000 outputs and found 65636 primes (22% of the outputs) where chance predicts 7745 (2.6%). Luck odds: under 1 in a billion.
2. 45n⁴ − 3416n³ + 96738n² − 1212769n + 5692031: +727% (give or take 4 points). Tested 300000 outputs and found 49750 primes (17% of the outputs) where chance predicts 6019 (2.0%). Luck odds: under 1 in a billion.
3. 6n⁴ − 558n³ + 19354n² − 296370n + 1688311: +706% (give or take 4 points). Tested 300000 outputs and found 50588 primes (17% of the outputs) where chance predicts 6276 (2.1%). Luck odds: under 1 in a billion.
4. 103n² − 4707n + 50383: +704% (give or take 3 points). Tested 300000 outputs and found 87135 primes (29% of the outputs) where chance predicts 10839 (3.6%). Luck odds: under 1 in a billion.
5. 36n² − 810n + 2753: +683% (give or take 3 points). Tested 300000 outputs and found 88236 primes (29% of the outputs) where chance predicts 11269 (3.8%). Luck odds: under 1 in a billion.
6. 43n² − 537n + 2971: +664% (give or take 3 points). Tested 300000 outputs and found 85512 primes (29% of the outputs) where chance predicts 11193 (3.7%). Luck odds: under 1 in a billion.
7. 47n² − 1701n + 10181: +654% (give or take 3 points). Tested 300000 outputs and found 84092 primes (28% of the outputs) where chance predicts 11157 (3.7%). Luck odds: under 1 in a billion.
8. 8n² − 488n + 7243: +634% (give or take 2 points). Tested 300000 outputs and found 87768 primes (29% of the outputs) where chance predicts 11953 (4.0%). Luck odds: under 1 in a billion.
9. 2n² − 108n + 1259: +632% (give or take 2 points). Tested 300000 outputs and found 92666 primes (31% of the outputs) where chance predicts 12660 (4.2%). Luck odds: under 1 in a billion.
10. 3n³ − 183n² + 3318n − 18757: +615% (give or take 3 points). Tested 300000 outputs and found 60222 primes (20% of the outputs) where chance predicts 8426 (2.8%). Luck odds: under 1 in a billion.

## Equations from published richness record lists

These equations sit on published record lists for richness and the measured percentages match the published scores.

1. n² + n − 501229: +701% (give or take 2 points). Tested 300000 outputs and found 104402 primes (35% of the outputs) where chance predicts 13038 (4.3%). Luck odds: under 1 in a billion.
2. 249582n² + 1: +692% (give or take 3 points). Tested 300000 outputs and found 66924 primes (22% of the outputs) where chance predicts 8445 (2.8%). Luck odds: under 1 in a billion.
3. 452042n² − 1: +687% (give or take 3 points). Tested 300000 outputs and found 65376 primes (22% of the outputs) where chance predicts 8306 (2.8%). Luck odds: under 1 in a billion.
4. n² + 2751n + 1: +648% (give or take 2 points). Tested 300000 outputs and found 97110 primes (32% of the outputs) where chance predicts 12991 (4.3%). Luck odds: under 1 in a billion.

## Recipes that start from the list of primes

Every recipe in this group needs the list of primes before the recipe can run. Adding a number built from many small primes to the nth prime gives a high percentage because a prime is never a multiple of 3 or 5 or 7 and the added number keeps that protection.

1. (the nth prime)² + the nth prime + 41: +579% (give or take 3 points). Tested 300000 outputs and found 72357 primes (24% of the outputs) where chance predicts 10658 (3.6%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
2. the nth prime + 30030: +412% (give or take 2 points). Tested 300000 outputs and found 108401 primes (36% of the outputs) where chance predicts 21189 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
3. the nth prime + 2310: +370% (give or take 1 point). Tested 300000 outputs and found 99980 primes (33% of the outputs) where chance predicts 21290 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
4. the nth prime + 210: +322% (give or take 1 point). Tested 300000 outputs and found 89972 primes (30% of the outputs) where chance predicts 21309 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
5. the nth prime + 30: +252% (give or take 1 point). Tested 300000 outputs and found 75046 primes (25% of the outputs) where chance predicts 21313 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
6. (the nth prime)² − 2: +239% (give or take 2 points). Tested 300000 outputs and found 36088 primes (12% of the outputs) where chance predicts 10659 (3.6%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
7. the nth prime + 6: +163% (give or take 1 point). Tested 300000 outputs and found 56140 primes (19% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
8. three neighboring primes added up: +162% (give or take 1 point). Tested 300000 outputs and found 51700 primes (17% of the outputs) where chance predicts 19759 (6.6%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
9. the nth prime + the next prime + 1: +147% (give or take 1 point). Tested 300000 outputs and found 50077 primes (17% of the outputs) where chance predicts 20306 (6.8%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
10. the nth prime written backward: +132% (give or take 1 point). Tested 300000 outputs and found 48180 primes (16% of the outputs) where chance predicts 20790 (6.9%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
11. (the nth prime)² + 4: +121% (give or take 1 point). Tested 300000 outputs and found 23541 primes (7.8% of the outputs) where chance predicts 10658 (3.6%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
12. n × the count of primes up to n + 1: +94% (give or take 1 point). Tested 300000 outputs and found 28216 primes (9.4% of the outputs) where chance predicts 14529 (4.8%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
13. the nth prime × the next prime + 2: +38% (give or take 1 point). Tested 300000 outputs and found 14733 primes (4.9% of the outputs) where chance predicts 10658 (3.6%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
14. the nth prime + 2: +33% (give or take 1 point). Tested 300000 outputs and found 28349 primes (9.4% of the outputs) where chance predicts 21316 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
15. the nth prime + 4: +32% (give or take 1 point). Tested 300000 outputs and found 28120 primes (9.4% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
16. 2 × the nth prime + 1: +31% (give or take 1 point). Tested 300000 outputs and found 26694 primes (8.9% of the outputs) where chance predicts 20306 (6.8%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.
17. the nth prime + n: +1% (give or take 1 point). Tested 300000 outputs and found 21347 primes (7.1% of the outputs) where chance predicts 21200 (7.1%). Luck odds: about 16 in 100 which means the gap could be luck. Note: the recipe needs the list of primes.
18. n + the count of primes up to n: 0% (give or take 1 point). Tested 300000 outputs and found 25818 primes (8.6% of the outputs) where chance predicts 25869 (8.6%). Luck odds: about 38 in 100 which means the gap could be luck. Note: the recipe needs the list of primes.
19. the nth prime − n: 0% (give or take 1 point). Tested 300000 outputs and found 21398 primes (7.1% of the outputs) where chance predicts 21443 (7.1%). Luck odds: about 38 in 100 which means the gap could be luck. Note: the recipe needs the list of primes.
20. n × the nth prime + 1: −1% (give or take 1 point). Tested 300000 outputs and found 11579 primes (3.9% of the outputs) where chance predicts 11731 (3.9%). Luck odds: about 8 in 100. Note: the recipe needs the list of primes.
21. the nth prime × the next prime − 2: −2% (give or take 1 point). Tested 300000 outputs and found 10429 primes (3.5% of the outputs) where chance predicts 10658 (3.6%). Luck odds: about 1 in 100. Note: the recipe needs the list of primes.
22. the halfway point between the nth prime and the next prime: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 21315 (7.1%). Luck odds: under 1 in a billion. Note: the recipe needs the list of primes.

## Well-known number lists

These number lists grow fast so most lines rest on a small count of primes and the luck odds on each line matter more than usual.

1. (2 to the power of the nth prime then plus 1) ÷ 3: +536% (give or take 142 points). Tested 167 outputs and found 20 primes (12% of the outputs) where chance predicts 3.1 (1.9%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits and the recipe needs the list of primes.
2. (2ⁿ − 1)² − 2: +451% (give or take 112 points). Tested 498 outputs and found 24 primes (4.8% of the outputs) where chance predicts 4.4 (0.87%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
3. (2ⁿ + 1)² − 2: +353% (give or take 99 points). Tested 498 outputs and found 21 primes (4.2% of the outputs) where chance predicts 4.6 (0.93%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
4. 2 to the power of the nth prime then minus 1: +312% (give or take 110 points). Tested 167 outputs and found 14 primes (8.4% of the outputs) where chance predicts 3.4 (2.0%). Luck odds: 1 in 70000. Note: outputs up to 300 digits and the recipe needs the list of primes.
5. the gap from (the product of the first n primes) to the next prime after that product plus 1: +312% (give or take 39 points). Tested 150 outputs and found 113 primes (75% of the outputs) where chance predicts 27.4 (18%). Luck odds: under 1 in a billion. Note: the recipe needs a search for the next prime.
6. 3 × 2ⁿ + 1: +115% (give or take 49 points). Tested 994 outputs and found 19 primes (1.9% of the outputs) where chance predicts 8.8 (0.89%). Luck odds: 1 in 500. Note: outputs up to 300 digits.
7. the list 1 then 2 then 5 then 12 then 29 where each number is twice the one before plus the one before that: +95% (give or take 49 points). Tested 784 outputs and found 16 primes (2.0% of the outputs) where chance predicts 8.2 (1.0%). Luck odds: about 1 in 100. Note: outputs up to 300 digits.
8. the list 2 then 1 then 3 then 4 then 7 where each number is the two before added up: +85% (give or take 35 points). Tested 1436 outputs and found 28 primes (1.9% of the outputs) where chance predicts 15.1 (1.1%). Luck odds: 1 in 500. Note: outputs up to 300 digits.
9. the count of ways to sort n objects into groups: +37% (give or take 56 points). Tested 215 outputs and found 6 primes (2.8% of the outputs) where chance predicts 4.4 (2.0%). Luck odds: about 28 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
10. the primes written side by side (2 then 23 then 235 then 2357 and so on): +24% (give or take 72 points). Tested 109 outputs and found 3 primes (2.8% of the outputs) where chance predicts 2.4 (2.2%). Luck odds: about 43 in 100 which means the gap could be luck. Note: outputs up to 300 digits and the recipe needs the list of primes.
11. n to the power π with decimals dropped: −1% (give or take 2 points). Tested 60000 outputs and found 1925 primes (3.2% of the outputs) where chance predicts 1936 (3.2%). Luck odds: about 41 in 100 which means the gap could be luck. Note: fewer inputs fit the precision used.
12. the list 3 then 0 then 2 then 3 then 2 then 5 where each number is the second and third numbers before added up: −16% (give or take 18 points). Tested 2457 outputs and found 22 primes (0.90% of the outputs) where chance predicts 26.2 (1.1%). Luck odds: about 24 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
13. the partition numbers (the count of ways to split n into a sum): −34% (give or take 7 points). Tested 20000 outputs and found 82 primes (0.41% of the outputs) where chance predicts 124 (0.62%). Luck odds: 1 in 20000. Note: outputs up to 152 digits.
14. the count of ways to pair up n sets of brackets: −67% (give or take 23 points). Tested 506 outputs and found 2 primes (0.40% of the outputs) where chance predicts 6.1 (1.2%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
15. 509203 × 2ⁿ − 1: −100% (give or take 18 points). Tested 977 outputs and found 0 primes (0.000% of the outputs) where chance predicts 5.7 (0.58%). Luck odds: 1 in 300. Note: outputs up to 300 digits.
16. 78557 × 2ⁿ + 1: −100% (give or take 17 points). Tested 980 outputs and found 0 primes (0.000% of the outputs) where chance predicts 5.9 (0.60%). Luck odds: 1 in 400. Note: outputs up to 300 digits.
17. the whole numbers written side by side (1 then 12 then 123 and so on): −100% (give or take 54 points). Tested 136 outputs and found 0 primes (0.000% of the outputs) where chance predicts 1.9 (1.4%). Luck odds: about 16 in 100 which means the gap could be luck. Note: outputs up to 300 digits.

## Powers of n plus 1 and related equations

A prime can divide n¹⁶ + 1 only when the prime is 1 more than a multiple of 32 so most small primes are locked out of the equations in this group.

1. n⁴ − n² + 1: +363% (give or take 3 points). Tested 300000 outputs and found 30212 primes (10% of the outputs) where chance predicts 6522 (2.2%). Luck odds: under 1 in a billion.
2. n⁶ + n⁵ + n⁴ + n³ + n² + n + 1: +346% (give or take 3 points). Tested 300000 outputs and found 19372 primes (6.5% of the outputs) where chance predicts 4348 (1.4%). Luck odds: under 1 in a billion.
3. n³² + 1: +267% (give or take 7 points). Tested 300000 outputs and found 2992 primes (1.00% of the outputs) where chance predicts 816 (0.27%). Luck odds: under 1 in a billion.
4. n¹⁶ + 1: +265% (give or take 5 points). Tested 300000 outputs and found 5952 primes (2.0% of the outputs) where chance predicts 1631 (0.54%). Luck odds: under 1 in a billion.
5. n⁴ + n³ + n² + n + 1: +194% (give or take 2 points). Tested 300000 outputs and found 19203 primes (6.4% of the outputs) where chance predicts 6522 (2.2%). Luck odds: under 1 in a billion.
6. n⁸ + 1: +110% (give or take 3 points). Tested 300000 outputs and found 6866 primes (2.3% of the outputs) where chance predicts 3262 (1.1%). Luck odds: under 1 in a billion.

## Factorials and Fibonacci numbers

Every line in this group is rough because the outputs grow so fast that fewer than 1500 outputs have 300 digits or fewer. The factorial recipes sit high because no prime up to n divides n! + 1 or n! − 1.

1. n! − 1 then bump the last digit: +360% (give or take 133 points). Tested 164 outputs and found 12 primes (7.3% of the outputs) where chance predicts 2.6 (1.6%). Luck odds: 1 in 50000. Note: outputs up to 300 digits.
2. n! − 1: +341% (give or take 127 points). Tested 164 outputs and found 12 primes (7.3% of the outputs) where chance predicts 2.7 (1.7%). Luck odds: 1 in 40000. Note: outputs up to 300 digits.
3. the nth Fibonacci number then bump the last digit: +85% (give or take 36 points). Tested 1435 outputs and found 27 primes (1.9% of the outputs) where chance predicts 14.6 (1.0%). Luck odds: 1 in 400. Note: outputs up to 300 digits.
4. the nth Fibonacci number: +44% (give or take 32 points). Tested 1434 outputs and found 20 primes (1.4% of the outputs) where chance predicts 13.8 (0.97%). Luck odds: about 7 in 100. Note: outputs up to 300 digits.

## Equations with n in the exponent

Every line in this group is rough because the outputs grow so fast that fewer than 1800 outputs have 300 digits or fewer.

1. 3ⁿ + 2 then bump the last digit: +337% (give or take 86 points). Tested 628 outputs and found 26 primes (4.1% of the outputs) where chance predicts 5.9 (0.95%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
2. 3ⁿ + 2: +296% (give or take 81 points). Tested 628 outputs and found 24 primes (3.8% of the outputs) where chance predicts 6.1 (0.96%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
3. 2ⁿ − 3 then bump the last digit: +279% (give or take 66 points). Tested 994 outputs and found 33 primes (3.3% of the outputs) where chance predicts 8.7 (0.88%). Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
4. 10ⁿ + 7: +278% (give or take 120 points). Tested 299 outputs and found 10 primes (3.3% of the outputs) where chance predicts 2.6 (0.88%). Luck odds: 1 in 2000. Note: outputs up to 300 digits.
5. 10ⁿ + 7 then bump the last digit: +278% (give or take 120 points). Tested 299 outputs and found 10 primes (3.3% of the outputs) where chance predicts 2.6 (0.88%). Luck odds: 1 in 2000. Note: outputs up to 300 digits.
6. 2ⁿ − 3: +206% (give or take 59 points). Tested 994 outputs and found 27 primes (2.7% of the outputs) where chance predicts 8.8 (0.89%). Luck odds: 1 in 2000000. Note: outputs up to 300 digits.
7. 3ⁿ − 2 then bump the last digit: +171% (give or take 70 points). Tested 627 outputs and found 15 primes (2.4% of the outputs) where chance predicts 5.5 (0.88%). Luck odds: 1 in 2000. Note: outputs up to 300 digits.
8. 3ⁿ − 2: +170% (give or take 70 points). Tested 627 outputs and found 15 primes (2.4% of the outputs) where chance predicts 5.5 (0.88%). Luck odds: 1 in 2000. Note: outputs up to 300 digits.
9. 2ⁿ ÷ n with decimals dropped then bump the last digit: +169% (give or take 46 points). Tested 1006 outputs and found 34 primes (3.4% of the outputs) where chance predicts 12.6 (1.3%). Luck odds: 1 in 2000000. Note: outputs up to 300 digits.
10. 2ⁿ ÷ 3 with decimals dropped then bump the last digit: +165% (give or take 52 points). Tested 996 outputs and found 26 primes (2.6% of the outputs) where chance predicts 9.8 (0.99%). Luck odds: 1 in 80000. Note: outputs up to 300 digits.
11. 2ⁿ + 3 then bump the last digit: +141% (give or take 50 points). Tested 996 outputs and found 23 primes (2.3% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: 1 in 6000. Note: outputs up to 300 digits.
12. 2ⁿ + n then bump the last digit: +101% (give or take 45 points). Tested 996 outputs and found 20 primes (2.0% of the outputs) where chance predicts 9.9 (1.00%). Luck odds: 1 in 300. Note: outputs up to 300 digits.
13. 1.5ⁿ with decimals dropped then bump the last digit: +94% (give or take 34 points). Tested 1702 outputs and found 33 primes (1.9% of the outputs) where chance predicts 17.0 (1.00%). Luck odds: 1 in 3000. Note: outputs up to 300 digits.
14. 2ⁿ + 3: +86% (give or take 44 points). Tested 996 outputs and found 18 primes (1.8% of the outputs) where chance predicts 9.7 (0.97%). Luck odds: about 1 in 100. Note: outputs up to 300 digits.
15. 2ⁿ − 1 then bump the last digit: +78% (give or take 43 points). Tested 995 outputs and found 17 primes (1.7% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: about 2 in 100. Note: outputs up to 300 digits.
16. nⁿ + 1 then bump the last digit: +62% (give or take 72 points). Tested 139 outputs and found 5 primes (3.6% of the outputs) where chance predicts 3.1 (2.2%). Luck odds: about 20 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
17. 2ⁿ − 1: +46% (give or take 39 points). Tested 995 outputs and found 14 primes (1.4% of the outputs) where chance predicts 9.6 (0.96%). Luck odds: about 11 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
18. 2ⁿ + n: +20% (give or take 35 points). Tested 996 outputs and found 12 primes (1.2% of the outputs) where chance predicts 10.0 (1.0%). Luck odds: about 30 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
19. 1.5ⁿ with decimals dropped: −1% (give or take 25 points). Tested 1701 outputs and found 16 primes (0.94% of the outputs) where chance predicts 16.2 (0.95%). Luck odds: about 55 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
20. 2ⁿ + 1 then bump the last digit: −10% (give or take 30 points). Tested 996 outputs and found 9 primes (0.90% of the outputs) where chance predicts 10.0 (1.0%). Luck odds: about 46 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
21. nⁿ + 1: −13% (give or take 62 points). Tested 138 outputs and found 2 primes (1.4% of the outputs) where chance predicts 2.3 (1.7%). Luck odds: about 60 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
22. 10ⁿ + 1: −26% (give or take 52 points). Tested 299 outputs and found 2 primes (0.67% of the outputs) where chance predicts 2.7 (0.91%). Luck odds: about 49 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
23. 10ⁿ + 1 then bump the last digit: −26% (give or take 52 points). Tested 299 outputs and found 2 primes (0.67% of the outputs) where chance predicts 2.7 (0.91%). Luck odds: about 49 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
24. n × 2ⁿ + 1 then bump the last digit: −43% (give or take 25 points). Tested 986 outputs and found 5 primes (0.51% of the outputs) where chance predicts 8.8 (0.89%). Luck odds: about 13 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
25. 2ⁿ + 1: −51% (give or take 22 points). Tested 996 outputs and found 5 primes (0.50% of the outputs) where chance predicts 10.1 (1.0%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
26. 2ⁿ ÷ n with decimals dropped: −51% (give or take 22 points). Tested 1003 outputs and found 5 primes (0.50% of the outputs) where chance predicts 10.2 (1.0%). Luck odds: about 6 in 100. Note: outputs up to 300 digits.
27. n × 2ⁿ + 1: −77% (give or take 16 points). Tested 986 outputs and found 2 primes (0.20% of the outputs) where chance predicts 8.8 (0.89%). Luck odds: 1 in 100. Note: outputs up to 300 digits.
28. 2ⁿ ÷ 3 with decimals dropped: −89% (give or take 11 points). Tested 995 outputs and found 1 prime (0.10% of the outputs) where chance predicts 9.0 (0.91%). Luck odds: 1 in 800. Note: outputs up to 300 digits.

## Geometry

These recipes count things in shapes such as grid points inside a circle or pieces of a cut pizza.

1. the star numbers 6 × n × (n − 1) + 1: +315% (give or take 2 points). Tested 300000 outputs and found 50145 primes (17% of the outputs) where chance predicts 12090 (4.0%). Luck odds: under 1 in a billion.
2. the count of grid points inside a circle of radius n: +102% (give or take 4 points). Tested 20000 outputs and found 2167 primes (11% of the outputs) where chance predicts 1072 (5.4%). Luck odds: under 1 in a billion. Note: the count takes long to compute.
3. the most pieces from n straight cuts of a pizza: +97% (give or take 1 point). Tested 300000 outputs and found 26500 primes (8.8% of the outputs) where chance predicts 13455 (4.5%). Luck odds: under 1 in a billion.
4. the most pieces from n flat cuts of a cake: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 9181 (3.1%). Luck odds: under 1 in a billion.

## Cubes and higher powers

Cubes and higher powers fit fewer inputs under 1 trillion (about 10000 for a cube and about 1000 for a fourth power) so the percentages in this group wobble more than the squared percentages.

1. n⁵ + 2 then bump the last digit: +262% (give or take 55 points). Tested 250 outputs and found 43 primes (17% of the outputs) where chance predicts 11.9 (4.8%). Luck odds: under 1 in a billion.
2. n³ − n + 1: +259% (give or take 9 points). Tested 9999 outputs and found 1493 primes (15% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
3. n³ − n + 1 then bump the last digit: +259% (give or take 9 points). Tested 9999 outputs and found 1493 primes (15% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
4. n⁴ + 1 then bump the last digit: +236% (give or take 28 points). Tested 998 outputs and found 149 primes (15% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
5. n³ + 2 then bump the last digit: +229% (give or take 9 points). Tested 9998 outputs and found 1368 primes (14% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
6. n³ + n² + 1: +208% (give or take 9 points). Tested 9998 outputs and found 1280 primes (13% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
7. n³ + n² + 1 then bump the last digit: +208% (give or take 9 points). Tested 9998 outputs and found 1280 primes (13% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
8. n³ + n + 1: +202% (give or take 9 points). Tested 9998 outputs and found 1254 primes (13% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
9. n³ + n + 1 then bump the last digit: +202% (give or take 9 points). Tested 9998 outputs and found 1254 primes (13% of the outputs) where chance predicts 415 (4.2%). Luck odds: under 1 in a billion.
10. n⁴ + n + 1 then bump the last digit: +164% (give or take 24 points). Tested 998 outputs and found 117 primes (12% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
11. n⁴ + 1: +148% (give or take 24 points). Tested 998 outputs and found 110 primes (11% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
12. n⁴ + n + 1: +146% (give or take 24 points). Tested 998 outputs and found 109 primes (11% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
13. n⁴ + 4 then bump the last digit: +76% (give or take 20 points). Tested 998 outputs and found 78 primes (7.8% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: 1 in 300000.
14. n⁶ + 1 then bump the last digit: +61% (give or take 57 points). Tested 98 outputs and found 8 primes (8.2% of the outputs) where chance predicts 5.0 (5.1%). Luck odds: about 13 in 100 which means the gap could be luck.
15. n³ + 2: +25% (give or take 5 points). Tested 9998 outputs and found 519 primes (5.2% of the outputs) where chance predicts 415 (4.2%). Luck odds: 1 in 2000000.
16. n⁵ + 2: +18% (give or take 31 points). Tested 250 outputs and found 14 primes (5.6% of the outputs) where chance predicts 11.9 (4.8%). Luck odds: about 31 in 100 which means the gap could be luck.
17. n⁴ + 4: −100% (give or take 2 points). Tested 998 outputs and found 0 primes (0.000% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
18. n⁴ + n² + 1: −100% (give or take 2 points). Tested 998 outputs and found 0 primes (0.000% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
19. n⁴ + n² + 1 then bump the last digit: −100% (give or take 2 points). Tested 998 outputs and found 0 primes (0.000% of the outputs) where chance predicts 44.3 (4.4%). Luck odds: under 1 in a billion.
20. n⁶ + 1: −100% (give or take 20 points). Tested 98 outputs and found 0 primes (0.000% of the outputs) where chance predicts 5.0 (5.1%). Luck odds: 1 in 100.

## Digits taken from the zeta sum

At position n the recipe takes the first n digits of a piece or a running total of the zeta sum (1/1 + 1/2 + 1/3 and so on with a power on each bottom number). Every line in this group rests on a handful of primes because each number is one digit longer than the number before.

1. the first n digits of the zeta running total 1/1² + 1/2² + 1/3² up to 1/n² then bump the last digit: +247% (give or take 100 points). Tested 2000 outputs and found 12 primes (0.60% of the outputs) where chance predicts 3.5 (0.17%). Luck odds: 1 in 4000. Note: positions 1 to 2000.
2. the first n decimal digits of the zeta piece 1/n then bump the last digit: +222% (give or take 93 points). Tested 2000 outputs and found 12 primes (0.60% of the outputs) where chance predicts 3.7 (0.19%). Luck odds: 1 in 2000. Note: positions 1 to 2000.
3. the first n decimal digits of the zeta piece 1/n³ then bump the last digit: +153% (give or take 76 points). Tested 2000 outputs and found 11 primes (0.55% of the outputs) where chance predicts 4.3 (0.22%). Luck odds: 1 in 200. Note: positions 1 to 2000.
4. the first n digits of the zeta running total 1/1 + 1/2 + 1/3 up to 1/n then bump the last digit: +78% (give or take 72 points). Tested 2000 outputs and found 6 primes (0.30% of the outputs) where chance predicts 3.4 (0.17%). Luck odds: about 13 in 100 which means the gap could be luck. Note: positions 1 to 2000.
5. the first n decimal digits of the zeta piece 1/n² then bump the last digit: +75% (give or take 66 points). Tested 2000 outputs and found 7 primes (0.35% of the outputs) where chance predicts 4.0 (0.20%). Luck odds: about 11 in 100 which means the gap could be luck. Note: positions 1 to 2000.
6. the first n digits of the zeta running total 1/1² + 1/2² + 1/3² up to 1/n²: +72% (give or take 70 points). Tested 2000 outputs and found 6 primes (0.30% of the outputs) where chance predicts 3.5 (0.17%). Luck odds: about 14 in 100 which means the gap could be luck. Note: positions 1 to 2000.
7. the first n digits of the zeta running total 1/1 + 1/2 + 1/3 up to 1/n: +18% (give or take 59 points). Tested 2000 outputs and found 4 primes (0.20% of the outputs) where chance predicts 3.4 (0.17%). Luck odds: about 44 in 100 which means the gap could be luck. Note: positions 1 to 2000.
8. the first n digits of the zeta running total 1/1³ + 1/2³ + 1/3³ up to 1/n³ then bump the last digit: +14% (give or take 57 points). Tested 2000 outputs and found 4 primes (0.20% of the outputs) where chance predicts 3.5 (0.18%). Luck odds: about 47 in 100 which means the gap could be luck. Note: positions 1 to 2000.
9. the first n decimal digits of the zeta piece 1/n: +7% (give or take 53 points). Tested 2000 outputs and found 4 primes (0.20% of the outputs) where chance predicts 3.8 (0.19%). Luck odds: about 52 in 100 which means the gap could be luck. Note: positions 1 to 2000.
10. the first n decimal digits of the zeta piece 1/n³: −9% (give or take 46 points). Tested 2000 outputs and found 4 primes (0.20% of the outputs) where chance predicts 4.4 (0.22%). Luck odds: about 55 in 100 which means the gap could be luck. Note: positions 1 to 2000.
11. the first n digits of the zeta running total 1/1³ + 1/2³ + 1/3³ up to 1/n³: −43% (give or take 40 points). Tested 2000 outputs and found 2 primes (0.10% of the outputs) where chance predicts 3.5 (0.18%). Luck odds: about 32 in 100 which means the gap could be luck. Note: positions 1 to 2000.
12. the first n decimal digits of the zeta piece 1/n²: −75% (give or take 25 points). Tested 2000 outputs and found 1 prime (0.050% of the outputs) where chance predicts 4.0 (0.20%). Luck odds: about 9 in 100. Note: positions 1 to 2000.

## Counting functions

These recipes use the count of numbers below n that share no factor with n and the total of the divisors of n.

1. n × the count of numbers below n that share no factor with n + 1: +213% (give or take 2 points). Tested 300000 outputs and found 41868 primes (14% of the outputs) where chance predicts 13392 (4.5%). Luck odds: under 1 in a billion.
2. the total of the divisors of n then plus n: −25% (give or take 1 point). Tested 300000 outputs and found 18143 primes (6.0% of the outputs) where chance predicts 24075 (8.0%). Luck odds: under 1 in a billion.
3. n + the count of numbers below n that share no factor with n: −35% (give or take 1 point). Tested 300000 outputs and found 16201 primes (5.4% of the outputs) where chance predicts 25067 (8.4%). Luck odds: under 1 in a billion.
4. the total of the divisors of n then plus 1: −36% (give or take 1 point). Tested 300000 outputs and found 15988 primes (5.3% of the outputs) where chance predicts 25120 (8.4%). Luck odds: under 1 in a billion.

## Square roots and decimal powers

Square roots scramble the outputs so the percentages sit near 0% and the bump adds about 150 points because the bump gives every output an ending of 1 or 3 or 7 or 9.

1. the leading digits of √3 then bump the last digit: +213% (give or take 99 points). Tested 1200 outputs and found 10 primes (0.83% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: 1 in 600. Note: 1200 numbers tested.
2. n to the power 1.5 then bump the last digit: +150% (give or take 1 point). Tested 300000 outputs and found 28776 primes (9.6% of the outputs) where chance predicts 11524 (3.8%). Luck odds: under 1 in a billion.
3. n to the power 2.5 then bump the last digit: +147% (give or take 3 points). Tested 63094 outputs and found 6282 primes (10.0% of the outputs) where chance predicts 2545 (4.0%). Luck odds: under 1 in a billion.
4. n × √2 then bump the last digit: +147% (give or take 1 point). Tested 300000 outputs and found 27912 primes (9.3% of the outputs) where chance predicts 11283 (3.8%). Luck odds: under 1 in a billion.
5. n² × √2 then bump the last digit: +147% (give or take 1 point). Tested 300000 outputs and found 29098 primes (9.7% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
6. the leading digits of √2 then bump the last digit: +118% (give or take 82 points). Tested 1200 outputs and found 7 primes (0.58% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: about 5 in 100. Note: 1200 numbers tested.
7. the leading digits of √3 (first 1 digit then first 2 digits and so on): +88% (give or take 77 points). Tested 1200 outputs and found 6 primes (0.50% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: about 10 in 100 which means the gap could be luck. Note: 1200 numbers tested.
8. n to the power 2.5: +2% (give or take 2 points). Tested 63094 outputs and found 2606 primes (4.1% of the outputs) where chance predicts 2545 (4.0%). Luck odds: about 12 in 100 which means the gap could be luck.
9. n to the power 1.5: 0% (give or take 1 point). Tested 300000 outputs and found 11467 primes (3.8% of the outputs) where chance predicts 11524 (3.8%). Luck odds: about 30 in 100 which means the gap could be luck.
10. n × √2: −2% (give or take 1 point). Tested 300000 outputs and found 11052 primes (3.7% of the outputs) where chance predicts 11283 (3.8%). Luck odds: about 1 in 100.
11. n² × √2: −2% (give or take 1 point). Tested 300000 outputs and found 11544 primes (3.8% of the outputs) where chance predicts 11793 (3.9%). Luck odds: about 1 in 100.
12. the leading digits of √2 (first 1 digit then first 2 digits and so on): −7% (give or take 54 points). Tested 1200 outputs and found 3 primes (0.25% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: about 60 in 100 which means the gap could be luck. Note: 1200 numbers tested.
13. √n: −100% (give or take 1 point). Tested 300000 outputs and found 101 primes (0.034% of the outputs) where chance predicts 52191 (17%). Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.

## A square divided by a whole number

Dividing a square gives a wide spread of percentages because the rounding rule decides whether each output splits into two factors.

1. n² ÷ 10 then bump the last digit: +180% (give or take 2 points). Tested 300000 outputs and found 33035 primes (11% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
2. n² ÷ 7 then bump the last digit: +136% (give or take 1 point). Tested 300000 outputs and found 27782 primes (9.3% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
3. n² ÷ 2 then bump the last digit: +135% (give or take 1 point). Tested 300000 outputs and found 27669 primes (9.2% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
4. n² ÷ 5 then bump the last digit: +120% (give or take 1 point). Tested 300000 outputs and found 26007 primes (8.7% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
5. n² ÷ 4 then bump the last digit: +108% (give or take 1 point). Tested 300000 outputs and found 24490 primes (8.2% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
6. n² ÷ 3 then bump the last digit: +101% (give or take 1 point). Tested 300000 outputs and found 23688 primes (7.9% of the outputs) where chance predicts 11791 (3.9%). Luck odds: under 1 in a billion.
7. (n² + 1) ÷ 3 then bump the last digit: +99% (give or take 1 point). Tested 299999 outputs and found 23524 primes (7.8% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
8. n² ÷ 10 with any decimals go up: +73% (give or take 1 point). Tested 300000 outputs and found 20372 primes (6.8% of the outputs) where chance predicts 11791 (3.9%). Luck odds: under 1 in a billion.
9. n² ÷ 12 with any decimals go up: +72% (give or take 1 point). Tested 300000 outputs and found 20265 primes (6.8% of the outputs) where chance predicts 11797 (3.9%). Luck odds: under 1 in a billion.
10. n² ÷ 8 with any decimals go up: +66% (give or take 1 point). Tested 300000 outputs and found 19620 primes (6.5% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
11. n² ÷ 6 with any decimals go up: +65% (give or take 1 point). Tested 300000 outputs and found 19511 primes (6.5% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
12. n² ÷ 5 with any decimals go up: +45% (give or take 1 point). Tested 300000 outputs and found 17147 primes (5.7% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
13. n² ÷ 2 with decimals of 0.3 or more go up: +37% (give or take 1 point). Tested 300000 outputs and found 16198 primes (5.4% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
14. n² ÷ 2 with decimals of 0.5 or more go up: +37% (give or take 1 point). Tested 300000 outputs and found 16199 primes (5.4% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
15. n² ÷ 2 with any decimals go up: +36% (give or take 1 point). Tested 300000 outputs and found 16098 primes (5.4% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
16. n² ÷ 10 with decimals of 0.3 or more go up: +25% (give or take 1 point). Tested 300000 outputs and found 14730 primes (4.9% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
17. n² ÷ 14: +15% (give or take 1 point). Tested 300000 outputs and found 13558 primes (4.5% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
18. n² ÷ 4 with any decimals go up: +13% (give or take 1 point). Tested 300000 outputs and found 13334 primes (4.4% of the outputs) where chance predicts 11790 (3.9%). Luck odds: under 1 in a billion.
19. n² ÷ 11 with any decimals go up: +6% (give or take 1 point). Tested 300000 outputs and found 12511 primes (4.2% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
20. n² ÷ 12 with decimals of 0.3 or more go up: +2% (give or take 1 point). Tested 300000 outputs and found 12026 primes (4.0% of the outputs) where chance predicts 11793 (3.9%). Luck odds: about 2 in 100.
21. n² ÷ 7 with decimals of 0.3 or more go up: +1% (give or take 1 point). Tested 300000 outputs and found 11923 primes (4.0% of the outputs) where chance predicts 11791 (3.9%). Luck odds: about 11 in 100 which means the gap could be luck.
22. n² ÷ 7 with decimals of 0.5 or more go up: +1% (give or take 1 point). Tested 300000 outputs and found 11962 primes (4.0% of the outputs) where chance predicts 11794 (3.9%). Luck odds: about 6 in 100.
23. n² ÷ 11 with decimals of 0.3 or more go up: −4% (give or take 1 point). Tested 300000 outputs and found 11335 primes (3.8% of the outputs) where chance predicts 11793 (3.9%). Luck odds: 1 in 90000.
24. n² ÷ 3 with any decimals go up: −6% (give or take 1 point). Tested 300000 outputs and found 11055 primes (3.7% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
25. n² ÷ 3 with decimals of 0.3 or more go up: −6% (give or take 1 point). Tested 300000 outputs and found 11138 primes (3.7% of the outputs) where chance predicts 11790 (3.9%). Luck odds: under 1 in a billion.
26. n² ÷ 6 with decimals of 0.3 or more go up: −6% (give or take 1 point). Tested 300000 outputs and found 11035 primes (3.7% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
27. n² ÷ 6 with decimals of 0.5 or more go up: −7% (give or take 1 point). Tested 300000 outputs and found 10929 primes (3.6% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
28. n² ÷ 9 with any decimals go up: −13% (give or take 1 point). Tested 300000 outputs and found 10276 primes (3.4% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
29. n² ÷ 10 with decimals of 0.5 or more go up: −14% (give or take 1 point). Tested 300000 outputs and found 10196 primes (3.4% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
30. n² ÷ 19: −19% (give or take 1 point). Tested 300000 outputs and found 9539 primes (3.2% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
31. n² ÷ 7 with any decimals go up: −19% (give or take 1 point). Tested 300000 outputs and found 9538 primes (3.2% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
32. n² ÷ 11 with decimals of 0.5 or more go up: −21% (give or take 1 point). Tested 300000 outputs and found 9275 primes (3.1% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
33. n² ÷ 5 with decimals of 0.5 or more go up: −27% (give or take 1 point). Tested 300000 outputs and found 8618 primes (2.9% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
34. n² ÷ 5 with decimals of 0.3 or more go up: −28% (give or take 1 point). Tested 300000 outputs and found 8490 primes (2.8% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
35. n² ÷ 8 with decimals of 0.5 or more go up: −31% (give or take 1 point). Tested 300000 outputs and found 8186 primes (2.7% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
36. n² ÷ 17: −32% (give or take 1 point). Tested 300000 outputs and found 7977 primes (2.7% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
37. n² ÷ 6: −32% (give or take 1 point). Tested 300000 outputs and found 7969 primes (2.7% of the outputs) where chance predicts 11791 (3.9%). Luck odds: under 1 in a billion.
38. n² ÷ 8 with decimals of 0.3 or more go up: −32% (give or take 1 point). Tested 300000 outputs and found 8024 primes (2.7% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
39. n² ÷ 11: −36% (give or take 1 point). Tested 300000 outputs and found 7581 primes (2.5% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
40. n² ÷ 7: −36% (give or take 1 point). Tested 300000 outputs and found 7508 primes (2.5% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
41. n² ÷ 18: −38% (give or take 1 point). Tested 300000 outputs and found 7266 primes (2.4% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
42. n² ÷ 13: −42% (give or take 1 point). Tested 300000 outputs and found 6870 primes (2.3% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
43. n² ÷ 12 with decimals of 0.5 or more go up: −43% (give or take 1 point). Tested 300000 outputs and found 6717 primes (2.2% of the outputs) where chance predicts 11797 (3.9%). Luck odds: under 1 in a billion.
44. n² ÷ 9 with decimals of 0.3 or more go up: −44% (give or take 1 point). Tested 300000 outputs and found 6617 primes (2.2% of the outputs) where chance predicts 11797 (3.9%). Luck odds: under 1 in a billion.
45. n² ÷ 10: −45% (give or take 1 point). Tested 300000 outputs and found 6463 primes (2.2% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
46. n² ÷ 15: −51% (give or take 1 point). Tested 300000 outputs and found 5829 primes (1.9% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
47. n² ÷ 20: −56% (give or take 1 point). Tested 300000 outputs and found 5234 primes (1.7% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
48. n² ÷ 9: −66% (give or take 1 point). Tested 300000 outputs and found 3971 primes (1.3% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
49. n² ÷ 9 with decimals of 0.5 or more go up: −69% (give or take 1 point). Tested 300000 outputs and found 3704 primes (1.2% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
50. (n² + 1) ÷ 3: −100% (give or take 1 point). Tested 299999 outputs and found 1 prime (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
51. n² ÷ 12: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
52. n² ÷ 16: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
53. n² ÷ 2: −100% (give or take 1 point). Tested 299998 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
54. n² ÷ 3: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11791 (3.9%). Luck odds: under 1 in a billion.
55. n² ÷ 3 with decimals of 0.5 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
56. n² ÷ 4: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11798 (3.9%). Luck odds: under 1 in a billion.
57. n² ÷ 4 with decimals of 0.3 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
58. n² ÷ 4 with decimals of 0.5 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
59. n² ÷ 5: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
60. n² ÷ 8: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.

## Equations and digits built from e

Recipes built from e behave like the plain number line because the endless decimals of e scramble which small primes divide the outputs. The leading-digit lines are rough because the computer could test 1200 numbers for each constant.

1. the leading digits of e then bump the last digit: +175% (give or take 83 points). Tested 1200 outputs and found 11 primes (0.92% of the outputs) where chance predicts 4.0 (0.33%). Luck odds: 1 in 400. Note: 1200 numbers tested.
2. n × e then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28106 primes (9.4% of the outputs) where chance predicts 11284 (3.8%). Luck odds: under 1 in a billion.
3. eⁿ with decimals dropped then bump the last digit: +128% (give or take 57 points). Tested 690 outputs and found 16 primes (2.3% of the outputs) where chance predicts 7.0 (1.0%). Luck odds: 1 in 400. Note: outputs up to 300 digits.
4. eⁿ with decimals dropped: +14% (give or take 43 points). Tested 689 outputs and found 7 primes (1.0% of the outputs) where chance predicts 6.1 (0.89%). Luck odds: about 41 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
5. n × e: −1% (give or take 1 point). Tested 300000 outputs and found 11227 primes (3.7% of the outputs) where chance predicts 11284 (3.8%). Luck odds: about 30 in 100 which means the gap could be luck.
6. the leading digits of e (first 1 digit then first 2 digits and so on): −2% (give or take 49 points). Tested 1200 outputs and found 4 primes (0.33% of the outputs) where chance predicts 4.1 (0.34%). Luck odds: about 61 in 100 which means the gap could be luck. Note: 1200 numbers tested.

## Other division equations

Dividing a cube or dividing by an expression with n often turns the output into a simpler hidden equation such as n² − n which means the percentage follows the hidden equation.

1. n × (n + 1) ÷ 2 then bump the last digit: +158% (give or take 1 point). Tested 300000 outputs and found 30380 primes (10% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
2. n² ÷ (n + 1) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28080 primes (9.4% of the outputs) where chance predicts 11284 (3.8%). Luck odds: under 1 in a billion.
3. n³ ÷ (n + 1) then bump the last digit: +125% (give or take 1 point). Tested 300000 outputs and found 26490 primes (8.8% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
4. (n³ + 5) ÷ (n + 1): +123% (give or take 1 point). Tested 300000 outputs and found 26332 primes (8.8% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
5. (n³ + 5) ÷ (n + 1) then bump the last digit: +123% (give or take 1 point). Tested 300000 outputs and found 26332 primes (8.8% of the outputs) where chance predicts 11794 (3.9%). Luck odds: under 1 in a billion.
6. n³ ÷ 2 then bump the last digit: +78% (give or take 6 points). Tested 12598 outputs and found 932 primes (7.4% of the outputs) where chance predicts 523 (4.2%). Luck odds: under 1 in a billion.
7. n³ ÷ 7 then bump the last digit: +69% (give or take 5 points). Tested 19127 outputs and found 1346 primes (7.0% of the outputs) where chance predicts 795 (4.2%). Luck odds: under 1 in a billion.
8. n³ ÷ 12: +30% (give or take 4 points). Tested 22891 outputs and found 1239 primes (5.4% of the outputs) where chance predicts 951 (4.2%). Luck odds: under 1 in a billion.
9. n³ ÷ 6: +29% (give or take 4 points). Tested 18168 outputs and found 973 primes (5.4% of the outputs) where chance predicts 755 (4.2%). Luck odds: under 1 in a billion.
10. n³ ÷ 15: +14% (give or take 3 points). Tested 24659 outputs and found 1166 primes (4.7% of the outputs) where chance predicts 1024 (4.2%). Luck odds: 1 in 100000.
11. n³ ÷ 20: +8% (give or take 3 points). Tested 27141 outputs and found 1220 primes (4.5% of the outputs) where chance predicts 1128 (4.2%). Luck odds: 1 in 300.
12. n³ ÷ 18: +4% (give or take 3 points). Tested 26204 outputs and found 1137 primes (4.3% of the outputs) where chance predicts 1089 (4.2%). Luck odds: about 8 in 100.
13. n⁴ ÷ (n² + 1) then bump the last digit: +4% (give or take 1 point). Tested 300000 outputs and found 12273 primes (4.1% of the outputs) where chance predicts 11795 (3.9%). Luck odds: 1 in 200000.
14. n² ÷ (n + 1): −1% (give or take 1 point). Tested 300000 outputs and found 11179 primes (3.7% of the outputs) where chance predicts 11284 (3.8%). Luck odds: about 16 in 100 which means the gap could be luck.
15. n³ ÷ 14: −5% (give or take 3 points). Tested 24098 outputs and found 953 primes (4.0% of the outputs) where chance predicts 1001 (4.2%). Luck odds: about 7 in 100.
16. n³ ÷ 17: −5% (give or take 3 points). Tested 25710 outputs and found 1011 primes (3.9% of the outputs) where chance predicts 1068 (4.2%). Luck odds: about 4 in 100.
17. n³ ÷ 10: −8% (give or take 3 points). Tested 21541 outputs and found 819 primes (3.8% of the outputs) where chance predicts 895 (4.2%). Luck odds: 1 in 200.
18. n³ ÷ 11: −11% (give or take 3 points). Tested 22237 outputs and found 820 primes (3.7% of the outputs) where chance predicts 924 (4.2%). Luck odds: 1 in 4000.
19. n³ ÷ 19: −22% (give or take 3 points). Tested 26681 outputs and found 860 primes (3.2% of the outputs) where chance predicts 1109 (4.2%). Luck odds: under 1 in a billion.
20. n³ ÷ 5: −23% (give or take 3 points). Tested 17097 outputs and found 546 primes (3.2% of the outputs) where chance predicts 710 (4.2%). Luck odds: under 1 in a billion.
21. n³ ÷ 3: −33% (give or take 3 points). Tested 14419 outputs and found 401 primes (2.8% of the outputs) where chance predicts 599 (4.2%). Luck odds: under 1 in a billion.
22. n³ ÷ 13: −44% (give or take 2 points). Tested 23510 outputs and found 545 primes (2.3% of the outputs) where chance predicts 977 (4.2%). Luck odds: under 1 in a billion.
23. n³ ÷ 7: −48% (give or take 3 points). Tested 19127 outputs and found 412 primes (2.2% of the outputs) where chance predicts 795 (4.2%). Luck odds: under 1 in a billion.
24. n ÷ 2: −50% (give or take 1 point). Tested 300000 outputs and found 13848 primes (4.6% of the outputs) where chance predicts 27785 (9.3%). Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.
25. n³ ÷ 16: −52% (give or take 2 points). Tested 25195 outputs and found 503 primes (2.0% of the outputs) where chance predicts 1047 (4.2%). Luck odds: under 1 in a billion.
26. n³ ÷ 8: −52% (give or take 2 points). Tested 19997 outputs and found 398 primes (2.0% of the outputs) where chance predicts 831 (4.2%). Luck odds: under 1 in a billion.
27. n³ ÷ 4: −67% (give or take 2 points). Tested 15871 outputs and found 218 primes (1.4% of the outputs) where chance predicts 659 (4.2%). Luck odds: under 1 in a billion.
28. n × (n + 1) ÷ 2: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.
29. n³ ÷ (n + 1): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
30. n³ ÷ 2: −100% (give or take 1 point). Tested 12598 outputs and found 1 prime (0.008% of the outputs) where chance predicts 524 (4.2%). Luck odds: under 1 in a billion.
31. n³ ÷ 9: −100% (give or take 1 point). Tested 20798 outputs and found 3 primes (0.014% of the outputs) where chance predicts 865 (4.2%). Luck odds: under 1 in a billion.
32. n⁴ ÷ (n² + 1): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.

## Equations and digits built from π

Recipes built from π behave like the plain number line because the endless decimals of π scramble which small primes divide the outputs. The leading-digit lines are rough because the computer could test 1200 numbers for each constant.

1. n² × π then bump the last digit: +153% (give or take 1 point). Tested 300000 outputs and found 29797 primes (9.9% of the outputs) where chance predicts 11796 (3.9%). Luck odds: under 1 in a billion.
2. n × π then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28289 primes (9.4% of the outputs) where chance predicts 11281 (3.8%). Luck odds: under 1 in a billion.
3. the leading digits of π then bump the last digit: +101% (give or take 71 points). Tested 1200 outputs and found 8 primes (0.67% of the outputs) where chance predicts 4.0 (0.33%). Luck odds: about 5 in 100. Note: 1200 numbers tested.
4. πⁿ with decimals dropped then bump the last digit: +46% (give or take 49 points). Tested 603 outputs and found 9 primes (1.5% of the outputs) where chance predicts 6.2 (1.0%). Luck odds: about 17 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
5. n × π: +1% (give or take 1 point). Tested 300000 outputs and found 11388 primes (3.8% of the outputs) where chance predicts 11281 (3.8%). Luck odds: about 16 in 100 which means the gap could be luck.
6. n² × π: +1% (give or take 1 point). Tested 300000 outputs and found 11868 primes (4.0% of the outputs) where chance predicts 11796 (3.9%). Luck odds: about 25 in 100 which means the gap could be luck.
7. the leading digits of π (first 1 digit then first 2 digits and so on): +1% (give or take 50 points). Tested 1200 outputs and found 4 primes (0.33% of the outputs) where chance predicts 4.0 (0.33%). Luck odds: about 56 in 100 which means the gap could be luck. Note: 1200 numbers tested.
8. n × π with any decimals go up: 0% (give or take 1 point). Tested 300000 outputs and found 11347 primes (3.8% of the outputs) where chance predicts 11307 (3.8%). Luck odds: about 36 in 100 which means the gap could be luck.
9. n × π with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 11281 primes (3.8% of the outputs) where chance predicts 11309 (3.8%). Luck odds: about 40 in 100 which means the gap could be luck.
10. n × π with decimals of 0.3 or more go up: 0% (give or take 1 point). Tested 300000 outputs and found 11352 primes (3.8% of the outputs) where chance predicts 11307 (3.8%). Luck odds: about 34 in 100 which means the gap could be luck.
11. πⁿ with decimals dropped: −2% (give or take 40 points). Tested 603 outputs and found 6 primes (1.00% of the outputs) where chance predicts 6.2 (1.0%). Luck odds: about 58 in 100 which means the gap could be luck. Note: outputs up to 300 digits.

## Logarithms

Logarithm recipes sit near 0% because a logarithm has endless decimals and the dropped decimals scramble the outputs. The recipe n ÷ ln(n) sits far lower because the same output repeats for many inputs in a row.

1. n × ln(n) then bump the last digit: +152% (give or take 1 point). Tested 300000 outputs and found 28428 primes (9.5% of the outputs) where chance predicts 11303 (3.8%). Luck odds: under 1 in a billion.
2. n² × ln(n) then bump the last digit: +152% (give or take 2 points). Tested 282270 outputs and found 28143 primes (10.0% of the outputs) where chance predicts 11147 (3.9%). Luck odds: under 1 in a billion.
3. n × ln(n) × ln(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28409 primes (9.5% of the outputs) where chance predicts 11327 (3.8%). Luck odds: under 1 in a billion.
4. n × log₂(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28335 primes (9.4% of the outputs) where chance predicts 11303 (3.8%). Luck odds: under 1 in a billion.
5. n² ÷ ln(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 29504 primes (9.8% of the outputs) where chance predicts 11753 (3.9%). Luck odds: under 1 in a billion.
6. n × log₁₀(n) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28121 primes (9.4% of the outputs) where chance predicts 11303 (3.8%). Luck odds: under 1 in a billion.
7. the leading digits of ln 2 then bump the last digit: +102% (give or take 76 points). Tested 1200 outputs and found 7 primes (0.58% of the outputs) where chance predicts 3.5 (0.29%). Luck odds: about 6 in 100. Note: 1200 numbers tested.
8. n² × ln(n): +1% (give or take 1 point). Tested 282269 outputs and found 11209 primes (4.0% of the outputs) where chance predicts 11146 (3.9%). Luck odds: about 28 in 100 which means the gap could be luck.
9. n × ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11339 primes (3.8% of the outputs) where chance predicts 11303 (3.8%). Luck odds: about 37 in 100 which means the gap could be luck.
10. n × ln(n) × ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11349 primes (3.8% of the outputs) where chance predicts 11327 (3.8%). Luck odds: about 42 in 100 which means the gap could be luck.
11. n × log₂(n): 0% (give or take 1 point). Tested 300000 outputs and found 11280 primes (3.8% of the outputs) where chance predicts 11303 (3.8%). Luck odds: about 42 in 100 which means the gap could be luck.
12. n² ÷ ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11809 primes (3.9% of the outputs) where chance predicts 11753 (3.9%). Luck odds: about 30 in 100 which means the gap could be luck.
13. n × log₁₀(n): −1% (give or take 1 point). Tested 300000 outputs and found 11237 primes (3.7% of the outputs) where chance predicts 11303 (3.8%). Luck odds: about 27 in 100 which means the gap could be luck.
14. the leading digits of ln 2 (first 1 digit then first 2 digits and so on): −43% (give or take 40 points). Tested 1200 outputs and found 2 primes (0.17% of the outputs) where chance predicts 3.5 (0.29%). Luck odds: about 32 in 100 which means the gap could be luck. Note: 1200 numbers tested.
15. n ÷ ln(n): −92% (give or take 1 point). Tested 300000 outputs and found 2645 primes (0.88% of the outputs) where chance predicts 33171 (11%). Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.

## Equations and digits built from φ (the golden ratio)

Recipes built from the golden ratio behave like the plain number line once decimals are dropped because the endless decimals scramble which small primes divide the outputs. The powers of the golden ratio measured higher at +66% and that line is rough because chance predicts just 13 primes.

1. n × φ (the golden ratio) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28340 primes (9.4% of the outputs) where chance predicts 11282 (3.8%). Luck odds: under 1 in a billion.
2. n² × φ (the golden ratio) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 29380 primes (9.8% of the outputs) where chance predicts 11789 (3.9%). Luck odds: under 1 in a billion.
3. φⁿ with decimals dropped then bump the last digit: +144% (give or take 42 points). Tested 1434 outputs and found 34 primes (2.4% of the outputs) where chance predicts 13.9 (0.97%). Luck odds: 1 in 300000. Note: outputs up to 300 digits.
4. the leading digits of φ (the golden ratio) then bump the last digit: +119% (give or take 83 points). Tested 1200 outputs and found 7 primes (0.58% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: about 4 in 100. Note: 1200 numbers tested.
5. φⁿ with decimals dropped: +66% (give or take 35 points). Tested 1433 outputs and found 22 primes (1.5% of the outputs) where chance predicts 13.3 (0.93%). Luck odds: about 2 in 100. Note: outputs up to 300 digits.
6. the leading digits of φ (the golden ratio) (first 1 digit then first 2 digits and so on): +25% (give or take 62 points). Tested 1200 outputs and found 4 primes (0.33% of the outputs) where chance predicts 3.2 (0.27%). Luck odds: about 40 in 100 which means the gap could be luck. Note: 1200 numbers tested.
7. n × φ (the golden ratio): +1% (give or take 1 point). Tested 300000 outputs and found 11418 primes (3.8% of the outputs) where chance predicts 11282 (3.8%). Luck odds: about 10 in 100 which means the gap could be luck.
8. n² × φ (the golden ratio): 0% (give or take 1 point). Tested 300000 outputs and found 11748 primes (3.9% of the outputs) where chance predicts 11789 (3.9%). Luck odds: about 35 in 100 which means the gap could be luck.

## Digit tricks

Digit tricks often force a factor. A number written twice side by side is a multiple of a number such as 1001 and a number followed by its own mirror image is a multiple of 11.

1. the digit 1 then n then the digit 1: +150% (give or take 1 point). Tested 300000 outputs and found 48580 primes (16% of the outputs) where chance predicts 19454 (6.5%). Luck odds: under 1 in a billion.
2. n × (the digit total of n) + 1: +127% (give or take 1 point). Tested 300000 outputs and found 46575 primes (16% of the outputs) where chance predicts 20524 (6.8%). Luck odds: under 1 in a billion.
3. n × (n written backward) + 1: +63% (give or take 1 point). Tested 300000 outputs and found 21049 primes (7.0% of the outputs) where chance predicts 12900 (4.3%). Luck odds: under 1 in a billion.
4. n followed by n written backward with the middle digit shared: +24% (give or take 1 point). Tested 300000 outputs and found 16876 primes (5.6% of the outputs) where chance predicts 13649 (4.5%). Luck odds: under 1 in a billion.
5. n written in base 2 and then read as a base 10 number: +15% (give or take 1 point). Tested 300000 outputs and found 9332 primes (3.1% of the outputs) where chance predicts 8093 (2.7%). Luck odds: under 1 in a billion.
6. n followed by n + 1: +4% (give or take 1 point). Tested 300000 outputs and found 12852 primes (4.3% of the outputs) where chance predicts 12334 (4.1%). Luck odds: 1 in 500000.
7. n² + (the digit total of n)²: −1% (give or take 1 point). Tested 300000 outputs and found 12882 primes (4.3% of the outputs) where chance predicts 13044 (4.3%). Luck odds: about 8 in 100.
8. the digits of n read as a base 11 number: −1% (give or take 1 point). Tested 300000 outputs and found 24841 primes (8.3% of the outputs) where chance predicts 25179 (8.4%). Luck odds: about 2 in 100.
9. n followed by the digit total of n: −3% (give or take 1 point). Tested 300000 outputs and found 18112 primes (6.0% of the outputs) where chance predicts 18636 (6.2%). Luck odds: 1 in 20000.
10. n² written backward: −3% (give or take 1 point). Tested 300000 outputs and found 12906 primes (4.3% of the outputs) where chance predicts 13340 (4.4%). Luck odds: 1 in 10000.
11. n written in base 3 and then read as a base 10 number: −20% (give or take 1 point). Tested 300000 outputs and found 10282 primes (3.4% of the outputs) where chance predicts 12873 (4.3%). Luck odds: under 1 in a billion.
12. n + (n written backward): −99% (give or take 1 point). Tested 300000 outputs and found 331 primes (0.11% of the outputs) where chance predicts 23999 (8.0%). Luck odds: under 1 in a billion.
13. n followed by n written backward: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 12334 (4.1%). Luck odds: under 1 in a billion.
14. n written twice side by side: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 12334 (4.1%). Luck odds: under 1 in a billion.

## Modulus (the remainder after division)

Modulus recipes mostly sit below 0% because the outputs stay small and repeat and a repeated prime counts once.

1. n × (n mod 7) + 1: +109% (give or take 1 point). Tested 300000 outputs and found 21168 primes (7.1% of the outputs) where chance predicts 10138 (3.4%). Luck odds: under 1 in a billion.
2. n² + n + 41 mod 1000000007: 0% (give or take 1 point). Tested 300000 outputs and found 15295 primes (5.1% of the outputs) where chance predicts 15254 (5.1%). Luck odds: about 37 in 100 which means the gap could be luck. Note: repeated primes counted once.
3. n² mod 1000003: −25% (give or take 1 point). Tested 300000 outputs and found 17667 primes (5.9% of the outputs) where chance predicts 23587 (7.9%). Luck odds: under 1 in a billion. Note: repeated primes counted once.
4. 3 to the power n mod (2n + 1): −49% (give or take 1 point). Tested 300000 outputs and found 7975 primes (2.7% of the outputs) where chance predicts 15753 (5.3%). Luck odds: under 1 in a billion. Note: repeated primes counted once.
5. 2 to the power n mod n: −79% (give or take 1 point). Tested 300000 outputs and found 6658 primes (2.2% of the outputs) where chance predicts 31021 (10%). Luck odds: under 1 in a billion. Note: repeated primes counted once.
6. 2 + (2 × n!) mod (n + 1): −91% (give or take 1 point). Tested 300000 outputs and found 25997 primes (8.7% of the outputs) where chance predicts 276294 (92%). Luck odds: under 1 in a billion. Note: a known formula whose output is 2 for most inputs and repeated primes counted once.
7. n² + (n mod 6): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 11792 (3.9%). Luck odds: under 1 in a billion.

## Trig functions (sine and cosine and tangent)

Trig recipes sit near 0% because the wave values scramble the outputs. A wave added to a prime-rich equation removes most of the extra primes because the wave breaks the dodging of small primes.

1. n² + n + 41 + 2 × the whole part of 5 × sin(n): +108% (give or take 1 point). Tested 300000 outputs and found 24489 primes (8.2% of the outputs) where chance predicts 11793 (3.9%). Luck odds: under 1 in a billion.
2. n² + n + 41 + 10 × sin(n): +8% (give or take 1 point). Tested 300000 outputs and found 12774 primes (4.3% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.
3. n × |tan(n)|: +1% (give or take 1 point). Tested 300000 outputs and found 13849 primes (4.6% of the outputs) where chance predicts 13721 (4.6%). Luck odds: about 14 in 100 which means the gap could be luck.
4. n + 1000 × sin(n): 0% (give or take 1 point). Tested 300000 outputs and found 11322 primes (3.8% of the outputs) where chance predicts 11281 (3.8%). Luck odds: about 35 in 100 which means the gap could be luck.
5. n × cos(n)²: 0% (give or take 1 point). Tested 300000 outputs and found 12018 primes (4.0% of the outputs) where chance predicts 11983 (4.0%). Luck odds: about 38 in 100 which means the gap could be luck.
6. n ÷ |sin(n)|: 0% (give or take 1 point). Tested 300000 outputs and found 13216 primes (4.4% of the outputs) where chance predicts 13252 (4.4%). Luck odds: about 38 in 100 which means the gap could be luck.
7. n² × sin(1 ÷ n): 0% (give or take 1 point). Tested 300000 outputs and found 19960 primes (6.7% of the outputs) where chance predicts 19953 (6.7%). Luck odds: about 48 in 100 which means the gap could be luck.
8. n² × |sin(n)|: 0% (give or take 1 point). Tested 300000 outputs and found 12103 primes (4.0% of the outputs) where chance predicts 12149 (4.0%). Luck odds: about 34 in 100 which means the gap could be luck.
9. n × (2 + sin(n)): −1% (give or take 1 point). Tested 300000 outputs and found 11444 primes (3.8% of the outputs) where chance predicts 11537 (3.8%). Luck odds: about 19 in 100 which means the gap could be luck.
10. n × |sin(n)|: −2% (give or take 1 point). Tested 300000 outputs and found 11405 primes (3.8% of the outputs) where chance predicts 11602 (3.9%). Luck odds: about 3 in 100.
11. 1000000 × |sin(n)|: −20% (give or take 1 point). Tested 300000 outputs and found 18328 primes (6.1% of the outputs) where chance predicts 22997 (7.7%). Luck odds: under 1 in a billion. Note: repeated primes counted once.
12. sin(e to the n) ÷ ln(n): −100% (). Tested 700 outputs and found 0 primes (0.000% of the outputs) where chance predicts 0.0 (0.000%). Luck odds: not measurable because every output is below 2. Note: every output is 0 or −1.

## Calculus (slopes and areas)

A slope or an area is another equation so the percentage follows the equation that the slope or the area turns into such as 2n + 1 for the slope of n² + n + 41.

1. slope of n² + n + 41 which is 2n + 1: +100% (give or take 1 point). Tested 300000 outputs and found 22543 primes (7.5% of the outputs) where chance predicts 11281 (3.8%). Luck odds: under 1 in a billion.
2. area under x² + x + 41 from 0 to n with decimals dropped: +6% (give or take 4 points). Tested 14421 outputs and found 636 primes (4.4% of the outputs) where chance predicts 598 (4.1%). Luck odds: about 7 in 100.
3. area under ln(x) from 1 to n with decimals dropped: +1% (give or take 1 point). Tested 300000 outputs and found 11520 primes (3.8% of the outputs) where chance predicts 11462 (3.8%). Luck odds: about 30 in 100 which means the gap could be luck.
4. area under x × sin(x)² from 0 to n with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 12516 primes (4.2% of the outputs) where chance predicts 12482 (4.2%). Luck odds: about 38 in 100 which means the gap could be luck.
5. area under 1 ÷ ln(x) from 2 to n with decimals dropped: −1% (give or take 2 points). Tested 20000 outputs and found 1594 primes (8.0% of the outputs) where chance predicts 1614 (8.1%). Luck odds: about 32 in 100 which means the gap could be luck. Note: repeated primes counted once.
6. slope of n³ + 2 which is 3n²: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime (0.000% of the outputs) where chance predicts 11795 (3.9%). Luck odds: under 1 in a billion.

## Step-by-step rules

Each recipe starts at 1 and builds the next number from the current number.

1. start at 1 and keep adding the smallest prime that does not divide the current number: +100% (give or take 1 point). Tested 300000 outputs and found 49097 primes (16% of the outputs) where chance predicts 24586 (8.2%). Luck odds: under 1 in a billion.
2. start at 1 and keep adding the digit total of the current number: +48% (give or take 1 point). Tested 300000 outputs and found 29945 primes (10.0% of the outputs) where chance predicts 20279 (6.8%). Luck odds: under 1 in a billion.
3. start at 1 and keep adding the count of 1s in the binary form of the current number: −5% (give or take 1 point). Tested 300000 outputs and found 20816 primes (6.9% of the outputs) where chance predicts 21816 (7.3%). Luck odds: under 1 in a billion.
4. start at 1 and keep adding the largest digit of the current number: −26% (give or take 1 point). Tested 300000 outputs and found 16498 primes (5.5% of the outputs) where chance predicts 22165 (7.4%). Luck odds: under 1 in a billion.
5. start at 1 and keep adding the current number written backward: −87% (give or take 13 points). Tested 703 outputs and found 1 prime (0.14% of the outputs) where chance predicts 7.9 (1.1%). Luck odds: 1 in 300. Note: outputs up to 300 digits.

## Best fractions

The best fractions for π are 3 and 22/7 and 333/106 and 355/113 and so on and the recipe tests the top number of each fraction. The lines are rough because the top numbers grow fast.

1. the top numbers of the best fractions for √2 (1 then 3 then 7 then 17 and so on): +88% (give or take 50 points). Tested 561 outputs and found 14 primes (2.5% of the outputs) where chance predicts 7.5 (1.3%). Luck odds: about 2 in 100. Note: outputs up to 300 digits.
2. the top numbers of the best fractions for π (3 then 22 then 333 then 355 and so on): +51% (give or take 53 points). Tested 561 outputs and found 8 primes (1.4% of the outputs) where chance predicts 5.3 (0.95%). Luck odds: about 17 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
3. the top numbers of the best fractions for e: +39% (give or take 44 points). Tested 392 outputs and found 10 primes (2.6% of the outputs) where chance predicts 7.2 (1.8%). Luck odds: about 19 in 100 which means the gap could be luck. Note: outputs up to 300 digits.

## Bit tricks

Bit tricks work on the base 2 form of a number. A trick that keeps every output even lands at −100%.

1. n combined with half of n by the exclusive-or rule: 0% (give or take 1 point). Tested 300000 outputs and found 25916 primes (8.6% of the outputs) where chance predicts 25995 (8.7%). Luck odds: about 31 in 100 which means the gap could be luck.
2. the binary digits of n written backward: −7% (give or take 1 point). Tested 300000 outputs and found 25956 primes (8.7% of the outputs) where chance predicts 28024 (9.3%). Luck odds: under 1 in a billion.
3. n² + (2ⁿ mod n): −33% (give or take 1 point). Tested 300000 outputs and found 8688 primes (2.9% of the outputs) where chance predicts 13043 (4.3%). Luck odds: under 1 in a billion.
4. n + (2ⁿ mod n): −41% (give or take 1 point). Tested 300000 outputs and found 15075 primes (5.0% of the outputs) where chance predicts 25479 (8.5%). Luck odds: under 1 in a billion.
5. n² combined with n by the exclusive-or rule: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 13043 (4.3%). Luck odds: under 1 in a billion.

## Equations famous for very few primes

These equations do not split into factors and still almost never give a prime because many small primes divide the outputs far more often than usual.

1. n⁶ + 1091: −97% (give or take 1 point). Tested 300000 outputs and found 132 primes (0.044% of the outputs) where chance predicts 4348 (1.4%). Luck odds: under 1 in a billion.
2. n⁶ + 29450922301244534: −99% (give or take 1 point). Tested 300000 outputs and found 26 primes (0.009% of the outputs) where chance predicts 4344 (1.4%). Luck odds: under 1 in a billion.
3. n¹² + 488669: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes (0.000% of the outputs) where chance predicts 2174 (0.72%). Luck odds: under 1 in a billion.

## Program files

The folder boring-things/research-program-files/prime-richness-scripts holds the Python files behind the list and the file master_list_data.json holds every line of the list with the raw counts.
