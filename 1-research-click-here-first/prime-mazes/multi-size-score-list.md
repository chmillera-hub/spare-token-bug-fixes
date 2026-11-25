# One pattern on many grid sizes: total three part scores for grids from 2 by 2 to 10 by 10 rooms

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026. The author of this repository asked for the experiments and the chatbot wrote the programs and ran the counts. The program is multi_size_scores.py in the folder boring-things/research-program-files/prime-mazes-scripts. The page proves nothing about primes. No other person has reviewed the page yet.

## What this list measures

Each room reads one number and opens one door: 0 and 4 and 8 open north. 1 and 5 and 9 open east. 2 and 6 open south. 3 and 7 open west. The numbers fill a square grid row by row starting at the top left room.

The three part score adds the largest region (the most rooms joined by open doors) and the longest walk (the most rooms one line can pass through without entering a room twice) and the door points. Every room on the edge of the grid is assumed to have a door to the outside that a player can open and a corner room has two. The player earns 1 door point for each outside door where the player can enter and walk through joined rooms to the opposite side of the grid.

Each entry is one pattern or one sequence scored on nine grids (2 by 2 rooms up to 10 by 10 rooms) and the nine scores are added. The highest possible total is 984 because the highest scores for the nine grids are 16 and 30 and 48 and 70 and 96 and 126 and 160 and 198 and 240.

Each line gives the total and then the nine scores in order from 2 by 2 rooms to 10 by 10 rooms.

## List 1: shapes that are redrawn for each grid size

1. Spiral (one hallway that winds into the center): total 984 of 984 (100%). Scores: 16 and 30 and 48 and 70 and 96 and 126 and 160 and 198 and 240
2. Zigzag (one hallway that snakes back and forth): total 984 of 984 (100%). Scores: 16 and 30 and 48 and 70 and 96 and 126 and 160 and 198 and 240
3. Comb (left column opens south and every other room opens west): total 744 of 984 (76%). Scores: 16 and 28 and 42 and 58 and 76 and 96 and 118 and 142 and 168
4. Nested rings (each layer of rooms is a clockwise loop): total 578 of 984 (59%). Scores: 16 and 30 and 40 and 52 and 64 and 76 and 88 and 100 and 112
5. Staircases (east then south over and over): total 252 of 984 (26%). Scores: 12 and 16 and 20 and 24 and 28 and 32 and 36 and 40 and 44
6. Rows (every room opens east): total 216 of 984 (22%). Scores: 8 and 12 and 16 and 20 and 24 and 28 and 32 and 36 and 40
7. Columns (every room opens south): total 216 of 984 (22%). Scores: 8 and 12 and 16 and 20 and 24 and 28 and 32 and 36 and 40
8. Bricks (pairs of rooms that open toward each other): total 40 of 984 (4%). Scores: 8 and 4 and 4 and 4 and 4 and 4 and 4 and 4 and 4

The spiral and the zigzag reach the highest possible score on every grid size because each one is a single hallway through every room.

## List 2: one short block of doors repeated over and over

A block is a short run of digits that repeats to fill the grid row by row. The program tested all 21844 blocks of 1 to 7 doors which make 21736 different repeating patterns. The digits here are door numbers (0 north and 1 east and 2 south and 3 west).

1. Block 0330100: total 402 of 984 (41%). Scores: 12 and 30 and 25 and 39 and 58 and 46 and 72 and 48 and 72
2. Block 2331112: total 402 of 984 (41%). Scores: 12 and 16 and 22 and 33 and 56 and 55 and 77 and 54 and 77
3. Block 2331122: total 396 of 984 (40%). Scores: 12 and 26 and 14 and 39 and 52 and 46 and 76 and 59 and 72
4. Block 2333311: total 396 of 984 (40%). Scores: 16 and 15 and 22 and 34 and 60 and 60 and 78 and 58 and 53
5. Block 233112: total 393 of 984 (40%). Scores: 12 and 30 and 29 and 44 and 40 and 62 and 47 and 72 and 57
6. Block 1233221: total 391 of 984 (40%). Scores: 16 and 25 and 27 and 30 and 55 and 51 and 73 and 54 and 60
7. Block 2333331: total 391 of 984 (40%). Scores: 16 and 18 and 18 and 24 and 58 and 71 and 75 and 57 and 54
8. Block 0333110: total 390 of 984 (40%). Scores: 8 and 10 and 21 and 29 and 59 and 55 and 76 and 55 and 77
9. Block 2233311: total 390 of 984 (40%). Scores: 16 and 13 and 37 and 30 and 59 and 51 and 74 and 58 and 52
10. Block 2331121: total 390 of 984 (40%). Scores: 12 and 30 and 14 and 40 and 43 and 44 and 76 and 59 and 72
11. Block 2332211: total 390 of 984 (40%). Scores: 12 and 26 and 28 and 30 and 58 and 42 and 76 and 57 and 61
12. Block 2332221: total 390 of 984 (40%). Scores: 12 and 29 and 19 and 31 and 56 and 44 and 77 and 61 and 61
13. Block 1233121: total 388 of 984 (39%). Scores: 16 and 26 and 27 and 31 and 48 and 51 and 73 and 54 and 62
14. Block 2233321: total 388 of 984 (39%). Scores: 16 and 13 and 29 and 34 and 56 and 53 and 74 and 60 and 53
15. Block 0333011: total 387 of 984 (39%). Scores: 8 and 22 and 25 and 30 and 60 and 51 and 77 and 55 and 59
16. Block 2333111: total 387 of 984 (39%). Scores: 16 and 13 and 25 and 34 and 61 and 49 and 79 and 57 and 53
17. Block 0330011: total 386 of 984 (39%). Scores: 12 and 25 and 27 and 30 and 58 and 42 and 76 and 56 and 60
18. Block 0333100: total 386 of 984 (39%). Scores: 8 and 23 and 21 and 33 and 59 and 55 and 72 and 44 and 71
19. Block 1233222: total 386 of 984 (39%). Scores: 16 and 22 and 28 and 29 and 47 and 53 and 76 and 55 and 60
20. Block 2332111: total 386 of 984 (39%). Scores: 12 and 25 and 24 and 31 and 60 and 40 and 77 and 56 and 61

The best block for each block length:

- 1 door: block 0 with total 216. Scores: 8 and 12 and 16 and 20 and 24 and 28 and 32 and 36 and 40
- 2 doors: block 03 with total 276. Scores: 16 and 16 and 22 and 24 and 32 and 32 and 42 and 40 and 52
- 3 doors: block 031 with total 321. Scores: 16 and 15 and 26 and 31 and 36 and 41 and 46 and 54 and 56
- 4 doors: block 0310 with total 340. Scores: 16 and 24 and 22 and 34 and 36 and 48 and 42 and 58 and 60
- 5 doors: block 23331 with total 383. Scores: 16 and 16 and 35 and 39 and 48 and 38 and 37 and 70 and 84
- 6 doors: block 233112 with total 393. Scores: 12 and 30 and 29 and 44 and 40 and 62 and 47 and 72 and 57
- 7 doors: block 0330100 with total 402. Scores: 12 and 30 and 25 and 39 and 58 and 46 and 72 and 48 and 72

No repeating block of 7 doors or fewer passes 42% of the highest possible total. A repeating block lines up well with some grid widths and badly with others so the nine scores swing up and down.

## List 3: well known number sequences

The first numbers of each sequence fill each grid (the first 4 numbers for 2 by 2 rooms and the first 100 numbers for 10 by 10 rooms).

1. Square numbers with one whole number in each room (1 4 9 16 ...): total 276 of 984 (28%). Scores: 16 and 16 and 22 and 24 and 32 and 32 and 42 and 40 and 52
2. Fibonacci numbers with one whole number in each room (1 1 2 3 5 8 ...): total 260 of 984 (26%). Scores: 8 and 15 and 26 and 44 and 46 and 35 and 12 and 11 and 63
3. Counting numbers with one whole number in each room (1 then 2 then 3 ...): total 250 of 984 (25%). Scores: 12 and 24 and 26 and 26 and 7 and 48 and 50 and 50 and 7
4. Digits of the counting numbers written in one row (1 2 3 ... 9 1 0 1 1 ...): total 199 of 984 (20%). Scores: 12 and 24 and 16 and 13 and 28 and 15 and 22 and 27 and 42
5. Digits of the square root of 2 (1 4 1 4 2 1 ...): total 177 of 984 (18%). Scores: 16 and 6 and 8 and 15 and 27 and 25 and 20 and 31 and 29
6. Digits of pi (3 1 4 1 5 9 ...): total 166 of 984 (17%). Scores: 6 and 8 and 15 and 12 and 15 and 25 and 29 and 33 and 23
7. Digits of the primes written in one row (2 3 5 7 1 1 1 3 ...): total 160 of 984 (16%). Scores: 16 and 6 and 15 and 23 and 11 and 18 and 21 and 26 and 24
8. Digits of e (2 7 1 8 2 8 ...): total 134 of 984 (14%). Scores: 16 and 6 and 23 and 8 and 15 and 13 and 19 and 18 and 16
9. One whole prime in each room (2 then 3 then 5 ...): total 98 of 984 (10%). Scores: 16 and 10 and 6 and 12 and 10 and 12 and 10 and 10 and 12

For comparison 300 sets of random digits averaged a total of 183 and the best of the 300 sets reached 248.

- Square numbers and Fibonacci numbers and counting numbers with one whole number in each room beat the random average.
- One whole prime in each room scores lowest because every prime above 2 is odd and odd numbers open east or west so no door ever joins two rows.
- The digits of pi and e and the square root of 2 and the primes land near the random average.

## What the three lists show together

- A shape that is redrawn to fit each grid can reach 100% on every size.
- A fixed repeating block tops out near 41% of the highest possible total.
- Well known sequences score between 10% and 28% which is close to random digits (about 19%).

## Weak points

- The totals add raw scores so the large grids count for more than the small grids.
- Blocks longer than 7 doors were not tested.
- Each well known sequence was read from its first number and a different starting point would change its scores.
