require open emdash.emdash3_2_one_cat_adjunction_family_views;
require open emdash.emdash3_2_one_cat_functor_closure;
require open emdash.emdash3_2_one_cat_action_paths;
/* Native whole kernel/cokernel inverse-mate observations.
   Faithfulness, annihilation and compatibility are derived from the original
   whole adjunctions and the ordinary family presentations. Original K/Q
   selections remain fixed; no ordinary factor record drives these operations. */
require open emdash.emdash3_2_one_cat_diagram_family_paths;
require open emdash.emdash3_2_kernel_cokernel_adjunctions;
require open emdash.emdash3_2_one_cat_terminal_family_paths;
require open emdash.emdash3_2_zero_arrow_family_action_paths;
require open emdash.emdash3_2_adjunction_untranspose_naturality;
require open emdash.emdash3_2_one_cat_adjunction_families;

// Generic component observation, before any inverse-mate specialization.
protected symbol kernel_cokernel_family_map_component_path [B I C : Cat]
 (F G : τ (Functor B (Functor_oplax_cat I C)))
 (eta : τ (@Transf B (Functor_oplax_cat I C) F G))
 (i : τ (Obj I)) (b : τ (Obj B))
 : τ (@= (Hom C
    (@fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) (@fapp0 B (Functor_oplax_cat I C) F b))
    (@fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) (@fapp0 B (Functor_oplax_cat I C) G b)))
  (@tapp0_fapp0 B C
    (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F)
    (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) G) b
    (@diagram_oplax_family_map_at B I C F G eta i))
  (@fapp1_fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i)
    (@fapp0 B (Functor_oplax_cat I C) F b) (@fapp0 B (Functor_oplax_cat I C) G b)
    (@tapp0_fapp0 B (Functor_oplax_cat I C) F G b eta)))
≔ @eq_refl (Hom C
    (@fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) (@fapp0 B (Functor_oplax_cat I C) F b))
    (@fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) (@fapp0 B (Functor_oplax_cat I C) G b)))
  (@fapp1_fapp0 (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i)
    (@fapp0 B (Functor_oplax_cat I C) F b) (@fapp0 B (Functor_oplax_cat I C) G b)
    (@tapp0_fapp0 B (Functor_oplax_cat I C) F G b eta));

// Faithfulness of E₀ after the native whole kernel inverse mate.
symbol one_cat_kernel_family_projection_reflect_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (A : τ (Functor B C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat
    C)))
  (k l : τ (@Transf B C A (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
    D))) (p : τ (@= (@Transf B C A (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T) A) D (@fapp0 _ _ (@one_cat_adjunction_family_untranspose_func B C
    (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1)
    (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P) A
    D) k) walking_arrow_src) (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat
    WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D (@fapp0 _ _
    (@one_cat_adjunction_family_untranspose_func B C (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category
    WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
    (@kernel_adjunction_evidence C S t T P) A D) l) walking_arrow_src)))
  : τ (@= (@Transf B C A (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) D))
    k l)
≔ @eq_ap (@Transf B (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) D) (@Transf B C A (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
  (@kernel_adjunction_func C S t T P) D)) (λ h : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 B C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D), @fapp0 _ _
  (@one_cat_adjunction_family_transpose_func B C (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category
  WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
  (@kernel_adjunction_evidence C S t T P) A D) h)
    (@fapp0 _ _ (@one_cat_adjunction_family_untranspose_func B C (Functor_oplax_cat WalkingArrow_cat C) C1
      (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func
      C S t T P) (@kernel_adjunction_evidence C S t T P) A D) k) (@fapp0 _ _
      (@one_cat_adjunction_family_untranspose_func B C (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category
      WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P) A D) l)
    (@one_cat_terminal_family_test_reflect_path B C C1 t T T0 A D (@fapp0 _ _
      (@one_cat_adjunction_family_untranspose_func B C (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category
      WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P) A D) k) (@fapp0 _ _ (@one_cat_adjunction_family_untranspose_func B C
      (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)
      A D) l) p);

// Faithfulness of E₁ after the native whole cokernel inverse mate.
symbol one_cat_cokernel_family_projection_reflect_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@CokernelAdjunctionStructure C S t T0)) (A : τ (Functor B C)) (D : τ (Functor B (Functor_oplax_cat
    WalkingArrow_cat C)))
  (k l : τ (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P)
    D) A)) (p : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) A)
    (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
    (@initial_arrow_diagram_func C t T0) A) (@fapp0 _ _ (@one_cat_adjunction_family_transpose_func B (Functor_oplax_cat
    WalkingArrow_cat C) C (@one_cat_oplax_functor_category WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P)
    (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 P) D A) k) walking_arrow_tgt)
    (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
    (@initial_arrow_diagram_func C t T0) A) (@fapp0 _ _ (@one_cat_adjunction_family_transpose_func B (Functor_oplax_cat
    WalkingArrow_cat C) C (@one_cat_oplax_functor_category WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P)
    (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 P) D A) l) walking_arrow_tgt)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) D)
    A) k l)
≔ @eq_ap (@Transf B (Functor_oplax_cat WalkingArrow_cat C) D (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) A)) (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
  (@cokernel_adjunction_func C S t T0 P) D) A) (λ h : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) D (@comp_cat_fapp0
  B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) A)), @fapp0 _ _
  (@one_cat_adjunction_family_untranspose_func B (Functor_oplax_cat WalkingArrow_cat C) C (@one_cat_oplax_functor_category
  WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
  (@cokernel_adjunction_evidence C S t T0 P) D A) h)
    (@fapp0 _ _ (@one_cat_adjunction_family_transpose_func B (Functor_oplax_cat WalkingArrow_cat C) C
      (@one_cat_oplax_functor_category WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 P) D A) k) (@fapp0 _ _
      (@one_cat_adjunction_family_transpose_func B (Functor_oplax_cat WalkingArrow_cat C) C (@one_cat_oplax_functor_category
      WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P) D A) l)
    (@one_cat_initial_family_test_reflect_path B C C1 t T T0 A D (@fapp0 _ _
      (@one_cat_adjunction_family_transpose_func B (Functor_oplax_cat WalkingArrow_cat C) C (@one_cat_oplax_functor_category
      WalkingArrow_cat C C1) C1 (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P) D A) k) (@fapp0 _ _ (@one_cat_adjunction_family_transpose_func B
      (Functor_oplax_cat WalkingArrow_cat C) C (@one_cat_oplax_functor_category WalkingArrow_cat C C1) C1
      (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t
      T0 P) D A) l) p);

// E₀ of the original counit is the selected whole kernel inclusion κ.
symbol one_cat_kernel_structural_evaluation_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func
    WalkingArrow_cat C walking_arrow_src)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat
    C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat
    C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
    (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)
    (@kernel_adjunction_inclusion C S t T P))
≔ eq_refl (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
  WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func
  C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P))
  walking_arrow_src);

// The original counit derives ∂∘κ=0 as one equality of whole transformations.
symbol one_cat_kernel_whole_annihilation [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func
    WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C)
    (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
    walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@kernel_adjunction_inclusion C S t T P))
    (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@Const_func
    (Functor_oplax_cat WalkingArrow_cat C) C t) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
    (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
    WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) walking_arrow_src walking_arrow_tgt
    walking_arrow_generator) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
    (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func
    C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
≔ @eq_trans (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
  (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
  WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
  walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf
  WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@kernel_adjunction_inclusion C S t
  T P)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P)
  (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
  walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt
  walking_arrow_generator) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
  (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C
  t T) (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
  (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat
  C) C) (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
  (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat
  WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
  WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
  walking_arrow_tgt)) walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_transf
  (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
  WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src
  walking_arrow_tgt walking_arrow_generator)) (@eq_sym (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
  (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0
  (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func
  WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
  (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
  (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
  WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func
  C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P))
  walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T
  P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat
  C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt
  walking_arrow_generator) (@kernel_adjunction_inclusion C S t T P))
      (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@Transf (Functor_oplax_cat WalkingArrow_cat C)
        C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (λ k
        : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)), @comp_fapp0 (Functor_cat (Functor_oplax_cat
        WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
        (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator) k)
        (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
        WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
        (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
        (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
        (@kernel_adjunction_evidence C S t T P)) walking_arrow_src) (@kernel_adjunction_inclusion C S t T P)
        (@one_cat_kernel_structural_evaluation_path C S C1 t T T0 P)))
    (@eq_trans (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
      (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
      (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_map_at (Functor_oplax_cat
      WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
      WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func
      (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T
      P)) walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@kernel_adjunction_func
      C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0
      (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator)) (@hom_to_path (@Transf_cat (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
  ((@one_cat_functor_category (Functor_oplax_cat WalkingArrow_cat C) C C1) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
  (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
      (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
      (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_map_at (Functor_oplax_cat
      WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
      WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func
      (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T
      P)) walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator))
  (@one_cat_modification (Functor_oplax_cat WalkingArrow_cat C) C C1 (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
      (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
      (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_map_at (Functor_oplax_cat
      WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
      WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func
      (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T
      P)) walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator))
    (λ d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)), @path_to_hom (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
      (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
      (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
      (@kernel_adjunction_evidence C S t T P)) walking_arrow_src)))
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_map_at (Functor_oplax_cat
      WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
      WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func
      (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T
      P)) walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator)))
      (@eq_sym _ _ _ (@one_cat_component_naturality_path (Functor_oplax_cat WalkingArrow_cat C) C C1 (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C)
        C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) d)
        (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C)
        C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) d (@counit_adj_transf C
        (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
        (@kernel_adjunction_evidence C S t T P)))))))) (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
        (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_tgt)) (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (λ k : τ (@Transf (Functor_oplax_cat
        WalkingArrow_cat C) C (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@diagram_oplax_evaluation_at_func
        WalkingArrow_cat C walking_arrow_tgt)), @comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C)
        (@kernel_adjunction_func C S t T P) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) k (@diagram_oplax_family_transf (Functor_oplax_cat
        WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
        WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P))
        walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
        WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)
        (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@counit_adj_transf C
        (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)
        (@kernel_adjunction_evidence C S t T P)) walking_arrow_tgt) (@diagram_oplax_family_transf (Functor_oplax_cat
        WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
        WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_tgt)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@one_cat_initial_family_arrow_path (Functor_oplax_cat WalkingArrow_cat C) C C1 t T0 (@diagram_oplax_evaluation_at_func
        WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C)
        WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
        (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P)) (@id_func (Functor_oplax_cat
        WalkingArrow_cat C)) (@counit_adj_transf C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t
        T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) walking_arrow_tgt))));

// E₁ of the original unit is the selected whole cokernel projection q.
symbol one_cat_cokernel_structural_evaluation_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
    walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat
    C) WalkingArrow_cat C (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat
    C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P))
    (@unit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P)
    (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt)
    (@cokernel_adjunction_projection C S t T0 P))
≔ eq_refl (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
  WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
  WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
  (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt);

// The original unit derives q∘∂=0 as one equality of whole transformations.
symbol one_cat_cokernel_whole_annihilation [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@CokernelAdjunctionStructure C S t T0))
  : τ (@= (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
    walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat
    C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func
    WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P) (@cokernel_adjunction_projection C S
    t T0 P) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt
    walking_arrow_generator)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C
    t) (@cokernel_adjunction_func C S t T0 P) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C)
    WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
    (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt
    walking_arrow_generator) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
    (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func
    C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) walking_arrow_src walking_arrow_tgt
    walking_arrow_generator)))
≔ @eq_trans (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
  walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat
  C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func
  WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P) (@cokernel_adjunction_projection C S t
  T0 P) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
  (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
  walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S
  t T0 P) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
  WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
  WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
  (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
  walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
  WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func (Functor_oplax_cat
  WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P) (@diagram_oplax_family_transf (Functor_oplax_cat
  WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
  WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src
  walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat
  C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func
  C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) walking_arrow_src walking_arrow_tgt
  walking_arrow_generator)) (@eq_sym (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func
  WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
  WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
  (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
  (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
  WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
  WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
  (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
  walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
  WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
  (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
  (@cokernel_adjunction_projection C S t T0 P) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src
  walking_arrow_tgt walking_arrow_generator))
      (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)) (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (λ
        k : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)), @comp_fapp0 (Functor_cat (Functor_oplax_cat
        WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P) k
        (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
        (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
        WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
        WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
        (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@cokernel_adjunction_projection C S t T0 P)
        (@one_cat_cokernel_structural_evaluation_path C S C1 t T T0 P)))
    (@eq_trans (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func
      (Functor_oplax_cat WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P) (@diagram_oplax_family_transf
      (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C
      (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P))
      walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_map_at (Functor_oplax_cat
      WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C
      (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t
      T0 P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C)
      C t) (@cokernel_adjunction_func C S t T0 P) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C)
      WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt
      walking_arrow_generator) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src))
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@eq_sym (@Transf (Functor_oplax_cat WalkingArrow_cat C)
      C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P))
      (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@hom_to_path (@Transf_cat (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P))
  ((@one_cat_functor_category (Functor_oplax_cat WalkingArrow_cat C) C C1) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P))
  (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
      walking_arrow_src walking_arrow_tgt walking_arrow_generator))
  (@one_cat_modification (Functor_oplax_cat WalkingArrow_cat C) C C1 (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
      walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (λ d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)), @path_to_hom (Hom_cat C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) d))
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P) d (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
      walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat C) C t) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat
      WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src)))
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P) d (@comp_fapp0 (Functor_cat (Functor_oplax_cat
      WalkingArrow_cat C) C) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_adjunction_func C S t T0 P)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
      WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
      (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
      WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
      (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
      (@eq_sym _ _ _ (@one_cat_component_naturality_path (Functor_oplax_cat WalkingArrow_cat C) C C1 (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat
        C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0
        P)) d)
        (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat
        C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0
        P)) d (@unit_adj_transf (Functor_oplax_cat
        WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
        (@cokernel_adjunction_evidence C S t T0 P))))))))) (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C)
        C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func (Functor_oplax_cat
        WalkingArrow_cat C) C t)) (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func
        WalkingArrow_cat C walking_arrow_src) (@cokernel_adjunction_func C S t T0 P)) (λ k : τ (@Transf (Functor_oplax_cat
        WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func
        (Functor_oplax_cat WalkingArrow_cat C) C t)), @comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@Const_func (Functor_oplax_cat WalkingArrow_cat
        C) C t) (@cokernel_adjunction_func C S t T0 P) (@diagram_oplax_family_transf (Functor_oplax_cat WalkingArrow_cat C)
        WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) walking_arrow_src
        walking_arrow_tgt walking_arrow_generator) k)
      (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C) WalkingArrow_cat C (@id_func (Functor_oplax_cat
        WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0 P)) (@unit_adj_transf (Functor_oplax_cat
        WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P) (@initial_arrow_diagram_func C t T0)
        (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src) (@diagram_oplax_family_transf (Functor_oplax_cat
        WalkingArrow_cat C) WalkingArrow_cat C (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat
        WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C
        walking_arrow_src)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@one_cat_terminal_family_arrow_path (Functor_oplax_cat WalkingArrow_cat C) C C1 t T (@diagram_oplax_evaluation_at_func
        WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_family_map_at (Functor_oplax_cat WalkingArrow_cat C)
        WalkingArrow_cat C (@id_func (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat
        C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_func C S t T0
        P)) (@unit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_func C S t T0 P)
        (@initial_arrow_diagram_func C t T0) (@cokernel_adjunction_evidence C S t T0 P)) walking_arrow_src))));

// Projected native kernel inverse mating preserves precomposition by a whole map.
symbol one_cat_kernel_family_projection_precomp_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (P : τ (@KernelAdjunctionStructure C S t T))
  (A0 A1 : τ (Functor B C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  (a : τ (@Transf B C A0 A1)) (h : τ (@Transf B C A1 (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (Functor_cat B C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P))
    D)))
  : τ (@= (@Transf B C A0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0) D (@fapp0 _ _ (@adjunction_untranspose_func (Functor_cat B C) (Functor_cat B (Functor_oplax_cat WalkingArrow_cat
    C)) (@comp_cat_cov_func B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T))
    (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P))
    (@one_cat_postcomp_adjunction B C (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat
    C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t
    T P)) A0 D) (@comp_fapp0 (Functor_cat B C) A0 A1 (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (Functor_cat B C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D)
    h a)) walking_arrow_src) (@comp_fapp0 (Functor_cat B C) A0 A1 (@diagram_oplax_family_at_func B WalkingArrow_cat C D
    walking_arrow_src) (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A1) D (@fapp0 _ _ (@adjunction_untranspose_func (Functor_cat B C)
    (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_cov_func B C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C
    (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C (Functor_oplax_cat WalkingArrow_cat C) C1
    (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C
    S t T P) (@kernel_adjunction_evidence C S t T P)) A1 D) h) walking_arrow_src) a))
≔ let M : Cat ≔ Functor_oplax_cat WalkingArrow_cat C in
  let R : Cat ≔ Functor_cat B C in
  let L : Cat ≔ Functor_cat B M in
  let J : τ (Functor C M) ≔ @terminal_arrow_diagram_func C t T in
  let K : τ (Functor M C) ≔ @kernel_adjunction_func C S t T P in
  let F : τ (Functor R L) ≔ @comp_cat_cov_func B C M J in
  let G : τ (Functor L R) ≔ @comp_cat_cov_func B M C K in
  let JD : τ (@Adjunction R L F G) ≔ @one_cat_postcomp_adjunction B C M C1
    (@one_cat_oplax_functor_category WalkingArrow_cat C C1) J K (@kernel_adjunction_evidence C S t T P) in
  let J0 : τ (Functor B M) ≔ @fapp0 R L F A0 in
  let J1 : τ (Functor B M) ≔ @fapp0 R L F A1 in
  let U0 : τ (Functor (Hom_cat R A0 (@fapp0 L R G D)) (Hom_cat L J0 D)) ≔
    @adjunction_untranspose_func R L F G JD A0 D in
  let U1 : τ (Functor (Hom_cat R A1 (@fapp0 L R G D)) (Hom_cat L J1 D)) ≔
    @adjunction_untranspose_func R L F G JD A1 D in
  let h1 : τ (Hom L J1 D) ≔ @fapp0 _ _ U1 h in
  let Fa : τ (Hom L J0 J1) ≔ @fapp1_fapp0 R L F A0 A1 a in
  let h0 : τ (Hom L J0 D) ≔ @fapp0 _ _ U0 (@comp_fapp0 R A0 A1 (@fapp0 L R G D) h a) in
  let p0 : τ (@= (Hom L J0 D) (@comp_fapp0 L J0 J1 D h1 Fa) h0) ≔
    @one_cat_untranspose_precomp_path R L
      (@one_cat_functor_category B M (@one_cat_oplax_functor_category WalkingArrow_cat C C1))
      F G JD A0 A1 D a h in
  let V : τ (Functor M C) ≔ @diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src in
  let Y : τ (Functor B C) ≔ @diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src in
  let alpha : τ (@Transf B C A0 Y) ≔ @diagram_oplax_family_map_at B WalkingArrow_cat C
    (@comp_cat_fapp0 B C M J A0) D h0 walking_arrow_src in
  let gamma : τ (@Transf B C A1 Y) ≔ @diagram_oplax_family_map_at B WalkingArrow_cat C
    (@comp_cat_fapp0 B C M J A1) D h1 walking_arrow_src in
  let beta : τ (@Transf B C A0 Y) ≔ @comp_fapp0 R A0 A1 Y gamma a in
  @hom_to_path (@Transf_cat B C A0 Y) ((@one_cat_functor_category B C C1) A0 Y) alpha beta
    (@one_cat_modification B C C1 A0 Y alpha beta
      (λ b : τ (Obj B),
        let h1b : τ (Hom C (@fapp0 B C A1 b) (@fapp0 B C Y b)) ≔
          @fapp1_fapp0 M C V (@fapp0 B M J1 b) (@fapp0 B M D b)
            (@tapp0_fapp0 B M J1 D b h1) in
        let Fab : τ (Hom C (@fapp0 B C A0 b) (@fapp0 B C A1 b)) ≔
          @fapp1_fapp0 M C V (@fapp0 B M J0 b) (@fapp0 B M J1 b)
            (@tapp0_fapp0 B M J0 J1 b Fa) in
        let h0b : τ (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b)) ≔
          @fapp1_fapp0 M C V (@fapp0 B M J0 b) (@fapp0 B M D b)
            (@tapp0_fapp0 B M J0 D b h0) in
        let ab : τ (Hom C (@fapp0 B C A0 b) (@fapp0 B C A1 b)) ≔ @tapp0_fapp0 B C A0 A1 b a in
        @path_to_hom (Hom_cat C (@fapp0 B C A0 b) (@fapp0 B C Y b))
          (@tapp0_fapp0 B C A0 Y b alpha) (@tapp0_fapp0 B C A0 Y b beta)
          (@eq_trans (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b))
            (@tapp0_fapp0 B C A0 Y b alpha) h0b (@tapp0_fapp0 B C A0 Y b beta)
            (@kernel_cokernel_family_map_component_path B WalkingArrow_cat C
              (@comp_cat_fapp0 B C M J A0) D h0 walking_arrow_src b)
            (@eq_trans (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b)) h0b
              (@comp_fapp0 C (@fapp0 B C A0 b) (@fapp0 B C A1 b) (@fapp0 B C Y b) h1b Fab)
              (@tapp0_fapp0 B C A0 Y b beta)
              (@eq_sym _ _ _
                (@eq_ap (Hom L J0 D) (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b))
                  (λ v : τ (Hom L J0 D), @fapp1_fapp0 M C V
                    (@fapp0 B M J0 b) (@fapp0 B M D b) (@tapp0_fapp0 B M J0 D b v))
                  (@comp_fapp0 L J0 J1 D h1 Fa) h0 p0))
              (@eq_trans (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b))
                (@comp_fapp0 C (@fapp0 B C A0 b) (@fapp0 B C A1 b) (@fapp0 B C Y b) h1b Fab)
                (@comp_fapp0 C (@fapp0 B C A0 b) (@fapp0 B C A1 b) (@fapp0 B C Y b) h1b ab)
                (@tapp0_fapp0 B C A0 Y b beta)
                (@eq_ap (@Transf B C A0 A1) (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b))
                  (λ v : τ (@Transf B C A0 A1), @comp_fapp0 C
                    (@fapp0 B C A0 b) (@fapp0 B C A1 b) (@fapp0 B C Y b)
                    h1b (@tapp0_fapp0 B C A0 A1 b v)) _ a
                  (@terminal_arrow_family_action_source_path B C t T A0 A1 a))
                (@eq_ap (Hom C (@fapp0 B C A1 b) (@fapp0 B C Y b))
                  (Hom C (@fapp0 B C A0 b) (@fapp0 B C Y b))
                  (λ v : τ (Hom C (@fapp0 B C A1 b) (@fapp0 B C Y b)),
                    @comp_fapp0 C (@fapp0 B C A0 b) (@fapp0 B C A1 b) (@fapp0 B C Y b) v ab)
                  h1b (@tapp0_fapp0 B C A1 Y b gamma)
                  (@eq_sym _ _ _ (@kernel_cokernel_family_map_component_path B WalkingArrow_cat C
                    (@comp_cat_fapp0 B C M J A1) D h1 walking_arrow_src b))))))));

// Projected native kernel inverse mating sends the whole canonical zero to zero.
symbol one_cat_kernel_family_projection_zero_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (A : τ (Functor B C))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C A (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)) (@diagram_oplax_family_map_at
    B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D (@fapp0 _ _
    (@adjunction_untranspose_func (Functor_cat B C) (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@comp_cat_cov_func B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func
    B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C
    (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1)
    (@terminal_arrow_diagram_func C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P))
    A D) (@comp_fapp0 (Functor_cat B C) A (@Const_func B C t) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (Functor_cat B C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D)
    (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
    (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B C)
    (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D))
    walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_transf B WalkingArrow_cat C
    (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) walking_arrow_src
    walking_arrow_tgt walking_arrow_generator))) walking_arrow_src) (@comp_fapp0 (Functor_cat B C) A (@Const_func B C
    t) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_transf B WalkingArrow_cat C
    (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
    (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)) walking_arrow_src walking_arrow_tgt
    walking_arrow_generator) (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat
    WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) walking_arrow_src walking_arrow_tgt
    walking_arrow_generator)))
≔ @eq_trans (@Transf B C A (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src))
  (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) D (@fapp0 _ _ (@adjunction_untranspose_func (Functor_cat B C) (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
  (@comp_cat_cov_func B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func B
  (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C
  (Functor_oplax_cat WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func
  C t T) (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) A D) (@comp_fapp0 (Functor_cat B
  C) A (@Const_func B C t) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B C)
  (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D)
  (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B C)
  (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D)) walking_arrow_src
  walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) walking_arrow_src walking_arrow_tgt
  walking_arrow_generator))) walking_arrow_src) (@comp_fapp0 (Functor_cat B C) A (@Const_func B C t)
  (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_map_at B WalkingArrow_cat C
  (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@Const_func B C t)) D (@fapp0 _ _
  (@adjunction_untranspose_func (Functor_cat B C) (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_cov_func
  B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func B (Functor_oplax_cat
  WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C (Functor_oplax_cat
  WalkingArrow_cat C) C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T)
  (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) (@Const_func B C t) D)
  (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
  (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B C)
  (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D)) walking_arrow_src
  walking_arrow_tgt walking_arrow_generator)) walking_arrow_src) (@diagram_oplax_family_transf B WalkingArrow_cat C
  (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) walking_arrow_src
  walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat B C) A (@Const_func B C t)
  (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_transf B WalkingArrow_cat C
  (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@diagram_oplax_family_at_func
  B WalkingArrow_cat C D walking_arrow_src)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)
  (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) walking_arrow_src walking_arrow_tgt walking_arrow_generator))
  (@one_cat_kernel_family_projection_precomp_path B C S C1 t T P A (@Const_func B C t) D (@diagram_oplax_family_transf B
  WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A)
  walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@diagram_oplax_family_transf B WalkingArrow_cat C
  (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B
  (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C
  (@kernel_adjunction_func C S t T P)) D)) walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@eq_ap
  (@Transf B C (@Const_func B C t) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)) (@Transf B C A
  (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src))
      (λ v : τ (@Transf B C (@Const_func B C t) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)),
        @comp_fapp0 (Functor_cat B C) A (@Const_func B C t) (@diagram_oplax_family_at_func B WalkingArrow_cat C D
        walking_arrow_src) v (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat
        WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) walking_arrow_src walking_arrow_tgt
        walking_arrow_generator))
      (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@Const_func B C t)) D (@fapp0 _ _ (@adjunction_untranspose_func (Functor_cat B C) (Functor_cat B
        (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_cov_func B C (Functor_oplax_cat WalkingArrow_cat C)
        (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C
        (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C (Functor_oplax_cat WalkingArrow_cat C) C1
        (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T)
        (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) (@Const_func B C t) D)
        (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B
        C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D))
        walking_arrow_src walking_arrow_tgt walking_arrow_generator)) walking_arrow_src) (@diagram_oplax_family_transf B
        WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
        (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)) walking_arrow_src walking_arrow_tgt
        walking_arrow_generator)
      (@one_cat_initial_family_arrow_path B C C1 t T0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D
        walking_arrow_src) (@diagram_oplax_family_map_at B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@Const_func B C t)) D (@fapp0 _ _ (@adjunction_untranspose_func
        (Functor_cat B C) (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (@comp_cat_cov_func B C (Functor_oplax_cat
        WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat
        C) C (@kernel_adjunction_func C S t T P)) (@one_cat_postcomp_adjunction B C (Functor_oplax_cat WalkingArrow_cat C)
        C1 (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@terminal_arrow_diagram_func C t T)
        (@kernel_adjunction_func C S t T P) (@kernel_adjunction_evidence C S t T P)) (@Const_func B C t) D)
        (@diagram_oplax_family_transf B WalkingArrow_cat C (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C)
        (@initial_arrow_diagram_func C t T0) (@fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat B
        C) (@comp_cat_cov_func B (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) D))
        walking_arrow_src walking_arrow_tgt walking_arrow_generator)) walking_arrow_src)));
