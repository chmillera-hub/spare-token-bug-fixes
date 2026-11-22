# Questions about reciprocals and painters and smoothing and the −1/12

> **About this page:** One AI model (Claude) wrote this page on 21 November 2026 from a back and forth chat with the author of this repository. The questions are the author's questions with the wording tidied and the answers are the chatbot's answers shortened. The page continues the pages [log-questions.md](log-questions.md) and [ladder-questions.md](ladder-questions.md). The facts are standard mathematics that a search will turn up so the page claims no new result. The value of the page is the plain-language route and the picture of each number as a painter with a small rate. A program rechecked every figure (the file reciprocal_questions_check.py in the folder boring-things/research-program-files/prime-richness-scripts) and no other person has reviewed the page yet.

## Question: is "take 1 over the number" another realm with its own round trip the way the logarithm is?

Yes in two different ways.

**The reciprocal as a realm.** Go in by taking 1 over each number. Add. Go back out by taking 1 over the result. One painter finishes a fence in 3 hours and another in 6 hours. Going in gives rates of 1/3 and 1/6 of a fence per hour. Adding gives 1/2. Going back out gives 2 hours working together.

Any reversible machine makes a realm of this kind and each realm turns a different outside operation into addition.

- The logarithm realm turns multiplying into adding.
- The reciprocal realm turns "product divided by sum" into adding.
- The squaring realm turns the long side of a right triangle into adding (3 squared plus 4 squared unpacks to 5).

The logarithm is special because the operation it converts is multiplication which is a rung of the main ladder of operations.

**Steps and totals.** The step from 1/3 to 1/4 is 1/12 so the steps of the reciprocals are the "1 over neighbors multiplied" terms. The step from the natural logarithm of 100 to the natural logarithm of 101 is 0.00995 which is close to 1/100 so the steps of the logarithm are close to the reciprocals. That makes a chain.

- Adding up 1/(5 × 6) + 1/(6 × 7) + … without end rebuilds the reciprocal 1/5.
- Adding up reciprocals rebuilds a logarithm.
- Adding up logarithms rebuilds the logarithm of 1 × 2 × 3 × … up to the top number.

So "take steps" and "add up" are a second pair of opposite machines. The pair "squeeze" and "unpack" changes which operation is in play. The pair "steps" and "totals" moves along the ladder of sums.

**Where the two pairs meet.** For a factor close to 1 the logarithm and the reciprocal announcement are nearly the same number. The natural logarithm of (1 − 1/101) is −0.00995 and −1/101 is −0.00990. That is why sums of reciprocals keep producing logarithms.

**The reciprocal seen from the logarithm side.** Taking 1 over a number flips the sign of the logarithm (the natural logarithm of 1/5 is −1.609). So the reciprocal is a mirror flip on the logarithm side which is why the reciprocal undoes itself.

**A limit on the likeness.** A product in the bottom of a fraction turns into a subtraction of reciprocals only when the gap between the two numbers is supplied. 1/3 − 1/5 equals 2 divided by 15 and the 2 is the gap. The logarithm never needs an extra piece of that kind.

## Question: how does the painter problem work step by step?

Two painters paint one fence. The first would take 3 hours alone and the second would take 6 hours alone.

The hours cannot be added. 3 + 6 = 9 hours would be the time to paint two fences one after the other. Two painters on one fence finish faster than either alone so the answer is below 3 hours.

- Going in: the first painter covers 1/3 of the fence each hour and the second covers 1/6.
- Working inside: in any one hour the fence gains 1/3 + 1/6 = 1/2.
- Going back out: half a fence each hour means 2 hours for the whole fence.
- Check: in 2 hours the first painter covers 2/3 and the second covers 1/3 which makes 1 fence.

More cases: two painters who each take 6 hours finish in 3 hours. Three painters who take 2 and 3 and 6 hours finish in exactly 1 hour because 1/2 + 1/3 + 1/6 = 1.

A time is "hours per fence" and a rate is "fence per hour". Quantities written as "something per hour" add when things happen during the same hours. The reciprocal moves a quantity into the form that adds.

## Question: where does "product divided by sum" come from?

Adding two fractions needs a shared bottom and the handy shared bottom is the product. 1/3 is 6/18 and 1/6 is 3/18 so 1/3 + 1/6 = 9/18. The top 9 is the sum 6 + 3 and the bottom 18 is the product 3 × 6. So the combined rate is "sum over product" and flipping gives the combined time as "product over sum": 18 divided by 9 = 2.

- 4 hours and 12 hours give 48 / 16 = 3 hours.
- 10 hours and 10 hours give 100 / 20 = 5 hours.
- 2 hours and 1000 hours give 2000 / 1002 = 1.996 hours so a very slow helper barely changes the result.

The answer is always below the smaller time and the faster painter dominates because a small time is a big rate.

The rule gives a kind of average. Two identical painters who finish together in 2 hours would each take 4 hours alone so 4 is the "rate average" of 3 and 6 while the plain average is 4.5. Driving out at 60 and back at 30 over equal distances gives an average speed of 40 and not 45 for the same reason.

## Question: how do the painters relate to counting primes?

Each number on the line acts as a painter who contributes a small share of one prime.

Near a number N the typical gap between primes is the natural logarithm of N. The gap is "numbers per prime" which matches hours per fence. The flip is 1 divided by the natural logarithm which is "primes per number" and matches fence per hour. Gaps cannot be added to get a count. Rates can because each number walked past hands over its own rate for one step.

**The painters from 10 to 20.** The rates are 0.434 and 0.417 and 0.402 and 0.390 and 0.379 and 0.369 and 0.361 and 0.353 and 0.346 and 0.340 and 0.334. The rates add to 4.12. The primes in that stretch are 11 and 13 and 17 and 19 which is 4 primes. Going back out: 11 numbers divided by 4.12 gives 2.67 numbers per prime and the true figure is 2.75.

**Longer stretches.** From 2 to 997 the rates add to 177.0 against the true 168. From 2 to one million the rates add to 78627 against the true 78498.

**The master lists use the same painters on different numbers.** For a recipe the painters are the outputs. Take n² + n + 41 for n from 0 to 9. The outputs are 41 and 43 and 47 and 53 and 61 and 71 and 83 and 97 and 113 and 131. The rates are 0.269 and 0.266 and 0.260 and 0.252 and 0.243 and 0.235 and 0.226 and 0.219 and 0.212 and 0.205 which add to 2.39. Plain numbers of those sizes would be expected to yield 2.39 primes and the recipe yields 10. Ten divided by 2.39 is 4.19 which reads as +319% for that tiny sample. The "chance" figure on each line of [ranked-list.md](ranked-list.md) is that sum of rates.

**Where the picture bends.** A painter paints a steady share each hour while a number is either prime or not. So each rate is a chance and the sum is an expected count which is why the lists carry a "give or take" figure.

## Question: is some kind of smoothing going on?

Yes. Each number is either prime or not so the true record along the number line is a jagged string of yes and no. Between 1000 and 1100 exactly 16 numbers are prime (16%) while 1 divided by the natural logarithm of 1050 is 14.4%. The rule "1 divided by the natural logarithm" is the jagged record averaged over a window. Swapping the jagged record for the smooth curve is what smoothing means in this setting.

Each rung of the ladder of sums smooths more.

- The count of primes below one million differs from the smooth estimate by about 129 primes which is about 0.16%.
- The sum of 1 over each prime below one million is 2.887328 and the smooth formula (the logarithm of the logarithm plus 0.2615) gives 2.887289. The difference is 0.00004.

A sum that weights each prime by 1/p barely notices any single large prime so the jaggedness washes out. The sum of 1 over each prime could not tell the real primes apart from numbers scattered at random with the rate 1 divided by the natural logarithm. The detail that makes the primes the primes lives in the jagged leftover.

The word "smooth" has a second meaning in this field. A number is called smooth when all of its prime pieces are small (720 is built only from 2 and 3 and 5).

## Question: does any of this connect with 1 + 2 + 3 + 4 + … and the value −1/12?

Yes. The −1/12 belongs to the same family as the gap constant 0.5772 because both are a fixed leftover after the growing part of a sum is taken away.

The sum 1 + 2 + 3 + 4 + … grows without limit in the ordinary sense. The −1/12 is the constant that is left when the growing part is separated out by smoothing.

All of these sums belong to one family: 1 divided by n raised to a power s added over every n. The dial at 2 gives 1 + 1/4 + 1/9 + … which settles at 1.645. The dial at 1 gives the reciprocal sum. The dial at 0 gives 1 + 1 + 1 + … with a leftover constant of −1/2. The dial at −1 gives 1 + 2 + 3 + … with a leftover constant of −1/12. For dial settings above 1 that family equals the sieve product over the primes which is why the family carries the prime information.

A proven rule links the value at a dial setting s to the value at the setting 1 − s. The setting −1 is tied to the setting 2 and the numbers agree: −1.645 divided by (2 × pi × pi) = −0.0833 = −1/12. The middle of that mirror is the setting 1/2 which is the critical line.

## Question: what are the faded sum and the smooth part?

Chopping means adding 1 + 2 + 3 + … up to a stopping point and cutting off dead. Chopping at 10 gives 55 and chopping at 100 gives 5050. Fading means every term stays and each term gets turned down by a dimmer that sinks gently toward zero.

The dimmer for the term n is 1/e raised to the power (n divided by 10) so each step along the sum is one tenth of a division by e.

- At n = 1 the dimmer is 0.905 and the dimmed term is 0.905.
- At n = 5 the dimmer is 0.607 and the dimmed term is 3.03.
- At n = 10 the dimmer is 0.368 and the dimmed term is 3.68 which is the largest.
- At n = 20 the dimmer is 0.135 and the dimmed term is 2.71.
- At n = 50 the dimmer is 0.0067 and the dimmed term is 0.34.
- At n = 100 the dimmer is 0.000045 and the dimmed term is 0.0045.

The whole endless dimmed sum totals 99.9167. The smooth part is the same quantity poured smoothly instead of added in whole-number steps which is the area under the curve "n times the dimmer" and that area is 10 squared = 100. The chunky sum falls short of the smooth pour by 0.0833 = 1/12.

- With "n divided by 10" the sum is 99.9167 and the smooth part is 100.
- With "n divided by 100" the sum is 9999.9167 and the smooth part is 10000.
- With "n divided by 1000" the sum is 999999.9167 and the smooth part is 1000000.

The smooth part grows without limit and the −1/12 stays put. Chopping hides the constant because chopping at N gives half of N squared plus half of N and the "half of N" piece from the abrupt edge swamps any small constant.

The same fade applied to 1 + 1 + 1 + … with "n divided by 10" gives 9.5083 against a smooth part of 10 and the leftover heads to −1/2 as the dimmer gets gentler. With the strongest dimmer (one full division by e per step) the faded 1 + 1 + 1 + … is 1/e + 1/e² + 1/e³ + … = 0.5820. That number breaks apart as 1 − 1/2 + 1/12 − 1/720 and so on (the first four pieces give 0.5819) so 0.5820 holds both the −1/2 and the 1/12.

## How the questions tie back to the lists

- The "chance" figure on each line of the master lists is a sum of painter rates taken over the outputs of a recipe.
- The percentage on each line is the true count of primes measured against that sum.
- The rule 1 divided by the natural logarithm is a smoothed record so short samples can sit well above or below the rule by luck which is why each line carries the odds that luck explains the result.
