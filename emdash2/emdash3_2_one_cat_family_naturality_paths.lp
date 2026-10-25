/* Whole naturality after the existing postcomposition-family lift.
   Scope is the ordinary target; no caller component square is supplied. */
require open emdash.emdash3_2_one_cat_whiskering_paths;
require open emdash.emdash3_2_one_cat_action_paths;
require open emdash.emdash3_2_one_cat_functor_closure;
require open emdash.emdash3_2_diagram_reindex_views;
require open emdash.emdash3_2_one_cat_modifications;

symbol one_cat_family_naturality_path [B A C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (F G : τ (Functor A C))
  (eta : τ (@Transf A C F G)) (D E : τ (Functor B A)) (alpha : τ (@Transf B A D E))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B A C F D) (@comp_cat_fapp0 B A C G E))
      (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B A C F D) (@comp_cat_fapp0 B A C G D)
        (@comp_cat_fapp0 B A C G E)
        (@fapp1_fapp0 (Functor_cat B A) (Functor_cat B C) (@comp_cat_cov_func B A C G) D E alpha)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C D F G) eta))
      (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B A C F D) (@comp_cat_fapp0 B A C F E)
        (@comp_cat_fapp0 B A C G E)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C E F G) eta)
        (@fapp1_fapp0 (Functor_cat B A) (Functor_cat B C) (@comp_cat_cov_func B A C F) D E alpha)))
≔ let F0 : τ (Functor B C) ≔ (@comp_cat_fapp0 B A C F D) in
  let G0 : τ (Functor B C) ≔ (@comp_cat_fapp0 B A C G E) in
  let L : τ (@Transf B C F0 G0) ≔ (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B A C F D) (@comp_cat_fapp0 B A C G D)
        (@comp_cat_fapp0 B A C G E)
        (@fapp1_fapp0 (Functor_cat B A) (Functor_cat B C) (@comp_cat_cov_func B A C G) D E alpha)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C D F G) eta)) in
  let R : τ (@Transf B C F0 G0) ≔ (@comp_fapp0 (Functor_cat B C) (@comp_cat_fapp0 B A C F D) (@comp_cat_fapp0 B A C F E)
        (@comp_cat_fapp0 B A C G E)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C E F G) eta)
        (@fapp1_fapp0 (Functor_cat B A) (Functor_cat B C) (@comp_cat_cov_func B A C F) D E alpha)) in
  @hom_to_path (@Transf_cat B C F0 G0)
    ((@one_cat_functor_category B C C1) F0 G0) L R
    (@one_cat_modification B C C1 F0 G0 L R
      (λ b : τ (Obj B),
        @path_to_hom (Hom_cat C (@fapp0 B C F0 b) (@fapp0 B C G0 b))
          (@tapp0_fapp0 B C F0 G0 b L) (@tapp0_fapp0 B C F0 G0 b R)
          (@one_cat_component_naturality_path A C C1 F G eta
            (@fapp0 B A D b) (@fapp0 B A E b)
            (@tapp0_fapp0 B A D E b alpha))));

// Shape evaluation of the same whole whiskering, retaining native family endpoints.
symbol one_cat_diagram_family_whiskering_path [A B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F G : τ (Functor A (Functor_cat I C))) (h : τ (@Transf A (Functor_cat I C) F G))
  (D : τ (Functor B A)) (i : τ (Obj I))
  : τ (@= (@Transf B C
      (@comp_cat_fapp0 B A C (@diagram_family_at_func A I C F i) D)
      (@comp_cat_fapp0 B A C (@diagram_family_at_func A I C G i) D))
      (@fapp1_fapp0 (Functor_cat B (Functor_cat I C)) (Functor_cat B C) (@diagram_family_evaluation_func B I C i) (@comp_cat_fapp0 B A (Functor_cat I C) F D) (@comp_cat_fapp0 B A (Functor_cat I C) G D) (@fapp0 _ _ (@comp_cat_con_fapp1_func B A (Functor_cat I C) D F G) h))
      (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C D
        (@diagram_family_at_func A I C F i) (@diagram_family_at_func A I C G i))
        (@fapp1_fapp0 (Functor_cat A (Functor_cat I C)) (Functor_cat A C) (@diagram_family_evaluation_func A I C i) F G h)))
≔ @one_cat_whiskering_path A B (Functor_cat I C) C (@one_cat_functor_category I C C1) C1 D
    (@diagram_evaluation_at_func I C i) F G h;

// Same whole whiskering law at the actual oplax diagram coefficient.
symbol one_cat_oplax_diagram_family_whiskering_path [A B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F G : τ (Functor A (Functor_oplax_cat I C))) (h : τ (@Transf A (Functor_oplax_cat I C) F G))
  (D : τ (Functor B A)) (i : τ (Obj I))
  : τ (@= (@Transf B C
      (@comp_cat_fapp0 B A C (@diagram_oplax_family_at_func A I C F i) D)
      (@comp_cat_fapp0 B A C (@diagram_oplax_family_at_func A I C G i) D))
      (@diagram_oplax_family_map_at B I C (@comp_cat_fapp0 B A (Functor_oplax_cat I C) F D)
        (@comp_cat_fapp0 B A (Functor_oplax_cat I C) G D)
        (@fapp0 _ _ (@comp_cat_con_fapp1_func B A (Functor_oplax_cat I C) D F G) h) i)
      (@fapp0 _ _ (@comp_cat_con_fapp1_func B A C D
        (@diagram_oplax_family_at_func A I C F i) (@diagram_oplax_family_at_func A I C G i))
        (@diagram_oplax_family_map_at A I C F G h i)))
≔ @one_cat_whiskering_path A B (Functor_oplax_cat I C) C (@one_cat_oplax_functor_category I C C1) C1 D
    (@diagram_oplax_evaluation_at_func I C i) F G h;
