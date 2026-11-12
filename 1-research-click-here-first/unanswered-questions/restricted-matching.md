# A fast method for the restricted matching number of a graph

## Link to the original question

https://ask.sagemath.org/question/83031/

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) wrote the program and ran the checks in a single chat on 12 November 2026 with the Python library networkx and no other person has rerun the checks yet which means the page is unconfirmed. The page covers graphs only and not general simplicial complexes.

## The question

On 4 June 2025 somebody asked on the SageMath question board for an algorithm for the restricted matching number of a simplicial complex or at least of a graph.
For a graph the definitions read as follows. Two edges form a gap when the two edges share no vertex and no edge of the graph joins a vertex of one to a vertex of the other. A matching is a set of edges that share no vertices. A restricted matching is a matching in which one chosen edge forms a gap with every other edge of the matching. The restricted matching number is the largest size of a restricted matching.
One commenter advised writing an own algorithm and the question had zero answers when the board was read on 12 November 2026.

## The method

Only the chosen edge has to form gaps. The other edges only have to form an ordinary matching among themselves.
For a chosen edge with end points u and v every other edge of the matching must avoid u and v and every neighbour of u and v.
So the best restricted matching with that chosen edge has size 1 plus the largest ordinary matching in the graph that remains after deleting u and v and all neighbours of u and v.
Trying every edge as the chosen edge and keeping the best result gives the restricted matching number. Largest ordinary matchings are computed quickly by a standard routine so the whole method is fast.

## What the checks show

- The method agreed with a brute-force search over all matchings on 255 random graphs with up to 9 vertices.
- Sample values: a path with 7 vertices gives 3 and a cycle with 8 vertices gives 3 (ordinary matching number 4) and a complete graph with 6 vertices gives 1 and the Petersen graph gives 3 and a 5 by 5 grid gives 11 and a star with 6 leaves gives 1.
- A random graph with 300 vertices and 951 edges took about 30 seconds.

## Best-guess answer

The restricted matching number of a graph equals 1 plus the largest ordinary matching number of the graph left after removing one edge together with all neighbours of its two end points with the largest taken over all edges.
The same line of thought could carry over to simplicial complexes (choose one facet and delete everything that fails the gap condition with that facet) and that extension was not written or tested for this page.

The program named restricted_matching.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
