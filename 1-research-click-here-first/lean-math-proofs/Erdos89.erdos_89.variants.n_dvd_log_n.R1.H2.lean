import OMAReductions.R_Erdos89_erdos_89_variants_n_dvd_log_n_R1
import Mathlib

/-! Cauchy-Schwarz over the distance classes. Split the ordered pairs `P` of distinct points by
their distance `d`. The class sizes sum to `|P|`, the squares of the class sizes count pairs of
ordered pairs at equal distance, and the number of classes is the number of distinct distances. -/

open Finset

theorem OMA.solution : OMA.R_Erdos89_erdos_89_variants_n_dvd_log_n_R1.H2 := by
  classical
  intro S P
  let f : EuclideanSpace ℝ (Fin 2) × EuclideanSpace ℝ (Fin 2) → ℝ := fun z => dist z.1 z.2
  let fib : ℝ → Finset (EuclideanSpace ℝ (Fin 2) × EuclideanSpace ℝ (Fin 2)) :=
    fun d => P.filter (fun z => f z = d)
  have h1 : P.card = ∑ d ∈ P.image f, (fib d).card := card_eq_sum_card_image f P
  have h2 : ∑ d ∈ P.image f, (fib d).card ^ 2
      ≤ ((P ×ˢ P).filter fun z => dist z.1.1 z.1.2 = dist z.2.1 z.2.2).card := by
    have hdisj : ∀ a ∈ P.image f, ∀ b ∈ P.image f, a ≠ b →
        Disjoint (fib a ×ˢ fib a) (fib b ×ˢ fib b) := by
      intro a _ b _ hab
      rw [Finset.disjoint_left]
      rintro ⟨x, y⟩ hx hy
      simp only [fib, mem_product, mem_filter] at hx hy
      exact hab (hx.1.2.symm.trans hy.1.2)
    have hsum : ∑ d ∈ P.image f, (fib d).card ^ 2
        = ((P.image f).biUnion fun d => fib d ×ˢ fib d).card := by
      rw [card_biUnion hdisj]
      simp [sq]
    rw [hsum]
    apply card_le_card
    intro z hz
    obtain ⟨d, _, hz⟩ := mem_biUnion.mp hz
    simp only [fib, mem_product, mem_filter] at hz
    simp only [mem_filter, mem_product]
    exact ⟨⟨hz.1.1, hz.2.1⟩, hz.1.2.trans hz.2.2.symm⟩
  have h3 : (P.image f).card = distinctDistances S := by
    unfold distinctDistances distanceSet
    congr
  calc P.card ^ 2 = (∑ d ∈ P.image f, (fib d).card) ^ 2 := by rw [← h1]
    _ ≤ (P.image f).card * ∑ d ∈ P.image f, (fib d).card ^ 2 := sq_sum_le_card_mul_sum_sq
    _ ≤ distinctDistances S
          * ((P ×ˢ P).filter fun z => dist z.1.1 z.1.2 = dist z.2.1 z.2.2).card := by
        rw [h3]
        exact Nat.mul_le_mul_left _ h2
