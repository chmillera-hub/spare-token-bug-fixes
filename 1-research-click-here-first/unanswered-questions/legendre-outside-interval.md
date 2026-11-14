# A workaround for associated Legendre functions outside the interval from −1 to 1

## Link to the original question

https://ask.sagemath.org/question/88040/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with the Python library mpmath and no other person has rerun the checks yet which means the page is unconfirmed. The checks ran in plain Python and not inside Sage.

## The question

On 2 March 2026 somebody asked on the SageMath question board whether the associated Legendre functions of the first and second kind (the versions used for x larger than 1) are missing from SageMath 10.8 while the Ferrers versions (the versions used between −1 and 1) exist and whether a workaround exists.
Two comments suggested looking at other libraries and the question had zero answers when the board was read on 12 November 2026.

## What the checks show

The library mpmath has the functions legenp and legenq and both accept the setting type=3 which selects the versions for x outside the interval from −1 to 1. The library mpmath is one of the libraries that ships inside SageMath so the workaround needs no extra installation as far as the page author knows.

- The value of legenq(ν, μ, x, type=3) matched the hypergeometric formula for Q (formula 14.3.7 of the Digital Library of Mathematical Functions written from memory) to at least 30 digits at five test points including non-whole values ν = 2.5 and μ = 0.5.
- Q with ν = 0 at x = 2 equaled 0.5·log((x+1)/(x−1)) exactly and Q with ν = 1 at x = 2 equaled (x/2)·log((x+1)/(x−1)) − 1 to 31 digits.
- P with ν = 1 and μ = 1 at x = 2 equaled √(x²−1) and P with ν = 2 and μ = 2 at x = 2 equaled 3·(x²−1).
- The setting type=2 gave the Ferrers version: P with ν = 1 and μ = 1 at x = 0.3 equaled −√(1−x²).

## Best-guess answer

A workaround worth trying inside Sage is:

import mpmath
mpmath.legenq(nu, mu, x, type=3)
mpmath.legenp(nu, mu, x, type=3)

The results are numbers and not symbolic expressions so the workaround fits number checks of formulas and does not fit symbolic manipulation.
The page did not test formula 14.3.19 itself and did not check whether the functions are missing from Sage 10.8.

The check file named legendre_q.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
