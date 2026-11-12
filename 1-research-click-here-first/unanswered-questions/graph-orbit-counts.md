# Counting graphs up to relabeling with the symmetric group (orbit counts by number of edges)

## Link to the original question

https://ask.sagemath.org/question/83156/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) wrote the program and ran the checks in a single chat on 12 November 2026 and no other person has rerun the checks yet which means the page is unconfirmed. The question was short on detail so the page computes two readings of the question.

## The question

On 18 June 2025 somebody asked on the SageMath question board how to compute the set of orbits of the symmetric group S_n acting on collections of k pairs of vertices in order to count graphs that are the same up to renaming the vertices.
The asker could count the collections and was stuck on counting the orbits.
One commenter asked for code and the question had zero answers when the board was read on 12 November 2026.

## The method

The counting lemma of Burnside says that the number of orbits equals the average number of collections left unchanged by a rearrangement of the vertices.
Rearrangements with the same cycle lengths leave the same number of collections unchanged so the program visits one rearrangement per cycle type (one per partition of n) and weights the result by the number of rearrangements of that type.
For one rearrangement the program finds the cycles of the induced rearrangement of vertex pairs and a collection is left unchanged exactly when the collection is built from whole cycles.

## What the checks show

- Reading 1 (simple graphs: k different pairs of different vertices): the formula matched a brute-force count for n = 3 and n = 4.
- Reading 1 for n = 4 gives 1 and 1 and 2 and 3 and 2 and 1 and 1 graphs with 0 to 6 edges (total 11) and for n = 5 the total is 34 and for n = 6 the total is 156 and for n = 7 the total is 1044. All four totals equal the known numbers of graphs on 4 to 7 unlabeled vertices and every sequence reads the same forwards and backwards.
- Reading 2 (pairs may repeat and a pair may use the same vertex twice): the formula matched a brute-force count for n = 3 and n = 4 and gives 1 and 2 and 7 and 22 and 69 and 198 and 550 for n = 5 with k from 0 to 6.

## Best-guess answer

The orbit counts come from the Burnside average over cycle types and no list of orbits has to be built.
The Python program computes either reading through two switches (loops and repeats) and needs only a fraction of a second for n = 7.

The program named graph_orbits.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
