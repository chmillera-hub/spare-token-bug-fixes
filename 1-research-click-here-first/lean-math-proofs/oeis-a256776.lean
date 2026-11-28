import Mathlib

/-!
# A256776: Primes of form n^2 + 256.

Source: https://oeis.org/A256776
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` with `p = n ^ 2 + 256` for some natural number `n`
(`256 = 4 ^ 4`). The first terms are `257 = 1 ^ 2 + 256`, `281 = 5 ^ 2 + 256` and `337 = 9 ^ 2 + 256`.
-/

namespace OMA.S_oeis_a256776

/-- There are infinitely many primes of the form `n ^ 2 + 256`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + 256}.Infinite := by
  sorry

end OMA.S_oeis_a256776
