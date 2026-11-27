# Lean math proofs

This folder holds three computer-checked proofs of two small math facts that an AI model (Claude) wrote on 27 November 2026 in the proof language Lean 4 which is a programming language where a program called the Lean checker accepts a proof only when every step follows from the rules of logic.

The two facts are steps inside two larger known results from the public project Left to Solve at https://lefttosolve.com which splits hard math results into smaller steps so that many people and AI agents can prove one step at a time. The collection of that project at https://github.com/GuillaumeBAUD-coder/open-math-agents had no proof file for either step when Claude copied the collection on 27 November 2026.

The two facts are small helper steps and are not solutions to open problems because the hard parts of both larger results are other steps that still have no proof in that collection.

- [Erdos946.erdos_946.variants.spiro_5040.R1.H2.lean](Erdos946.erdos_946.variants.spiro_5040.R1.H2.lean) proves a counting fact which says that among the whole numbers from 1 to X at most X divided by B numbers can be divided evenly by the square of some whole number larger than B (for example at most 10 of the numbers from 1 to 100 are divisible by the square of a number larger than 10). The counting fact is one of two steps toward a 1981 result of Claudia Spiro about Erdős problem 946 which says that infinitely many whole numbers n have the same count of divisors as the number n + 5040.
- [Erdos1162.erdos_1162.variants.pyber.R1.H1.lean](Erdos1162.erdos_1162.variants.pyber.R1.H1.lean) proves a lower bound on the number of subgroups of the symmetric group on n objects where the symmetric group means the collection of all ways to rearrange n objects and a subgroup means a smaller collection of rearrangements that is closed under doing one rearrangement after another. The bound says that the number of subgroups is at least 2 raised to the power a times b where a is n divided by 4 rounded down and a + b is n divided by 2 rounded down (for example 8 objects give at least 2^4 = 16 subgroups). The bound is the easier of two steps toward a 1993 result of László Pyber about Erdős problem 1162.
- [Erdos1162.erdos_1162.variants.roney_dougal_tracey.R1.H1.lean](Erdos1162.erdos_1162.variants.roney_dougal_tracey.R1.H1.lean) holds the same proof of the same lower bound with a different first line because the project lists the lower bound a second time as a step toward a sharper 2025 result of Roney-Dougal and Tracey.

## How the proofs were checked

Claude ran the checking script of the Left to Solve project (the file tools/check.sh at version 630fcab of the collection) on each of the three files and the script printed "accepted" for all three files which means the Lean checker found no gap and the proofs use only the three standard starting assumptions of Lean (propext and Classical.choice and Quot.sound). No person has reread the proofs and the Left to Solve project has not received or reviewed the proofs because nobody has sent the proofs to the project yet.

## The idea behind each proof

- The counting proof adds up the multiples of each square because exactly X divided by d squared (rounded down) of the numbers from 1 to X are multiples of d squared. The sum of 1 divided by d squared over every d larger than B stays below 1 divided by B because each term 1 divided by d squared is at most 1/(d-1) minus 1/d and those differences cancel in a chain.
- The subgroup proof swaps objects in pairs because a + b separate pairs of objects can each be swapped or left alone which gives a collection of 2^(a+b) rearrangements. Each grid of zeros and ones with a rows and b columns then picks out a different subgroup inside that collection and there are 2^(a times b) such grids.
