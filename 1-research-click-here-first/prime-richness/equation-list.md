# Prime counts for 86 equations compared with the number line

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each percentage comes from a computer count and not from a written proof.

## What the page shows

The page lists 86 equations and reports how many primes the outputs of each equation contain compared with plain counting numbers of the same size. The comparison is written as a percentage because a percentage shows the gap at a glance: +564% means the equation produced 564% more primes than the number line and −88% means the equation produced 88% fewer primes and −100% means the equation produced no primes.

## How each equation was tested

For each equation the computer plugged whole numbers into n and dropped any decimal places from the output without rounding which means 1.99 becomes 1.

For most equations the computer tested outputs under 1 trillion. The computer used every input when 300000 or fewer inputs fit under 1 trillion and used 300000 random inputs when more inputs fit because testing a trillion inputs one by one would take days.

For the fast-growing equations such as 2ⁿ − 1 the computer tested every output with 300 digits or fewer because fewer than 40 outputs of an equation such as 2ⁿ − 1 fit under 1 trillion.

The count that chance predicts was found by adding up the chance of being prime for each tested output. The chance for an ordinary number is 1 divided by the natural logarithm of the number which means about 1 in 28 for a number near 1 trillion.

Percentages between −2% and +2% are treated as no difference from the number line because random sampling of 300000 inputs makes the percentage wobble by 1 or 2 points. The plain number line itself measured −1% in the test for that reason.

## Ranking of the 66 equations tested under 1 trillion

The list runs from the most primes to the fewest primes and each percentage compares the equation with the plain number line.

- n² − 79n + 1601: +566%
- n² + n + 41: +564%
- 2n² + 29: +491%
- 210n + 1: +335%
- n² + n + 17: +318%
- 30n + 1: +276%
- 2n² − 1: +267%
- n³ − n + 1: +259%
- n² − n − 1: +254%
- 3n² + 3n + 1: +237%
- n³ + n² + 1: +208%
- n³ + n + 1: +202%
- 6n + 1: +200%
- 4n² + 1: +176%
- 10n + 1: +149%
- n⁴ + 1: +148%
- n⁴ + n + 1: +146%
- (n³ + 5) ÷ (n + 1): +123%
- n² + n + 1: +121%
- 4n + 3: +102%
- 2n + 1: +101%
- n² − 2: +87%
- n² + 1: +36%
- n³ + 2: +25%
- n⁵ + 2: +18%
- n² + 3: +12%
- n to the power 2.5: +2%
- n ÷ ln(n): +2%
- n × φ (the golden ratio): +1%
- n × π: +1%
- n² × π: +1%
- n² × ln(n): +1%
- n² ÷ ln(n): 0%
- n × ln(n): 0%
- n × ln(n) × ln(n): 0%
- n × log₂(n): 0%
- n ÷ 2: 0%
- n² × φ (the golden ratio): 0%
- n to the power 1.5: 0%
- n × e: −1%
- n × log₁₀(n): −1%
- n² ÷ (n + 1): −1%
- n: −1%
- √n: −2%
- n × √2: −2%
- n² × √2: −2%
- n² ÷ 7: −36%
- n² ÷ 10: −45%
- n³ ÷ 7: −48%
- n³ ÷ 2: −100%
- (n² + 1) ÷ 3: −100%
- n² ÷ 5: −100%
- 2n: −100%
- 6n + 3: −100%
- n² − 1: −100%
- n² + n + 2: −100%
- n² + 5n + 6: −100%
- n⁴ + 4: −100%
- n⁴ + n² + 1: −100%
- n⁶ + 1: −100%
- n² ÷ 2: −100%
- n² ÷ 3: −100%
- n² ÷ 4: −100%
- n × (n + 1) ÷ 2: −100%
- n³ ÷ (n + 1): −100%
- n⁴ ÷ (n² + 1): −100%

## Ranking of the 20 fast-growing equations

The list runs from the most primes to the fewest primes and each percentage is rough because each fast-growing equation produced fewer than 30 primes.

- n! − 1: +341%
- 3ⁿ + 2: +296%
- 10ⁿ + 7: +278%
- 2ⁿ − 3: +206%
- n! + 1 (1 × 2 × 3 up to n then add 1): +185%
- 3ⁿ − 2: +170%
- 2ⁿ + 3: +86%
- φⁿ with decimals dropped: +66%
- 2ⁿ − 1: +46%
- the nth Fibonacci number: +44%
- 2ⁿ + n: +20%
- eⁿ with decimals dropped: +14%
- 1.5ⁿ with decimals dropped: −1%
- πⁿ with decimals dropped: −2%
- nⁿ + 1: −13%
- 10ⁿ + 1: −26%
- 2ⁿ + 1: −51%
- 2ⁿ ÷ n with decimals dropped: −51%
- n × 2ⁿ + 1: −77%
- 2ⁿ ÷ 3 with decimals dropped: −89%

## Details for each equation

Each line gives the percentage and the reason where a reason is known and the raw counts so a reader can check each percentage.

### Straight-line equations

- n has about the same rate of primes as the number line at −1% because n is the plain number line itself (11116 primes found where chance predicts 11282).
- 2n has 100% fewer primes than the number line because every output is even (0 primes found where chance predicts 11282).
- 2n + 1 has 101% more primes than the number line because every output is odd so the prime 2 never divides an output (22670 primes found where chance predicts 11283).
- 4n + 3 has 102% more primes than the number line because every output is odd so the prime 2 never divides an output (22799 primes found where chance predicts 11283).
- 6n + 1 has 200% more primes than the number line because the primes 2 and 3 never divide an output (33894 primes found where chance predicts 11283).
- 6n + 3 has 100% fewer primes than the number line because every output is a multiple of 3 (0 primes found where chance predicts 11282).
- 10n + 1 has 149% more primes than the number line because the primes 2 and 5 never divide an output (28119 primes found where chance predicts 11283).
- 30n + 1 has 276% more primes than the number line because the primes 2 and 3 and 5 never divide an output (42449 primes found where chance predicts 11283).
- 210n + 1 has 335% more primes than the number line because the primes 2 and 3 and 5 and 7 never divide an output (49050 primes found where chance predicts 11284).

### Squared equations

- n² + 1 has 36% more primes than the number line because 2 divides every second output and 5 divides two of every five outputs (16062 primes found where chance predicts 11795).
- n² + n + 1 has 121% more primes than the number line because every output is odd (26026 primes found where chance predicts 11790).
- n² − n − 1 has 254% more primes than the number line because 2 and every prime ending in 3 or 7 never divide an output of the golden ratio equation n² − n − 1 (41751 primes found where chance predicts 11794).
- n² − 2 has 87% more primes than the number line because about half of the primes (such as 3 and 5 and 11 and 13) never divide an output (22001 primes found where chance predicts 11793).
- n² + 3 has 12% more primes than the number line because 2 divides every second output and 3 divides every third output while about half of the larger primes never divide an output (13217 primes found where chance predicts 11796).
- 2n² − 1 has 267% more primes than the number line because every output is odd (43336 primes found where chance predicts 11794).
- 4n² + 1 has 176% more primes than the number line because every output is odd and 3 never divides an output (32527 primes found where chance predicts 11792).
- 3n² + 3n + 1 has 237% more primes than the number line because 2 and 3 and 5 never divide an output (39763 primes found where chance predicts 11793). 3n² + 3n + 1 is the gap between two neighboring cubes such as 27 − 8 = 19.
- n² + n + 17 has 318% more primes than the number line because no prime below 17 ever divides an output (49315 primes found where chance predicts 11793).
- 2n² + 29 has 491% more primes than the number line because no prime below 29 ever divides an output (69693 primes found where chance predicts 11793).
- n² + n + 41 has 564% more primes than the number line because no prime below 41 ever divides an output (78263 primes found where chance predicts 11795).
- n² − 79n + 1601 has 566% more primes than the number line because n² − 79n + 1601 produces the same outputs as n² + n + 41 with the inputs shifted by 40 (78597 primes found where chance predicts 11794).
- n² − 1 has 100% fewer primes than the number line because the equation splits into (n − 1) × (n + 1) (0 primes found where chance predicts 11793).
- n² + n + 2 has 100% fewer primes than the number line because every output is even (0 primes found where chance predicts 11796).
- n² + 5n + 6 has 100% fewer primes than the number line because the equation splits into (n + 2) × (n + 3) (0 primes found where chance predicts 11794).

### Cubes and higher powers

- n³ + 2 has 25% more primes than the number line because 2 divides every second output and 3 divides every third output while many larger primes never divide an output (519 primes found where chance predicts 415).
- n³ + n + 1 has 202% more primes than the number line because every output is odd (1254 primes found where chance predicts 415).
- n³ + n² + 1 has 208% more primes than the number line because every output is odd (1280 primes found where chance predicts 415).
- n³ − n + 1 has 259% more primes than the number line because 2 and 3 never divide an output (1493 primes found where chance predicts 415).
- n⁴ + 1 has 148% more primes than the number line because the primes 3 and 5 and 7 and 11 and 13 never divide an output (110 primes found where chance predicts 44.3).
- n⁴ + n + 1 has 146% more primes than the number line because every output is odd (109 primes found where chance predicts 44.3).
- n⁵ + 2 has 18% more primes than the number line (14 primes found where chance predicts 11.9). Just 250 inputs fit under 1 trillion for n⁵ + 2 which makes the percentage rough.
- n⁴ + 4 has 100% fewer primes than the number line because the equation secretly splits into (n² + 2n + 2) × (n² − 2n + 2) (0 primes found where chance predicts 44.3).
- n⁴ + n² + 1 has 100% fewer primes than the number line because the equation secretly splits into (n² + n + 1) × (n² − n + 1) (0 primes found where chance predicts 44.3).
- n⁶ + 1 has 100% fewer primes than the number line because the equation secretly splits into (n² + 1) × (n⁴ − n² + 1) (0 primes found where chance predicts 5.0). Just 98 inputs fit under 1 trillion for n⁶ + 1 and the splitting guarantees no primes at any size.

### Division with the decimal places dropped

- n ÷ 2 has about the same rate of primes as the number line at 0% because each whole number shows up twice in a row which means the outputs are the plain number line repeated (11248 primes found where chance predicts 11282).
- n² ÷ 2 has 100% fewer primes than the number line because the output is 2 × (n ÷ 2)² for even n and (n − 1) × (n + 1) ÷ 2 for odd n and both forms have two factors (0 primes found where chance predicts 11794).
- n² ÷ 3 has 100% fewer primes than the number line because the output is either 3 × (n ÷ 3)² or (n − 1) × (n + 1) ÷ 3 and both forms have two factors (0 primes found where chance predicts 11791).
- n² ÷ 4 has 100% fewer primes than the number line because the output is a perfect square for even n and two neighboring numbers multiplied for odd n (0 primes found where chance predicts 11798).
- n² ÷ 5 has 100% fewer primes than the number line because the output takes the form n² ÷ 5 or (n − 1) × (n + 1) ÷ 5 or (n − 2) × (n + 2) ÷ 5 and all three forms have two factors (1 prime found where chance predicts 11795).
- n² ÷ 7 has 36% fewer primes than the number line because some outputs take forms with two factors such as (n − 1) × (n + 1) ÷ 7 while other outputs take the form (n² − 2) ÷ 7 which does not split (7508 primes found where chance predicts 11796).
- n² ÷ 10 has 45% fewer primes than the number line because some outputs take forms with two factors such as (n − 1) × (n + 1) ÷ 10 while other outputs take forms such as (n² − 6) ÷ 10 which do not split (6463 primes found where chance predicts 11792).
- (n² + 1) ÷ 3 has 100% fewer primes than the number line because dropping the decimals leaves either n² ÷ 3 or (n − 1) × (n + 1) ÷ 3 and both forms have two factors (1 prime found where chance predicts 11795).
- n³ ÷ 2 has 100% fewer primes than the number line because the output is n³ ÷ 2 for even n and (n − 1) × (n² + n + 1) ÷ 2 for odd n and both forms have two factors (1 prime found where chance predicts 524).
- n³ ÷ 7 has 48% fewer primes than the number line because some outputs take forms with two factors such as (n − 1) × (n² + n + 1) ÷ 7 while other outputs do not split (412 primes found where chance predicts 795).
- n × (n + 1) ÷ 2 has 100% fewer primes than the number line because the division is exact for every input and the output is two numbers multiplied (0 primes found where chance predicts 11792).
- n² ÷ (n + 1) has about the same rate of primes as the number line at −1% because dropping the decimals leaves n − 1 for every input which means the outputs are the plain number line (11179 primes found where chance predicts 11284).
- n³ ÷ (n + 1) has 100% fewer primes than the number line because dropping the decimals leaves n² − n for every input and n² − n is even (0 primes found where chance predicts 11795).
- (n³ + 5) ÷ (n + 1) has 123% more primes than the number line because dropping the decimals leaves n² − n + 1 for every input above 3 and every output of n² − n + 1 is odd (26332 primes found where chance predicts 11794).
- n⁴ ÷ (n² + 1) has 100% fewer primes than the number line because dropping the decimals leaves n² − 1 for every input above 1 and n² − 1 splits into (n − 1) × (n + 1) (0 primes found where chance predicts 11795).

### Square roots and special multipliers with the decimal places dropped

- n × √2 has about the same rate of primes as the number line at −2% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11052 primes found where chance predicts 11283).
- n × φ (the golden ratio) has about the same rate of primes as the number line at +1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11418 primes found where chance predicts 11282).
- n × π has about the same rate of primes as the number line at +1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11388 primes found where chance predicts 11281).
- n × e has about the same rate of primes as the number line at −1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11227 primes found where chance predicts 11284).
- n² × √2 has about the same rate of primes as the number line at −2% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11544 primes found where chance predicts 11793).
- n² × φ (the golden ratio) has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11748 primes found where chance predicts 11789).
- n² × π has about the same rate of primes as the number line at +1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11868 primes found where chance predicts 11796).
- n to the power 1.5 has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11467 primes found where chance predicts 11524).
- n to the power 2.5 has about the same rate of primes as the number line at +2% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (2606 primes found where chance predicts 2545).
- √n has about the same rate of primes as the number line at −2% because each whole number repeats many times in a row which means the outputs are the plain number line repeated (10871 primes found where chance predicts 11062).

### Logarithms with the decimal places dropped

- n × ln(n) has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11339 primes found where chance predicts 11303). The output of n × ln(n) is close to the size of the nth prime number.
- n × log₂(n) has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11280 primes found where chance predicts 11303).
- n × log₁₀(n) has about the same rate of primes as the number line at −1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11237 primes found where chance predicts 11303).
- n × ln(n) × ln(n) has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11349 primes found where chance predicts 11327).
- n² × ln(n) has about the same rate of primes as the number line at +1% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11209 primes found where chance predicts 11146).
- n² ÷ ln(n) has about the same rate of primes as the number line at 0% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11809 primes found where chance predicts 11753).
- n ÷ ln(n) has about the same rate of primes as the number line at +2% likely because dropping the decimals scrambles the outputs so each small prime divides the outputs at the ordinary rate (11446 primes found where chance predicts 11266). The output of n ÷ ln(n) is close to the count of primes below n.

### Fast-growing equations (tested on outputs up to 300 digits)

- 2ⁿ − 1 has 46% more primes than the number line (14 primes found where chance predicts 9.6 which makes the percentage rough). A prime output of 2ⁿ − 1 requires n to be prime.
- 2ⁿ + 1 has 51% fewer primes than the number line because a prime output of 2ⁿ + 1 requires n to be a power of 2 and the last prime found was at n = 16 (5 primes found where chance predicts 10.1 which makes the percentage rough).
- 2ⁿ + 3 has 86% more primes than the number line (18 primes found where chance predicts 9.7 which makes the percentage rough).
- 2ⁿ − 3 has 206% more primes than the number line (27 primes found where chance predicts 8.8 which makes the percentage rough).
- 2ⁿ + n has 20% more primes than the number line (12 primes found where chance predicts 10.0 which makes the percentage rough).
- 3ⁿ − 2 has 170% more primes than the number line (15 primes found where chance predicts 5.5 which makes the percentage rough).
- 3ⁿ + 2 has 296% more primes than the number line (24 primes found where chance predicts 6.1 which makes the percentage rough).
- 10ⁿ + 1 has 26% fewer primes than the number line because a prime output of 10ⁿ + 1 requires n to be a power of 2 (2 primes found where chance predicts 2.7 which makes the percentage rough).
- 10ⁿ + 7 has 278% more primes than the number line (10 primes found where chance predicts 2.6 which makes the percentage rough).
- n × 2ⁿ + 1 has 77% fewer primes than the number line (2 primes found where chance predicts 8.8 which makes the percentage rough).
- n! + 1 (1 × 2 × 3 up to n then add 1) has 185% more primes than the number line because no prime up to n divides the output (10 primes found where chance predicts 3.5 which makes the percentage rough).
- n! − 1 has 341% more primes than the number line because no prime up to n divides the output (12 primes found where chance predicts 2.7 which makes the percentage rough).
- nⁿ + 1 has 13% fewer primes than the number line (2 primes found where chance predicts 2.3 which makes the percentage rough).
- the nth Fibonacci number has 44% more primes than the number line (20 primes found where chance predicts 13.8 which makes the percentage rough). A prime Fibonacci number requires n to be prime or n to equal 4.
- 1.5ⁿ with decimals dropped has 1% fewer primes than the number line (16 primes found where chance predicts 16.2 which makes the percentage rough).
- φⁿ with decimals dropped has 66% more primes than the number line (22 primes found where chance predicts 13.3 which makes the percentage rough).
- eⁿ with decimals dropped has 14% more primes than the number line (7 primes found where chance predicts 6.1 which makes the percentage rough).
- πⁿ with decimals dropped has 2% fewer primes than the number line (6 primes found where chance predicts 6.2 which makes the percentage rough).
- 2ⁿ ÷ n with decimals dropped has 51% fewer primes than the number line (5 primes found where chance predicts 10.2 which makes the percentage rough).
- 2ⁿ ÷ 3 with decimals dropped has 89% fewer primes than the number line because the output is even for odd n and splits into two factors for even n (1 prime found where chance predicts 9.0 which makes the percentage rough).

## Program file

The file equation_table.py in the folder boring-things/research-program-files/prime-richness-scripts reruns every count on this page and needs the free Python packages gmpy2 and mpmath.
