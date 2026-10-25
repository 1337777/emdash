/* The original adjunction cells after ordinary-target transposition. */
require open emdash.emdash3_2_one_cat_kernel_cokernel_transposes;

// The kernel zero column retains its whole src endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  ⊢ @diagram_oplax_family_at_func (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) walking_arrow_src
    ≡ @Const_func (Functor_oplax_cat WalkingArrow_cat C) C t;

// The kernel zero column retains its whole tgt endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (P : τ (@KernelAdjunctionStructure C S t T))
  ⊢ @diagram_oplax_family_at_func (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_kernel_counit_zero_column_func C S C1 t T P) walking_arrow_tgt
    ≡ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt;

// The transposed counit retains its src horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (P : τ (@KernelAdjunctionStructure C S t T)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _ walking_arrow_src
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) d (@one_cat_kernel_counit_transpose C S C1 t T P))
    ≡ @terminal_arrow_fapp0 C t T
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) d);

// The transposed counit retains its tgt horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (P : τ (@KernelAdjunctionStructure C S t T)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _ walking_arrow_tgt
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) d (@one_cat_kernel_counit_transpose C S C1 t T P))
    ≡ @fapp1_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d walking_arrow_tgt walking_arrow_src walking_arrow_generator;

// Its parameter Hom action remains at the original kernel arrow family.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (P : τ (@KernelAdjunctionStructure C S t T)) (d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) d e (@one_cat_kernel_counit_transpose C S C1 t T P)
    : τ (Functor (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d e)
      (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_kernel_counit_zero_column_func C S C1 t T P) e)));

// The cokernel zero column retains its whole src endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  ⊢ @diagram_oplax_family_at_func (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) walking_arrow_src
    ≡ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src;

// The cokernel zero column retains its whole tgt endpoint.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0))
  ⊢ @diagram_oplax_family_at_func (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) walking_arrow_tgt
    ≡ @Const_func (Functor_oplax_cat WalkingArrow_cat C) C t;

// The transposed unit retains its src horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _ walking_arrow_src
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@cokernel_adjunction_arrow_func C S t T0 Q) d (@one_cat_cokernel_unit_transpose C S C1 t T0 Q))
    ≡ @fapp1_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d walking_arrow_tgt walking_arrow_src walking_arrow_generator;

// The transposed unit retains its tgt horizontal component.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _ walking_arrow_tgt
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@cokernel_adjunction_arrow_func C S t T0 Q) d (@one_cat_cokernel_unit_transpose C S C1 t T0 Q))
    ≡ @initial_arrow_fapp0 C t T0
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 Q) d);

// Its parameter Hom action remains at the original cokernel arrow family.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  (Q : τ (@CokernelAdjunctionStructure C S t T0)) (d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  ⊢ @tapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) (@cokernel_adjunction_arrow_func C S t T0 Q) d e (@one_cat_cokernel_unit_transpose C S C1 t T0 Q)
    : τ (Functor (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) d e)
      (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_cokernel_unit_zero_column_func C S C1 t T0 Q) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) e)));
