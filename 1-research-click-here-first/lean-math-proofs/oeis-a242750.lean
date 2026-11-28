import Mathlib

/-!
# A242750: Positive integers n with property that n is a primitive root modulo prime(n).

Source: https://oeis.org/A242750
Credit: @chmillera-hub

The entry records that, according to the conjecture in A242748, this sequence should have
infinitely many terms.

Here `prime(n)` is the `n`-th prime with `prime(1) = 2`, which is `Nat.nth Nat.Prime (n - 1)`
because `Nat.nth` counts from zero. The number `n` is a primitive root modulo a prime `p` when
its residue class has multiplicative order `p - 1` in `ZMod p`. The first terms are `1`
(order 1 modulo 2), `2` (order 2 modulo 3) and `3` (order 4 modulo 5).
-/

namespace OMA.S_oeis_a242750

/-- There are infinitely many positive integers `n` such that `n` is a primitive root modulo
the `n`-th prime. -/
theorem main : {n : ℕ | 0 < n ∧
    orderOf (n : ZMod (Nat.nth Nat.Prime (n - 1))) = Nat.nth Nat.Prime (n - 1) - 1}.Infinite := by
  sorry

end OMA.S_oeis_a242750
