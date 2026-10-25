/* Original raw fields are observations of the same nonidentity native map. */
require open emdash.emdash3_2_zero_arrow_cone_chain_pairs;
require open emdash.emdash3_2_zero_arrow_cone_maps;
// Type the existing represented-map introduction before specializing its coefficient.
// This transparent reviewer definition retains the original Homdc-frame input.
symbol reviewer_represented_homdc_map [A B : Cat] (F : τ (Functor A B))
  [a0 a1 : τ (Obj A)] [b0 b1 : τ (Obj B)]
  [h0 : τ (Hom B (@fapp0 A B F a0) b0)]
  [h1 : τ (Hom B (@fapp0 A B F a1) b1)]
  (p : τ (Hom A a0 a1)) (q : τ (Hom B b0 b1))
  (theta : τ (Obj (@homdc_fibre A B
    (@comp_cat_fapp0 (Op_cat A) (Functor_cart_cat B Cat_cart) (Catd_cat B)
      (Functor_cart_include B Cat_cart) (@represented_comma_prof A B F))
    a0 a1 b0 b1 h0 h1 p q)))
  : τ (Hom (@RepresentedComma_cat A B F)
      (@represented_comma_obj A B F a0 b0 h0)
      (@represented_comma_obj A B F a1 b1 h1))
≔ @represented_comma_map A B F a0 a1 b0 b1 h0 h1 p q theta;


assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A0 A1 : τ (Obj C))
  (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0) d0))
  (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A1) d1))
  (a : τ (Hom C A0 A1)) (b : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (theta : τ (Obj (@homdc_fibre C (Functor_oplax_cat WalkingArrow_cat C)
    (@comp_cat_fapp0 (Op_cat C) (Functor_cart_cat (Functor_oplax_cat WalkingArrow_cat C) Cat_cart)
      (Catd_cat (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cart_include (Functor_oplax_cat WalkingArrow_cat C) Cat_cart) (@represented_comma_prof C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)))
    A0 A1 d0 d1 h0 h1 a b))) ⊢
  @computational_chain_pair_map_next C S A0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0)
      A1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
    (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0)) (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A1 d1 h1)) (@zero_arrow_cone_chain_pair_map C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0) (@zero_arrow_cone_obj C t T A1 d1 h1) (@reviewer_represented_homdc_map C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0 A1 d0 d1 h0 h1 a b theta))
  ≡ a;

assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A0 A1 : τ (Obj C))
  (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0) d0))
  (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A1) d1))
  (a : τ (Hom C A0 A1)) (b : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (theta : τ (Obj (@homdc_fibre C (Functor_oplax_cat WalkingArrow_cat C)
    (@comp_cat_fapp0 (Op_cat C) (Functor_cart_cat (Functor_oplax_cat WalkingArrow_cat C) Cat_cart)
      (Catd_cat (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cart_include (Functor_oplax_cat WalkingArrow_cat C) Cat_cart) (@represented_comma_prof C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)))
    A0 A1 d0 d1 h0 h1 a b))) ⊢
  @computational_chain_pair_map_middle C S A0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0)
      A1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
    (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0)) (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A1 d1 h1)) (@zero_arrow_cone_chain_pair_map C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0) (@zero_arrow_cone_obj C t T A1 d1 h1) (@reviewer_represented_homdc_map C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0 A1 d0 d1 h0 h1 a b theta))
  ≡ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0 d1 b;

assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A0 A1 : τ (Obj C))
  (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h0 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0) d0))
  (h1 : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A1) d1))
  (a : τ (Hom C A0 A1)) (b : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (theta : τ (Obj (@homdc_fibre C (Functor_oplax_cat WalkingArrow_cat C)
    (@comp_cat_fapp0 (Op_cat C) (Functor_cart_cat (Functor_oplax_cat WalkingArrow_cat C) Cat_cart)
      (Catd_cat (Functor_oplax_cat WalkingArrow_cat C)) (Functor_cart_include (Functor_oplax_cat WalkingArrow_cat C) Cat_cart) (@represented_comma_prof C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T)))
    A0 A1 d0 d1 h0 h1 a b))) ⊢
  @computational_chain_pair_map_prev C S A0 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0)
      A1 (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
    (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0)) (@zero_arrow_cone_chain_pair C C1 t T S (@zero_arrow_cone_obj C t T A1 d1 h1)) (@zero_arrow_cone_chain_pair_map C C1 t T S (@zero_arrow_cone_obj C t T A0 d0 h0) (@zero_arrow_cone_obj C t T A1 d1 h1) (@reviewer_represented_homdc_map C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A0 A1 d0 d1 h0 h1 a b theta))
  ≡ @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 b;

// Object-set truncation alone is not the required local-Hom profile.
assertnot (C : Cat) (objects_set : τ (IsSetGrpd (Obj C))) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) ⊢
  @zero_arrow_cone_universal_transf C objects_set t T
  : τ (@Transf (@ZeroArrowCone_cat C t T) (Functor_oplax_cat WalkingArrow_cat C)
      (@comp_cat_fapp0 (@ZeroArrowCone_cat C t T) C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) (@zero_arrow_cone_first_func C t T))
      (@zero_arrow_cone_diagram_func C t T));
