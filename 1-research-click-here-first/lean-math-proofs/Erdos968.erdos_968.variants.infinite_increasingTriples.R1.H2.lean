import OMAReductions.R_Erdos968_erdos_968_variants_infinite_increasingTriples_R1
import Mathlib

/-! Chebyshev's lower bound gives `p_n / (n + 1) ≤ 2 log p_n` for `n ≥ 13`.
With `P = p_n` there are `n + 1` primes up to `P`, and Mathlib's Chebyshev bounds give
`P log 2 - log (P + 1) ≤ ψ(P) ≤ (n + 1) log P`. Since `2 log 2 > 1` the term `log (P + 1)`
is absorbed once `P ≥ 15`. -/

theorem OMA.solution : OMA.R_Erdos968_erdos_968_variants_infinite_increasingTriples_R1.H2 := by
  refine Filter.eventually_atTop.mpr ⟨13, fun n hn => ?_⟩
  unfold Erdos968.u
  obtain ⟨P, hPdef⟩ : ∃ P, P = Nat.nth Nat.Prime n := ⟨_, rfl⟩
  rw [← hPdef]
  have hP : n + 2 ≤ P := hPdef ▸ Nat.add_two_le_nth_prime n
  have hπ : Nat.primeCounting P = n + 1 := by
    have h1 : Nat.primeCounting' P = n := hPdef ▸ Nat.primeCounting'_nth_eq n
    have hp : P.Prime := hPdef ▸ Nat.prime_nth_prime n
    simp only [Nat.primeCounting, Nat.primeCounting'] at *
    rw [Nat.count_succ, h1, if_pos hp]
  have h1 := Chebyshev.psi_ge P
  have h2 := Chebyshev.psi_le_primeCounting_mul_log P
  rw [hπ] at h2
  push_cast at h2
  have hlog : Real.log ((P : ℝ) + 1) ≤ 4 * Real.log 2 + ((P : ℝ) + 1) / 16 - 1 := by
    have h3 := Real.log_le_sub_one_of_pos (show (0 : ℝ) < ((P : ℝ) + 1) / 16 by positivity)
    rw [Real.log_div (by positivity) (by norm_num)] at h3
    have h16 : Real.log 16 = 4 * Real.log 2 := by
      rw [show (16 : ℝ) = 2 ^ 4 by norm_num, Real.log_pow]; norm_num
    linarith
  have hl1 := Real.log_two_gt_d9
  have hl2 := Real.log_two_lt_d9
  have hP' : (15 : ℝ) ≤ P := by exact_mod_cast (by omega : 15 ≤ P)
  have hmul : (P : ℝ) * 0.6931 ≤ P * Real.log 2 :=
    mul_le_mul_of_nonneg_left (by linarith) (by linarith)
  rw [div_le_iff₀ (by positivity)]
  nlinarith
