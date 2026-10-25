/* Ordinary observations of actual terminal/initial arrow-diagram maps.
   These projections and zero equations do not require selected universals.
   Ordinary naturality is derived from the existing cells using C1.
   Raw projections keep unrestricted C; diagrams use the existing oplax coefficient. */
require open emdash.emdash3_2_zero_arrow_diagrams;
require open emdash.emdash3_2_additive_categories;
require open emdash.emdash3_2_one_cat_action_paths;

symbol terminal_arrow_test_incoming [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d))
  : τ (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d))
≔ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d h;

symbol terminal_arrow_test_tip [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d))
  : τ (Hom C t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
≔ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d h;

symbol terminal_arrow_test_outgoing [C : Cat] (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
≔ @tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator);

// The existing two naturality cells give an ordinary comparison of the cuts.
symbol terminal_arrow_test_naturality_path [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d))
  : τ (@= (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
      (@comp_fapp0 C _ _ _ (@terminal_arrow_test_outgoing C d) (@terminal_arrow_test_incoming C t T A d h))
      (@comp_fapp0 C A t _ (@terminal_arrow_test_tip C t T A d h) (@terminal_arrow_fapp0 C t T A)))
≔ @eq_sym _ _ _
    (@one_cat_component_naturality_path (Functor_oplax_cat WalkingArrow_cat C) C C1
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d h);

// Initiality of a terminal object in a preadditive category supplies the
// zero comparison; no separately selected whole initial structure is assumed.
symbol terminal_arrow_test_chain_path [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d))
  : τ (@= (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
      (@comp_fapp0 C _ _ _ (@terminal_arrow_test_outgoing C d) (@terminal_arrow_test_incoming C t T A d h))
      (@preadditive_hom_zero C S A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)))
≔ @eq_trans (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)) _ _ _
    (@terminal_arrow_test_naturality_path C C1 t T A d h)
    (@eq_trans (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)) _ _ _
      (@eq_ap (Hom C t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
        (Hom C A (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))
        (λ q : τ (Hom C t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)),
          @comp_fapp0 C A t _ q (@terminal_arrow_fapp0 C t T A)) _ _
        (@preadditive_terminal_to_zero_path C S t
          (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) T (@terminal_arrow_test_tip C t T A d h)))
      (@preadditive_comp_zero_left_path C S A t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
        (@terminal_arrow_fapp0 C t T A)));

// Initiality controls the endomorphisms of t, without needing a new
// opposite preadditive structure or any reverse to an arbitrary arrow.
// Native carrier annotation avoids premature injective-Hom decomposition
// of Hom(TotalOp(C),t,t) versus Hom(C,t,t); their endomorphism carriers coincide.
symbol preadditive_initial_identity_zero_path [C : Cat] (S : τ (@PreadditiveCategory C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  : τ (@= (Obj (Hom_cat C t t)) (@id C t) (@preadditive_hom_zero C S t t))
≔ @eq_trans (Obj (Hom_cat C t t)) (@id C t)
    (@is_contr_center (Obj (Hom_cat C t t)) (@terminal_hom_contr (TotalOp_cat C) t T t))
    (@preadditive_hom_zero C S t t)
    (@eq_sym (Obj (Hom_cat C t t)) _ _
      (@is_contr_path (Obj (Hom_cat C t t)) (@terminal_hom_contr (TotalOp_cat C) t T t) (@id C t)))
    (@is_contr_path (Obj (Hom_cat C t t)) (@terminal_hom_contr (TotalOp_cat C) t T t)
      (@preadditive_hom_zero C S t t));

symbol preadditive_initial_incoming_zero_path [C : Cat] (S : τ (@PreadditiveCategory C))
  [t A : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t)) (f : τ (Hom C A t))
  : τ (@= (Hom C A t) f (@preadditive_hom_zero C S A t))
≔ @eq_trans (Hom C A t) f (@comp_fapp0 C A t t (@id C t) f)
    (@preadditive_hom_zero C S A t) (eq_refl f)
    (@eq_trans (Hom C A t) _ _ _
      (@eq_ap (Hom C t t) (Hom C A t) (λ e : τ (Hom C t t), @comp_fapp0 C A t t e f)
        (@id C t) (@preadditive_hom_zero C S t t)
        (@preadditive_initial_identity_zero_path C S t T))
      (@preadditive_comp_zero_left_path C S A t t f));

symbol initial_arrow_test_outgoing [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A)))
  : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) A)
≔ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A) h;

symbol initial_arrow_test_tip [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A)))
  : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) t)
≔ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A) h;

symbol initial_arrow_test_chain_path [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t)) (A : τ (Obj C))
  (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A)))
  : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) A)
      (@comp_fapp0 C _ _ _ (@initial_arrow_test_outgoing C t T A d h) (@terminal_arrow_test_outgoing C d))
      (@preadditive_hom_zero C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) A))
≔ @eq_trans (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) A) _ _ _
    (@one_cat_component_naturality_path (Functor_oplax_cat WalkingArrow_cat C) C C1
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator) d (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) A) h)
    (@eq_trans (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) A) _ _ _
      (@eq_ap (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) t)
        (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) A)
        (λ q : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) t),
          @comp_fapp0 C _ t A (@initial_arrow_fapp0 C t T A) q) _ _
        (@preadditive_initial_incoming_zero_path C S t (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
          T (@initial_arrow_test_tip C t T A d h)))
      (@preadditive_comp_zero_right_path C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) t A
        (@initial_arrow_fapp0 C t T A)));
