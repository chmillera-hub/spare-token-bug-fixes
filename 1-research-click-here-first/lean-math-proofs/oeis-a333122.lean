import Mathlib

/-!
# A333122: Numbers m such that m = prime(k) + prime(k+5) = prime(k+1) + prime(k+4) for some k.

Source: https://oeis.org/A333122
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: this sequence is infinite."

Here `prime(k)` is the `k`-th prime with `prime(1) = 2`. Mathlib's `Nat.nth Nat.Prime` is indexed
from `0` (`Nat.nth Nat.Prime 0 = 2`), so `prime(k)` for `k ≥ 1` is `Nat.nth Nat.Prime j` with
`j = k - 1 ≥ 0`, and letting `j` range over all natural numbers covers exactly the same indices.
The first term is `24 = prime(3) + prime(8) = prime(4) + prime(7) = 5 + 19 = 7 + 17`, that is
`j = 2`.
-/

namespace OMA.S_oeis_a333122

/-- There are infinitely many `m` with `m = p_j + p_(j+5) = p_(j+1) + p_(j+4)` for some `j`. -/
theorem main : {m : ℕ | ∃ j : ℕ, m = Nat.nth Nat.Prime j + Nat.nth Nat.Prime (j + 5) ∧
    m = Nat.nth Nat.Prime (j + 1) + Nat.nth Nat.Prime (j + 4)}.Infinite := by
  sorry

end OMA.S_oeis_a333122
