/* Existing native represented-comma/zero-arrow-cone construction.
   Objects and directed Homs are unchanged; the qualified whole observation
   is introduced separately, only for an explicitly one-categorical target. */
require open emdash.emdash3_2_cubical_internalization;
require open emdash.emdash3_2_zero_arrow_diagrams;

// Hom_B(F[-],-), retaining the Cartesian inner family required by
// the corrected two-sided total. No ordinary-family coercion is needed.
symbol represented_comma_prof [A B : Cat] (F : τ (Functor A B))
  : τ (Functor (Op_cat A) (Functor_cart_cat B Cat_cart))
≔ @comp_cat_fapp0 (Op_cat A) (Op_cat B) (Functor_cart_cat B Cat_cart)
    (@hom_int B B (@id_func B)) (@Op_func A B F);

symbol RepresentedComma_cat [A B : Cat] (F : τ (Functor A B)) : Cat
≔ @homdc_total_cat A B (@represented_comma_prof A B F);

symbol represented_comma_obj [A B : Cat] [F : τ (Functor A B)]
  (a : τ (Obj A)) (b : τ (Obj B)) (h : τ (Hom B (@fapp0 A B F a) b))
  : τ (Obj (@RepresentedComma_cat A B F))
≔ @homdc_total_obj A B (@represented_comma_prof A B F) a b h;

symbol represented_comma_source_func [A B : Cat] (F : τ (Functor A B))
  : τ (Functor (@RepresentedComma_cat A B F) A)
≔ @homdc_total_source_func A B (@represented_comma_prof A B F);

symbol represented_comma_target_func [A B : Cat] (F : τ (Functor A B))
  : τ (Functor (@RepresentedComma_cat A B F) B)
≔ @homdc_total_target_func A B (@represented_comma_prof A B F);

// The existing nested-pair map, elaborated before specializing the target
// to an alternating-dual diagram category. This is a definition, with no
// new arrow data, projection rule or equality transport.
symbol represented_comma_map [A B : Cat] [F : τ (Functor A B)]
  [x0 x1 : τ (Obj A)] [y0 y1 : τ (Obj B)]
  [h0 : τ (Hom B (@fapp0 A B F x0) y0)]
  [h1 : τ (Hom B (@fapp0 A B F x1) y1)]
  (a : τ (Hom A x0 x1)) (b : τ (Hom B y0 y1))
  (alpha : τ (Hom (Hom_cat B (@fapp0 A B F x0) y1)
    (@comp_fapp0 B (@fapp0 A B F x0) y0 y1 b h0)
    (@comp_fapp0 B (@fapp0 A B F x0) (@fapp0 A B F x1) y1 h1
      (@fapp1_fapp0 A B F x0 x1 a))))
  : τ (Hom (@RepresentedComma_cat A B F)
      (@represented_comma_obj A B F x0 y0 h0)
      (@represented_comma_obj A B F x1 y1 h1))
≔ Struct_sigma a (Struct_sigma b alpha);

// Two nested Sigma eliminations at the existing represented-map owner.
// The coefficient remains generic while the native Hom's binders are checked.
symbol represented_comma_map_ind [A B : Cat] (F : τ (Functor A B))
  [a0 a1 : τ (Obj A)] [b0 b1 : τ (Obj B)]
  [h0 : τ (Hom B (@fapp0 A B F a0) b0)]
  [h1 : τ (Hom B (@fapp0 A B F a1) b1)]
  (M : τ (Hom (@RepresentedComma_cat A B F)
      (@represented_comma_obj A B F a0 b0 h0)
      (@represented_comma_obj A B F a1 b1 h1)) → Grpd)
  (step : Π p : τ (Hom A a0 a1), Π q : τ (Hom B b0 b1),
    Π alpha : τ (Hom (Hom_cat B (@fapp0 A B F a0) b1)
      (@comp_fapp0 B (@fapp0 A B F a0) b0 b1 q h0)
      (@comp_fapp0 B (@fapp0 A B F a0) (@fapp0 A B F a1) b1 h1
        (@fapp1_fapp0 A B F a0 a1 p))),
    τ (M (@represented_comma_map A B F a0 a1 b0 b1 h0 h1 p q alpha)))
  (m : τ (Hom (@RepresentedComma_cat A B F)
      (@represented_comma_obj A B F a0 b0 h0)
      (@represented_comma_obj A B F a1 b1 h1)))
  : τ (M m)
≔ @sigma_ind _ _ M
    (λ p : τ (Hom A a0 a1), λ rest : τ _,
      @sigma_ind _ _ (λ r : τ _, M (Struct_sigma p r))
        (λ q : τ (Hom B b0 b1), λ alpha : τ _, step p q alpha) rest) m;

// The zero-cone's datum is an actual transformation J(A)⇒d of arrow diagrams.
symbol ZeroArrowCone_cat [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject C t)) : Cat
≔ @RepresentedComma_cat C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T);

symbol zero_arrow_cone_obj [C : Cat] [t : τ (Obj C)] [T : τ (@TerminalObject C t)]
  (A : τ (Obj C)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (h : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
    (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) A) d))
  : τ (Obj (@ZeroArrowCone_cat C t T))
≔ @represented_comma_obj C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T) A d h;

symbol zero_arrow_cone_first_func [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  : τ (Functor (@ZeroArrowCone_cat C t T) C)
≔ @represented_comma_source_func C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T);

symbol zero_arrow_cone_diagram_func [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  : τ (Functor (@ZeroArrowCone_cat C t T) (Functor_oplax_cat WalkingArrow_cat C))
≔ @represented_comma_target_func C (Functor_oplax_cat WalkingArrow_cat C)
    (@terminal_arrow_diagram_func C t T);

// Both other vertices are whole evaluations of the retained diagram.
symbol zero_arrow_cone_vertex_func [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (i : τ (Obj WalkingArrow_cat))
  : τ (Functor (@ZeroArrowCone_cat C t T) C)
≔ @diagram_oplax_family_at_func (@ZeroArrowCone_cat C t T) WalkingArrow_cat C
    (@zero_arrow_cone_diagram_func C t T) i;

// The outgoing differential is a whole transformation over the comma category.
symbol zero_arrow_cone_differential_transf [C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject C t))
  : τ (@Transf (@ZeroArrowCone_cat C t T) C
    (@zero_arrow_cone_vertex_func C t T walking_arrow_src)
    (@zero_arrow_cone_vertex_func C t T walking_arrow_tgt))
≔ @diagram_oplax_family_transf (@ZeroArrowCone_cat C t T) WalkingArrow_cat C
    (@zero_arrow_cone_diagram_func C t T) walking_arrow_src walking_arrow_tgt walking_arrow_generator;
