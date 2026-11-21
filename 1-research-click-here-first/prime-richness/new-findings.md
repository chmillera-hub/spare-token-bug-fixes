# Prime richness results that a quick search did not turn up

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each result comes from a computer count and not from a written proof unless the section says a proof exists.

## What the page is for

The page answers a group of questions about how often prime numbers show up in the outputs of different recipes so that a person or an AI agent with the same question can read the answer here and skip the computing.

The page keeps the results that a quick web search did not turn up on 21 November 2026. A result that is missing from a quick search can still sit inside a research paper so the page claims "not quickly searchable" and does not claim "new to mathematics".

The last section lists the related results that a quick search does answer so a reader can skip computing those results as well.

## How the percentages work

Each percentage compares a recipe with plain counting numbers of the same size. The computer counts the primes among the outputs of the recipe and divides by the count that chance predicts for ordinary numbers of those sizes. The chance that an ordinary number is prime is about 1 divided by the natural logarithm of the number which means about 1 in 28 for a number near 1 trillion.

+150% means the recipe produced 2.5 times as many primes as the number line. 0% means the same rate as the number line. −100% means the recipe produced no primes.

Every recipe that produces a decimal uses one rule: drop the decimal places with no rounding which means 1.99 becomes 1.

## Dividing a square or a cube by a whole number and dropping the decimals

The recipe is n² ÷ k with the decimal places dropped for n = 2 and 3 and 4 and so on. The computer tested 300000 random inputs with outputs under 1 trillion for each k.

- n² ÷ 2: −100%
- n² ÷ 3: −100%
- n² ÷ 4: −100%
- n² ÷ 5: −100%
- n² ÷ 6: −32%
- n² ÷ 7: −36%
- n² ÷ 8: −100%
- n² ÷ 9: −66%
- n² ÷ 10: −45%
- n² ÷ 11: −36%
- n² ÷ 12: −100%
- n² ÷ 13: −42%
- n² ÷ 14: +15%
- n² ÷ 15: −51%
- n² ÷ 16: −100%
- n² ÷ 17: −32%
- n² ÷ 18: −38%
- n² ÷ 19: −19%
- n² ÷ 20: −56%

The −100% cases have a clear cause because dropping the decimals turns every output into a form with two factors. For n² ÷ 3 the output is either 3 × (n ÷ 3)² or (n − 1) × (n + 1) ÷ 3 and both forms split into two whole-number factors once n is large. A 2025 paper at https://arxiv.org/abs/2501.04851 proves the n² ÷ 5 case.

The cases between −19% and −66% are mixtures because some outputs split into two factors and other outputs do not. For n² ÷ 7 the outputs of the form (n − 1) × (n + 1) ÷ 7 and (n − 2) × (n + 2) ÷ 7 split while the outputs of the form (n² − 2) ÷ 7 do not split.

n² ÷ 14 is the one divisor from 2 to 20 that landed above the number line.

The same test for cubes (every input with an output under 1 trillion):

- n³ ÷ 2: −100%
- n³ ÷ 3: −33%
- n³ ÷ 4: −67%
- n³ ÷ 5: −23%
- n³ ÷ 6: +29%
- n³ ÷ 7: −48%
- n³ ÷ 8: −52%
- n³ ÷ 9: −100%
- n³ ÷ 10: −8%
- n³ ÷ 11: −11%
- n³ ÷ 12: +30%
- n³ ÷ 13: −44%
- n³ ÷ 14: −5%
- n³ ÷ 15: +14%
- n³ ÷ 16: −52%
- n³ ÷ 17: −5%
- n³ ÷ 18: +4%
- n³ ÷ 19: −22%
- n³ ÷ 20: +8%

Each cube percentage rests on 500 to 1200 predicted primes which means a wobble of about 4 points from chance.

## Dividing by an expression with n and dropping the decimals

Four recipes turn into plain equations once the decimals are dropped and a few lines of algebra confirm each one.

- n² ÷ (n + 1) leaves n − 1 for every input above 0 which means the outputs are the plain number line (measured −1%).
- n³ ÷ (n + 1) leaves n² − n for every input above 0 and n² − n is even so the recipe has no primes (measured −100%).
- n⁴ ÷ (n² + 1) leaves n² − 1 for every input above 1 and n² − 1 splits into (n − 1) × (n + 1) so the recipe has no primes (measured −100%).
- (n³ + 5) ÷ (n + 1) leaves n² − n + 1 for every input above 3 and every output of n² − n + 1 is odd (measured +123%).

## Square roots and π and e and logarithms give the same prime rate as the number line

Seventeen recipes multiply or divide by a number with endless non-repeating decimals and then drop the decimals. Every one of the seventeen landed between −2% and +2% which is inside the wobble from sampling 300000 inputs.

The seventeen recipes are n × √2 and n × φ (the golden ratio) and n × π and n × e and n² × √2 and n² × φ and n² × π and n to the power 1.5 and n to the power 2.5 and √n and n × ln(n) and n × log₂(n) and n × log₁₀(n) and n × ln(n) × ln(n) and n² × ln(n) and n² ÷ ln(n) and n ÷ ln(n).

The likely reason is that the dropped decimals scramble the outputs so each small prime divides the outputs at the ordinary rate which is 1 of every 2 outputs for the prime 2 and 1 of every 3 outputs for the prime 3.

The page [equation-list.md](equation-list.md) gives the raw counts for all seventeen recipes and for 69 more equations.

## The right-end pieces of a prime

The recipe takes a prime and reads pieces from the right end. For the prime 2147483647 the pieces are 7 and 47 and 647 and 3647 and so on. A piece that starts with 0 is skipped because 047 repeats the check on 47.

The computer tested 200000 random primes with 12 digits.

- The pieces with 2 or more digits landed at +150% against the number line.
- Ordinary 12-digit numbers that end in 1 or 3 or 7 or 9 landed on the same +150% for their pieces.
- Ordinary 12-digit numbers with any ending landed at 0%.

So the +150% is explained by the last digit. Every prime above 5 ends in 1 or 3 or 7 or 9 and every piece shares that last digit which means every piece dodges the primes 2 and 5 and that multiplies the prime rate by 2.5. The whole number being prime adds almost nothing beyond the last digit with one exception described in the next section.

How many prime pieces a 12-digit prime has out of 11 pieces (share of the 200000 primes):

- 0 prime pieces: 4%
- 1 prime piece: 17%
- 2 prime pieces: 28%
- 3 prime pieces: 27%
- 4 prime pieces: 16%
- 5 prime pieces: 6%
- 6 or more prime pieces: under 2%

A 2026 paper at https://arxiv.org/abs/2603.08451 studies how the count of prime pieces spreads out across all whole numbers.

## The removed first digit changes the chance for the longest piece

The longest piece of a prime is the prime with the first digit removed. The computer tested 600000 random primes with 12 digits (skipping primes whose second digit is 0) and sorted the results by the digit that was removed.

- Removed digit 1: +77%
- Removed digit 2: +74%
- Removed digit 3: +247%
- Removed digit 4: +80%
- Removed digit 5: +78%
- Removed digit 6: +254%
- Removed digit 7: +110%
- Removed digit 8: +78%
- Removed digit 9: +242%

The cause is the prime 3. Removing a first digit of 3 or 6 or 9 subtracts a multiple of 3 so the piece leaves the same remainder as the whole prime when divided by 3. The whole prime is not a multiple of 3 which means the piece cannot be a multiple of 3 either. Removing a first digit of 1 or 2 or 4 or 5 or 8 shifts the remainder which gives the piece a 1 in 2 chance of being a multiple of 3 where ordinary numbers have a 1 in 3 chance. The prime 7 gives the same kind of protection when the removed digit is 7.

The measured percentages match a standard unproven prediction about pairs of primes a fixed distance apart. The prediction gives +76% for the removed digits 1 and 2 and 4 and 5 and 8 and gives +252% for the removed digits 3 and 6 and 9 and gives +111% for the removed digit 7.

## The reversed pieces of a prime

The recipe takes a prime and reads the first digit and then the first two digits written backward and then the first three digits written backward and so on. For the prime 2147483647 the pieces are 2 and 12 and 412 and 7412 and so on up to the whole number written backward.

Every reversed piece ends in the first digit of the prime so the first digit decides almost everything. The computer tested 200000 random primes with 12 digits. The percentages cover the pieces shorter than the whole number.

- First digit 3: +147%
- First digit 7: +144%
- First digit 1: +62% (the one-digit piece 1 is not prime and the longer pieces sit near +150%)
- First digit 9: +61% (the one-digit piece 9 is not prime and the longer pieces sit near +150%)
- First digit 2: −22% (the one-digit piece 2 is prime and every longer piece is even)
- First digit 5: −22% (the one-digit piece 5 is prime and every longer piece ends in 5)
- First digit 4 or 6 or 8: −100%

Across all 200000 primes the reversed pieces landed at +10% against the number line.

The whole number written backward gets an extra boost. For primes that start with 1 or 3 or 7 or 9 the full reversal landed at about +310% which is far above the +150% from the last digit. Reversing a number keeps the same digits so the digits add up to the same total. A number is a multiple of 3 exactly when the digits add up to a multiple of 3 so the full reversal of a prime cannot be a multiple of 3. A similar digit rule protects the full reversal from the prime 11 when the number has an even count of digits. Dodging 2 and 3 and 5 and 11 together predicts +312%.

The piece made from the first 11 digits written backward landed at +24% across all the primes where the shorter pieces landed near +11%. The cause is the same digit-total rule because the first 11 digits add up to the total for the whole prime minus the last digit.

The reversed pieces of a number are the same list as the right-end pieces of the number written backward. So the reversed check and the right-end check are one check applied to a number and to the mirror image of the number.

## The 467 primes where every reversed piece is prime

A complete computer search found exactly 467 primes where every reversed piece is prime including the whole number written backward. The search is complete because each such prime written backward is a prime where every right-end piece is prime and that family has 4260 members and then ends.

The largest of the 467 is 79168736654243369351 which has 20 digits.

Count by number of digits:

- 1 digit: 4
- 2 digits: 5
- 3 digits: 14
- 4 digits: 20
- 5 digits: 34
- 6 digits: 46
- 7 digits: 62
- 8 digits: 65
- 9 digits: 56
- 10 digits: 41
- 11 digits: 38
- 12 digits: 23
- 13 digits: 27
- 14 digits: 19
- 15 digits: 6
- 16 digits: 2
- 17 digits: 3
- 18 digits: 1
- 19 digits: 0
- 20 digits: 1

The file [champions-467.txt](champions-467.txt) lists all 467 primes with one prime on each line.

## Bumping the first digit to 1 or 3 or 7 or 9 before reading the reversed pieces

The bump rule moves the first digit of the prime up to the nearest of 1 or 3 or 7 or 9. So 0 becomes 1 and 2 becomes 3 and 4 or 5 or 6 becomes 7 and 8 becomes 9. A first digit of 1 or 3 or 7 or 9 stays unchanged. The bump removes the trivial failures where every piece is even or ends in 5.

The computer tested 200000 random primes with 12 digits.

- Without the bump the reversed pieces landed at +10% against the number line.
- With the bump the reversed pieces landed at +119% against the number line.
- With the bump the pieces with 2 or more digits landed near +150% for every first digit.
- The share of primes with zero prime pieces fell from 34% to 2%.

The +119% is the last-digit effect again. Against ordinary numbers that also end in 1 or 3 or 7 or 9 the bumped pieces with 2 to 10 digits landed between −1% and +3% which is inside the wobble from sampling.

The bump has a side effect on the whole number written backward. When the first digit was unchanged the full reversal landed at about +65% against ordinary numbers with the same ending. When the first digit was bumped by 1 or 2 (a first digit of 2 or 5 or 6 or 8) the full reversal landed at about −25% because the bump changes the digit total and that gives the reversal a 1 in 2 chance of being a multiple of 3. A first digit of 4 becomes 7 which adds exactly 3 to the digit total so those reversals keep the protection from the prime 3 and landed at +48%.

## How often a bump turns a non-prime into a prime

The recipe takes a non-prime number that ends in 0 or 2 or 4 or 5 or 6 or 8 and bumps the last digit up to the nearest of 1 or 3 or 7 or 9. For example 123456 becomes 123457 which is prime and 98765 becomes 98767 which is not prime because 98767 = 283 × 349.

Share of bumped numbers that are prime by size:

- 2-digit numbers: 57% (every number tested)
- 3-digit numbers: 41% (every number tested)
- 4-digit numbers: 29% (every number tested)
- 5-digit numbers: 23% (every number tested)
- 6-digit numbers: 19.1% (every number tested)
- 9-digit numbers: 12.6% (random sample of 360000)
- 12-digit numbers: 9.3% (random sample of 360000)
- 18-digit numbers: 6.2% (random sample of 360000)

The starting digit makes no difference. For 6-digit numbers the shares were 19.14% for an ending of 0 and 19.18% for an ending of 2 and 19.12% for an ending of 4 or 5 or 6 and 19.11% for an ending of 8. The endings 4 and 5 and 6 match exactly because all three land on the same number ending in 7.

A rule of thumb for larger numbers is 110% divided by the count of digits because the bumped number is an ordinary number ending in 1 or 3 or 7 or 9 and such a number has 2.5 times the usual chance of being prime.

About 65% of 6-digit non-primes have an ending that the bump changes. The other 35% already end in 1 or 3 or 7 or 9.

## The product of the first primes divided by one more than the largest prime

The recipe multiplies the primes from 2 up to a prime p and divides by p + 1 and drops the decimals. For p = 7 the recipe gives 210 ÷ 8 = 26.25 which becomes 26.

The first entries are 0 and 1 and 5 and 26 and 192 and 2145 and 28361 and 484984 and 9295536 and 215656441 and 6267515316 and 195282582495.

The division is exact when p + 1 has no repeated prime factor such as 6 = 2 × 3 or 14 = 2 × 7 or 30 = 2 × 3 × 5. An exact division leaves several of the used primes multiplied together so an exact entry after 5 is never prime.

The computer tested every p below 2000 which is 301 entries above 1.

- 108 entries were exact divisions.
- 55 entries had no used prime as a factor where ordinary numbers of those sizes would give roughly 25.
- 2 entries passed the prime test: the entry 5 (for p = 5) and a 620-digit entry (for p = 1483).
- Chance predicts about 2.4 primes for 301 ordinary numbers of the same sizes and about 1.8 primes after counting the exact divisions and the blocked small primes.

The 620-digit entry passed 40 rounds of a strong probable-prime test which is strong evidence and not a full proof.

A quick search found a neighboring list at OEIS A126147 (the product of the primes before p divided by p with decimals dropped) and did not find the list on this page.

## The sum of 1 over each Fibonacci prime

The Fibonacci primes are the Fibonacci numbers that are prime: 2 and 3 and 5 and 13 and 89 and 233 and 1597 and so on. The sum 1/2 + 1/3 + 1/5 + 1/13 + 1/89 + 1/233 + 1/1597 and so on equals

1.126447227672853338601666004413811616329

Nobody knows whether the list of Fibonacci primes ever ends. The digits above are safe either way because the computer checked every Fibonacci number up to position 3000 and any Fibonacci prime past position 3000 is larger than 10 to the power 600 and so cannot change the digits shown. The sum is guaranteed to stay finite because the sum of 1 over every Fibonacci number is about 3.3599.

## Fast-growing recipes

Twenty fast-growing recipes such as 2ⁿ − 3 and n! − 1 and the nth Fibonacci number were tested on every output with 300 digits or fewer. Each recipe produced fewer than 30 primes so each percentage is rough.

The highest were n! − 1 at +341% (12 primes where chance predicts 2.7) and 3ⁿ + 2 at +296% (24 primes where chance predicts 6.1) and 10ⁿ + 7 at +278% (10 primes where chance predicts 2.6).

The lowest were 2ⁿ ÷ 3 with decimals dropped at −89% (1 prime where chance predicts 9.0) and n × 2ⁿ + 1 at −77% (2 primes where chance predicts 8.8).

The page [equation-list.md](equation-list.md) lists all twenty.

## A page that checks any equation

The page [checker.html](checker.html) lets a visitor type an equation such as n^2 + n + 41 and reports the predicted percentage against the number line plus a live computer count. The checker reads equations built from whole numbers and n and + and − and × and powers. The checker runs in a web browser at https://chmillera-hub.github.io/spare-token-bug-fixes/1-research-click-here-first/prime-richness/checker.html

## What a quick search already answers

A reader can skip computing the results below because a quick search finds each one.

- Equations with many primes such as n² + n + 41 and the richness score for an equation appear in the Online Encyclopedia of Integer Sequences (oeis.org) and in public encyclopedia pages about prime-generating polynomials.
- The product of the first primes minus the total of the same primes is OEIS A355590 (0 and 1 and 20 and 193 and 2282 and 29989 and so on). The primes on that list are OEIS A120851 (193 and 29989 and 13082761331669749).
- The product of the first primes plus 1 or minus 1 appears on public pages about primorial primes.
- The primes where every right-end piece is prime are called left-truncatable primes. A quick search gives the count 4260 and the largest one which is 357686312646216567629137.
- The primes that stay prime when written backward are OEIS A007500.
- The sum of 1 over every Fibonacci number (about 3.3599) is OEIS A079586.
- The proof that n² ÷ 5 with decimals dropped has no primes past n = 6 is at https://arxiv.org/abs/2501.04851

## Program files

The folder boring-things/research-program-files/prime-richness-scripts holds the Python files behind every number on this page. Each file needs the free Python package gmpy2 and two files also need the free package mpmath.

- divide_table.py prints the n² ÷ k and n³ ÷ k percentages.
- equation_table.py prints the counts for the 86 equations.
- right_end_pieces.py and removed_first_digit.py print the right-end piece results.
- reversed_pieces.py and champions.py print the reversed piece results and the list of 467 primes.
- bumped_pieces.py and bump_conversion.py print the bump results.
- primorial_lists.py prints the results for the product of the first primes.
- fib_prime_sum.py prints the sum of 1 over each Fibonacci prime.
