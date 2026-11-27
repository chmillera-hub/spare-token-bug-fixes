# Questions about door mazes on other shapes of room and on pictures that grow

> **About this page:** One AI model (Claude) wrote this page on 27 November 2026 from a back and forth chat with the author of this repository. The author proposed every test and every rule on this page: hexagon rooms in place of square rooms and counting numbers on both shapes and other shapes of room and the Einstein hat tile and pictures that grow from one room and squares that read no numbers and towers that show visits. The chatbot wrote the programs and ran the counts. The numbers are measurements from the program [shapes-animation.html](shapes-animation.html) in this folder and from the programs in the folder boring-things/research-program-files/prime-mazes-scripts/shape-grid-scripts. The outline of the hat tile is the published shape and the page claims no new result about the hat tile. No other person has reviewed the page or the programs yet.

## The rule that every test shares

Each room reads one number and opens one door. The doors of a room are counted clockwise starting from the door that points most nearly north. The count goes around again when the number is larger than the number of doors so a 7 in a room with 6 doors opens door 1.

The three part score is the same score as on the square grid pages in this folder: the size of the largest region of connected rooms plus the number of rooms on the longest walk that never visits a room twice plus 1 point for each outside door where a player could enter and walk through to the opposite side of the grid.

## What changes when the rooms are hexagons?

The program [hexagon-animation.html](hexagon-animation.html) draws the same maze with hexagons. A hexagon has 6 doors so the digits 0 and 6 open the same door and so do 1 and 7 and 2 and 8 and 3 and 9. The digits 4 and 5 each have a door to themselves. The digits of pi on a hexagon grid of size 12 scored 45 of 336.

The pictures [pi-small-grids.png](pi-small-grids.png) and [pi-large-grids.png](pi-large-grids.png) show the digits of pi on squares and on hexagons side by side for four grid sizes.

## How many kinds of pattern do the counting numbers make?

The counting numbers 1 2 3 4 make exactly as many kinds of pattern as a room has doors.

- On hexagons there are 6 kinds. The kind depends on the remainder when the length of a row is divided by 6.
- On squares there are 4 kinds. The kind depends on the remainder when the length of a row is divided by 4.
- The kinds fall into three families on both shapes. A row length that is a multiple of the number of doors gives vertical bands because every room in a column opens the same door. A row length that is one more or one less than a multiple gives diagonal bands because the door shifts by one from each row to the next. Every other row length gives small closed tiles.

The pictures [small-hexagons-counting.png](small-hexagons-counting.png) and [large-hexagons-counting.png](large-hexagons-counting.png) show hexagon grids of sizes 12 to 17 and 30 to 35. The pictures [counting-on-small-squares.png](counting-on-small-squares.png) and [counting-on-large-squares.png](counting-on-large-squares.png) show square grids of sizes 12 to 15 and 32 to 35.

## Do hexagons score higher than squares on random digits?

Yes in most trials. A hexagon grid beat a square grid of the same size in 63% to 83% of trials with random digits across grid sizes from 12 to 60 when both were scored as a percentage of the highest possible score. One likely reason is that a room with more doors has more neighbors to join.

## Which other shapes of room were tried?

The program [shapes-animation.html](shapes-animation.html) switches between seven shapes.

- Triangles with 3 doors.
- Squares with 4 doors.
- Five sided rooms with 5 doors in the pattern known as the Cairo tiling.
- Hexagons with 6 doors.
- Eight sided rooms with squares between them.
- Ten sided rooms with squares between them. No flat grid can give every room ten neighbors because the average number of neighbors in a flat grid cannot go above 6. So a large room here is an eight sided outline where two of the slanted sides hold two doors each.
- The Einstein hat tile with 13 sides. One side is twice as long as the short sides and holds two doors so a hat has 14 doors.

Average scores for random digits at grid size 12 as a percentage of the highest possible score: triangles 8.8% and squares 10.1% and five sided rooms 10.5% and hexagons 11.6% and the eight sided mix 13.9% and the ten sided mix 13.7%. These averages come from the first version of the ten sided grid where each square was cut into two halves. The picture [six-grids-pi.png](six-grids-pi.png) shows the digits of pi on the six grids.

## What happens when the picture grows from one room?

The author proposed a second mode. The picture starts with one room. Each number picks a door of the room where the walk stands. A new room appears behind the door when the space is empty and the walk steps into the new room. When an old room already sits behind the door the door opens and the walk steps into the old room.

For the hat tile a new hat can often sit against a door in several ways. The number divided by 14 with the remainder dropped picks one way from the list of ways that do not overlap any hat. A step where no hat fits leaves the picture unchanged. The program checked that every hat covers exactly 8 small kites and that no two hats overlap in every run.

Findings from 3600 numbers unless a line says otherwise:

- Counting numbers freeze on most shapes because the doors get picked in clockwise order which walks the path around a small circle. The picture stops at 4 rooms on triangles and 4 on squares and 5 on five sided rooms and 6 on hexagons and 44 on hat tiles.
- Whole primes on squares make a flat line of 34 rooms because every prime after 2 is odd so only the east door and the west door get picked.
- Whole primes on hexagons never step back because every prime after 3 leaves a remainder of 1 or 5 when divided by 6 and both of those doors point upward. The result is 3599 rooms in one thin zigzag column.
- Prime gaps on squares make a straight vertical line of 683 rooms because every gap after the first is even.
- Prime gaps on hexagons stay inside a strip 7 units wide and 650 units tall. A likely reason is that a gap with remainder 2 and a gap with remainder 4 must take turns.
- Digits of pi and random digits make wandering clusters with many loops on every shape.
- Whole primes on hat tiles grow a long ribbon of 1863 hats and 927 of those hats are mirrored. The chatbot did not work out why the ribbon leans one way.
- Prime gaps on hat tiles make a thin chain of 2328 hats and only 117 of those hats are mirrored.

The picture [growing-rooms.png](growing-rooms.png) shows twelve growing pictures after 900 numbers each.

## What should happen to the squares between the large rooms?

The author tried four rules for the squares on the eight sided grid and the ten sided grid.

- **Squares read numbers like any room.** Digits of pi on a grid of size 12 scored 31 of 258 on the eight sided grid and 48 of 258 on the ten sided grid.
- **Squares read no numbers and start with every door open.** The whole grid is one region before the first number is read so two of the three score parts stop measuring anything. The picture [open-squares.png](open-squares.png) shows this rule.
- **Squares read no numbers and start with every door closed.** The scores drop to about 5% because the squares stop opening doors.
- **Squares read no numbers and a square disappears when a large room picks a door into the square.** A square that has disappeared keeps every door open. The scores land in a middle range that still differs from one sequence to the next. The picture [disappearing-squares.png](disappearing-squares.png) shows the digits of pi on the ten sided grid under this rule.

The author then set one more rule for the longest walk: a square that reads no numbers is not a step of the walk. A walk passes from one large room straight to another large room when a square joins the two rooms. The highest possible score on a grid of size 12 is then 209 which is 113 rooms for the largest region plus 64 large rooms for the longest walk plus 32 outside doors.

Scores on a grid of size 12 under the disappearing rule with the walk rule (each score is a lower bound because the search for the longest walk ran out of time):

- Digits of pi: 132 of 209 on the eight sided grid and 146 of 209 on the ten sided grid.
- Digits of the primes written in one row: 157 and 177.
- Whole primes: 169 and 157.
- Counting numbers: 156 and 166.
- Prime gaps: 47 and 172. The eight sided score is low because even numbers pick only the straight doors on that grid so no square ever disappears.
- Random digits averaged 63.1% on the eight sided grid and 66.9% on the ten sided grid over 100 runs each.

## Which new number sequences were added?

The program offers 25 more sequences: seven polynomial formulas and the terms of sums such as the Fibonacci numbers and the factorials and the Catalan numbers and the partition numbers plus Collatz step counts and divisor counts and the Recaman sequence and the digits of e and of the square root of 2 and of the golden ratio. A term too large for the program to hold exactly is replaced by the remainder after dividing by 10090080 because that remainder picks the same door in a room with any number of doors from 1 to 16.

- x squared on a square grid makes clean vertical stripes because a square number leaves a remainder of 0 or 1 when divided by 4.
- A formula whose values are all odd (such as x squared plus x plus 41) freezes at 2 or 3 rooms on growing squares and never steps back on growing hexagons.
- A formula with many even values (such as x squared) does the reverse: one straight line of 3601 squares and a freeze at 4 rooms on hexagons.
- Fibonacci numbers on growing squares make one flat line of 2401 rooms because the remainders of the Fibonacci numbers repeat in a short cycle.
- Collatz step counts on growing squares make a web of thin corridors with 2340 rooms.
- The Recaman sequence on growing hexagons makes a compact cluster of 203 rooms because the walk keeps stepping back into old rooms.

The picture [new-sequences.png](new-sequences.png) shows ten of these runs.

## How are repeat visits shown?

A room in a growing picture can be visited many times. The author asked for stacks and for a view like a landscape. The stacks view draws one more outline for each visit. The landscape view tilts the picture and draws each room as a tower whose height is the number of visits. A number on top shows the true count once a stack stops rising. In 1600 terms of the Recaman sequence on hexagons the most visited room was visited 52 times. The picture [visit-towers.png](visit-towers.png) shows eight runs.

## How does this connect to food and shelter and deep human connection?

A door maze does not feed or house anyone. The tie is in the method. One person with no training in mathematics asked plain questions and each answer was posted where anyone can read the answer for free. A reader who wonders about the same patterns can find the work already done and spend the saved time and money on meals or rent or on a long conversation with another person.

## What was not checked

- No other person has rerun the programs.
- The longest walk is a lower bound on grids with many loops because the search stops after 4 million tries.
- The choice among several hat placements uses the remainder trick only up to 16 placements and the chatbot did not confirm that more than 16 placements never occur for very large terms.
- The chatbot looked at the pictures as screenshots and did not view this page as shown on the GitHub site.
