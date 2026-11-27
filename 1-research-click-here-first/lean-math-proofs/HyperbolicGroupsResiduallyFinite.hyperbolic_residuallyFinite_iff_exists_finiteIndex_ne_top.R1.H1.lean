import OMAReductions.R_HyperbolicGroupsResiduallyFinite_hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top_R1
import Mathlib

/-! A nontrivial residually finite group has a proper subgroup of finite index:
pick `g ≠ 1` and a finite index subgroup that misses `g`. -/

theorem OMA.solution : OMA.R_HyperbolicGroupsResiduallyFinite_hyperbolic_residuallyFinite_iff_exists_finiteIndex_ne_top_R1.H1 := by
  intro h G _ _ _
  obtain ⟨g, hg⟩ := exists_ne (1 : G)
  obtain ⟨H, hH, hgH⟩ := Group.residuallyFinite_iff_exists_finiteIndex.mp (h G) g hg
  exact ⟨H, fun htop => hgH (htop ▸ Subgroup.mem_top g), hH⟩
