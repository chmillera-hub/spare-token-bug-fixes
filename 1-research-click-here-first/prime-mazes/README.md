# Prime mazes

This folder holds experiments that turn the digits of prime numbers into mazes. The author of this repository proposed the rules and an AI model (Claude) wrote the programs and ran the counts on 25 November 2026 and no other person has rechecked the pages.

- [champion-primes-zero-north.png](champion-primes-zero-north.png) is a picture of eight primes drawn on door grids under the version of the rule where 0 opens north.
- [champion-primes.png](champion-primes.png) is a picture of eight primes drawn on door grids with the digits inside the rooms.
- [door-grids-zero-north.png](door-grids-zero-north.png) is a picture of six grids of 40 by 40 rooms under the version of the rule where 0 opens north.
- [door-grids.png](door-grids.png) is a picture of six grids of 40 by 40 rooms fed by different number sources.
- [hallway-walk-findings.md](hallway-walk-findings.md) reports a rule where each number is the length of a hallway and the walker turns right after each hallway: the digits of the primes written in one row drift 969 steps east because primes with 4 digits line up with the 4 directions.
- [hallway-walks.png](hallway-walks.png) is a picture of eight hallway walks.
- [maze-animation.html](maze-animation.html) is a program for a web browser: pick the door rule (0 opens north or 1 opens north) and where the numbers are taken from and a grid size and press Play to watch each room open a door and read the scores.
- [maze-test-findings.md](maze-test-findings.md) reports the maze test where each digit opens one door of a room: all 1061 primes with 4 digits and all 45086079 primes with 9 digits scored by longest walk and by crossings from one side of the square to the opposite side (80279 primes with 9 digits make one hallway through all 9 rooms and the smallest is 100101299) plus larger grids and primes built to make one hallway through 100 rooms.
- [maze-test-zero-north.md](maze-test-zero-north.md) repeats the maze test under a second version of the rule where 0 opens north: the lean of the primes flips from top to bottom crossings to side to side crossings and 91720 primes with 9 digits make one hallway through all 9 rooms and the smallest is 102002003.
- [ranking-list-zero-north.txt](ranking-list-zero-north.txt) is a plain text ranking of primes by maze score under the version of the rule where 0 opens north.
- [ranking-list.txt](ranking-list.txt) is a plain text ranking of primes by maze score under the version of the rule where 1 opens north.

The maze program runs in a web browser at this address: https://chmillera-hub.github.io/spare-token-bug-fixes/1-research-click-here-first/prime-mazes/maze-animation.html
