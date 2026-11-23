# Delivery routes

This folder holds computer tests of how close a batch of guesses lands to the shortest possible delivery route (the puzzle often called the traveling salesman problem). An AI chatbot (Claude) ran the tests and wrote the page on 23 November 2026 and no other person has rechecked the page.

- [route-guessing-findings.md](route-guessing-findings.md) reports how much longer the best of 10000 random routes is than the proven shortest route for problems with 6 to 280 stops (0% longer at 8 stops and 209% longer at 52 stops and 1092% longer at 280 stops) and then shows that one simple rule (drive to the nearest unvisited stop 9 times out of 10) brings the same 10000 guesses to between 6% and 15% longer on the same problems.
