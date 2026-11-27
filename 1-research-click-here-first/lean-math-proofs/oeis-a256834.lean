import Mathlib

/-!
# A256834: Primes of form n^2 + 1296.

Source: https://oeis.org/A256834
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` with `p = n ^ 2 + 1296` for some natural number `n`
(`1296 = 6 ^ 4`). The first terms are `1297 = 1 ^ 2 + 1296`, `1321 = 5 ^ 2 + 1296` and
`1657 = 19 ^ 2 + 1296`.
-/

namespace OMA.S_oeis_a256834

/-- There are infinitely many primes of the form `n ^ 2 + 1296`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + 1296}.Infinite := by
  sorry

end OMA.S_oeis_a256834
