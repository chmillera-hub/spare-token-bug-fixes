import Mathlib

/-!
# A302984: Number of ways to write n as x^2 + 2*y^2 + 2^z + 5*2^w with x,y,z,w nonnegative integers.

Source: https://oeis.org/A302984
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: a(n) > 0 for all n > 5."

`a(n) > 0` says that `n` has at least one representation `n = x ^ 2 + 2 * y ^ 2 + 2 ^ z + 5 * 2 ^ w`
with `x, y, z, w` nonnegative integers, which `main` states with natural numbers. The smallest
value of the right-hand side is `0 + 0 + 1 + 5 = 6`, and the entry gives
`6 = 0 ^ 2 + 2 * 0 ^ 2 + 2 ^ 0 + 5 * 2 ^ 0`.
-/

namespace OMA.S_oeis_a302984

/-- Every `n > 5` is of the form `x ^ 2 + 2 * y ^ 2 + 2 ^ z + 5 * 2 ^ w`. -/
theorem main : ∀ n : ℕ, 5 < n → ∃ x y z w : ℕ, n = x ^ 2 + 2 * y ^ 2 + 2 ^ z + 5 * 2 ^ w := by
  sorry

end OMA.S_oeis_a302984
