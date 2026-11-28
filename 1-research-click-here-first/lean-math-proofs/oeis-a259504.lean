import Mathlib

/-!
# A259504: Numbers k such that k and k+1 are the product of exactly three (not necessarily distinct) primes.

Source: https://oeis.org/A259504
Credit: @chmillera-hub

The entry records the conjecture that this sequence is infinite.

A number is a product of exactly three primes, counted with multiplicity, when
`ArithmeticFunction.cardFactors` (the function usually written as capital Omega) takes the value 3.
The first terms are `27 = 3 * 3 * 3` (with `28 = 2 * 2 * 7`) and `44 = 2 * 2 * 11`
(with `45 = 3 * 3 * 5`).
-/

namespace OMA.S_oeis_a259504

/-- There are infinitely many `k` such that `k` and `k + 1` each have exactly three prime
factors counted with multiplicity. -/
theorem main : {k : ℕ | ArithmeticFunction.cardFactors k = 3 ∧
    ArithmeticFunction.cardFactors (k + 1) = 3}.Infinite := by
  sorry

end OMA.S_oeis_a259504
