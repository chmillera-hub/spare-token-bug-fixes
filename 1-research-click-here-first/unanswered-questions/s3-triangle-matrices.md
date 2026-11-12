# The map from the symmetric group S3 to rotations and reflections of a triangle

## Link to the original question

https://ask.sagemath.org/question/87352/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with the Python library sympy and no other person has rerun the checks yet which means the page is unconfirmed. No Sage command was tested because Sage was not installed.

## The question

On 12 January 2026 somebody asked on the SageMath question board how to define the map from the symmetric group S3 (the six ways to rearrange three things) into 2 by 2 matrices so that the generators become a rotation by 120 degrees and a reflection.
The question had zero answers and zero comments when the board was read on 12 November 2026.

## The construction

Place the three things at the corners of an equilateral triangle centered at the origin with corner k at the angle 120·k degrees.
Every rearrangement p of the corners is carried out by exactly one 2 by 2 matrix: the matrix that sends corner k to corner p(k).

- The 3-cycle 0→1→2→0 gives the rotation by 120 degrees with rows (−1/2 and −√3/2) and (√3/2 and −1/2).
- The swap of corners 1 and 2 gives the reflection across the x axis with rows (1 and 0) and (0 and −1).
- The other four matrices are products of those two matrices.

## What the checks show

- Each of the six matrices moves every corner k to corner p(k).
- The map respects multiplication for all 36 pairs of rearrangements (doing two rearrangements in a row matches multiplying the two matrices).
- All six matrices are different so the map loses no information.
- Every matrix keeps lengths unchanged.
- The traces are 2 for the identity and 0 for the three swaps and −1 for the two 3-cycles which matches the known character of the two-dimensional irreducible representation of S3.

## Best-guess answer

Sending the 3-cycle to the rotation matrix and the swap to the reflection matrix defines the wanted map because the two matrices satisfy the same rules as the two generators (the rotation applied three times is the identity and the reflection applied twice is the identity and the checks confirm all 36 products).
One detail about order: sympy writes p*q for "first p then q" so the matching matrix product is M(q)·M(p) and a system that composes the other way needs M(p)·M(q).
A Sage user can enter the same two matrices by hand and the exact Sage commands for building the map object were not tested.

The check file named s3_matrices.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
