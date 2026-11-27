import Mathlib

/-!
# A234798: Numbers k such that (k^i)+7 for 1<=i<=7 are seven prime numbers.

Source: https://oeis.org/A234798
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: the sequence is infinite."

A natural number `k` is a term when `k ^ i + 7` is prime for every `i` with `1 ≤ i ≤ 7`. The
entry lists `0` as a term ("0 is in the sequence since (0^i)+7 = 7 is prime for i>0"), which
agrees with `0 ^ i = 0` for `i ≥ 1` in Lean; the next term is `3981186`.
-/

namespace OMA.S_oeis_a234798

/-- There are infinitely many `k` with `k ^ i + 7` prime for all `1 ≤ i ≤ 7`. -/
theorem main : {k : ℕ | ∀ i : ℕ, 1 ≤ i → i ≤ 7 → (k ^ i + 7).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a234798
