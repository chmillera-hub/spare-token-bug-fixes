# Ranking of number sequences on growing ten sided rooms and the patterns behind the scores

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026 from a back and forth chat with the author of this repository. The author asked for a ranking of sequences on the ten sided rooms and sent screenshots of single runs and asked what pattern each picture shows. The chatbot ran the counts and wrote the explanations. The numbers are measurements from the program [shapes-animation.html](shapes-animation.html) in this folder and from the programs in the folder boring-things/research-program-files/prime-mazes-scripts/shape-grid-scripts. The facts about last digits are standard arithmetic and the page claims no new result. No other person has reviewed the page yet.

## The setup

The picture starts with one ten sided room. Each number picks one of the 10 doors so the door is the last digit of the number. Door 0 points up. Doors 1 and 2 point up and right. Door 3 points right. Door 4 points down and right. Door 5 points down. Doors 6 and 7 point down and left. Door 8 points left. Door 9 points up and left. A diagonal door passes through a square and the square appears as an extra room. A new large room appears when the space behind a door is empty. The walk steps into the old room when a room is already there.

The score is the number of rooms placed plus the longest walk through open doors that never enters a room twice. A square counts as a room placed and does not count as a step of the walk. Each sequence got 3600 numbers. The words at least mean the search for the longest walk ran out of time.

## The ranking

1. x squared minus x plus 1: at least 9362 (5761 rooms plus a walk of 3601)
2. x squared plus x plus 41: at least 9361 (5761 plus 3600)
3. x cubed plus x: 7922 (4321 plus 3601)
4. Doubling numbers: at least 7205 (4503 plus 2702)
5. Tripling numbers: at least 7205 (4503 plus 2702)
6. Factorials: 7202 (3603 plus 3599)
7. Catalan numbers: at least 6998 (3681 plus 3317)
8. Divisor counts: at least 6296 (4409 plus 1887)
9. Whole primes: at least 5943 (4077 plus 1866)
10. Last digit of each prime: at least 5943 (the same walk as whole primes)
11. Digits of the primes written in one row: at least 5447 (4182 plus 1265)
12. 2 times x squared minus 1: 5043 (4321 plus 722)
13. Count of smaller numbers that share no factor: at least 4724
14. Collatz step counts: at least 4441
15. Running totals of the primes: at least 4401
16. Prime gaps: at least 4204
17. Digits of pi: at least 3234
18. Digits of the golden ratio: at least 3089
19. Random digits: about 2947 on average over 5 runs
20. Digits of e: at least 2774
21. Digits of the square root of 2: at least 2674
22. Partition numbers: at least 2145
23. Recaman sequence: at least 806
24. Whole part of n times the natural logarithm of n: at least 641
25. Fibonacci numbers: at least 97
26. Counting numbers: 26
27. x to the power 5: 26
28. Cube numbers: 24
29. Running totals of 1 + 2 + 3 + 4: 22
30. Square numbers: 16
31. x squared plus 1: 15
32. x to the power 4: 10

The picture [ten-patterns.png](ten-patterns.png) shows ten of these runs.

## What separates the top from the bottom?

- The top sequences never step back. The last digits of x squared minus x plus 1 repeat as 1 3 7 3 1 and those five doors add up to 3 rooms right and 1 room up. The walk had zero steps back in 3600 numbers.
- The bottom eight sequences are closed loops. Each has last digits that repeat in a short cycle whose doors cancel out. The picture stops growing within the first 13 numbers (59 for the Fibonacci numbers) and every later number only raises towers.
- The digits of pi and e and the golden ratio and the square root of 2 land within a few hundred points of random digits.

## Do the last digits of every polynomial repeat?

Yes for every polynomial with whole number coefficients. Adding 10 to x does not change the last digit of x so the value at x and the value at x plus 10 end in the same digit. The cycle length is 1 or 2 or 5 or 10.

On the ten sided rooms a polynomial walk therefore has one of two fates. When the doors of one cycle cancel the picture freezes into a small loop. When the doors do not cancel the walk shifts by the same step after every cycle and marches in a straight band.

- **Square numbers.** The last digits are 1 4 9 6 5 6 9 4 1 0. The walk goes out two rooms and returns and then goes out three rooms the other way and returns. The picture is 6 large rooms and 4 squares. Two end rooms get one visit in each lap and the other four rooms get two visits.
- **2 times x squared minus 1.** The last digits are 1 7 7 1 9. The walk steps to a side room and returns and steps to the opposite side room and returns and then moves one room up and left. The picture is a ladder. Each room on the middle line gets 3 visits and each cycle adds 6 rooms.
- **Factorials.** Every factorial from 120 onward ends in 0 so the walk goes straight up.

A formula with a fraction can have a longer cycle: the running totals of 1 + 2 + 3 + 4 repeat every 20 values.

## Why do whole primes climb on ten sided rooms?

Every prime after 5 ends in 1 or 3 or 7 or 9 so only four doors are used. Door 1 and door 7 are opposite and cancel. Door 9 pushes up and left and door 3 pushes right. The net push is one room upward for about every four primes.

- Among the first 3600 primes 892 end in 1 and 910 end in 3 and 903 end in 7 and 893 end in 9.
- The walk ended 882 rooms above the start which is 0.245 rooms for each prime.
- The walk ended 7 rooms right of the start and stayed between 9 rooms left and 15 rooms right.
- A prime ending in 1 sits next to a prime ending in 7 at 563 places. Each such pair sends the walk out and straight back which accounts for about half of the 1204 steps back.

## What do the digits of the golden ratio do?

The first 3481 digits make a wandering cloud that drifted up and right. The walk ended 75 rooms right and 95 rooms up which is 121 rooms from the start. The cloud measures about 153 rooms along the diagonal from lower left to upper right and about 52 rooms across.

- The room favors that diagonal because two doors point up and right and two doors point down and left. In 2000 walks with random digits the average cloud measured about 91 rooms along that diagonal and about 73 across.
- The digit 6 showed up 309 times and the digit 1 showed up 376 times where an even spread gives about 348. That left 734 steps up and right against 674 steps down and left.
- 6.7% of the 2000 random walks ended farther from the start. So the drift is within what chance produces and the page does not claim a property of the golden ratio.

## What happens with counting numbers on the Einstein hat tile?

The walk places 44 hats and then falls into a closed circuit. The hat runs read the counting numbers from 10 upward.

- The last new hat was placed at the 57th number. No hat was placed after that in 3249 numbers.
- The walk then repeats the same lap every 28 numbers. One lap visits 17 hats once and 4 hats twice and spends 3 numbers on doors where no hat fits.
- The first 23 hats form the approach path and get one visit each with two exceptions. Hats 24 to 44 form the circuit.
- A hat has 14 doors so the door count returns every 14 numbers and the lap takes two turns of that count.

## Is there a pattern in Collatz step counts on the hat tile?

Yes. Neighboring numbers often take the same number of Collatz steps.

- For the numbers 1 to 3600 a number has the same step count as the number before in 1416 of 3599 cases which is 39.3%. The longest run of equal step counts is 14 numbers.
- Of those 1416 repeats 633 placed a new hat and 262 stepped back into an old hat and 521 hit a door where no hat fits.
- When no hat fits the walk stays put. A repeat then tries the same door and fails again. More than half of the 951 failed steps happened on a repeat.
- The same step counts in shuffled order (20 shuffles) averaged 1268 hats and 747 failed steps and 1586 steps back. The true order gave 1470 hats and 951 failed steps and 1180 steps back. So the order of the step counts matters and not only which values appear.

The page says nothing about whether the Collatz conjecture is true.

## How does this connect to food and shelter and deep human connection?

A ranking of number walks does not feed or house a person. The tie is that the work sits in public for free. A person who wonders why a picture freezes or marches or wanders can read the reason here without paying for the answer and can spend the saved hours on earning a meal or keeping a home or on a long talk with another person about what matters to both of them.

## What was not checked

- No other person has rerun the programs.
- The longest walk is a lower bound wherever the page says at least. Neighbors in the middle of the ranking could swap places with a longer search.
- The ranking used 3600 numbers and a different count could reorder the middle of the list.
- The chatbot traced the square numbers and the ladder by hand from the door directions and checked the counts against the author's screenshots.
