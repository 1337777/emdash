/* Original image cover A→Im(a) from the original coimage quotient and fixed comparison. */
require open emdash.emdash3_2_one_cat_coimage_cover_descent;
require open emdash.emdash3_2_one_cat_adjunction_normality;

symbol one_cat_image_family_source_transf [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (F : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0 B
    (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F))
≔ (@comp_fapp0 (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src)
  (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) F)
  (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@fapp0 _ _
  (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q)
  (@adjunction_image_func C S t T T0 P Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))
  (@cokernel_adjunction_family_projection_transf B C S t T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat
  C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) F)));

symbol one_cat_image_family_source_reflect_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (N : τ (@OneCatAdjunctionNormality C S C1 t T T0 P Q))
  (F : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C))) (Y : τ (Functor B C))
  (u v : τ (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0
    P Q) F) Y))
  (p : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) Y) (@comp_fapp0
    (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0 B
    (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) Y u
    (@one_cat_image_family_source_transf B C S C1 t T T0 P Q F)) (@comp_fapp0 (Functor_cat B C)
    (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0 B (Functor_oplax_cat
    WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) Y v (@one_cat_image_family_source_transf B
    C S C1 t T T0 P Q F))))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0
    P Q) F) Y) u v)
≔ @omega_equiv_precomp_reflect_path (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
  (@adjunction_coimage_func C S t T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
  (@adjunction_image_func C S t T T0 P Q) F) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat
  WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q))
  (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))
    (@one_cat_adjunction_normality_family B C S C1 t T T0 P Q N F) Y u v
    (@one_cat_cokernel_family_quotient_reflect_path B C S C1 t T T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat
      WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) F) Y
      (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_coimage_func C S t T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_image_func C S t T T0 P Q) F) Y u (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat
        WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P
        Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)))
      (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_coimage_func C S t T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_image_func C S t T T0 P Q) F) Y v (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat
        WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P
        Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)))
      (@eq_trans _ _ _ _ (@eq_sym _ _ _ (@comp_assoc (Functor_cat B C) (@diagram_oplax_family_at_func B
        WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_coimage_func C S t T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
        (@adjunction_image_func C S t T T0 P Q) F) Y u (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat
        WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P
        Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))
        (@cokernel_adjunction_family_projection_transf B C S t T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat
        WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) F))))
        (@eq_trans _ _ _ _ p (@comp_assoc (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C F
          walking_arrow_src) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S
          t T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T
          T0 P Q) F) Y v (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F
          (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q))
          (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)) (@cokernel_adjunction_family_projection_transf
          B C S t T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
          (@kernel_adjunction_arrow_func C S t T P) F))))));

// Compare the two restrictions of the same original kernel inclusion.
symbol one_cat_image_family_inclusion_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (F : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0
    P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt))
    (@kernel_adjunction_family_inclusion_transf B C S t T P (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C)
    (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F)) (@fapp0 _ _
    (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
    (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P
    (@cokernel_adjunction_arrow_func C S t T0 Q))))
≔ @eq_trans (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@kernel_adjunction_family_inclusion_transf B C S t T P (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)))
      (@one_cat_kernel_family_inclusion_whisker_path B C S C1 t T P (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F))
      (@eq_trans (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@fapp0 _ _ (@comp_cat_con_fapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_arrow_func C S t T0 Q) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P))) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)))
        (@eq_sym (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@fapp0 _ _ (@comp_cat_con_fapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_arrow_func C S t T0 Q) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P))) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P))
          (@prewhisker_assoc_path B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C F (@cokernel_adjunction_arrow_func C S t T0 Q) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@kernel_adjunction_inclusion C S t T P)))
        (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt))
          (λ u : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)), @fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) u)
          (@fapp0 _ _ (@comp_cat_con_fapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_arrow_func C S t T0 Q) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P)) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q))
          (@eq_sym (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)) (@fapp0 _ _ (@comp_cat_con_fapp1_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_adjunction_arrow_func C S t T0 Q) (@kernel_adjunction_func C S t T P) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)) (@kernel_adjunction_inclusion C S t T P))
            (@one_cat_kernel_family_inclusion_whisker_path (Functor_oplax_cat WalkingArrow_cat C) C S C1 t T P (@cokernel_adjunction_arrow_func C S t T0 Q)))));

// κ_Im∘a_F is the original coimage-to-target factor.
symbol one_cat_image_family_comparison_factor_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (F : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T
    T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@comp_fapp0 (Functor_cat B
    C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) F)
    (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F)
    (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)
    (@kernel_adjunction_family_inclusion_transf B C S t T P (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C)
    (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0 Q) F)) (@fapp0 _ _
    (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q)
    (@adjunction_image_func C S t T T0 P Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))) (@fapp0 _ _
    (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q)
    (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@one_cat_adjunction_coimage_to_target C
    S C1 t T T0 P Q)))
≔ @eq_trans _ _ _ _
    (@eq_ap (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T
      T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@Transf B C
      (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) F)
      (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt))
      (λ k : τ (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t
        T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)), (@comp_fapp0
        (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t
        T T0 P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P
        Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt) k (@fapp0 _ _
        (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P
        Q) (@adjunction_image_func C S t T T0 P Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)))) _ _
      (@one_cat_image_family_inclusion_path B C S C1 t T T0 P Q F))
    (@eq_trans _ _ _ _ (@eq_sym _ _ _ (@prewhisker_comp_path B (Functor_oplax_cat WalkingArrow_cat C) C C1 F
      (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q)
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@one_cat_coimage_image_comparison C S
      C1 t T T0 P Q) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P
      (@cokernel_adjunction_arrow_func C S t T0 Q))))
      (@eq_ap (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
        (@Transf B C (@comp_cat_fapp0 B
        (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func
        B WalkingArrow_cat C F walking_arrow_tgt))
        (λ v : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)
          (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)), (@fapp0 _ _
          (@comp_cat_con_fapp1_func B (Functor_oplax_cat WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0
          P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) v))
        (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))
        (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q)
        (@eq_trans (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@adjunction_coimage_func C S t T T0 P Q) (@fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@comp_cat_cov_func (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_adjunction_func C S t T P)) (@cokernel_adjunction_arrow_func C S t T0 Q)) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)) (@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q) (@eq_refl (@Transf (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q)
        (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)) (@comp_fapp0 (Functor_cat (Functor_oplax_cat WalkingArrow_cat C) C) (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf (Functor_oplax_cat WalkingArrow_cat C) C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q)) (@one_cat_coimage_image_comparison C S C1 t T T0 P Q))) (@one_cat_coimage_target_kernel_factor_path C S C1 t T T0 P Q))));

// The source-to-image map reconstructs the original differential.
symbol one_cat_image_family_source_factor_path [B C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (P : τ (@KernelAdjunctionStructure C S t T)) (Q : τ (@CokernelAdjunctionStructure C S t T0))
  (F : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src)
    (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@comp_fapp0 (Functor_cat B C)
    (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0 B (Functor_oplax_cat
    WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat
    C F walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf B C S t T P (@comp_cat_fapp0 B
    (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@cokernel_adjunction_arrow_func C S t T0
    Q) F)) (@one_cat_image_family_source_transf B C S C1 t T T0 P Q F)) (@diagram_oplax_family_transf B
    WalkingArrow_cat C F walking_arrow_src walking_arrow_tgt walking_arrow_generator))
≔ @eq_trans _ _ _ _ (@comp_assoc (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C F
  walking_arrow_src) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0
  P Q) F) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_image_func C S t T T0 P Q) F)
  (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt) (@kernel_adjunction_family_inclusion_transf
  B C S t T P (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
  (@cokernel_adjunction_arrow_func C S t T0 Q) F)) (@fapp0 _ _ (@comp_cat_con_fapp1_func B (Functor_oplax_cat
  WalkingArrow_cat C) C F (@adjunction_coimage_func C S t T T0 P Q) (@adjunction_image_func C S t T T0 P Q))
  (@one_cat_coimage_image_comparison C S C1 t T T0 P Q)) (@cokernel_adjunction_family_projection_transf B C S t
  T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
  (@kernel_adjunction_arrow_func C S t T P) F)))
    (@eq_trans _ _ _ _
      (@eq_ap (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t
        T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)) (@Transf B C
        (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@diagram_oplax_family_at_func B
        WalkingArrow_cat C F walking_arrow_tgt))
        (λ v : τ (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C
          S t T T0 P Q) F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt)), (@comp_fapp0
          (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_src) (@comp_cat_fapp0
          B (Functor_oplax_cat WalkingArrow_cat C) C (@adjunction_coimage_func C S t T T0 P Q) F)
          (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt) v
          (@cokernel_adjunction_family_projection_transf B C S t T0 Q (@comp_cat_fapp0 B (Functor_oplax_cat
          WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@kernel_adjunction_arrow_func C S t T P) F)))) _
          _
        (@one_cat_image_family_comparison_factor_path B C S C1 t T T0 P Q F))
      (@one_cat_coimage_family_factor_path B C S C1 t T T0 P Q F));
