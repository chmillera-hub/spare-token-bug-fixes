# Calculations behind the Mobius strip document

These seven small Python programs produced the computer checks mentioned in the document and in the four finding pages beside the document. Each program needs only Python with the numpy package.

- cut_pieces_linking.py builds a band with a chosen number of half twists and slices the band lengthwise into equal strips and counts how many times each pair of resulting loops winds through each other.
- pinch_off_handedness.py checks that a plain loop hiding one right half twist and one left half twist splits crosswise into two Mobius strips of opposite handedness.
- entangled_pair_rules.py simulates two ribbon rules for entangled pairs and compares both rules with the measured quantum behavior.
- half_angle_from_directions.py tests whether the half-angle rule for entangled pairs comes out of evenly random directions in spaces with two to fifty dimensions.
- smallest_paper_strip.py checks that a strip 1.732 times as long as wide folds flat into a triangle Mobius strip with no stretching.
- dimension_followup.py gives exact formulas for the combined test score in two to five dimensions and checks the far-end average in two to six dimensions and compares two mixes of twist arrows that share the same average arrow.
- knots_from_cutting.py names the knot that a center cut leaves behind for bands with one to nine half twists by working out two standard knot numbers.
