import OMAReductions.R_Erdos398_erdos_398_R1
import Mathlib

/-! For `n ≥ 4` write `n! = 4 q`. A square root `m` of `4 q + 1` is odd, say `m = 2 x + 1`, and
`(2 x + 1) ^ 2 = 4 x (x + 1) + 1`, so `n! + 1` is a square exactly when `q = x (x + 1)`. -/

theorem OMA.solution : OMA.R_Erdos398_erdos_398_R1.H1 := by
  intro n hn
  obtain ⟨q, hq⟩ : 4 ∣ n.factorial := Nat.dvd_factorial (by norm_num) hn
  rw [hq, Nat.mul_div_cancel_left q (by norm_num)]
  constructor
  · rintro ⟨m, hm⟩
    obtain ⟨y, rfl | rfl⟩ := Nat.even_or_odd' m
    · have h : (2 * y) ^ 2 = 4 * (y * y) := by ring
      omega
    · have h : (2 * y + 1) ^ 2 = 4 * (y * (y + 1)) + 1 := by ring
      exact ⟨y, by omega⟩
  · rintro ⟨x, hx⟩
    refine ⟨2 * x + 1, ?_⟩
    have h : (2 * x + 1) ^ 2 = 4 * (x * (x + 1)) + 1 := by ring
    omega
