import OMAReductions.R_ElliottHalberstamConjecture_elliott_halberstam_variants_bombieri_vinogradov_R1
import Mathlib

/-! Finite partial summation. Write `S t = ∑_{p ≤ t} f p log p`. Removing the prime powers from
the von Mangoldt sum costs at most `ψ x - θ x`, so `|S t| ≤ K = M + (ψ x - θ x)` for `t ≤ x`.
By induction on `t`, `|∑_{p ≤ t} f p - S t / log t| ≤ K (1 / log 2 - 1 / log t)`, because adding
a prime `t + 1` changes both terms by `f (t + 1)` and `1 / log` is decreasing. -/

open Finset Real ArithmeticFunction

theorem OMA.solution : OMA.R_ElliottHalberstamConjecture_elliott_halberstam_variants_bombieri_vinogradov_R1.H2 := by
  intro x f M hx hf hM
  classical
  obtain ⟨K, hK⟩ : ∃ K : ℝ, K = M + (Chebyshev.psi x - Chebyshev.theta x) := ⟨_, rfl⟩
  rw [← hK]
  let g : ℕ → ℝ := fun n => if n.Prime then f n else 0
  let T : ℕ → ℝ := fun t => ∑ n ∈ Icc 1 t, g n
  let S : ℕ → ℝ := fun t => ∑ n ∈ Icc 1 t, g n * Real.log n
  let R : ℕ → ℝ := fun t => ∑ n ∈ Icc 1 t, (if n.Prime then 0 else Λ n)
  have hRx : R x = Chebyshev.psi x - Chebyshev.theta x := by
    rw [Chebyshev.psi_sub_theta_eq_sum_not_prime, Nat.floor_natCast, sum_filter]
    refine sum_congr ?_ (fun n _ => ?_)
    · ext n; simp only [mem_Icc, mem_Ioc]; omega
    · by_cases h : n.Prime <;> simp [h]
  have hRmono : ∀ t ≤ x, R t ≤ R x := by
    intro t ht
    apply sum_le_sum_of_subset_of_nonneg (Icc_subset_Icc_right ht)
    intro n _ _
    split_ifs
    · exact le_rfl
    · exact vonMangoldt_nonneg
  have hS : ∀ t ≤ x, |S t| ≤ K := by
    intro t ht
    have hsplit : S t = ∑ n ∈ Icc 1 t, f n * Λ n
        - ∑ n ∈ Icc 1 t, (if n.Prime then 0 else f n * Λ n) := by
      rw [← sum_sub_distrib]
      refine sum_congr rfl (fun n _ => ?_)
      by_cases h : n.Prime
      · simp [g, h, vonMangoldt_apply_prime h]
      · simp [g, h]
    have h2 : |∑ n ∈ Icc 1 t, (if n.Prime then 0 else f n * Λ n)| ≤ R t := by
      refine (abs_sum_le_sum_abs _ _).trans (sum_le_sum fun n hn => ?_)
      have hn' : n ≤ x := (mem_Icc.mp hn).2.trans ht
      by_cases h : n.Prime
      · simp [h]
      · simp only [h, if_false, abs_mul]
        calc |f n| * |Λ n| ≤ 1 * |Λ n| := mul_le_mul_of_nonneg_right (hf n hn') (abs_nonneg _)
          _ = Λ n := by rw [one_mul, abs_of_nonneg vonMangoldt_nonneg]
    obtain ⟨a1, a2⟩ := abs_le.mp (hM t ht)
    obtain ⟨b1, b2⟩ := abs_le.mp h2
    have h4 := hRmono t ht
    rw [hsplit, abs_le]
    constructor <;> linarith
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have key : ∀ t, 2 ≤ t → t ≤ x →
      |T t - S t / Real.log t| ≤ K * (1 / Real.log 2 - 1 / Real.log t) := by
    intro t ht
    induction t, ht using Nat.le_induction with
    | base =>
      intro _
      have hT2 : T 2 = f 2 := by simp [T, g, sum_Icc_succ_top, Nat.prime_two]
      have hS2 : S 2 = f 2 * Real.log 2 := by simp [S, g, sum_Icc_succ_top, Nat.prime_two]
      rw [hT2, hS2]
      simp [hlog2.ne']
    | succ t ht ih =>
      intro htx
      have ih' := ih (by omega)
      have hSt := hS t (by omega)
      have hTs : T (t + 1) = T t + g (t + 1) := sum_Icc_succ_top (by omega) _
      have hSs : S (t + 1) = S t + g (t + 1) * Real.log ((t + 1 : ℕ) : ℝ) :=
        sum_Icc_succ_top (by omega) _
      have ht2 : (2 : ℝ) ≤ t := by exact_mod_cast ht
      have hlt : (0 : ℝ) < Real.log t := Real.log_pos (by linarith)
      have hlt1 : (0 : ℝ) < Real.log ((t + 1 : ℕ) : ℝ) :=
        Real.log_pos (by push_cast; linarith)
      have hmono : Real.log t ≤ Real.log ((t + 1 : ℕ) : ℝ) :=
        Real.log_le_log (by linarith) (by push_cast; linarith)
      have hd : 0 ≤ 1 / Real.log t - 1 / Real.log ((t + 1 : ℕ) : ℝ) := by
        rw [sub_nonneg]; exact one_div_le_one_div_of_le hlt hmono
      have heq : T (t + 1) - S (t + 1) / Real.log ((t + 1 : ℕ) : ℝ)
          = (T t - S t / Real.log t)
            + S t * (1 / Real.log t - 1 / Real.log ((t + 1 : ℕ) : ℝ)) := by
        rw [hTs, hSs]; field_simp; ring
      rw [heq]
      calc |(T t - S t / Real.log t) + S t * (1 / Real.log t - 1 / Real.log ((t + 1 : ℕ) : ℝ))|
          ≤ |T t - S t / Real.log t|
            + |S t * (1 / Real.log t - 1 / Real.log ((t + 1 : ℕ) : ℝ))| := abs_add_le _ _
        _ ≤ K * (1 / Real.log 2 - 1 / Real.log t)
            + K * (1 / Real.log t - 1 / Real.log ((t + 1 : ℕ) : ℝ)) := by
            rw [abs_mul, abs_of_nonneg hd]
            exact add_le_add ih' (mul_le_mul_of_nonneg_right hSt hd)
        _ = K * (1 / Real.log 2 - 1 / Real.log ((t + 1 : ℕ) : ℝ)) := by ring
  have hfin := key x hx le_rfl
  have hSx := hS x le_rfl
  have hTx : ∑ p ∈ Nat.primesLE x, f p = T x := by
    rw [Nat.primesLE_eq_filter_Icc_one, sum_filter]
  rw [hTx]
  have hx2 : (2 : ℝ) ≤ x := by exact_mod_cast hx
  have hlx : (0 : ℝ) < Real.log x := Real.log_pos (by linarith)
  have e : T x = (T x - S x / Real.log x) + S x / Real.log x := by ring
  rw [e]
  calc |(T x - S x / Real.log x) + S x / Real.log x|
      ≤ |T x - S x / Real.log x| + |S x / Real.log x| := abs_add_le _ _
    _ ≤ K * (1 / Real.log 2 - 1 / Real.log x) + K / Real.log x := by
        rw [abs_div, abs_of_pos hlx]
        exact add_le_add hfin (div_le_div_of_nonneg_right hSx hlx.le)
    _ = K / Real.log 2 := by ring
