# Equation search: equations whose outputs score high on many grid sizes

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026. The author of this repository asked for the experiments and the chatbot wrote the programs and ran the counts. The program is equation_search.py in the folder boring-things/research-program-files/prime-mazes-scripts. The page proves nothing about primes. No other person has reviewed the page yet.

## The rule

Each room reads one number and opens one door: 0 and 4 and 8 open north. 1 and 5 and 9 open east. 2 and 6 open south. 3 and 7 open west. The numbers fill a square grid row by row starting at the top left room. The three part score adds the largest region and the longest walk and the door points and every room on the edge of the grid is assumed to have a door to the outside that a player can open.

In every equation n is the room number counted from 0 in reading order. A number larger than 9 opens the door for its remainder after division by 4.

## An equation that maxes every grid size

This equation uses the number of rooms along one side which is written k.

- r = floor(n / k) which is the row
- c = n - k * r which is the column
- p = r mod 2 which is 0 on even rows and 1 on odd rows
- door = 1 + 2 * p + (1 - 2 * p) * floor((c + p * (k - 1 - 2 * c)) / (k - 1))

In plain words even rows give 1 (east) and end with a 2 (south) while odd rows give 3 (west) and begin with a 2 (south). The outputs draw one hallway that snakes through every room.

- 2 by 2 rooms: 1223 which scores 16 of 16
- 3 by 3 rooms: 112233112 which scores 30 of 30
- 4 by 4 rooms: 1112233311122333 which scores 48 of 48
- 5 by 5 rooms: 1111223333111122333311112 which scores 70 of 70

The program checked every grid from 2 by 2 to 12 by 12 rooms and the equation reached the highest possible score on all 11 sizes.

## Equations that do not use the grid width

The program tested 14589 equations that depend on n alone: quadratics with a remainder and floors of fractions and floors of squares and floors of square roots and powers with a remainder and sums of two floors. Each equation was scored on the nine grids from 2 by 2 to 10 by 10 rooms where the highest possible total is 984.

1. (3*n*n + n + 10) mod 11: total 458 of 984 (47%). Scores: 16 and 10 and 32 and 48 and 65 and 47 and 58 and 60 and 122
2. (3*n*n + 7*n + 3) mod 11: total 445 of 984 (45%). Scores: 12 and 15 and 35 and 39 and 58 and 50 and 50 and 63 and 123
3. (8*n*n + 6*n + 9) mod 11: total 430 of 984 (44%). Scores: 16 and 23 and 34 and 49 and 54 and 60 and 58 and 70 and 66
4. (n*n + 6*n + 0) mod 9: total 426 of 984 (43%). Scores: 12 and 19 and 40 and 29 and 41 and 49 and 85 and 58 and 93
5. (3*n*n + 6*n + 1) mod 11: total 424 of 984 (43%). Scores: 12 and 24 and 11 and 49 and 36 and 55 and 50 and 70 and 117
6. (5*n*n + 3*n + 8) mod 9: total 410 of 984 (42%). Scores: 12 and 26 and 35 and 22 and 37 and 60 and 86 and 56 and 76
7. (8*n*n + 4*n + 4) mod 9: total 408 of 984 (41%). Scores: 16 and 18 and 21 and 39 and 36 and 38 and 73 and 58 and 109
8. (5*n*n + 2*n + 1) mod 9: total 405 of 984 (41%). Scores: 8 and 15 and 39 and 33 and 36 and 48 and 87 and 67 and 72
9. (3*n*n + 5*n + 1) mod 11: total 405 of 984 (41%). Scores: 8 and 10 and 41 and 40 and 37 and 58 and 56 and 75 and 80
10. (8*n*n + 0*n + 1) mod 11: total 405 of 984 (41%). Scores: 16 and 21 and 34 and 50 and 46 and 56 and 52 and 59 and 71
11. (n*n + 8*n + 7) mod 9: total 400 of 984 (41%). Scores: 16 and 19 and 24 and 33 and 38 and 60 and 79 and 43 and 88
12. (n*n + 4*n + 4) mod 9: total 397 of 984 (40%). Scores: 6 and 19 and 31 and 21 and 40 and 46 and 87 and 56 and 91

The best equation is (3*n*n + n + 10) mod 11. Its outputs begin 10 and 3 and 2 and 7 and 7 and 2 and 3 and 10 and 1 and 9 and 1 and then repeat every 11 steps.

For comparison the best repeating block of 7 doors or fewer scored 402 and random digits average about 183.

## Maxing out grids with an equation that ignores the width

No equation in the search maxed more than one grid size. Most of the equations that maxed a grid maxed 2 by 2 rooms and a few (such as 9^n mod 43 and 6^n mod 13) maxed 3 by 3 rooms.

A wider grid cuts the same outputs into rows at different places so an equation has to know the row length to keep one hallway whole.

## Weak points

- The search covered six families of simple equations and not every possible equation.
- The equation that uses the grid width was checked on 11 grid sizes and no proof for all sizes was written out although the snake shape works the same way at any width.
- The totals add raw scores so the large grids count for more than the small grids.
