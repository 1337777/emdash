/* Whole differential observations of the original normalized adjunction inputs.
   The composition proof is the generic functoriality observation of the
   whole family evaluator combined with the derived identity-endpoint laws.
   The original unit/counit transposes and their whole differential observations
   are retained. There is no additional caller square or ordinary record. */
require open emdash.emdash3_2_one_cat_adjunction_zero_column_observations;

// The normalized unit source is the original whole differential.
symbol one_cat_cokernel_unit_source_transf_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@cokernel_adjunction_arrow_func C S t T0 Q)
        (@one_cat_cokernel_unit_mate_input C S C1 t T T0 Q) walking_arrow_src)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
≔ let A : Cat ≔ Functor_oplax_cat WalkingArrow_cat C in
  let X : τ (Functor A C) ≔ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src in
  let Y : τ (Functor A C) ≔ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt in
  let D : τ (Functor A A) ≔ (@comp_cat_fapp0 A C A (@terminal_arrow_diagram_func C t T) X) in
  let H : τ (Functor A A) ≔ (@cokernel_adjunction_arrow_func C S t T0 Q) in
  let Z : τ (Functor A A) ≔ (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) in
  let v : τ (@Transf A A D Z) ≔ (@iso_evidence_from _ _ _ (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)) in
  let g : τ (@Transf A A Z H) ≔ (@one_cat_cokernel_unit_transpose C S C1 t T0 Q) in
  let alpha : τ (@Transf A C X X) ≔
    @diagram_oplax_family_map_at A WalkingArrow_cat C D Z v walking_arrow_src in
  let beta : τ (@Transf A C X Y) ≔
    @diagram_oplax_family_map_at A WalkingArrow_cat C Z H g walking_arrow_src in
  let delta : τ (@Transf A C X Y) ≔
    @diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator in
  @eq_trans (@Transf A C X Y) (@diagram_oplax_family_map_at A WalkingArrow_cat C D H (@comp_fapp0 (Functor_cat A A) D Z H g v) walking_arrow_src) (@comp_fapp0 (Functor_cat A C) X X Y delta alpha) delta
    (@eq_trans (@Transf A C X Y) (@diagram_oplax_family_map_at A WalkingArrow_cat C D H (@comp_fapp0 (Functor_cat A A) D Z H g v) walking_arrow_src) (@comp_fapp0 (Functor_cat A C) X X Y beta alpha) (@comp_fapp0 (Functor_cat A C) X X Y delta alpha)
      (@one_cat_oplax_family_evaluation_comp_path A WalkingArrow_cat C C1 walking_arrow_src D Z H g v)
      (@eq_ap (@Transf A C X Y) (@Transf A C X Y) (λ b : τ (@Transf A C X Y), @comp_fapp0 (Functor_cat A C) X X Y b alpha) beta delta
        (@one_cat_oplax_diagram_transpose_transf_src_path A WalkingArrow_cat C C1
          (@id_func A) (@comp_cat_fapp0 A C A (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 Q)) (@unit_adj_transf A C (@cokernel_adjunction_func C S t T0 Q) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 Q)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
    (@eq_ap (@Transf A C X X) (@Transf A C X Y) (λ a : τ (@Transf A C X X), @comp_fapp0 (Functor_cat A C) X X Y delta a)
      alpha (@id (Functor_cat A C) X) (@one_cat_cokernel_unit_zero_column_from_src_path C S C1 t T T0 Q));

// The normalized counit target is the original whole differential.
symbol one_cat_kernel_counit_target_transf_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@kernel_adjunction_arrow_func C S t
        T P) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
        (@one_cat_kernel_counit_mate_input C S C1 t T T0 P) walking_arrow_tgt)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
≔ let A : Cat ≔ Functor_oplax_cat WalkingArrow_cat C in
  let X : τ (Functor A C) ≔ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src in
  let Y : τ (Functor A C) ≔ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt in
  let D : τ (Functor A A) ≔ (@comp_cat_fapp0 A C A (@initial_arrow_diagram_func C t T0) Y) in
  let H : τ (Functor A A) ≔ (@kernel_adjunction_arrow_func C S t T P) in
  let Z : τ (Functor A A) ≔ (@one_cat_kernel_counit_zero_column_func C S C1 t T P) in
  let v : τ (@Transf A A Z D) ≔ (@iso_evidence_to _ _ _ (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)) in
  let g : τ (@Transf A A H Z) ≔ (@one_cat_kernel_counit_transpose C S C1 t T P) in
  let alpha : τ (@Transf A C Y Y) ≔
    @diagram_oplax_family_map_at A WalkingArrow_cat C Z D v walking_arrow_tgt in
  let beta : τ (@Transf A C X Y) ≔
    @diagram_oplax_family_map_at A WalkingArrow_cat C H Z g walking_arrow_tgt in
  let delta : τ (@Transf A C X Y) ≔
    @diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator in
  @eq_trans (@Transf A C X Y) (@diagram_oplax_family_map_at A WalkingArrow_cat C H D (@comp_fapp0 (Functor_cat A A) H Z D v g) walking_arrow_tgt) (@comp_fapp0 (Functor_cat A C) X Y Y alpha delta) delta
    (@eq_trans (@Transf A C X Y) (@diagram_oplax_family_map_at A WalkingArrow_cat C H D (@comp_fapp0 (Functor_cat A A) H Z D v g) walking_arrow_tgt) (@comp_fapp0 (Functor_cat A C) X Y Y alpha beta) (@comp_fapp0 (Functor_cat A C) X Y Y alpha delta)
      (@one_cat_oplax_family_evaluation_comp_path A WalkingArrow_cat C C1 walking_arrow_tgt H Z D v g)
      (@eq_ap (@Transf A C X Y) (@Transf A C X Y) (λ b : τ (@Transf A C X Y), @comp_fapp0 (Functor_cat A C) X Y Y alpha b) beta delta
        (@one_cat_oplax_diagram_transpose_transf_tgt_path A WalkingArrow_cat C C1
          (@comp_cat_fapp0 A C A (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func A) (@counit_adj_transf C A (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
    (@eq_ap (@Transf A C Y Y) (@Transf A C X Y) (λ a : τ (@Transf A C Y Y), @comp_fapp0 (Functor_cat A C) X Y Y a delta)
      alpha (@id (Functor_cat A C) Y) (@one_cat_kernel_counit_zero_column_to_tgt_path C S C1 t T T0 P));
