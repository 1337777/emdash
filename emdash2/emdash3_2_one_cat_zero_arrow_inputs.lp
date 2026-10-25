/* Realization-facing input adapters for ordinary zero-composite data.
   The existing whole arrow-diagram functor acts on a native homdc square;
   path_to_hom supplies the filler from the given equation. These definitions
   reuse the existing Cartesian square action and its oplax inclusion
   before any universal operation. The actual terminal/initial diagram
   object is decoded for that action; no equality transport is supplied.
   OneCat is explicit; no arbitrary diagram eta or selected K/Q is assumed. */
require open emdash.emdash3_2_one_cat_arrow_diagrams;
require open emdash.emdash3_2_zero_arrow_cones;
require open emdash.emdash3_2_additive_categories;

// (b,d,d∘b=0) supplies J(X)⇒Arr(d) through native square action.
symbol terminal_zero_composite_transf
  [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B)))
  : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
      (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
      (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d)))
≔ @fapp1_fapp0 (Functor_cart_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
    (Functor_cart_oplax_include WalkingArrow_cat C) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)) (@walking_arrow_func C A B d)
    (@fapp1_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
      (@one_cat_arrow_cart_diagram_func C C1) (@lax_edge C X t (@terminal_arrow_fapp0 C t T X)) (@lax_edge C A B d)
      (@lax_square C X A t B (@terminal_arrow_fapp0 C t T X) d b (@preadditive_hom_zero C S t B) (@path_to_hom (Hom_cat C X B) _ _
      (@eq_trans (Hom C X B) _ _ _
        (@preadditive_comp_zero_left_path C S X t B (@terminal_arrow_fapp0 C t T X))
        (@eq_sym (Hom C X B) _ _ zero)))));

// The dual input: (d,b,b∘d=0) supplies Arr(d)⇒I(X).
symbol initial_zero_composite_transf
  [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  [A B X : τ (Obj C)] (d : τ (Hom C A B)) (b : τ (Hom C B X))
  (zero : τ (@= (Hom C A X) (@comp_fapp0 C A B X b d)
    (@preadditive_hom_zero C S A X)))
  : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d))
      (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X))
≔ @fapp1_fapp0 (Functor_cart_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
    (Functor_cart_oplax_include WalkingArrow_cat C) (@walking_arrow_func C A B d) (@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) X))
    (@fapp1_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
      (@one_cat_arrow_cart_diagram_func C C1) (@lax_edge C A B d) (@lax_edge C t X (@initial_arrow_fapp0 C t T X))
      (@lax_square C A t B X d (@initial_arrow_fapp0 C t T X) (@preadditive_hom_zero C S A t) b (@path_to_hom (Hom_cat C A X) _ _
      (@eq_trans (Hom C A X) _ _ _ zero
        (@eq_sym (Hom C A X) _ _
          (@preadditive_comp_zero_right_path C S A t X (@initial_arrow_fapp0 C t T X)))))));

// Form the existing native H input, without selecting a kernel first.
symbol zero_composite_native_cone
  [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B)))
  : τ (Obj (@ZeroArrowCone_cat C t T))
≔ @zero_arrow_cone_obj C t T X (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d))
    (@terminal_zero_composite_transf C S C1 t T X A B b d zero);
