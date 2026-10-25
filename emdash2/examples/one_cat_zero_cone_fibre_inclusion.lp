require open emdash.emdash3_2_one_cat_zero_cone_fibre_inclusion;
// Elaborate the original two-stage inclusion before specializing the
// diagram coefficient. These are transparent reviewer definitions only.
symbol probe_fibre_inclusion [A B : Cat] (F : τ (Functor A B))
  (a : τ (Obj A)) (b : τ (Obj B))
  : τ (Functor (Hom_cat B (@fapp0 A B F a) b) (@RepresentedComma_cat A B F))
≔ let E : τ (Functor (Op_cat A) (Functor_cart_cat B Cat_cart)) ≔
    @represented_comma_prof A B F in
  let E_a : τ (Catd B) ≔ @fapp0 (Op_cat A) (Functor_cart_cat B Cat_cart) E a in
  let D : τ (Catd (TotalOp_cat A)) ≔ @homdc_op_edge_catd A B E in
  @comp_cat_fapp0 (Fibre_cat E_a b) (@Sigma_cat B E_a) (@homdc_total_cat A B E)
    (@TotalOp_func (Fibre_cat D a) (@Sigma_cat (TotalOp_cat A) D)
      (@sigma_fibre_inclusion_func (TotalOp_cat A) D a))
    (@sigma_fibre_inclusion_func B E_a b);

symbol probe_fibre_middle [A B : Cat] (F : τ (Functor A B))
  (a : τ (Obj A)) (b : τ (Obj B))
  [h k : τ (Hom B (@fapp0 A B F a) b)]
  (alpha : τ (Hom (Hom_cat B (@fapp0 A B F a) b) h k))
  : τ (Hom B b b)
≔ sigma_Fst (sigma_Snd (@fapp1_fapp0 (Hom_cat B (@fapp0 A B F a) b)
    (@RepresentedComma_cat A B F) (@probe_fibre_inclusion A B F a b) h k alpha));

symbol probe_fibre_cell [A B : Cat] (F : τ (Functor A B))
  (a : τ (Obj A)) (b : τ (Obj B))
  [h k : τ (Hom B (@fapp0 A B F a) b)]
  (alpha : τ (Hom (Hom_cat B (@fapp0 A B F a) b) h k))
  : τ (Hom (Hom_cat B (@fapp0 A B F a) b) h k)
≔ sigma_Snd (sigma_Snd (@fapp1_fapp0 (Hom_cat B (@fapp0 A B F a) b)
    (@RepresentedComma_cat A B F) (@probe_fibre_inclusion A B F a b) h k alpha));

symbol C : Cat;
symbol C1 : τ (IsNCat (cat_succ cat_zero) C);
symbol t : τ (Obj C);
symbol T : τ (@TerminalObject C t);
symbol a : τ (Obj C);
symbol d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C));
symbol h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
  (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a) d);
symbol k : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
  (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a) d);
symbol alpha : τ (Hom (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C)
  (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a) d) h k);
symbol inclusion ≔ @zero_arrow_cone_fibre_inclusion_func C C1 t T a d;
symbol mapped ≔ @fapp1_fapp0 _ _ inclusion h k alpha;

// The generic observations specialize to the actual whole public inclusion.
assert ⊢ inclusion ≡ @probe_fibre_inclusion C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a d;

// Both bases remain fixed and the existing fibre cell is retained.
assert ⊢ sigma_Fst mapped ≡ @id C a;
assert ⊢ @probe_fibre_middle C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a d h k alpha ≡ @id (Functor_oplax_cat WalkingArrow_cat C) d;
assert ⊢ @probe_fibre_cell C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a d h k alpha ≡ alpha;

// The full Hom functor remains available for the next cell.
assert ⊢ @fapp1_func _ _ inclusion h k : τ (Functor
  (Hom_cat (@Hom_cat (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a) d) h k)
  (Hom_cat (@ZeroArrowCone_cat C t T)
    (@zero_arrow_cone_obj C t T a d h) (@zero_arrow_cone_obj C t T a d k)));

// Point inclusion retains the original transformation.
assert [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  (a : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a) d)) ⊢
  @fapp0 _ _ (@zero_arrow_cone_fibre_inclusion_func C C1 t T a d) h
  ≡ @zero_arrow_cone_obj C t T a d h;
