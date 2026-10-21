require open emdash.emdash3_2_zero_arrow_diagram_observations;
require open emdash.emdash3_2_one_cat_diagram_family_reflection;
/* Ordinary zero tests at the original arbitrary walking-arrow diagram.
   Compose the canonical raw input with the actual reconstruction comparison.
   No kernel/cokernel is selected, and the supplied diagram is not replaced
   by an equality cast or by a newly selected presentation. */
require open emdash.emdash3_2_one_cat_diagram_reconstruction;
require open emdash.emdash3_2_one_cat_zero_arrow_inputs;

// The actual original d is the target; no diagram object is replaced.
symbol terminal_diagram_test_transf [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (b : τ (Hom C X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)))
  (zero : τ (@= (Hom C X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)) (@comp_fapp0 C X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d) b)
    (@preadditive_hom_zero C S X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d))))
  : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X) d)
≔ @comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d))) d
    (@fapp1_fapp0 (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_diagram_oplax_include_func C C1) (@walking_arrow_func C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d)) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d) (@one_cat_diagram_reconstruction_to C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d)))
    (@terminal_zero_composite_transf C S C1 t T X (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) b (@terminal_arrow_test_outgoing C d) zero);

// Dually keep d as the actual source and compose its reconstruction inverse.
symbol initial_diagram_test_transf [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  (X : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (b : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) X))
  (zero : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) X) (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) X b (@terminal_arrow_test_outgoing C d))
    (@preadditive_hom_zero C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) X)))
  : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X))
≔ @comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) d (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d))) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X)
    (@initial_zero_composite_transf C S C1 t T (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) X (@terminal_arrow_test_outgoing C d) b zero)
    (@fapp1_fapp0 (Functor_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_diagram_oplax_include_func C C1) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d) (@walking_arrow_func C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d) (@terminal_arrow_test_outgoing C d)) (@one_cat_diagram_reconstruction_from C C1 (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d)));
