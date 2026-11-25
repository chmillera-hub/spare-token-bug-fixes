# Master challenge: sequences scored on the two circle test and the maze test together

> **About this page:** One AI model (Claude) wrote this page on 25 November 2026. The author of this repository asked whether any sequence does well on both tests and the chatbot wrote the programs and ran the counts. The programs are master_challenge.py and master_challenge_digits.py in the folder boring-things/research-program-files/prime-mazes-scripts. The page proves nothing about primes. No other person has reviewed the page yet.

## The two tests

**The two circle test** is described on the pages in the folder [prime-richness](../prime-richness). A sequence feeds two circles of marks one term at a time. On the cumulative circle each term moves the arrow that many marks so the arrow shows the running total. On the literal circle the arrow lands on the mark with the same number as the term after full turns are removed. Each circle size gets 30 steps for each mark. The score adds the average share of marks reached on each circle so a sequence that fills both circles on every size scores 200.

**The maze test** is described on the other pages in this folder. Each room reads one number and opens one door (0 and 4 and 8 north and 1 and 5 and 9 east and 2 and 6 south and 3 and 7 west) and the three part score adds the largest region and the longest walk and the door points. The maze total on this page adds the scores for the nine grids from 2 by 2 to 10 by 10 rooms where the highest possible total is 984.

## Why one sequence can do well on both

The maze reads the first numbers of a sequence: 16 for a grid of 4 by 4 rooms and 100 for a grid of 10 by 10 rooms. The circle test reads thousands of numbers. So the start of a sequence decides the maze score and the long tail decides the circle score.

## Part 1: sequences of the digits 0 to 9

The circles here use the block rule from the prime-richness pages: a circle reads as many digits at a time as its size is written with. The program tested every circle size from 2 to 1000 marks. The maze reads one digit in each room.

- **Digits of pi alone:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 187 of 984 and the sequence maxes no maze size. The sequence begins 141592653589793238462643383279
- **Perfect 8 by 8 grid with equal digits and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 349 of 984 and the sequence maxes the maze at 8 by 8 rooms. The sequence begins 519611920767476354969203863982
- **Perfect 6 by 6 grid with equal digits and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 305 of 984 and the sequence maxes the maze at 2 by 2 rooms and 6 by 6 rooms. The sequence begins 236737649560299734687120118824
- **Perfect 10 by 10 grid (random number improved digit by digit) and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 377 of 984 and the sequence maxes the maze at 10 by 10 rooms. The sequence begins 277177277725849021285258475828
- **Perfect 12 by 12 spiral and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 310 of 984 and the sequence maxes the maze at 12 by 12 rooms. The sequence begins 111111111112111111111122011111
- **16 digits that max 3 by 3 and 4 by 4 rooms (2332120331120333) and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 293 of 984 and the sequence maxes the maze at 3 by 3 rooms and 4 by 4 rooms. The sequence begins 233212033112033314159265358979
- **9 digits that max 2 by 2 and 3 by 3 rooms (150492837) and then the digits of pi:** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 201 of 984 and the sequence maxes the maze at 2 by 2 rooms and 3 by 3 rooms. The sequence begins 150492837141592653589793238462
- **Repeating block 1590372648:** circle score 85.7 of 200 (both circles filled on 641 and 8 of 999 sizes) and maze total 383 of 984 and the sequence maxes the maze at 2 by 2 rooms. The sequence begins 159037264815903726481590372648
- **Counting numbers written in a line (123456789101112):** circle score 200.0 of 200 (both circles filled on 999 and 999 of 999 sizes) and maze total 199 of 984 and the sequence maxes no maze size. The sequence begins 123456789101112131415161718192

So a sequence of digits can be perfect on the circles and perfect on the maze at one or two grid sizes. The most maze sizes any one fixed sequence maxed is two which matches the limit on the page [max-score-points-list.md](max-score-points-list.md).

A repeating block does well on the maze total and badly on the circles because a repeating block keeps landing on the same few marks.

## Part 2: sequences of whole numbers

The circles here read each whole number as one term on every circle size from 2 to 200 marks. The maze reads one whole number in each room. Each line gives the circle score out of 200 and the maze total out of 984 and then the average of the two as percents.

### Named sequences

1. 1 + 2 + 3 + 5 + 6 + 7 (numbers with no repeated prime piece): circle 192.4 and maze 294 (29.9%) and average 63.0%
2. 1 - 2 + 3 - 4 (counting numbers with flipping signs): circle 200.0 and maze 250 (25.4%) and average 62.7%
3. 4 + 6 + 8 + 9 (composite numbers): circle 200.0 and maze 191 (19.4%) and average 59.7%
4. 1 + 2 + 5 + 8 + 11 (whole part of n times the root of n): circle 200.0 and maze 185 (18.8%) and average 59.4%
5. 0 + 1 + 3 + 5 + 8 (whole part of n times the natural logarithm of n): circle 200.0 and maze 175 (17.8%) and average 58.9%
6. 4 - 6 + 8 - 9 (composite numbers with flipping signs): circle 200.0 and maze 170 (17.3%) and average 58.6%
7. 1 + 2 + 4 + 5 + 7 (whole part of n times the root of 2): circle 199.9 and maze 148 (15.0%) and average 57.5%
8. 1 + 3 + 4 + 6 + 8 (whole part of n times the golden ratio): circle 199.8 and maze 134 (13.6%) and average 56.8%
9. 1 - 3 + 5 - 7 (odd numbers with flipping signs): circle 168.6 and maze 216 (22.0%) and average 53.1%
10. 1 + 2 + 3 + 4 (counting numbers): circle 145.9 and maze 250 (25.4%) and average 49.2%
11. 2 - 3 + 5 - 7 (primes with flipping signs): circle 164.5 and maze 140 (14.2%) and average 48.2%
12. 2 + 3 + 5 + 7 (primes): circle 164.5 and maze 98 (10.0%) and average 46.1%
13. repeating block 0 3 3 0 1 0 0 (best short block from the maze test): circle 98.9 and maze 402 (40.9%) and average 45.2%
14. repeating block 1 5 9 0 3 7 2 6 4 8 (best block with equal digits from the maze test): circle 101.7 and maze 383 (38.9%) and average 44.9%
15. 1 - 4 + 9 - 16 (squares with flipping signs): circle 118.2 and maze 276 (28.0%) and average 43.6%
16. 1 + 2 + 2 + 3 + 2 + 4 (number of divisors of n): circle 138.0 and maze 171 (17.4%) and average 43.2%
17. 1 + 1 + 2 + 3 + 5 (Fibonacci numbers): circle 111.6 and maze 260 (26.4%) and average 41.1%
18. 1 + 4 + 9 + 16 (squares): circle 104.0 and maze 276 (28.0%) and average 40.0%
19. 1 + 4 + 1 + 5 + 9 (digits of pi after the decimal point): circle 119.3 and maze 187 (19.0%) and average 39.3%
20. 1 + 8 + 27 + 64 (cubes): circle 87.3 and maze 326 (33.1%) and average 38.4%
21. 1 + 1 + 1 + 1 (steady 1): circle 102.5 and maze 216 (22.0%) and average 36.6%
22. 1 + 3 + 6 + 10 (triangular numbers): circle 112.8 and maze 146 (14.8%) and average 35.6%
23. 2 + 4 + 6 + 8 (even numbers): circle 108.1 and maze 136 (13.8%) and average 33.9%
24. 1 + 2 + 2 + 4 (gaps between neighboring primes): circle 95.7 and maze 122 (12.4%) and average 30.1%
25. 1 + 3 + 5 + 7 (odd numbers): circle 112.0 and maze 40 (4.1%) and average 30.0%

### Equations: the best average of the two tests

The program tested 14589 equations where n counts from 0.

1. floor(sqrt(35*n)): circle 200.0 and maze 383 (38.9%) and average 69.5%
2. floor(17*n / 40): circle 199.9 and maze 380 (38.6%) and average 69.3%
3. floor(sqrt(30*n)): circle 200.0 and maze 379 (38.5%) and average 69.3%
4. floor(n/3) + floor(n/10): circle 199.1 and maze 384 (39.0%) and average 69.3%
5. floor(sqrt(43*n)): circle 200.0 and maze 377 (38.3%) and average 69.2%
6. floor(sqrt(29*n)): circle 200.0 and maze 376 (38.2%) and average 69.1%
7. floor(8*n / 19): circle 199.7 and maze 376 (38.2%) and average 69.0%
8. floor(13*n / 31): circle 200.0 and maze 374 (38.0%) and average 69.0%
9. floor(11*n / 26): circle 199.8 and maze 374 (38.0%) and average 68.9%
10. floor(14*n / 33): circle 199.8 and maze 373 (37.9%) and average 68.9%
11. floor(19*n / 40): circle 200.0 and maze 371 (37.7%) and average 68.8%
12. floor(16*n / 37): circle 199.8 and maze 367 (37.3%) and average 68.6%

### Equations: the best score on whichever test is weaker

1. (3*n*n + n + 10) mod 11: circle 108.3 and maze 458 (46.5%) and the weaker test is at 46.5%
2. (3*n*n + 7*n + 3) mod 11: circle 108.3 and maze 445 (45.2%) and the weaker test is at 45.2%
3. (8*n*n + 6*n + 9) mod 11: circle 108.2 and maze 430 (43.7%) and the weaker test is at 43.7%
4. (n*n + 6*n + 0) mod 9: circle 94.8 and maze 426 (43.3%) and the weaker test is at 43.3%
5. (3*n*n + 6*n + 1) mod 11: circle 108.3 and maze 424 (43.1%) and the weaker test is at 43.1%
6. (5*n*n + 3*n + 8) mod 9: circle 97.5 and maze 410 (41.7%) and the weaker test is at 41.7%
7. (8*n*n + 4*n + 4) mod 9: circle 99.1 and maze 408 (41.5%) and the weaker test is at 41.5%
8. (5*n*n + 2*n + 1) mod 9: circle 97.5 and maze 405 (41.2%) and the weaker test is at 41.2%

## What the results show

- The two tests pull in opposite directions for a plain equation. The circles reward a sequence that keeps reaching new remainders and the maze rewards a tight repeating structure of doors.
- Slow growing equations such as the whole part of the square root of 35 times n do best at both because each value repeats a few times (which helps the maze) while the values still climb through every number (which fills the circles).
- The circle champion 1 - 2 + 3 - 4 scores 200 on the circles and 25% on the maze. The maze champion (3*n*n + n + 10) mod 11 scores 47% on the maze and 108 on the circles.
- The primes score 164.5 on the circles and 98 on the maze which is the weakest maze score among the well known sequences.

## Weak points

- The circle runs used fewer sizes than the prime-richness pages which went up to 5000 marks.
- The digit sequences in Part 1 were built on purpose so they show what is possible and say nothing about primes.
- Each maze total adds raw scores so the large grids count for more than the small grids.
- The search did not find a sequence that maxes three maze sizes and did not prove that none exists.
