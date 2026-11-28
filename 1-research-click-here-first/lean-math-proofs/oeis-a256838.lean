import Mathlib

/-!
# A256838: Primes of form n^2 + 10000.

Source: https://oeis.org/A256838
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` with `p = n ^ 2 + 10000` for some natural number `n`
(`10000 = 10 ^ 4`). The first terms are `10009 = 3 ^ 2 + 10000` and `10169 = 13 ^ 2 + 10000`.
-/

namespace OMA.S_oeis_a256838

/-- There are infinitely many primes of the form `n ^ 2 + 10000`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + 10000}.Infinite := by
  sorry

end OMA.S_oeis_a256838
