/* Original diagram-evaluation reviewer, with corrected shape variance.
   All ten positive and three negative observations are retained. */
require open emdash.emdash3_2_diagram_evaluation;

assert (I C : Cat) (i : τ (Obj I)) (F : τ (Functor I C))
  ⊢ @fapp0 _ _ (@diagram_evaluation_at_func I C i) F ≡ @fapp0 I C F i;
assert (I C : Cat) (i j : τ (Obj I)) (u : τ (Hom I i j)) (F : τ (Functor I C))
  ⊢ @tapp0_fapp0 _ _ _ _ F (@diagram_evaluation_transf I C i j u)
    ≡ @fapp1_fapp0 I C F i j u;
assert (I C : Cat) (i j : τ (Obj I))
  ⊢ @fapp1_func I (Functor_oplax_cat (Functor_cat I C) C)
      (@diagram_evaluation_func I C) i j
    : τ (Functor (Hom_cat I i j)
      (@Transf_oplax_cat (Functor_cat I C) C
        (@diagram_evaluation_at_func I C i) (@diagram_evaluation_at_func I C j)));
assert (I C : Cat) (i : τ (Obj I))
  (F G : τ (Functor I C)) (eta : τ (@Transf I C F G))
  ⊢ @fapp1_fapp0 _ _ (@diagram_evaluation_at_func I C i) F G eta
    ≡ @tapp0_fapp0 I C F G i eta;
assert (I C : Cat) (i j : τ (Obj I)) (u : τ (Hom I i j))
  (F G : τ (Functor I C)) (eta : τ (@Transf I C F G))
  ⊢ eq_refl (@tapp1_fapp0 I C F G i j eta u)
    : τ (@= (Obj (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j)))
      (@tapp1_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C j))
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C i))
        G F (@diagram_evaluation_transf I C i j u) eta)
      (@tapp1_fapp0 I C F G i j eta u));

// Decode the complete Even-dual mixed functor before taking its next Hom.
assert (I C : Cat) (i j : τ (Obj I)) (u : τ (Hom I i j))
  (F G : τ (Functor I C)) (eta theta : τ (@Transf I C F G))
  ⊢ @fapp1_func (@Transf_cat I C F G)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
      (@EvenDual_func _ _
        (@tapp1_func _ _ _ _ G F (@diagram_evaluation_transf I C i j u))) eta theta
    : τ (Functor (Hom_cat (@Transf_cat I C F G) eta theta)
      (Hom_cat (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
        (@tapp1_fapp0 I C F G i j eta u) (@tapp1_fapp0 I C F G i j theta u)));
assertnot (I C : Cat) (i : τ (Obj I)) (F : τ (Functor I C)) (other : τ (Obj C))
  ⊢ @fapp0 _ _ (@diagram_evaluation_at_func I C i) F ≡ other;

// Whole family evaluation uses the existing postcomposition representation.
assert (B I C : Cat) (i : τ (Obj I)) (F : τ (Functor B (Functor_cat I C)))
  ⊢ eq_refl (@fapp0 _ _ (@diagram_family_evaluation_func B I C i) F)
    : τ (@= (Functor B C)
      (@fapp0 _ _ (@diagram_family_evaluation_func B I C i) F)
      (@diagram_family_at_func B I C F i));
assert (B I C : Cat) (i : τ (Obj I))
  (F G : τ (Functor B (Functor_cat I C))) (h : τ (@Transf B (Functor_cat I C) F G))
  ⊢ @fapp1_fapp0 _ _ (@diagram_family_evaluation_func B I C i) F G h
    ≡ @fapp0 _ _ (@comp_cat_cov_fapp1_func B (Functor_cat I C) C
      (@diagram_evaluation_at_func I C i) F G) h;

// Whole family comparisons use actual opposite-profile prewhiskering.
assert (A B I C : Cat) (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) (F : τ (Functor A B))
  (i j : τ (Obj I)) (u v : τ (Hom I i j))
  ⊢ eq_refl (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u)
    : τ (@= (@Transf_oplax A C
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D i) F)
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D j) F))
      (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func A B C F)
        (@OddDual_func _ _ (@diagram_family_at_func B I C D i))
        (@OddDual_func _ _ (@diagram_family_at_func B I C D j))
        (@diagram_family_transf B I C D i j u)));
assertnot (A B I C : Cat) (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) (F : τ (Functor A B))
  (i j : τ (Obj I)) (u v : τ (Hom I i j))
  ⊢ eq_refl (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u)
    : τ (@= (@Transf_oplax A C
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D i) F)
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D j) F))
      (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func A B C F)
        (@OddDual_func _ _ (@diagram_family_at_func B I C D i))
        (@OddDual_func _ _ (@diagram_family_at_func B I C D j))
        (@diagram_family_transf B I C D i j v)));
assert (B I C : Cat) (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) (i j : τ (Obj I)) (u v : τ (Hom I i j))
  ⊢ eq_refl (@diagram_family_transf B I C D i j u)
    : τ (@= (@Transf_oplax B C (@diagram_family_at_func B I C D i) (@diagram_family_at_func B I C D j))
      (@diagram_family_transf B I C D i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func B (Functor_cat I C) C D)
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C i))
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C j))
        (@diagram_evaluation_transf I C i j u)));
assertnot (B I C : Cat) (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) (i j : τ (Obj I)) (u v : τ (Hom I i j))
  ⊢ eq_refl (@diagram_family_transf B I C D i j u)
    : τ (@= (@Transf_oplax B C (@diagram_family_at_func B I C D i) (@diagram_family_at_func B I C D j))
      (@diagram_family_transf B I C D i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func B (Functor_cat I C) C D)
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C i))
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C j))
        (@diagram_evaluation_transf I C i j v)));
