import Mathlib

/-!
# A342064: Primes p such that p^8 - 1 has 384 divisors.

Source: https://oeis.org/A342064
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: sequence is infinite."

The sequence is the set of primes `p` for which `p ^ 8 - 1` has exactly `384` positive divisors.
The number of divisors of `m` is `m.divisors.card` in Mathlib. For a prime `p` the number
`p ^ 8 - 1` is positive, so the natural-number subtraction is the ordinary difference. The first
terms are `821, 997, 2819`.
-/

namespace OMA.S_oeis_a342064

/-- There are infinitely many primes `p` such that `p ^ 8 - 1` has exactly `384` divisors. -/
theorem main : {p : ℕ | p.Prime ∧ (p ^ 8 - 1).divisors.card = 384}.Infinite := by
  sorry

end OMA.S_oeis_a342064
