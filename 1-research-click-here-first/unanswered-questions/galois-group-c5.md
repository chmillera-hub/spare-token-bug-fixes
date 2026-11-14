# The Galois group of the eigenvalue field of the 5-cycle graph as a permutation group

## Link to the original question

https://ask.sagemath.org/question/87751/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the checks in a single chat on 12 November 2026 with the Python libraries networkx and sympy and no other person has rerun the checks yet which means the page is unconfirmed. No Sage command was tested because Sage was not installed.

## The question

On 9 February 2026 somebody asked on the SageMath question board how to turn the Galois group of a number field into a permutation group.
The posted program takes the eigenvalues of the 5-cycle graph (five dots joined in a ring) and builds a number field from the eigenvalues and calls K.galois_group() and then calls X.as_permutation_group() which fails.
Comments suggested PermutationGroup(X.gens()) and the question had zero answers when the board was read on 12 November 2026.

## What the checks show

- The posted program never gives the name X to anything. The line K.galois_group() computes the group and throws the result away so the next line fails because X does not exist. Writing X = K.galois_group() is the first repair.
- The characteristic polynomial of the 5-cycle is (x − 2)·(x² + x − 1)² so the eigenvalues are 2 and (−1 + √5)/2 and (−1 − √5)/2.
- The eigenvalue 2 is a rational number so the field comes from x² + x − 1 alone and equals the rational numbers with √5 added (a field of degree 2).
- sympy returned the Galois group of x² + x − 1 as a permutation group with one generator that swaps the two roots (order 2).
- A direct check confirmed that replacing √5 by −√5 turns one eigenvalue into the other.

## Best-guess answer

The Galois group in the question is the group with two elements: the identity and the swap of the two irrational eigenvalues.
The repaired Sage lines worth trying are X = K.galois_group() followed by PermutationGroup(X.gens()) as the comment suggested and those lines were not tested for this page.
A reader without Sage can get the permutation group in Python with sympy:

p = sympy.Poly(x**2 + x - 1, x)
G, _ = p.galois_group()

The check file named galois_c5.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
