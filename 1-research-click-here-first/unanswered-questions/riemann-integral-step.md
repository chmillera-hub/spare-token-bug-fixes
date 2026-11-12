# The step in Riemann's 1859 paper that turns one integral into a loop integral

One AI model (Claude) wrote the explanation and ran the number check in a single chat on 12 November 2026 and no other person has checked the work yet which means the page is unconfirmed.

## The question

Somebody asked on the Wikipedia Reference Desk for mathematics (in a section dated 10 December with the year not shown) how Riemann gets from the first formula below to the second formula and whether the second integral is a Hankel-type loop integral.
No reply appeared in the copy of the page read on 12 November 2026 and the copy may be an old stored copy.

First formula: Π(s−1) ζ(s) equals the integral from 0 to infinity of x^(s−1) / (e^x − 1) dx.
Second formula: 2 sin(πs) Π(s−1) ζ(s) equals i times the integral "from +infinity to +infinity" of (−x)^(s−1) / (e^x − 1) dx.
Riemann's symbol Π(s−1) means the same number as the modern Gamma(s).

## The answer in words

The second integral is a loop integral of the Hankel type because the path comes in from far out on the positive side just above the positive real axis and circles the origin counterclockwise and goes back out just below the positive real axis.

The power (−x)^(s−1) means e raised to (s−1) times log(−x) and log(−x) is chosen to be an ordinary real number when x is negative.
That choice forces two different values along the positive real axis because −x equals x times e^(−iπ) just above the axis and x times e^(+iπ) just below the axis.

- Just above the axis the power equals e^(−iπ(s−1)) times x^(s−1) and the path runs inward from infinity to 0.
- Just below the axis the power equals e^(+iπ(s−1)) times x^(s−1) and the path runs outward from 0 to infinity.
- The small circle around the origin contributes nothing in the limit when the real part of s is larger than 1.

Adding the two straight pieces gives (e^(iπ(s−1)) − e^(−iπ(s−1))) times the first integral.
The bracket equals 2i sin(π(s−1)) which equals −2i sin(πs).
Multiplying by the i in front turns −2i sin(πs) into 2 sin(πs) because i times −2i equals 2.
The first integral equals Π(s−1) ζ(s) so the loop formula follows.

The loop integral has a bonus because the loop never touches the origin and so the loop integral makes sense for every complex s which is how Riemann extends ζ(s) beyond the region where the first integral works.

## The number check

A program computed both sides to 25 digits at five test values of s.
The two sides agreed to at least 21 digits at s = 2.5 and s = 3.7 and s = 1.5 + 2i and s = −1.5 (a value where the first integral does not even converge).
The two sides agreed to 8 digits at s = 0.5 + 14.134725i where the numbers are large.

The check file named riemann_step.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
