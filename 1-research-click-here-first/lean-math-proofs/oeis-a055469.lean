import Mathlib

/-!
# A055469: Primes of the form k(k+1)/2+1 (i.e., central polygonal numbers, or one more than triangular numbers).

Source: https://oeis.org/A055469
Credit: @chmillera-hub

The entry records the conjecture (Daniel Forgues, Apr 21 2015): "It is conjectured that this
sequence is infinite."

The sequence is the set of primes `p` of the form `k (k + 1) / 2 + 1` with `k` a natural number.
The product `k * (k + 1)` is always even, so the natural-number division by `2` is exact and
`k * (k + 1) / 2` is the `k`-th triangular number. The value `k = 0` gives `1`, which is not prime,
so allowing it changes nothing. The first terms are `2, 7, 11, 29, 37` (from `k = 1, 3, 4, 7, 8`).
-/

namespace OMA.S_oeis_a055469

/-- There are infinitely many primes of the form `k (k + 1) / 2 + 1`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ k : ℕ, p = k * (k + 1) / 2 + 1}.Infinite := by
  sorry

end OMA.S_oeis_a055469
