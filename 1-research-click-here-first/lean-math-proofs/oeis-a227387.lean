import Mathlib

/-!
# A227387: Numbers n such that sigma(n)*7 < sigma(n-1) + sigma(n+1).

Source: https://oeis.org/A227387
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: the sequence is infinite."

`sigma` is the sum-of-divisors function, `ArithmeticFunction.sigma 1` in Mathlib. The term
`sigma(n-1)` is a sum over the divisors of a positive integer only when `n ≥ 2`, so the set in
`main` is restricted to `n ≥ 2` (Mathlib gives `sigma 0 = 0` and `0 - 1 = 0`, which would make
`n = 0` satisfy the inequality by convention only). Removing finitely many small values does not
change whether the set is infinite. The first terms are `41902660799` and `41902660801`.
-/

namespace OMA.S_oeis_a227387

/-- There are infinitely many `n` with `7 * sigma(n) < sigma(n-1) + sigma(n+1)`. -/
theorem main : {n : ℕ | 2 ≤ n ∧ ArithmeticFunction.sigma 1 n * 7
    < ArithmeticFunction.sigma 1 (n - 1) + ArithmeticFunction.sigma 1 (n + 1)}.Infinite := by
  sorry

end OMA.S_oeis_a227387
