# The smallest paper Mobius strip is 1.732 times as long as wide

November 12 2026

## The question

The main document in this folder says that "a paper strip that is made too short compared with the width of the strip cannot hold the half twist without tearing or passing through the surface of the same strip". The main document then suggests that a particle made of ribbon "could therefore have a smallest possible size". This page asks how short the strip can get and puts a number on the answer.

## The answer from published mathematics

A smooth paper Mobius strip that does not pass through its own surface has to be more than 1.732 times as long as wide. The number 1.732 is the square root of 3. Mathematicians guessed this limit in 1977 and a full proof was published in January 2025 in a mathematics journal named Annals of Mathematics. The proof is here: https://arxiv.org/abs/2308.12641

The same proof shows what the tightest strip looks like. A strip that gets closer and closer to the limit gets closer and closer to a flat triangle with three equal sides and three layers of paper. The tightest Mobius strip is therefore not a round loop.

## What the computer check confirmed

The chatbot did not check the proof because the proof is advanced mathematics. The chatbot checked the flat triangle with a small program because a flat fold can be checked with simple geometry.

- The program took a strip with a width of 1 and a length of 1.732 and folded the strip flat along three slanted creases. Each crease runs from one long edge to the other long edge at 60 degrees and the three creases form a zigzag.
- The two short ends of the strip landed on exactly the same line with one end flipped (the gap was 0.0). The flipped join is the join that makes a Mobius strip. The unflipped ends missed each other by a full strip width (a gap of 1.0).
- The folding stretched nothing because the distance between nearby points inside each piece changed by less than one part in a thousand million million.
- The folded shape is a triangle with three equal sides. The height of the triangle equals the width of the strip and each side is 1.155 times the width of the strip.

## A paper version to try

A person can cut a strip 10 centimeters wide and 17.3 centimeters long. The first crease runs from the bottom left corner up to the top edge at 60 degrees. The second crease runs from that spot on the top edge down to the bottom edge at 60 degrees. The third crease runs from that spot on the bottom edge up to the top right corner. Folding along the three creases in a zigzag stacks the paper into one triangle and the two short ends then meet along one side of the triangle with one end flipped. Taping the two short ends together makes the triangle Mobius strip. The chatbot did not try the fold with real paper.

## What this could mean for the ribbon picture

The smallest size in the main document now has a number. A ribbon that behaves like paper could not be shorter than 1.732 widths which means a ribbon particle with a fixed width could not shrink below a length of 1.732 widths. The tightest ribbon particle could look like a flat three-layer triangle and not like a round loop.

## What stays unproven

- The limit holds for paper which means a sheet that cannot stretch and cannot pass through its own surface. Nobody knows whether a ribbon of space would follow paper rules and a stretchy ribbon could be made shorter.
- The chatbot checked only the flat triangle and relied on the published proof for the claim that no smooth strip can be shorter.
- No other person has rerun the program which means the numbers from the program are unconfirmed.

## How to check this page

The program is named smallest_paper_strip.py and sits in the folder boring-things/research-program-files/mobius-strip-calculations in this repository. The program needs only Python with the numpy package.

## Who made this page

An AI chatbot (Claude) ran the check and wrote this page at the request of Charles.
