/* Original selected lifts, with the formal inclusion's existing properties. */
require open emdash.emdash3_2_kernel_adjunction_unmate_paths;
require open emdash.emdash3_2_abelian_categories;


// Compare the complete source-and-embedding input before transporting monicity.
symbol kernel_presentation_inclusion_data_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (`Σ_ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@Struct_sigma (Obj C) (λ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_presentation_func C S t T W P) d) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C _ _ d (@kernel_presentation_inclusion C S t T W P))) (@Struct_sigma (Obj C) (λ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@kernel_presentation_selected_object C S W d) (@computational_kernel_morphism C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d) (@kernel_presentation_selected C S W d))))
≔ @eq_refl (`Σ_ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@Struct_sigma (Obj C) (λ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_presentation_func C S t T W P) d) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C _ _ d (@kernel_presentation_inclusion C S t T W P)));

symbol kernel_presentation_inclusion_monic [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@IsMonic C (@fapp0 _ _ (@kernel_presentation_func C S t T W P) d)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
      (@tapp0_fapp0 _ _ _ _ d (@kernel_presentation_inclusion C S t T W P)))
≔ @ind_eq (`Σ_ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@Struct_sigma (Obj C) (λ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@kernel_presentation_func C S t T W P) d) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C _ _ d (@kernel_presentation_inclusion C S t T W P))) (@Struct_sigma (Obj C) (λ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)) (@kernel_presentation_selected_object C S W d) (@computational_kernel_morphism C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d) (@kernel_presentation_selected C S W d)))
    (@kernel_presentation_inclusion_data_path C S t T W P d)
    (λ z : τ (`Σ_ M : τ (Obj C), Hom C M (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)), @IsMonic C (sigma_Fst z) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (sigma_Snd z))
    (@computational_kernel_morphism_is_monic C S
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@terminal_arrow_test_outgoing C d) (@kernel_presentation_selected C S W d));

symbol kernel_presentation_test_lift_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject C t)] [W : τ (@HasComputationalKernels C S)]
  (P : τ (@KernelPresentation C S t T W)) (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (e : τ (@WeakKernelAnnihilator C S
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
    (@terminal_arrow_test_outgoing C d) X))
  : τ (@= (Hom C X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d))
      (@comp_fapp0 C X (@fapp0 _ _ (@kernel_presentation_func C S t T W P) d) _
        (@tapp0_fapp0 _ _ _ _ d (@kernel_presentation_inclusion C S t T W P))
        (@kernel_presentation_test_lift C S W X d e))
      (@weak_kernel_annihilator_arrow C S
        (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
        (@terminal_arrow_test_outgoing C d) X e))
≔ @eq_trans _ _ _ _
    (@eq_sym _ _ _ (@kernel_presentation_unlift_source_semantic_path C S t T W P X d
      (@kernel_presentation_test_lift C S W X d e)))
    (@kernel_presentation_unlift_lift_source_path C S t T W P X d e);
