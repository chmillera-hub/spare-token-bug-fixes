# Joining twists: a left-handed and a right-handed Mobius strip cancel while two left-handed strips add

November 15 2026

## The question

The main document in this folder now pictures an electron as the half twist of a Mobius strip. The twist of a left-handed Mobius strip could be an ordinary electron and the twist of a right-handed Mobius strip could be the mirror-image partner of the electron which physicists call a positron. This page asks what happens when two Mobius strips join into one strip. The page compares a left-handed strip joining a right-handed strip with two left-handed strips joining each other.

## How the strips were joined

The computer cut each Mobius strip once across the width and joined the cut ends straight across so the parts became one longer closed band. No extra flip was added at a joint. A joint taped with one end flipped over would add one more half twist and would change every result on this page.

The program built each joined band as points in space and then measured three things. The program checked whether the band has one side or two sides and counted the edges and counted how many times the edges wind through each other.

## Result one: the shape of the joined band

- One left-handed strip alone has 1 half twist and one side and one edge. One right-handed strip alone is the mirror image.
- A left-handed strip joined to a right-handed strip has 0 half twists. The joined band is a plain loop with two sides and two edges and the two edges do not wind through each other at all. The two twists cancel completely.
- A left-handed strip joined to a left-handed strip has 2 half twists which is one full twist. The joined band has two sides and two edges and the two edges wind through each other once. The full twist cannot be removed without a cut because the two edges are linked like two links of a chain.
- A right-handed strip joined to a right-handed strip is the mirror image of two left-handed strips joined.
- Two left-handed strips and one right-handed strip joined together have 1 left-handed half twist. The joined band is a left-handed Mobius strip again because one left twist and the right twist cancel and one left twist is left over.
- Three left-handed strips joined have 3 half twists and one side. Four left-handed strips joined have 4 half twists and two sides.
- Two left-handed strips and two right-handed strips joined have 0 half twists and make a plain loop.

So the joined band is not a mess in either case. The joined band follows one simple rule which is that half twists add like numbers with a plus or minus sign. A left twist counts as minus one and a right twist counts as plus one and the joined band holds the sum.

## Result two: the energy in a simple elastic model

The second test treated the band like a springy rod in which twisting costs energy and bending into a loop costs energy. The twist was free to spread along the joined band. The two starting strips each had a length of 1 and the joined band had a length of 2.

- Left joined to right: the twist energy fell from 9.87 to 0.00 as the two opposite twists spread into each other. All of the twist energy was freed (100 percent). The joined band settled into a plain relaxed loop.
- Left joined to left: the twist energy settled at 9.87 which equals the twist energy of the two separate strips. None of the twist energy was freed (0 percent). One full twist spread over a band of double length stores the same twist energy as two half twists on two bands of single length.
- The bending energy fell by the same amount in both cases (from 39.48 to 9.87) because one large loop is bent more gently than two small loops. Handedness made no difference to the bending energy.

## How the results line up with measured physics

- Twists adding like signed numbers matches electric charge because electric charge also adds like signed numbers and the total electric charge never changes in any measured reaction.
- Left joined to right matches an electron meeting a positron. A real electron and a real positron destroy each other and all of the energy leaves as light. The joined band lost all of the twist and all of the twist energy and the main document pictures an untwisted loop as carrying only ripples.
- Left joined to left matches two electrons. Two real electrons never destroy each other and the total charge stays at two. The joined band kept both twists locked in and freed no twist energy.
- Sides match a known rule about pairs. A band with an odd number of half twists has one side so an ant needs two laps to return right side up. A band with an even number of half twists has two sides so one lap is enough. Real particles follow the same odd and even rule because one electron needs two full turns to look the same while a pair of electrons acting together needs one full turn. Paired electrons acting as one object are what make some metals carry electricity with no resistance at very low temperatures.
- A real electron can also merge with a proton inside the core of some atoms. The merged pair becomes a neutron which has no charge and one very light fast particle called a neutrino flies off. The neutrino flying off echoes the main document where new simple strips leave as very light fast particles.

## Where the results strain

- Two real electrons push each other apart and no particle with the charge of two electrons and the lightness of an electron has ever been found. The ribbon picture would need a reason why two left-handed strips rarely join or why the joined band quickly splits back into two left-handed strips.
- The elastic model is a springy rod and is not a paper ribbon. A real paper ribbon links twisting and bending together so the energy numbers for paper could differ.
- The joining was straight across. Nobody knows whether strips of space would join straight across or with a flip.
- The tests show that the twist counting matches charge counting. The tests do not show why a twist would push or pull on another twist the way electric charges push and pull on each other.

## A paper version to try

A person can make two Mobius strips from paper with one twisted to the left and one twisted to the right. Cutting each strip once across the width and taping the four cut ends into one long loop with no extra flip could give a plain loop with no twist. Doing the same with two left-handed strips could give a loop with one full twist. Cutting the loop with one full twist down the middle could give two loops linked like a chain which shows that the full twist was locked in. The chatbot did not try the paper version with real paper.

## How to check this page

The program is named twist_joining.py and sits in the folder boring-things/research-program-files/mobius-strip-calculations in this repository. The program needs only Python with the numpy package. No other person has rerun the program which means every number on this page is unconfirmed.

## Who made this page

An AI chatbot (Claude) ran the tests and wrote this page.
