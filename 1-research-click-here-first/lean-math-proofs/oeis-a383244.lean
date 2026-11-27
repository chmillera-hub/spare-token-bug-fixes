import Mathlib

/-!
# A383244: Primes of the form p(k)*p(k+1)*(p(k+1) - p(k)) + 1 sorted by increasing k.

Source: https://oeis.org/A383244
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: there are infinitely many such primes."

Here `p(k)` is the `k`-th prime with `p(1) = 2`. Mathlib's `Nat.nth Nat.Prime` is indexed from
`0` (`Nat.nth Nat.Prime 0 = 2`), so the pair of consecutive primes `p(k), p(k+1)` for `k ≥ 1` is
`Nat.nth Nat.Prime j, Nat.nth Nat.Prime (j + 1)` for `j = k - 1 ≥ 0`, and letting `j` range over
all natural numbers covers exactly the same pairs. The first terms are `7 = 2 * 3 * 1 + 1`,
`31 = 3 * 5 * 2 + 1` and `71 = 5 * 7 * 2 + 1`. Since `p(k+1) > p(k)` the natural-number
subtraction is the ordinary difference.
-/

namespace OMA.S_oeis_a383244

/-- There are infinitely many primes of the form `p * q * (q - p) + 1` with `p < q` consecutive
primes. -/
theorem main : {r : ℕ | r.Prime ∧ ∃ j : ℕ,
    r = Nat.nth Nat.Prime j * Nat.nth Nat.Prime (j + 1)
      * (Nat.nth Nat.Prime (j + 1) - Nat.nth Nat.Prime j) + 1}.Infinite := by
  sorry

end OMA.S_oeis_a383244
