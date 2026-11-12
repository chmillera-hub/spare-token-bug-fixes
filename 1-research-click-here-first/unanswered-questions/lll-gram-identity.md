# Why the PARI function qflllgram returned an identity matrix

## Link to the original question

https://ask.sagemath.org/question/83810/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with PARI version 2.15.4 through the Python package cypari on small made-up lattices and no other person has rerun the checks yet which means the page is unconfirmed. The checks did not use the number field data from the question and did not run inside Sage.

## The question

On 13 August 2025 somebody asked on the SageMath question board why calling qflllgram on a Gram matrix G (the table of dot products of the basis vectors of a lattice) returned an identity matrix while handing the same Gram matrix to the function qflll gave "the expected reduced basis".
The asker computes reduced bases of log-unit lattices of number fields.
One commenter asked for runnable code and the question had zero answers when the board was read on 12 November 2026.

## What the checks show

- The function qflllgram does not return a reduced basis. The function returns a whole-number matrix T (a change of basis) and the reduced basis is the old basis multiplied by T.
- For a basis that was already short and nearly at right angles qflllgram returned the identity matrix. An identity matrix therefore means "the basis handed in is already reduced" and not "something went wrong".
- For the same lattice described by a skewed basis (vector lengths 1.005 and 7.428) qflllgram returned a matrix with the entries 1 and −7 and 0 and 1 and multiplying the skewed basis by that matrix gave short vectors again (lengths 1.005 and 1.158).
- The function qflll expects the basis vectors themselves as columns. Calling qflll on the basis returned the same matrix as calling qflllgram on the Gram matrix.
- Calling qflll on the Gram matrix returned a different matrix (entries 15 and −82 and −2 and 11) because qflll then treats the columns of the Gram matrix as if those columns were basis vectors which describes a different lattice.

## Best-guess answer

One possibility that fits the report is that the log-unit basis from PARI was already reduced so qflllgram correctly answered with the identity matrix and the output of qflll on the Gram matrix only looked like a result because qflll was reducing a different lattice.
The reduced basis comes from multiplying the matrix of basis vectors by the matrix that qflllgram returns and the reduced Gram matrix is T transposed times G times T.

The check file named lll_gram.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
