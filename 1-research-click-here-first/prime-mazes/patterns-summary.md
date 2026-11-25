# Patterns that stand out across the maze tests

> **About this page:** One AI model (Claude) wrote this summary on 25 November 2026 from the other pages in this folder. Every figure is taken from those pages and uses the rule where 0 opens north. The summary proves nothing about primes. No other person has reviewed the page yet.

## Patterns caused by the last digit of a prime

- **Prime grids lean sideways.** Of the 45086079 primes with 9 digits 58.1% have a side to side crossing and 41.8% have a top to bottom crossing while all numbers with 9 digits sit near 50% for both. The cause is the bottom right room which reads 1 or 3 or 7 or 9 and therefore never opens north.
- **The lean follows the labels and not the primes.** When 1 opened north the lean pointed the other way at 55.9% top to bottom. So the pattern is about which door the odd digits are assigned to.
- **A ring drawn by a prime can turn clockwise and cannot turn counterclockwise** because the other direction needs the last room to open north and north takes an even digit.
- **A zigzag prime exists on grids with an even side** because an odd side would need the last room to open south which also takes an even digit.

## Patterns caused by odd and even

- **One whole prime in each room gives pure rows.** Every prime above 2 is odd and odd numbers open east or west so no door ever joins two rows. That source scored the lowest of all well known sequences at 98 of 984.
- **Gaps between primes give pure columns** because every gap after the first is even and even numbers open north or south.
- **Half of each gap looks random** because dividing the gaps by 2 removes the evenness.

## Patterns caused by neighbors sharing digits

- **First digits of primes make bands.** Thousands of neighboring primes share a first digit so whole stretches of rooms open the same door. On a grid of 300 by 300 rooms the largest region had 8700 rooms and 174 regions crossed side to side while random digits gave a largest region of 72 rooms and no crossing.

## Where primes look like other numbers

- 0.203% of primes with 9 digits make one hallway through all 9 rooms against 0.214% of all numbers with 9 digits.
- 10.16% of primes join the two corners against 10.09% of all numbers.
- So apart from the last digit the digits of a prime behave like random digits in this test.

## Patterns that come from the maze rules alone

- **A joined group can never hold two doors that a digit opened onto the outside.** A group of joined rooms needs all but one of its doors to hold itself together so at most one door is left over. All 262144 door patterns on 3 by 3 rooms obey that rule.
- **Large grids fall apart into islands.** One door for each room opens about 44% of the inner walls and a random grid needs about 50% before one region can stretch across. Two numbers in each room open about 68% and then 99.5% of the rooms join into one region.
- **Perfect grids are rare.** 46 of 256 door patterns max the grid of 2 by 2 rooms and 504 of 262144 max the grid of 3 by 3 rooms.

## Patterns about sequences across grid sizes

- **No fixed sequence maxes 2 by 2 and 3 by 3 and 4 by 4 rooms together** because a wider grid cuts the same sequence into rows at different places. The most any fixed sequence earned was 2 points.
- **An equation that knows the grid width maxes every size** while the best equation that ignores the width reached 47% of the possible total.
- **Luck fades as grids grow and small fixes do not.** The best random number earned 100% on 4 by 4 rooms and 43% on 10 by 10 rooms. Changing one digit at a time lifted the number for 8 by 8 rooms from 54% to 100%.
- **Equal use of all ten digits does not block a perfect score.** Perfect grids with equal digits were found for every size from 4 by 4 to 8 by 8 rooms.

## The thread that ties the patterns together

Nearly every pattern that is special to primes traces back to how primes are written: the last digit is never even and every prime above 2 is odd and neighboring primes share leading digits. The maze works like a magnifying glass for those digit habits. No pattern on these pages points to deeper prime structure beyond those habits and the tests so far could not rule one out.

## Where each figure is from

- [maze-test-zero-north.md](maze-test-zero-north.md) holds the crossing counts and the hallway counts and the grid of 300 by 300 rooms.
- [neat-shapes-findings.md](neat-shapes-findings.md) holds the rings and the zigzag.
- [random-search-findings.md](random-search-findings.md) holds the random numbers and the rule about outside doors.
- [multi-size-score-list.md](multi-size-score-list.md) and [max-score-points-list.md](max-score-points-list.md) hold the sequences scored on many grid sizes.
- [equation-search-findings.md](equation-search-findings.md) and [equal-digits-findings.md](equal-digits-findings.md) hold the equations and the equal digit grids.
