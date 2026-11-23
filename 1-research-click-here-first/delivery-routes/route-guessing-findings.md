# Delivery route guessing tests

> **About this page:** An AI chatbot (Claude) wrote this page and ran the tests on 23 November 2026 after the author of this repository asked how close 10000 guesses land to the shortest possible delivery route. No other person has rechecked the page. The programs that produced every number sit in the folder boring-things/research-program-files/delivery-routes-scripts so anyone can rerun the tests.

## The question

A delivery route problem (often called the traveling salesman problem) asks for the shortest loop that visits every stop once and returns to the starting stop. The number of possible loops grows explosively because each added stop multiplies the count of loops. The question tested here is how close a person or program lands to the shortest loop by making 10000 guesses and keeping the shortest guess.

## Test 1: 10000 completely random routes

Each test built 10000 random loops and kept the shortest random loop so the shortest random loop could be compared against the proven shortest loop. The small problems used randomly placed stops with the shortest loop proven by an exact method. The larger problems are standard public benchmark problems (eil51 and berlin52 and kroA100 and ch150 and a280) whose shortest loops are already proven.

How much longer the best of 10000 random loops was than the proven shortest loop:

- 6 stops: 0% longer because only 60 distinct loops exist
- 8 stops: 0% longer because only 2520 distinct loops exist
- 10 stops: 4% longer
- 12 stops: 15% longer
- 14 stops: 21% longer
- 20 stops placed on a circle: 174% longer
- 30 stops placed on a circle: 363% longer
- 51 stops (eil51): 207% longer
- 52 stops (berlin52): 209% longer
- 100 stops (kroA100): 551% longer
- 150 stops (ch150): 616% longer
- 280 stops (a280): 1092% longer which means about 12 times the shortest length

Random guessing stops working past roughly 12 stops because 10000 guesses become a vanishing sliver of all possible loops. At 52 stops the 10000 guesses cover about 1 loop out of every 10 to the 62nd power so the best random guess (209% longer) barely beats an average random guess (297% longer).

## Two meanings of "the best 10% of answers"

The phrase "best 10% of answers" can mean two separate targets and the difference matters because one target is trivial and the other target is strict.

- Ranking in the top 10% of all loops is trivial because a single random guess lands in the top 10% one time out of ten.
- Landing within 10% of the shortest length is strict because nearly all loops are far longer than the shortest loop. The best of 10000 random loops for 100 stops ranks around the top 0.01% of all loops and that loop is still about 6.5 times the shortest length since the short loops sit in an extremely thin tail.

## Test 2: one simple rule added to the guessing

The added rule builds each loop one stop at a time by driving to the nearest unvisited stop 9 times out of 10 and to the second-nearest unvisited stop 1 time out of 10. The rule adds almost no complexity because each step only compares distances from the current stop.

How much longer the best of 10000 rule-built loops was than the proven shortest loop:

- 12 stops: 0% longer (blind random was 15% longer)
- 14 stops: 0% longer (blind random was 21% longer)
- 51 stops: 8% longer (blind random was 207% longer)
- 52 stops: 6% longer (blind random was 209% longer)
- 100 stops: 13% longer (blind random was 551% longer)
- 150 stops: 9% longer (blind random was 616% longer)
- 280 stops: 15% longer (blind random was 1092% longer)

The nearest-stop rule works because the rule throws away nearly all terrible loops before any guessing happens. Blind random loops zigzag across the whole map on almost every leg whereas short loops almost always link stops with close neighbors so guessing among close-neighbor loops concentrates the 10000 guesses where short loops live.

## How much randomness helps

Four versions of the nearest-stop rule were tested with 10000 loops each because the amount of randomness changed the results a great deal. The percentages run in the order 51 stops then 52 stops then 100 stops then 150 stops then 280 stops.

- Always the nearest stop with only the starting stop random: 13% and 8% and 16% and 9% and 15% longer. The always-nearest version wastes most of the 10000 guesses because each starting stop produces one fixed loop so 52 stops give only 52 distinct loops.
- Nearest stop 9 times out of 10: 8% and 6% and 13% and 9% and 15% longer. The 9-out-of-10 version won or tied on every benchmark because the occasional second-nearest choice creates thousands of distinct short loops.
- Coin flip between the two nearest stops: 14% and 21% and 34% and 37% and 53% longer.
- Random pick among the three nearest stops: 36% and 39% and 63% and 69% and 80% longer.

More randomness lengthened the loops on the large problems because each second-rate choice adds extra distance and a 280-stop loop with a coin flip per step piles up about 140 second-rate choices.

## A repair method for comparison

A repair method starts from one random loop and repeatedly uncrosses pairs of road segments that cross each other until no uncrossing shortens the loop. One run of the repair method landed 9% to 17% longer than the shortest loop on the benchmark problems. On 52 stops the repair method used about 6400 small checks which means less effort than 10000 random guesses while landing at 16% longer where blind random guessing landed at 209% longer.

## What the tests suggest

- Effort matters less than where the effort goes because 10000 blind guesses and 10000 rule-built guesses cost similar computing work while the rule-built guesses finish about 25 to 70 times closer to the shortest loop on the benchmark problems.
- Finding a loop that is close to the shortest loop is a different and easier problem than finding the exact shortest loop for map-style distances because simple methods reach within about 10% without the work doubling per added stop.
- The 9-out-of-10 rule stalls around 6% to 15% longer because a driver who always grabs a nearby stop strands faraway stops and must make long return trips near the end of the loop. Closing the remaining gap needs a repair step such as uncrossing road segments.

## Limits of these tests

Each number is from one run with one random seed so a rerun with another seed can shift each percentage by a few points. The repair method was run once per problem from a single random starting loop. The benchmark problems all use straight-line map distances so the results might not carry over to route problems whose distances follow no map logic (for example a detour that costs less than the direct path).
