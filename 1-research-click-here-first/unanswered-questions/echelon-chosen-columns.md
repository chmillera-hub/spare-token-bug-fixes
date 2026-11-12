# Row-reducing a matrix so the identity appears on any chosen columns

## Link to the original question

https://ask.sagemath.org/question/83654/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with the Python library sympy and no other person has rerun the checks yet which means the page is unconfirmed. No Sage command was tested because Sage was not installed.

## The question

On 1 August 2025 somebody asked on the SageMath question board how to get an echelon form of a matrix G with k rows and n columns (k smaller than n and rank k) where the k by k identity matrix sits on any chosen set of k columns such as the last k columns.
The built-in command G.echelon_form() puts the identity on the first columns.
The question had zero answers and zero comments when the board was read on 12 November 2026.

## The method

Take the k by k block B made of the chosen columns of G and multiply G from the left by the inverse of B.
The product has the identity on the chosen columns because the inverse of B times B is the identity and the product has the same row space as G because multiplying from the left by an invertible matrix only recombines rows.
The method works exactly when the chosen columns are linearly independent.

## What the checks show

- For a random 3 by 7 whole-number matrix the method put the identity on the columns (4 and 5 and 6) and on (1 and 3 and 6) and on (6 and 0 and 2) and the row space stayed the same in all three cases. The order of the chosen columns decides which row gets which 1.
- The same method with arithmetic modulo 2 worked for a 4 by 8 matrix over the field with two elements (the setting of binary codes).
- Choosing two linearly dependent columns raised a clear error because no such form exists then.

## Best-guess answer

In Python with sympy:

block = G.extract(list(range(k)), list(cols))
E = block.inv() * G

Over a field with p elements the line becomes (block.inv_mod(p) * G) with every entry reduced modulo p.
In Sage the matching line worth trying is G.matrix_from_columns(cols).inverse() * G and that line was not tested for this page.

The check file named echelon_columns.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
