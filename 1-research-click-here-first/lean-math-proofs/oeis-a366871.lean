import Mathlib

/-!
# A366871: a(0) = 0; a(n) = n - a(floor(a(n-1)/5)).

Source: https://oeis.org/A366871
Credit: @chmillera-hub

The entry records the conjecture: `a(n) ~ c*n`, where
`c = 1/(1 + 1/(5 + 1/(1 + 1/(5 + ...)))) = (3*sqrt(5) - 5)/2 = 0.8541019662496845...`.

The sequence is stated through its defining recurrence: `main` quantifies over every
`a : ℕ → ℕ` with `a 0 = 0` and `a n = n - a (a (n - 1) / 5)` for `n ≥ 1`. There is exactly one such
function and it is the OEIS sequence. Indeed the recurrence gives `a n ≤ n` for all `n`, so the
index `a (n - 1) / 5` is at most `(n - 1) / 5 < n` and `a n` is determined by earlier values; and
since `a (a (n - 1) / 5) ≤ a (n - 1) / 5 ≤ n`, the natural-number subtraction never truncates. The
division `a (n - 1) / 5` is the floor, as in the source. The first terms are
`0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11`.

`a(n) ~ c*n` is asymptotic equivalence as `n → ∞`, with `c` the closed form `(3 * √5 - 5) / 2`
given in the source for the periodic continued fraction.
-/

namespace OMA.S_oeis_a366871

/-- `a(n) ~ c * n` with `c = (3 * √5 - 5) / 2`. -/
theorem main : ∀ a : ℕ → ℕ, a 0 = 0 → (∀ n : ℕ, 1 ≤ n → a n = n - a (a (n - 1) / 5)) →
    Asymptotics.IsEquivalent Filter.atTop (fun n : ℕ => (a n : ℝ))
      (fun n : ℕ => (3 * Real.sqrt 5 - 5) / 2 * (n : ℝ)) := by
  sorry

end OMA.S_oeis_a366871
