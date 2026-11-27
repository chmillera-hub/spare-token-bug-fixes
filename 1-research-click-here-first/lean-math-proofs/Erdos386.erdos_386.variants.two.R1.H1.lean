import OMAReductions.R_Erdos386_erdos_386_variants_two_R1
import Mathlib

/-! If `8 P + 1 = r ^ 2` then `r = 2 y + 1` is odd and `y (y + 1) = 2 P`, so `P` is the binomial
coefficient `(y + 1).choose 2`. From `P ≥ 6` we get `y ≥ 3`. -/

theorem OMA.solution : OMA.R_Erdos386_erdos_386_variants_two_R1.H1 := by
  rintro P hP ⟨r, hr⟩
  obtain ⟨y, rfl | rfl⟩ := Nat.even_or_odd' r
  · have h : 2 * y * (2 * y) = 4 * (y * y) := by ring
    omega
  · have h1 : (2 * y + 1) * (2 * y + 1) = 4 * (y * (y + 1)) + 1 := by ring
    have h2 : y * (y + 1) = 2 * P := by omega
    have h3 : 3 ≤ y := by
      by_contra hc
      have hy : y ≤ 2 := by omega
      have h4 : y * (y + 1) ≤ 2 * 3 := Nat.mul_le_mul hy (by omega)
      omega
    refine ⟨y + 1, by omega, ?_, by nlinarith⟩
    rw [Nat.choose_two_right, Nat.add_sub_cancel, mul_comm, h2]
    omega
