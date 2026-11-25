# How much does knowing the answer shrink a search? Step counts from mazes and delivery routes

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026 from a back and forth chat with the author of this repository. The author asked how much knowing the solution to a problem helps a solver rebuild the steps and whether the help is like lowering an exponent. The chatbot wrote the programs and ran the counts. The counts are measurements from the programs in the folder boring-things/research-program-files/delivery-routes-scripts/known-answer-scripts. The ideas behind the solvers are standard textbook methods and the step counts are fresh measurements. No other person has reviewed the page yet.

## Short answer

The savings depend on the shape of the problem and on which piece of the answer the solver holds.

- In a branching maze a solver who knows where the exit is cuts the exponent of the work roughly in half.
- In a flat maze the same knowledge saves a fixed factor of about 2 and a sense of direction saves a factor of about 9 to 16.
- In a delivery route search a solver who knows the exact best distance saves a factor of about 10 to 35 while the work still multiplies by about 3.3 for each added city.
- A rough hint (a distance 10% above the best) saved almost nothing in the delivery route search.

## Test 1: a branching maze

The maze is a random network of 3 million rooms where every room has 4 doors. The number of rooms within reach roughly triples with every step. A "step" in the tables is one room opened.

- The blind solver searches outward from the start and asks "is this the exit?" at every room.
- The two-end solver knows which room is the exit and searches from the start and from the exit until the two searches meet.

Both solvers find a shortest route. Each line is an average over 25 pairs of rooms.

- Exit 4 doors away: blind 115 steps and two-end 10 steps (11 times fewer).
- Exit 6 doors away: blind 955 steps and two-end 34 steps (28 times fewer).
- Exit 8 doors away: blind 8108 steps and two-end 106 steps (76 times fewer).
- Exit 10 doors away: blind 75700 steps and two-end 322 steps (235 times fewer).
- Exit 12 doors away: blind 618678 steps and two-end 970 steps (638 times fewer).
- Exit 14 doors away: blind 2464841 steps and two-end 2913 steps (846 times fewer).

The exponent of the two-end count divided by the exponent of the blind count stayed between 0.49 and 0.54 for every distance from 3 to 14 doors. So knowing the exit turned a count like 3 to the power d into a count like 3 to the power d ÷ 2 which is the square root. The line for 14 doors understates the savings because the blind solver had already opened most of the 3 million rooms and ran out of maze.

## Test 2: a flat maze

The maze is a square grid where 30% of the squares are walls. The number of squares within reach grows like the distance squared and not like a power with the distance in the exponent. A third solver named compass knows the position of the exit and always opens the square with the lowest total of steps walked plus straight-line steps left.

- Route of about 25 steps: blind 544 steps and two-end 235 steps and compass 61 steps.
- Route of about 50 steps: blind 1998 steps and two-end 878 steps and compass 169 steps.
- Route of about 100 steps: blind 8648 steps and two-end 3767 steps and compass 711 steps.
- Route of about 200 steps: blind 33044 steps and two-end 15378 steps and compass 2054 steps.
- Route of about 400 steps: blind 130759 steps and two-end 62549 steps and compass 8501 steps.

The two-end solver saved a factor of 2.1 to 2.3 at every size because two circles of half the radius cover half the area of one full circle. The compass solver saved a factor of 9 to 16 because the compass solver searches a narrow band toward the exit. So in a flat world the same knowledge is worth a fixed factor and not a change in the exponent.

## Test 3: a delivery route with the best distance handed over

Cities are random points in a square and the goal is the shortest round trip (the puzzle often called the traveling salesman problem). A "step" is one partial route extended by one city.

- The blind solver tries every ordering.
- The learner drops a partial route when the distance so far plus the cheapest possible finish cannot beat the best full route found so far.
- The told solver works like the learner and also receives the true best distance at the start and stops at the first route that matches.
- The rough hint solver receives a distance 10% above the true best.
- Checking a route that someone hands over takes one step for each city.

Each line gives the typical count (the geometric mean over 6 to 30 random maps).

- 8 cities: blind 13699 steps and learner 936 steps and rough hint 929 steps and told 95 steps.
- 9 cities: blind 109600 steps and learner 1963 steps and rough hint 1956 steps and told 130 steps.
- 10 cities: blind 986409 steps and learner 5111 steps and rough hint 5072 steps and told 276 steps.
- 11 cities: blind 9864100 steps and learner 14871 steps and rough hint 14864 steps and told 429 steps.
- 12 cities: blind 108505111 steps and learner 22031 steps and rough hint 20989 steps and told 753 steps.
- 13 cities: blind 1302061344 steps and learner 258751 steps and rough hint 258715 steps and told 20176 steps.

What the counts show:

- The told solver needed 10 to 35 times fewer steps than the learner.
- From 7 to 13 cities the steps multiplied by about 3.3 for each added city for the learner and for the told solver alike while the blind count multiplied by about 9.3. So knowing the best distance divided the work by a factor and left the growth rate where the growth rate was.
- The rough hint saved less than 5% because the learner finds a route within 10% of the best almost at once by visiting the nearest city first.
- The told solver saves the most in the last phase. The learner must keep searching after finding the best route to confirm that no shorter route exists and the told solver stops the moment a route matches the known distance.

The line for 13 cities rests on 6 maps so the jump in that line is partly luck of the draw.

## How the three tests fit together

- Knowing the endpoint is worth a square root when the search space branches and worth a factor near 2 when the search space is flat.
- Knowing the value of the best answer is worth a sizable fixed factor because the solver can skip the proof that nothing better exists.
- Holding the full answer drops the work to a simple check (13 steps for 13 cities against 258751 steps for the learner) although checking that the route is the best possible is a different and far more costly job.

## Weak points

- The delivery route solver uses a simple estimate for the cheapest possible finish and a stronger estimate would shrink every count and could change the factor between the learner and the told solver.
- The maps are small (7 to 13 cities) so the growth rates could drift for larger maps.
- The branching maze has 4 doors in each room and the flat maze has 30% walls and other settings were not tried.
