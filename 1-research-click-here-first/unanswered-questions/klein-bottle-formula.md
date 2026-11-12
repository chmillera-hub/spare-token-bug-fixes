# Is a four-coordinate formula Lawson's Klein bottle (the checks say torus)

One AI model (Claude) ran the checks in a single chat on 12 November 2026 and no other person has rerun the checks yet which means the page is unconfirmed.

## The question

Somebody asked on the Wikipedia Reference Desk for mathematics (in a section dated 11 December with the year not shown) whether the formula below describes Lawson's Klein bottle inside the three-dimensional sphere.
No reply appeared in the copy of the page read on 12 November 2026 and the copy may be an old stored copy.

The formula: w = cos θ cos φ and x = cos θ sin φ and y = sin θ cos φ and z = sin θ sin φ.
A Klein bottle is a closed surface with only one side and a torus is the surface of a ring doughnut which has two sides.

## What the checks show

Lawson's family of surfaces (written here from memory and not looked up today) uses two whole numbers m and k in the formula (cos mx cos y and sin mx cos y and cos kx sin y and sin kx sin y).

- The formula in the question equals the family member with m = 1 and k = 1 exactly (difference zero at 100000 random points) after renaming x as φ and y as θ.
- Every point of the formula in the question satisfies w times z = x times y which is the equation of a torus inside the sphere (the Clifford torus).
- The formula in the question gives the same point at (θ + π and φ + π) as at (θ and φ). That repeat keeps the handedness of the surface so the result is still a two-sided torus covered twice.
- The family member with m = 2 and k = 1 gives the same point at (x + π and −y) as at (x and y). That repeat flips the handedness of the surface (the minus sign in front of y) which is exactly what makes a one-sided Klein bottle.

## Best-guess answer

The formula in the question describes a torus and not a Klein bottle.
Lawson's Klein bottle is the family member with m = 2 and k = 1 which means the formula w = cos 2x cos y and x-coordinate = sin 2x cos y and third coordinate = cos x sin y and fourth coordinate = sin x sin y.
The naming of Lawson's family rests on memory so a reader who needs certainty could compare with Lawson's 1970 paper on minimal surfaces in the three-dimensional sphere.

The check file named lawson_check.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
