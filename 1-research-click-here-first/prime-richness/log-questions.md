# Questions about logarithms and e and the prime baseline

> **About this page:** One AI model (Claude) wrote this page on 21 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The facts on this page are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route through the facts. A program rechecked every figure (the file log_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## Why the page sits in this folder

Every percentage in this folder compares a recipe with the plain number line and the plain number line baseline is "the chance that a number is prime is about 1 divided by the natural logarithm of the number". So a reader who wants to know what the percentages rest on needs to know what a natural logarithm is and why the number e = 2.718 is inside the baseline. The questions below build that picture one step at a time.

## Question: is a logarithm the count of how many times the base gets multiplied?

Yes with one adjustment. A logarithm counts the copies of the base and not the multiplication signs. The number 100000 is 10 × 10 × 10 × 10 × 10 which has five 10s and four multiplication signs so the base 10 logarithm of 100000 is 5.

- The base 10 logarithm of 1000 is 3 because three 10s make 1000.
- The base 2 logarithm of 1024 is 10 because ten 2s make 1024.
- The base 10 logarithm of 50 is about 1.7 because 50 sits between one 10 and two 10s and 10 raised to the power 1.7 is about 50.

The natural logarithm uses the base e = 2.718. The natural logarithm of 100000 is 11.513 which means about 11.5 copies of 2.718 multiplied together make 100000. One 10 is worth 2.3026 copies of 2.718 so any base 10 logarithm times 2.3026 gives the natural logarithm.

## Question: what is the difference between (log of 5) divided by 2 and log of (5 divided by 2)?

Dividing outside the logarithm takes a square root of the 5 while dividing inside the logarithm removes one "copy of 2" from the 5.

- (log of 5) divided by 2 = 0.6990 / 2 = 0.3495 which is the logarithm of 2.236 and 2.236 is the square root of 5.
- log of (5 / 2) = log of 2.5 = 0.3979 which equals 0.6990 − 0.3010 where 0.3010 is the logarithm of 2.

The reason is that a logarithm is a count of copies and counts of copies add when numbers multiply. So multiplying inside becomes adding outside and dividing inside becomes subtracting outside and a square root inside becomes dividing by 2 outside.

A worked case: 10000 is four 10s and 100 is two 10s. Dividing 10000 by 100 cancels two of the four 10s and leaves two 10s so the logarithm of the answer is 4 − 2 = 2. The number 2 is worth 0.301 of a copy of 10 so 10000 divided by 2 leaves 4 − 0.301 = 3.699 copies and 10 raised to the power 3.699 is 5000.

## Question: is a logarithm a kind of compression?

Yes. A logarithm takes in a big number and hands back the small count of copies of the base that rebuilds the number. The number 1000000000000 takes thirteen digits to write and the base 10 logarithm is 12.

The compression is like a blurry thumbnail of a photo when only a few digits of the logarithm are kept. The logarithm of 997 is 2.99870 and the logarithm of 998 is 2.99913 so telling those two neighbors apart needs four or five decimal places. Restoring every digit of a big number needs the logarithm written to about as many digits as the number had.

The measure of information is itself a logarithm. Picking one item out of 1024 takes ten yes-or-no questions because ten 2s make 1024 so the base 2 logarithm of the pile size is the smallest number of bits that can label every item.

## Question: is writing a number as e to a power also compression?

Raising e to a power and taking the natural logarithm are one machine running in two directions. The natural logarithm is the squeezing step (997 goes in and 6.905 is handed back). Raising e to a power is the unpacking step (6.905 goes in and 997 is handed back). A number written on paper as "e to the power 6.905" is the squeezed form sitting on the shelf with a label that says which base unpacks the number.

## Question: when the count is not a whole number can the whole part unpack first while the leftover part waits?

Yes. A power splits wherever the count splits because counts of copies add when numbers multiply. So e to the power 6.905 equals (e to the power 6) × (e to the power 0.905). The whole part unpacks by plain repeated multiplying: six copies of 2.718 make 403.4. The leftover part is a root and not a plain multiplication: 0.905 of a copy is worth 2.472. The product 403.4 × 2.472 is 997.

The whole part sets the rough size and the leftover part sets the fine detail. Base 10 shows the split most clearly. The base 10 logarithm of 997 is 2.9987 so 997 = (10 to the power 2) × (10 to the power 0.9987) = 100 × 9.97. The whole part 2 says "three digit number" and the leftover part 0.9987 says "the digits are 9 9 7". A number written as 9.97 × 10² is that same split written on paper.

## Question: how does the product of the (1 − 1/p) factors relate to the expression (1 + 1/n) multiplied n times that equals e?

The expression (1 + 1/n) multiplied n times closes in on e = 2.718 as n grows (2.7048 at n = 100). The minus version (1 − 1/n) multiplied n times closes in on 1/e = 0.3679 (0.3660 at n = 100 and 0.3677 at n = 1000).

So one factor (1 − 1/n) is worth about "one n-th of a division by e". A fraction of a division means a smaller shrinking step that has to be repeated before the total equals one full division.

- One full division by e multiplies by 0.3679.
- Half of a division multiplies by 0.6065 because 0.6065 × 0.6065 = 0.3679.
- One tenth of a division multiplies by 0.9048 because ten copies of 0.9048 multiplied together make 0.3679. The factor (1 − 1/10) = 0.9 is close to 0.9048.

The sieve removes the multiples of each prime. After the prime 2 half of all numbers are left. After the prime 3 one third are left. After the prime 5 the share left is 26.7% and after the prime 7 the share is 22.9% and after the prime 11 the share is 20.8%. Each prime p multiplies the share left by (1 − 1/p).

The prime 7 gives the factor 0.8571 and one seventh of a division by e is 0.8669. The prime 101 gives 0.990099 and one hundred-and-first of a division by e is 0.990148. So stacking the primes acts like (1/2 + 1/3 + 1/5 + 1/7 + …) divisions by e. The sum of 1 over each prime up to x grows like the natural logarithm of the natural logarithm of x and "1/e raised to a natural logarithm" undoes the logarithm. The result is that the share left after sieving by every prime up to x is about 0.5615 divided by the natural logarithm of x.

## Question: where does the constant 0.5772 come from?

The constant 0.5772 (often written with the Greek letter gamma) is the gap between the sum 1 + 1/2 + 1/3 + … + 1/n and the natural logarithm of n.

- At n = 10 the sum is 2.9290 and the natural logarithm is 2.3026 so the gap is 0.6264.
- At n = 100 the gap is 0.5822.
- At n = 1000 the gap is 0.5777.
- At n = 1000000 the sum is 14.3927 and the natural logarithm is 13.8155 so the gap is 0.5772.

A picture: a staircase has steps that are 1 tall and then 1/2 tall and then 1/3 tall and each step is 1 wide. A smooth downhill slide touches the back corner of every step. The area under the slide is the natural logarithm and the area of the staircase is the sum. The gap is the total area of the corner pieces of the steps that poke above the slide. The first four corner pieces have areas 0.3069 and 0.0945 and 0.0457 and 0.0269 which total 0.4740 and the rest of the pieces bring the total to 0.5772.

The sieve constant 0.5615 is 1/e raised to the power 0.5772. The link exists because the sieve product turned upside down becomes the sum 1 + 1/2 + 1/3 + … so the head start of the sum over the logarithm is carried into the sieve.

The primes have a constant of the same kind. The sum 1/2 + 1/3 + 1/5 + … over the primes stays ahead of "the natural logarithm of the natural logarithm" by a gap that settles at 0.2615. For the primes up to 997 the sum is 2.198 and the natural logarithm of 6.905 is 1.932 so the gap there is 0.266.

## Question: what is the 1.123 figure?

A sieve needs only the primes up to the square root of N to find every prime below N. The natural logarithm of a square root is half the natural logarithm of the number. So "0.5615 divided by the natural logarithm" becomes 0.5615 divided by half of ln N which is 1.123 divided by ln N. The true share of primes near N is 1 divided by ln N so the sieve multiplication overshoots by 12.3%. The overshoot exists because the multiplication treats each prime as removing an exact share and that treatment is rough for primes near the square root of N which have only a few multiples below N.

The percentages in this folder use 1 divided by the natural logarithm as the baseline so the percentages do not carry the 12.3% overshoot.

## Question: what is the infinite sum 1/e + 1/e² + 1/e³ + …?

The sum is 1 divided by (e − 1) = 0.5820. Each term is the term before multiplied by 0.3679 so the total is "first term divided by (1 minus the shrink factor)" = 0.3679 / 0.6321. The running totals are 0.3679 then 0.5032 then 0.5530 then 0.5713 then 0.5781. Starting the sum with a leading 1 gives 1.5820.

## Question: how do the numbers near 0.56 relate to the Omega constant?

The Omega constant is 0.5671 and is the one number that equals 1/e raised to itself. Six numbers built from e and pi sit between 0.56 and 0.59.

- 0.5615 is the sieve constant.
- 0.5642 is 1 divided by the square root of pi which is the scaling number that makes the area under a bell curve equal 1.
- 0.5671 is the Omega constant.
- 0.5724 is half the natural logarithm of pi.
- 0.5772 is the gap constant from the question above.
- 0.5820 is the sum 1/e + 1/e² + 1/e³ + …

One real mechanism sits inside the cluster. Feeding any starting number into "1/e raised to that number" over and over spirals in to the Omega constant. Starting from 0.5772 the chain runs 0.5615 then 0.5704 then 0.5653 then 0.5682 and each bounce lands on the other side of 0.5671 and keeps about 57% of the distance. Starting from 0 the chain runs 1 then 0.3679 then 0.6922 then 0.5005 then 0.6062 then 0.5454 then 0.5796 then 0.5601. So the sieve constant 0.5615 sits near the Omega constant because 0.5772 does and that makes the pair one coincidence and not two.

The closeness of 0.5772 to the Omega constant has no known explanation and no known equation builds one from the other. Short recipes built from e and pi mostly land between 0 and 1 and a window from 0.56 to 0.58 covers 2% of that stretch so a few hundred recipes would put several in the window by chance.

A test for a real link: a real link is an equation that turns one number into the other and the equation holds in any number base. A link that is only matching digits stops when more digits are written. The square of the Omega constant is 0.32165 which opens with 3 then 2 then 1 and the sieve overshoot figure is 1.123 but 1.123 is the rounded form of 1.12292 so the mirror of 1 2 3 and 3 2 1 is a base 10 accident. The square of the Omega constant does have one exact meaning: the square equals 1/e raised to the power 1.1343 which is twice the Omega constant.

The Omega constant is proven to be a number that is not the root of any whole-number polynomial. Whether 0.5772 can be written as a fraction is an open question.

## Question: how does the bell curve connect to the square root and the half?

Taking a square root cuts a logarithm in half. The natural logarithm of 1000000 is 13.82 and the natural logarithm of the square root 1000 is 6.91.

The height of the bell curve at a given distance from the center is 1/e raised to the power (distance squared divided by 2) where the distance is counted in typical wobbles. So the bell curve is written in divisions by e.

- At 1 typical wobble the height has had half a division by e which leaves 0.6065.
- At 2 typical wobbles the height has had 2 divisions by e which leaves 0.1353.
- At 3 typical wobbles the height has had 4.5 divisions by e which leaves 0.0111.

The size of one typical wobble in a count is the square root of the expected count. A stretch of the number line expected to hold 10000 primes typically lands within about 100 of that count. The "give or take" figure on each line of the master lists uses that square root. The counts of primes in a window follow the bell curve while the single gaps between neighboring primes follow the lopsided waiting-time shape.

## Question: what is the rule where a prime such as 997 gets divided by a logarithm?

The rule estimates how many primes sit below a number: divide the number by the natural logarithm of the number. The natural logarithm of 997 is 6.905 (the base 10 logarithm is 3). Exactly 168 primes sit at or below 997.

- 997 / 6.905 = 144.4 which undershoots 168 by about 14%.
- 997 / (6.905 − 1) = 168.8 which is nearly exact.

Old hand-counted tables suggested a correction of 1.08366 in place of 1. At one million the true count is 78498 and the 1.08366 version gives 78543 while the 1 version gives 78030 so the old guess did fit the tables of the time. The correction drifts down to exactly 1 as the numbers grow without limit.

## Question: is subtracting 1 from the logarithm the same as removing one copy of e?

Yes. 6.905 − 1 = 5.905 and 5.905 copies of 2.718 make 366.8 which is 997 divided by e. So the corrected rule is "997 divided by the natural logarithm of 366.8". The plain rule applies the thin prime share at 997 to the whole stretch from 1 to 997 and the smaller numbers in the stretch are richer in primes. The repair uses the prime share at 366.8 as the stand-in for the whole stretch.

## Question: what does "the average of the natural logarithm" mean?

Take the natural logarithm of every number in the stretch and add the logarithms and divide by how many numbers there were.

- For 1 through 10 the average is 1.510 and the natural logarithm of 10 minus 1 is 1.303.
- For 1 through 100 the average is 3.637 and the natural logarithm of 100 minus 1 is 3.605.
- For 1 through 997 the average is 5.909 and the natural logarithm of 997 minus 1 is 5.905.

The average sits one copy of e below the top for this reason. Think of each number below 997 as "997 with some copies of e taken away".

- About 63.2% of the numbers sit between 367 and 997 and are missing less than one copy.
- About 23.3% sit between 135 and 367 and are missing between one and two copies.
- About 8.6% sit between 50 and 135 and are missing between two and three copies.
- About 5.0% sit below 50 and are missing three copies or more.

Each band is 1/e times the size of the band before. The average number of missing copies across the bands is exactly 1. The band pattern is the same waiting-time shape that the gaps between primes follow.

## Question: what does "a typical multiplying size of 997 divided by e" mean?

Numbers can be averaged by adding or by multiplying. For 2 and 8 the adding average is 5 because 5 + 5 = 2 + 8. The multiplying average is 4 because 4 × 4 = 2 × 8.

For 1 through 997 the adding average is 499 and the multiplying average is about 368 which sits next to 997 / e = 366.8. A logarithm turns multiplying into adding so the average natural logarithm (5.909) and the multiplying average (368) are one fact said two ways because 5.909 copies of 2.718 make 368.

The multiplying average is the better stand-in for the prime count. Using 499 gives 997 / 6.213 = 160.5 and using 366.8 gives 168.8 and the true count is 168.

## Question: does e relate to random events?

Yes. The number e shows up when many small independent chances get multiplied.

- If an event is expected once on average then the chance of zero events is 1/e = 36.8%.
- If random numbers between 0 and 1 are added until the total passes 1 then the average count of numbers needed is e.
- The waiting-time curve is 1/e raised to (the wait divided by the average wait) so a wait of twice the average shows up 13.5% of the time.

The primes behave enough like small independent chances that e ends up under the whole prime baseline.

## How the questions tie back to the lists

- The baseline on every line of [ranked-list.md](ranked-list.md) is 1 divided by the natural logarithm of each output.
- The "give or take" figure on each line is a square root because of the bell curve rule above.
- The lines built from the product of all primes up to some prime lean on the unpacking direction. The product of all primes up to 1009 has a natural logarithm of 963 which means the product has about 419 digits.
- A recipe that blocks the small primes gains the factor that the sieve would have removed which is why blocking every prime up to p multiplies the prime share by about 1.78 times the natural logarithm of p (1.78 is 1 divided by 0.5615).
