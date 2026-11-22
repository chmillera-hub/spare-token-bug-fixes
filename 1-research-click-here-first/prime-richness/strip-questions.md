# Questions about strips of light and the −1/12 and what a zero means

> **About this page:** One AI model (Claude) wrote this page on 22 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the seven earlier question pages in this folder (the last one is [lamp-questions.md](lamp-questions.md) which sets up the lamps). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route and the picture of separate lamps set against a smooth strip of light. A program rechecked every figure (the file strip_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## The picture the page uses

A lamp at distance n gives a brightness of 1 divided by n raised to a fading power. With a fading power of 2 the lamps at 1 and 2 and 3 and so on total 1.6449. A strip is the smooth version: light spread evenly along the line with one lamp's worth in every unit of length. "The dial" on this page is the fading power.

## Question: how good is the shortcut "e to the power 1/n is 1 plus 1/n"?

The miss is about 1 divided by (2 × n × n).

- For n = 1000 the true value is 1.0010005 and the miss is 0.0000005.
- For n = 100 the true value is 1.0100502 and the miss is 0.00005.
- For n = 10 the true value is 1.105171 and the miss is 0.0052 (the rule gives 0.005).
- For n = 5 the true value is 1.22140 and the miss is 0.0214 (the rule gives 0.02).
- For n = 2 the true value is 1.64872 and the miss is 0.149 (the rule gives 0.125).
- For n = 1 the true value is 2.71828 and the miss is 0.718 (the rule gives 0.5).

Making n ten times larger makes the miss a hundred times smaller. As a share of the 1/n being added the miss is about 1 / (2 × n): 0.05% for n = 1000 and 5% for n = 10 and 72% for n = 1.

The exact value is 1 + 1/n + 1/(2 × n²) + 1/(6 × n³) + 1/(24 × n⁴) and so on. The shortcut keeps the first two pieces. The first dropped piece is the "growth on the growth" bonus that separates smooth growth from a chunky step.

## Question: how does "2 × n × n" relate to "2 × pi × pi"?

The two meet at the 1/12.

- The bottoms 2 and 6 from the string above build the 1/12: turning "e to a power minus 1" upside down and collecting pieces gives (1/2 × 1/2) − 1/6 = 1/4 − 1/6 = 1/12.
- The hidden lap points of sideways growth give the same 1/12 as a sum of shares. The share from lap k is 1 divided by (2 × (pi × k) × (pi × k)): 0.0507 from lap 1 and 0.0127 from lap 2 and 0.0056 from lap 3. Adding every lap gives 1.645 divided by (2 × pi × pi) = 1/12.

Each lap share has the shape of the miss rule with pi × k in place of n. The match of the 1/12 by both routes is exact and proven. The chatbot knows of no deeper reason that makes the two shapes one mechanism: the 2 in the miss rule is the bottom 1 × 2 and the 2 in the lap share arises from each lap point having a mirror twin.

## Question: how does the 1/12 relate to 1 + 2 + 3 + 4 + … ?

- The sum 1 + 1/4 + 1/9 + … settles at 1.645 = pi × pi / 6.
- Dividing 1.645 by 2 × pi × pi = 19.739 gives 1/12.
- With a minus sign that is −1/12 which is the leftover constant under 1 + 2 + 3 + 4 + …

The sum 1 + 2 + 3 + … is the dial at −1 and the sum 1 + 1/4 + 1/9 + … is the dial at 2. The mirror rule pairs a dial setting s with 1 − s so those two sums are partners.

The sum 1 + 2 + 3 + … grows without limit in the ordinary sense. The −1/12 is the constant left over once the growing part is removed. The same 0.08333 arrives by three routes: the mirror rule (1.645 / 19.739) and the faded sum (99.9167 against a smooth part of 100) and the bottoms of the string for e (1/4 − 1/6).

## Question: what is the −1/12 in terms of the lamps?

The −1/12 is not the brightness of any row of lamps. A row for 1 + 2 + 3 + … would have lamps that get brighter with distance so the row has no total and a brightness cannot be negative.

The −1/12 is a correction number. Every sum taken in whole-number steps differs a little from the same quantity poured smoothly. The first two correction numbers are 1/2 and 1/12 and those are the leftover constants under 1 + 1 + 1 + … and 1 + 2 + 3 + … with minus signs.

The correction at work on real lamps: take the lamps (fading power 2) from distance 10 outward.

- A strip from 10 outward gives 1/10 = 0.1.
- Half of the first lamp adds 1/200 = 0.005.
- The 1/12 correction adds 0.000167.
- The three add to 0.105167 and the true total of the separate lamps is 0.105166.

One more tie: gather the whole lamp row into the single lamp at 0.780 units that matches the row. Push that lamp 4.44 times further (4.44 is pi times the square root of 2) to 3.46 units (the square root of 12). The lamp there has a brightness of exactly 1/12.

## Question: how do separate lamps compare with a strip of light and what about odd lamps only?

A strip from some distance outward gives 1 divided by the starting distance. A strip from 1 gives 1. A strip from one half gives 2. A strip that reaches your spot gives light without limit.

**Every whole number.** Let each lamp stand for the piece of strip half a unit to each side.

- The piece from 0.5 to 1.5 gives 1.333 and the lamp at 1 gives 1.
- The piece from 1.5 to 2.5 gives 0.267 and the lamp at 2 gives 0.25.
- The piece from 2.5 to 3.5 gives 0.114 and the lamp at 3 gives 0.111.
- The piece from 9.5 to 10.5 gives 0.010025 and the lamp at 10 gives 0.01.

The strip from 0.5 outward gives 2 and the lamps give 1.645. The strip wins because the near half of each piece gains more than the far half loses.

**Odd lamps only.** The odd lamps sit 2 apart so each lamp stands for a piece of strip 2 units long at half strength.

- The piece from 2 to 4 gives 0.125 and the lamp at 3 gives 0.111.
- The piece from 4 to 6 gives 0.0417 and the lamp at 5 gives 0.04.
- The pieces from 2 outward total 0.25 and the odd lamps from 3 outward total 0.2337.

The piece for the lamp at 1 would run from 0 to 2 and reach your spot. So the odd row has a finite total only because the lamp at 1 is a bulb at a fixed distance.

**The correction scales with the spacing.** For lamps 2 apart the second correction number doubles to 2/12. The odd lamps from 11 outward: the half-strength strip gives 1/22 = 0.04545 and half the first lamp adds 0.00413 and the spacing correction adds 0.00025. The three add to 0.04984 and the true total is 0.04984.

## Question: are 0.6449 and the gap constant 0.5772 related?

Both are the same kind of leftover: separate lamps minus the strip from 1 outward.

- With a fading power of 2 the lamps total 1.6449 and the strip totals 1. The leftover is 0.6449.
- With a fading power of 1 the lamps total 1 + 1/2 + 1/3 + … and the strip totals the natural logarithm. Both grow without limit and the difference settles at 0.5772.

The leftover along the dial:

- At 2 the leftover is 0.6449.
- At 1.5 the leftover is 0.6124.
- At 1.1 the leftover is 0.5844.
- At 1.01 the leftover is 0.5779.
- At 1.001 the leftover is 0.5773.
- At 1 the leftover is 0.5772.
- At 1/2 the leftover is 0.5396.
- At 0 the leftover is 0.5.

So 0.6449 slides smoothly into 0.5772 and on down. The difference 0.6449 − 0.5772 = 0.0677 is the drift between the dial settings 2 and 1 and has no tidy formula that the chatbot knows of.

The corner pieces (each lamp against the piece of strip from that lamp to the next): for a fading power of 1 the pieces are 0.3069 and 0.0945 and 0.0457 and 0.0269 and so on. For a fading power of 2 the pieces are 0.5 and 0.0833 and 0.0278 and 0.0125 and so on.

At a fading power of 2 both totals are finite so the leftover is a plain subtraction with a neat formula (pi × pi / 6 minus 1). At a fading power of 1 both totals are infinite and only the difference is finite.

## Question: how are the lamp totals computed at fading powers such as 1.01 and 1.001?

Adding one by one is hopeless. At a fading power of 1.01 the first thousand lamps total 7.25 and the first million total 13.48 while the true total is 100.578.

The method: add the first few lamps directly and swap the rest for a strip plus the two corrections.

For 1.01:

- The lamps at 1 through 9 give 2.80454.
- The strip from 10 outward gives 97.72372.
- Half of the lamp at 10 gives 0.04886.
- The 1/12 correction gives 0.00082.

The total is 100.577944 and the true value is 100.577943.

For 1.001 the same four pieces are 2.82651 and 997.70006 and 0.04989 and 0.00083. The total is 1000.577289 and the true value is 1000.577288.

The strip from 1 outward gives exactly 100 at 1.01 and exactly 1000 at 1.001 so the leftovers are 0.5779 and 0.5773.

## Question: how does this relate to the zeros on the critical line?

Between the dial settings 0 and 1 the lamp total and the strip total are both infinite. The difference settles and that difference is what "the zeta function at that setting" means. At the dial setting 1/2 with the lamps at 1 through 29 and the strip method:

- The lamps give 9.4026.
- The strip part gives −10.9545.
- Half of the lamp at 30 gives 0.0913.
- The 1/12 correction gives 0.0003.

The total is −1.46035.

With a sideways amount switched on each lamp becomes an arrow of length 1 over the square root of its distance turned by an angle that depends on the sideways amount and the logarithm of the distance. The strip becomes an arrow too.

At the first zero (sideways amount 14.1347) the lamps at 1 through 29 give an arrow pointing 0.264 left and 0.284 down. The strip and the corrections give an arrow pointing 0.264 right and 0.284 up. The two cancel to within 0.00003. At the second zero (21.0220) the arrows cancel to within 0.00009. At a sideways amount of 10 the leftover has length 1.549 and at 18 the leftover has length 2.337.

So a zero is a setting where the separate lamps and the smooth strip agree exactly. The critical line claim says that exact agreement can happen only when the fading power is 1/2.

## Question: is the claim that infinite primes mean infinite zeros on the critical line?

No. Infinitely many zeros on the dial setting 1/2 is proven and more than 40% of all zeros are proven to sit there. The claim is that every zero sits there.

The link between endless primes and endless zeros is real. The lamp total equals a product with one factor per prime. A finite product of such factors is never zero so zeros exist only because the primes go on forever.

There are 29 zeros with a pitch below 100 and 649 below 1000 and 1747146 below one million. The zeros get more crowded as the pitch rises while the primes get sparser as the numbers rise.

## Question: is the sideways part there to make up for using square roots?

No. The two settings have separate jobs. The dial sets the arrow lengths and the sideways amount sets the arrow directions.

With no sideways part every arrow points the same way. Between the dial settings 0 and 1 with no sideways part the leftover is always below zero (−0.5 at 0 and −1.46 at 1/2).

Turning alone is not enough. At a dial of 1 the total is never zero for any sideways amount (a proven fact that is the same as the rule "1 divided by the natural logarithm"). At a dial of 2 the lamp at 1 has length 1 and all the other lamps together total 0.645 so the others can never cancel the first.

A full cancellation needs the far lamps to matter as much as the near lamps. A dial of 1/2 is the balance point that the mirror rule leaves in place.

With no sideways part the leftover is exactly zero at the dial settings −2 and −4 and −6. Those zeros belong to the mirror rule and play no part in the prime ripples.

## Question: 1 + 1/2 + 1/3 + … grows like the natural logarithm. What is the matching growth at the dial setting 1/2?

Twice the square root of x.

- Up to 100 the sum of 1 over each square root is 18.59 and 2 × √100 is 20 (a difference of −1.41).
- Up to 10000 the sum is 198.54 and 2 × √10000 is 200 (a difference of −1.455).

The difference heads to −1.4604.

The strip from 1 to x for a fading power s is (x raised to the power h minus 1) divided by h where h is 1 − s. At x = 100 that is 18 for h = 1/2 and 5.85 for h = 0.1 and 4.71 for h = 0.01 and 4.606 for h = 0.0001. The natural logarithm of 100 is 4.605. So the logarithm is what power growth turns into when the power shrinks to zero.

## Question: why would zeros show up at the dial setting 1/2 and almost nowhere else?

Nobody has proven why. That unanswered "why" is the hypothesis.

- **Dial above 1.** The lamp total equals the product over the primes. No factor is zero and the product settles so the total is never zero. Proven.
- **Dial below 0.** The mirror rule carries that fact over. The mirror rule contains a wave that crosses zero at −2 and −4 and −6 and those are the only zeros there. Proven.
- **The edges at 0 and 1.** No zeros. Proven.
- **Between 0 and 1.** The mirror rule pairs every zero at 1/2 plus an offset with a twin at 1/2 minus the offset.

A zero normally needs two things at once: the left-right part of the leftover arrow is zero and the up-down part is zero. On the dial setting 1/2 the mirror rule locks the leftover onto one direction once a known turn is undone. The leftover then acts like one ordinary number that swings positive and negative:

- −1.549 at a sideways amount of 10.
- 0 at 14.13.
- +2.337 at 18.
- 0 at 21.02.
- −1.455 at 23.
- 0 at 25.01.
- +2.809 at 28.
- 0 at 30.42.
- −0.926 at 31.7.

A number that changes sign has to pass through zero. Off the line nothing forces the two parts to vanish together. Near the first zero with the dial moved to 0.7 the leftover never gets smaller than 0.146. A zero off the line is not ruled out by this.

## Question: what does a zero mean? Are the lamps moving?

The lamps never move. Brightness can only add up so swap the lamps for speakers that all hum one pitch.

- The dial sets the volume. At a dial of 1/2 the speaker at distance n has a volume of 1 over the square root of n.
- The sideways amount is the pitch. Each hum reaches you with a delay equal to the logarithm of the speaker's distance.

At most pitches something is left over (1.55 at a pitch of 10 and 2.34 at 18). At a pitch of 14.13 the pushes and pulls from the whole row cancel and the result is silence. Silence happens again at 21.02 and 25.01 and 30.42. Each silent pitch is a zero.

At a pitch of 14.13 the first arrows are:

- The speaker at 1 gives an arrow of length 1 pointing right.
- The speaker at 2 gives an arrow of length 0.707 pointing left and a little up.
- The speaker at 3 gives an arrow of length 0.577 pointing left and a little down.
- The speaker at 4 gives an arrow of length 0.5 pointing right and down.

Laid tip to tail the arrows wander near the starting point and with the far part of the row handled as a strip the path closes up on the start.

The row of speakers at the whole numbers is a product over the primes. The prime count is governed by that row turned upside down. Where the row goes silent the upside-down version blows up the way a wine glass rings at its natural pitch. So each silent pitch of the whole numbers is a ringing pitch of the primes.

## How the questions tie back to the lists

- The baseline on the master lists (1 divided by the natural logarithm) is the proven fact that no zero sits at the dial setting 1.
- The "give or take" figure on each line is square root sized which is the size of every prime ripple if every zero sits at the dial setting 1/2.
- The strip-plus-corrections method is the same idea as the "chance" figure on each line: a smooth estimate standing in for a jagged count.
