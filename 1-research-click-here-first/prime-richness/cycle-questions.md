# Questions about cycles in the digits of polynomials and why the primes have no cycle

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The author reasoned that a polynomial must have a cycle in its digits and the primes have none so no polynomial can output the primes. The author also described the square of a prime as the signature of that prime. The page continues the sixteen earlier question pages in this folder (the last one is [random-questions.md](random-questions.md)). The counts are measurements from the programs in the folder boring-things/research-program-files/prime-richness-scripts/cycle-scripts. The mathematics is standard and the page claims no new result. No other person has reviewed the page yet.

## Do the other digits of a polynomial cycle the way the last digit does?

Yes for every digit counted from the right end and no for the digits at the front.

Adding 100 to x does not change the last two digits of x. So the value of a polynomial with whole number coefficients at x and at x plus 100 end in the same two digits. The tens digit therefore repeats in a cycle that divides 100 and the hundreds digit in a cycle that divides 1000.

Measured cycle lengths for the last digit then the tens digit then the hundreds digit then the thousands digit:

- x squared: 10 then 50 then 500 then 5000.
- x cubed: 10 then 100 then 1000 then 10000.
- x squared minus x plus 1: 5 then 100 then 1000 then 10000.
- 2 times x squared minus 1: 5 then 50 then 250 then 2500.
- x to the power 4: 10 then 50 then 250 then 1250.
- x squared plus x plus 41: 5 then 100 then 1000 then 10000.

A polynomial also skips many endings. Square numbers end in only 22 of the 100 possible pairs of last two digits and fourth powers end in only 12.

The first digit does not cycle because the first digit depends on the size of the number. For the square numbers the first digit stays at 1 for 5 values in a row and later for 13 values and later for 42 values. Each stretch is about three times longer than the one before so no fixed cycle length fits.

## Do the last digits of the primes cycle?

No. The last digits of the first ten primes are 2 3 5 7 1 3 7 9 3 9 and the last digits of the next ten are 1 7 1 3 7 3 9 1 7 1. A known theorem rules out a cycle that starts later: for each of the digits 1 and 3 and 7 and 9 there are runs of consecutive primes that all end in that digit and those runs get as long as anyone asks for. A fixed cycle would cap the length of such runs.

## Does that mean no polynomial outputs the primes?

Yes and the author's reasoning is valid for a polynomial with whole number coefficients that is supposed to give the primes in order. Such a polynomial has last digits that repeat every 10 values and the last digits of the primes in order do not.

A polynomial that outputs only primes without listing every prime needs one more step. Suppose the polynomial gives a prime q at some x. Adding q to x does not change the remainder after dividing by q. So the values at x plus q and x plus 2q are divisible by q. A polynomial that is not constant grows without limit so those values soon exceed q and are not prime. So no polynomial in one variable with whole number coefficients outputs only primes unless the polynomial is constant. This result is old and well known.

Two limits: a known polynomial in 26 variables has positive outputs that are exactly the primes and the argument says nothing about formulas that are not polynomials.

## Can a polynomial rule that picks certain primes find a cycle?

None showed up in the tests. The chatbot took the 1270607 primes below 20 million and picked primes by position. For each picked list the program tried every cycle length and measured how often the last digit matched the last digit one cycle later. A true cycle gives 100% and four digits with no pattern give about 25%.

- Every second prime up to every 60th prime from every starting offset (1830 lists of about 20000 primes): the best match anywhere was 26.56%.
- The primes in positions n squared: 28.66%. Random lists of the same length reach 29.05% on average because many cycle lengths get tried.
- The primes in positions n cubed: 36.47% on a list of 103 primes. Random lists that short reach 34.88% on average and 44.44% at most.
- The primes in positions 1 and 3 and 6 and 10: 28.60% against 28.32% for random lists.
- The primes in positions n squared plus n plus 41 and 2 times n squared minus 1 and 1000 times n plus 7: 29.50% and 31.72% and 29.05% which all sit inside the range that random lists reach.

For the full list of primes the lack of a cycle is proven. For primes picked by a polynomial rule the chatbot knows of no proof either way. The tests and the common belief that the last digits of primes behave like random digits both point to no cycle.

## Does each new prime break a cycle that could have formed?

Yes and there is an exact version of the idea. Cross out the multiples of 2 and the numbers left repeat every 2. Cross out the multiples of 3 as well and the numbers left repeat every 6. Add 5 and the numbers left repeat every 30 with 8 survivors in each block: 1 and 7 and 11 and 13 and 17 and 19 and 23 and 29. Then 7 crosses out 49 and 77 and 91 which the cycle of 30 had kept. The new cycle is 210 long with 48 survivors. Then 11 breaks that cycle and the new cycle is 2310 long.

So every stage has a cycle and every new prime breaks the cycle and replaces the cycle with a longer one. The cycle lengths 2 then 6 then 30 then 210 then 2310 grow without limit. Each prime is certain to break something because the square of the prime survived every smaller prime.

## Can the breaks be predicted beyond the square of the prime?

Yes. A new prime breaks the old cycle at the new prime times each survivor of the old cycle. For 7 the breaks are 7 times 7 and 7 times 11 and 7 times 13 and 7 times 17 and 7 times 19 and 7 times 23 and 7 times 29 and 7 times 31 which gives 49 and 77 and 91 and 119 and 133 and 161 and 203 and 217.

The spacing of the breaks is the old spacing stretched by the prime. The survivors of the cycle of 30 are spaced 4 then 2 then 4 then 2 then 4 then 6 then 2 then 6 and the breaks made by 7 are spaced 28 then 14 then 28 then 14 then 28 then 42 then 14 then 42.

Every survivor below the square of the next prime is a true prime. After crossing out by 2 and 3 and 5 every survivor below 49 is prime.

The process is predictable one step at a time. No shortcut that skips the steps is known.

## Why is the square of a prime the signature of that prime?

The square is the smallest number where that prime is the only prime inside. Every multiple of 7 below 49 holds a smaller prime that claims the number first: 14 holds 2 and 21 holds 3 and 35 holds 5. The number 49 is seven copies of 7 and no smaller prime divides 49.

- The square of a prime has exactly three divisors. Below 200 the numbers with exactly three divisors are 4 and 9 and 25 and 49 and 121 and 169.
- 60.793% of the numbers up to one million are not divisible by the square of any prime. That share equals 6 divided by pi squared which ties the squares of the primes to the zeta function at 2.
- In the family x squared plus x plus a constant the run of primes ends at the square of the constant every time: 1681 for 41 and 289 for 17 and 121 for 11 and 25 for 5 and 9 for 3 and 4 for 2. Putting the constant minus 1 in for x always gives the constant squared.

A limit: the square is not the break for every polynomial. The formula 2 times x squared plus 29 fails first at 1711 which is 29 times 59. What holds for every polynomial is that a prime output plants a later output divisible by that same prime.

## Which numbers does each prime truly cross off?

These are the numbers where the prime is the smallest prime inside so no smaller prime claims the number first.

- 2: 4 and 6 and 8 and 10 and 12 and 14.
- 3: 9 and 15 and 21 and 27 and 33 and 39.
- 5: 25 and 35 and 55 and 65 and 85 and 95.
- 7: 49 and 77 and 91 and 119 and 133 and 161.
- 11: 121 and 143 and 187 and 209 and 253 and 319.
- 13: 169 and 221 and 247 and 299 and 377 and 403.
- 29: 841 and 899 and 1073 and 1189 and 1247.
- 97: 9409 and 9797 and 9991 and 10379 and 10573.
- 997: only 994009 below one million.

Share of all numbers up to one million that each prime is the first to cross off: 50.000% for 2 and 16.667% for 3 and 6.667% for 5 and 3.809% for 7 and 2.078% for 11 and 1.598% for 13 and 1.128% for 17 and 0.950% for 19 and 0.743% for 23 and 0.124% for 97. Each share matches the rule that a prime gets one share out of its own size from what the smaller primes left. So 2 and 3 and 5 together cross off 73.3% of all numbers.

Inside each list sits a stricter group: the pure powers where no other prime appears at all such as 4 and 8 and 16 for 2 and 9 and 27 and 81 for 3 and 49 and 343 for 7.

## If the list of primes is capped can a polynomial output every prime on the list?

Yes. For any finite list of numbers a polynomial exists that hits every number in order when the degree may be one less than the length of the list. One million primes need a degree of 999999.

- The polynomial for the first 3 primes is one half of x squared minus one half of x plus 2.
- The polynomial for the first 5 primes has the coefficients 6 and −103/12 and 47/8 and −17/12 and 1/8.

Each polynomial fails right after the cap. The one for 3 primes continues with 8 then 12 then 17. The one for 5 primes continues with 22 then 48 then 100. The one for 10 primes continues with −426 then −4189 then −21722.

The coefficients must be fractions. A polynomial with whole number coefficients changes by an even amount when x moves by 2 and the primes go from 2 at the first position to 5 at the third position which is a change of 3. So no polynomial with whole number coefficients matches even the first three primes in order.

The capped polynomial is not a pattern in the primes. The polynomial for one million primes needs about one million coefficients that are worked out from the primes themselves so the polynomial stores the list and does not shorten or explain the list.

## How does this connect to food and shelter and deep human connection?

Knowing where a prime first shows itself does not cook a meal or pay rent. The page offers an example of a hidden thing that becomes visible at one exact spot. A person who learns to ask where something first shows itself can ask the same about another person's heart because people also carry things that louder voices cover until one moment when nothing else can speak for them. The page sits in public for free so the hours a reader saves can go toward earning food or keeping a home or sitting with someone long enough to hear that first uncovered word.

## What was not checked

- No other person has rerun the programs.
- The tests for picked primes cover primes below 20 million and a handful of picking rules. A rule that was not tried could behave differently.
- The chatbot stated the theorem about long runs of primes with the same last digit and the polynomial in 26 variables from memory of the literature and did not look either one up again.
