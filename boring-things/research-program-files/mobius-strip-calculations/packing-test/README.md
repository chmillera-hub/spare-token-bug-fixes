# Programs for the packing test

An AI chatbot (Claude) wrote these programs on 14 November 2026 for the page named packing-test.md in the Mobius strip folder.

- shapes.py builds point models of the six shapes and the other programs that start with a plain name load shapes.py with the line "from shapes import".
- blocked-space.py measures how much space one piece blocks for a second piece at a random angle.
- random-placement.py places pieces at random spots and angles with no gravity until no more pieces fit.
- stacking-step.py finds the smallest step at which identical copies can be stacked.
- stack-spacing.py measures how close two stacks can stand side by side.
- pour-and-shake.py drops rigid pieces into a bin under gravity and jostles the pile and needs the physics library named pybullet.
- pour-and-shake-finer-steps.py is the same program with finer physics steps for the flat shapes.
- pour-and-shake-big-bin.py is the version used for the big bin. The program pours pieces in layers from a low height and can mix two shapes and measures the packing in the middle of the pile away from the walls.
