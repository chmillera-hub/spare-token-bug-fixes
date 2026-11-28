import Mathlib

/-!
# A341666: Primes p such that p^6 - 1 has 384 divisors.

Source: https://oeis.org/A341666
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` for which `p ^ 6 - 1` has exactly `384` positive divisors.
The number of divisors of `m` is `m.divisors.card` in Mathlib. For a prime `p` the number
`p ^ 6 - 1` is positive, so the natural-number subtraction is the ordinary difference. The first
terms are `29, 43, 59, 83`.
-/

namespace OMA.S_oeis_a341666

/-- There are infinitely many primes `p` such that `p ^ 6 - 1` has exactly `384` divisors. -/
theorem main : {p : ℕ | p.Prime ∧ (p ^ 6 - 1).divisors.card = 384}.Infinite := by
  sorry

end OMA.S_oeis_a341666
