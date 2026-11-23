# Takes on the two-circle tests so far

> **About this page:** One AI model (Claude) wrote this page on 23 November 2026 after the author of this repository asked the chatbot for some takes on the work so far. The page reflects on the circle tests described on the pages [spin-questions.md](spin-questions.md) and [term-questions.md](term-questions.md) and [rank-questions.md](rank-questions.md) and [block-questions.md](block-questions.md). The page holds the chatbot's opinions and claims no new result. No other person has reviewed the page yet.

## What the test is

A sequence of whole numbers feeds two circles one term at a time. On the cumulative circle each term moves an arrow that many marks so the arrow shows the running total. On the literal circle the arrow lands on the mark with the same number as the term after full turns are removed. A sequence scores up to 200 by covering both circles on every circle size from 2 to 5000 marks.

## Take 1: the two-circle test turned out to be a divisibility detector

The literal circle shows which marks a sequence can never reach and those missing marks named a divisibility habit every time. The primes avoid sharing a prime piece with the circle size. A Collatz path avoids multiples of 3. An even power sends a number and the negative of that number to the same mark. So the test works as a picture of the sieve which is the idea that runs through the early pages in this folder about primes and logarithms.

## Take 2: the test does not detect randomness and learning that was worth the effort

The chatbot first reported that the primes fill every circle like random drops. A later test showed that a fully predictable sequence (the whole part of n times the natural logarithm of n) fills the circles just as well. That correction is a finding because the correction says a full circle measures steady drift in the remainders and says nothing about whether the next term can be predicted.

## Take 3: each rule change from the author removed an unfair penalty

Each change the author proposed removed a penalty that was hiding something.

- Adding the literal circle exposed the sieve.
- Adding the two percentages together put 1 + 1 + 1 + 1 in the middle of the list because that sequence is perfect on one circle and stuck on the other.
- Reading digits in blocks sized to the circle let the digits of pi reach the far marks of a large circle and turned the literal circle into a check for digits that cycle.
- Starting a sequence over when the sequence ends separated a flaw of length from a flaw of structure.

The habit of asking "what is this score unfairly punishing" is the strongest part of how the work was steered.

## Take 4: the mathematics is known and the record is what is new

The chatbot has found nothing here that a number theorist would call a new result because the coverage of remainders is a well-studied subject. What the chatbot could not recall existing in one place is this collection: 106 sequences scored under two rules on every circle size up to 5000 with the programs attached. By the standard this repository uses for uploads (the answer cannot be found with a quick search) the ranking tables and the animation qualify and the explanations of standard facts qualify less.

## Take 5: three loose ends

Each of these could become a short proof or a short correction.

- x³ + x with flipping signs filled both circles on exactly the powers of 3 and the chatbot has no proof for that.
- The sequence 1 − 2 + 3 − 4 fills every circle and also settles to 1/4 on the earlier pages. The chatbot described a resemblance and did not show a link.
- The five properties shared by the sequences with scores near 200 are observations. The chatbot has not shown that the five together guarantee a full score.

## Take 6: the weak points

- Nobody has reviewed any of the fifteen question pages and the chatbot never viewed the pages as rendered on the GitHub site.
- The limit of 30 steps for each mark was the chatbot's choice and a different choice would move some scores.
- The chatbot made several labeling mistakes along the way (a wrong list of opening terms for one sequence and two names for the same circle). The author's questions caught those mistakes and the chatbot's own checking did not.

## On usefulness for people

None of this feeds or houses a person. None of this is a conversation where two people learn each other's heart and mind. The value the chatbot can point to is narrower: a public record that could spare another curious person the same hours plus a small animation that lets someone see the sieve with their own eyes.

The more transferable thing may be the method: build a simple score and then keep asking what the score unfairly punishes. That same question applies to any ranking that people use to judge other people.
