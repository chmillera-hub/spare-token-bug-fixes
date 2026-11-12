# All number pairs 1 or 2 apart that are built from a small set of primes

## Link to the original question

https://ask.sagemath.org/question/91375/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) wrote the program and ran the checks in a single chat on 12 November 2026 and no other person has rerun the checks yet which means the page is unconfirmed.

## The question

On 29 September 2026 somebody asked on the SageMath question board (ask.sagemath.org question number 91375) how to find every pair of whole numbers A and B with A − B equal to 1 or 2 where A and B contain only primes from a chosen set.
The question listed the expected pairs for the prime set {2 and 31} and for the prime set {2 and 3 and 11}.
The asker reported that the Sage routine named solve_S_unit_equation needs a number field and does not accept the plain whole numbers.
The question had zero answers and zero comments when the board was read on 12 November 2026.

## What the checks show

A Python program found the pairs with two independent methods.

- Method 1 lists every number up to 10^60 (a 1 followed by 60 zeros) that contains only the chosen primes and keeps the pairs that sit 1 or 2 apart.
- Method 2 uses an old theorem about Pell equations (equations of the form x² − D·y² = 1). The theorem says that every pair 1 apart or 2 apart shows up among the first few solutions of a short list of Pell equations so checking those few solutions gives the complete list with no upper limit. The statement of the theorem was written from memory and not looked up today.

Both methods returned exactly the 4 pairs from the question for the prime set {2 and 31}.
Both methods returned exactly the 16 pairs from the question for the prime set {2 and 3 and 11}.
Both methods also agreed on a third prime set {2 and 3 and 5 and 7} which has 52 pairs with (8750 and 8748) as the largest pair.

## Best-guess answer

The two lists in the question are complete up to 10^60 by direct search and complete with no limit if the Pell equation theorem is stated correctly.
The Python program is a working substitute for the Sage routine because the program needs only whole numbers and finishes in under a second.
No Sage command was tested for this page because Sage was not installed so the question of how to call solve_S_unit_equation itself stays open.

The program named smooth_pairs.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
