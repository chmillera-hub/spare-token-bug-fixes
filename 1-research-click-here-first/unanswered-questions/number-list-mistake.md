# A mistake found in a published number list (OEIS A394252)

One AI model (Claude) did the search and the computing in a single chat on 12 November 2026 and no other person has rerun the work yet which means every result on this page is unconfirmed except the one sum that any reader can check on a calculator.

## The question

The Online Encyclopedia of Integer Sequences holds an entry numbered A394252 at the address https://oeis.org/A394252 and the entry was submitted in March 2026.
The rule of the list is that the first term is 1 and each later term number n is the smallest whole number above the previous term that cannot be written as a sum of exactly n-1 earlier terms when repeats are allowed.
The comments inside the entry say that runs appear where each term is double the previous term and that nobody has a proof about how long those doubling runs get.

## Finding 1: the published term 31 breaks the rule of the list

The copy of the entry read on 12 November 2026 lists 13265690624 as term 31.
The number 13265690624 can be written as a sum of exactly 30 earlier terms because two copies of 829105664 plus twenty-eight copies of 414552832 add up to 13265690624.
Term 31 is supposed to be a number that 30 earlier terms cannot reach which means 13265690624 cannot be term 31.
The published term 32 (39657914368) is also wrong because term 32 was built on top of the wrong term 31.

## Finding 2: values for terms 31 to 38 from an exact program

- Term 31 is 19759378432
- Term 32 is 39518756864
- Term 33 is 79037513728
- Term 34 is 158075027456
- Term 35 is 316150054912
- Term 36 is 632300109824
- Term 37 is 1890267484160
- Term 38 is 3780534968320

The program that produced the eight values reproduced the first 30 published terms and matched a slow brute-force check through term 17 which means the eight values depend on the program being correct beyond term 30.

## Finding 3: a short proof of a limit on doubling runs

Suppose a doubling run starts at position s and has lasted L terms so far.
The next doubled number equals 2^L copies of the first term of the run.
Two equal copies can be merged into one bigger term of the same run and each merge lowers the count of terms by one.
Merging therefore lets the doubled number be written with any count of terms from 2 up to 2^L.
The doubled number sits at position s + L and so the doubled number fails as a term whenever s + L - 1 is between 2 and 2^L.
The doubling therefore must stop once s + L - 1 is at most 2^L.

The limit matches every run computed so far (run lengths 2 and 2 and 3 and 4 and 5 and 5 and 5 and 5 and 6).
The published run of 6 terms starting at position 26 violates the limit because 26 + 5 - 1 is 30 and 30 is less than 32.
The proof gives only an upper limit because nobody has proven yet that doubling always continues right up to the limit.

## What is still open

- Nobody has proven that a run always reaches the limit.
- Nobody has proven the pattern that the first term after a run equals three times the last term of the run minus the last term of the run before.
- The editors of the encyclopedia may have corrected the entry after 12 November 2026.
- Nothing has been sent to the encyclopedia.

The program files sit in the folder named boring-things at the top of this project inside research-program-files inside unanswered-questions-scripts.
