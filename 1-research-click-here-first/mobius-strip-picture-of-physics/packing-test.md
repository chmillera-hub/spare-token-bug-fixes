# Packing test: how much room do Mobius strips need compared with flat strips and plain loops?

An AI chatbot (Claude) ran these computer tests and wrote this page on 14 November 2026. No other person has rerun the tests which means every number on this page is unconfirmed.

## The prediction being tested

The owner of this repository predicted that Mobius strips are fluffy which means that a pile of Mobius strips needs more room than a pile of flat strips. The reason offered was that the half twist makes a Mobius strip bump into neighbors more readily. The prediction matters for the ribbon picture in this folder because flat pieces of space turning into twisted loops could then need more room.

## The six shapes

Every shape was made from the same strip which means the same length and the same width and the same thickness. Every shape was rigid so no shape could bend or be pressed flat.

- A straight flat strip.
- A flat ring like a washer.
- An untwisted loop that looks like an open-ended cylinder.
- A Mobius strip which is a loop with one half twist.
- A loop with two half twists.
- A loop with three half twists.

The strip was about 6.3 units long and 0.5 units wide. The loops were about 2.5 units across.

## Test 1: pour and shake

A physics program dropped pieces at random angles into a square bin under gravity. The program jostled the pile and added more pieces until pieces stuck out above the rim. The count is how much strip sat below the rim in units of whole strips.

Small bin (4 units wide):

- Flat ring: about 96 strips.
- Mobius strip: about 56 strips.
- Untwisted loop: about 52 strips.
- Loop with two half twists: about 48 strips.
- Loop with three half twists: about 47 strips.
- Straight flat strip: about 12 to 16 strips because the strip is longer than the bin is wide so the strips jammed at steep angles.

Medium bin (6 units wide):

- Flat ring: about 413 strips.
- Mobius strip: about 188 strips.
- Untwisted loop: about 176 strips.
- Loop with two half twists: about 165 strips.
- Loop with three half twists: about 152 strips.
- Straight flat strip: about 140 strips. The strip is still slightly longer than the bin is wide so many strips rested at an angle.

Large bin (7 units wide so that a straight strip can lie flat):

- Straight flat strip: about 355 strips.
- Mobius strip: about 299 strips.
- Untwisted loop: about 285 strips.
- Loop with two half twists: about 266 strips.
- Loop with three half twists: about 251 strips.
- The flat ring was not run in the large bin because the run needed more computer time than was available.

## Test 2: orderly stacking

A program looked for the smallest step at which identical copies of one shape can be stacked and then measured how close two stacks can stand.

- Flat pieces stack one thickness apart like sheets of paper.
- Every closed loop needed a step of one full strip width because some part of the ribbon stands edge-on to the stacking direction. The check covered 163 stacking directions.
- The space per piece in the tightest stacks found was 0.20 for the straight strip and 0.37 for the flat ring and 2.08 for the untwisted loop and 2.26 for two half twists and 2.47 for the Mobius strip and 2.56 for three half twists.

## Test 3: random placement with no gravity

A program placed pieces at random spots and random angles in a box and stopped when no more pieces fit. Between 84 and 92 pieces fit for every shape so the six shapes came out the same within the noise of the test.

## Findings

1. Flat pieces packed tightest in the pour and shake test. Flat rings fit about twice as much strip as any loop. Straight flat strips fit about 19 percent more strip than Mobius strips in the bin where the straight strip could lie flat.
2. A straight strip packs poorly in a bin narrower than the strip because the strips jam at steep angles. So the result for a flat strip depends on the bin being wide enough.
3. The Mobius strip was not fluffier than the untwisted loop in the pour and shake test. The Mobius strip fit 5 to 7 percent more strip than the untwisted loop in all three bins. So that part of the prediction was not supported.
4. More twist made loops fluffier. Loops with two half twists fit about 6 to 8 percent less strip than the untwisted loop and loops with three half twists fit about 10 to 14 percent less.
5. The orderly stacking test ranked the Mobius strip as needing about 19 percent more room than the untwisted loop. The two tests disagree because neat stacks and shaken piles are different arrangements.
6. Here is a possibility for finding 3. The Mobius shape used here has a stretch where the ribbon lies flat like a ring and that flat stretch could let neighbors slide in close while an open-ended cylinder holds an empty middle.
7. So the tests suggest that room needed goes up when a flat strip closes into a loop and goes up again with two or more half twists. A single half twist sits slightly on the tighter side of the plain loop in a shaken pile.

## Limits of the tests

- Each loop count in the small and medium bins is the mean of two random starts. The counts in the large bin and the flat ring in the medium bin come from one start except for the straight strip which had two starts.
- One run of the straight strip in the medium bin was thrown out because pieces passed through each other in the physics program.
- Jostling raised each count by a few percent. A longer or harder shake could settle the piles further.
- Pieces were rigid. A paper loop can be pressed flat with creases and a pressed loop would pack far tighter.
- The Mobius shape was the standard textbook shape. A relaxed paper Mobius strip settles into a different shape and could pack differently.
- The stacks in test 2 are the tightest found and no proof shows that tighter stacks do not exist.
- A single web search found no published study of packing many Mobius strips together.
- The link from paper-like shapes to space itself is an idea in this folder and the tests measure paper-like shapes alone.

## How to rerun the tests

The programs sit in the folder named packing-test inside the mobius-strip-calculations folder inside the boring-things folder of this repository. The page named README.md in that folder says what each program does.
