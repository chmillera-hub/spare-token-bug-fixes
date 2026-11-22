# Questions about why the zeros sit on the dial setting 1/2

> **About this page:** One AI model (Claude) wrote this page on 22 November 2026 after the author of this repository asked why the zeros would sit on the dial setting 1/2 and almost nowhere else between 0 and 1. The page continues the eight earlier question pages in this folder (the last one is [strip-questions.md](strip-questions.md) which sets up the speakers and the zeros) and reuses the lamp and speaker pictures from those pages. Where the page says Part 2 the page means [ladder-questions.md](ladder-questions.md) and Part 4 means [pi-ripples-questions.md](pi-ripples-questions.md) and Part 6 means [coin-flip-questions.md](coin-flip-questions.md) and Part 7 means [lamp-questions.md](lamp-questions.md) and Part 8 means [strip-questions.md](strip-questions.md). The ideas on this page are known to people who study the zeta function so the page claims no new result and the page does not move the proof of the critical line claim forward. The tables were computed fresh for this page and a program rechecked every figure (the files in the folder boring-things/research-program-files/prime-richness-scripts/half-dial-scripts). No other person has reviewed the page yet.

## The picture the page uses

A row of speakers sits at the distances 1 and 2 and 3 and so on. The dial sets the volume so the speaker at distance n has a volume of 1 divided by n raised to the dial. The pitch is the sideways amount so the arrow for the speaker at distance n is turned by the pitch times the natural logarithm of n.

The leftover is the one arrow that remains after every speaker arrow is added and the smooth strip is taken away. The leftover is the value of the zeta function at that dial and pitch. A zero is a dial and a pitch where the leftover has a length of 0.

The mirror rule is the proven rule that ties the leftover at a dial setting s to the leftover at the dial setting 1 − s.

The page measures the leftover by the natural logarithm of its length. A leftover of length 1 has a logarithm of 0. A leftover of length 0.3679 has a logarithm of −1. A leftover of length 0 has no logarithm because no count of copies of e multiplies out to 0. So a zero is a spot where the logarithm of the leftover's length drops without limit.

## The short version

- Zeros have to exist and the number of zeros is fixed because the primes hold the average logarithm of the leftover flat on the right side of the strip while the mirror rule tilts the average on the left side. A flat floor joins a ramp through a bend and each bend is made of zeros.
- The bend sits at 1/2 because 1/2 is the dial setting where the wobble of the prime factors stops having a ceiling. Independent wobbles add by squares and squaring the prime volumes doubles the dial so the border at the dial setting 1 lands on 1/2.
- Zeros sit on 1/2 with ease because the mirror image of every speaker is exactly as loud as the speaker there. A zero leaves 1/2 as one of a pair after two neighbouring zeros run into each other.
- The mirror rule alone is not enough. One row tested below obeys a mirror rule and is not a product over the primes and that row has zeros off the line.
- What is proven says zeros off the line are rare. What is not proven is that zeros off the line number exactly none.

## Question: do zeros have to exist at all and is the number of zeros fixed?

Yes to both. Two facts fix the number of zeros before anyone finds a single zero because one fact keeps the right side of the strip flat and the other fact tilts the left side.

A program averaged the logarithm of the leftover's length along one dial setting at a time over every pitch from 100 to 3100.

- At the dial setting 2 the average is −0.00003.
- At 1 the average is −0.00002.
- At 0.75 the average is −0.00001.
- At 0.6 the average is −0.000004.
- At 0.55 the average is +0.000002.
- At 0.5 the average is +0.00009.
- At 0.4 the average is 0.5316.
- At 0.25 the average is 1.3289.
- At 0 the average is 2.6578.

The right side is flat at 0. To the right of the dial setting 1 the reason is the product over the primes: the row equals a product with one factor for each prime and each factor averages to exactly 0 on the logarithm scale. The factor for the prime 2 at the dial setting 0.75 swings between a length of 0.627 and a length of 2.467 as the pitch turns and the average logarithm of that factor over one full turn is 0. Between the dial settings 1/2 and 1 the product no longer settles and the average still heads to 0 as the stretch of pitch grows which is a proven result.

The left side is a straight ramp. The reason is the mirror rule: the leftover at a dial setting left of 1/2 equals the leftover at the mirror dial setting times a stretch factor and the length of the stretch factor is (pitch divided by 2 × pi) raised to the power (1/2 minus the dial). The average natural logarithm of (pitch divided by 2 × pi) from 100 to 3100 is 5.3157. So the ramp climbs 5.3157 for each full unit of dial: 0.1 × 5.3157 = 0.5316 and 0.25 × 5.3157 = 1.3289 and 0.5 × 5.3157 = 2.6579 (against the measured 2.6578).

So the graph of the average is a flat floor on the right and a ramp on the left and the floor meets the ramp in a corner at the dial setting 1/2.

A proven counting rule ties every bend in that graph to zeros: across a band of dial settings the slope of the average changes by 2 × pi times the number of zeros inside the band for each unit of pitch. A band of dial settings that holds no zeros leaves the graph straight. The slope changes by 5.3157 at the corner so the rule gives 5.3157 divided by (2 × pi) = 0.846 zeros for each unit of pitch. The true number of zeros with a pitch between 100 and 3100 is 2538 which is 0.846 for each unit of pitch.

So zeros have to exist because a ramp cannot turn into a flat floor without a bend and a bend is made of zeros. The size of the bend fixes how many zeros there are. The place of the bend fixes where the zeros are and the measured bend sits at 1/2.

## Question: why would the corner sit at exactly 1/2? (The half of the answer that the primes supply.)

The dial setting 1/2 is where the wobble of the prime factors stops having a ceiling.

Each prime factor wobbles on the logarithm scale as the pitch turns. For the prime p the average squared wobble is close to half of 1 divided by p raised to the power (2 × the dial). Independent wobbles add by squares which is the coin flip rule from Part 6. The primes turn independently because the arrow for the prime p turns at a rate equal to the stick length of p (0.693 for the prime 2 and 1.099 for the prime 3) and no pile of one stick length equals a pile of another stick length (Part 2).

So the pile of squared wobble for the whole row should be half the brightness of a lamp at every prime (Part 7) with the fading power set to twice the dial plus a small extra from the powers of primes. The measured piles below used every pitch from 100 to 3100.

- Dial 2: the prime lamps total 0.0770. The predicted pile is 0.0390 and the measured pile is 0.0390.
- Dial 1.5: the prime lamps total 0.1748. Predicted 0.0896 and measured 0.0896.
- Dial 1: the prime lamps total 0.4522. Predicted 0.2368 and measured 0.2369.
- Dial 0.9: the prime lamps total 0.5683. Predicted 0.2992 and measured 0.2991.
- Dial 0.8: the prime lamps total 0.7348. Predicted 0.3887 and measured 0.3881.
- Dial 0.75: the prime lamps total 0.8496. Predicted 0.4502 and measured 0.4488.
- Dial 0.7: the prime lamps total 0.9990. Predicted 0.5301 and measured 0.5265.
- Dial 0.6: the prime lamps total 1.5198. Predicted 0.8052 and measured 0.7775.
- Dial 0.55: the prime lamps total 2.1088. Predicted 1.1103 and measured 1.0100.
- Dial 0.5: the prime lamps are the sum of 1 over each prime which grows without limit. No finite pile exists and the measured pile is 1.548.

The prime lamp total at the dial setting 1 is the 0.4522 from Part 7. The measured pile falls a little short at 0.6 and at 0.55 and a likely reason is that prime lamps with a fading power near 1 settle slowly so the primes far beyond the pitch range had not yet added a full share.

The fading power is twice the dial because squaring a volume doubles the power. The prime lamps settle on a finite total for every fading power above 1. At a fading power of exactly 1 the prime lamps are the sum 1/2 + 1/3 + 1/5 + … which is the third rung of the ladder in Part 2 and grows like the logarithm of the logarithm. A fading power of 1 is a dial setting of 1/2.

What the ceiling means for zeros. A product of independent factors with a finite pile of squared wobble settles on a finite logarithm (a proven fact about independent chances) and a finite logarithm means a leftover that is not 0. So at a dial setting right of 1/2 a zero needs the turning angles of the primes to line up in a way that independent angles almost never do. On the dial setting 1/2 the pile has no ceiling so the logarithm of the leftover's length can swing down without limit and a zero is a spot where the logarithm has dropped the whole way.

The pile on 1/2 keeps growing with the pitch while the piles right of 1/2 stay put.

- Pitches 100 to 3100: the pile is 1.548 on the dial setting 1/2 and 0.4488 on 0.75 and 0.2369 on 1.
- A stretch of 15000 starting at one million: 1.945 on 1/2 and 0.4501 on 0.75 and 0.2368 on 1.
- A stretch of 10000 starting at one billion: 2.172 on 1/2 and 0.4501 on 0.75 and 0.2368 on 1.
- A stretch of 1500 starting at one trillion: 2.358 on 1/2 and 0.4506 on 0.75 and 0.2371 on 1.

On 1/2 the pile gained 0.398 and then 0.227 and then 0.186. Half of the gain in the logarithm of the logarithm of (pitch divided by 2 × pi) over the same three steps is 0.406 and 0.227 and 0.156. The stretch at one trillion is the shortest so the last measured figure carries the most sampling noise.

Two separate facts point at 1/2. The mirror rule pairs the dial setting s with 1 − s and the midpoint of that pairing is 1/2. The squares rule doubles the dial and the prime lamps stop settling at a fading power of 1 which is a dial setting of 1/2. Both facts trace back to one border: the dial setting 1 is where the plain sum 1 + 1/2 + 1/3 + … passes from settling to growing without limit.

## Question: what does the dial setting 1/2 have that lets zeros sit there? (The half of the answer that the mirror rule supplies.)

On the dial setting 1/2 the stretch factor in the mirror rule has a length of exactly 1 at every pitch. So a speaker and the mirror image of that speaker are equally loud on 1/2 and two equally loud arrows cancel whenever the turn between the two arrows is half a lap.

Keep one speaker (the speaker at distance 1) and the mirror image of that speaker. On the dial setting 1/2 the pair cancels at these pitches: 14.52 and 20.65 and 25.49 and 29.74 and 33.62 and 37.26 and 40.70 and 43.99. The true zeros are 14.13 and 21.02 and 25.01 and 30.42 and 32.94 and 37.59 and 40.92 and 43.33. So one speaker and one mirror image already lay down a row of zeros on 1/2 with the right spacing and the right count because the pitches where the pair cancels are the pitches where the count formula from Part 4 reads a whole number plus one half (0.5 at 14.52 and 1.5 at 20.65 and 2.5 at 25.49).

Move the dial to 0.7 and the mirror image is quieter than the speaker: 0.846 times as loud at the pitch 14.52 and 0.575 times as loud at 100 and 0.363 times as loud at 1000. Two arrows of different lengths cannot cancel at any turn. The length of the stretch factor is 1 on the dial setting 1/2 and shrinks steadily to the right and grows steadily to the left (a program confirmed the steady change for pitches from 7 to 60 and the power formula in the first question covers higher pitches). So the model with one speaker and one mirror image has every zero above a pitch of 7 on the dial setting 1/2.

The primes then shift each of those baseline pitches. The other speakers add a turn to the row and the turn can be written with the primes because the row is a product over the primes. The typical miss below is found by squaring the misses against the first twelve true zeros and averaging and taking the square root.

- No primes: 14.52 and 20.65 and 25.49 and 29.74 and 33.62. The typical miss is 0.51.
- The prime 2: 14.14 and 21.29 and 24.69 and 30.27 and 33.14. The typical miss is 0.28.
- The primes up to 3: the typical miss is 0.16.
- The primes up to 7: the typical miss is 0.08.
- The primes up to 13: 14.10 and 21.02 and 25.02 and 30.38 and 32.99. The typical miss is 0.05.
- The primes up to 31: 14.07 and 21.03 and 25.01 and 30.45 and 32.92. The typical miss is 0.04.

The gaps between neighbouring zeros in that stretch average 3.85 so the primes move each baseline pitch by a small share of one gap.

A limit of the shift table: the shifting step keeps every pitch on the dial setting 1/2 by the way the step is built. So the shift table shows where along the line the primes put each zero and the shift table cannot show that zeros stay on the line.

## Question: how could a zero leave the dial setting 1/2?

Two at a time. On the dial setting 1/2 the leftover acts like one signed number once a known turn is undone (Part 8). A curve that passes from below 0 to above 0 still has to cross 0 after a small nudge so a single crossing cannot vanish. Under the mirror rule every zero off the line has a twin at the mirror dial setting. So a zero cannot slide off the line alone: two neighbouring zeros on the line first have to run into each other and then the two leave together as a twin pair. Seen from the line a departure looks like a hump of the signed leftover that turns around before reaching 0.

A close call sits near the pitch 7005. Zeros sit at 7005.0629 and at 7005.1006. The gap is 0.0377 where the average gap at that height is 0.8955 so the two zeros are 4.2% of an average gap apart. Between the two zeros the signed leftover rises to +0.00397. The 23 humps between the pitches 6995 and 7015 have a middle size of 1.60 and the two humps beside the small hump reach −1.45 and −7.64. A hump that stopped 0.004 lower would have left the two zeros off the line as a twin pair.

Part 4 measured that neighbouring zeros keep apart (no gap among the first 200 was below a quarter of the average gap). Zeros that keep apart seldom run into each other and zeros that do not run into each other cannot leave the line. Nobody has proven that the keeping apart holds at every height.

Proven results say the claim has no room to spare. Mathematicians studied a family of smoothed copies of the zeta row with one smoothing knob. Every zero of a smoothed copy sits on the line exactly when the knob is at or above one threshold. The critical line claim is the same statement as "the threshold is 0 or below". The threshold is proven to be 0 or above (published in 2020) and proven to be 0.22 or below (published in 2019). So any amount of roughening in place of smoothing is proven to push some zeros off the line.

## Question: is the mirror rule enough by itself to keep zeros on 1/2?

No. A program tested three rows that each obey a mirror rule with the midpoint 1/2.

- The quarter turn row. The speakers get a repeating pattern of five weights: 1 and a quarter turn forward and a quarter turn back and −1 and 0. So the speaker at distance 1 has the weight 1 and the speaker at 2 is given a quarter turn forward and the speaker at 3 a quarter turn back and the speaker at 4 has the weight −1 and the speaker at 5 is switched off and then the pattern repeats. The weights multiply the way whole numbers do: the weight at 2 times the weight at 3 equals the weight at 6. So the quarter turn row is a product with one factor for each prime.
- The swapped quarter turn row. The pattern is the same with the two quarter turns trading places. The swapped quarter turn row is a product over the primes too.
- The blended row. The blended row adds the two rows above in equal shares (each share has a length of 0.52 and the two shares are turned 15.9 degrees in opposite directions). The blend works out to the plain weights 1 and 0.2841 and −0.2841 and −1 and 0. The blended weights do not multiply: the weight at 2 times the weight at 3 is −0.0807 while the weight at 6 is 1. So the blended row is not a product over the primes.

The blended row obeys the mirror rule for a pattern of five to 27 digits at four test settings.

The zeros with a pitch below 200:

- The quarter turn row has 130 zeros and all 130 sit on the dial setting 1/2.
- The swapped quarter turn row has 129 zeros and all 129 sit on 1/2.
- The blended row has 130 zeros. 122 sit on 1/2 and 4 sit to the right and 4 sit to the left as mirror twins.

The count formula for a pattern of five gives 129.5.

The four zeros of the blended row to the right of 1/2:

- Dial 0.8085 at the pitch 85.699.
- Dial 0.6508 at the pitch 114.163.
- Dial 0.5744 at the pitch 166.479.
- Dial 0.7243 at the pitch 176.702.

On the line the signed leftover of the blended row turns around early at each of those pitches: at −0.357 near 85.70 and at −0.096 near 114.16 and at +0.029 near 166.48 and at +0.228 near 176.71. The gap between the zeros on the line across each of those pitches is about three average gaps (4.54 near 85.70 where the average gap is 1.49) which is the room that two missing zeros leave.

The flat floor test from the first question catches the blended row. The counting rule predicts how far each zero to the right lifts the average logarithm.

- Dial 0.9: the blended row averages +0.0002 and the counting rule predicts 0.
- Dial 0.75: the blended row averages 0.0020 and the counting rule predicts 0.0018.
- Dial 0.65: 0.0074 against a predicted 0.0073.
- Dial 0.6: 0.0121 against a predicted 0.0121.
- Dial 0.55: 0.0174 against a predicted 0.0175.
- Dial 0.51: 0.0223 against a predicted 0.0226.

The quarter turn row and the swapped quarter turn row stayed between −0.0010 and +0.0016 at every one of those dial settings.

So the mirror rule supplies the midpoint and the twin pairing and the product over the primes supplies the reason zeros stay on the midpoint. Blending two prime products broke the product and four twin pairs left the line below a pitch of 200.

## Question: how close does the leftover of the zeta row get to 0 along other dial settings?

The smallest length of the leftover for every pitch from 100 to 3100:

- Dial 2: 0.674.
- Dial 1.5: 0.518.
- Dial 1: 0.295.
- Dial 0.9: 0.241.
- Dial 0.8: 0.181.
- Dial 0.75: 0.145.
- Dial 0.7: 0.109.
- Dial 0.6: 0.049.
- Dial 0.55: 0.027.
- Dial 0.5: exactly 0 at 2538 pitches.

The deepest dip along each dial setting from 0.55 to 0.8 sits near the pitch 1329.13. That pitch lies between two zeros on the line at 1329.04 and 1329.21 which are 0.16 apart where the average gap is 1.17. So in that range the nearest thing to a zero off the line is the shadow of a close pair of zeros on the line.

The dips deepen slowly with height. Along the dial setting 0.75 the smallest length on a sampling grid was about 0.12 in the stretch at one million and about 0.11 in the stretch at one billion and about 0.16 in the shorter stretch at one trillion. Along the dial setting 1 the smallest lengths were about 0.27 and 0.27 and 0.30.

## Question: what is proven and what is not?

Proven:

- No zero has a dial setting of 1 or more and no zero of the prime ripple kind has a dial setting of 0 or less.
- The average logarithm of the leftover heads to 0 along every dial setting right of 1/2. By the counting rule a flat average means that for any small distance the share of zeros farther than that distance from 1/2 shrinks toward 0% as the pitch grows.
- Infinitely many zeros sit on 1/2. A result published in 2020 put the share of zeros on the line a little above five twelfths which is about 41.7%.
- A paper posted in August 2026 reports a proof that at least two thirds of the zeros sit on the line and are single crossings. The paper states that an AI model found and wrote the argument and that two mathematicians checked the argument and that a proof checking program verified the argument. A search on 22 November 2026 found no journal review of the paper yet so the two thirds figure is newer and less settled than the 41.7% figure.
- Researchers using computers have checked the first 12.36 trillion zeros (every zero with a pitch below about 3 trillion) and each one sits on 1/2.

Not proven: that every zero sits on 1/2.

The gap between the two lists in one sentence: the turning angles of the primes behave like independent angles over any long stretch of pitch and a zero off the line would be one exceptional pitch where the angles line up so "rare" is proven and "none at all" is not.

## Question: did this page make progress on the critical line claim?

No. The page proves nothing new and the page rules out no zero that was not already ruled out.

What the tables do show is each piece of the "why" as a number a reader can recheck: the flat floor and the ramp and the corner at 1/2 and the prime wobble that matches the prime lamps down to the dial setting 0.7 and the baseline zeros from one speaker and one mirror image and the blended row that loses zeros off the line once the product over the primes is broken.

A proof would have to turn "the prime angles almost never line up right of 1/2" into "the prime angles line up right of 1/2 at no pitch at all" and the page has no method for that step.

## Question: how does this page help with food and shelter and deep human connection?

Food and shelter: the page does not put a meal or a roof in front of any person because the page is about where the zeros of one sum sit. One indirect tie exists. The evenness of the primes is part of why a phone can find a fresh prime with hundreds of digits within seconds and such primes sit inside the digital locks that guard the bank transfers and benefit payments that people use to pay for groceries and rent. Those locks work today whether or not anyone proves the critical line claim so a proof would not add a meal or a roof either.

Deep human connection: the page offers one small thing. Another person can recheck every table on the page so a reader who knows more has a concrete spot to answer (a figure that looks wrong or a mechanism that the page left out) and an answer of that kind lets two people learn how the other person thinks. A page cannot stand in for knowing another person's heart and mind.

## How the questions tie back to the lists

- The "give or take" figure on each line of the master lists is a square root because independent wobbles add by squares. The same squares rule applied to the prime factors is what picks out the dial setting 1/2.
- The baseline on every line (1 divided by the natural logarithm) is the proven fact that no zero sits at the dial setting 1. At the dial setting 1 the prime wobble is the finite pile 0.2368 built from the prime lamps 0.4522.
- The "could be luck" column treats the primes as independent chances. The prime wobble table on this page is a direct check of that picture: the measured piles match the independent prediction to three decimal places at the dial settings 2 and 1.5 and 1.

## Numbers that this page adds to the list in Part 7

36. 5.3157 is the average natural logarithm of (pitch divided by 2 × pi) from 100 to 3100 and is the slope of the ramp left of 1/2.
37. 0.846 is 5.3157 divided by (2 × pi) and is the number of zeros for each unit of pitch in that stretch.
38. 0.2368 is the pile of squared prime wobble at the dial setting 1 which is half of the prime lamps 0.4522 plus a small extra.
39. 14.52 and 20.65 and 25.49 are the first three pitches where one speaker and one mirror image cancel.
40. 0.00397 is the height of the small hump between the two close zeros near the pitch 7005.
41. 0.2841 is the middle weight of the blended row.
42. 0.8085 and 85.699 are the dial setting and the pitch of the first zero of the blended row that sits off the line.
