# Calculations behind the Mobius strip document

These three small Python programs produced the computer checks mentioned in the document. Each program needs only Python with the numpy package.

- cut_pieces_linking.py builds a band with a chosen number of half twists and slices the band lengthwise into equal strips and counts how many times each pair of resulting loops winds through each other.
- pinch_off_handedness.py checks that a plain loop hiding one right half twist and one left half twist splits crosswise into two Mobius strips of opposite handedness.
- entangled_pair_rules.py simulates two ribbon rules for entangled pairs and compares both rules with the measured quantum behavior.
