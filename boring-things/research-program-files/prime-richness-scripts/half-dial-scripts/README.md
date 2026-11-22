# Programs that recheck the page half-dial-questions.md

> **About this page:** One AI model (Claude) wrote these programs on 22 November 2026 to compute and recheck every figure on the page half-dial-questions.md in the prime-richness folder. No other person has reviewed the programs yet.

The programs need Python with the free packages mpmath and numpy and scipy and sympy. Run the programs from inside this folder in the order below because the later programs read the result files that the earlier programs write.

- zfun.py holds the shared routine that adds up the zeta function quickly and is used by the other programs.
- p1_mixed.py tests the mirror rule of the blended row and finds the zeros of the blended row on the dial setting 1/2: `python3 p1_mixed.py`
- p1b_offline.py finds the zeros of the blended row off the dial setting 1/2: `python3 p1b_offline.py`
- p2_dials.py measures the zeta function along one dial setting for pitches 100 to 3100. Run the program once for each line: `python3 p2_dials.py 2 0.02` and then the same with `1.5 0.02` and `1 0.02` and `0.9 0.02` and `0.8 0.02` and `0.75 0.02` and `0.7 0.02` and `0.6 0.02` and `0.55 0.01` and `0.5 0.004` and `0.4 0.02` and `0.25 0.02` and `0 0.02`
- p3_baseline.py finds the pitches where one speaker and one mirror image cancel and the shift from the primes: `python3 p3_baseline.py`
- p4_pair.py measures the close pair of zeros near the pitch 7005: `python3 p4_pair.py`
- p5_heights.py measures the wobble at great pitch heights: `python3 p5_heights.py 1e6 15000 0.07` and `python3 p5_heights.py 1e9 10000 0.045` and `python3 p5_heights.py 1e12 1500 0.04` (the last run takes about 20 minutes)
- p6_misc.py computes the predicted wobble piles and the smallest leftover lengths: `python3 p6_misc.py`
- p7_pure.py counts the zeros of the two quarter turn rows: `python3 p7_pure.py`
- p8_detector.py runs the flat floor test on the blended row: `python3 p8_detector.py`
- check.py compares every figure in half-dial-questions.txt (a plain text copy of the page kept in this folder) with the result files and prints the number of mismatches: `python3 check.py`
