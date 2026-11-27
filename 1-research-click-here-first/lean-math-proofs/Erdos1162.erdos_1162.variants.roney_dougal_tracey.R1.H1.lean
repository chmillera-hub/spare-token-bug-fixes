import OMAReductions.R_Erdos1162_erdos_1162_variants_roney_dougal_tracey_R1
import Mathlib

/-! Lower bound for the number of subgroups of `S_n`.

For `(a + b) * 2 ≤ n` the elementary abelian group `(ℤ/2)^(a+b)` embeds in `S_n`
(each coordinate translates its own copy of `ℤ/2`), and every `a × b` matrix `M` over `ℤ/2`
gives the subgroup `{(v, v * M)}`, the graph of a linear map. Different matrices give
different graphs, so `S_n` has at least `2 ^ (a * b)` subgroups. -/

open Equiv

/-- The graph of the linear map `v ↦ v * M`, as a subgroup of `(ℤ/2)^a × (ℤ/2)^b`. -/
private def graph {a b : ℕ} (M : Fin a → Fin b → ZMod 2) :
    AddSubgroup (Fin a ⊕ Fin b → ZMod 2) where
  carrier := {x | ∀ j, x (Sum.inr j) = ∑ i, x (Sum.inl i) * M i j}
  zero_mem' := by intro j; simp
  add_mem' := by
    intro x y hx hy j
    simp only [Set.mem_setOf_eq] at hx hy
    simp [hx j, hy j, add_mul, Finset.sum_add_distrib]
  neg_mem' := by
    intro x hx j
    simp only [Set.mem_setOf_eq] at hx
    simp [hx j, Finset.sum_neg_distrib]

private lemma graph_injective {a b : ℕ} : Function.Injective (@graph a b) := by
  intro M M' h
  funext i j
  have hx : (Sum.elim (Pi.single i 1) (M i) : Fin a ⊕ Fin b → ZMod 2) ∈ graph M := by
    change ∀ j, _ = ∑ i', _ * M i' j
    intro j
    simp [Pi.single_apply]
  rw [h] at hx
  have h2 : ∀ j, (Sum.elim (Pi.single i 1) (M i) : Fin a ⊕ Fin b → ZMod 2) (Sum.inr j)
      = ∑ i', (Sum.elim (Pi.single i 1) (M i) : Fin a ⊕ Fin b → ZMod 2) (Sum.inl i') * M' i' j := hx
  simpa [Pi.single_apply] using h2 j

/-- Translate the copy of `ℤ/2` above `i` by `c i`. -/
private def shift {ι : Type} (c : ι → ZMod 2) : Perm (ι × ZMod 2) where
  toFun p := (p.1, p.2 + c p.1)
  invFun p := (p.1, p.2 - c p.1)
  left_inv p := by simp
  right_inv p := by simp

private def shiftHom (ι : Type) : Multiplicative (ι → ZMod 2) →* Perm (ι × ZMod 2) where
  toFun x := shift (Multiplicative.toAdd x)
  map_one' := by ext p <;> simp [shift]
  map_mul' x y := by ext p <;> simp [shift, add_comm, add_left_comm]

private lemma shiftHom_injective (ι : Type) : Function.Injective (shiftHom ι) := by
  intro x y h
  apply Multiplicative.toAdd.injective
  funext i
  have := congrArg (fun σ : Perm (ι × ZMod 2) => (σ (i, 0)).2) h
  simpa [shiftHom, shift] using this

private lemma count (a b n : ℕ) (h : (a + b) * 2 ≤ n) :
    2 ^ (a * b) ≤ Nat.card (Subgroup (Perm (Fin n))) := by
  obtain ⟨e⟩ : Nonempty ((Fin a ⊕ Fin b) × ZMod 2 ↪ Fin n) := by
    apply Function.Embedding.nonempty_of_card_le
    simpa [ZMod.card] using h
  let F : (Fin a → Fin b → ZMod 2) → Subgroup (Perm (Fin n)) := fun M =>
    Subgroup.map (Perm.viaEmbeddingHom e)
      (Subgroup.map (shiftHom (Fin a ⊕ Fin b)) (AddSubgroup.toSubgroup (graph M)))
  have hF : Function.Injective F := by
    intro M M' hMM
    apply graph_injective
    apply AddSubgroup.toSubgroup.injective
    apply Subgroup.map_injective (shiftHom_injective _)
    exact Subgroup.map_injective (Perm.viaEmbeddingHom_injective e) hMM
  have hc := Nat.card_le_card_of_injective F hF
  have h2 : Nat.card (Fin a → Fin b → ZMod 2) = 2 ^ (a * b) := by
    simp [Nat.card_eq_fintype_card, ZMod.card, ← pow_mul, mul_comm]
  rw [h2] at hc
  exact hc

theorem OMA.solution : OMA.R_Erdos1162_erdos_1162_variants_roney_dougal_tracey_R1.H1 := by
  intro n
  exact count _ _ n (by omega)
