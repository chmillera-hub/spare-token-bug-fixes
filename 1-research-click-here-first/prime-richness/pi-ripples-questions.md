# Questions about where pi enters and the ripples of the prime count

> **About this page:** One AI model (Claude) wrote this page on 21 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the pages [log-questions.md](log-questions.md) and [ladder-questions.md](ladder-questions.md) and [reciprocal-questions.md](reciprocal-questions.md). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route and the pictures (lamps on a growing circle and a chord of pure tones). A program rechecked every figure (the file pi_ripples_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## Question: the sum 1/e + 1/e² + 1/e³ + … = 0.5820 breaks apart as 1 − 1/2 + 1/12 minus tiny pieces. What are the tiny pieces?

- Start with 1.
- Subtract 1/2 which gives 0.5.
- Add 1/12 which gives 0.583333.
- Subtract 1/720 which gives 0.581944.
- Add 1/30240 which gives 0.5819775.
- Subtract 1/1209600 which gives 0.5819767.
- Add 1/47900160 which changes the eighth decimal place.

The target is 0.58197671.

The dimmer 1/e raised to n unpacks into the string 1 − n + (n squared)/2 − (n cubed)/6 + … where the bottoms are 1 and 1 × 2 and 1 × 2 × 3. So the faded sum holds every sum of powers at once with each one divided by its bottom.

- 1 + 1 + 1 + … has the leftover constant −1/2 which gives the −1/2 piece.
- 1 + 2 + 3 + … has the leftover constant −1/12 which gives the +1/12 piece.
- The sum of squares has a leftover constant of 0 so no piece appears.
- The sum of cubes has the leftover constant 1/120 and 1/120 divided by 6 gives the 1/720 piece.
- The sum of fourth powers has a leftover constant of 0.
- The sum of fifth powers has the leftover constant −1/252 and 1/252 divided by 120 gives the 1/30240 piece.

Each piece is smaller than the one before by a factor of 60 then 42 then 40 then 39.6. The factor settles toward 39.48 which is 2 × pi multiplied by itself.

## Question: where does the pi come from?

Growth with base e has a second direction. A tiny push along the direction a number already points makes the number bigger. A tiny push at a right angle swings the number around a circle of radius 1. The distance around that circle is 2 × pi = 6.283 so a pile of sideways pushes totaling 6.283 returns the number to 1. A pile of 1 swings the number through 57.3 degrees.

The sum 1/e + 1/e² + … with a general dimmer strength x equals 1 divided by (e raised to x minus 1). That fraction blows up wherever e raised to x equals 1. In ordinary growth that happens at x = 0. In the sideways direction that happens again at 6.283 and 12.566 and 18.850 which are 1 and 2 and 3 full laps.

Each hidden lap point adds a share to the 1/12 piece. The share from lap k is 2 divided by (2 × pi × k) squared.

- Lap 1 adds 0.0507 which is about 61% of the 1/12.
- Lap 2 adds 0.0127.
- Lap 3 adds 0.0056.

The shares total 0.0833 = 1/12.

## Question: how does −1/12 relate to 1.645?

−1/12 equals −1.645 divided by 19.739. The number 1.645 is the settled total of 1 + 1/4 + 1/9 + 1/16 + … and 19.739 is 2 × pi × pi. The sum 1.645 is a rounded form of pi × pi divided by 6 = 1.6449341. Dividing 2 × pi × pi by the rounded 1.645 gives 11.9995 and dividing by the unrounded value gives exactly 12 because the pi × pi cancels and leaves 2 × 6.

The next pair follows the same pattern. The sum of cubes has the leftover constant 1/120 and the sum of 1 over each fourth power settles at 1.0823 = pi to the fourth power divided by 90. The recipe "multiply by 6 and divide by 8 × pi to the fourth power" turns 1.0823 into 1/120.

The running totals of 1 + 1/4 + 1/9 + … are 1 and 1.25 and 1.361 and 1.424 and 1.464 and after 1000 terms the total is 1.6439.

## Question: where does the 6 in pi × pi divided by 6 come from? (The wave route.)

The sine wave crosses zero at every whole multiple of pi. The wave can be described two ways.

- Built from powers the wave near zero is x minus (x cubed divided by 6) where the 6 is 1 × 2 × 3.
- Built from its zero crossings the wave is x times (1 − x squared over pi squared) times (1 − x squared over 4 pi squared) times (1 − x squared over 9 pi squared) and so on.

Multiplying out the second description the "x cubed" part collects (1 + 1/4 + 1/9 + …) divided by pi squared. The two descriptions must agree so that quantity equals 1/6.

## Question: is there a different way to see the pi squared? (The lamp route.)

"The zeta function at 2" means the dial of the family of sums is set to 2 which picks out 1 + 1/4 + 1/9 + …

The brightness of a lamp falls off as 1 divided by the distance squared. Stand at 0 on a number line with lamps at 1 and 2 and 3 and so on. The total brightness is 1 + 1/4 + 1/9 + …

**Stage 0.** Take a circle whose distance around is 2. Stand at the bottom with one lamp at the top. Pi is "around divided by across" so the lamp is 2 / pi = 0.6366 away. The brightness is 1 / (0.6366 × 0.6366) = 2.4674 = pi × pi / 4. One pi is there because the lamp is one "across" away. The second pi is there because brightness uses the distance twice. The 4 is the distance around squared.

**The swap.** For a triangle with a square corner the two short sides a and b and the height h down to the long side obey 1/h² = 1/a² + 1/b². So one lamp at distance h is exactly as bright as two lamps at distances a and b.

**Stage 1.** Draw a circle twice as big touching your spot. Its center lands where the old lamp was. A level line through the center hits the circle at two points. Lamps at those two points replace the old lamp. Each new lamp is 0.9003 away in a straight line and gives 1.2337 so the two give 2.4674. Along the rim the lamps sit 1 to your left and 1 to your right.

**Stage 2.** The same swap on each lamp with a circle of distance around 8 gives four lamps at rim spots 1 and 3 on each side. The straight distances are 0.9745 and 2.3527 and the total brightness is 2.4674.

**Every later stage.** The lamps sit 2 apart along the rim at the odd spots and the total stays 2.4674. On a huge circle the rim near you is almost straight. With a distance around of 1024 the nearest straight distances are 0.999998 and 2.99996. In the limit the lamps sit at straight distances 1 and 3 and 5 and so on to each side.

So 2 × (1 + 1/9 + 1/25 + …) = pi × pi / 4. The row added directly creeps upward: 2 then 2.222 then 2.302 then 2.343.

## Question: how does pi × pi / 4 become pi × pi / 6?

- One side alone gives half: 1 + 1/9 + 1/25 + … = pi × pi / 8 = 1.2337.
- The even lamps at 2 and 4 and 6 are still missing. Their brightness is 1/4 + 1/16 + 1/36 + … and each term is one quarter of a term of the full sum. So the even lamps are one quarter of the full sum (0.4112).
- The odd lamps are therefore three quarters of the full sum. 1.2337 × 4/3 = 1.6449 = pi × pi / 6.

## Question: what is the chance that a number picked at random has no repeated prime piece?

The chance is 6 divided by (pi × pi) = 60.79%. Exactly 607926 of the numbers from 1 to one million have no repeated prime piece.

A number fails when some prime squared divides the number. The sieve with squares removes the multiples of 4 (75% left) and then of 9 (66.7% left) and of 25 (64.0%) and of 49 (62.7%) and of 121 (62.2%) and of 169 (61.8%). The share settles at 60.79%.

The ordinary sieve has shrink announcements 1/2 and 1/3 and 1/5 whose pile grows without limit so the share left heads to zero. The square sieve has announcements 1/4 and 1/9 and 1/25 whose pile settles at 0.4522 so a positive share survives.

Flipped upside down the factor for the prime 2 becomes 1 / (1 − 1/4) = 1 + 1/4 + 1/16 + … and the prime 3 gives 1 + 1/9 + 1/81 + … Multiplying those sums across every prime produces 1 over each whole number squared exactly once because each number is built from primes in one way. So the flipped product is pi × pi / 6.

The same number is the chance that two numbers picked at random share no prime piece. Out of one million random pairs 608244 shared no prime piece.

## Question: what does the zeta function at 1/2 mean?

The dial at 1/2 gives 1 + 1/√2 + 1/√3 + … which adds 1 over the square root of each whole number. The total is 18.59 after 100 terms and 198.54 after 10000 terms. The growing part is twice the square root of the number of terms. Taking the growing part away leaves −1.41 and then −1.455 and the leftover heads to −1.4604 which is the value of the zeta function at 1/2.

The mirror rule pairs the setting s with the setting 1 − s so the setting 1/2 pairs with itself.

The dial can also carry a sideways amount. A sideways amount does not change the size of a term and only turns the term. With the dial at 1/2 plus a sideways amount t the term for the number n is an arrow of length 1 over the square root of n turned by an angle of t times the natural logarithm of n. The critical line is the family of settings with the dial at 1/2 and every sideways amount.

For certain sideways amounts the chain of arrows closes up and the total is zero. The first few are 14.13 and 21.02 and 25.01. Each such zero produces one ripple in the count of primes.

## Question: 1 divided by the square root of 3 looks like another number near the Omega constant. Is the number related?

1 divided by the square root of 3 is 0.5773503 and the gap constant is 0.5772157. The two agree to three digits and differ by 0.00013. No equation is known that ties the two together.

In its own right 0.57735 is the slope of a line tilted at 30 degrees and the distance from the center of a triangle with three equal sides of length 1 to a corner and the typical wobble of a value picked evenly at random between −1 and 1.

Feeding 0.57735 into "1/e raised to that number" gives 0.56138 next to the sieve constant 0.56146. That closeness is forced by the first one.

Two unrelated numbers between 0 and 1 agree to within 0.00013 about once in 4000 tries and simple recipes number in the thousands. A real link holds for every digit. This match stops at three digits.

## Question: what are the ripples?

Add the natural logarithm of a prime each time a prime or a power of a prime is passed on the number line. That running total is a jagged staircase and the smooth guess for the staircase at the point x is x.

A ripple is a pure wave added to the smooth guess. The first ripple (from the zero at 14.13) has these values.

- +0.37 at 8 and −0.41 at 10.
- +0.46 at 12.5 and −0.57 at 16.
- +0.63 at 20 and −0.71 at 25.
- +0.78 at 31 and −0.88 at 39.
- +0.99 at 49 and −1.10 at 61.

Each crest is about 1.56 times further along than the one before so the wave is evenly spaced on the logarithm scale. The height at each point is 0.14 times the square root of that point. The ripple from 21.02 repeats at a factor of 1.35 and the ripple from 25.01 at a factor of 1.29.

A plus value says the staircase runs ahead of the smooth guess there and a minus value says the staircase runs behind. Added together the ripples pile up where a prime or a power of a prime sits and cancel in between. A sharp click can be built from many pure tones that peak at one instant and the staircase is a row of clicks.

A count at 20.5 where the true staircase is 19.266:

- The smooth guess alone gives 18.663.
- Adding the first ripple gives 19.272.
- Adding 200 ripples gives 19.256.

At 50.5 the true staircase is 49.485 and the smooth guess gives 48.662 and 200 ripples give 49.557. The totals settle slowly and higher points need many more ripples. With every ripple included the formula is exact which is a proven result.

## Question: why is "no zero at dial 1" the same as the rule 1 divided by the natural logarithm?

The height of a ripple is x raised to its dial position. The smooth guess is a ramp which is x raised to the power 1. A zero at dial 1 would give a ripple that grows as fast as the ramp so the staircase would never settle onto the ramp. With every dial below 1 each ripple shrinks as a share of the ramp. "The staircase closes in on the ramp" unpacks to "primes near a number show up at the rate 1 divided by the natural logarithm". That was proven in 1896.

At one million a ripple at dial 1/2 has a height near 141 (0.014% of the ramp). A ripple at dial 0.9 would have a height near 35500 (about 3.6%). A ripple at dial 1 would stay near 14% at every size.

## Question: what are the smooth ramp and the chord of pure tones and the same square root rate?

On the logarithm scale each ripple is a pure tone with a fixed pitch. The pitches 14.13 and 21.02 and 25.01 and 30.42 and 32.94 are not whole-number multiples of one another so the chord sounds like a bell. The staircase equals the ramp plus all the tones.

Subtract the ramp and divide by the square root of x. If every zero has its dial at 1/2 then what remains is a steady chord whose tones never get louder or quieter. The loudness of each tone is about 2 divided by its pitch (0.141 and 0.095 and 0.080 for the first three).

The steady chord measured: +0.13 at 10000 and +0.16 at 100000 and −0.41 at one million.

A zero at dial 0.6 would leave a tone growing like x raised to the power 0.1 which is 4 times louder at one million and ten billion times louder at a 100 digit number. The unproven claim about the critical line says no tone does that.

The mirror rule pairs a zero at dial 1/2 plus an offset with a partner at 1/2 minus the offset so zeros cannot all sit left of 1/2. Every zero exactly on 1/2 is the calmest arrangement the mirror allows. What is proven: every zero of this kind has its dial strictly between 0 and 1. More than 40% of the zeros sit exactly on 1/2. Computers have checked about the first ten trillion zeros and found every one on 1/2.

## Question: what hidden regularity does the wave view expose?

The gaps between primes from 50 million to 100 million have an average of 18.1 and a spread of 15.5. A spread nearly as large as the average is the mark of the waiting-time shape.

The first 200 pitches with gaps rescaled to an average of 1:

- The spread of the gaps is 0.36 against 1 for a waiting-time shape.
- The smallest gap is 0.32 and the largest is 1.96.
- No gap is below one quarter of the average where a waiting-time shape would put 22% of the gaps.
- 5% of the gaps are below half the average where a waiting-time shape would put 39%.

A short formula counts the pitches below any height: (height / (2 × pi)) times (the natural logarithm of (height / (2 × pi)) minus 1) plus 7/8. At 100 the formula gives 29.002 and the true count is 29. At 396 the formula gives 198.998 and the true count is 199. The "minus 1" is the average-logarithm correction from the first page.

The pitches determine every prime and the primes determine every pitch. The raggedness of the primes is traded for a list that is evenly spread. The regularity is statistical: no formula is known that gives the pitches one by one.

## Question: could digits be stored as arrows tilted at different degrees to save space?

The scheme is a reversible code. A slope of 0.577 belongs to an arrow at 29.985 degrees and a slope of 0.698 belongs to an arrow at 34.915 degrees.

A typical chunk does not get shorter. One hundredth of a degree moves the slope by about 0.0002 so the angle must be written to two decimal places. There are 1000 possible three-digit chunks so any code needs 1000 different labels.

Some numbers get a huge saving. The slope of an arrow at exactly 30 degrees is 0.5773502691896… and "30" plus the word "slope" rebuild every digit. A number can be stored in less space exactly when a short recipe produces the number. Most long strings of digits have no recipe shorter than the digits because there are far more long strings than short recipes.

Sound and photo files are stored as lists of waves with a strength for each wave. The saving there is from the smoothness of the data and from dropping weak waves.

## Question: what more is there to the sum of 1 over each prime growing like the logarithm of the logarithm?

**The sum counts prime pieces.** The sum of 1 over each prime up to x is the average number of different primes dividing a number up to x. The average over every number up to one million is 2.854 against a sum of 2.887.

- 7.9% of the numbers up to one million have exactly one prime piece (the primes and the powers of one prime).
- 28.9% have two different prime pieces.
- 38.0% have three.
- 20.8% have four.
- 4.2% have five.
- 0.23% have six and 8 numbers have seven.

A typical 100 digit number has about 5.7 different prime pieces.

**Equal gains for each doubling of the digit count.** Primes up to 100 give 1.803. Primes up to 10000 give 2.483 (a gain of 0.680). Primes up to one hundred million give 3.175 (a gain of 0.692). The 5760226 primes with 5 to 8 digits add no more than the 1204 primes with 3 or 4 digits.

**The smoothness.** At one hundred million the true sum is 3.174975 and the formula "double logarithm plus 0.2615" gives 3.174971.

## Question: why is the expected count of different primes dividing a random number equal to the sum of 1 over each prime?

Make a tally sheet. The rows are the numbers 1 through 30. The columns are the primes 2 and 3 and 5 and 7 and 11 and 13 and 17 and 19 and 23 and 29. Put a mark wherever the column's prime divides the row's number.

**Counting by rows.** Each row's marks are that number's different prime pieces. The number 30 has three marks (2 and 3 and 5) and the number 16 has one mark and the number 1 has none. The rows total 43 marks so the average is 43 / 30 = 1.43 marks per number.

**Counting by columns.** The column for 2 has 15 marks because every second number gets one. The column for 3 has 10. The column for 5 has 6. The column for 7 has 4. The columns for 11 and 13 have 2 each. The columns for 17 and 19 and 23 and 29 have 1 each. The columns total 15 + 10 + 6 + 4 + 2 + 2 + 1 + 1 + 1 + 1 = 43.

Both counts cover the same marks so the totals agree. The column for a prime p holds about 30 / p marks so the average per number is about 1/2 + 1/3 + 1/5 + … That sum over the ten primes is 1.53. The true 1.43 is a little lower because a column cannot hold a part of a mark (30 / 7 is 4.29 and the column holds 4).

The rule needs no assumption that the primes act independently. Averages add even when the events overlap. The number 30 sits in three columns at once and is counted once in each.

## How the questions tie back to the lists

- Blocking the small primes lifts a recipe because most of the average count of prime pieces sits with the small primes (1/2 + 1/3 + 1/5 + 1/7 is 1.176 of a total near 5.7 for a 100 digit number).
- The "give or take" figure on each line is square root sized which is the same size as the ripples when the dial sits at 1/2.
- The stronger bump rule avoids outputs that share small prime pieces which is a sieve of the same kind as the square sieve above.
