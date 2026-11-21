# Sum formulas with no leftover terms for zeta(7) through zeta(15)

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 20 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. The formulas were checked by number matching and not by a written proof.

## What this page answers

The page named other-bases.md in this folder found a base that writes zeta(5) purely as sums with no leftover terms and found no base that does the same for zeta(7). This page asks whether any base reaches zeta(7) or higher with no leftover terms.

The answer from the search is yes. A base near 0.7136 gives formulas with no leftover terms for zeta(3) and zeta(5) and zeta(7) and zeta(9). Two bases near 0.8221 and 0.8501 give a formula with no leftover terms for zeta(11) and the base near 0.8501 also gives formulas with no leftover terms for zeta(13) and zeta(15).

Each base on this page is 1 divided by a Salem number. A Salem number is a number bigger than 1 that solves an equation with whole-number coefficients that reads the same forwards and backwards and whose other solutions (apart from 1 divided by the number) all sit at distance exactly 1 from zero in the plane of complex numbers. Ladders of sums in the two bases near 0.8221 and 0.8501 are described in a free 1999 paper (https://arxiv.org/abs/math/9906134) and that paper works with formulas that keep leftover terms. A free web search on 20 November 2026 did not turn up formulas with no leftover terms written out for zeta(7) or zeta(9) or zeta(11) or zeta(13) or zeta(15).

## What the chatbot could say from memory before the search

Before the search the chatbot knew that ladders in the base near 0.8501 reach very high zeta numbers with leftover terms. The chatbot did not know that formulas with no leftover terms reach zeta(15) and did not know any of the counts or coefficients on this page.

## Notation

zeta(7) means 1/1^7 + 1/2^7 + 1/3^7 and so on forever and the other zeta numbers use their own power in the same way.

x is the base which is a number between 0 and 1 that each section names.

L = ln(1/x) which is the natural logarithm of 1 divided by the base.

F(y) means the sum of y^n/n^s for n = 1 and 2 and 3 and so on forever. The number s matches the zeta number in the formula which means s is 5 inside a zeta(5) formula and 7 inside a zeta(7) formula and 9 inside a zeta(9) formula.

The sign × means multiplication.

A leftover term on this page means an extra piece such as pi^2 × L^5 or L^7 that sits beside the sums in a formula. A formula with no leftover terms is built from the sums alone.

## The five bases

- The base near 0.580691832 solves x^4 - x^3 - x^2 - x + 1 = 0.
- The base near 0.713639174 solves x^6 - x^4 - x^3 - x^2 + 1 = 0.
- The base near 0.780860694 solves x^8 - x^5 - x^4 - x^3 + 1 = 0.
- The base near 0.822103630 solves x^10 - x^6 - x^5 - x^4 + 1 = 0.
- The base near 0.850137131 solves x^10 + x^9 - x^7 - x^6 - x^5 - x^4 - x^3 + x + 1 = 0.

## How many independent formulas each base gave

The first count in each line allows leftover terms and the second count allows no leftover terms.

The base near 0.5807:

- zeta(3) gave 9 formulas with leftover terms allowed and 7 with none.
- zeta(5) gave 6 formulas with leftover terms allowed and 3 with none.
- zeta(7) gave 3 formulas with leftover terms allowed and 0 with none.
- zeta(9) gave 0 formulas.

The base near 0.7136:

- zeta(3) gave 21 formulas with leftover terms allowed and 19 with none.
- zeta(5) gave 16 formulas with leftover terms allowed and 13 with none.
- zeta(7) gave 11 formulas with leftover terms allowed and 7 with none.
- zeta(9) gave 6 formulas with leftover terms allowed and 1 with none.
- zeta(11) gave 1 formula with leftover terms allowed and 0 with none.
- zeta(13) gave 0 formulas.

The base near 0.7809:

- zeta(3) gave 34 formulas with leftover terms allowed and 32 with none.
- zeta(5) gave 27 formulas with leftover terms allowed and 24 with none.
- zeta(7) gave 20 formulas with leftover terms allowed and 16 with none.
- zeta(9) gave 13 formulas with leftover terms allowed and 8 with none.
- zeta(11) gave 6 formulas with leftover terms allowed and 0 with none.
- zeta(13) gave 0 formulas.

The base near 0.8221:

- zeta(3) gave 46 formulas with leftover terms allowed and 44 with none.
- zeta(5) gave 37 formulas with leftover terms allowed and 34 with none.
- zeta(7) gave 28 formulas with leftover terms allowed and 24 with none.
- zeta(9) gave 19 formulas with leftover terms allowed and 14 with none.
- zeta(11) gave 10 formulas with leftover terms allowed and 4 with none.
- The search found no formula for zeta(13) in this base. The 1999 paper reports one formula with leftover terms for zeta(13) in this base which means that formula probably has coefficients too large for this search to catch.

The base near 0.8501:

- zeta(3) gave 64 formulas with leftover terms allowed and 62 with none.
- zeta(5) gave 55 formulas with leftover terms allowed and 52 with none.
- zeta(7) gave 46 formulas with leftover terms allowed and 42 with none.
- zeta(9) gave 37 formulas with leftover terms allowed and 32 with none.
- zeta(11) gave 28 formulas with leftover terms allowed and 22 with none.
- zeta(13) gave 19 formulas with leftover terms allowed and 12 with none.
- zeta(15) gave 10 formulas with leftover terms allowed and 2 with none.
- The search found no formula for zeta(17) in this base. The 1999 paper reports one formula with leftover terms for zeta(17) in this base which means that formula probably has coefficients too large for this search to catch.

The counts with leftover terms allowed drop by the same amount at each step inside one base (by 3 in the first base and by 5 in the second and by 7 in the third and by 9 in the last two). The count with no leftover terms equals the first count minus the number of kinds of leftover term (2 kinds for zeta(3) and 3 kinds for zeta(5) and 4 kinds for zeta(7) and so on) because each kind of leftover term uses up one formula when the kind is cancelled.

## zeta(5) with no leftover terms in the base near 0.5807

377810 × zeta(5) = 2810160 × F(x) - 7099380 × F(x^2) + 6402240 × F(x^3) - 2498985 × F(x^4) + 10780992 × F(x^5) - 17519220 × F(x^6) + 3576960 × F(x^7) - 612900 × F(x^8) + 11019520 × F(x^9) - 4413636 × F(x^10) - 2563920 × F(x^11) + 2019570 × F(x^12) - 223560 × F(x^14) - 2465088 × F(x^15) - 478560 × F(x^18) - 90126 × F(x^20) + 154068 × F(x^30) - 13135 × F(x^36)

## zeta(7) with no leftover terms in the base near 0.7136

1171888948773144 × zeta(7) = 1376746653930843081600 × F(x) - 7848250166290579028550 × F(x^2) + 14264115269936511750400 × F(x^3) - 5411030153866759007775 × F(x^4) - 5335313668680561289920 × F(x^5) - 3796534049472567140150 × F(x^6) + 5077292721223161110400 × F(x^7) - 1416926484422900206875 × F(x^8) + 17554668662292708945600 × F(x^9) - 5186669676201266161923 × F(x^10) - 14922840240350391888000 × F(x^11) - 3958806843680467541875 × F(x^12) + 4422560529658067193600 × F(x^13) + 755769424985081263800 × F(x^14) + 12374891291638727359872 × F(x^15) - 4143480581896952623425 × F(x^16) - 5512788179149737225600 × F(x^17) + 2005229477195460102825 × F(x^18) - 638336998624978532502 × F(x^20) + 2303705579037407700800 × F(x^21) - 1929027773549264062500 × F(x^22) + 199633274886926931925 × F(x^24) - 653893232311634636160 × F(x^25) + 127286744166165074400 × F(x^26) + 277308069318405809325 × F(x^28) - 300885356423948933546 × F(x^30) - 169352232520100000000 × F(x^33) + 86137315299214644150 × F(x^34) - 65069012092983172416 × F(x^35) - 8620653056442134400 × F(x^39) + 28734026193137153070 × F(x^40) - 22828201242110495325 × F(x^42) + 3005269671627022275 × F(x^48) - 1989460151526745800 × F(x^56) + 2646128633126562500 × F(x^66) + 1016703313952862069 × F(x^70) - 205737475474203125 × F(x^84)

## zeta(9) with no leftover terms in the base near 0.7136

2452560098501579945503408436937477615 × zeta(9) = 28546016393904423944962297887227577600 × F(x) - 114112379253008268337830633524243975670 × F(x^2) + 167045362544745659900436362137851622400 × F(x^3) + 48001395715707695001694663604033116215 × F(x^4) - 332668559472960321942778046083775950080 × F(x^5) + 135995132565826316445440618978876797620 × F(x^6) + 165586631668168642773800855080716944640 × F(x^7) - 125331911640406923615217709123688373770 × F(x^8) + 394365186788827854772115678197200648960 × F(x^9) - 349002037244293594588632068094242163204 × F(x^10) - 517860596024621514501736892496170757120 × F(x^11) + 363760589180870312013169098846509753755 × F(x^12) + 136601371999219685772251066799678958080 × F(x^13) + 247196860162012632948548929879917028230 × F(x^14) + 273459290035342336987296674590245842176 × F(x^15) - 589483532792163093673825881388860411600 × F(x^16) - 214120680253046530151241229021291921920 × F(x^17) + 95679800951381495219478131828741865060 × F(x^18) + 326387843829691448858953529566210207308 × F(x^20) + 57525971058498890977432562120466529280 × F(x^21) - 161517553960280608958677724731156071030 × F(x^22) - 109805434830774078330188057175423607275 × F(x^24) - 6963840971497818922381148501383850496 × F(x^25) + 89424929775842859861762588733313825370 × F(x^26) + 22973182466146161252629950643923689255 × F(x^28) - 26208445455853716026720069796843058674 × F(x^30) - 6302163361352207878893689609994810880 × F(x^33) + 836408907238463008403286050864421570 × F(x^34) + 1536471502269271903948276332935760384 × F(x^35) - 1840868152048606418161656264601816320 × F(x^37) - 1755020834828150572350516215708582400 × F(x^39) + 504141235170391507209770535878784195 × F(x^40) + 319657460022087848320667888674418820 × F(x^42) + 643508771431764784745401115092394630 × F(x^48) - 35240698195343285602596669723035655 × F(x^56) + 24617825630282062026928475039042230 × F(x^66) - 6001841805739343374797954425530314 × F(x^70) - 2126438611208395082817436853349575 × F(x^84)

## Where the other formulas are

The plain text file named salem-formulas.txt in this folder holds every formula from this page plus the formulas that are too long to print here which include zeta(3) and zeta(5) and zeta(7) and zeta(9) with no leftover terms in the base near 0.7809 and zeta(11) and zeta(13) and zeta(15) with no leftover terms in the base near 0.8501 (115 sums each with coefficients up to 42 digits long for zeta(11) and 31 digits long for zeta(13) and 263 digits long for zeta(15)).

## How fast the sums shrink

The sums in these bases shrink slowly because each base sits close to 1. With 100 terms of each sum the zeta(7) formula in the base near 0.7136 missed zeta(7) by about 5.2 × 10^-23 and with 200 terms the miss was about 1.0 × 10^-39. A person who wants many digits quickly is better served by the golden ratio formulas on the page named long-formulas.md because those sums shrink faster.

## How the search worked

The search ran in two steps. The first step looked for products of the numbers 1 - x^k that multiply out to an exact power of x because every known formula of this kind starts from such a product. The second step turned each product into a combination of sums and then ran an integer relation search (a procedure that hunts for whole-number coefficients that make a weighted total equal exactly zero) with between 3000 and 16000 digits.

The same two steps reproduced the published counts for the golden ratio base (5 and 3 and 2 and 1) which is a sign that the method works correctly.

Every formula printed on this page and in the text file was checked a second time with a separate library routine for the sums at 330 digits or more and both sides agreed to more than 290 digits after allowing for the size of the coefficients.

The program files sit in the boring-things folder of this repository in research-program-files/zeta-sums-scripts (the file ladder-search.py runs both steps for one base and the file salem-check.py repeats the second check).

## Limits of the search

A search does not prove that a formula is impossible because a formula could use ingredients that were not included in the test.

The only leftover terms allowed were products of powers of pi and powers of L.

The first step only looked at the numbers 1 - x^k for k up to a few hundred (300 for the first base and 400 and 500 and 600 for the next three and 700 for the last base) which means a product that needs a higher k would be missed.

The formulas are very likely consequences of mathematics that is already published because the ladders with leftover terms are in the published record. What the web search could not find is the formulas with no leftover terms written out with their coefficients.

## Sources

A free 1999 paper on ladders in the two bases near 0.8221 and 0.8501: https://arxiv.org/abs/math/9906134
