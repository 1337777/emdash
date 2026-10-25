/* Native point-diagram maps retain both endpoint identities and the selected inverse. */

require open emdash.emdash3_2_zero_arrow_family_point_diagrams;

assert [K C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A : τ (Functor K C))
  (D : τ (Functor K (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Transf K (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 K C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) D)) (x : τ (Obj K))
    ⊢ (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 K (Functor_oplax_cat
  WalkingArrow_cat C)
  (@zero_arrow_family_incoming_func K C t T A D h) x) (@fapp0 (@ZeroArrowCone_cat C t T) (Functor_oplax_cat
  WalkingArrow_cat C) (@zero_arrow_family_incoming_func (@ZeroArrowCone_cat C t T) C t T
  (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T) (@zero_arrow_cone_universal_transf C
  C1 t T)) (@zero_arrow_family_point_input K C t T A D h x)) (@zero_arrow_family_point_diagram_map K C
  C1 t T A D h x)) ≡ (@id C (@fapp0 K C A x));

assert [K C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (A : τ (Functor K C))
  (D : τ (Functor K (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Transf K (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 K C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) D)) (x : τ (Obj K))
    ⊢ (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@zero_arrow_family_incoming_func K C t T A D h) x) (@fapp0 (@ZeroArrowCone_cat C t T) (Functor_oplax_cat
  WalkingArrow_cat C) (@zero_arrow_family_incoming_func (@ZeroArrowCone_cat C t T) C t T
  (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T) (@zero_arrow_cone_universal_transf C
  C1 t T)) (@zero_arrow_family_point_input K C t T A D h x)) (@zero_arrow_family_point_diagram_map K C
  C1 t T A D h x)) ≡ (@id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) D x)));

assert [K C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj
  C)]
  (T : τ (@TerminalObject C t)) (A : τ (Functor K C))
  (D : τ (Functor K (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Transf K (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 K C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) D)) (x : τ (Obj K))
    ⊢ (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0
  (@ZeroArrowCone_cat C t T) (Functor_oplax_cat
  WalkingArrow_cat C) (@zero_arrow_family_incoming_func (@ZeroArrowCone_cat C t T) C t T
  (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T) (@zero_arrow_cone_universal_transf C
  C1 t T)) (@zero_arrow_family_point_input K C t T A D h x)) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@zero_arrow_family_incoming_func K C t T A D h) x) (@zero_arrow_family_point_diagram_inverse K C C1
  t T A D h x)) ≡ (@id C (@fapp0 K C A x));

assert [K C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj
  C)]
  (T : τ (@TerminalObject C t)) (A : τ (Functor K C))
  (D : τ (Functor K (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Transf K (Functor_oplax_cat WalkingArrow_cat C) (@comp_cat_fapp0 K C (Functor_oplax_cat WalkingArrow_cat C)
  (@terminal_arrow_diagram_func C t T) A) D)) (x : τ (Obj K))
    ⊢ (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@fapp0 (@ZeroArrowCone_cat C t T) (Functor_oplax_cat
  WalkingArrow_cat C) (@zero_arrow_family_incoming_func (@ZeroArrowCone_cat C t T) C t T
  (@zero_arrow_cone_first_func C t T) (@zero_arrow_cone_diagram_func C t T) (@zero_arrow_cone_universal_transf C
  C1 t T)) (@zero_arrow_family_point_input K C t T A D h x)) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
  (@zero_arrow_family_incoming_func K C t T A D h) x) (@zero_arrow_family_point_diagram_inverse K C C1
  t T A D h x)) ≡ (@id C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C) D x)));
