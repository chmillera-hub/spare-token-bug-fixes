# Where the time goes in the algorithm of Cornacchia for writing N as a sum of two squares

## Link to the original question

https://ask.sagemath.org/question/85618/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the timings in a single chat on 12 November 2026 in Python with the library sympy and no other person has rerun the timings yet which means the page is unconfirmed. The cost statements in the last section come from standard number theory written from memory.

## The question

On 25 October 2025 somebody asked on the SageMath question board for the computational cost of the algorithm of Cornacchia.
The asker hopes to factor a number N by writing N as a sum of two squares and posted a short Sage program that returned (23 and 14) for N = 725.
One commenter pointed to timing tools and the question had zero answers when the board was read on 12 November 2026.

## How the algorithm splits into two steps

Step 1 finds a square root of −1 modulo N (a number r with r·r + 1 divisible by N).
Step 2 runs the division steps of Euclid on N and r until the remainder drops below the square root of N.

## What the timings show

The Python version reproduced the example from the question (23 and 14 for N = 725).

When N is a prime number:

- At 64 bits step 1 took 0.28 milliseconds and step 2 took 0.004 milliseconds.
- At 1024 bits step 1 took about 22 milliseconds and step 2 took 0.19 milliseconds.
- At 2048 bits step 1 took about 160 to 200 milliseconds and step 2 took 0.9 milliseconds.

Step 2 is always cheap and step 1 dominates even for a prime N.

When N is a product of two unknown primes the library routine for step 1 slowed down sharply (about 1 millisecond at 40 bits and about 90 milliseconds at 64 bits and about 675 milliseconds at 72 bits) while step 2 stayed under 0.01 milliseconds.

A last check showed why step 1 is the hard part for a product of two primes: two unrelated square roots of −1 modulo N = 1000033 · 1000037 gave the factor 1000033 through one greatest common divisor calculation.

## Best-guess answer

Step 2 costs about the same as one greatest common divisor calculation which grows roughly with the square of the number of digits.
Step 1 costs a modest power of the number of digits when N is prime.
Step 1 for a composite N is as hard as factoring N because the ability to find square roots modulo N hands over the factors (as the last check shows) so every known general method for step 1 factors N first.
The plan in the question therefore runs in a circle because the algorithm of Cornacchia needs the factors of N (or something equally hard to get) before the algorithm can produce the two squares.

The timing file named cornacchia_cost.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
