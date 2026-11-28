import Mathlib

/-!
# A334838: Positive integers m with prime(m) in the form x^2 + m*y^2, where x and y are positive integers.

Source: https://oeis.org/A334838
Credit: @chmillera-hub

The entry records the conjecture that this sequence has infinitely many terms.

Here `prime(m)` is the `m`-th prime with `prime(1) = 2`, which is `Nat.nth Nat.Prime (m - 1)`
because `Nat.nth` counts from zero. The first terms are `1` (since `2 = 1 ^ 2 + 1 * 1 ^ 2`),
`2` (since `3 = 1 ^ 2 + 2 * 1 ^ 2`) and `12` (since `37 = 5 ^ 2 + 12 * 1 ^ 2`).
-/

namespace OMA.S_oeis_a334838

/-- There are infinitely many positive integers `m` such that the `m`-th prime equals
`x ^ 2 + m * y ^ 2` for some positive integers `x` and `y`. -/
theorem main : {m : ℕ | 0 < m ∧ ∃ x y : ℕ, 0 < x ∧ 0 < y ∧
    Nat.nth Nat.Prime (m - 1) = x ^ 2 + m * y ^ 2}.Infinite := by
  sorry

end OMA.S_oeis_a334838
