# Questions about the ladder of sums and chunky steps and the shuffle each prime gives

> **About this page:** One AI model (Claude) wrote this page on 21 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the page [log-questions.md](log-questions.md). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route and the pictures the author and the chatbot built along the way (the announcers and the jar with two notebooks). A program rechecked every figure (the file ladder_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## Question: how do the prime counting equations use the squeeze and the unpacking?

The equations run a three-step loop. A logarithm squeezes so that multiplying turns into adding. The adding gets done. A power of e unpacks the result back into a count.

The loop is needed because primes belong to multiplying (every number is a product of primes) and counting belongs to adding (the number line goes up by 1 each step). A logarithm is the tool that carries a multiplying fact over into an adding fact.

## Question: does a product of primes really turn into a sum of logarithms?

Yes. The number 60 is 2 × 2 × 3 × 5. The natural logarithm of 60 is 4.094 which equals 0.693 + 0.693 + 1.099 + 1.609 and those are the natural logarithms of 2 and 2 and 3 and 5.

Each prime has a fixed length: 0.693 for the prime 2 and 1.099 for the prime 3 and 1.609 for the prime 5 and 1.946 for the prime 7. Every whole number is a stick built by laying prime lengths end to end. A prime number is a stick made of one piece. Each whole number can be built in only one way so no pile of 0.693 lengths ever equals a pile of 1.099 lengths which is the squeezed form of the fact that a power of 2 never equals a power of 3.

## Question: what bookkeeping forces the rule "1 divided by the natural logarithm"?

Add the natural logarithms of every number from 1 to 997 and the total is 5891.4. The primes must hand out that same total because the prime 2 puts 0.693 into every second number and again into every fourth number and the prime 3 puts 1.099 into every third number and so on. A program confirmed both totals are 5891.4.

The balance says the sum of (logarithm of p) divided by p over the primes up to x must stay close to the logarithm of x. For primes up to 997 the sum is 5.61 against 6.905 and for primes up to one million the sum is 12.48 against 13.82 so the gap stays near 1.3. The balance holds only if primes near a number thin out at the rate 1 divided by the natural logarithm because a thicker supply of primes would hand out too much weight.

The best simple count adds 1 divided by the natural logarithm for every number from 2 to the top. That sum is 177.0 at 997 against the true count 168 and 78627 at one million against the true count 78498. The "chance" figure on each line of the master lists is that same sum taken over the outputs of a recipe.

## Question: is the logarithm a round trip into another realm and back?

Yes. Take 6 × 7. Going in: the natural logarithms are 1.7918 and 1.9459. Working on the logarithm side: 1.7918 + 1.9459 = 3.7377. Going back out: e raised to the power 3.7377 is 42.

On the logarithm side every operation drops one level. Multiplying becomes adding and dividing becomes subtracting and raising to a power becomes multiplying and taking a root becomes dividing. The number 1 becomes 0 because multiplying by 1 changes nothing and adding 0 changes nothing. The number 0 cannot be carried across because no count of copies of e multiplies out to 0.

The base is a choice of measuring unit. Every base carries multiplying over to adding and base e is the unit where the prime rule has no leftover factor.

## Question: how did anyone invent a system that drops every operation one level?

The need was practical. Around the year 1600 astronomers and ship navigators multiplied seven digit numbers by hand all day.

The seed is ancient. Write the doublings 1 and 2 and 4 and 8 and 16 and 32 in one row and the step numbers 0 and 1 and 2 and 3 and 4 and 5 beneath. Multiplying two numbers in the top row matches adding the two step numbers beneath (4 × 8 = 32 sits above 2 + 3 = 5). The top row has big gaps so the trick worked only for doublings.

The leap was to pack the top row so densely that every number had a step number. One inventor used a multiplier barely below 1 so the row crept along in tiny steps and spent about twenty years computing the table by hand and published the table in 1614. The table happened to sit near base 1/e because (1 − 1/n) multiplied n times closes in on 1/e. The number e itself was noticed decades later through questions about interest on money.

The "one level down" behavior was not designed piece by piece. Multiplying is repeated adding and raising to a power is repeated multiplying so the operations form a ladder. A logarithm counts repeats and counting the repeats of one rung is the job of the rung below.

## Question: why is a power of zero equal to 1 and not 0?

Taking more and more square roots heads toward 1. The values of e to the powers 1 and 0.5 and 0.25 and 0.125 are 2.718 and 1.6487 and 1.2840 and 1.1331. The power 0.001 gives 1.0010 and the power 0.0001 gives 1.0001.

Walking down the whole number powers divides by 2.718 each step: 20.09 then 7.389 then 2.718 then 1 then 0.3679. The pattern passes straight through 1.

Adding starts from 0 because adding nothing leaves 0. Multiplying starts from 1 because 1 is the number that changes nothing when multiplied in. So zero copies of e multiplied in leaves the starting 1 untouched.

For a tiny count the result is almost exactly 1 plus the count. That holds for base e and not for other bases (10 to the power 0.001 is 1.0023) and that property is what makes e the natural base.

## Question: is matrix math another kind of compression?

A matrix packs a different thing. A logarithm squeezes one number. A matrix (a grid of numbers) stores a whole action such as "turn every point on a page by 30 degrees" in four numbers.

- The literal next squeeze after a logarithm is the logarithm of a logarithm. A 100 digit number has a natural logarithm of 230 and the logarithm of 230 is 5.4.
- Turning by 30 degrees and then by 45 degrees means multiplying two grids and the result is a turn by 75 degrees. So the angle acts as the logarithm of the turning grid.
- The grid with 1 and 1 on the top row and 1 and 0 on the bottom row produces the Fibonacci numbers when multiplied by itself (the tenth power holds 89 and 55 and 55 and 34). The stretch factors of that grid are 1.618 and −0.618 so the golden ratio is the stretch factor of the Fibonacci grid.

## Question: does any mathematics attach a matrix to each prime and look for patterns?

Yes and one piece of that work sits inside the prediction formula of the checker page in this folder.

Take x² + 1 and ask which whole numbers x make x² + 1 divisible by a prime. For 5 the values 2 and 3 work. For 7 no value works. For 13 the values 5 and 8 work. The equation has two hidden roots and each prime either leaves the two roots in place or swaps the two roots. "Leave in place" is the grid with rows 1 0 and 0 1. "Swap" is the grid with rows 0 1 and 1 0. The number of working values is the sum along the diagonal of the prime's grid.

The predicted percentage for an equation multiplies one factor for each prime and each factor depends on how many values of n make the output divisible by that prime. That count is the diagonal sum. The equation n² + n + 41 scores high because every prime below 41 gets the swap grid which means no small prime divides an output.

## Question: what is the shuffle and what does "fair sampler" mean?

Take x³ − 2. The number of working values for a prime is always 0 or 1 or 3. For 5 the value 3 works. For 7 and 13 no value works. For 11 the value 7 works. For 31 the values 4 and 7 and 20 work. For 43 the values 20 and 32 and 34 work.

The equation has three hidden roots. Arithmetic with remainders after dividing by a prime p has one special move which is raising a number to the power p. The move leaves every ordinary whole number unchanged and keeps every equation true so the move sends each root to a root. A root that stays in place is a working value.

Three roots can be shuffled six ways.

- One shuffle leaves all three roots in place and gives 3 working values.
- Three shuffles swap two roots and leave one in place and give 1 working value.
- Two shuffles rotate all three roots and give 0 working values.

No shuffle leaves exactly two roots in place which is why a count of 2 never appears.

A count over all 664577 primes from 5 to ten million:

- 16.64% of the primes gave 3 working values against a fair share of 16.67%.
- 50.01% gave 1 working value against a fair share of 50%.
- 33.35% gave 0 working values against a fair share of 33.33%.

A proven theorem says the primes hand out the shuffles that an equation allows in exactly fair proportions. (Some equations allow only part of the full set of shuffles. The equation x³ − 2 allows all six.)

The average number of working values per prime in the count was 0.9993 and the fair shares give exactly 1. An average of 1 means an equation that does not factor loses outputs to the primes at the same average rate as the number line. So a high percentage is won by getting "no working values" at the small primes where each dodge is worth the most.

For x² + 1 the remainder of the prime after dividing by 4 decides the shuffle. For x³ − 2 no remainder rule of that kind exists and predicting the shuffle for such equations is one of the largest research efforts in mathematics.

Three more facts from this area stated without detail: for equations such as y² = x³ + x + 1 each prime gets a two by two grid whose stretch factors have a size equal to the square root of the prime. The spacings of the ripples that correct the prime count match the spacings of the stretch factors of huge grids of random numbers (checked by computer and unproven). A grid that marks which numbers divide which has a summary number whose slow growth is equivalent to the unproven claim about the critical line.

## Question: why does the sum of 1 over each prime grow like the logarithm of the logarithm?

Two squeezes are stacked.

Moving from n to n + 1 raises the natural logarithm by almost exactly 1/n. So adding 1/2 + 1/3 + 1/4 + … walks along the logarithm scale and the distance walked up to x is the natural logarithm of x.

Primes near n show up at a rate of 1 divided by the natural logarithm of n. So in the sum over primes each step is kept a fraction of the time and the fraction is 1 divided by the distance already walked. A walk where the step at distance u is weighted by 1/u is the same kind of sum again along the logarithm scale. The total is the logarithm of the distance walked.

- Up to 10 the sum over primes is 1.176.
- Up to 100 the sum is 1.803.
- Up to 1000 the sum is 2.198.
- Up to one million the sum is 2.887 (the logarithm of the logarithm is 2.626 and the gap heads to 0.2615).

The sum over all whole numbers gains 0.693 each time the top number doubles. The sum over primes gains 0.693 each time the top number is squared. A total of 4 needs every prime up to about 10 to the power 18. A total of 10 needs every prime up to a number with over 7000 digits. The sum still grows without limit.

## Question: is there a ladder where each rung is the rung above squeezed once more?

Yes.

- 1 + 1 + 1 + … up to x totals x.
- 1 + 1/2 + 1/3 + … up to x totals about the natural logarithm of x.
- 1/2 + 1/3 + 1/5 + … over the primes up to x totals about the logarithm of the logarithm of x.

The rule that moves down one rung: divide each term by the running total of the rung above. On the top rung the running total at n is n and dividing each 1 by n gives 1/n. On the second rung the running total at n is the natural logarithm of n and dividing each 1/n by that logarithm gives 1 divided by (n times the natural logarithm of n). Keeping only the primes does that dividing automatically.

The sum 1 + 2 + 3 + 4 + … sits one rung above the top because each term n is the running total of 1 + 1 + 1 + … Going up the ladder multiplies each term by the running total and going down divides.

The next rung down would grow like the logarithm of the logarithm of the logarithm which is about 0.97 at one million and about 1.69 at a 100 digit number. The chatbot knows of no famous family of numbers that sits on that rung. Twin primes (pairs such as 11 and 13) thin out faster than every rung so the sum of 1 over each twin prime settles on a finite total near 1.9. That finite total is proven while the question of whether twin primes go on forever is open.

## Question: why does dividing by the running total give a logarithm?

Dividing a step by the running total turns the step into a percentage of what is already there and adding up percentage growths is what a logarithm measures.

Plain counting announces how much each new 1 adds: going from 1 to 2 is +100% and from 2 to 3 is +50% and from 3 to 4 is +33%. So the reciprocals 1 + 1/2 + 1/3 + … are the percentage growths of plain counting added together.

Percentage growths really multiply. The product (1 + 1/1) × (1 + 1/2) × (1 + 1/3) up to (1 + 1/10) equals exactly 11 because 2/1 × 3/2 × 4/3 cancels in a chain. A logarithm turns the multiplying into adding so the sum 1 + 1/2 + … + 1/10 = 2.93 tracks the natural logarithm of 11 = 2.40 with a fixed gap.

The rule holds for any growing total. For the square numbers the steps are 1 and 3 and 5 and the running totals are 1 and 4 and 9. Dividing each step by its total and adding up to the 1000th square gives 13.33 and the natural logarithm of 1000 squared is 13.82.

A check on the second rung: from 1000 to one million the sum of 1 divided by (n times the logarithm of n) rose by 0.6931 and the sum of 1 over each prime rose by 0.6892 and the logarithm of the logarithm rose by 0.6931.

## Question: what are the first announcer and the second announcer?

Picture a jar that gets one marble at a time and two people with notebooks.

The first person writes how big each new marble is compared with what the jar held: 1 then 1/2 then 1/3 then 1/4. The running total of the first notebook is 1 then 1.5 then 1.83 then 2.08.

The second person watches only the first notebook and asks the same question about that total. The line 1/2 lands on a total of 1 so the second person writes 50%. The line 1/3 lands on 1.5 so the second person writes 22%. The line 1/4 lands on 1.83 so the second person writes 13.6%. The line 1/5 lands on 2.08 so the second person writes 9.6%.

- At 1000 marbles the first notebook totals 7.49 and the second notebook totals 2.15.
- At one million marbles the first notebook totals 14.39 and the second notebook totals 2.81.

The first notebook gains 0.693 whenever the jar doubles. The second notebook gains about 0.693 whenever the first notebook doubles which takes roughly squaring the jar.

Reading the first notebook only at the prime-numbered marbles gives a total that rises in step with the second notebook. Primes near a marble show up about once in every "first notebook total" marbles so skipping to the primes thins the lines by the same amount the second person divides by. Near 1000 the first notebook's line is 0.1% and primes show up once per 6.9 numbers so the prime lines average 0.0145% per number which is the second person's line there.

## Question: what is the equation for e doing in this language?

The expression (1 + 1/n) multiplied n times is n announcements of "+1/n". The pile of announcements is exactly 1 (100%) and the product is where the number ends up.

- One step of +100% ends at 2.
- Two steps of +50% end at 2.25.
- Four steps of +25% end at 2.4414.
- Ten steps of +10% end at 2.5937.
- One hundred steps of +1% end at 2.7048.
- One thousand steps of +0.1% end at 2.7169.

So e = 2.718 is where a number ends up when 100% of growth is delivered in pieces so small that the pieces blend into smooth growth. The natural logarithm of a number is the pile of tiny announcements needed to grow from 1 to that number (690.5% for 997).

Taking the logarithm of the equation turns the n multiplications into n additions of one small number. For n = 10 the small number is the natural logarithm of 1.1 = 0.09531 and ten of those total 0.9531. For n = 100 the total is 0.99503 and for n = 1000 the total is 0.9995. The total closes in on 1 which means one copy of e.

## Question: why does a chunky step fall short of a smooth step?

A chunky step delivers all its growth at the end. Smooth growth lets the growth made early start growing too.

- A chunk of +100% ends at 2 and a smooth 100% ends at 2.718.
- A chunk of +50% ends at 1.5 and a smooth 50% ends at 1.6487.
- A chunk of +10% ends at 1.1 and a smooth 10% ends at 1.1052.
- A chunk of +1% ends at 1.01 and a smooth 1% ends at 1.01005.

The bonus that smooth growth earns is about half of the announced amount squared. A bank that pays 100% once at the end of a year turns 1 into 2 and a bank that pays that 100% spread over every instant turns 1 into 2.718.

A shrinking chunk misses in the other direction. A chunk of −50% leaves 0.5 and a smooth 50% shrink leaves 0.6065.

The shortfalls explain two constants.

- The gap constant 0.5772 is the total shortfall of the counting chunks +100% and +50% and +33% and so on. The first three shortfalls are 0.3069 and 0.0945 and 0.0457.
- The sieve factors (1 − 1/p) are shrinking chunks. The prime 2 misses by 0.1931 and the prime 3 by 0.0721 and the prime 5 by 0.0231 and the prime 7 by 0.0113. Across all primes the misses total 0.3157.
- The prime constant 0.2615 equals 0.5772 minus 0.3157.

The "half of the amount squared" bonus is also where the "distance squared divided by 2" in the bell curve formula originates.

## Question: which infinite sums add up to exactly 1?

- 1/2 + 1/4 + 1/8 + … totals 1 because each term fills half of what is missing. With a leading 1 in front the total is 2.
- 9/10 + 9/100 + 9/1000 + … totals 1 which is why 0.999 repeating equals 1.
- 2/3 + 2/9 + 2/27 + … totals 1.
- 1/2 + 1/6 + 1/12 + 1/20 + … totals 1 where the bottoms are 1 × 2 and 2 × 3 and 3 × 4 and 4 × 5.
- 1/2 + 2/6 + 3/24 + 4/120 + … totals 1 with running totals 1/2 and 5/6 and 23/24 and 119/120.

A shrinking sum where each term is the term before times a fixed factor r totals "first term divided by (1 − r)". So a first term of (1 − r) gives exactly 1.

The fourth sum works by cancelling. 1/2 is 1/1 − 1/2. 1/6 is 1/2 − 1/3. 1/12 is 1/3 − 1/4. 1/20 is 1/4 − 1/5. Lined up the −1/2 cancels the +1/2 and the −1/3 cancels the +1/3 and the −1/4 cancels the +1/4. The pieces left are the 1/1 at the front and the −1/5 at the back so four terms total 4/5. After n terms the total is 1 minus 1/(n + 1). A sum that folds up into its two end pieces is called a telescoping sum.

## Question: why is the chance of zero events the same as the chance of one event when one event is expected?

Split a day into 100 slots with a 1 in 100 chance of an event in each slot.

Zero events needs all 100 slots empty which has chance 0.99 multiplied 100 times = 0.3660.

Exactly one event needs one slot to fire (chance 1/100) and 99 slots to stay empty. The event can sit in any of 100 slots. The 100 choices cancel the 1/100 chance and what is left is 0.99 multiplied 99 times = 0.3697.

- With 10 slots the chances are 34.9% for zero and 38.7% for one.
- With 100 slots the chances are 36.6% and 37.0%.
- With 1000 slots the chances are 36.77% and 36.81%.

Both close in on 1/e = 36.79%. The tie needs the expected count to be exactly 1 because the cancellation is "number of slots times chance per slot". With an expected count of 2 the chances are 13.5% for zero and 27.1% for one.

For an expected count of 1 the full list is 36.8% for zero and 36.8% for one and 18.4% for two and 6.1% for three and 1.5% for four. The chances cover every outcome so the chances total 1 which is the same as saying 1 + 1 + 1/2 + 1/6 + 1/24 + … equals e.

A window of the number line with a length equal to the natural logarithm of the numbers inside is expected to hold 1 prime. The slot model predicts about 36.8% of those windows hold no prime. Real primes track the model closely and not exactly because primes are not fully independent.

## How the questions tie back to the lists

- The "chance" figure on each line of [ranked-list.md](ranked-list.md) is the sum of 1 divided by the natural logarithm over the outputs.
- The predicted percentage on the checker page multiplies one factor per prime and each factor uses the count of working values which is the diagonal sum of the shuffle that prime gives.
- An equation that does not factor meets the primes at the same average rate as the number line so the high lines on the lists win by dodging the small primes.
