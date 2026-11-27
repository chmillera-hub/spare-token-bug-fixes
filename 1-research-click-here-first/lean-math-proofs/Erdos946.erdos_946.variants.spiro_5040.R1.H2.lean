import OMAReductions.R_Erdos946_erdos_946_variants_spiro_5040_R1
import Mathlib

/-! The integers `v ≤ X` divisible by `d ^ 2` for some `d > B` number at most `X / B`:
there are `⌊X / d ^ 2⌋` multiples of `d ^ 2` up to `X`, and
`∑_{B < d ≤ X} 1 / d ^ 2 ≤ 1 / B - 1 / X` by telescoping `1 / d ^ 2 ≤ 1 / (d - 1) - 1 / d`. -/

open Finset

private lemma sum_inv_sq (B : ℕ) (hB : 0 < B) (M : ℕ) (hM : B ≤ M) :
    ∑ d ∈ Ioc B M, (1 : ℚ) / (d : ℚ) ^ 2 ≤ 1 / B - 1 / M := by
  induction M, hM using Nat.le_induction with
  | base => simp
  | succ M hM ih =>
    rw [sum_Ioc_succ_top hM]
    have hM0 : (0 : ℚ) < M := by exact_mod_cast hB.trans_le hM
    have key : (1 : ℚ) / ((M : ℚ) + 1) ^ 2 ≤ 1 / M - 1 / ((M : ℚ) + 1) := by
      rw [div_sub_div _ _ hM0.ne' (by positivity), div_le_div_iff₀ (by positivity) (by positivity)]
      nlinarith
    push_cast
    linarith

theorem OMA.solution : OMA.R_Erdos946_erdos_946_variants_spiro_5040_R1.H2 := by
  intro B X hB S hS
  have hsub : S ⊆ (Ioc B X).biUnion (fun d => (Ioc 0 X).filter (fun v => d ^ 2 ∣ v)) := by
    intro v hv
    obtain ⟨hv0, hvX, d, hd, hdv⟩ := hS v hv
    refine mem_biUnion.mpr ⟨d, mem_Ioc.mpr ⟨hd, ?_⟩, mem_filter.mpr ⟨mem_Ioc.mpr ⟨hv0, hvX⟩, hdv⟩⟩
    have h1 : d ^ 2 ≤ v := Nat.le_of_dvd hv0 hdv
    have h2 : d ≤ d ^ 2 := Nat.le_self_pow two_ne_zero d
    omega
  have hcard : S.card ≤ ∑ d ∈ Ioc B X, X / d ^ 2 := by
    refine (card_le_card hsub).trans (card_biUnion_le.trans ?_)
    refine le_of_eq (sum_congr rfl fun d _ => ?_)
    exact Nat.Ioc_filter_dvd_card_eq_div X (d ^ 2)
  rcases le_or_gt B X with hBX | hBX
  · have hB' : (0 : ℚ) < B := by exact_mod_cast hB
    have hX' : (0 : ℚ) < X := by exact_mod_cast hB.trans_le hBX
    have hterm : ∀ d ∈ Ioc B X, ((X / d ^ 2 : ℕ) : ℚ) ≤ (X : ℚ) * (1 / (d : ℚ) ^ 2) := by
      intro d _
      have h : ((X / d ^ 2 : ℕ) : ℚ) ≤ (X : ℚ) / ((d ^ 2 : ℕ) : ℚ) := Nat.cast_div_le
      push_cast at h
      rw [mul_one_div]
      exact h
    have hq : (S.card : ℚ) ≤ X * (1 / B - 1 / X) := by
      calc (S.card : ℚ) ≤ ((∑ d ∈ Ioc B X, X / d ^ 2 : ℕ) : ℚ) := by exact_mod_cast hcard
        _ = ∑ d ∈ Ioc B X, ((X / d ^ 2 : ℕ) : ℚ) := by push_cast; rfl
        _ ≤ ∑ d ∈ Ioc B X, (X : ℚ) * (1 / (d : ℚ) ^ 2) := sum_le_sum hterm
        _ = X * ∑ d ∈ Ioc B X, 1 / (d : ℚ) ^ 2 := by rw [mul_sum]
        _ ≤ X * (1 / B - 1 / X) :=
            mul_le_mul_of_nonneg_left (sum_inv_sq B hB X hBX) hX'.le
    have h3 : (X : ℚ) * (1 / B - 1 / X) = X / B - 1 := by field_simp
    rw [h3] at hq
    have h5 : (B : ℚ) * S.card ≤ B * (X / B - 1) := mul_le_mul_of_nonneg_left hq hB'.le
    have h4 : (B : ℚ) * (X / B - 1) = X - B := by field_simp
    have h6 : (B : ℚ) * S.card ≤ X := by linarith
    exact_mod_cast h6
  · have hE : Ioc B X = ∅ := Ioc_eq_empty (by omega)
    rw [hE, sum_empty] at hcard
    have : S.card = 0 := by omega
    simp [this]
