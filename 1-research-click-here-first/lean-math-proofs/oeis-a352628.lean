import Mathlib

/-!
# A352628: Number of ways to write n as a^2 + 2*b^2 + c^4 + 2*d^4 + 3*c^2*d^2, where a,b,c,d are nonnegative integers.

Source: https://oeis.org/A352628
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: a(n) > 0 for all n = 0,1,2,.... In other words,
each nonnegative integer can be written as a^2 + 2*b^2 + (c^2+d^2)*(c^2+2*d^2) with a,b,c,d
integers."

`a(n) > 0` says that `n` has at least one representation
`n = a ^ 2 + 2 * b ^ 2 + c ^ 4 + 2 * d ^ 4 + 3 * c ^ 2 * d ^ 2` with `a, b, c, d` nonnegative
integers, which is what `main` states with natural numbers. Only even powers occur, so allowing
all integers `a, b, c, d` gives the same set of values, and
`(c ^ 2 + d ^ 2) * (c ^ 2 + 2 * d ^ 2) = c ^ 4 + 2 * d ^ 4 + 3 * c ^ 2 * d ^ 2`.
The entry also says "It seems that a(n) = 1 only for n = 0, 21, 71, 157, 175, 190, 316, 476, 526";
that remark is not part of the conjecture stated here.
-/

namespace OMA.S_oeis_a352628

/-- Every natural number is of the form `a ^ 2 + 2 * b ^ 2 + c ^ 4 + 2 * d ^ 4 + 3 * c ^ 2 * d ^ 2`. -/
theorem main : ∀ n : ℕ, ∃ a b c d : ℕ,
    n = a ^ 2 + 2 * b ^ 2 + c ^ 4 + 2 * d ^ 4 + 3 * c ^ 2 * d ^ 2 := by
  sorry

end OMA.S_oeis_a352628
