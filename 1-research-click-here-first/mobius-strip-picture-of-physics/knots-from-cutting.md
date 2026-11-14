# A ribbon with three half twists turns into a knot when the ribbon splits down the middle

November 12 2026

## The question

The main document in this folder pictures the particles inside atoms as knots which means ribbons braided so tightly that the braid cannot come undone without a cut. The main document also says "a knot could be very unlikely to tie by accident" and suggests that knots need a forge which means a place violent enough to mash ribbons together.

This page asks whether a knot can also come from a much simpler event which is one twisted ribbon splitting lengthwise. Nothing gets tied in a lengthwise split because the ribbon only comes apart along its own middle line.

## The answer from published mathematics

The answer is yes and the answer is old news to mathematicians because paper-craft pages and mathematics courses describe the result.

- A band with one half twist (a Mobius strip) that is cut down the middle gives one long loop with no knot.
- A band with three half twists that is cut down the middle gives one long loop tied in a trefoil knot. A trefoil knot is the simplest knot there is and looks like a pretzel with three crossings.
- A band with five half twists gives a knot with five crossings and a band with seven half twists gives a knot with seven crossings.
- The edge of an uncut band with three half twists is already a trefoil knot which means the knot is present in the outline of the ribbon before any cut happens.

Three pages that describe the result are linked in the sources part at the bottom of this page.

## What the computer check confirmed

The chatbot built each band as a curve in a computer and did not rely on a picture. The program followed the middle line of the long loop that a center cut leaves behind and then worked out two standard knot numbers that mathematicians use to tell knots apart.

The first knot number is named the determinant and the second knot number comes from a formula named the Alexander polynomial. A loop with no knot gives 1 and 1. The trefoil knot gives 3 and 3. The five-crossing knot gives 5 and 11. The seven-crossing knot gives 7 and 43. The nine-crossing knot gives 9 and 171.

- One half twist gave 1 and 1 which means no knot.
- Three half twists gave 3 and 3 which matches the trefoil knot.
- Five half twists gave 5 and 11 which matches the five-crossing knot.
- Seven half twists gave 7 and 43 which matches the seven-crossing knot.
- Nine half twists gave 9 and 171 which matches the nine-crossing knot.
- The edge of the uncut band gave the same numbers as the cut loop for one and three and five and seven half twists.
- Looking at the three-half-twist loop from five other directions gave 3 and 3 every time which is what a true knot number has to do because a knot does not change when a person walks around the knot.

Three more checks fit the cutting guide inside the main document.

- A ribbon twisted the other way gave the mirror-image knot because every crossing flipped its handedness (the crossing total changed from minus 3 to plus 3 for three half twists). A left-handed trefoil knot cannot be turned into a right-handed trefoil knot without a cut.
- A cut at one third of the width of a band with three half twists gave a long loop that is a trefoil knot and a center strip with no knot.
- A band with an even number of half twists (two or four or six) gave two loops and each loop alone had no knot.

## A paper version to try

A person can tape two paper strips end to end to get one long strip because a long strip is easier to twist. Give one end three half twists and tape the two ends together. Cut along the middle of the band all the way around. One long loop comes out and the loop cannot be laid flat as a plain ring because the loop is tied in a trefoil knot. The chatbot did not try the cut with real paper.

## What this could mean for the ribbon picture

Here are four possibilities and each one is a what-if and not a proven piece of physics.

- Knots might not need tying. A ribbon with three half twists that splits lengthwise becomes a knot with no braiding step which could give the ribbon picture a second road to the knots that the main document uses for the particles inside atoms.
- The forge could still matter. The main document says removing or cutting a twist takes a violent event so a forge could be the place where ribbons get three half twists and where ribbons split.
- A ribbon with three half twists could count as a hidden knot. The edge of that ribbon is a trefoil knot before any cut which could mean a thrice-twisted ribbon already carries the long life of a knot.
- Mirror knots could picture matter and antimatter. The main document already pairs a left-handed strip with a right-handed strip. The left-handed and right-handed trefoil knots are a matching pair that cannot be turned into each other which fits the same idea one step up.

The count of half twists also sorts ribbons into families because one half twist gives no knot and three give the simplest knot and five and seven give the next knots. One possibility is that such a ladder could picture a family of heavier and heavier particles and nothing on this page tests that possibility.

## What stays unproven

- Nothing shows that space is built from ribbons or that a ribbon of space can split lengthwise.
- The page does not show how often a ribbon would pick up three half twists.
- The two knot numbers tell the knots on this page apart and two different knots can share the same two numbers in general. The match with published mathematics is the stronger evidence for the names of the knots.
- No other person has rerun the program which means the numbers from the program are unconfirmed.

## How to check this page

The program is named knots_from_cutting.py and sits in the folder boring-things/research-program-files/mobius-strip-calculations in this repository. The program needs only Python with the numpy package and takes about one minute.

## Sources

- An encyclopedia page that says a strip with three half twists divided lengthwise becomes a strip tied in a trefoil knot: https://en.wikipedia.org/wiki/M%C3%B6bius_strip
- A course page that lists what comes out for any number of half twists and says the edge of a band with three half twists is the trefoil knot: https://futurelearn.com/info/courses/flexagons/0/steps/48222
- A paper-craft page with photos of the cut bands with three and five half twists: https://mathcraft.wonderhowto.com/how-to/math-craft-monday-community-submissions-plus-make-mobius-strips-0131281

## Who made this page

An AI chatbot (Claude) ran the check and wrote this page.
