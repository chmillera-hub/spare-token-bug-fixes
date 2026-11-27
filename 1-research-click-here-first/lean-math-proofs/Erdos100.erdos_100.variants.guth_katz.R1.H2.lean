import OMAReductions.R_Erdos100_erdos_100_variants_guth_katz_R1
import Mathlib

/-! The distinct distances are reals in `[0, diam A]` that pairwise differ by at least `1`, so
taking integer parts is injective on them and lands in `{0, …, ⌊diam A⌋}`. -/

open Finset

theorem OMA.solution : OMA.R_Erdos100_erdos_100_variants_guth_katz_R1.H2 := by
  classical
  intro A hA
  obtain ⟨D, hD⟩ : ∃ D : ℝ, D = Metric.diam (A : Set (EuclideanSpace ℝ (Fin 2))) := ⟨_, rfl⟩
  rw [← hD]
  have hD0 : 0 ≤ D := hD ▸ Metric.diam_nonneg
  have hbd : ∀ p ∈ A, ∀ q ∈ A, dist p q ≤ D := fun p hp q hq =>
    hD ▸ Metric.dist_le_diam_of_mem A.finite_toSet.isBounded hp hq
  have hinj : Set.InjOn (fun t : ℝ => ⌊t⌋₊) (distanceSet A : Set ℝ) := by
    intro s hs t ht hst
    simp only [distanceSet, coe_image, Set.mem_image, mem_coe, mem_offDiag] at hs ht
    obtain ⟨⟨p1, q1⟩, ⟨hp1, hq1, _⟩, rfl⟩ := hs
    obtain ⟨⟨p2, q2⟩, ⟨hp2, hq2, _⟩, rfl⟩ := ht
    by_contra hne
    have h1 := hA p1 q1 p2 q2 hp1 hq1 hp2 hq2 hne
    have a1 := Nat.floor_le (dist_nonneg : 0 ≤ dist p1 q1)
    have a2 := Nat.lt_floor_add_one (dist p1 q1)
    have b1 := Nat.floor_le (dist_nonneg : 0 ≤ dist p2 q2)
    have b2 := Nat.lt_floor_add_one (dist p2 q2)
    simp only at hst
    rw [hst] at a1 a2
    rw [ge_iff_le, le_abs] at h1
    rcases h1 with h | h <;> linarith
  have hmaps : ∀ t ∈ distanceSet A, ⌊t⌋₊ ∈ Finset.range (⌊D⌋₊ + 1) := by
    intro t ht
    simp only [distanceSet, mem_image, mem_offDiag] at ht
    obtain ⟨⟨p, q⟩, ⟨hp, hq, _⟩, rfl⟩ := ht
    exact mem_range.mpr (Nat.lt_succ_of_le (Nat.floor_le_floor (hbd p hp q hq)))
  have hcard : (distanceSet A).card ≤ ⌊D⌋₊ + 1 := by
    have := Finset.card_le_card_of_injOn (fun t : ℝ => ⌊t⌋₊) hmaps hinj
    simpa using this
  have h5 : ((distinctDistances A : ℕ) : ℝ) ≤ (⌊D⌋₊ : ℝ) + 1 := by
    unfold distinctDistances
    exact_mod_cast hcard
  linarith [Nat.floor_le hD0]
