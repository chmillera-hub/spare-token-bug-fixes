import Mathlib

/-!
# A160026: Primes p such that p^4 + 17^4 + 3^4 is prime.

Source: https://oeis.org/A160026
Credit: @chmillera-hub

The entry records the conjecture: "It is conjectured that the sequence is infinite."

The sequence is the set of primes `p` for which `p ^ 4 + 17 ^ 4 + 3 ^ 4` is prime. The first
terms are `13, 29, 37, 59`; the entry notes that `3` is not a term because
`3 ^ 4 + 17 ^ 4 + 3 ^ 4 = 83683 = 67 * 1249`.
-/

namespace OMA.S_oeis_a160026

/-- There are infinitely many primes `p` with `p ^ 4 + 17 ^ 4 + 3 ^ 4` prime. -/
theorem main : {p : ℕ | p.Prime ∧ (p ^ 4 + 17 ^ 4 + 3 ^ 4).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a160026
