import Mathlib

/-!
# A356109: Numbers k such that k^2 + {1,3,7,13} are prime.

Source: https://oeis.org/A356109
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: the sequence is infinite."

A natural number `k` is a term when the four numbers `k ^ 2 + 1`, `k ^ 2 + 3`, `k ^ 2 + 7` and
`k ^ 2 + 13` are all prime. The first terms are `2` (giving `5, 7, 11, 17`), `4` (giving
`17, 19, 23, 29`) and `10`. The value `k = 0` is not a term because `1` is not prime.
-/

namespace OMA.S_oeis_a356109

/-- There are infinitely many `k` with `k ^ 2 + 1`, `k ^ 2 + 3`, `k ^ 2 + 7`, `k ^ 2 + 13` all
prime. -/
theorem main : {k : ℕ | (k ^ 2 + 1).Prime ∧ (k ^ 2 + 3).Prime ∧ (k ^ 2 + 7).Prime ∧
    (k ^ 2 + 13).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a356109
