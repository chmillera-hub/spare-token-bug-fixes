import Mathlib

/-!
# A235390: Numbers k such that k^(2^i)+1 are primes for i=0...5.

Source: https://oeis.org/A235390
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: the sequence is infinite."

A natural number `k` is a term when the six numbers `k ^ (2 ^ i) + 1` for `i = 0, 1, 2, 3, 4, 5`
(that is `k + 1`, `k ^ 2 + 1`, `k ^ 4 + 1`, `k ^ 8 + 1`, `k ^ 16 + 1`, `k ^ 32 + 1`) are all prime.
The first term is `1` (all six numbers equal `2`) and the second is `7072833120`.
-/

namespace OMA.S_oeis_a235390

/-- There are infinitely many `k` with `k ^ (2 ^ i) + 1` prime for all `i ≤ 5`. -/
theorem main : {k : ℕ | ∀ i : ℕ, i ≤ 5 → (k ^ (2 ^ i) + 1).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a235390
