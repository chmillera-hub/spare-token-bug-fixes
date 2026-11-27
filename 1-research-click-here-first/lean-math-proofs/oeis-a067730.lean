import Mathlib

/-!
# A067730: Numbers n such that sigma(n-1) + sigma(n+1) = sigma(2n).

Source: https://oeis.org/A067730
Credit: @chmillera-hub

The entry records the conjecture (Benoit Cloitre, Feb 18 2002): "Conjecture: sequence contains
odd values only."

`sigma` is the sum-of-divisors function, `ArithmeticFunction.sigma 1` in Mathlib. The defining
equation involves `sigma(n-1)`, which is a sum over the divisors of a positive integer only when
`n ≥ 2`, so `main` ranges over `n ≥ 2` (for `n = 1` the term `sigma(0)` has no meaning in the
source, and for `n = 0` neither does `sigma(n-1)`). The first terms are `309, 425, 2135, 2913`;
for instance `sigma(308) + sigma(310) = 672 + 576 = 1248 = sigma(618)`.
-/

namespace OMA.S_oeis_a067730

/-- Every `n ≥ 2` with `sigma(n-1) + sigma(n+1) = sigma(2n)` is odd. -/
theorem main : ∀ n : ℕ, 2 ≤ n →
    ArithmeticFunction.sigma 1 (n - 1) + ArithmeticFunction.sigma 1 (n + 1)
      = ArithmeticFunction.sigma 1 (2 * n) → Odd n := by
  sorry

end OMA.S_oeis_a067730
