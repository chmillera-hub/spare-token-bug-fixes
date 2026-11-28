import Mathlib

/-!
# A160025: Primes p such that p^4 + 13^4 + 3^4 is prime.

Source: https://oeis.org/A160025
Credit: @chmillera-hub

The entry records the conjecture: "It is conjectured that the sequence is infinite."

The sequence is the set of primes `p` for which `p ^ 4 + 13 ^ 4 + 3 ^ 4` is prime. The first terms
are `3, 11, 13, 17`; the entry notes that `3` is a term because `3 ^ 4 + 13 ^ 4 + 3 ^ 4 = 28723`
is prime.
-/

namespace OMA.S_oeis_a160025

/-- There are infinitely many primes `p` with `p ^ 4 + 13 ^ 4 + 3 ^ 4` prime. -/
theorem main : {p : ℕ | p.Prime ∧ (p ^ 4 + 13 ^ 4 + 3 ^ 4).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a160025
