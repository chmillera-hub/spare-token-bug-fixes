# Computing q·P on an elliptic curve modulo p² without the division error

## Link to the original question

https://ask.sagemath.org/question/83276/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the computation in a single chat on 12 November 2026 in Python (with the PARI library for the point count) on the exact numbers from the question and no other person has rerun the computation yet which means the page is unconfirmed. No Sage command was tested.

## The question

On 30 June 2025 somebody asked on the SageMath question board why computing q·P fails with a ZeroDivisionError for a point P on an elliptic curve over the whole numbers modulo p² where q is the number of points of the same curve modulo p.
The asker recalled that the group modulo p² is the group modulo p together with one extra cyclic part of size p so the largest order of a point should be the least common multiple of q and p.
Comments reported that the code works on a newer Sage version and the question had zero answers when the board was read on 12 November 2026.

## Why the division error happens

The point q·P reduces to the neutral point (the point at infinity) modulo p and q·P is still a real non-trivial point modulo p².
The ordinary x and y coordinates of such a point would need a division by a number that is divisible by p and no such division exists modulo p².
Addition formulas written for a field hit exactly that impossible division.

## What the computation shows

The program uses projective coordinates (three numbers X and Y and Z per point) and addition formulas that contain no division at all.

- The point count modulo p from PARI is q = 115792089237316195423570985008687907852611146790557618865587299996221326510560 which differs from p.
- The point P with x = 12010 lies on the curve modulo p².
- The point q·P lies on the curve modulo p² and has X and Z divisible by p with Y not divisible by p so q·P reduces to the neutral point modulo p.
- The point q·P is not the neutral point modulo p².
- Multiplying once more by p gives exactly the neutral point modulo p² (X = 0 and Z = 0).

## Best-guess answer

The computation confirms the expectation in the question for this point: q·P is a non-trivial point of order p inside the extra cyclic part and p·q·P is the neutral point.
Any system can compute q·P by using projective coordinates with division-free addition formulas and the Python program does so in under a second after the point count is known.

The program named curve_mod_p2.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
