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

## Main test: pour and shake in a big bin

The owner of this repository pointed out that the first bins were so small that pieces kept getting stuck on the walls. So the test was rerun in a bin 11 units wide which has four times the room of the largest earlier bin. Each run held roughly 850 to 1250 pieces. The packing was measured in the middle of the pile away from the walls and the floor and the top. The numbers are strips per unit of space so a larger number means tighter packing.

- Straight flat strip: 1.37 or more. The run was stopped by a time limit when the pile had almost filled the measuring zone so the true number could be a little higher.
- Untwisted loop like an open-ended cylinder: 0.945
- Mobius strip which has one half twist: 0.940
- Loop with two half twists: 0.900
- Loop with three half twists: 0.792
- Loop with four half twists: 0.766
- Loop with five half twists: 0.696
- Loop with six half twists: 0.674

Mixes with equal numbers of two shapes poured together:

- Mobius strips mixed with untwisted loops: 0.946
- Mobius strips mixed with straight flat strips: 1.10. The middle of that pile held about 70 percent straight strips and 30 percent Mobius strips because the two shapes did not stay evenly mixed.

## An equation for the loops and how the equation did when tested

The first draft equation was fitted to the loops with zero to three half twists. The draft said that the space per strip grows with the cube of the number of half twists. The draft predicted 0.66 for four half twists and the measured value was 0.766. So the first draft failed the test.

The second equation was fitted to the loops with zero to four half twists:

space per strip = 1.02 + 0.07 x (number of half twists)

The packing number is 1 divided by the space per strip. The second equation was then tested on two new runs.

- Five half twists: the equation predicted 0.73 and the measured value was 0.696.
- Six half twists: the equation predicted 0.70 and the measured value was 0.674.

So the second equation landed within about 5 percent on both new runs and predicted slightly tighter packing than was measured. A fit to all seven loops gives space per strip = 1.01 + 0.08 x (number of half twists). So each half twist costs roughly 8 percent more room per strip. The fit is loosest at the start because the first half twist cost almost nothing.

A rule for mixes was also tested. The rule says that the space taken by a mix is the sum of the space each shape takes alone. The rule predicted 0.943 for Mobius strips mixed with untwisted loops and the measured value was 0.946. The rule predicted 1.21 or more for Mobius strips mixed with straight strips and the measured value was 1.10. So the rule held for two kinds of loop and failed for loops mixed with flat strips.

## Earlier test: pour and shake in small bins where the walls affected the counts

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

1. Straight flat strips packed tightest. Straight strips fit about 45 percent more strip per unit of space than any plain loop in the big bin.
2. The Mobius strip and the untwisted loop packed the same away from the walls (0.940 and 0.945). So the prediction that a Mobius strip is fluffier than an untwisted loop was not supported. The small edge that the Mobius strip showed in the small bins looks like an effect of the walls.
3. More twist made loops fluffier in a steady way. Each extra half twist cost roughly 8 percent more room per strip and a loop with six half twists needed about 40 percent more room than an untwisted loop.
4. So the room needed goes up in two steps. Closing a flat strip into a loop costs the most room. Adding twists beyond the first half twist costs more room again.
5. Mixing Mobius strips with untwisted loops changed nothing because the mix packed like either shape alone.
6. Mixing Mobius strips with straight flat strips packed about 9 percent looser than the simple sum rule predicts. Here is a possibility for the cause. Flat strips pack tightly by lying in layers and loops scattered among the strips break up the layers.
7. The two shapes in that mix did not stay evenly mixed because the middle of the pile ended up with more straight strips than Mobius strips.
8. The orderly stacking test ranked the Mobius strip as needing about 19 percent more room than the untwisted loop. Neat stacks and shaken piles are different arrangements so the two tests answer different questions.

## Limits of the tests

- Each run in the big bin was done once so a difference of a few percent between two shapes could be chance.
- The flat ring and a flat half ring were not finished in the big bin because flat pieces pack so tightly that the runs needed more computer time than was available.
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
