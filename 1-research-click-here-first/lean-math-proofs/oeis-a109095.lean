import Mathlib

/-!
# A109095: Numbers N such that N! is the product of exactly two smaller factorials (larger than 1).

Source: https://oeis.org/A109095
Credit: @chmillera-hub

The entry says: "N = x! is considered to be a trivial solution because then
N! = N*(N-1)! = x!*(N-1)!. Therefore every factorial appears in this sequence." and records the
conjecture: "All terms except a(2) = 10 appear to be trivial solutions. (From Erdős's paper this
is known as Surányi's conjecture.)"

A number `N` is a term when `N ! = a ! * b !` for some `a` and `b` with `a ! > 1`, `b ! > 1`
(that is, `2 ≤ a` and `2 ≤ b`) and both factorials smaller than `N !` (that is, `a < N` and
`b < N`). A term is trivial when it is itself a factorial, `N = x !`. So the conjecture says that
every term other than `10` is a factorial. The first terms are `6 = 3 !`, `10` (from
`10 ! = 6 ! * 7 !`), `24 = 4 !`, `120 = 5 !`.
-/

namespace OMA.S_oeis_a109095

/-- Every `N` whose factorial is a product of two smaller factorials larger than `1` is `10` or is
itself a factorial. -/
theorem main : ∀ N a b : ℕ, 2 ≤ a → a < N → 2 ≤ b → b < N →
    Nat.factorial N = Nat.factorial a * Nat.factorial b →
    N = 10 ∨ ∃ x : ℕ, N = Nat.factorial x := by
  sorry

end OMA.S_oeis_a109095
