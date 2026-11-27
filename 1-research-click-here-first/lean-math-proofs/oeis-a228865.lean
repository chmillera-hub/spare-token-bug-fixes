import Mathlib

/-!
# A228865: Primes of the form n^2 + pi(n).

Source: https://oeis.org/A228865
Credit: @chmillera-hub

The entry records the conjecture: "Conjecture: the sequence is infinite."

`pi(n)` is the number of primes less than or equal to `n`, `Nat.primeCounting n` in Mathlib. The
sequence is the set of primes `p` with `p = n ^ 2 + pi(n)` for some natural number `n`. The first
terms are `5 = 2 ^ 2 + 1` and `11 = 3 ^ 2 + 2`, and the entry gives `449 = 21 ^ 2 + pi(21)` with
`pi(21) = 8`.
-/

namespace OMA.S_oeis_a228865

/-- There are infinitely many primes of the form `n ^ 2 + pi(n)`. -/
theorem main : {p : ℕ | p.Prime ∧ ∃ n : ℕ, p = n ^ 2 + Nat.primeCounting n}.Infinite := by
  sorry

end OMA.S_oeis_a228865
