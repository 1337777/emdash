/*
  Reviewer example: a classified lax transfor between strict endpoint
  diagrams has one selected strict graph package.
*/

require open emdash.emdash3_2_gray_transformation_graph_profile;

// Default functors expose the original whole graph and its action directly.
assert [B C : Cat]
  (SF SG : τ (@Functor B C))
  (L : τ (@LaxTransfor
    B C
    (SF)
    (SG)))
  [x y : τ (Obj B)]
  (g : τ (Hom B x y)) ⊢
  @fapp1_fapp0
    B (@LaxArrow_cat C)
    ((@gray_transf_graph_func B C SF SG L))
    x y g
  ≡ @gray_transf_graph_arrow
      B C
      (SF)
      (SG)
      L x y g;

assert [B C : Cat]
  (SF SG : τ (@Functor B C))
  (L : τ (@LaxTransfor
    B C
    (SF)
    (SG))) ⊢
  @eq_refl
    (Functor B (@LaxArrow_cat C))
    ((@gray_transf_graph_func B C SF SG L))
  : τ (@=
      (Functor B (@LaxArrow_cat C))
      ((@gray_transf_graph_func B C SF SG L))
      (@gray_transf_graph_func
        B C
        (SF)
        (SG)
        L));

assert [B C : Cat]
  (SF SG : τ (@Functor B C))
  (L : τ (@LaxTransfor
    B C
    (SF)
    (SG)))
  (x : τ (Obj B)) ⊢
  @fapp0
    B (@LaxArrow_cat C)
    ((@gray_transf_graph_func B C SF SG L))
    x
  ≡ @gray_transf_graph_obj
      B C
      (SF)
      (SG)
      L x;

assert [B C : Cat]
  (SF SG : τ (@Functor B C))
  (L : τ (@LaxTransfor
    B C
    (SF)
    (SG)))
  [x y : τ (Obj B)]
  (g : τ (Hom B x y)) ⊢
  @fapp1_fapp0
    B (@LaxArrow_cat C)
    ((@gray_transf_graph_func B C SF SG L))
    x y g
  ≡ @gray_transf_graph_arrow
      B C
      (SF)
      (SG)
      L x y g;

// Canonical strictness is derived for the actual default graph functor.
assert [B C : Cat]
  (SF SG : τ (@Functor B C))
  (L : τ (@LaxTransfor
    B C
    (SF)
    (SG))) ⊢
  @functor_is_strict
    B (@LaxArrow_cat C)
    (@gray_transf_graph_func B C SF SG L)
  : τ (@IsStrictFunctor
      B (@LaxArrow_cat C)
      ((@gray_transf_graph_func B C SF SG L)));
