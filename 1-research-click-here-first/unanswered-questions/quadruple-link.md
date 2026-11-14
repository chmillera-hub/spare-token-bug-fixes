# Linking two formulas for special Pythagorean quadruples (and why the solver choked)

## Link to the original question

https://ask.sagemath.org/question/85649/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with the Python library sympy and no other person has rerun the checks yet which means the page is unconfirmed.

## The question

On 28 October 2025 somebody asked on the SageMath question board how to connect two descriptions of whole-number solutions of a² + b² + c² = d² that also satisfy d + a = c².
The first description uses four numbers u and v and s and t and the second description uses two numbers m and n.
The asker put eleven equations with N = 65 into the Sage solver and the solver failed and a later attempt reported "the dimension of the ideal is 7".
The question had zero answers when the board was read on 12 November 2026.

## What the checks show

- The formulas in m and n satisfy a² + b² + c² = d² for every m and n (the difference expands to zero).
- The formulas in m and n satisfy d + a = c² for every m and n (the difference expands to zero).
- The extra equation a = 3·(3N − 3)/6 + 1 turns into N = (4m + 1)·(4n + 1). The number N is therefore tied to m and n by a simple product.
- For N = 65 the product rule leaves exactly four whole-number pairs: (m and n) = (0 and 16) or (1 and 3) or (3 and 1) or (16 and 0).
- Each pair gives one quadruple: (97 and −1054 and 34 and 1059) and (97 and 14 and 14 and 99) and (97 and 374 and 22 and 387) and (97 and 9506 and 98 and 9507). All four pass both equations.
- Each quadruple has exactly 4 whole-number choices of (u and v and s and t). For example (m and n) = (1 and 3) matches (u and v and s and t) = (−7 and 7 and 1 and 0).

## Best-guess answer

The link between the two descriptions is a short chain: split N into two factors of the form 4m + 1 and 4n + 1 and compute a and b and c and d from m and n and then find u and v and s and t from u² + v² = (d + a)/2 and s² + t² = (d − a)/2 with b and c picking out the matching signs.
One possibility for the solver failure is that two of the eleven equations are identities that add no information so the system has more freedom than a general solver expects and searching whole numbers directly (as the program does) avoids the problem.

The check file named quadruple_link.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
