# The half-angle rule can come from random directions in three dimensions

November 12 2026

## The question

The main document in this folder says that the half-angle rate for entangled pairs "was put in by assumption and was not derived from the shape of the ribbon". This page tests whether a simple rule about directions in space can produce the half-angle rate so that the rate no longer has to be put in as a formula.

## What the half-angle rate is

Entangled pairs are two particles created together and each particle goes to a detector which is a device that can be pointed in any direction. Experiments show that the share of pairs giving matching results depends on the angle between the two detectors. The measured share follows the half-angle rate which means the share equals the square of the cosine of half the angle. In plain numbers the share is 100 percent at an angle of 0 degrees and about 85 percent at 45 degrees and 50 percent at 90 degrees and about 15 percent at 135 degrees and 0 percent at 180 degrees.

## The rule that was tested

The rule uses three arrows because an arrow is the simplest way to picture a direction.

- The twist arrow is the direction of the twist of the far strip.
- The detector arrow is the direction the far detector points.
- The hidden arrow points in an evenly random direction at the moment of measurement. One possible picture is the flat face of a ribbon that tumbles freely so that the face is equally likely to point any way.

The far strip agrees with the twist arrow when the hidden arrow sits lower along the detector direction than the twist arrow does. "Lower along the detector direction" means that if the detector arrow points straight up then the tip of the hidden arrow is at a smaller height than the tip of the twist arrow.

## What the computer check found

The program ran one million random hidden arrows for each angle and also worked out the exact share with no randomness.

Finding 1. In a space with three dimensions the rule gives exactly the half-angle rate. The simulated shares matched the half-angle rate within 0.001 at every angle tested.

- At 22.5 degrees quantum physics gives 0.9619 and the rule in three dimensions gives 0.9619.
- At 45 degrees quantum physics gives 0.8536 and the rule gives 0.8536.
- At 67.5 degrees quantum physics gives 0.6913 and the rule gives 0.6913.
- At 135 degrees quantum physics gives 0.1464 and the rule gives 0.1464.

The match is exact because of an old proven fact about balls. When a ball is cut into slices of equal thickness like a loaf of bread every slice carries the same amount of outer skin. The fact means the height of an evenly random point on a ball is evenly spread between the bottom and the top. So the share of hidden arrows that sit lower than the twist arrow grows in a straight line with the height of the twist arrow and that height is the cosine of the angle. One half plus one half of the cosine of an angle is the same number as the square of the cosine of half the angle.

Finding 2. In a space with two dimensions the rule fails. A hidden arrow that is random around a circle gives a share that changes in a straight line with the angle (0.7500 at 45 degrees where experiments need 0.8536). Experiments rule out the straight line. This matters for the main document because the main document pictures randomness as the circling tip of a corkscrew and a circling tip is a random point on a circle.

Finding 3. In a space with four or more dimensions the rule overshoots. Physicists use a combined test score to judge entangled pairs. Any rule where the results are set in advance cannot score above 2.000 and quantum physics cannot score above 2.828 and experiments agree with 2.828.

- The rule in two dimensions scores 2.000.
- The rule in three dimensions scores 2.828.
- The rule in four dimensions scores 3.273.
- The rule in five dimensions scores 3.536.
- The rule in ten dimensions scores 3.940 and the score creeps toward 4.000 as the count of dimensions grows.

Three is therefore the only count of dimensions where this rule matches what experiments measure.

Finding 4. A full run of pairs in three dimensions matched quantum physics with detectors pointing anywhere in space and not only inside one flat plane. The run also showed that no message can be sent because the average result at the far end stayed at zero (within 0.001) no matter where the first detector pointed.

## What this could mean for the ribbon picture

The half-angle rate can now rest on two simpler assumptions in place of an assumed formula. The first assumption is that some hidden direction is evenly random in three dimensions at the moment of measurement. The second assumption is the lower-than rule described above.

The result also fits one sentence in the main document. The main document says a Mobius strip "may be the simplest flat thing that reaches into three directions of space". The rule on this page works only when the hidden direction has three directions of space to point into.

## What stays unproven

- The rule is still an assumption because nothing shows that space is built from ribbons or that a ribbon face tumbles evenly.
- The rule still needs the whole ribbon to respond as one object at the same instant because a proven result in physics says no rule with results set in advance can score above 2.000.
- The rule for a single particle has been known to physicists for decades as far as the chatbot knows. The chatbot did not search the published research to learn whether the comparison across two and three and four dimensions is already in print.
- No other person has rerun the program which means the numbers on this page are unconfirmed.

## How to check this page

The program is named half_angle_from_directions.py and sits in the folder boring-things/research-program-files/mobius-strip-calculations in this repository. The program needs only Python with the numpy package and prints every number on this page.

## Who made this page

An AI chatbot (Claude) ran the test and wrote this page.
