# Points for a perfect grid: sequences ranked by how many grid sizes they max out

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026. The author of this repository proposed the points rule and the chatbot wrote the programs and ran the counts. The programs are max_score_points.py and max_score_points_pairs.py and max_score_points_triples.py in the folder boring-things/research-program-files/prime-mazes-scripts. The page proves nothing about primes. No other person has reviewed the page yet.

## The points rule

Each room reads one number and opens one door: 0 and 4 and 8 open north. 1 and 5 and 9 open east. 2 and 6 open south. 3 and 7 open west. The numbers fill a square grid row by row starting at the top left room.

A sequence earns 1 point for each grid size where the sequence reaches the highest possible three part score. The highest possible score needs one line that passes through every room which also joins every room into one region and makes every outside door lead to the opposite side. A sequence that scores one short of the highest score on a grid earns no point for that grid.

One sequence is read on every grid size: the first 4 numbers fill the grid of 2 by 2 rooms and the first 9 numbers fill the grid of 3 by 3 rooms and so on. The grids run from 2 by 2 rooms to 12 by 12 rooms so 11 points are possible. The digits written below are door numbers (0 north and 1 east and 2 south and 3 west).

## The ranking

### 11 points of 11: shapes that are redrawn for each grid size (listed for comparison)

- The spiral earns a point on every grid size.
- The zigzag earns a point on every grid size.

These two are not one fixed sequence because the numbers are chosen again for each grid size. Every entry below is one fixed sequence.

### 2 points: the most any fixed sequence earned

- Repeating block 110030: maxes 2 by 2 rooms and 3 by 3 rooms.
- Repeating block 110033: maxes 2 by 2 rooms and 3 by 3 rooms.
- Repeating block 11100333: maxes 2 by 2 rooms and 4 by 4 rooms.
- Repeating block 23331112: maxes 2 by 2 rooms and 4 by 4 rooms.
- Sequence 2332120331120333: maxes 3 by 3 rooms and 4 by 4 rooms.
- Sequence 2332120333120333: maxes 3 by 3 rooms and 4 by 4 rooms.
- Sequence 2332120333230330: maxes 3 by 3 rooms and 4 by 4 rooms.
- Sequence 2332121023031110: maxes 3 by 3 rooms and 4 by 4 rooms.
- Sequence 2332121123031110: maxes 3 by 3 rooms and 4 by 4 rooms.

Exactly 53 sequences of 9 numbers max both 2 by 2 rooms and 3 by 3 rooms and exactly 6 sequences of 16 numbers max both 3 by 3 rooms and 4 by 4 rooms.

### 1 point

- 15632 repeating blocks of 8 doors or fewer max 2 by 2 rooms and no other size. The shortest is the block 03.
- 76 repeating blocks max 3 by 3 rooms and no other size. The shortest is the block 033010.
- 2 repeating blocks max 4 by 4 rooms and no other size. The shortest is the block 03331110.
- The digits of the primes written in one row: maxes 2 by 2 rooms.
- The digits of e: maxes 2 by 2 rooms.
- The digits of the square root of 2: maxes 2 by 2 rooms.
- The one whole prime in each room: maxes 2 by 2 rooms.
- The square numbers with one whole number in each room: maxes 2 by 2 rooms.

### 0 points

- The digits of pi.
- The digits of the counting numbers written in one row.
- The counting numbers with one whole number in each room.
- The Fibonacci numbers with one whole number in each room.
- Every other repeating block of 8 doors or fewer (the program tested all 87380 blocks and 15714 different repeating patterns earned at least 1 point).

## Limits the search found

- **No sequence maxes 2 by 2 and 3 by 3 and 4 by 4 rooms together.** The program checked all 53 sequences that max the first two sizes and none can be continued to max the third.
- **No sequence maxes 3 by 3 and 4 by 4 and 5 by 5 rooms together.** The program checked all 6 sequences that max the first two of those sizes and none can be continued.
- **No repeating block of 8 doors or fewer maxes any grid larger than 4 by 4 rooms.**
- **Perfect grids are rare.** 46 of the 256 door patterns max 2 by 2 rooms (18%) and 504 of the 262144 door patterns max 3 by 3 rooms (0.19%).

The reason fixed sequences do so poorly is that a wider grid cuts the same sequence into rows at different places. A hallway that works for rows of 3 rooms is chopped apart when the rows are 4 rooms long.

## The open question

The chatbot did not find any fixed sequence that earns 3 points and did not prove that 3 points are impossible. Sets of sizes that skip a size (such as 2 by 2 and 4 by 4 and 6 by 6 rooms) were not searched completely because the number of door patterns grows too fast.

## Weak points

- The search for sequences that max 2 by 2 and 4 by 4 rooms ran out of time so the two repeating blocks listed for that pair are examples and not a full count.
- Repeating blocks longer than 8 doors were not tested.
- Each well known sequence was read from its first number.
- The rule gives no credit for a near miss so a sequence that scores 239 of 240 counts the same as a sequence that scores 20.
