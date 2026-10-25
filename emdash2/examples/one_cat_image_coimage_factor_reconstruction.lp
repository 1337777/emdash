require open emdash.emdash3_2_zero_arrow_diagram_observations;
/* Reviewer-side reconstruction observations of the whole factor programs. */
require open emdash.emdash3_2_one_cat_image_coimage_factors;
require open emdash.emdash3_2_homology_adjunction_record_data;

// Semantic cokernel mate reconstruction, by the existing mate comparison.
// This reviewer helper is an observation; the factor program imports none
// of the ordinary record interfaces from the reference module above.
symbol probe_semantic_cokernel_reconstruction
  [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X)))
  : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) X)
      (@comp_fapp0 C _ _ _
        (@fapp0 _ _ (@adjunction_untranspose_semantic_func (Functor_oplax_cat WalkingArrow_cat C) C
          (@cokernel_adjunction_func C S t T Q) (@initial_arrow_diagram_func C t T)
          (@cokernel_adjunction_evidence C S t T Q) d X) h)
        (@tapp0_fapp0 _ _ _ _ d (@cokernel_adjunction_projection C S t T Q)))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ h))
≔ @eq_trans _ _ _ _
    (@eq_sym _ _ _
      (@eq_ap
        (Functor
          (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d
            (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X))
          (Hom_cat C (@fapp0 _ _ (@cokernel_adjunction_func C S t T Q) d) X))
        (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) X)
        (λ L : τ (Functor
          (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d
            (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X))
          (Hom_cat C (@fapp0 _ _ (@cokernel_adjunction_func C S t T Q) d) X)),
          @comp_fapp0 C _ _ _ (@fapp0 _ _ L h)
            (@tapp0_fapp0 _ _ _ _ d (@cokernel_adjunction_projection C S t T Q)))
        (@cokernel_adjunction_colift_func C S t T Q X d)
        (@adjunction_untranspose_semantic_func (Functor_oplax_cat WalkingArrow_cat C) C
          (@cokernel_adjunction_func C S t T Q) (@initial_arrow_diagram_func C t T)
          (@cokernel_adjunction_evidence C S t T Q) d X)
        (@adjunction_untranspose_semantic_path (Functor_oplax_cat WalkingArrow_cat C) C
          (@cokernel_adjunction_func C S t T Q) (@initial_arrow_diagram_func C t T)
          (@cokernel_adjunction_evidence C S t T Q) d X)))
    (@cokernel_adjunction_colift_reconstruction C S t T Q X d h);

// The actual coimage factor reconstructs f after the original π_f.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @probe_semantic_cokernel_reconstruction C S t T0 Q
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@fapp0 _ _ (@kernel_adjunction_arrow_func C S t T P) d)
      (@tapp0_fapp0 _ _ _ _ d (@one_cat_kernel_counit_mate_input C S C1 t T T0 P))
    : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
      (@comp_fapp0 C _ _ _
        (@tapp0_fapp0 _ _ _ _ d (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q))
        (@tapp0_fapp0 _ _ _ _ d (@adjunction_coimage_projection C S t T T0 P Q)))
      (@terminal_arrow_test_outgoing C d));

// The actual image factor reconstructs f before the original ι_f.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @kernel_adjunction_semantic_boundary_reconstruction C S t T P
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
      (@fapp0 _ _ (@cokernel_adjunction_arrow_func C S t T0 Q) d)
      (@tapp0_fapp0 _ _ _ _ d (@one_cat_cokernel_unit_mate_input C S C1 t T T0 Q))
    : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
      (@comp_fapp0 C _ _ _
        (@tapp0_fapp0 _ _ _ _ d (@adjunction_image_inclusion C S t T T0 P Q))
        (@tapp0_fapp0 _ _ _ _ d (@one_cat_adjunction_source_to_image C S C1 t T T0 P Q)))
      (@terminal_arrow_test_outgoing C d));
