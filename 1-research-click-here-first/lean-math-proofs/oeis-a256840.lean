import Mathlib

/-!
# A256840: Primes of form n^2 + 20736.

Source: https://oeis.org/A256840
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` with `p = n ^ 2 + 20736` for some natural number `n`
(`20736 = 12 ^ 4`). The first terms are `20857 = 11 ^ 2 + 20736` and `21577 = 29 ^ 2 + 20736`.
-/

namespace OMA.S_oeis_a256840

/-- There are infinitely many primes of the form `n ^ 2 + 20736`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + 20736}.Infinite := by
  sorry

end OMA.S_oeis_a256840
