# Questions about locks and lap lengths and the coin flip inside the critical line

> **About this page:** One AI model (Claude) wrote this page on 22 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the five earlier question pages in this folder (the last one is [prime-pieces-questions.md](prime-pieces-questions.md)). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route. A program rechecked every figure (the file coin_flip_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet. "The critical line claim" on this page means the unproven statement that every ripple of the prime count has its dial at exactly 1/2 (the earlier page [pi-ripples-questions.md](pi-ripples-questions.md) explains the dial and the ripples).

## Question: if the critical line claim is correct does that mean primes are truly random and can never be predicted which makes cryptography secure?

No on both counts.

The primes are fully predictable either way. Anyone can compute the next prime after any number with a fixed procedure. The claim says the count of primes strays from the smooth estimate by amounts about the size of a square root which is the size of the straying in a long run of coin flips. So the claim is about the size of the wobble and not about whether a prime can be known in advance.

The comparison with noise holds for the size of the wobble and fails in two ways. True white noise has every pitch at equal strength while the wobble of the primes is a chord of specific pitches with the low pitches loudest. And the primes obey rigid rules that random numbers would break: no prime above 2 is even and primes past 5 end only in 1 or 3 or 7 or 9.

One widely used kind of digital lock is built by multiplying two large primes. The lock is safe as long as nobody has a fast way to take the product and recover the two primes. That is a statement about how slow un-multiplying is. The critical line claim is a statement about how evenly primes are spread. Neither statement is known to imply the other.

The primes themselves are public. The secret is which two primes a person picked. There are roughly 10 to the power 305 primes of the size used in such locks so the secrecy sits in a private random choice among a vast supply.

A version of the claim does help people who build locks: the version guarantees that certain tests for whether a number is prime finish quickly and that primes are never too far apart so a search for a fresh large prime ends fast.

A method exists that would un-multiply large numbers quickly on a large enough quantum computer. As of the chatbot's knowledge in the middle of 2026 no publicly known machine was near the needed size. That method has nothing to do with the critical line claim.

## Question: how does the method for un-multiplying large numbers relate to the earlier pages?

The heart of the method is finding the lap length of a repeating pattern.

Take 15 and the starting number 7. Multiply by 7 over and over and keep only the remainder after dividing by 15. The remainders run 7 then 4 then 13 then 1 and then repeat. The lap length is 4. Halfway around the lap is 4. Then 4 − 1 = 3 and 4 + 1 = 5 which are the two prime pieces of 15.

- **Laps.** Sideways growth with base e returns to 1 after a pile of 2 × pi. Repeated multiplying in remainder arithmetic returns to 1 after a whole number of steps. In both cases the lap length carries the hidden information.
- **Pure tones and cancelling arrows.** For a 600 digit number the lap is far too long to walk. The quantum machine holds all the steps at once and splits the repeating pattern into pure tones. Each possible answer has an arrow. Arrows for wrong pitches cancel and arrows for the true pitch line up.
- **The slow direction of the squeeze.** In remainder arithmetic the backwards question "how many multiplications by 7 reach this remainder" has no fast known answer on an ordinary computer. Locks are built on that lopsidedness.
- **The stick.** A lock number is two giant prime pieces with no small scraps to pull off. The best methods on ordinary computers hunt for helper numbers built only from small prime pieces and such numbers are rare.
- **Doubling.** A power of one million takes about 20 squarings and not a million multiplications.
- **Shared pieces.** The last step finds the prime piece that two numbers share with a very old fast procedure.

## Question: what is a lap length?

A lap length is the number of times a starting number must be multiplied by itself (keeping only remainders) before the pattern returns to 1. A lap always exists because only finitely many remainders are possible and multiplying by a number that shares no prime piece with the divisor can be undone.

Laps for the prime 7:

- Powers of 3 leave 3 and 2 and 6 and 4 and 5 and 1 which is a lap of 6.
- Powers of 2 leave 2 and 4 and 1 which is a lap of 3.
- Powers of 6 leave 6 and 1 which is a lap of 2.

Every lap divides evenly into 6 which is 7 − 1.

**A logarithm lives inside the lap.** The powers of 3 reach every remainder from 1 to 6 so each remainder has a step number: 3 is step 1 and 2 is step 2 and 6 is step 3 and 4 is step 4 and 5 is step 5. Multiply 2 × 6 which is 12 and leaves 5. The step numbers of 2 and 6 are 2 and 3 and 2 + 3 = 5 and step 5 is the remainder 5. Step numbers turn multiplying into adding around a clock.

**Why halfway around the lap splits a number.** A number built from two primes runs two clocks at once. For 15 with the starting number 7 the clock for 3 has a lap of 1 and the clock for 5 has a lap of 4. Halfway is 7 × 7 which leaves 4. On the clock for 3 that value is 1 and on the clock for 5 that value is one short of 5. So 4 − 1 is divisible by 3 and 4 + 1 is divisible by 5. The trick works because the two clocks disagree at the halfway point.

**A second example.** For 21 the powers of 2 leave 2 and 4 and 8 and 16 and 11 and 1 which is a lap of 6. Halfway is 8. Then 8 − 1 = 7 and 8 + 1 = 9 and 9 shares the piece 3 with 21.

**When the trick fails.** For 15 with the starting number 14 the lap is 2 and halfway is 14 which is one short of 15 on both clocks. Nothing splits and a different starting number has to be tried. At least half of all starting numbers work.

**A lap that shows in decimals.** The lap of the powers of 10 for a prime is the repeat length of 1 over that prime. 1/7 is 0.142857 repeating with 6 digits. 1/11 repeats every 2 digits and 1/37 every 3 digits and 1/13 every 6 digits and 1/17 every 16 digits.

## Question: what percentage of numbers have every prime piece used only once?

About 60.79% which is 6 divided by (pi × pi).

- Up to 10 there are 7 such numbers.
- Up to 100 there are 61.
- Up to 1000 there are 608.
- Up to 10000 there are 6083.
- Up to 100000 there are 60794.
- Up to one million there are 607926.
- Up to ten million there are 6079291.

Up to 30 the numbers that qualify are 1 and 2 and 3 and 5 and 6 and 7 and 10 and 11 and 13 and 14 and 15 and 17 and 19 and 21 and 22 and 23 and 26 and 29 and 30. The numbers left out are 4 and 8 and 9 and 12 and 16 and 18 and 20 and 24 and 25 and 27 and 28 because each is divisible by 4 or 9 or 25.

The breakdown up to one million: 78498 primes and 209867 products of two different primes and 206964 products of three and 92966 products of four and 18387 products of five and 1235 products of six and 8 products of seven plus the number 1. The primes are about 13% of the group.

## Question: how does the critical line relate to all of this? (The coin flip.)

Take only the numbers with no repeated prime piece. Give each one a plus if the count of prime pieces is even and a minus if the count is odd. So 6 = 2 × 3 gets a plus and 30 = 2 × 3 × 5 gets a minus and every prime gets a minus.

- Up to 10000 there are 3030 pluses and 3053 minuses so the minuses lead by 23.
- Up to 100000 there are 30373 pluses and 30421 minuses so the minuses lead by 48.
- Up to one million there are 304069 pluses and 303857 minuses so the pluses lead by 212.
- Up to ten million there are 3040164 pluses and 3039127 minuses so the pluses lead by 1037.

For fair coin flips the lead after N flips is about the square root of N. The square root of one million is 1000 and the square root of ten million is 3162. The critical line claim is exactly equivalent to the statement that the lead never grows faster than a shade above the square root at any size. So the claim says "whether a number has an even or odd count of prime pieces behaves like a fair coin".

The reason: the pluses and minuses are the tops of the zeta family turned upside down. The upside-down family blows up exactly where the ordinary family is zero. A sum with those tops settles for every dial setting to the right of the rightmost blow-up point. So the dial position of the rightmost zero is the growth rate of the lead.

The "give or take" figure on each line of the master lists is the square root of a count because luck moves a count by about its square root. The critical line claim is that same standard applied to the number line itself. If the claim holds then the true count of primes stays within (the square root of x times the natural logarithm of x divided by 25.1) of the smooth estimate. At one million that fence is 550 and the true miss is 129. At ten million the fence is 2028 and the true miss is 338.

## Question: how do the zeros showing up on the critical line relate to the numbers with no repeated prime piece?

The zeros show up at three levels.

**Level 1: the 60.79% itself.** The share is 1 divided by the zeta family at the dial setting 2 where the sum settles at 1.645. No zeros are involved.

**Level 2: how closely the count hugs 60.79%.** Up to 10000 the prediction is 6079.3 and the true count is 6083. Up to 100000 the prediction is 60792.7 and the true count is 60794. Up to one million the prediction is 607927.1 and the true count is 607926. Up to ten million the prediction is 6079271.0 and the true count is 6079291. The misses are far below the square root. This sieve works with squares of primes so the zeros enter with their dial cut in half and a zero at dial 1/2 gives a ripple whose height is x raised to the power 1/4 (about 32 at one million). A zero at dial 0.8 would give ripples of height x raised to the power 0.4 (about 250 at one million). The best bound that has been proven from the critical line claim for this count is somewhat weaker than the power 1/4 (about the power 0.31).

**Level 3: the balance of even and odd.** The lead of pluses over minuses has one ripple per zero with no halving of the dial. A zero at dial 0.8 would let the lead swing on the scale of x raised to the power 0.8 which is about 63000 at one million and about 398000 at ten million. The observed leads are 212 and 1037.

The count of primes and the count of numbers with no repeated piece and the balance of even against odd are corrected by ripples from the one list of zeros. The observed misses fit the claim and do not prove the claim because a zero slightly off the line very high up would show only at sizes beyond any count a computer can run.

## Question: square roots are mostly irrational with chaotic digits. Does that relate to the coin flip square root?

The square root has two different jobs.

**Job 1: why a square root is irrational.** Taking a square root cuts a number's stick in half. 36 = 2 × 2 × 3 × 3 has every prime piece twice so half the stick is 2 × 3 = 6. The number 2 is a single piece of length 0.693 and half of that piece cannot be built from prime lengths. A square root is a tidy number only for perfect squares. Up to one million only 1000 numbers are perfect squares (0.1%). The numbers with no repeated prime piece are the numbers whose square root cannot be simplified at all while a number such as 12 simplifies to 2 times the square root of 3.

**Job 2: why coin flips wobble by a square root.** Independent wobbles do not add directly. Their squares add in the way the two short sides of a right triangle combine into the long side. Each flip has a wobble of 1 so N flips have a combined squared wobble of N and the wobble is the square root of N.

**Where the jobs meet.** The digits of an irrational square root look like coin flips. The first 100000 digits of the square root of 2 hold the digits 0 through 9 this many times: 9959 and 10106 and 9876 and 10058 and 10100 and 10002 and 9939 and 10008 and 10007 and 9945. The typical wobble for a fair ten-sided die over that many rolls is about 95 and the largest miss is 124. Even digits showed up 49881 times and odd digits 50119 times against a typical wobble of 158.

Nobody has proven that the digits of the square root of 2 stay balanced forever and nobody has proven the critical line claim. In both cases a fully determined object behaves like fair coin flips in every count a computer can run.

## How the questions tie back to the lists

- The "could be luck" column on the master lists applies the square root standard to each recipe. The critical line claim applies that standard to the plain number line.
- The stronger bump rule and the recipes that block small primes are sieves and the square sieve on this page shows how a sieve can leave a fixed share standing.
