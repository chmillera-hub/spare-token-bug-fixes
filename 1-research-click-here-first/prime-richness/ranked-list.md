# Master list of 423 equations and sums ranked by prime percentage

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each percentage comes from a computer count and not from a written proof.

## What the list shows

The list ranks 423 equations and running sums by how many primes the outputs contain compared with plain counting numbers of the same size. The top of the list holds the recipe with the most primes and the bottom of the list holds the recipes at −100% which means the recipes that produced no primes. +859% means the recipe produced 859% more primes than the number line.

The page [grouped-list.md](grouped-list.md) holds the same lines sorted into groups by type of equation.

## The rules behind every line

An output with decimal places has the decimal places dropped with no rounding (1.99 becomes 1) unless the line names a different rounding rule.

"Bump" means the last digit of a number moves up to the nearest of 1 or 3 or 7 or 9 so 0 becomes 1 and 2 becomes 3 and 4 or 5 or 6 becomes 7 and 8 becomes 9. "Bump carried into the next addition" means a running total is bumped and the next number is added to the bumped total.

A prime that an equation outputs more than once counts once so an equation that keeps repeating the same prime gets a low percentage.

## How to judge how solid a line is

Each line carries three numbers that show how much testing stands behind the percentage because a percentage from 30 tested outputs deserves far less trust than a percentage from 300000 tested outputs.

"Give or take" is the wobble that luck alone puts on the percentage. A line that reads +341% (give or take 128 points) could have landed anywhere from about +210% to about +470% by luck while a line that reads +859% (give or take 3 points) is pinned down tightly.

"Tested" is the count of outputs the computer checked and "found" is the count of different primes among those outputs and "chance predicts" is the count of primes that ordinary numbers of the same sizes would give.

"Luck odds" works like the p-value from science. The luck odds say how often plain luck would produce a gap this large if the equation really had the same prime rate as the number line. Luck odds of 1 in 50000 mean the gap is almost surely real. Luck odds of about 10 in 100 or more mean the gap could be luck and the line says so. 70 of the 423 lines carry that warning.

## What stands out

The three lines at the very top (+1307%) are circular because those recipes add up the gaps between neighboring primes which means the recipe needs the list of primes before the recipe can run. Every total is prime so those lines show the ceiling: an equation where 100% of the outputs are prime sits near +1300% at that size.

The highest percentage from a recipe that does not need the primes in advance is +1108% for multiplying n by the product of every prime up to 1009 and adding 1. No highest possible percentage exists for that family because a longer multiplier blocks more primes (+457% for primes up to 17 and +726% up to 97 and +1030% up to 541 and +1108% up to 1009).

The highest percentages with outputs near 1 trillion belong to running sums that form a squared equation: start at 5660169547 then add 30 + 60 + 90 and so on at +865% and n² + n + 26853927251 at +859%. About 37% to 39% of the totals tested were prime where ordinary numbers of that size are prime about 4% of the time.

Carrying the bump into the next addition rescues sums that had no primes. 1 + 2 + 3 + 4 and so on moves from −100% to +222% because the carried bump locks the totals onto the two equations 2m² − 1 and 2m² + 2m − 1. Starting the same carried sum at 28 reaches +322%.

Trig functions and square roots and π and e and logarithms land near 0% because the dropped decimals scramble the outputs so each small prime divides the outputs at the ordinary rate.

A rounding rule can change a structured equation a lot. For example n² ÷ 10 sits at −44% with decimals dropped and at +73% when any decimals round up. Dropping the decimals subtracts the remainder and the remainder of a square is often a square such as 1 or 4 or 9 and a square minus a square splits into two factors.

## The ranked list

1. start at 2 then add the gaps between neighboring primes: +1307% (give or take 3 points). Tested 300000 outputs and found 300000 primes where chance predicts 21316. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
2. start at 2 then add the gaps between neighboring primes then bump each total: +1307% (give or take 3 points). Tested 300000 outputs and found 299999 primes where chance predicts 21316. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
3. the gaps between neighboring primes added up with the bump carried into the next addition: +1307% (give or take 3 points). Tested 300000 outputs and found 299999 primes where chance predicts 21315. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
4. (the product of every prime up to 1009) × n + 1: +1108% (give or take 20 points). Tested 300000 outputs and found 3713 primes where chance predicts 307. Luck odds: under 1 in a billion. Note: outputs have about 425 digits.
5. (the product of every prime up to 541) × n + 1: +1030% (give or take 14 points). Tested 300000 outputs and found 6534 primes where chance predicts 578. Luck odds: under 1 in a billion. Note: outputs have about 226 digits.
6. n² + n + 3399714628553118047: +972% (give or take 4 points). Tested 300000 outputs and found 75368 primes where chance predicts 7031. Luck odds: under 1 in a billion. Note: outputs have 19 digits and the equation is a known record from published research.
7. start at 5660169547 then add 30 + 60 + 90 and so on: +865% (give or take 3 points). Tested 300000 outputs and found 111218 primes where chance predicts 11521. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
8. start at 190514189597 then add 30 + 60 + 90 and so on: +862% (give or take 3 points). Tested 300000 outputs and found 107017 primes where chance predicts 11129. Luck odds: under 1 in a billion.
9. start at 24600021781 then add 30 + 60 + 90 and so on: +861% (give or take 3 points). Tested 300000 outputs and found 109706 primes where chance predicts 11416. Luck odds: under 1 in a billion.
10. n² + n + 26853927251: +859% (give or take 3 points). Tested 300000 outputs and found 116748 primes where chance predicts 12173. Luck odds: under 1 in a billion.
11. start at 26853927251 then add 2 + 4 + 6 + 8 and so on: +859% (give or take 3 points). Tested 300000 outputs and found 116748 primes where chance predicts 12173. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
12. start at 100800448037 then add 210 + 420 + 630 and so on: +857% (give or take 3 points). Tested 300000 outputs and found 102125 primes where chance predicts 10666. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
13. start at 29717281333 then add 6 + 12 + 18 and so on: +854% (give or take 3 points). Tested 300000 outputs and found 113475 primes where chance predicts 11889. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
14. start at 473317155281 then add 6 + 12 + 18 and so on: +846% (give or take 3 points). Tested 300000 outputs and found 104947 primes where chance predicts 11092. Luck odds: under 1 in a billion.
15. n² + n + 21425625701: +842% (give or take 3 points). Tested 300000 outputs and found 115251 primes where chance predicts 12237. Luck odds: under 1 in a billion.
16. n² + n + 379580297267: +840% (give or take 3 points). Tested 300000 outputs and found 105451 primes where chance predicts 11221. Luck odds: under 1 in a billion.
17. start at 404492439881 then add 6 + 12 + 18 and so on: +838% (give or take 3 points). Tested 300000 outputs and found 104578 primes where chance predicts 11147. Luck odds: under 1 in a billion.
18. n² + n + 5384581877: +830% (give or take 3 points). Tested 300000 outputs and found 116789 primes where chance predicts 12554. Luck odds: under 1 in a billion.
19. (the product of every prime up to 97) × n + 1: +726% (give or take 5 points). Tested 300000 outputs and found 25674 primes where chance predicts 3108. Luck odds: under 1 in a billion. Note: outputs have about 43 digits.
20. n² + n + 247757: +725% (give or take 3 points). Tested 300000 outputs and found 107471 primes where chance predicts 13030. Luck odds: under 1 in a billion.
21. n² + n + 72491: +640% (give or take 2 points). Tested 300000 outputs and found 96507 primes where chance predicts 13034. Luck odds: under 1 in a billion.
22. n² + n + 27941: +630% (give or take 2 points). Tested 300000 outputs and found 95140 primes where chance predicts 13036. Luck odds: under 1 in a billion.
23. n² − 79n + 1601: +566% (give or take 2 points). Tested 300000 outputs and found 78597 primes where chance predicts 11794. Luck odds: under 1 in a billion.
24. n² − 79n + 1601 then bump the last digit: +566% (give or take 2 points). Tested 300000 outputs and found 78597 primes where chance predicts 11794. Luck odds: under 1 in a billion.
25. n² + n + 41: +564% (give or take 2 points). Tested 300000 outputs and found 78263 primes where chance predicts 11795. Luck odds: under 1 in a billion.
26. n² + n + 41 then bump the last digit: +564% (give or take 2 points). Tested 300000 outputs and found 78263 primes where chance predicts 11795. Luck odds: under 1 in a billion.
27. start at 41 then add 2 + 4 + 6 + 8 and so on: +564% (give or take 2 points). Tested 300000 outputs and found 86613 primes where chance predicts 13042. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
28. start at 29 then add 2 + 6 + 10 + 14 and so on: +492% (give or take 2 points). Tested 300000 outputs and found 74919 primes where chance predicts 12656. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
29. 2n² + 29: +491% (give or take 2 points). Tested 300000 outputs and found 69693 primes where chance predicts 11793. Luck odds: under 1 in a billion.
30. 2n² + 29 then bump the last digit: +491% (give or take 2 points). Tested 300000 outputs and found 69693 primes where chance predicts 11793. Luck odds: under 1 in a billion.
31. 510510 × n + 1 (510510 is 2 × 3 × 5 × 7 × 11 × 13 × 17): +457% (give or take 2 points). Tested 300000 outputs and found 62894 primes where chance predicts 11295. Luck odds: under 1 in a billion.
32. start at 1 then add 30030 + 30030 + 30030 and so on: +422% (give or take 2 points). Tested 300000 outputs and found 71656 primes where chance predicts 13717. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
33. 51051 × n + 1 then bump the last digit (51051 is 3 × 7 × 11 × 13 × 17): +400% (give or take 2 points). Tested 300000 outputs and found 63523 primes where chance predicts 12706. Luck odds: under 1 in a billion.
34. start at 1 then add 2310 + 4620 + 6930 and so on (multiples of 2310): +368% (give or take 2 points). Tested 300000 outputs and found 46609 primes where chance predicts 9961. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
35. n! − 1 then bump the last digit: +360% (give or take 133 points). Tested 164 outputs and found 12 primes where chance predicts 2.6. Luck odds: 1 in 50000. Note: outputs up to 300 digits.
36. n! − 1: +341% (give or take 127 points). Tested 164 outputs and found 12 primes where chance predicts 2.7. Luck odds: 1 in 40000. Note: outputs up to 300 digits.
37. the gaps between neighboring primes added up then bump each total: +341% (give or take 1 point). Tested 300000 outputs and found 93921 primes where chance predicts 21315. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
38. start at 1 then add 210 + 210 + 210 and so on: +338% (give or take 2 points). Tested 300000 outputs and found 77774 primes where chance predicts 17762. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
39. 3ⁿ + 2 then bump the last digit: +337% (give or take 86 points). Tested 628 outputs and found 26 primes where chance predicts 5.9. Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
40. 210n + 1: +335% (give or take 2 points). Tested 300000 outputs and found 49050 primes where chance predicts 11284. Luck odds: under 1 in a billion.
41. 210n + 1 then bump the last digit: +335% (give or take 2 points). Tested 300000 outputs and found 49050 primes where chance predicts 11284. Luck odds: under 1 in a billion.
42. start at 28 then add 1 + 2 + 3 + 4 and so on with the bump carried into the next addition: +322% (give or take 2 points). Tested 300000 outputs and found 56776 primes where chance predicts 13453. Luck odds: under 1 in a billion.
43. n² + n + 17: +318% (give or take 2 points). Tested 300000 outputs and found 49315 primes where chance predicts 11793. Luck odds: under 1 in a billion.
44. n² + n + 17 then bump the last digit: +318% (give or take 2 points). Tested 300000 outputs and found 49315 primes where chance predicts 11793. Luck odds: under 1 in a billion.
45. n² − n − 1 then bump the last digit: +298% (give or take 2 points). Tested 300000 outputs and found 46939 primes where chance predicts 11794. Luck odds: under 1 in a billion.
46. start at 1 then add 210 + 420 + 630 and so on (multiples of 210): +298% (give or take 2 points). Tested 300000 outputs and found 43060 primes where chance predicts 10829. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
47. 3ⁿ + 2: +296% (give or take 81 points). Tested 628 outputs and found 24 primes where chance predicts 6.1. Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
48. 2ⁿ − 3 then bump the last digit: +279% (give or take 66 points). Tested 994 outputs and found 33 primes where chance predicts 8.7. Luck odds: under 1 in a billion. Note: outputs up to 300 digits.
49. 10ⁿ + 7: +278% (give or take 120 points). Tested 299 outputs and found 10 primes where chance predicts 2.6. Luck odds: 1 in 2000. Note: outputs up to 300 digits.
50. 10ⁿ + 7 then bump the last digit: +278% (give or take 120 points). Tested 299 outputs and found 10 primes where chance predicts 2.6. Luck odds: 1 in 2000. Note: outputs up to 300 digits.
51. 30n + 1: +276% (give or take 2 points). Tested 300000 outputs and found 42449 primes where chance predicts 11283. Luck odds: under 1 in a billion.
52. 30n + 1 then bump the last digit: +276% (give or take 2 points). Tested 300000 outputs and found 42449 primes where chance predicts 11283. Luck odds: under 1 in a billion.
53. start at 1 then add 30 + 30 + 30 and so on: +275% (give or take 1 point). Tested 300000 outputs and found 75251 primes where chance predicts 20089. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
54. 1 + 8 + 27 + 64 and so on (cubes) with the bump carried into the next addition: +274% (give or take 2 points). Tested 300000 outputs and found 25180 primes where chance predicts 6727. Luck odds: under 1 in a billion.
55. 2n² − 1: +267% (give or take 2 points). Tested 300000 outputs and found 43336 primes where chance predicts 11794. Luck odds: under 1 in a billion.
56. 2n² − 1 then bump the last digit: +267% (give or take 2 points). Tested 300000 outputs and found 43336 primes where chance predicts 11794. Luck odds: under 1 in a billion.
57. 4n² + 1 then bump the last digit: +266% (give or take 2 points). Tested 300000 outputs and found 43124 primes where chance predicts 11792. Luck odds: under 1 in a billion.
58. n⁵ + 2 then bump the last digit: +262% (give or take 55 points). Tested 250 outputs and found 43 primes where chance predicts 11.9. Luck odds: under 1 in a billion.
59. n³ − n + 1: +259% (give or take 9 points). Tested 9999 outputs and found 1493 primes where chance predicts 415. Luck odds: under 1 in a billion.
60. n³ − n + 1 then bump the last digit: +259% (give or take 9 points). Tested 9999 outputs and found 1493 primes where chance predicts 415. Luck odds: under 1 in a billion.
61. n² − n − 1: +254% (give or take 2 points). Tested 300000 outputs and found 41751 primes where chance predicts 11794. Luck odds: under 1 in a billion.
62. the first n digits of the zeta running total 1/1² + 1/2² + 1/3² up to 1/n² then bump the last digit: +247% (give or take 100 points). Tested 2000 outputs and found 12 primes where chance predicts 3.5. Luck odds: 1 in 4000. Note: positions 1 to 2000.
63. 3n² + 3n + 1: +237% (give or take 2 points). Tested 300000 outputs and found 39763 primes where chance predicts 11793. Luck odds: under 1 in a billion.
64. 3n² + 3n + 1 then bump the last digit: +237% (give or take 2 points). Tested 300000 outputs and found 39763 primes where chance predicts 11793. Luck odds: under 1 in a billion.
65. 6 + 12 + 18 + 24 and so on (multiples of 6) then bump each total: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes where chance predicts 12441. Luck odds: under 1 in a billion.
66. 6 + 12 + 18 + 24 and so on (multiples of 6) with the bump carried into the next addition: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes where chance predicts 12441. Luck odds: under 1 in a billion.
67. n⁴ + 1 then bump the last digit: +236% (give or take 28 points). Tested 998 outputs and found 149 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
68. start at 1 then add 6 + 12 + 18 + 24 and so on: +236% (give or take 2 points). Tested 300000 outputs and found 41823 primes where chance predicts 12441. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
69. n³ + 2 then bump the last digit: +229% (give or take 9 points). Tested 9998 outputs and found 1368 primes where chance predicts 415. Luck odds: under 1 in a billion.
70. start at 1 then add 4 + 8 + 12 + 16 and so on then bump each total: +226% (give or take 2 points). Tested 300000 outputs and found 41304 primes where chance predicts 12657. Luck odds: under 1 in a billion.
71. 1 + 2 + 3 + 4 and so on with the bump carried into the next addition: +222% (give or take 2 points). Tested 300000 outputs and found 43383 primes where chance predicts 13454. Luck odds: under 1 in a billion.
72. the first n decimal digits of the zeta piece 1/n then bump the last digit: +222% (give or take 93 points). Tested 2000 outputs and found 12 primes where chance predicts 3.7. Luck odds: 1 in 2000. Note: positions 1 to 2000.
73. 2 + 6 + 12 + 20 and so on (n times n + 1) then bump each total: +216% (give or take 2 points). Tested 300000 outputs and found 28438 primes where chance predicts 8986. Luck odds: under 1 in a billion.
74. 2 + 6 + 12 + 20 and so on (n times n + 1) with the bump carried into the next addition: +216% (give or take 2 points). Tested 300000 outputs and found 28438 primes where chance predicts 8986. Luck odds: under 1 in a billion.
75. the leading digits of √3 then bump the last digit: +213% (give or take 99 points). Tested 1200 outputs and found 10 primes where chance predicts 3.2. Luck odds: 1 in 600. Note: 1200 numbers tested.
76. start at 28 then add 1 + 2 + 3 + 4 and so on then bump each total: +212% (give or take 2 points). Tested 300000 outputs and found 41933 primes where chance predicts 13453. Luck odds: under 1 in a billion.
77. n³ + n² + 1: +208% (give or take 9 points). Tested 9998 outputs and found 1280 primes where chance predicts 415. Luck odds: under 1 in a billion.
78. n³ + n² + 1 then bump the last digit: +208% (give or take 9 points). Tested 9998 outputs and found 1280 primes where chance predicts 415. Luck odds: under 1 in a billion.
79. 2ⁿ − 3: +206% (give or take 59 points). Tested 994 outputs and found 27 primes where chance predicts 8.8. Luck odds: 1 in 2000000. Note: outputs up to 300 digits.
80. start at 1 then add 30 + 60 + 90 and so on (multiples of 30): +204% (give or take 2 points). Tested 300000 outputs and found 35456 primes where chance predicts 11655. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
81. n³ + n + 1: +202% (give or take 9 points). Tested 9998 outputs and found 1254 primes where chance predicts 415. Luck odds: under 1 in a billion.
82. n³ + n + 1 then bump the last digit: +202% (give or take 9 points). Tested 9998 outputs and found 1254 primes where chance predicts 415. Luck odds: under 1 in a billion.
83. 6 + 6 + 6 + 6 and so on then bump each total: +200% (give or take 1 point). Tested 300000 outputs and found 67500 primes where chance predicts 22536. Luck odds: under 1 in a billion.
84. 6n + 1: +200% (give or take 2 points). Tested 300000 outputs and found 33894 primes where chance predicts 11283. Luck odds: under 1 in a billion.
85. 6n + 1 then bump the last digit: +200% (give or take 2 points). Tested 300000 outputs and found 33894 primes where chance predicts 11283. Luck odds: under 1 in a billion.
86. n² + 3 then bump the last digit: +199% (give or take 2 points). Tested 300000 outputs and found 35271 primes where chance predicts 11796. Luck odds: under 1 in a billion.
87. 1 + 9 + 25 + 49 and so on (odd squares) with the bump carried into the next addition: +194% (give or take 2 points). Tested 300000 outputs and found 25380 primes where chance predicts 8622. Luck odds: under 1 in a billion.
88. 1 + 8 + 27 + 64 and so on (cubes) then bump each total: +185% (give or take 2 points). Tested 300000 outputs and found 19152 primes where chance predicts 6727. Luck odds: under 1 in a billion.
89. n! + 1 (1 × 2 × 3 up to n then add 1): +185% (give or take 90 points). Tested 165 outputs and found 10 primes where chance predicts 3.5. Luck odds: 1 in 300. Note: outputs up to 300 digits.
90. n² ÷ 10 then bump the last digit: +180% (give or take 2 points). Tested 300000 outputs and found 33035 primes where chance predicts 11792. Luck odds: under 1 in a billion.
91. n² − 2 then bump the last digit: +179% (give or take 2 points). Tested 300000 outputs and found 32890 primes where chance predicts 11793. Luck odds: under 1 in a billion.
92. 1 + 3 + 9 + 27 and so on (powers of 3) then bump each total: +176% (give or take 69 points). Tested 629 outputs and found 16 primes where chance predicts 5.8. Luck odds: 1 in 3000. Note: outputs up to 300 digits.
93. 4n² + 1: +176% (give or take 2 points). Tested 300000 outputs and found 32527 primes where chance predicts 11792. Luck odds: under 1 in a billion.
94. the leading digits of e then bump the last digit: +175% (give or take 83 points). Tested 1200 outputs and found 11 primes where chance predicts 4.0. Luck odds: 1 in 400. Note: 1200 numbers tested.
95. start at 1 then add 4 + 8 + 12 + 16 and so on: +173% (give or take 1 point). Tested 300000 outputs and found 34603 primes where chance predicts 12657. Luck odds: under 1 in a billion.
96. 3ⁿ − 2 then bump the last digit: +171% (give or take 70 points). Tested 627 outputs and found 15 primes where chance predicts 5.5. Luck odds: 1 in 2000. Note: outputs up to 300 digits.
97. 3ⁿ − 2: +170% (give or take 70 points). Tested 627 outputs and found 15 primes where chance predicts 5.5. Luck odds: 1 in 2000. Note: outputs up to 300 digits.
98. 1 + 4 + 9 + 16 and so on (squares) with the bump carried into the next addition: +169% (give or take 2 points). Tested 300000 outputs and found 24179 primes where chance predicts 8986. Luck odds: under 1 in a billion.
99. 2ⁿ ÷ n with decimals dropped then bump the last digit: +169% (give or take 46 points). Tested 1006 outputs and found 34 primes where chance predicts 12.6. Luck odds: 1 in 2000000. Note: outputs up to 300 digits.
100. 2ⁿ ÷ 3 with decimals dropped then bump the last digit: +165% (give or take 52 points). Tested 996 outputs and found 26 primes where chance predicts 9.8. Luck odds: 1 in 80000. Note: outputs up to 300 digits.
101. n⁴ + n + 1 then bump the last digit: +164% (give or take 24 points). Tested 998 outputs and found 117 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
102. 1 + 11 + 111 + 1111 and so on with the bump carried into the next addition: +163% (give or take 98 points). Tested 300 outputs and found 7 primes where chance predicts 2.7. Luck odds: about 2 in 100. Note: outputs up to 300 digits.
103. 1 + 2 + 3 + 4 and so on then bump each total: +159% (give or take 1 point). Tested 300000 outputs and found 34905 primes where chance predicts 13454. Luck odds: under 1 in a billion.
104. n × (n + 1) ÷ 2 then bump the last digit: +158% (give or take 1 point). Tested 300000 outputs and found 30380 primes where chance predicts 11792. Luck odds: under 1 in a billion.
105. start at 1 then add 4 + 8 + 12 + 16 and so on with the bump carried into the next addition: +158% (give or take 1 point). Tested 300000 outputs and found 32609 primes where chance predicts 12657. Luck odds: under 1 in a billion.
106. n × π with decimals dropped added up with the bump carried into the next addition: +156% (give or take 1 point). Tested 300000 outputs and found 32763 primes where chance predicts 12789. Luck odds: under 1 in a billion.
107. n × π with decimals dropped added up then bump each total: +154% (give or take 1 point). Tested 300000 outputs and found 32438 primes where chance predicts 12789. Luck odds: under 1 in a billion.
108. the digit totals of 1 and 2 and 3 and so on added up then bump each total: +154% (give or take 1 point). Tested 300000 outputs and found 52249 primes where chance predicts 20584. Luck odds: under 1 in a billion.
109. √n with decimals dropped added up with the bump carried into the next addition: +154% (give or take 1 point). Tested 300000 outputs and found 45312 primes where chance predicts 17808. Luck odds: under 1 in a billion.
110. 4n + 3 then bump the last digit: +153% (give or take 1 point). Tested 300000 outputs and found 28501 primes where chance predicts 11283. Luck odds: under 1 in a billion.
111. n² × π then bump the last digit: +153% (give or take 1 point). Tested 300000 outputs and found 29797 primes where chance predicts 11796. Luck odds: under 1 in a billion.
112. the first n decimal digits of the zeta piece 1/n³ then bump the last digit: +153% (give or take 76 points). Tested 2000 outputs and found 11 primes where chance predicts 4.3. Luck odds: 1 in 200. Note: positions 1 to 2000.
113. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime) then bump each total: +152% (give or take 2 points). Tested 300000 outputs and found 21007 primes where chance predicts 8350. Luck odds: under 1 in a billion.
114. 2n + 1 then bump the last digit: +152% (give or take 1 point). Tested 300000 outputs and found 28468 primes where chance predicts 11283. Luck odds: under 1 in a billion.
115. 4 + 9 + 25 + 49 and so on (squares of primes) then bump each total: +152% (give or take 2 points). Tested 300000 outputs and found 19635 primes where chance predicts 7797. Luck odds: under 1 in a billion.
116. n × ln(n) then bump the last digit: +152% (give or take 1 point). Tested 300000 outputs and found 28428 primes where chance predicts 11303. Luck odds: under 1 in a billion.
117. n² × ln(n) then bump the last digit: +152% (give or take 2 points). Tested 282270 outputs and found 28143 primes where chance predicts 11147. Luck odds: under 1 in a billion.
118. 2 + 5 + 11 + 17 and so on (every second prime) then bump each total: +151% (give or take 1 point). Tested 300000 outputs and found 29409 primes where chance predicts 11723. Luck odds: under 1 in a billion.
119. 2 + 5 + 11 + 17 and so on (every second prime) with the bump carried into the next addition: +151% (give or take 1 point). Tested 300000 outputs and found 29383 primes where chance predicts 11723. Luck odds: under 1 in a billion.
120. 4 + 9 + 25 + 49 and so on (squares of primes) with the bump carried into the next addition: +151% (give or take 2 points). Tested 300000 outputs and found 19553 primes where chance predicts 7797. Luck odds: under 1 in a billion.
121. n × ln(n) with decimals dropped added up then bump each total: +151% (give or take 1 point). Tested 300000 outputs and found 30500 primes where chance predicts 12143. Luck odds: under 1 in a billion.
122. n × ln(n) × ln(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28409 primes where chance predicts 11327. Luck odds: under 1 in a billion.
123. n × log₂(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28335 primes where chance predicts 11303. Luck odds: under 1 in a billion.
124. n × π then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28289 primes where chance predicts 11281. Luck odds: under 1 in a billion.
125. n × φ (the golden ratio) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 28340 primes where chance predicts 11282. Luck odds: under 1 in a billion.
126. n² + 1 then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 29573 primes where chance predicts 11795. Luck odds: under 1 in a billion.
127. n² ÷ ln(n) then bump the last digit: +151% (give or take 1 point). Tested 300000 outputs and found 29504 primes where chance predicts 11753. Luck odds: under 1 in a billion.
128. 1 + 1 + 1 + 1 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 60236 primes where chance predicts 24140. Luck odds: under 1 in a billion.
129. 1 + 16 + 81 + 256 and so on (fourth powers) with the bump carried into the next addition: +150% (give or take 2 points). Tested 300000 outputs and found 13409 primes where chance predicts 5370. Luck odds: under 1 in a billion.
130. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime) with the bump carried into the next addition: +150% (give or take 2 points). Tested 300000 outputs and found 20849 primes where chance predicts 8350. Luck odds: under 1 in a billion.
131. 2 + 2 + 2 + 2 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 60236 primes where chance predicts 24140. Luck odds: under 1 in a billion.
132. 3 + 3 + 3 + 3 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 57097 primes where chance predicts 22853. Luck odds: under 1 in a billion.
133. 6 + 6 + 6 + 6 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 55890 primes where chance predicts 22358. Luck odds: under 1 in a billion.
134. 7 + 7 + 7 + 7 and so on with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 54249 primes where chance predicts 21697. Luck odds: under 1 in a billion.
135. n to the power 1.5 then bump the last digit: +150% (give or take 1 point). Tested 300000 outputs and found 28776 primes where chance predicts 11524. Luck odds: under 1 in a billion.
136. n × ln(n) with decimals dropped added up with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 30353 primes where chance predicts 12144. Luck odds: under 1 in a billion.
137. start at 1 then add 10 + 10 + 10 and so on: +150% (give or take 1 point). Tested 300000 outputs and found 54175 primes where chance predicts 21697. Luck odds: under 1 in a billion. Note: the bump changes nothing for these totals.
138. the digit totals of 1 and 2 and 3 and so on added up with the bump carried into the next addition: +150% (give or take 1 point). Tested 300000 outputs and found 51241 primes where chance predicts 20530. Luck odds: under 1 in a billion.
139. 10n + 1: +149% (give or take 1 point). Tested 300000 outputs and found 28119 primes where chance predicts 11283. Luck odds: under 1 in a billion.
140. 10n + 1 then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28119 primes where chance predicts 11283. Luck odds: under 1 in a billion.
141. 2 + 3 + 5 + 7 and so on (primes) with the bump carried into the next addition: +149% (give or take 1 point). Tested 300000 outputs and found 30117 primes where chance predicts 12083. Luck odds: under 1 in a billion.
142. n then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28088 primes where chance predicts 11282. Luck odds: under 1 in a billion.
143. n × e then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28106 primes where chance predicts 11284. Luck odds: under 1 in a billion.
144. n × log₁₀(n) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28121 primes where chance predicts 11303. Luck odds: under 1 in a billion.
145. n! + 1 (1 × 2 × 3 up to n then add 1) then bump the last digit: +149% (give or take 75 points). Tested 166 outputs and found 11 primes where chance predicts 4.4. Luck odds: 1 in 200. Note: outputs up to 300 digits.
146. n² × φ (the golden ratio) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 29380 primes where chance predicts 11789. Luck odds: under 1 in a billion.
147. n² ÷ (n + 1) then bump the last digit: +149% (give or take 1 point). Tested 300000 outputs and found 28080 primes where chance predicts 11284. Luck odds: under 1 in a billion.
148. 2 + 3 + 5 + 7 and so on (primes) then bump each total: +148% (give or take 1 point). Tested 300000 outputs and found 29913 primes where chance predicts 12083. Luck odds: under 1 in a billion.
149. 2n then bump the last digit: +148% (give or take 1 point). Tested 300000 outputs and found 27930 primes where chance predicts 11282. Luck odds: under 1 in a billion.
150. n⁴ + 1: +148% (give or take 24 points). Tested 998 outputs and found 110 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
151. n to the power 2.5 then bump the last digit: +147% (give or take 3 points). Tested 63094 outputs and found 6282 primes where chance predicts 2545. Luck odds: under 1 in a billion.
152. n × √2 then bump the last digit: +147% (give or take 1 point). Tested 300000 outputs and found 27912 primes where chance predicts 11283. Luck odds: under 1 in a billion.
153. n² + n + 41 added up with the bump carried into the next addition: +147% (give or take 2 points). Tested 300000 outputs and found 22226 primes where chance predicts 8985. Luck odds: under 1 in a billion.
154. n² × √2 then bump the last digit: +147% (give or take 1 point). Tested 300000 outputs and found 29098 primes where chance predicts 11793. Luck odds: under 1 in a billion.
155. n⁴ + n + 1: +146% (give or take 24 points). Tested 998 outputs and found 109 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
156. φⁿ with decimals dropped then bump the last digit: +144% (give or take 42 points). Tested 1434 outputs and found 34 primes where chance predicts 13.9. Luck odds: 1 in 300000. Note: outputs up to 300 digits.
157. 2ⁿ + 3 then bump the last digit: +141% (give or take 50 points). Tested 996 outputs and found 23 primes where chance predicts 9.6. Luck odds: 1 in 6000. Note: outputs up to 300 digits.
158. n² ÷ 7 then bump the last digit: +136% (give or take 1 point). Tested 300000 outputs and found 27782 primes where chance predicts 11795. Luck odds: under 1 in a billion.
159. n² ÷ 2 then bump the last digit: +135% (give or take 1 point). Tested 300000 outputs and found 27669 primes where chance predicts 11796. Luck odds: under 1 in a billion.
160. eⁿ with decimals dropped then bump the last digit: +128% (give or take 57 points). Tested 690 outputs and found 16 primes where chance predicts 7.0. Luck odds: 1 in 400. Note: outputs up to 300 digits.
161. 1 + 11 + 111 + 1111 and so on then bump each total: +126% (give or take 91 points). Tested 300 outputs and found 6 primes where chance predicts 2.7. Luck odds: about 6 in 100. Note: outputs up to 300 digits.
162. 1 + 3 + 9 + 27 and so on (powers of 3) with the bump carried into the next addition: +126% (give or take 62 points). Tested 629 outputs and found 13 primes where chance predicts 5.8. Luck odds: 1 in 100. Note: outputs up to 300 digits.
163. n² + n + 2 then bump the last digit: +126% (give or take 1 point). Tested 300000 outputs and found 26603 primes where chance predicts 11796. Luck odds: under 1 in a billion.
164. n³ ÷ (n + 1) then bump the last digit: +125% (give or take 1 point). Tested 300000 outputs and found 26490 primes where chance predicts 11795. Luck odds: under 1 in a billion.
165. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on) with the bump carried into the next addition: +125% (give or take 2 points). Tested 100000 outputs and found 18634 primes where chance predicts 8267. Luck odds: under 1 in a billion.
166. n² + 5n + 6 then bump the last digit: +124% (give or take 1 point). Tested 300000 outputs and found 26395 primes where chance predicts 11794. Luck odds: under 1 in a billion.
167. (n³ + 5) ÷ (n + 1): +123% (give or take 1 point). Tested 300000 outputs and found 26332 primes where chance predicts 11794. Luck odds: under 1 in a billion.
168. (n³ + 5) ÷ (n + 1) then bump the last digit: +123% (give or take 1 point). Tested 300000 outputs and found 26332 primes where chance predicts 11794. Luck odds: under 1 in a billion.
169. 1 + 3 + 5 + 7 and so on (odd numbers) with the bump carried into the next addition: +123% (give or take 1 point). Tested 300000 outputs and found 29138 primes where chance predicts 13043. Luck odds: under 1 in a billion.
170. 2 + 4 + 6 + 8 and so on (even numbers) then bump each total: +123% (give or take 1 point). Tested 300000 outputs and found 29139 primes where chance predicts 13044. Luck odds: under 1 in a billion.
171. 2 + 4 + 6 + 8 and so on (even numbers) with the bump carried into the next addition: +123% (give or take 1 point). Tested 300000 outputs and found 29139 primes where chance predicts 13044. Luck odds: under 1 in a billion.
172. n² + n + 1: +121% (give or take 1 point). Tested 300000 outputs and found 26026 primes where chance predicts 11790. Luck odds: under 1 in a billion.
173. n² + n + 1 then bump the last digit: +121% (give or take 1 point). Tested 300000 outputs and found 26026 primes where chance predicts 11790. Luck odds: under 1 in a billion.
174. n² ÷ 5 then bump the last digit: +120% (give or take 1 point). Tested 300000 outputs and found 26007 primes where chance predicts 11795. Luck odds: under 1 in a billion.
175. the leading digits of φ (the golden ratio) then bump the last digit: +119% (give or take 83 points). Tested 1200 outputs and found 7 primes where chance predicts 3.2. Luck odds: about 4 in 100. Note: 1200 numbers tested.
176. the leading digits of √2 then bump the last digit: +118% (give or take 82 points). Tested 1200 outputs and found 7 primes where chance predicts 3.2. Luck odds: about 5 in 100. Note: 1200 numbers tested.
177. n × (n mod 7) + 1: +109% (give or take 1 point). Tested 300000 outputs and found 21168 primes where chance predicts 10138. Luck odds: under 1 in a billion.
178. n² + n + 41 + 2 × the whole part of 5 × sin(n): +108% (give or take 1 point). Tested 300000 outputs and found 24489 primes where chance predicts 11793. Luck odds: under 1 in a billion.
179. n² ÷ 4 then bump the last digit: +108% (give or take 1 point). Tested 300000 outputs and found 24490 primes where chance predicts 11798. Luck odds: under 1 in a billion.
180. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on) then bump each total: +103% (give or take 2 points). Tested 100000 outputs and found 17002 primes where chance predicts 8395. Luck odds: under 1 in a billion.
181. 4n + 3: +102% (give or take 1 point). Tested 300000 outputs and found 22799 primes where chance predicts 11283. Luck odds: under 1 in a billion.
182. the leading digits of ln 2 then bump the last digit: +102% (give or take 76 points). Tested 1200 outputs and found 7 primes where chance predicts 3.5. Luck odds: about 6 in 100. Note: 1200 numbers tested.
183. 2n + 1: +101% (give or take 1 point). Tested 300000 outputs and found 22670 primes where chance predicts 11283. Luck odds: under 1 in a billion.
184. 2ⁿ + n then bump the last digit: +101% (give or take 45 points). Tested 996 outputs and found 20 primes where chance predicts 9.9. Luck odds: 1 in 300. Note: outputs up to 300 digits.
185. n² ÷ 3 then bump the last digit: +101% (give or take 1 point). Tested 300000 outputs and found 23688 primes where chance predicts 11791. Luck odds: under 1 in a billion.
186. the leading digits of π then bump the last digit: +101% (give or take 71 points). Tested 1200 outputs and found 8 primes where chance predicts 4.0. Luck odds: about 5 in 100. Note: 1200 numbers tested.
187. 2 + 2 + 2 + 2 and so on then bump each total: +100% (give or take 1 point). Tested 300000 outputs and found 49096 primes where chance predicts 24586. Luck odds: under 1 in a billion.
188. slope of n² + n + 41 which is 2n + 1: +100% (give or take 1 point). Tested 300000 outputs and found 22543 primes where chance predicts 11281. Luck odds: under 1 in a billion.
189. (n² + 1) ÷ 3 then bump the last digit: +99% (give or take 1 point). Tested 299999 outputs and found 23524 primes where chance predicts 11795. Luck odds: under 1 in a billion.
190. the first n primes added up then plus 1 for even totals: +99% (give or take 1 point). Tested 300000 outputs and found 23995 primes where chance predicts 12084. Luck odds: under 1 in a billion.
191. 1 + 3 + 5 + 7 and so on (odd numbers) then bump each total: +96% (give or take 1 point). Tested 300000 outputs and found 25564 primes where chance predicts 13043. Luck odds: under 1 in a billion.
192. 1.5ⁿ with decimals dropped then bump the last digit: +94% (give or take 34 points). Tested 1702 outputs and found 33 primes where chance predicts 17.0. Luck odds: 1 in 3000. Note: outputs up to 300 digits.
193. the leading digits of √3 (first 1 digit then first 2 digits and so on): +88% (give or take 77 points). Tested 1200 outputs and found 6 primes where chance predicts 3.2. Luck odds: about 10 in 100 which means the gap could be luck. Note: 1200 numbers tested.
194. 3 + 3 + 3 + 3 and so on then bump each total: +87% (give or take 1 point). Tested 300000 outputs and found 44506 primes where chance predicts 23787. Luck odds: under 1 in a billion.
195. n² − 2: +87% (give or take 1 point). Tested 300000 outputs and found 22001 primes where chance predicts 11793. Luck odds: under 1 in a billion.
196. 2ⁿ + 3: +86% (give or take 44 points). Tested 996 outputs and found 18 primes where chance predicts 9.7. Luck odds: about 1 in 100. Note: outputs up to 300 digits.
197. n² + n + 41 added up then bump each total: +86% (give or take 1 point). Tested 300000 outputs and found 16708 primes where chance predicts 8985. Luck odds: under 1 in a billion.
198. the nth Fibonacci number then bump the last digit: +85% (give or take 36 points). Tested 1435 outputs and found 27 primes where chance predicts 14.6. Luck odds: 1 in 400. Note: outputs up to 300 digits.
199. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers) then bump each total: +82% (give or take 36 points). Tested 1435 outputs and found 25 primes where chance predicts 13.8. Luck odds: 1 in 200. Note: outputs up to 300 digits.
200. √n with decimals dropped added up then bump each total: +80% (give or take 1 point). Tested 300000 outputs and found 31998 primes where chance predicts 17820. Luck odds: under 1 in a billion.
201. 1 + 2 + 4 + 8 and so on (powers of 2) then bump each total: +78% (give or take 43 points). Tested 996 outputs and found 17 primes where chance predicts 9.6. Luck odds: about 2 in 100. Note: outputs up to 300 digits.
202. 2ⁿ − 1 then bump the last digit: +78% (give or take 43 points). Tested 995 outputs and found 17 primes where chance predicts 9.6. Luck odds: about 2 in 100. Note: outputs up to 300 digits.
203. n³ ÷ 2 then bump the last digit: +78% (give or take 6 points). Tested 12598 outputs and found 932 primes where chance predicts 523. Luck odds: under 1 in a billion.
204. the first n digits of the zeta running total 1/1 + 1/2 + 1/3 up to 1/n then bump the last digit: +78% (give or take 72 points). Tested 2000 outputs and found 6 primes where chance predicts 3.4. Luck odds: about 13 in 100 which means the gap could be luck. Note: positions 1 to 2000.
205. n⁴ + 4 then bump the last digit: +76% (give or take 20 points). Tested 998 outputs and found 78 primes where chance predicts 44.3. Luck odds: 1 in 300000.
206. start at 2 then add the gaps between neighboring primes with the bump carried into the next addition: +76% (give or take 1 point). Tested 300000 outputs and found 37465 primes where chance predicts 21315. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
207. 7 + 7 + 7 + 7 and so on then bump each total: +75% (give or take 1 point). Tested 300000 outputs and found 38940 primes where chance predicts 22276. Luck odds: under 1 in a billion.
208. the first n decimal digits of the zeta piece 1/n² then bump the last digit: +75% (give or take 66 points). Tested 2000 outputs and found 7 primes where chance predicts 4.0. Luck odds: about 11 in 100 which means the gap could be luck. Note: positions 1 to 2000.
209. 1 + 3 + 6 + 10 and so on (triangle numbers) with the bump carried into the next addition: +74% (give or take 1 point). Tested 300000 outputs and found 16011 primes where chance predicts 9179. Luck odds: under 1 in a billion.
210. n² ÷ 10 with any decimals go up: +73% (give or take 1 point). Tested 300000 outputs and found 20372 primes where chance predicts 11791. Luck odds: under 1 in a billion.
211. n² ÷ 12 with any decimals go up: +72% (give or take 1 point). Tested 300000 outputs and found 20265 primes where chance predicts 11797. Luck odds: under 1 in a billion.
212. the first n digits of the zeta running total 1/1² + 1/2² + 1/3² up to 1/n²: +72% (give or take 70 points). Tested 2000 outputs and found 6 primes where chance predicts 3.5. Luck odds: about 14 in 100 which means the gap could be luck. Note: positions 1 to 2000.
213. n³ ÷ 7 then bump the last digit: +69% (give or take 5 points). Tested 19127 outputs and found 1346 primes where chance predicts 795. Luck odds: under 1 in a billion.
214. n² ÷ 8 with any decimals go up: +66% (give or take 1 point). Tested 300000 outputs and found 19620 primes where chance predicts 11798. Luck odds: under 1 in a billion.
215. φⁿ with decimals dropped: +66% (give or take 35 points). Tested 1433 outputs and found 22 primes where chance predicts 13.3. Luck odds: about 2 in 100. Note: outputs up to 300 digits.
216. n² ÷ 6 with any decimals go up: +65% (give or take 1 point). Tested 300000 outputs and found 19511 primes where chance predicts 11795. Luck odds: under 1 in a billion.
217. nⁿ + 1 then bump the last digit: +62% (give or take 72 points). Tested 139 outputs and found 5 primes where chance predicts 3.1. Luck odds: about 20 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
218. n⁶ + 1 then bump the last digit: +61% (give or take 57 points). Tested 98 outputs and found 8 primes where chance predicts 5.0. Luck odds: about 13 in 100 which means the gap could be luck.
219. start at 28 then add 1 + 2 + 3 + 4 and so on: +56% (give or take 1 point). Tested 300000 outputs and found 21051 primes where chance predicts 13453. Luck odds: under 1 in a billion.
220. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers) with the bump carried into the next addition: +47% (give or take 33 points). Tested 1435 outputs and found 20 primes where chance predicts 13.6. Luck odds: about 6 in 100. Note: outputs up to 300 digits.
221. 1 + 2 + 4 + 8 and so on (powers of 2): +46% (give or take 39 points). Tested 996 outputs and found 14 primes where chance predicts 9.6. Luck odds: about 11 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
222. 2ⁿ − 1: +46% (give or take 39 points). Tested 995 outputs and found 14 primes where chance predicts 9.6. Luck odds: about 11 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
223. πⁿ with decimals dropped then bump the last digit: +46% (give or take 49 points). Tested 603 outputs and found 9 primes where chance predicts 6.2. Luck odds: about 17 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
224. n² ÷ 5 with any decimals go up: +45% (give or take 1 point). Tested 300000 outputs and found 17147 primes where chance predicts 11793. Luck odds: under 1 in a billion.
225. the nth Fibonacci number: +44% (give or take 32 points). Tested 1434 outputs and found 20 primes where chance predicts 13.8. Luck odds: about 7 in 100. Note: outputs up to 300 digits.
226. 1 + 9 + 25 + 49 and so on (odd squares) then bump each total: +38% (give or take 1 point). Tested 300000 outputs and found 11857 primes where chance predicts 8622. Luck odds: under 1 in a billion.
227. n² ÷ 2 with decimals of 0.3 or more go up: +37% (give or take 1 point). Tested 300000 outputs and found 16198 primes where chance predicts 11792. Luck odds: under 1 in a billion.
228. n² ÷ 2 with decimals of 0.5 or more go up: +37% (give or take 1 point). Tested 300000 outputs and found 16199 primes where chance predicts 11792. Luck odds: under 1 in a billion.
229. 1 + 2 + 4 + 8 and so on (powers of 2) with the bump carried into the next addition: +36% (give or take 38 points). Tested 996 outputs and found 13 primes where chance predicts 9.6. Luck odds: about 17 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
230. n² + 1: +36% (give or take 1 point). Tested 300000 outputs and found 16062 primes where chance predicts 11795. Luck odds: under 1 in a billion.
231. n² ÷ 2 with any decimals go up: +36% (give or take 1 point). Tested 300000 outputs and found 16098 primes where chance predicts 11795. Luck odds: under 1 in a billion.
232. 1 + 4 + 9 + 16 and so on (squares) then bump each total: +35% (give or take 1 point). Tested 300000 outputs and found 12173 primes where chance predicts 8986. Luck odds: under 1 in a billion.
233. the gaps between neighboring primes added up: +33% (give or take 1 point). Tested 300000 outputs and found 28349 primes where chance predicts 21315. Luck odds: under 1 in a billion. Note: circular because the recipe needs the list of primes to begin with.
234. n³ ÷ 12: +30% (give or take 4 points). Tested 22891 outputs and found 1239 primes where chance predicts 951. Luck odds: under 1 in a billion.
235. n³ ÷ 6: +29% (give or take 4 points). Tested 18168 outputs and found 973 primes where chance predicts 755. Luck odds: under 1 in a billion.
236. n² ÷ 10 with decimals of 0.3 or more go up: +25% (give or take 1 point). Tested 300000 outputs and found 14730 primes where chance predicts 11796. Luck odds: under 1 in a billion.
237. n³ + 2: +25% (give or take 5 points). Tested 9998 outputs and found 519 primes where chance predicts 415. Luck odds: 1 in 2000000.
238. the leading digits of φ (the golden ratio) (first 1 digit then first 2 digits and so on): +25% (give or take 62 points). Tested 1200 outputs and found 4 primes where chance predicts 3.2. Luck odds: about 40 in 100 which means the gap could be luck. Note: 1200 numbers tested.
239. 2ⁿ + n: +20% (give or take 35 points). Tested 996 outputs and found 12 primes where chance predicts 10.0. Luck odds: about 30 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
240. n⁵ + 2: +18% (give or take 31 points). Tested 250 outputs and found 14 primes where chance predicts 11.9. Luck odds: about 31 in 100 which means the gap could be luck.
241. the first n digits of the zeta running total 1/1 + 1/2 + 1/3 up to 1/n: +18% (give or take 59 points). Tested 2000 outputs and found 4 primes where chance predicts 3.4. Luck odds: about 44 in 100 which means the gap could be luck. Note: positions 1 to 2000.
242. n² ÷ 14: +15% (give or take 1 point). Tested 300000 outputs and found 13558 primes where chance predicts 11793. Luck odds: under 1 in a billion.
243. eⁿ with decimals dropped: +14% (give or take 43 points). Tested 689 outputs and found 7 primes where chance predicts 6.1. Luck odds: about 41 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
244. n³ ÷ 15: +14% (give or take 3 points). Tested 24659 outputs and found 1166 primes where chance predicts 1024. Luck odds: 1 in 100000.
245. the first n digits of the zeta running total 1/1³ + 1/2³ + 1/3³ up to 1/n³ then bump the last digit: +14% (give or take 57 points). Tested 2000 outputs and found 4 primes where chance predicts 3.5. Luck odds: about 47 in 100 which means the gap could be luck. Note: positions 1 to 2000.
246. n² ÷ 4 with any decimals go up: +13% (give or take 1 point). Tested 300000 outputs and found 13334 primes where chance predicts 11790. Luck odds: under 1 in a billion.
247. n² + 3: +12% (give or take 1 point). Tested 300000 outputs and found 13217 primes where chance predicts 11796. Luck odds: under 1 in a billion.
248. n² + n + 41 + 10 × sin(n): +8% (give or take 1 point). Tested 300000 outputs and found 12774 primes where chance predicts 11795. Luck odds: under 1 in a billion.
249. n³ ÷ 20: +8% (give or take 3 points). Tested 27141 outputs and found 1220 primes where chance predicts 1128. Luck odds: 1 in 300.
250. the first n decimal digits of the zeta piece 1/n: +7% (give or take 53 points). Tested 2000 outputs and found 4 primes where chance predicts 3.8. Luck odds: about 52 in 100 which means the gap could be luck. Note: positions 1 to 2000.
251. area under x² + x + 41 from 0 to n with decimals dropped: +6% (give or take 4 points). Tested 14421 outputs and found 636 primes where chance predicts 598. Luck odds: about 7 in 100.
252. n² ÷ 11 with any decimals go up: +6% (give or take 1 point). Tested 300000 outputs and found 12511 primes where chance predicts 11795. Luck odds: under 1 in a billion.
253. n² − 1 then bump the last digit: +5% (give or take 1 point). Tested 300000 outputs and found 12439 primes where chance predicts 11793. Luck odds: 1 in 500000000.
254. n × π with decimals dropped added up: +4% (give or take 1 point). Tested 300000 outputs and found 13352 primes where chance predicts 12789. Luck odds: 1 in 3000000.
255. n³ ÷ 18: +4% (give or take 3 points). Tested 26204 outputs and found 1137 primes where chance predicts 1089. Luck odds: about 8 in 100.
256. n⁴ ÷ (n² + 1) then bump the last digit: +4% (give or take 1 point). Tested 300000 outputs and found 12273 primes where chance predicts 11795. Luck odds: 1 in 200000.
257. n to the power 2.5: +2% (give or take 2 points). Tested 63094 outputs and found 2606 primes where chance predicts 2545. Luck odds: about 12 in 100 which means the gap could be luck.
258. n² ÷ 12 with decimals of 0.3 or more go up: +2% (give or take 1 point). Tested 300000 outputs and found 12026 primes where chance predicts 11793. Luck odds: about 2 in 100.
259. 2 + 5 + 11 + 17 and so on (every second prime): +1% (give or take 1 point). Tested 300000 outputs and found 11845 primes where chance predicts 11723. Luck odds: about 13 in 100 which means the gap could be luck.
260. area under ln(x) from 1 to n with decimals dropped: +1% (give or take 1 point). Tested 300000 outputs and found 11520 primes where chance predicts 11462. Luck odds: about 30 in 100 which means the gap could be luck.
261. n × ln(n) with decimals dropped added up: +1% (give or take 1 point). Tested 300000 outputs and found 12315 primes where chance predicts 12144. Luck odds: about 6 in 100.
262. n × |tan(n)|: +1% (give or take 1 point). Tested 300000 outputs and found 13849 primes where chance predicts 13721. Luck odds: about 14 in 100 which means the gap could be luck.
263. n × π: +1% (give or take 1 point). Tested 300000 outputs and found 11388 primes where chance predicts 11281. Luck odds: about 16 in 100 which means the gap could be luck.
264. n × φ (the golden ratio): +1% (give or take 1 point). Tested 300000 outputs and found 11418 primes where chance predicts 11282. Luck odds: about 10 in 100 which means the gap could be luck.
265. n² × ln(n): +1% (give or take 1 point). Tested 282269 outputs and found 11209 primes where chance predicts 11146. Luck odds: about 28 in 100 which means the gap could be luck.
266. n² × π: +1% (give or take 1 point). Tested 300000 outputs and found 11868 primes where chance predicts 11796. Luck odds: about 25 in 100 which means the gap could be luck.
267. n² ÷ 7 with decimals of 0.3 or more go up: +1% (give or take 1 point). Tested 300000 outputs and found 11923 primes where chance predicts 11791. Luck odds: about 11 in 100 which means the gap could be luck.
268. n² ÷ 7 with decimals of 0.5 or more go up: +1% (give or take 1 point). Tested 300000 outputs and found 11962 primes where chance predicts 11794. Luck odds: about 6 in 100.
269. n÷1 + n÷2 + n÷3 up to n÷n with decimals dropped in each piece: +1% (give or take 1 point). Tested 300000 outputs and found 21800 primes where chance predicts 21482. Luck odds: about 2 in 100.
270. the leading digits of π (first 1 digit then first 2 digits and so on): +1% (give or take 50 points). Tested 1200 outputs and found 4 primes where chance predicts 4.0. Luck odds: about 56 in 100 which means the gap could be luck. Note: 1200 numbers tested.
271. 1 + 1 + 1 + 1 and so on: 0% (give or take 1 point). Tested 300000 outputs and found 25997 primes where chance predicts 26086. Luck odds: about 29 in 100 which means the gap could be luck.
272. 1 + 1 + 1 + 1 and so on then bump each total: 0% (give or take 1 point). Tested 300000 outputs and found 25995 primes where chance predicts 26085. Luck odds: about 29 in 100 which means the gap could be luck.
273. 1 + 3 + 9 + 27 and so on (powers of 3): 0% (give or take 41 points). Tested 629 outputs and found 6 primes where chance predicts 6.0. Luck odds: about 55 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
274. 1 × 2 + 2 × 3 + 3 × 5 + 4 × 7 and so on (n times the nth prime): 0% (give or take 1 point). Tested 300000 outputs and found 8367 primes where chance predicts 8350. Luck odds: about 43 in 100 which means the gap could be luck.
275. area under x × sin(x)² from 0 to n with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 12516 primes where chance predicts 12482. Luck odds: about 38 in 100 which means the gap could be luck.
276. n + 1000 × sin(n): 0% (give or take 1 point). Tested 300000 outputs and found 11322 primes where chance predicts 11281. Luck odds: about 35 in 100 which means the gap could be luck.
277. n to the power 1.5: 0% (give or take 1 point). Tested 300000 outputs and found 11467 primes where chance predicts 11524. Luck odds: about 30 in 100 which means the gap could be luck.
278. n × (1 + 1/2 + 1/3 up to 1/n) with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 21340 primes where chance predicts 21425. Luck odds: about 28 in 100 which means the gap could be luck.
279. n × cos(n)²: 0% (give or take 1 point). Tested 300000 outputs and found 12018 primes where chance predicts 11983. Luck odds: about 38 in 100 which means the gap could be luck.
280. n × ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11339 primes where chance predicts 11303. Luck odds: about 37 in 100 which means the gap could be luck.
281. n × ln(n) × ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11349 primes where chance predicts 11327. Luck odds: about 42 in 100 which means the gap could be luck.
282. n × log₂(n): 0% (give or take 1 point). Tested 300000 outputs and found 11280 primes where chance predicts 11303. Luck odds: about 42 in 100 which means the gap could be luck.
283. n × π with any decimals go up: 0% (give or take 1 point). Tested 300000 outputs and found 11347 primes where chance predicts 11307. Luck odds: about 36 in 100 which means the gap could be luck.
284. n × π with decimals dropped: 0% (give or take 1 point). Tested 300000 outputs and found 11281 primes where chance predicts 11309. Luck odds: about 40 in 100 which means the gap could be luck.
285. n × π with decimals of 0.3 or more go up: 0% (give or take 1 point). Tested 300000 outputs and found 11352 primes where chance predicts 11307. Luck odds: about 34 in 100 which means the gap could be luck.
286. n ÷ |sin(n)|: 0% (give or take 1 point). Tested 300000 outputs and found 13216 primes where chance predicts 13252. Luck odds: about 38 in 100 which means the gap could be luck.
287. n² + n + 41 mod 1000000007: 0% (give or take 1 point). Tested 300000 outputs and found 15295 primes where chance predicts 15254. Luck odds: about 37 in 100 which means the gap could be luck. Note: repeated primes counted once.
288. n² × sin(1 ÷ n): 0% (give or take 1 point). Tested 300000 outputs and found 19960 primes where chance predicts 19953. Luck odds: about 48 in 100 which means the gap could be luck.
289. n² × |sin(n)|: 0% (give or take 1 point). Tested 300000 outputs and found 12103 primes where chance predicts 12149. Luck odds: about 34 in 100 which means the gap could be luck.
290. n² × φ (the golden ratio): 0% (give or take 1 point). Tested 300000 outputs and found 11748 primes where chance predicts 11789. Luck odds: about 35 in 100 which means the gap could be luck.
291. n² ÷ ln(n): 0% (give or take 1 point). Tested 300000 outputs and found 11809 primes where chance predicts 11753. Luck odds: about 30 in 100 which means the gap could be luck.
292. 1 + 3 + 6 + 10 and so on (triangle numbers) then bump each total: −1% (give or take 1 point). Tested 300000 outputs and found 9080 primes where chance predicts 9179. Luck odds: about 15 in 100 which means the gap could be luck.
293. 1.5ⁿ with decimals dropped: −1% (give or take 25 points). Tested 1701 outputs and found 16 primes where chance predicts 16.2. Luck odds: about 55 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
294. 2 + 3 + 5 + 7 and so on (primes): −1% (give or take 1 point). Tested 300000 outputs and found 12012 primes where chance predicts 12084. Luck odds: about 26 in 100 which means the gap could be luck.
295. 4 + 9 + 25 + 49 and so on (squares of primes): −1% (give or take 1 point). Tested 300000 outputs and found 7749 primes where chance predicts 7797. Luck odds: about 30 in 100 which means the gap could be luck.
296. area under 1 ÷ ln(x) from 2 to n with decimals dropped: −1% (give or take 2 points). Tested 20000 outputs and found 1594 primes where chance predicts 1614. Luck odds: about 32 in 100 which means the gap could be luck. Note: repeated primes counted once.
297. n: −1% (give or take 1 point). Tested 300000 outputs and found 11116 primes where chance predicts 11282. Luck odds: about 6 in 100.
298. n × (2 + sin(n)): −1% (give or take 1 point). Tested 300000 outputs and found 11444 primes where chance predicts 11537. Luck odds: about 19 in 100 which means the gap could be luck.
299. n × e: −1% (give or take 1 point). Tested 300000 outputs and found 11227 primes where chance predicts 11284. Luck odds: about 30 in 100 which means the gap could be luck.
300. n × log₁₀(n): −1% (give or take 1 point). Tested 300000 outputs and found 11237 primes where chance predicts 11303. Luck odds: about 27 in 100 which means the gap could be luck.
301. n² ÷ (n + 1): −1% (give or take 1 point). Tested 300000 outputs and found 11179 primes where chance predicts 11284. Luck odds: about 16 in 100 which means the gap could be luck.
302. the first n primes added up: −1% (give or take 1 point). Tested 300000 outputs and found 12012 primes where chance predicts 12084. Luck odds: about 26 in 100 which means the gap could be luck.
303. n × |sin(n)|: −2% (give or take 1 point). Tested 300000 outputs and found 11405 primes where chance predicts 11602. Luck odds: about 3 in 100.
304. n × √2: −2% (give or take 1 point). Tested 300000 outputs and found 11052 primes where chance predicts 11283. Luck odds: about 1 in 100.
305. n² × √2: −2% (give or take 1 point). Tested 300000 outputs and found 11544 primes where chance predicts 11793. Luck odds: about 1 in 100.
306. the leading digits of e (first 1 digit then first 2 digits and so on): −2% (give or take 49 points). Tested 1200 outputs and found 4 primes where chance predicts 4.1. Luck odds: about 61 in 100 which means the gap could be luck. Note: 1200 numbers tested.
307. πⁿ with decimals dropped: −2% (give or take 40 points). Tested 603 outputs and found 6 primes where chance predicts 6.2. Luck odds: about 58 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
308. n² ÷ 11 with decimals of 0.3 or more go up: −4% (give or take 1 point). Tested 300000 outputs and found 11335 primes where chance predicts 11793. Luck odds: 1 in 90000.
309. n³ ÷ 14: −5% (give or take 3 points). Tested 24098 outputs and found 953 primes where chance predicts 1001. Luck odds: about 7 in 100.
310. n³ ÷ 17: −5% (give or take 3 points). Tested 25710 outputs and found 1011 primes where chance predicts 1068. Luck odds: about 4 in 100.
311. n² ÷ 3 with any decimals go up: −6% (give or take 1 point). Tested 300000 outputs and found 11055 primes where chance predicts 11792. Luck odds: under 1 in a billion.
312. n² ÷ 3 with decimals of 0.3 or more go up: −6% (give or take 1 point). Tested 300000 outputs and found 11138 primes where chance predicts 11790. Luck odds: under 1 in a billion.
313. n² ÷ 6 with decimals of 0.3 or more go up: −6% (give or take 1 point). Tested 300000 outputs and found 11035 primes where chance predicts 11796. Luck odds: under 1 in a billion.
314. n² ÷ 6 with decimals of 0.5 or more go up: −7% (give or take 1 point). Tested 300000 outputs and found 10929 primes where chance predicts 11794. Luck odds: under 1 in a billion.
315. the leading digits of √2 (first 1 digit then first 2 digits and so on): −7% (give or take 54 points). Tested 1200 outputs and found 3 primes where chance predicts 3.2. Luck odds: about 60 in 100 which means the gap could be luck. Note: 1200 numbers tested.
316. n³ ÷ 10: −8% (give or take 3 points). Tested 21541 outputs and found 819 primes where chance predicts 895. Luck odds: 1 in 200.
317. the first n decimal digits of the zeta piece 1/n³: −9% (give or take 46 points). Tested 2000 outputs and found 4 primes where chance predicts 4.4. Luck odds: about 55 in 100 which means the gap could be luck. Note: positions 1 to 2000.
318. 2ⁿ + 1 then bump the last digit: −10% (give or take 30 points). Tested 996 outputs and found 9 primes where chance predicts 10.0. Luck odds: about 46 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
319. n³ ÷ 11: −11% (give or take 3 points). Tested 22237 outputs and found 820 primes where chance predicts 924. Luck odds: 1 in 4000.
320. the digits of π added up (3 + 1 + 4 + 1 + 5 and so on): −11% (give or take 1 point). Tested 100000 outputs and found 7474 primes where chance predicts 8395. Luck odds: under 1 in a billion.
321. n² ÷ 9 with any decimals go up: −13% (give or take 1 point). Tested 300000 outputs and found 10276 primes where chance predicts 11798. Luck odds: under 1 in a billion.
322. nⁿ + 1: −13% (give or take 62 points). Tested 138 outputs and found 2 primes where chance predicts 2.3. Luck odds: about 60 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
323. n² ÷ 10 with decimals of 0.5 or more go up: −14% (give or take 1 point). Tested 300000 outputs and found 10196 primes where chance predicts 11793. Luck odds: under 1 in a billion.
324. n² ÷ 19: −19% (give or take 1 point). Tested 300000 outputs and found 9539 primes where chance predicts 11798. Luck odds: under 1 in a billion.
325. n² ÷ 7 with any decimals go up: −19% (give or take 1 point). Tested 300000 outputs and found 9538 primes where chance predicts 11795. Luck odds: under 1 in a billion.
326. 1000000 × |sin(n)|: −20% (give or take 1 point). Tested 300000 outputs and found 18328 primes where chance predicts 22997. Luck odds: under 1 in a billion. Note: repeated primes counted once.
327. n² ÷ 11 with decimals of 0.5 or more go up: −21% (give or take 1 point). Tested 300000 outputs and found 9275 primes where chance predicts 11795. Luck odds: under 1 in a billion.
328. n³ ÷ 19: −22% (give or take 3 points). Tested 26681 outputs and found 860 primes where chance predicts 1109. Luck odds: under 1 in a billion.
329. n³ ÷ 5: −23% (give or take 3 points). Tested 17097 outputs and found 546 primes where chance predicts 710. Luck odds: under 1 in a billion.
330. 6n + 3 then bump the last digit: −25% (give or take 1 point). Tested 300000 outputs and found 8510 primes where chance predicts 11282. Luck odds: under 1 in a billion.
331. n² mod 1000003: −25% (give or take 1 point). Tested 300000 outputs and found 17667 primes where chance predicts 23587. Luck odds: under 1 in a billion. Note: repeated primes counted once.
332. 10ⁿ + 1: −26% (give or take 52 points). Tested 299 outputs and found 2 primes where chance predicts 2.7. Luck odds: about 49 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
333. 10ⁿ + 1 then bump the last digit: −26% (give or take 52 points). Tested 299 outputs and found 2 primes where chance predicts 2.7. Luck odds: about 49 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
334. n² ÷ 5 with decimals of 0.5 or more go up: −27% (give or take 1 point). Tested 300000 outputs and found 8618 primes where chance predicts 11794. Luck odds: under 1 in a billion.
335. n² ÷ 5 with decimals of 0.3 or more go up: −28% (give or take 1 point). Tested 300000 outputs and found 8490 primes where chance predicts 11798. Luck odds: under 1 in a billion.
336. n² ÷ 8 with decimals of 0.5 or more go up: −31% (give or take 1 point). Tested 300000 outputs and found 8186 primes where chance predicts 11793. Luck odds: under 1 in a billion.
337. n² ÷ 17: −32% (give or take 1 point). Tested 300000 outputs and found 7977 primes where chance predicts 11796. Luck odds: under 1 in a billion.
338. n² ÷ 6: −32% (give or take 1 point). Tested 300000 outputs and found 7969 primes where chance predicts 11791. Luck odds: under 1 in a billion.
339. n² ÷ 8 with decimals of 0.3 or more go up: −32% (give or take 1 point). Tested 300000 outputs and found 8024 primes where chance predicts 11793. Luck odds: under 1 in a billion.
340. n³ ÷ 3: −33% (give or take 3 points). Tested 14419 outputs and found 401 primes where chance predicts 599. Luck odds: under 1 in a billion.
341. 1 + 16 + 81 + 256 and so on (fourth powers) then bump each total: −34% (give or take 1 point). Tested 300000 outputs and found 3526 primes where chance predicts 5370. Luck odds: under 1 in a billion.
342. n² ÷ 11: −36% (give or take 1 point). Tested 300000 outputs and found 7581 primes where chance predicts 11794. Luck odds: under 1 in a billion.
343. n² ÷ 7: −36% (give or take 1 point). Tested 300000 outputs and found 7508 primes where chance predicts 11796. Luck odds: under 1 in a billion.
344. n² ÷ 18: −38% (give or take 1 point). Tested 300000 outputs and found 7266 primes where chance predicts 11792. Luck odds: under 1 in a billion.
345. n² ÷ 13: −42% (give or take 1 point). Tested 300000 outputs and found 6870 primes where chance predicts 11794. Luck odds: under 1 in a billion.
346. n × 2ⁿ + 1 then bump the last digit: −43% (give or take 25 points). Tested 986 outputs and found 5 primes where chance predicts 8.8. Luck odds: about 13 in 100 which means the gap could be luck. Note: outputs up to 300 digits.
347. n² ÷ 12 with decimals of 0.5 or more go up: −43% (give or take 1 point). Tested 300000 outputs and found 6717 primes where chance predicts 11797. Luck odds: under 1 in a billion.
348. the first n digits of the zeta running total 1/1³ + 1/2³ + 1/3³ up to 1/n³: −43% (give or take 40 points). Tested 2000 outputs and found 2 primes where chance predicts 3.5. Luck odds: about 32 in 100 which means the gap could be luck. Note: positions 1 to 2000.
349. the leading digits of ln 2 (first 1 digit then first 2 digits and so on): −43% (give or take 40 points). Tested 1200 outputs and found 2 primes where chance predicts 3.5. Luck odds: about 32 in 100 which means the gap could be luck. Note: 1200 numbers tested.
350. n² ÷ 9 with decimals of 0.3 or more go up: −44% (give or take 1 point). Tested 300000 outputs and found 6617 primes where chance predicts 11797. Luck odds: under 1 in a billion.
351. n³ ÷ 13: −44% (give or take 2 points). Tested 23510 outputs and found 545 primes where chance predicts 977. Luck odds: under 1 in a billion.
352. n² ÷ 10: −45% (give or take 1 point). Tested 300000 outputs and found 6463 primes where chance predicts 11792. Luck odds: under 1 in a billion.
353. n³ ÷ 7: −48% (give or take 3 points). Tested 19127 outputs and found 412 primes where chance predicts 795. Luck odds: under 1 in a billion.
354. 3 to the power n mod (2n + 1): −49% (give or take 1 point). Tested 300000 outputs and found 7975 primes where chance predicts 15753. Luck odds: under 1 in a billion. Note: repeated primes counted once.
355. n ÷ 2: −50% (give or take 1 point). Tested 300000 outputs and found 13848 primes where chance predicts 27785. Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.
356. 2ⁿ + 1: −51% (give or take 22 points). Tested 996 outputs and found 5 primes where chance predicts 10.1. Luck odds: about 6 in 100. Note: outputs up to 300 digits.
357. 2ⁿ ÷ n with decimals dropped: −51% (give or take 22 points). Tested 1003 outputs and found 5 primes where chance predicts 10.2. Luck odds: about 6 in 100. Note: outputs up to 300 digits.
358. n² ÷ 15: −51% (give or take 1 point). Tested 300000 outputs and found 5829 primes where chance predicts 11798. Luck odds: under 1 in a billion.
359. n³ ÷ 16: −52% (give or take 2 points). Tested 25195 outputs and found 503 primes where chance predicts 1047. Luck odds: under 1 in a billion.
360. n³ ÷ 8: −52% (give or take 2 points). Tested 19997 outputs and found 398 primes where chance predicts 831. Luck odds: under 1 in a billion.
361. n² ÷ 20: −56% (give or take 1 point). Tested 300000 outputs and found 5234 primes where chance predicts 11795. Luck odds: under 1 in a billion.
362. the digit totals of 1 and 2 and 3 and so on added up: −60% (give or take 1 point). Tested 300000 outputs and found 8181 primes where chance predicts 20584. Luck odds: under 1 in a billion.
363. n² ÷ 9: −66% (give or take 1 point). Tested 300000 outputs and found 3971 primes where chance predicts 11794. Luck odds: under 1 in a billion.
364. n³ ÷ 4: −67% (give or take 2 points). Tested 15871 outputs and found 218 primes where chance predicts 659. Luck odds: under 1 in a billion.
365. n² ÷ 9 with decimals of 0.5 or more go up: −69% (give or take 1 point). Tested 300000 outputs and found 3704 primes where chance predicts 11792. Luck odds: under 1 in a billion.
366. 1 + 2 + 6 + 24 and so on (factorials): −71% (give or take 29 points). Tested 166 outputs and found 1 prime where chance predicts 3.4. Luck odds: about 15 in 100 which means the gap could be luck. Note: outputs up to 300 digits and the bump changes nothing for these totals.
367. the first n decimal digits of the zeta piece 1/n²: −75% (give or take 25 points). Tested 2000 outputs and found 1 prime where chance predicts 4.0. Luck odds: about 9 in 100. Note: positions 1 to 2000.
368. n × 2ⁿ + 1: −77% (give or take 16 points). Tested 986 outputs and found 2 primes where chance predicts 8.8. Luck odds: 1 in 100. Note: outputs up to 300 digits.
369. 2 to the power n mod n: −79% (give or take 1 point). Tested 300000 outputs and found 6658 primes where chance predicts 31021. Luck odds: under 1 in a billion. Note: repeated primes counted once.
370. 1 + 1 + 2 + 3 + 5 and so on (Fibonacci numbers): −86% (give or take 10 points). Tested 1435 outputs and found 2 primes where chance predicts 14.1. Luck odds: 1 in 10000. Note: outputs up to 300 digits.
371. 2ⁿ ÷ 3 with decimals dropped: −89% (give or take 11 points). Tested 995 outputs and found 1 prime where chance predicts 9.0. Luck odds: 1 in 800. Note: outputs up to 300 digits.
372. 2 + (2 × n!) mod (n + 1): −91% (give or take 1 point). Tested 300000 outputs and found 25997 primes where chance predicts 276294. Luck odds: under 1 in a billion. Note: a known formula whose output is 2 for most inputs and repeated primes counted once.
373. n ÷ ln(n): −92% (give or take 1 point). Tested 300000 outputs and found 2645 primes where chance predicts 33171. Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.
374. (n² + 1) ÷ 3: −100% (give or take 1 point). Tested 299999 outputs and found 1 prime where chance predicts 11795. Luck odds: under 1 in a billion.
375. 1 + 11 + 111 + 1111 and so on: −100% (give or take 37 points). Tested 300 outputs and found 0 primes where chance predicts 2.7. Luck odds: about 7 in 100. Note: outputs up to 300 digits.
376. 1 + 16 + 81 + 256 and so on (fourth powers): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 5370. Luck odds: under 1 in a billion.
377. 1 + 2 + 3 + 4 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 13455. Luck odds: under 1 in a billion.
378. 1 + 2 + 3 up to n: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11795. Luck odds: under 1 in a billion.
379. 1 + 3 + 5 + 7 and so on (odd numbers): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 13043. Luck odds: under 1 in a billion.
380. 1 + 3 + 6 + 10 and so on (triangle numbers): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 9179. Luck odds: under 1 in a billion.
381. 1 + 4 + 9 + 16 and so on (squares): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 8986. Luck odds: under 1 in a billion.
382. 1 + 8 + 27 + 64 and so on (cubes): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 6727. Luck odds: under 1 in a billion.
383. 1 + 9 + 25 + 49 and so on (odd squares): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 8623. Luck odds: under 1 in a billion.
384. 1² + 2² + 3² up to n²: −100% (give or take 1 point). Tested 14421 outputs and found 1 prime where chance predicts 599. Luck odds: under 1 in a billion.
385. 1² + 2² + 3² up to n² then plus 1: −100% (give or take 1 point). Tested 14421 outputs and found 2 primes where chance predicts 600. Luck odds: under 1 in a billion.
386. 2 + 2 + 2 + 2 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 24586. Luck odds: under 1 in a billion.
387. 2 + 4 + 6 + 8 and so on (even numbers): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 13044. Luck odds: under 1 in a billion.
388. 2 + 6 + 12 + 20 and so on (n times n + 1): −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 8986. Luck odds: under 1 in a billion.
389. 2n: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11282. Luck odds: under 1 in a billion.
390. 3 + 3 + 3 + 3 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 23787. Luck odds: under 1 in a billion.
391. 6 + 12 + 18 + 24 and so on (multiples of 6): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 12441. Luck odds: under 1 in a billion.
392. 6 + 6 + 6 + 6 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 22536. Luck odds: under 1 in a billion.
393. 6n + 3: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11282. Luck odds: under 1 in a billion.
394. 7 + 7 + 7 + 7 and so on: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 22276. Luck odds: under 1 in a billion.
395. n × (n + 1) ÷ 2: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11792. Luck odds: under 1 in a billion.
396. n² + (n mod 6): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11792. Luck odds: under 1 in a billion.
397. n² + 5n + 6: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11794. Luck odds: under 1 in a billion.
398. n² + n + 2: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11796. Luck odds: under 1 in a billion.
399. n² + n + 41 added up: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 8985. Luck odds: under 1 in a billion.
400. n² ÷ 12: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11794. Luck odds: under 1 in a billion.
401. n² ÷ 16: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11795. Luck odds: under 1 in a billion.
402. n² ÷ 2: −100% (give or take 1 point). Tested 299998 outputs and found 0 primes where chance predicts 11794. Luck odds: under 1 in a billion.
403. n² ÷ 3: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11791. Luck odds: under 1 in a billion.
404. n² ÷ 3 with decimals of 0.5 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11793. Luck odds: under 1 in a billion.
405. n² ÷ 4: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11798. Luck odds: under 1 in a billion.
406. n² ÷ 4 with decimals of 0.3 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11796. Luck odds: under 1 in a billion.
407. n² ÷ 4 with decimals of 0.5 or more go up: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11792. Luck odds: under 1 in a billion.
408. n² ÷ 5: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 11795. Luck odds: under 1 in a billion.
409. n² ÷ 8: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11794. Luck odds: under 1 in a billion.
410. n² − 1: −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11793. Luck odds: under 1 in a billion.
411. n³ ÷ (n + 1): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11795. Luck odds: under 1 in a billion.
412. n³ ÷ 2: −100% (give or take 1 point). Tested 12598 outputs and found 1 prime where chance predicts 524. Luck odds: under 1 in a billion.
413. n³ ÷ 9: −100% (give or take 1 point). Tested 20798 outputs and found 3 primes where chance predicts 865. Luck odds: under 1 in a billion.
414. n⁴ + 4: −100% (give or take 2 points). Tested 998 outputs and found 0 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
415. n⁴ + n² + 1: −100% (give or take 2 points). Tested 998 outputs and found 0 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
416. n⁴ + n² + 1 then bump the last digit: −100% (give or take 2 points). Tested 998 outputs and found 0 primes where chance predicts 44.3. Luck odds: under 1 in a billion.
417. n⁴ ÷ (n² + 1): −100% (give or take 1 point). Tested 300000 outputs and found 0 primes where chance predicts 11795. Luck odds: under 1 in a billion.
418. n⁶ + 1: −100% (give or take 20 points). Tested 98 outputs and found 0 primes where chance predicts 5.0. Luck odds: 1 in 100.
419. sin(e to the n) ÷ ln(n): −100% (). Tested 700 outputs and found 0 primes where chance predicts 0.0. Luck odds: not measurable because every output is below 2. Note: every output is 0 or −1.
420. slope of n³ + 2 which is 3n²: −100% (give or take 1 point). Tested 300000 outputs and found 1 prime where chance predicts 11795. Luck odds: under 1 in a billion.
421. √1 + √2 + √3 up to √n with decimals dropped in each piece: −100% (give or take 1 point). Tested 300000 outputs and found 16 primes where chance predicts 17820. Luck odds: under 1 in a billion.
422. √n: −100% (give or take 1 point). Tested 300000 outputs and found 101 primes where chance predicts 52191. Luck odds: under 1 in a billion. Note: inputs 2 to 300001 in order with repeated primes counted once.
423. √n with decimals dropped added up: −100% (give or take 1 point). Tested 300000 outputs and found 16 primes where chance predicts 17820. Luck odds: under 1 in a billion.

## Program files

The folder boring-things/research-program-files/prime-richness-scripts holds the Python files behind the list and the file master_list_data.json holds every line of the list with the raw counts.
