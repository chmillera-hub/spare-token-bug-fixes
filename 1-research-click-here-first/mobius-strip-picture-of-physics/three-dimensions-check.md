# Checking the three-dimensions result against published research and three new tests

November 12 2026

## What this page is

The page named half-angle-finding.md in this folder reports that one simple rule about a random arrow matches experiments on entangled pairs only when space has three dimensions. That page also says the chatbot never searched published research. This page reports that search and reports three new computer tests of the same rule.

Entangled pairs are two particles created together whose measurement results stay linked after the two particles are carried far apart.

## The rule in one paragraph

The rule uses three arrows because an arrow is the simplest picture of a direction. The twist arrow is the direction of the twist of the far ribbon strip. The detector arrow is the direction the far detector points. The hidden arrow points in an evenly random direction at the moment of measurement. The far strip agrees with the twist arrow when the tip of the hidden arrow sits lower along the detector direction than the tip of the twist arrow sits.

## What published research already contains

The search used a web search tool on 12 November 2026 and the search was short which means published work that the search missed could exist.

- The rule for one particle in three dimensions is already in print because physics papers describe a well-known model of one spinning particle where a hidden arrow is drawn evenly from all directions on a ball and the result depends on which side the hidden arrow falls. Two papers that describe the well-known model are linked in the sources part at the bottom of this page.
- One physics preprint first posted in 2001 and revised in 2024 states the same three-way pattern in the summary at the top of the preprint. The summary says a theory of entangled pairs built on a hidden space would stay under the classical limit with fewer than three dimensions and would match quantum physics with exactly three dimensions and would pass the quantum limit with more than three dimensions.
- The chatbot could not compare the method of the 2001 preprint with the rule on this page because the full text that the chatbot could open did not contain the calculation across dimensions. The method of the 2001 preprint could be the same as the rule on this page or could be different.
- A separate group of published papers reaches the number three by another road because those papers replace the ball of states of one quantum particle with a ball in any count of dimensions and find that entangled pairs exist only when the ball has three dimensions.

Here is a guess about what the search means: the three-way pattern is probably not a new discovery because the summary of the 2001 preprint states the same pattern. The tumbling ribbon picture and the short program could still be useful because any person with Python can rerun the program in under one minute.

## New test 1: exact formulas for the combined test score

Physicists use a combined test score to judge entangled pairs. Any rule where the results are set in advance cannot score above 2 and quantum physics cannot score above 2.828 and experiments agree with 2.828.

The earlier page gave the scores as rounded numbers from a computer. This page adds exact formulas for four counts of dimensions and the computer numbers match the exact formulas to four decimal places.

- In two dimensions the score is exactly 2.
- In three dimensions the score is exactly 2 times the square root of 2 which is about 2.8284.
- In four dimensions the score is exactly 2 plus 4 divided by pi which is about 3.2732.
- In five dimensions the score is exactly 5 divided by the square root of 2 which is about 3.5355.
- The score keeps climbing toward 4 as dimensions are added because the computer gave 3.9402 in ten dimensions and a number within 0.0001 of 4 in fifty dimensions. The number 4 is the largest score that arithmetic allows for any rule.

## New test 2: the far-end average in every count of dimensions

The earlier page checked only in three dimensions that no message can be sent. This page ran two million simulated pairs for each of five detector angles in two and three and four and five and six dimensions.

The average result at the far end stayed within 0.003 of zero in every run. The far-end average staying at zero means the far person sees an even split no matter where the near person points the near detector. So the rule in four or more dimensions scores above the quantum limit and still sends no message with fully linked pairs.

## New test 3: two mixes with the same average arrow

Quantum physics has a property that could be named arrow averaging. Arrow averaging means that a detector cannot tell apart two different mixes of particles when the two mixes share the same average arrow.

The test built two mixes of twist arrows.

- Mix one has the twist arrow tilted 60 degrees to the left of straight up half of the time and 60 degrees to the right of straight up the other half of the time.
- Mix two has the twist arrow straight up three quarters of the time and straight down one quarter of the time.
- Both mixes have the same average arrow because both averages point straight up with half the full length.

The test then pointed a detector straight up and counted how often the far strip agreed.

- In two dimensions mix one agreed 66.67 percent of the time and mix two agreed 75 percent of the time.
- In three dimensions mix one agreed 75 percent of the time and mix two agreed 75 percent of the time.
- In four dimensions mix one agreed 80.45 percent of the time and mix two agreed 75 percent of the time.
- In five dimensions mix one agreed 84.38 percent of the time and mix two agreed 75 percent of the time.
- In ten dimensions mix one agreed 94.13 percent of the time and mix two agreed 75 percent of the time.

A second run with the detector tilted 40 degrees gave the same pattern because the two mixes matched in three dimensions (69.15 percent for both) and differed in every other count of dimensions tested.

Three dimensions is the only count where the two mixes cannot be told apart. The reason is that the agree rate in three dimensions rises in a straight line with the height of the twist arrow and a straight-line rate depends only on the average arrow.

## Why test 3 could matter

The two mixes in test 3 were not picked at random. Quantum physics describes partly linked pairs which means pairs where the two results match more often than chance and less often than always. For one such partly linked pair quantum physics says the far particles form mix two when the near person points the near detector straight up. Quantum physics says the same far particles form mix one when the near person points the near detector sideways.

So here is a possibility worth testing. If the ribbon picture hands partly linked pairs the same arrows that quantum physics hands partly linked pairs then the rule in four dimensions could let the near person send a message faster than light. The near person could send the message by choosing between straight up and sideways and the far person could read the message by counting agreements (about 80 percent against 75 percent). The same reasoning could apply in two dimensions and in five or more dimensions because the two mixes differ there too.

The general idea behind test 3 is already in print. One linked paper in the sources part argues that any rate that is not a straight line lets people signal with linked pairs. The chatbot did not find the specific test with a random arrow in several counts of dimensions in print and the search was short.

Test 3 gives a second and separate reason for the number three. The combined test score says four or more dimensions would disagree with experiments. Test 3 says two dimensions and four or more dimensions could also break the ban on faster-than-light messages for partly linked pairs.

## What stays unproven

- The rule is still an assumption because nothing shows that space is built from ribbons or that a ribbon face tumbles evenly.
- The main document describes only fully linked pairs. Test 3 assumes that the ribbon picture would treat partly linked pairs the way quantum physics does and nobody has worked out whether a ribbon could do that.
- The rule still needs the whole ribbon to respond as one object at the same instant because a proven result in physics says no rule with results set in advance can score above 2.
- No person has rerun the new program which means every number on this page is a single unconfirmed analysis by one AI chatbot.

## How to check this page

The program is named dimension_followup.py and sits in the folder boring-things/research-program-files/mobius-strip-calculations in this repository. The program needs only Python with the numpy package and prints every number on this page in about one minute.

## Sources

- The 2001 preprint with the three-way pattern in the summary: https://arxiv.org/abs/quant-ph/0105020
- A review paper that describes the well-known model of one particle with a hidden arrow on a ball (part 2.6 of the review): https://arxiv.org/abs/1501.03202
- A second paper that describes the same well-known model in a part about one particle: https://arxiv.org/abs/0910.4222
- A paper that finds entangled pairs only when the ball of states has three dimensions: https://arxiv.org/abs/1111.4060
- A paper that derives the number of dimensions of space from properties of one quantum particle: https://arxiv.org/abs/1206.0630
- A paper arguing that any rate that is not a straight line lets people signal with linked pairs: https://arxiv.org/abs/2512.12636

## Who made this page

An AI chatbot (Claude) ran the search and the tests and wrote this page.
