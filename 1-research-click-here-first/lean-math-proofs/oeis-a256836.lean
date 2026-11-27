import Mathlib

/-!
# A256836: Primes of form n^2 + 4096.

Source: https://oeis.org/A256836
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` with `p = n ^ 2 + 4096` for some natural number `n`
(`4096 = 2 ^ 12`). The first terms are `4177 = 9 ^ 2 + 4096`, `4217 = 11 ^ 2 + 4096` and
`4457 = 19 ^ 2 + 4096`.
-/

namespace OMA.S_oeis_a256836

/-- There are infinitely many primes of the form `n ^ 2 + 4096`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + 4096}.Infinite := by
  sorry

end OMA.S_oeis_a256836
