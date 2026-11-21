# Later prime richness findings

> **About this page:** One AI model (Claude) ran the computations and wrote this page in a single chat on 21 November 2026. No other person has rerun the work yet which means the results are unconfirmed by a human reviewer. Each result comes from a computer count and not from a written proof unless the section says a proof exists.

## What the page is for

The page continues the page [new-findings.md](new-findings.md) with results from later in the same chat. Each section holds a result that the chatbot could not state from memory before computing and that a quick web search did not turn up on 21 November 2026. A result missing from a quick search can still sit inside a research paper so the page claims "not quickly searchable" and does not claim "new to mathematics".

Every percentage compares a recipe with plain counting numbers of the same size so +150% means 2.5 times as many primes as the number line and −100% means no primes. A prime that a recipe outputs more than once counts once.

The pages [ranked-list.md](ranked-list.md) and [grouped-list.md](grouped-list.md) hold every line with the raw counts.

## The ceiling when every output is prime

An ordinary number with d digits has about a 1 in 2.3 × d chance of being prime. So a recipe whose outputs are all prime beats the number line by a factor of about 2.3 × d which gives about +1300% for 7-digit outputs and about +2700% for 13-digit outputs and about +23000% for 100-digit outputs. A measured case: starting at 2 and adding the gaps between neighboring primes gives a prime at every step and landed at +1307% for totals up to 7 digits.

## Relative percentage against absolute share

The percentage on each line is relative to chance at the size of the outputs. The absolute share of outputs that are prime can be low while the percentage is high.

- n² + n + 26853927251 at +859%: 39% of the outputs were prime where chance predicts 4.1% (outputs of about 11 or 12 digits).
- (the product of every prime up to 1009) × n + 1 at +1108%: 1.2% of the outputs were prime where chance predicts 0.10% (outputs of about 425 digits).

## The best equation of the form n² + n + A with A below 900 billion

A computer search kept every A below 900 billion where no prime up to 47 can divide any output and then scored the survivors by which larger primes can divide an output. The best ones were then counted on every input from 1 to 300000.

- n² + n + 26853927251: +859% (116748 primes where chance predicts 12173). The smallest prime that can divide an output is 97.
- n² + n + 21425625701: +842%
- n² + n + 379580297267: +840%
- n² + n + 5384581877: +830%
- n² + n + 247757: +725% (the last entry of the public record list OEIS A331940 as a quick search showed the list on 21 November 2026)
- n² + n + 41: +564%

The four equations at the top beat the last entry of the public record list. The search did not record which A is the first one above 247757 to beat 247757 so the search does not give the next entry of the record list.

## The best starting number for a sum of multiples

A running sum that starts at c and adds 2a + 4a + 6a and so on has the total a × n² + a × n + c after n steps. A computer search over starting numbers below 200 billion (below 600 billion for the multiples of 6) found these:

- Start at 5660169547 then add 30 + 60 + 90 and so on: +865% (111218 primes in 300000 steps where chance predicts 11521)
- Start at 24600021781 then add 30 + 60 + 90 and so on: +861%
- Start at 100800448037 then add 210 + 420 + 630 and so on: +857%
- Start at 29717281333 then add 6 + 12 + 18 and so on: +854%

Start at 41 then add 2 + 4 + 6 and so on gives exactly the totals of n² + n + 41 which shows that the prime-rich squared equations are running sums of even numbers with a chosen starting number.

## Bumping the last digit of every output

The bump moves the last digit of a number up to the nearest of 1 or 3 or 7 or 9 so 0 becomes 1 and 2 becomes 3 and 4 or 5 or 6 becomes 7 and 8 becomes 9. The bump was applied to the outputs of 86 equations and the result sorts into three groups.

- The bump changes nothing when the outputs already end in 1 or 3 or 7 or 9. n² + n + 41 stays at +564% and 6n + 1 stays at +200% (an output of 6n + 1 that ends in 5 gets bumped to a multiple of 3).
- The bump adds a fixed 2.5 times to a recipe with no structure. The plain number line moves from −1% to +149% and all 17 recipes with square roots or π or e or logarithms land between +147% and +153%.
- The bump is unpredictable on a structured equation. n² − 1 moves from −100% to +5% while n² + n + 2 moves from −100% to +126%. n² ÷ 10 with decimals dropped moves from −45% to +180%. n⁴ + n² + 1 stays at −100% because every output is odd and no output ends in 5.

## Running sums with the bump carried into the next addition

A running sum was tested three ways: the plain total at each step and the total bumped for the test alone and the total bumped and then carried into the next addition. Each sum ran for 300000 steps.

- 1 + 2 + 3 + 4 and so on: −100% plain and +159% bumped and +222% with the bump carried
- 1 + 8 + 27 + 64 and so on (cubes): −100% plain and +185% bumped and +274% with the bump carried
- 1 + 4 + 9 + 16 and so on (squares): −100% plain and +35% bumped and +169% with the bump carried
- 1 + 9 + 25 + 49 and so on (odd squares): −100% plain and +38% bumped and +194% with the bump carried
- 1 + 16 + 81 + 256 and so on (fourth powers): −100% plain and −34% bumped and +150% with the bump carried
- 2 + 3 + 5 + 7 and so on (primes): −1% plain and +148% bumped and +149% with the bump carried

The carried totals of 1 + 2 + 3 run 1 then 3 then 7 then 11 then 17 then 23 then 31 then 39 then 49 then 59. After the first steps the bump adds exactly 1 at every second step so the totals lock onto two equations woven together: 2m² − 1 (1 and 7 and 17 and 31 and 49) and 2m² + 2m − 1 (3 and 11 and 23 and 39 and 59). Neither equation has an even output or an output ending in 5.

The starting number matters for the carried sum. Among the starting numbers 0 to 600 the best start for 1 + 2 + 3 with the bump carried was 28 at +322% and the worst start landed at +23%.

Adding 1 over and over with the bump carried walks through every number ending in 1 or 3 or 7 or 9. That walk found 60236 primes in 300000 steps which is every prime above 5 below the last total and the percentage is +150%. Adding 2 or 3 or 6 or 7 over and over with the bump carried gives +150% as well.

Adding up the gaps between neighboring primes gives totals that are each a prime minus 2. The plain totals landed at +33% because a total is prime exactly when the two primes are a twin pair. The recipe needs the list of primes so the recipe is circular.

## Rounding rules for n² ÷ k

Each line gives the percentage for four rounding rules in the order: decimals dropped then decimals of 0.3 or more go up then decimals of 0.5 or more go up then any decimals go up.

- n² ÷ 2: −100% then +37% then +37% then +36%
- n² ÷ 3: −100% then −6% then −100% then −6%
- n² ÷ 4: −100% then −100% then −100% then +13%
- n² ÷ 5: −100% then −28% then −27% then +45%
- n² ÷ 6: −30% then −6% then −7% then +65%
- n² ÷ 7: −37% then +1% then +1% then −19%
- n² ÷ 8: −100% then −32% then −31% then +66%
- n² ÷ 9: −67% then −44% then −69% then −13%
- n² ÷ 10: −44% then +25% then −14% then +73%
- n² ÷ 11: −37% then −4% then −21% then +6%
- n² ÷ 12: −100% then +2% then −43% then +72%

Rounding any decimals up beat dropping the decimals for every k from 2 to 12. Dropping the decimals subtracts the remainder and the remainder of a square is often a square such as 1 or 4 or 9 and a square minus a square splits into two factors (n² − 4 equals (n − 2) × (n + 2)). Rounding up adds a number and a square plus a number does not split that way.

A scrambled recipe ignores the rounding rule. n × π landed at 0% under all three rounding rules tested.

## Trig functions and modulus and the repeat rule

- Recipes such as n × |sin(n)| and n² × |sin(n)| and n × |tan(n)| and n ÷ |sin(n)| with decimals dropped landed within 2 points of 0%.
- Adding a wave to a prime-rich equation removes most of the edge. n² + n + 41 sits at +564% and n² + n + 41 + 10 × sin(n) with decimals dropped landed at +8%.
- Taking a remainder removes the edge as well. n² + n + 41 mod 1000000007 landed at 0%.
- n × (n mod 7) + 1 landed at +109%.
- The known formula 2 + (2 × n!) mod (n + 1) outputs nothing except primes. With a repeated prime counted once the formula landed at −91% because the output is 2 for almost every input. The formula finds exactly the primes that counting 1 2 3 4 5 finds with the same count of inputs.

## Growing runs of digits from constants and from the zeta sum

The recipe takes the first digit of a constant and then the first two digits and so on (3 then 31 then 314 for π). For π and e and the golden ratio and √2 and √3 and ln 2 the first 1200 such numbers gave 23 primes in total where chance predicts 21. With the last digit bumped the same six constants gave 50 primes.

The same idea on the zeta sum (the first n decimal digits of the piece 1/nˢ and the first n digits of the running total up to 1/nˢ for s = 1 and 2 and 3 and positions 1 to 2000) gave 21 primes where chance predicts 22.5 and gave 52 primes with the bump. So digits pulled from these constants and sums behave like random digits for primes and the bump adds roughly the usual 2.5 times.

## Long-run percentages for equations known for other records

A quick search finds these equations with their record runs of primes and did not turn up their long-run percentages. Each equation was counted on inputs 1 to 300000.

- −66n³ + 3845n² − 60897n + 251831: +747%
- 45n⁴ − 3416n³ + 96738n² − 1212769n + 5692031: +727%
- 6n⁴ − 558n³ + 19354n² − 296370n + 1688311: +706%
- 103n² − 4707n + 50383: +704%
- 36n² − 810n + 2753: +683%
- 43n² − 537n + 2971: +664%
- 47n² − 1701n + 10181: +654%
- 8n² − 488n + 7243: +634%
- 2n² − 108n + 1259: +632%
- 3n³ − 183n² + 3318n − 18757: +615%

Equations known for very few primes:

- n¹² + 488669: 0 primes in 300000 inputs where chance predicts 2174
- n⁶ + 29450922301244534: −99% (26 primes where chance predicts 4344)
- n⁶ + 1091: −97% (132 primes where chance predicts 4348)

Powers of n plus 1 and related equations:

- n⁴ − n² + 1: +363%
- n⁶ + n⁵ + n⁴ + n³ + n² + n + 1: +346%
- n³² + 1: +267% and n¹⁶ + 1: +265% and n⁸ + 1: +110%

Recipes that start from the nth prime: the nth prime + 2 landed at +33% and + 6 at +163% and + 30 at +252% and + 210 at +322% and + 2310 at +370% and + 30030 at +412%. (The nth prime)² − 2 landed at +239%.

## Two number lists with a surprising prime rate

The partition number for n counts the ways to split n into a sum. Among the first 20000 partition numbers the computer found 82 primes where chance predicts 124 which is −34% and luck alone gives a gap that large about 1 time in 15000. A likely cause is the known pattern where every fifth partition number is a multiple of 5 with similar patterns for 7 and 11.

The top number of the fraction 1 + 1/2 + 1/3 up to 1/n was prime 30 times in the first 682 fractions where chance predicts 6.9 which is +333% and the luck odds are under 1 in a billion. A likely cause is that each small prime divides very few of those top numbers which a paper at https://arxiv.org/abs/2503.15714 studies.

## Invented recipes

About 55 recipes were made up for the test so no search would hold their results. The clearest ones:

- The largest prime that divides n² + 1: +796% (70780 different primes from 100000 inputs and the recipe needs a factoring step)
- (The nth prime)² + the nth prime + 41: +579% and n² + n + 41 fed back into itself: +569%
- n² + 1 with every factor of 2 and 5 divided out: +358%
- The count of grid points inside a circle of radius n: +102% because the count is odd for every radius
- The most pieces from n straight cuts of a pizza: +97% and the most pieces from n flat cuts of a cake: −100% because the cake formula splits into factors
- n + (n written backward): −99% because the result is a multiple of 11 when n has an even count of digits
- n² combined with n by the exclusive-or rule on binary digits: −100% because n² and n are both even or both odd
- The halfway point between the nth prime and the next prime: −100% because the halfway point sits strictly between two neighboring primes
- n written in base 2 and then read as a base 10 number: +15% and n written in base 3 and then read as a base 10 number: −20%
- Start at 1 and keep adding the smallest prime that does not divide the current number: +100%

## A jump rule whose every jump is prime

A known rule starts at 7 and at step n adds the largest number that divides both n and the running value. In 3 million steps the jump was 1 for all but 81 steps. Each of the 81 other jumps was prime and the 81 jumps held 31 different primes. So the rule never jumps by a non-prime above 1 and still finds far fewer primes than counting 1 2 3 4 5 does.

## Equations with no numbers in them

A one-variable equation with no numbers at all is a multiple of x for every input so such an equation has no primes. For example x³ + x² + x equals x × (x² + x + 1).

With two or three variables and no numbers each recipe got 300000 random inputs. The highest were x¹⁶ + y¹⁶ at +196% and x³ + x² × y + y³ at +115% and x³ + x × y + y³ at +109% and x × y + x + y at +94% and x² + x × y + y² at +66% and x² + y² at +28%. Recipes such as x³ + y² and x² + y² + z² and x³ + y³ + z³ landed within 2 points of 0%. Recipes such as x³ + y³ and x⁴ + x² × y² + y⁴ and x² + y² + x + y landed at −100% because the first two split into factors and the third is even for every input.

With one variable and every coefficient equal to 1 and a lone + 1 at the end a complete search scored all 65535 equations up to the 16th power by which small primes can divide the outputs. The best ones were then counted on inputs 1 to 300000.

- x¹⁴ + x¹³ + x¹² + x¹⁰ + x⁹ + x⁷ + x⁵ + x⁴ + x² + x + 1: +637% (13742 primes where chance predicts 1864)
- x¹⁶ + x¹⁵ + x¹³ + x¹¹ + x¹⁰ + x⁸ + x⁶ + x⁵ + x³ + x + 1: +603%
- x¹⁵ + x¹¹ + x¹⁰ + x⁹ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1: +563%
- x⁶ + x⁵ + x⁴ + x³ + x² + x + 1: +346% and x¹⁶ + 1: +265% and x² + x + 1: +123% and x² + 1: +37% (simple members of the same family for comparison)

So an equation with no large number anywhere can still reach +637% because the choice of which powers are present blocks small primes the way a hand-picked large number does. The best equations sit near the top of the searched range so a search past the 16th power would probably find higher percentages.

## Bumping recipes that give no primes

The bump was applied to recipes that sit at or near −100%. Each line gives the percentage before the bump and after the bump (300000 inputs each).

- the most pieces from n flat cuts of a cake: −100% plain and +182% bumped
- n × (n + 1) ÷ 2 (the totals of 1 + 2 + 3): −100% plain and +159% bumped
- n¹² + 488669: −100% plain and +155% bumped
- n² ÷ 12 with decimals dropped: −100% plain and +154% bumped
- the halfway point between the nth prime and the next prime: −100% plain and +154% bumped
- n² combined with n by the exclusive-or rule: −100% plain and +150% bumped
- n² ÷ 8 with decimals dropped: −100% plain and +147% bumped
- x × y: −100% plain and +143% bumped
- n² ÷ 2 with decimals dropped: −100% plain and +134% bumped
- n² + n + 2: −100% plain and +127% bumped
- n⁶ + 1091: −97% plain and +121% bumped
- n² ÷ 5 with decimals dropped: −100% plain and +121% bumped
- n² ÷ 16 with decimals dropped: −100% plain and +119% bumped
- n² ÷ 4 with decimals dropped: −100% plain and +110% bumped
- 3n²: −100% plain and +105% bumped
- x² + y² + x + y: −100% plain and +105% bumped
- 2n: −100% plain and +100% bumped
- n² ÷ 3 with decimals dropped: −100% plain and +99% bumped
- n² + (n mod 6): −100% plain and +97% bumped
- n⁴ + 4: −100% plain and +81% bumped
- n⁶ + 1: −100% plain and +71% bumped
- x³ + y³: −100% plain and +65% bumped
- n written twice side by side: −100% plain and +56% bumped
- n followed by n written backward: −100% plain and +44% bumped
- the totals of 1² + 2² + 3²: −100% plain and +35% bumped
- n³ ÷ 9 with decimals dropped: −100% plain and +26% bumped
- n² − 1: −100% plain and +5% bumped
- x⁴ + x² × y² + y⁴: −100% plain and −16% bumped
- 6n + 3: −100% plain and −25% bumped
- n + (n written backward): −99% plain and −94% bumped
- n⁴ + n² + 1: −100% plain and −100% bumped

A recipe sits at −100% because one reason covers every output such as "even for every input" or "splits into two factors". The bump nudges an output up by 1 or 2 or 3 and the nudged number no longer equals the factored form. A recipe whose structure is fully broken lands near +150% because a bumped number ends in 1 or 3 or 7 or 9.

n⁴ + n² + 1 stays at −100% because every output already ends in 1 or 3 or 7 or 9 so the bump changes nothing. n² − 1 reaches just +5% because the bump often adds exactly 1 and n² − 1 plus 1 is a perfect square. 2n reaches +100% because the endings 4 and 6 are both bumped to the same number ending in 7 and a repeated prime counts once.

n¹² + 488669 gave 0 primes in 300000 inputs before the bump and 5551 primes after the bump. So the lack of primes in that equation rests on an exact pattern of which small primes divide the outputs and the pattern does not survive a shift of 1 to 3 in the last digit.

## Stacking two ways of blocking small primes

n² + n + 26853927251 blocks every prime below 97 by the choice of the added number. Feeding the equation inputs that are multiples of the primes that can still divide an output blocks those primes as well because the output then leaves the same remainder as 26853927251 when divided by any of those primes.

- With the 11 such primes up to 300 folded into the input: +992% (7770 primes in 100000 tests where chance predicts 711 and outputs of about 62 digits)
- With the 52 such primes up to 1000 folded into the input: +1167% (1900 primes in 100000 tests where chance predicts 150 and outputs of about 292 digits)

The measured +1167% matched the predicted +1161%. About 1 of every 53 outputs was prime where ordinary numbers of about 292 digits give about 1 of every 670. The stacked recipe beat the +1108% of (the product of every prime up to 1009) × n + 1 while using shorter outputs.

## Changing the last digit to one fixed digit

The rule replaces the last digit of every output with one fixed digit. Each line gives the percentage for the plain outputs and for the usual bump (the last digit moves up to the nearest of 1 or 3 or 7 or 9) and then for the last digit changed to 1 and to 3 and to 7 and to 9. Each recipe ran on inputs 1 to 300000 in order.

- n: 0% plain and 0% with the usual bump and −75% to 1 and −75% to 3 and −75% to 7 and −75% to 9
- 10n: −100% plain and +150% with the usual bump and +150% to 1 and +150% to 3 and +150% to 7 and +150% to 9
- 2n: −100% plain and +100% with the usual bump and −50% to 1 and −50% to 3 and −50% to 7 and −50% to 9
- 6n: −100% plain and +200% with the usual bump and +50% to 1 and +50% to 3 and +50% to 7 and +50% to 9
- 30n: −100% plain and +275% with the usual bump and +275% to 1 and −100% to 3 and +275% to 7 and −100% to 9
- 210n: −100% plain and +338% with the usual bump and +338% to 1 and −100% to 3 and −100% to 7 and −100% to 9
- n²: −100% plain and +96% with the usual bump and +165% to 1 and +113% to 3 and +210% to 7 and +76% to 9
- n² − 1: −100% plain and +5% with the usual bump and +118% to 1 and +106% to 3 and +199% to 7 and +46% to 9
- n² + 1: +37% plain and +153% with the usual bump and +119% to 1 and +134% to 3 and +165% to 7 and +131% to 9
- n² + n: −100% plain and +123% with the usual bump and +228% to 1 and +91% to 3 and +159% to 7 and +70% to 9
- n² + n + 41: +564% plain and +564% with the usual bump and +272% to 1 and +302% to 3 and +222% to 7 and +145% to 9
- n² ÷ 2 with decimals dropped: −100% plain and +134% with the usual bump and +213% to 1 and +113% to 3 and +150% to 7 and +92% to 9
- n × (n + 1) ÷ 2: −100% plain and +159% with the usual bump and +229% to 1 and +148% to 3 and +173% to 7 and +157% to 9
- n³: −100% plain and −33% with the usual bump and +78% to 1 and +114% to 3 and +110% to 7 and +111% to 9
- n⁴ + 4: −100% plain and +81% with the usual bump and +7% to 1 and +211% to 3 and +107% to 7 and +99% to 9
- n × π with decimals dropped: 0% plain and +129% with the usual bump and −22% to 1 and −21% to 3 and −22% to 7 and −22% to 9
- n² × π with decimals dropped: −2% plain and +149% with the usual bump and +149% to 1 and +148% to 3 and +152% to 7 and +151% to 9
- 2ⁿ mod n then plus n²: −33% plain and +133% with the usual bump and +121% to 1 and +163% to 3 and +130% to 7 and +147% to 9

No digit wins for every equation. The digit 7 was the best fixed digit for n² (+210%) and n² − 1 (+199%) and n² + 1 (+165%). The digit 1 was the best for n² + n (+228%) and n × (n + 1) ÷ 2 (+229%) and n² ÷ 2 (+213%). The digit 3 was the best for n⁴ + 4 (+211%).

The main cause is the prime 3. For n² the changed numbers are multiples of 3 for 20% of the inputs when the digit is 1 or 7 and for 43% of the inputs when the digit is 3 or 9 where ordinary numbers are multiples of 3 for 33%. So the best digit for an equation is a digit that makes multiples of 3 rare for that equation.

Three more patterns show in the lines. For 30n the digits 1 and 7 give +275% and the digits 3 and 9 give −100% because 30n + 3 and 30n + 9 are multiples of 3. For 210n the digit 1 gives +338% and the digit 7 gives −100% because 210n + 7 is a multiple of 7. A fixed digit lowers n² + n + 41 from +564% to between +145% and +302% because changing the last digit breaks the blocking of small primes that the equation has.

A recipe whose outputs rise slowly does badly under a fixed digit because ten inputs in a row give the same changed number and a repeated prime counts once. The plain number line falls to −75% under any fixed digit while the usual bump keeps the plain number line at 0%.

The primes themselves show almost no preference for a last digit. Below 100 million there are 1440298 primes ending in 1 and 1440474 ending in 3 and 1440495 ending in 7 and 1440186 ending in 9. The digit 7 leads by about 2 primes in every 10000 and a proven theorem says the four shares become equal in the long run.

## The sample-size numbers on the master lists

Each line of the master lists carries the count of outputs tested and the count of primes found and the count chance predicts plus two guards against small samples. "Give or take" is 100 times the square root of the count of primes found divided by the count chance predicts. "Luck odds" is the chance that a count at least that far from the predicted count shows up when the true rate equals the number line rate and the odds are worked out with the standard formula for counts of rare events. A line is marked "the gap could be luck" when the luck odds are about 10 in 100 or more.

## Program files

The folder boring-things/research-program-files/prime-richness-scripts holds the Python files behind this page: quad_search.py and sum_search.py (the two searches) and equation_table_bump.py and running_sums.py and more_sums.py (the bump and the running sums) and wild_batch.py (rounding rules and trig and modulus and the digits of constants) and zeta_digits.py and meaty.py (equations known for other records and number lists) and weird.py (the invented recipes) and hybrid.py (the stacked recipe) and lastdigit.py (the last digit changed to one fixed digit) and no_numbers.py (equations with no numbers) and dead_bump.py (the bump on recipes with no primes) and master_list_indicators.py (the sample-size numbers).
