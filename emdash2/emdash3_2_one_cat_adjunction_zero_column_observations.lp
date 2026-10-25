/* Whole identity endpoint laws for the original native zero columns.
   The construction maps and inverses remain computational categorical data. */
require open emdash.emdash3_2_one_cat_adjunction_zero_columns;
require open emdash.emdash3_2_one_cat_terminal_adjunction_family_observations;

symbol one_cat_kernel_counit_zero_column_to_src_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_src) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_src) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_kernel_counit_zero_column_to_tgt_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_tgt) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_tgt) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_kernel_counit_zero_column_from_src_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_src) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_src) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_kernel_counit_zero_column_from_tgt_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_tgt) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) walking_arrow_tgt) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_cokernel_unit_zero_column_to_src_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_src) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_src) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_cokernel_unit_zero_column_to_tgt_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_tgt) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@iso_evidence_to (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_tgt) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_cokernel_unit_zero_column_from_src_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_src) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_src) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));

symbol one_cat_cokernel_unit_zero_column_from_tgt_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_tgt) (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)))
≔ let A : Cat ≔ (Functor_oplax_cat WalkingArrow_cat C) in
  let X : τ (Functor A C) ≔ (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) in
  let alpha : τ (@Transf A C X X) ≔ (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@iso_evidence_from (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) walking_arrow_tgt) in
  let beta : τ (@Transf A C X X) ≔ (@id (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)) in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));
