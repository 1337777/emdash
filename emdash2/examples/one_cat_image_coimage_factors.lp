require open emdash.emdash3_2_zero_arrow_diagram_observations;
/* Whole factor programs at the original P/Q, with no extra square inputs. */
require open emdash.emdash3_2_one_cat_image_coimage_factors;

// The actual kernel zero-column comparison fixes the nonzero endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@iso_evidence_to _ _ _ (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)))
    ≡ @id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d);

// The actual kernel zero-column comparison fixes the nonzero endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@iso_evidence_from _ _ _ (@one_cat_kernel_counit_zero_column_evidence C S C1 t T T0 P)))
    ≡ @id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d);

// The normalized counit retains its src horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@one_cat_kernel_counit_mate_input C S C1 t T T0 P))
    ≡ @terminal_arrow_fapp0 C t T
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) d);

// The normalized counit retains its tgt horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@one_cat_kernel_counit_mate_input C S C1 t T T0 P))
    ≡ @terminal_arrow_test_outgoing C d;

// The actual cokernel zero-column comparison fixes the nonzero endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@iso_evidence_to _ _ _ (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)))
    ≡ @id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d);

// The actual cokernel zero-column comparison fixes the nonzero endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@iso_evidence_from _ _ _ (@one_cat_cokernel_unit_zero_column_evidence C S C1 t T T0 Q)))
    ≡ @id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d);

// The normalized unit retains its src horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@one_cat_cokernel_unit_mate_input C S C1 t T T0 Q))
    ≡ @terminal_arrow_test_outgoing C d;

// The normalized unit retains its tgt horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) _ _ d (@one_cat_cokernel_unit_mate_input C S C1 t T T0 Q))
    ≡ @initial_arrow_fapp0 C t T0
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 Q) d);

// The coimage_to_target whole map retains action on arbitrary diagram maps.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (u v : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d e))
  ⊢ @fapp1_func _ _ (@tapp1_func (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q)) u v
    : τ (Functor (Hom_cat (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d e) u v)
      (Hom_cat (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) e))
        (@tapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q) u)
        (@tapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q) v)));

// The source_to_image whole map retains action on arbitrary diagram maps.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (u v : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d e))
  ⊢ @fapp1_func _ _ (@tapp1_func (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@adjunction_image_func C S t T T0 P Q) d e (@one_cat_adjunction_source_to_image C S C1 t T T0 P Q)) u v
    : τ (Functor (Hom_cat (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d e) u v)
      (Hom_cat (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) e))
        (@tapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@adjunction_image_func C S t T T0 P Q) d e (@one_cat_adjunction_source_to_image C S C1 t T T0 P Q) u)
        (@tapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@adjunction_image_func C S t T T0 P Q) d e (@one_cat_adjunction_source_to_image C S C1 t T T0 P Q) v)));
