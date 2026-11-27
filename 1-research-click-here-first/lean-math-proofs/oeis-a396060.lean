import Mathlib

/-!
# A396060: Numbers m such that m^2 + 1 and m^2 - m + 1 are both prime numbers.

Source: https://oeis.org/A396060
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: There are infinitely many numbers m such that the
two polynomials m^2 + 1 and m^2 - m + 1 are prime."

A natural number `m` is a term when `m ^ 2 + 1` and `m ^ 2 - m + 1` are both prime. Since
`m ≤ m ^ 2` for every natural number `m`, the natural-number subtraction `m ^ 2 - m` is the
ordinary difference. The first terms are `2, 4, 6, 16`; the entry gives `6` as a term because
`6 ^ 2 + 1 = 37` and `37 - 6 = 31` are prime. The values `m = 0` and `m = 1` are not terms because
then `m ^ 2 - m + 1 = 1`.
-/

namespace OMA.S_oeis_a396060

/-- There are infinitely many `m` with `m ^ 2 + 1` and `m ^ 2 - m + 1` both prime. -/
theorem main : {m : ℕ | (m ^ 2 + 1).Prime ∧ (m ^ 2 - m + 1).Prime}.Infinite := by
  sorry

end OMA.S_oeis_a396060
