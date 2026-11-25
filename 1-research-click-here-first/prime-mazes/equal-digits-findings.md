# Equal digits: high scoring sequences that use all ten digits equally often

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026. The author of this repository asked for the experiments and the chatbot wrote the programs and ran the counts. The program is equal_digits_search.py in the folder boring-things/research-program-files/prime-mazes-scripts. The page proves nothing about primes. No other person has reviewed the page yet.

## The rule

Each room reads one number and opens one door: 0 and 4 and 8 open north. 1 and 5 and 9 open east. 2 and 6 open south. 3 and 7 open west. The numbers fill a square grid row by row starting at the top left room. The three part score adds the largest region and the longest walk and the door points and every room on the edge of the grid is assumed to have a door to the outside that a player can open.

## What equal digits means for the doors

Three digits open north (0 and 4 and 8) and three open east (1 and 5 and 9) while two open south and two open west. Equal use of all ten digits therefore gives about 30% north doors and 30% east doors and 20% south doors and 20% west doors. The spiral and the zigzag on other pages use almost no north doors so both fail this rule.

## The best grid found for each size

The program started from a shuffled set of equal digits and swapped two digits at a time which keeps the count of every digit fixed. When the number of rooms does not divide by 10 each digit appears either the lower or the higher of two neighboring counts.

- **4 by 4 rooms:** score 48 of 48. The number is 6373956411280594 (the ten digits 0 to 9 appear 1 and 2 and 1 and 2 and 2 and 2 and 2 and 1 and 1 and 2 times).
- **5 by 5 rooms:** score 70 of 70. The number is 1993727960644246873851550 (the ten digits 0 to 9 appear 2 and 2 and 2 and 2 and 3 and 3 and 3 and 3 and 2 and 3 times).
- **6 by 6 rooms:** score 96 of 96. The number is 236737649560299734687120118824515090 (the ten digits 0 to 9 appear 4 and 4 and 4 and 3 and 3 and 3 and 4 and 4 and 3 and 4 times).
- **7 by 7 rooms:** score 126 of 126. The number is 1952956876746367210432834234116030027719049558598 (the ten digits 0 to 9 appear 5 and 5 and 5 and 5 and 5 and 5 and 5 and 5 and 4 and 5 times).
- **8 by 8 rooms:** score 160 of 160. The number is 5196119207674763549692038639825842033643025542180787670351149158 (the ten digits 0 to 9 appear 6 and 7 and 6 and 7 and 6 and 7 and 7 and 6 and 6 and 6 times).
- **9 by 9 rooms:** score 195 of 198. The number is 952295612075642346083101682198833142877014637994403296595410682895518506403737777 (the ten digits 0 to 9 appear 8 and 8 and 8 and 8 and 8 and 8 and 8 and 9 and 8 and 8 times).
- **10 by 10 rooms:** score 237 of 240. The number is 1616756723062347382802599184748511214114867364302702545648308992358590477615203363070675289959099418 (the ten digits 0 to 9 appear 10 and 10 and 10 and 10 and 10 and 10 and 10 and 10 and 10 and 10 times).
- **12 by 12 rooms:** score 325 of 336. The number is 927561921512091460824237433638278595594124698770472730144958905610512873879608479564687689203320168110659054678333283634521920647347458710519150 (the ten digits 0 to 9 appear 14 and 15 and 14 and 14 and 15 and 15 and 14 and 15 and 14 and 14 times).

So equal digits do not block the highest score: the program found a perfect grid for every size from 4 by 4 to 8 by 8 rooms. The results for 9 by 9 and 10 by 10 and 12 by 12 rooms are the best found in about two minutes each and are not proven limits.

## One repeating block of ten digits that uses each digit once

The program tested all 25200 different door arrangements of such a block on the nine grids from 2 by 2 to 10 by 10 rooms where the highest possible total is 984. The average block scored 203 and the lowest scored 88.

1. Block 1590372648: total 383 of 984. Scores: 16 and 23 and 21 and 52 and 18 and 15 and 63 and 79 and 96
2. Block 1592376048: total 377 of 984. Scores: 8 and 17 and 15 and 23 and 19 and 43 and 57 and 99 and 96
3. Block 1237064859: total 375 of 984. Scores: 16 and 15 and 36 and 12 and 20 and 46 and 66 and 94 and 70
4. Block 1590372486: total 373 of 984. Scores: 16 and 25 and 15 and 52 and 40 and 16 and 55 and 58 and 96
5. Block 1592370648: total 373 of 984. Scores: 8 and 16 and 21 and 23 and 21 and 41 and 62 and 85 and 96
6. Block 1237604859: total 371 of 984. Scores: 16 and 18 and 20 and 12 and 18 and 47 and 63 and 107 and 70
7. Block 1237046859: total 369 of 984. Scores: 16 and 18 and 20 and 35 and 20 and 48 and 55 and 87 and 70
8. Block 1503729468: total 367 of 984. Scores: 16 and 10 and 15 and 56 and 44 and 17 and 57 and 68 and 84
9. Block 1592306748: total 367 of 984. Scores: 8 and 18 and 31 and 27 and 15 and 45 and 58 and 79 and 86
10. Block 1503726948: total 364 of 984. Scores: 16 and 8 and 12 and 59 and 14 and 16 and 56 and 99 and 84
11. Block 1592370468: total 364 of 984. Scores: 8 and 14 and 17 and 52 and 21 and 38 and 50 and 68 and 96
12. Block 1523760489: total 364 of 984. Scores: 8 and 18 and 14 and 23 and 15 and 43 and 58 and 103 and 82

## Points for maxing out a grid size with equal digits

- 5 blocks earn 2 points by maxing both 2 by 2 and 3 by 3 rooms: 1504928376 and 1250948376 and 1590234786 and 2316045987 and 1206345987.
- 4535 blocks max 2 by 2 rooms and no other size.
- 41 blocks max 3 by 3 rooms and no other size.
- 20619 blocks earn no points.
- No block of this kind maxes any grid larger than 3 by 3 rooms.

## Equations with equal digits

The equation (a*n + b) mod 10 gives each digit once every 10 steps when a is 1 or 3 or 7 or 9. The program tested all 40 such equations.

1. (9*n + 7) mod 10 with outputs 7654321098: total 294 of 984.
2. (9*n + 1) mod 10 with outputs 1098765432: total 288 of 984.
3. (9*n + 6) mod 10 with outputs 6543210987: total 286 of 984.
4. (9*n + 9) mod 10 with outputs 9876543210: total 278 of 984.
5. (n + 1) mod 10 with outputs 1234567890: total 270 of 984.
6. (9*n + 5) mod 10 with outputs 5432109876: total 270 of 984.
7. (9*n + 0) mod 10 with outputs 0987654321: total 267 of 984.
8. (9*n + 8) mod 10 with outputs 8765432109: total 267 of 984.

Counting down beats counting up by a little and both land well under the best block.

## Weak points

- The swap search had one run for each grid size.
- Repeating blocks longer than ten digits were not tested.
- The numbers are built digit sets and are not primes.
