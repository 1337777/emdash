/* Whole diagram transposition in an ordinary target.
   First exchange h:F⇒G, then introduce its arrow family in Functor_cat(B,C)
   and exchange the remaining walking-arrow and B arguments. This keeps
   every column and shape-arrow action in one internal functor term.
   C1 states the ordinary scope; no general lax/oplax interchange theorem
   or manually supplied naturality square is introduced. */
require open emdash.emdash3_2_one_cat_diagram_family_reflection;

// i ↦ the whole B-family of arrows h(b)[i]:F(b)[i]→G(b)[i].
symbol one_cat_diagram_transpose_family_func
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G))
  : τ (Functor I (Functor_cat B (Functor_cat WalkingArrow_cat C)))
≔ @comp_cat_fapp0 I
    (Functor_cat WalkingArrow_cat (Functor_cat B C))
    (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_family_exchange_func WalkingArrow_cat B C C1)
    (@one_cat_transf_arrow_diagram_func I (Functor_cat B C) (@one_cat_functor_category B C C1)
      (@one_cat_family_exchange B I C C1 F) (@one_cat_family_exchange B I C C1 G)
      (@one_cat_family_exchange_map B I C C1 F G h));

// The column at i is an observation of the original whole family.
symbol one_cat_diagram_transpose_column_func
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G)) (i : τ (Obj I))
  : τ (Functor B (Functor_cat WalkingArrow_cat C))
≔ @fapp0 I (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_diagram_transpose_family_func B I C C1 F G h) i;

// Shape-arrow action is the same whole family Hom action; no equality transport.
symbol one_cat_diagram_transpose_transf
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_cat I C))]
  (h : τ (@Transf B (Functor_cat I C) F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf B (Functor_cat WalkingArrow_cat C)
      (@one_cat_diagram_transpose_column_func B I C C1 F G h i)
      (@one_cat_diagram_transpose_column_func B I C C1 F G h j))
≔ @fapp1_fapp0 I (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_diagram_transpose_family_func B I C C1 F G h) i j u;

// Native-input counterpart of ordinary diagram transposition. OneCat(C)
// is the existing semantic guard: the naturality squares of these evaluated
// maps commute in the ordinary target. This is not unrestricted exchange of
// two lax transformation directions. Every map below is an actual composite.

// Exchange the original map by prewhiskering the precomposition telescope
// with the whole native evaluator. This keeps the I-action internal.
symbol one_cat_oplax_diagram_transpose_shape_transf
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G))
  : τ (@Transf I (Functor_cat B C)
      (@diagram_oplax_family_shape_func B I C F)
      (@diagram_oplax_family_shape_func B I C G))
≔ @fapp0 _ _
    (@comp_cat_con_fapp1_func I (Functor_cat (Functor_oplax_cat I C) C)
      (Functor_cat B C) (@diagram_oplax_evaluation_func I C)
      (@comp_cat_con_func B (Functor_oplax_cat I C) C F)
      (@comp_cat_con_func B (Functor_oplax_cat I C) C G))
    (@hom_precomp_along_tele_transf Cat_cat Cat_cat (@id_func Cat_cat)
      C B (Functor_oplax_cat I C) F G h);

// The same exchange / arrow-family / exchange outline as the original
// ordinary version, with its actual native input and output diagram profiles.
symbol one_cat_oplax_diagram_transpose_family_func
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G))
  : τ (Functor I (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)))
≔ @comp_cat_fapp0 I (Functor_cat WalkingArrow_cat (Functor_cat B C))
    (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@one_cat_family_oplax_exchange_func WalkingArrow_cat B C C1)
    (@one_cat_transf_arrow_diagram_func I (Functor_cat B C)
      (@one_cat_functor_category B C C1)
      (@diagram_oplax_family_shape_func B I C F)
      (@diagram_oplax_family_shape_func B I C G)
      (@one_cat_oplax_diagram_transpose_shape_transf B I C C1 F G h));

// Canonical whole column view. Its comparison with the actual I-functor's
// projection is checked independently; the I-functor and its action below
// remain the constructed whole owners, not a pointwise assembly.
symbol one_cat_oplax_diagram_transpose_column_func
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G)) (i : τ (Obj I))
  : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C))
≔ @transf_arrow_diagram_func B C
    (@comp_cat_fapp0 B (Functor_oplax_cat I C) C
      (@diagram_oplax_evaluation_at_func I C i) F)
    (@comp_cat_fapp0 B (Functor_oplax_cat I C) C
      (@diagram_oplax_evaluation_at_func I C i) G)
    (@fapp0 _ _ (@comp_cat_cov_fapp1_func B (Functor_oplax_cat I C) C
      (@diagram_oplax_evaluation_at_func I C i) F G) h);

symbol one_cat_oplax_diagram_transpose_transf
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C)
      (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i)
      (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h j))
≔ @fapp1_fapp0 I (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@one_cat_oplax_diagram_transpose_family_func B I C C1 F G h) i j u;

// Whole src evaluation of the transposed shape map, consumed by the
// original K/Q mate observations. Existing ordinary modification/reflection
// derives the equality from the actual components; no new comparison rule.
symbol one_cat_oplax_diagram_transpose_transf_src_path
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F) (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C j) F))
      (@diagram_oplax_family_map_at B WalkingArrow_cat C
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i)
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h j)
        (@one_cat_oplax_diagram_transpose_transf B I C C1 F G h i j u) walking_arrow_src) (@diagram_oplax_family_transf B I C F i j u))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F) in
  let Y : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C j) F) in
  let alpha : τ (@Transf B C X Y) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i)
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h j)
        (@one_cat_oplax_diagram_transpose_transf B I C C1 F G h i j u) walking_arrow_src) in
  let beta : τ (@Transf B C X Y) ≔ (@diagram_oplax_family_transf B I C F i j u) in
  @hom_to_path (@Transf_cat B C X Y) ((@one_cat_functor_category B C C1) X Y)
    alpha beta (@one_cat_modification B C C1 X Y alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (fapp0 X b) (fapp0 Y b))
        (@tapp0_fapp0 B C X Y b alpha) (@tapp0_fapp0 B C X Y b beta)
        (@eq_refl (Hom C (fapp0 X b) (fapp0 Y b)) (@tapp0_fapp0 B C X Y b beta))));

// Whole tgt evaluation of the transposed shape map, consumed by the
// original K/Q mate observations. Existing ordinary modification/reflection
// derives the equality from the actual components; no new comparison rule.
symbol one_cat_oplax_diagram_transpose_transf_tgt_path
  [B I C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (h : τ (@Transf B (Functor_oplax_cat I C) F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) G) (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C j) G))
      (@diagram_oplax_family_map_at B WalkingArrow_cat C
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i)
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h j)
        (@one_cat_oplax_diagram_transpose_transf B I C C1 F G h i j u) walking_arrow_tgt) (@diagram_oplax_family_transf B I C G i j u))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) G) in
  let Y : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C j) G) in
  let alpha : τ (@Transf B C X Y) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i)
        (@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h j)
        (@one_cat_oplax_diagram_transpose_transf B I C C1 F G h i j u) walking_arrow_tgt) in
  let beta : τ (@Transf B C X Y) ≔ (@diagram_oplax_family_transf B I C G i j u) in
  @hom_to_path (@Transf_cat B C X Y) ((@one_cat_functor_category B C C1) X Y)
    alpha beta (@one_cat_modification B C C1 X Y alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (fapp0 X b) (fapp0 Y b))
        (@tapp0_fapp0 B C X Y b alpha) (@tapp0_fapp0 B C X Y b beta)
        (@eq_refl (Hom C (fapp0 X b) (fapp0 Y b)) (@tapp0_fapp0 B C X Y b beta))));
