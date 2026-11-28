# Questions about the sum over prime squares and the square root level and the critical line

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The author proposed moving one level down from the squares of the primes to the square roots of the primes and asked how that level relates to the critical line. The page continues the seventeen earlier question pages in this folder (the last one is [cycle-questions.md](cycle-questions.md)). The numbers are measurements from the program square_root_level.py in the folder boring-things/research-program-files/prime-richness-scripts/cycle-scripts. The mathematics is standard and the page claims no new result. The pairing of the square as looking forward and the square root as looking backward is the chatbot's framing of the author's idea. No other person has reviewed the page yet.

## What is the sum of one over the square of each prime?

The sum 1/4 + 1/9 + 1/25 + 1/49 and so on through every prime settles at about 0.4522474200.

- The first 10 primes give 0.4450106.
- The first 100 primes give 0.4519928.
- The first 10000 primes give 0.4522467.
- All 664579 primes below ten million give 0.4522474142.
- A formula built from the zeta function at 2 and 4 and 6 and so on gives 0.452247420041065498.

No simple closed form is known. The matching sum over every whole number equals pi squared divided by 6.

The prime 2 contributes 55.3% of the sum and 3 contributes 24.6% and 5 contributes 8.8% and 7 contributes 4.5%. So the first four primes carry about 93% of the total.

A caution: the share of numbers divisible by some prime square is 39.2% and not 45.2%. The plain sum counts a number such as 36 twice because 36 is divisible by both 4 and 9.

## What does the square root of a prime mean in the crossing off picture?

The square looks forward and the square root looks backward. The square of 7 is 49 which is the first number that 7 gets to cross off. The square root of a number tells which primes got a say in whether the number survived. The square root of 97 is about 9.85 so the primes with a say are 2 and 3 and 5 and 7 because 4 and 9 and 25 and 49 sit below 97. The prime 11 had no say because 11 does not start crossing off until 121.

The square root is also the halfway point. A prime is the prime to the power 1 and the number 1 is the prime to the power 0. The square root is the prime to the power one half and the square root times the square root gives the prime back.

## How do the three levels behave as sums?

- **Power 2.** The sum of one over the square of each prime settles at 0.4522.
- **Power 1.** The sum of one over each prime grows without limit and very slowly: 2.198 for primes up to one thousand and 2.705 up to one hundred thousand and 3.041 up to ten million. Power 1 is the edge between settling and not settling.
- **Power one half.** The sum of one over the square root of each prime grows fast: 12.7 for primes up to one thousand and 70.1 up to one hundred thousand and 461.6 up to ten million.

So at the square root level the primes are too loud to add up. The plain recipe that builds the zeta function out of primes stops working there.

## How does the square root level relate to the critical line?

On the critical line at one half each prime enters with a size of one over the square root of the prime and with an angle. The angle is the height on the line times the natural logarithm of the prime. As the height changes each prime turns at a different speed.

The sizes alone add to infinity. So the total can vanish only when the directions cancel and a zero of the zeta function is a height where the cancellation is complete.

A simple test with the primes below 100000: add one over the square root of each prime times the cosine of the angle and scan the heights from 10 to 40.

- The sum averaged 0.04 over those heights.
- The lowest value was −5.27 at a height of 14.05 which is beside the first zero at 14.13.
- At the first four zeros the sum read −4.62 and −3.14 and −3.41 and −3.46.

So the primes line up against themselves most strongly near the zeros.

## Why one half and not another power?

Two known facts point at one half and both are forms of balance.

- The zeta function has a mirror rule that trades the power s for the power 1 minus s. One half is the one power that the mirror leaves in place.
- Each zero sends a wave through the count of primes. The loudness of the wave from a zero at one half is the square root of how far the count has gone. With every zero on the line every wave has that same loudness. A zero off the line would make one wave louder than the others and its mirror partner quieter.

The belief that every zero sits on the line is unproven. One way to say the belief is that the count of primes strays from the smooth prediction by about a square root and no more. Nothing on this page is evidence for or against the belief.

## How much must the number of steps grow for each extra step of drift?

A walk of fair coin flips typically drifts about the square root of its length. So 3600 steps go with a typical drift of 60.

- A drift of 61 goes with 3721 steps which is 121 more.
- A drift of 62 goes with 3844 steps which is 123 more.
- A drift of 63 goes with 3969 steps which is 125 more.

The added amount is two times the current drift plus one. In relative terms the steps grow about twice as fast as the drift: a drift that rises 1.67% from 60 to 61 needs 3.36% more steps. Doubling the drift takes four times the steps.

This lopsided cost is why square root wandering is tame. A drift of 60 is 1.67% of a walk of 3600 steps and a drift of 600 is 0.17% of a walk of 360000 steps. The hexagon door walk on the page [order-test-findings.md](../prime-mazes/order-test-findings.md) and its neighbors showed the same scale for whole primes: 24 steps sideways after 3600 primes. The number 60 is a typical size and not a guaranteed value.

## How does this connect to food and shelter and deep human connection?

These sums do not cook a meal or pay rent. The tie is that a question asked out loud in plain words led to a clear picture of a famous unsolved problem and the picture sits in public for free. A reader who wants the same picture can save the hours of searching and put those hours toward earning food or keeping a home or toward a long talk with another person about what each one carries inside.

## What was not checked

- No other person has rerun the program.
- The scan near the zeros used a simple sum with a sharp cutoff at 100000. With a cutoff at ten million the same sum swings widely so the scan shows a tendency and is not a method for finding zeros.
- The chatbot stated the mirror rule and the link between zeros and waves from memory of the standard literature.
