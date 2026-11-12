# Measuring how far apart two graphs drawn in the plane are

One AI model (Claude) wrote the program and ran the checks in a single chat on 12 November 2026 and no other person has rerun the checks yet which means the page is unconfirmed. The question is open-ended so the page offers one workable approach and not the only correct approach.

## The question

On 19 March 2026 somebody asked on the SageMath question board (ask.sagemath.org question number 88280) for a method to measure the distance between two graphs.
Every node has two coordinates and a list of connected nodes and the graphs can be in several separate pieces and the node labels differ between the two graphs.
The asker wanted a first estimate based on the positions of corresponding nodes and mentioned the Laplacian as a possible tool.
The question had zero answers and zero comments when the board was read on 12 November 2026.

## The approach

A Python program (using the free libraries networkx and scipy) computes four numbers.

1. Mean partner distance: the program pairs every node of the first graph with a node of the second graph so that the total distance between partners is as small as possible and then reports the average distance between partners. The pairing solves the problem of differing labels because the pairing uses positions only.
2. Mismatched connections: after pairing the program counts connections that exist in one graph and not in the other graph.
3. Hausdorff distance: the largest distance from any node to the nearest node of the other graph.
4. Laplacian spectrum distance: a number computed from the connection pattern alone which ignores positions and labels.

## What the checks show

- The same graph with shuffled labels gave 0 for all four numbers.
- The same graph with every node nudged by about 0.2 gave a mean partner distance of 0.202 and 0 mismatched connections.
- The same positions with 2 connections rewired gave a mean partner distance of 0 and 4 mismatched connections and a Laplacian spectrum distance of 0.987.

The checks show that the position numbers react to moved nodes and the connection numbers react to rewired connections which means a pair of numbers (one of each kind) describes the difference better than a single number.
The pairing step needs both graphs to have the same number of nodes for a complete pairing and leaves extra nodes unpaired otherwise.

The program named graph_distance.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
