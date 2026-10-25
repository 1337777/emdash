/*
  Emdash v3.2: retained fixed-forward pseudofunctor data for default functors.

  Public Functor is strict; its existing extracted compositor computes to the
  strict default. The readable endpoint paths use the established stable
  postcomposition views and default functor-composition path.

  IsPseudoFunctor remains the existing dependent property with actual selected
  OmegaEquivAlong inverse data. This migration does not replace that inverse,
  add a compositor, or introduce a lax-functor carrier. Existing supplied
  identity/composition property constructors retain their original status.
*/

require open emdash.emdash3_2_gray_profiles;
require open emdash.emdash3_2_strict_functor_actions;
require open emdash.emdash3_2_path_pseudo_laxity;

symbol readable_pseudo_post_raw_source
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Obj (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @hom_postcomp_fapp0
    B B (@id_func B)
    (@fapp0 A B F X)
    (@fapp0 A B F Y)
    (@fapp0 A B F Z)
    (@fapp1_fapp0 A B F Y Z g)
    (@fapp1_fapp0 A B F X Y f);

symbol readable_pseudo_post_raw_target
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Obj (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @fapp1_fapp0 A B F X Z (@comp_fapp0 A X Y Z g f);

symbol readable_pseudo_post_stable_action
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Obj (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @fapp1_fapp0 A B F X Z
    (@hom_postcomp_fapp0 A A (@id_func A) X Y Z g f);

/*
  Readable endpoint views under the strict default. The stable postcomposition
  owners need not share a runtime normal form. Their existing endpoint paths
  and the generic functor-composition path compare the intrinsic action with
  the readable mapped composite, without a new unification rule.
*/

symbol readable_pseudo_post_stable_comp_path
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_stable_action A B F X Y Z g f)
      (@readable_pseudo_post_raw_target A B F X Y Z g f))
≔ @eq_ap
    (Hom A X Z)
    (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
    (λ r : τ (Hom A X Z), @fapp1_fapp0 A B F X Z r)
    (@hom_postcomp_fapp0 A A (@id_func A) X Y Z g f)
    (@comp_fapp0 A X Y Z g f)
    (@path_pseudo_laxity_postcomp_comp_path
      A A (@id_func A) X Y Z g f);

symbol readable_pseudo_post_source_path
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@readable_pseudo_post_raw_source A B F X Y Z g f))
≔ @eq_trans
    (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@strict_functor_compositor_lhs A B F X Y Z g f)
    (@readable_pseudo_post_raw_target A B F X Y Z g f)
    (@readable_pseudo_post_raw_source A B F X Y Z g f)
    (@readable_pseudo_post_stable_comp_path A B F X Y Z g f)
    (@eq_trans
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_target A B F X Y Z g f)
      (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B F Y) (@fapp0 A B F Z)
        (@fapp1_fapp0 A B F Y Z g) (@fapp1_fapp0 A B F X Y f))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@functor_composition_path A B F X Y Z g f)
      (@eq_sym
        (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
        (@readable_pseudo_post_raw_source A B F X Y Z g f)
        (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B F Y) (@fapp0 A B F Z)
          (@fapp1_fapp0 A B F Y Z g) (@fapp1_fapp0 A B F X Y f))
        (@path_pseudo_laxity_postcomp_comp_path B B (@id_func B)
          (@fapp0 A B F X) (@fapp0 A B F Y) (@fapp0 A B F Z)
          (@fapp1_fapp0 A B F Y Z g) (@fapp1_fapp0 A B F X Y f))));

symbol readable_pseudo_post_target_path
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_rhs A B F X Y Z g f)
      (@readable_pseudo_post_raw_target A B F X Y Z g f))
≔ @readable_pseudo_post_stable_comp_path A B F X Y Z g f;

protected symbol readable_pseudo_post_source_reframe
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@strict_functor_compositor_lhs A B F X Y Z g f))
≔ @path_to_hom
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@readable_pseudo_post_raw_source A B F X Y Z g f)
    (@strict_functor_compositor_lhs A B F X Y Z g f)
    (@eq_sym
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@readable_pseudo_post_source_path A B F X Y Z g f));

protected symbol readable_pseudo_post_target_reframe
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@strict_functor_compositor_rhs A B F X Y Z g f)
      (@readable_pseudo_post_raw_target A B F X Y Z g f))
≔ @path_to_hom
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@strict_functor_compositor_rhs A B F X Y Z g f)
    (@readable_pseudo_post_raw_target A B F X Y Z g f)
    (@readable_pseudo_post_target_path A B F X Y Z g f);

// Readable post/left cell obtained only by reframing the existing internal
// compositor. No independent coherence cell is declared.
symbol readable_pseudo_post_cell
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@readable_pseudo_post_raw_target A B F X Y Z g f))
≔ @comp_fapp0
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@readable_pseudo_post_raw_source A B F X Y Z g f)
    (@strict_functor_compositor_rhs A B F X Y Z g f)
    (@readable_pseudo_post_raw_target A B F X Y Z g f)
    (@readable_pseudo_post_target_reframe A B F X Y Z g f)
    (@comp_fapp0
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@strict_functor_compositor_lhs A B F X Y Z g f)
      (@strict_functor_compositor_rhs A B F X Y Z g f)
      (@fapp1_compositor A B F X Y Z g f)
      (@readable_pseudo_post_source_reframe A B F X Y Z g f));

// Pre/right readable source for the same composite.
symbol readable_pseudo_pre_raw_source
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Obj (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
≔ @hom_precomp_along_fapp0
    B B (@id_func B)
    (@fapp0 B B (@id_func B) (@fapp0 A B F Z))
    (@fapp0 A B F X)
    (@fapp0 A B F Y)
    (@fapp1_fapp0 A B F X Y f)
    (@fapp1_fapp0 A B F Y Z g);

// Existing proof-time post/pre comparison, now retained as first-class path.
symbol readable_pseudo_post_pre_source_path
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@=
      (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@readable_pseudo_pre_raw_source A B F X Y Z g f))
≔ @eq_refl
    (Hom B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@readable_pseudo_post_raw_source A B F X Y Z g f);

protected symbol readable_pseudo_post_pre_reframe
  [A B : Cat]
  (F : τ (Functor A B))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_source A B F X Y Z g f)
      (@readable_pseudo_pre_raw_source A B F X Y Z g f))
≔ @path_to_hom
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@readable_pseudo_post_raw_source A B F X Y Z g f)
    (@readable_pseudo_pre_raw_source A B F X Y Z g f)
    (@readable_pseudo_post_pre_source_path A B F X Y Z g f);

// Normal-pseudofunctor property: every existing readable compositor is a
// fixed-forward native omega-equivalence. Identity preservation remains the
// default strict-functor convention.
symbol IsPseudoFunctor
  [A B : Cat]
  (F : τ (Functor A B))
  : Grpd
≔ @Pi_grpd
    (Obj A)
    (λ X : τ (Obj A),
      @Pi_grpd
        (Obj A)
        (λ Y : τ (Obj A),
          @Pi_grpd
            (Obj A)
            (λ Z : τ (Obj A),
              @Pi_grpd
                (Hom A Y Z)
                (λ g : τ (Hom A Y Z),
                  @Pi_grpd
                    (Hom A X Y)
                    (λ f : τ (Hom A X Y),
                      @OmegaEquivAlong
                        (Hom_cat B
                          (@fapp0 A B F X)
                          (@fapp0 A B F Z))
                        _ _
                        (@readable_pseudo_post_cell
                          A B F X Y Z g f))))));

// Post/left readable compositor:
//   F[g] o F[f] ~= F[g o f]
// at the stable hom_postcomp owner used by source-varying hom families.
symbol pseudo_compositor_equiv
  [A B : Cat]
  [F : τ (Functor A B)]
  (P : τ (@IsPseudoFunctor A B F))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (@OmegaEquivAlong
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      _ _
      (@readable_pseudo_post_cell A B F X Y Z g f))
≔ P X Y Z g f;

// Pre/right reverse adjustment uses the selected left inverse of the one
// fixed-forward post cell, followed by the existing post/pre endpoint reframe.
// The `OmegaEquivAlong` right inverse and both cancellation laws remain
// available to later coherence consumers.
symbol pseudo_pre_inverse
  [A B : Cat]
  [F : τ (Functor A B)]
  (P : τ (@IsPseudoFunctor A B F))
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y))
  : τ (Hom
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      (@readable_pseudo_post_raw_target A B F X Y Z g f)
      (@readable_pseudo_pre_raw_source A B F X Y Z g f))
≔ @comp_fapp0
    (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
    (@readable_pseudo_post_raw_target A B F X Y Z g f)
    (@readable_pseudo_post_raw_source A B F X Y Z g f)
    (@readable_pseudo_pre_raw_source A B F X Y Z g f)
    (@readable_pseudo_post_pre_reframe A B F X Y Z g f)
    (@omega_equiv_along_left_inv
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
      _ _
      (@readable_pseudo_post_cell A B F X Y Z g f)
      (@pseudo_compositor_equiv A B F P X Y Z g f));

// Supplied identity proof. Constructing it transparently requires the
// extracted unit/normality interface, which remains separate.
constant symbol identity_is_pseudo
  (A : Cat)
  : τ (@IsPseudoFunctor A A (@id_func A));

// Supplied composition proof. A transparent constructor requires the next
// internal action comparing the composite functor's intrinsic compositor with
// the two component properties.
constant symbol comp_is_pseudo
  [A B C : Cat]
  [F : τ (Functor A B)]
  (PF : τ (@IsPseudoFunctor A B F))
  [G : τ (Functor B C)]
  (PG : τ (@IsPseudoFunctor B C G))
  : τ (@IsPseudoFunctor
      A C (@comp_cat_fapp0 A B C G F));
