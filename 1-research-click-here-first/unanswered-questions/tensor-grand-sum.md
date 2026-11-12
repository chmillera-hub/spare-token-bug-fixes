# The sum of every entry of a repeated tensor product of [z², c]

One AI model (Claude) ran the checks in a single chat on 12 November 2026 and no other person has rerun the checks yet which means the page is unconfirmed.

## The question

On 18 April 2026 somebody asked on the SageMath question board (ask.sagemath.org question number 88560) how to take the tensor product of the pair [z², c] with itself again and again and then add up every entry (the grand sum) and then look at the limit as the number of copies n grows without end.
One commenter asked for clarification and the question had zero answers when the board was read on 12 November 2026.

## What the checks show

The tensor product of n copies of [z², c] has 2^n entries and each entry is a product that picks either z² or c from every copy.
Adding all 2^n entries therefore gives the same result as multiplying out (z² + c) times itself n times.
A program built the tensor products for n = 1 to 7 (up to 128 entries) and the sum of all entries equaled (z² + c)^n exactly every time.

## Best-guess answer

The grand sum of n copies equals (z² + c)^n so nobody needs to build the huge tensor product to get the sum.
The limit as n grows depends only on the single number w = z² + c:

- The grand sum shrinks to 0 when the size of w is less than 1 (for example w = 1/2 or w = i/2).
- The grand sum stays at 1 forever when w equals exactly 1.
- The grand sum has no limit when the size of w equals 1 and w is not 1 (for example w = −1 flips between −1 and 1).
- The grand sum grows without end when the size of w is larger than 1 (for example w = 3/2).

The boundary where the size of z² + c equals 1 is a different boundary from the famous Mandelbrot picture because the Mandelbrot picture feeds each result back into z and the grand sum only raises one fixed number to higher powers.

The check file named grand_sum.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
