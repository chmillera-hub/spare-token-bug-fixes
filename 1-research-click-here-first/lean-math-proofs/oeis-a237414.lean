import Mathlib

/-!
# A237414: Primes p with p^2 - 2 and prime(p)^2 - 2 both prime.

Source: https://oeis.org/A237414
Credit: @chmillera-hub

The entry records that, according to the conjecture in A237413, this sequence should have
infinitely many terms.

Here `prime(p)` is the `p`-th prime with `prime(1) = 2`, which is `Nat.nth Nat.Prime (p - 1)`
because `Nat.nth` counts from zero. The first terms are `2` (since `2 ^ 2 - 2 = 2` and
`prime(2) ^ 2 - 2 = 3 ^ 2 - 2 = 7`) and `3` (since `3 ^ 2 - 2 = 7` and
`prime(3) ^ 2 - 2 = 5 ^ 2 - 2 = 23`).
-/

namespace OMA.S_oeis_a237414

/-- There are infinitely many primes `p` such that `p ^ 2 - 2` and `prime(p) ^ 2 - 2` are both
prime, where `prime(p)` is the `p`-th prime. -/
theorem main : {p : ℕ | p.Prime ∧ (p ^ 2 - 2).Prime ∧
    ((Nat.nth Nat.Prime (p - 1)) ^ 2 - 2).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a237414
