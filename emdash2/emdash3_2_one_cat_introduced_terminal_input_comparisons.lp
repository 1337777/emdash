/* Retain both original diagram presentations in the native input comparison. */
require open emdash.emdash3_2_one_cat_zero_cone_fibre_inclusion;
require open emdash.emdash3_2_one_cat_diagram_map_paths;
require open emdash.emdash3_2_zero_arrow_diagram_observations;
require open emdash.emdash3_2_one_cat_zero_arrow_inputs;
require open emdash.emdash3_2_one_cat_diagram_map_equivalences;
require open emdash.emdash3_2_one_cat_zero_cone_map_equivalences;

require open emdash.emdash3_2_one_cat_diagram_family_reflection;

    // Retain the original ordinary shape map before its actual coefficient image.
    protected symbol introduced_input_diagram_original_map [K C : Cat]
            (C1 : τ (IsNCat (cat_succ cat_zero) C))
            [F G : τ (Functor K C)] (u : τ (@Transf K C F G)) (x : τ (Obj K))
            : τ (@Transf WalkingArrow_cat C (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)) (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)))
    ≔ @one_cat_original_diagram_map C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)) (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u))
                    (@id C (@fapp0 K C F x)) (@id C (@fapp0 K C G x))
                    (@path_to_hom (Hom_cat C (@fapp0 K C F x) (@fapp0 K C G x))
                            (@fapp1_fapp0 WalkingArrow_cat C (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x))
                                    walking_arrow_src walking_arrow_tgt walking_arrow_generator)
                            (@tapp0_fapp0 K C F G x u) (@eq_refl (Hom C (@fapp0 K C F x) (@fapp0 K C G x)) (@tapp0_fapp0 K C F G x u)));

    // Whole inclusion through the existing OneCat mapping comparison.
    protected symbol introduced_input_diagram_coefficient_func [C : Cat]
            (C1 : τ (IsNCat (cat_succ cat_zero) C))
            : τ (Functor (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C))
    ≔ @one_cat_diagram_oplax_include_func C C1;

    // Existing Cartesian exchange, after the actual OneCat admission of evaluation.
protected symbol introduced_input_cart_family_func [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor K (Functor_oplax_cat I C)))
  : τ (Functor K (Functor_cart_cat I C))
≔ @one_cat_oplax_family_cart_func K I C C1 D;

// This is the existing native exchange comparison, used before specialization.
protected symbol introduced_input_cart_family_roundtrip [K I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor K (Functor_oplax_cat I C)))
  : τ (@= (Functor K (Functor_oplax_cat I C))
      (@comp_cat_fapp0 K (Functor_cart_cat I C) (Functor_oplax_cat I C)
        (Functor_cart_oplax_include I C) (@introduced_input_cart_family_func K I C C1 D)) D)
≔ @one_cat_oplax_family_roundtrip K I C C1 D;


// Reflection through the existing Cartesian and ordinary whole comparisons.
protected symbol introduced_input_oplax_map_path [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [d e : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))]
  (h k : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) d e))
  (p : τ (@= (Hom C
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) e))
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d e h)
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d e k)))
  (q : τ (@= (Hom C
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
    (@fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) e))
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e h)
    (@fapp1_fapp0 _ C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e k)))
  : τ (@= (Hom (Functor_oplax_cat WalkingArrow_cat C) d e) h k)
≔ @one_cat_oplax_diagram_map_path C C1 d e h k p q;

// Reconstruct the evaluated diagram as its introduced generator, retaining actual endpoints.
symbol introduced_input_diagram_map [K C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (F G : τ (Functor K C)) (u : τ (@Transf K C F G)) (x : τ (Obj K))
  (A : τ (Obj C))
  (b : τ (Hom C A (@fapp0 K C F x)))
  (zero : τ (@= (Hom C A (@fapp0 K C G x)) (@comp_fapp0 C A (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C
  F G x u) b) (@preadditive_hom_zero C S A (@fapp0 K C G x))))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C
  t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)))
  (incoming : τ (@= (Hom C A (@fapp0 K C F x)) (@terminal_arrow_test_incoming C t T A (@fapp0 K
  (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) b))
 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K
  C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u))))
≔ @fapp1_fapp0 (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@introduced_input_diagram_coefficient_func C C1) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)) (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)) (@introduced_input_diagram_original_map K C C1 F G u x);

symbol introduced_input_diagram_equiv [K C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (F G : τ (Functor K C)) (u : τ (@Transf K C F G)) (x : τ (Obj K))
  (A : τ (Obj C))
  (b : τ (Hom C A (@fapp0 K C F x)))
  (zero : τ (@= (Hom C A (@fapp0 K C G x)) (@comp_fapp0 C A (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C
  F G x u) b) (@preadditive_hom_zero C S A (@fapp0 K C G x))))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C
  t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)))
  (incoming : τ (@= (Hom C A (@fapp0 K C F x)) (@terminal_arrow_test_incoming C t T A (@fapp0 K
  (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) b))
 : τ (@OmegaEquivAlong (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u))) (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming))
≔ @one_cat_omega_equiv_fmap (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
                    (@one_cat_oplax_functor_category WalkingArrow_cat C C1) (@introduced_input_diagram_coefficient_func C C1)
                    (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)) (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)) (@introduced_input_diagram_original_map K C C1 F G u x)
                    (@one_cat_diagram_map_equiv C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)) (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)) (@introduced_input_diagram_original_map K C C1 F G u x)
                            (@omega_equiv_along_refl C (@fapp0 K C F x)) (@omega_equiv_along_refl C (@fapp0 K C G x)));

// Original incoming recovery and ordinary terminal uniqueness determine compatibility.
symbol introduced_input_diagram_compatibility [K C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (F G : τ (Functor K C)) (u : τ (@Transf K C F G)) (x : τ (Obj K))
  (A : τ (Obj C))
  (b : τ (Hom C A (@fapp0 K C F x)))
  (zero : τ (@= (Hom C A (@fapp0 K C G x)) (@comp_fapp0 C A (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C
  F G x u) b) (@preadditive_hom_zero C S A (@fapp0 K C G x))))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C
  t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)))
  (incoming : τ (@= (Hom C A (@fapp0 K C F x)) (@terminal_arrow_test_incoming C t T A (@fapp0 K
  (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) b))
 : τ (@= (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u)))) (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat
  WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u))) (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming) h)
  (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G
  x u) zero))
≔ @introduced_input_oplax_map_path C C1 (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func
  C t T) A) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)))
  (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u))) (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming) h)
  (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G
  x u) zero) incoming
 (@eq_trans _ _ _ _
  (@preadditive_terminal_to_zero_path C S t (@fapp0 K C G x) T (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 C
  (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0
  K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u))) (@comp_fapp0 (Functor_oplax_cat
  WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A)
  (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)
  (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u)))
  (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming) h)))
  (@eq_sym _ _ _ (@preadditive_terminal_to_zero_path C S t (@fapp0 K C G x) T (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u))) (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G
  x u) zero)))));

symbol one_cat_introduced_terminal_input_comparison_map [K C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (F G : τ (Functor K C)) (u : τ (@Transf K C F G)) (x : τ (Obj K))
  (A : τ (Obj C))
  (b : τ (Hom C A (@fapp0 K C F x)))
  (zero : τ (@= (Hom C A (@fapp0 K C G x)) (@comp_fapp0 C A (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C
  F G x u) b) (@preadditive_hom_zero C S A (@fapp0 K C G x))))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C
  t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)))
  (incoming : τ (@= (Hom C A (@fapp0 K C F x)) (@terminal_arrow_test_incoming C t T A (@fapp0 K (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) b))
  : τ (Hom (@ZeroArrowCone_cat C t T) (@zero_arrow_cone_obj C t T A (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) h) (@zero_composite_native_cone C S C1 t T A (@fapp0 K C F x)
  (@fapp0 K C G x) b (@tapp0_fapp0 K C F G x u) zero))
≔ @zero_cone_native_map C t T A A (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K
  C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C F G x u))) h
  (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G
  x u) zero) (@id C A) (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming)
  (@path_to_hom (Hom_cat (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u)))) (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat
  WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u))) (@introduced_input_diagram_map K C S C1 t T F G u x A b zero h incoming) h)
  (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G
  x u) zero) (@introduced_input_diagram_compatibility K C S C1 t T F G u x A b zero h incoming));

symbol one_cat_introduced_terminal_input_comparison_equiv [K C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (F G : τ (Functor K C)) (u : τ (@Transf K C F G)) (x : τ (Obj K))
  (A : τ (Obj C))
  (b : τ (Hom C A (@fapp0 K C F x)))
  (zero : τ (@= (Hom C A (@fapp0 K C G x)) (@comp_fapp0 C A (@fapp0 K C F x) (@fapp0 K C G x) (@tapp0_fapp0 K C
  F G x u) b) (@preadditive_hom_zero C S A (@fapp0 K C G x))))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C
  t T) A) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x)))
  (incoming : τ (@= (Hom C A (@fapp0 K C F x)) (@terminal_arrow_test_incoming C t T A (@fapp0 K (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) b))
  : τ (@OmegaEquivAlong (@ZeroArrowCone_cat C t T) (@zero_arrow_cone_obj C t T A (@fapp0 K (Functor_oplax_cat
  WalkingArrow_cat C) (@transf_arrow_diagram_func K C F G u) x) h) (@zero_composite_native_cone C S C1 t T A
  (@fapp0 K C F x) (@fapp0 K C G x) b (@tapp0_fapp0 K C F G x u) zero)
  (@one_cat_introduced_terminal_input_comparison_map K C S C1 t T F G u x A b zero h incoming))
≔ @one_cat_zero_cone_map_equiv C C1 t T A A (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@transf_arrow_diagram_func K C F G u) x) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
  (@tapp0_fapp0 K C F G x u))) h (@terminal_zero_composite_transf C S C1 t T A (@fapp0 K C F x) (@fapp0 K C
  G x) b (@tapp0_fapp0 K C F G x u) zero) (@one_cat_introduced_terminal_input_comparison_map K C S C1 t T
  F G u x A b zero h incoming) (@omega_equiv_along_refl C A) (@introduced_input_diagram_equiv K C S C1 t T
  F G u x A b zero h incoming);
