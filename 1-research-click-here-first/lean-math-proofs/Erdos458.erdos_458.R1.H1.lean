import OMAReductions.R_Erdos458_erdos_458_R1
import Mathlib

/-! The logarithm of `lcm(1, …, n)` is Chebyshev's function `ψ n`, the sum of the von Mangoldt
function over `1, …, n`, so the difference of two such logarithms is the sum over the gap. -/

open Finset ArithmeticFunction

theorem OMA.solution : OMA.R_Erdos458_erdos_458_R1.H1 := by
  intro a b hab
  have key : ∀ n : ℕ, Real.log (Erdos458.lcm_upto n : ℝ) = ∑ k ∈ Ioc 0 n, vonMangoldt k := by
    intro n
    have h := Chebyshev.psi_eq_log_lcmUpto n
    rw [Chebyshev.psi, Nat.floor_natCast] at h
    rw [h]
    rfl
  rw [key, key, ← Finset.sum_Ioc_consecutive _ (Nat.zero_le a) hab]
  ring
