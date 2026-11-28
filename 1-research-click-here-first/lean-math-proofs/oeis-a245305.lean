import Mathlib

/-!
# A245305: Numbers k such that 4k+1, 4k+3, and 6k+5 are all primes.

Source: https://oeis.org/A245305
Credit: @chmillera-hub

The entry records that the infinitude of the sequence would follow from the (unproved)
conjecture of Dickson. The statement below is that infinitude.

The first terms are `1` (giving the primes 5, 7, 11) and `4` (giving the primes 17, 19, 29).
-/

namespace OMA.S_oeis_a245305

/-- There are infinitely many `k` such that `4 * k + 1`, `4 * k + 3` and `6 * k + 5` are all
prime. -/
theorem main : {k : ℕ | (4 * k + 1).Prime ∧ (4 * k + 3).Prime ∧ (6 * k + 5).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a245305
