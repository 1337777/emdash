/* Universal records observing the existing whole H = Q ∘ Arr(K(h) ∘ η).
   These point records retain the actual boundary factor. They do not redefine
   H, cap its higher action, or impose a new diagram grammar. */
require open emdash.emdash3_2_homology_records;
require open emdash.emdash3_2_homology_adjunction_record_data;
require open emdash.emdash3_2_kernel_adjunction_records;
require open emdash.emdash3_2_cokernel_adjunction_records;
require open emdash.emdash3_2_homology_families;

/* Boundary factor from an ACTUAL whole unit formula, not a chosen raw lift. */

symbol kernel_semantic_boundary [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X) d))
  : τ (Hom C X (@fapp0 _ _ (@kernel_presentation_func C S t T W P) d))
≔ @kernel_adjunction_semantic_boundary C S t T
    (@kernel_presentation_structure C S t T W P) X d h;

symbol kernel_semantic_boundary_reconstruction [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X) d))
  : τ (@= (Hom C X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d))
      (@comp_fapp0 C X (@fapp0 _ _ (@kernel_presentation_func C S t T W P) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@tapp0_fapp0 _ _ _ _ d (@kernel_presentation_inclusion C S t T W P)) (@kernel_semantic_boundary C S t T W P X d h))
      (@terminal_arrow_test_incoming C t T X d h))
≔ @kernel_adjunction_semantic_boundary_reconstruction C S t T
    (@kernel_presentation_structure C S t T W P) X d h;

symbol kernel_semantic_boundary_factor [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X) d))
  : τ (@KernelFactorSpace C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@terminal_arrow_test_outgoing C d) (@fapp0 _ _ (@kernel_presentation_func C S t T W P) d) (@tapp0_fapp0 _ _ _ _ d (@kernel_presentation_inclusion C S t T W P)) X
      (@terminal_arrow_kernel_test C S C1 t T X d h))
≔ @kernel_adjunction_semantic_boundary_factor C S C1 t T
    (@kernel_presentation_structure C S t T W P) X d h;

/* All operational fields are the whole family's own observations. */

symbol homology_family_record [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [T0 : τ (@TerminalObject (TotalOp_cat C) t)]
  [W : τ (@HasComputationalKernels C S)] [V : τ (@HasComputationalCokernels C S)]
  (P : τ (@KernelPresentation C S t T W)) (Q : τ (@CokernelPresentation C S t T0 V))
  (A : τ (Functor B C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C)
    (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D))
  (b : τ (Obj B))
  : τ (@HomologyRecord C S (@fapp0 B C A b) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b)) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b))
      (@homology_family_pair B C S C1 t T A D h b))
≔ @homology_record_intro C S (@fapp0 B C A b) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b)) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b))
    (@homology_family_pair B C S C1 t T A D h b)
    (@kernel_presentation_record C S t T W P (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b))
    (@kernel_semantic_boundary_factor C S C1 t T W P (@fapp0 B C A b) (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C) D b) (@tapp0_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D b h))
    (@cokernel_presentation_record C S t T0 V Q
      (@fapp0 B (Functor_oplax_cat WalkingArrow_cat C)
        (@kernel_family_boundary_diagram_func B C S t T W P A D h) b));
