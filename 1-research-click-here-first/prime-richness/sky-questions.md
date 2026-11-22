# Questions about crowded lamps and the dark night sky

> **About this page:** One AI model (Claude) wrote this page on 22 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the ten earlier question pages in this folder (the last one is [root-questions.md](root-questions.md) which found the boundary at the square root). The facts are standard mathematics and physics that a search will turn up so the page claims no new result. The value of the page is the plain-language route. A program rechecked every figure (the file sky_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) except two known values that the page marks. No other person has reviewed the page yet.

## Question: is the boundary the same thing as lamps at 2 and 4 and 8 and 16 being pulled in to 1 and 2 and 3 and 4?

Yes with one detail: which fading rule the lamps follow.

**With the "1 over the distance" rule.** Lamps at 2 and 4 and 8 and 16 give 1/2 + 1/4 + 1/8 + … which settles at exactly 1. Lamps at 1 and 2 and 3 and 4 give 1 + 1/2 + 1/3 + … which grows without limit.

**With the inverse-square rule.** Lamps at 2 and 4 and 8 give 1/4 + 1/16 + 1/64 + … = 1/3 and lamps at 1 and 2 and 3 give 1.645. Under that rule the lamps have to be pulled in to the square roots before the total becomes infinite.

A lamp at the root of k under the inverse-square rule gives 1/k and a lamp at k under the "1 over the distance" rule gives 1/k. Both descriptions land on the row 1 and 1/2 and 1/3 and 1/4 which just fails to settle.

Under the "1 over the distance" rule the totals on the way in are 1 for the doublings and 1.645 for lamps at the squares and 2.612 for lamps at each whole number raised to the power 1.5 and 10.58 for the power 1.1 and 100.6 for the power 1.01 and infinity for the whole numbers themselves.

Lamps at the primes with "1 over the distance" fading give the sum of 1 over each prime which is infinite at the double logarithm pace. So the primes are spaced just closely enough to land on the infinite side and the squares are not.

## Question: with only the inverse-square rule how does the total explode when the lamps are pulled in to the square roots?

The pull is not proportional. The lamp at 1 stays at 1. The lamp at 4 moves to 2. The lamp at 100 moves to 10. The lamp at 10000 moves to 100. A proportional pull would not explode: halving every distance turns 1.645 into 6.58.

After the pull the far lamps crowd together.

- Between 1 and 2 there are 3 lamps (the roots of 1 and 2 and 3).
- Between 2 and 3 there are 5 lamps (the roots of 4 through 8).
- Between 3 and 4 there are 7 lamps.
- Between 10 and 11 there are 21 lamps.

Before the pull every stretch of one unit held 1 lamp.

- Between 1 and 2 the light was 1 and is now 1.833.
- Between 2 and 3 the light was 0.25 and is now 0.885.
- Between 3 and 4 the light was 0.111 and is now 0.600.
- Between 10 and 11 the light was 0.01 and is now 0.191.

Before the pull each stretch gave 1 over the distance squared. After the pull each stretch gives about 2 over the distance because each lamp fades as 1 over the distance squared while the number of lamps in a stretch grows as about twice the distance.

- Out to a distance of 10 the total is 5.19.
- Out to a distance of 100 the total is 9.79.
- Out to a distance of 1000 the total is 14.39.
- Out to a distance of one million the total is 28.21.

Each tenfold step in distance adds 4.6 which is twice the natural logarithm of 10.

Pulling each lamp to its number raised to a power gives 1.645 for a power of 1 and 1.882 for 0.9 and 2.612 for 0.75 and 5.592 for 0.6 and 10.58 for 0.55 and 100.6 for 0.505 and 1000.6 for 0.5005 and infinity for 0.5. For a power above 1/2 the fading still beats the crowding.

## Question: light fades at a squared rate so do the distances need to be square roots to reach the tipping row 1 over n?

Yes. The square root undoes the squaring in the fading rule.

- Light fades as 1 over the distance squared.
- The row 1 + 1/2 + 1/3 + … is the tipping point.
- For the lamp at number n to give exactly 1/n the distance squared has to equal n.

The lamp for 4 sits at 2 and gives 1/4. The lamp for 9 sits at 3 and gives 1/9. The lamp for 100 sits at 10 and gives 1/100.

If brightness faded as 1 over the distance the lamps would tip at the whole numbers. With 1 over the distance squared the lamps tip at the square roots. With 1 over the distance cubed the lamps would tip at the cube roots.

On the critical line the strength of each source is 1 over the square root of n and the energy of a wave is the strength squared so the energies are 1/n. A quantity that gets squared needs a square root in the setup to land on 1 over n.

## Question: is this the puzzle about why the night sky is dark?

Yes. The total is decided by a race between how fast each lamp fades and how fast the number of lamps grows with distance. Random placement or tidy placement makes almost no difference.

- **A line.** Each stretch of one unit holds about the same number of lamps and each lamp fades as 1 over the distance squared. The total is finite.
- **A flat sheet.** A ring one unit wide at distance d holds about 6.28 × d lamps. Each gives 1 over d squared so the ring gives about 6.28 / d. The total grows forever at a logarithm's pace. Lamps on a square grid out to a distance of 300 total 38.4.
- **Space.** A shell one unit thick at distance d holds about 12.57 × d squared stars. Each gives 1 over d squared so every shell gives the same 12.57. The total is infinite.

The square root lamps behave like the flat sheet because in both the number of lamps in a stretch grows in proportion to the distance.

The rule: if the number of lamps within a distance d grows slower than d squared the total is finite. A line is on the finite side and a sheet is on the boundary and space is on the infinite side.

An endless unchanging universe evenly filled with stars would have a sky as bright as the surface of a star in every direction. The real sky is dark because the universe has a finite age (light from beyond a certain distance has not had time to arrive) and because the expansion of space stretches the light from far galaxies to wavelengths the eye cannot see.

## Question: if lamps are placed at random on a line what is the chance of infinite brightness?

Zero under the inverse-square rule. The far lamps always add up to a finite amount and a huge total needs one lamp to land almost on top of you.

A count of 20000 random layouts with one lamp per unit of length on average:

- The middle layout has a total of 3.49.
- One layout in ten has a total above 91.5.
- The brightest layout has a total of about 1.27 billion.
- The average over all the layouts is about 128000.
- The 20 brightest layouts hold 98.6% of all the light in the 20000 layouts.

So every layout is finite and the average is carried by a few layouts with a very close lamp. With more and more layouts the average keeps climbing without limit.

Lamps at the primes thin out along the line so the prime lamps total just 0.4522.

## Question: 1 over n already adds up to infinity so does taking numbers away still leave infinity for the primes?

Not by that logic alone. Taking a finite amount away from an infinite total leaves an infinite total: the first million terms of 1 + 1/2 + 1/3 + … add up to about 14.4. Going from all whole numbers to the primes removes infinitely many terms and the removed terms add up to infinity so the leftover has to be worked out case by case.

Groups kept from 1 + 1/2 + 1/3 + … :

- The even numbers give an infinite total.
- The primes give an infinite total at the double logarithm pace.
- The perfect squares give 1.645.
- The doublings 2 and 4 and 8 give 1.
- The twin primes give about 1.9 (a known value that the program did not recompute).
- The numbers with no digit 9 give about 22.9 (a known value that the program did not recompute).

The total is infinite when the group stays dense enough. Primes near n show up about once in every "natural logarithm of n" numbers. Squares near n show up about once in every "twice the root of n" numbers.

The reason that works for the primes: the sum over all whole numbers equals a product with one factor for each prime. If the sum of 1 over each prime were finite the product would be finite. The product equals 1 + 1/2 + 1/3 + … which is infinite. So the two infinities are linked through the product over the primes.

## Question: light is 1 over the distance squared. What physical things go as 1 over the distance?

1. **The strength of a wave in open space.** Brightness is energy and energy goes by the wave's strength squared. The strength of the wave from a lamp falls as 1 over the distance. The pressure of a sound wave from a small speaker does the same.
2. **Energy spreading across a flat sheet.** Ripples on a pond spread around a circle and the distance around a circle grows in plain proportion to the distance so the energy of a ripple falls as 1 over the distance.
3. **Light from a long line.** The energy from a long glowing tube falls as 1 over the distance for as long as the tube looks long from where you stand.
4. **Stored energy of gravity.** The pull of gravity falls as 1 over the distance squared and the energy needed to climb away (counted from far away) goes as 1 over the distance.
5. **How big something looks.** The width of an object as seen by the eye falls as 1 over the distance and the patch of view the object covers falls as 1 over the distance squared.

How the spreading rules line up with the dial:

- In open space the energy fades as 1 over the distance squared and the wave strength as 1 over the distance.
- On a flat sheet the energy fades as 1 over the distance and the wave strength as 1 over the square root of the distance once the ripple is far from its source.
- Along a string or inside a pipe a wave has nowhere to spread.

The row with the dial at 2 is energy in open space. The row with the dial at 1 is wave strength in open space and energy on a flat sheet. The row with the dial at 1/2 (the critical line) is wave strength on a flat sheet. So the critical line setup is a row of sources making ripples on a pond.

## How the questions tie back to the lists

- The prime baseline on the master lists rests on the primes being just dense enough for the sum of 1 over each prime to be infinite.
- The random layouts show a case where the average is carried by a few rare results which is why each line of the lists reports a count and the odds of luck and not an average alone.

## Numbers that this page adds to the list in Part 7

46. 4.6 is twice the natural logarithm of 10 and is the light gained for each tenfold step in distance by lamps at the square roots.
47. 6.28 and 12.57 are 2 × pi and 4 × pi which count the lamps in a ring of a sheet and in a shell of space.
48. 22.9 is the total of 1 over each whole number with no digit 9.
