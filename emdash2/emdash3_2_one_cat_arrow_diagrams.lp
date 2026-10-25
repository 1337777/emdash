require open emdash.emdash3_2_cubical_arrow;
require open emdash.emdash3_2_arrow_diagram_families;
require open emdash.emdash3_2_one_cat_transfor_profiles;

/* Ordinary-target realization of the existing native arrow category. */

// Native squares in a OneCat target express the naturality of this family.
// There is no extra caller-supplied square or a new arrow-category carrier.
injective symbol one_cat_arrow_universal_transf
  [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (@Transf (@LaxArrow_cat C) C (@cubical_src_func C) (@cubical_tgt_func C));

rule @tapp0_fapp0 _ _ _ _
      (Struct_sigma _ (Struct_sigma _ $u))
      (@one_cat_arrow_universal_transf _ _)
  ↪ $u;

// Observe the original universal arrow after its total-dual identity normalizes.
// lhs-audit: keep 1,5,6 -- qualified opposite-source and constructor-visible identity endpoints.
rule @tapp1_fapp0 (CoAbove2_cat (Op_cat $K)) _ _ _
    (Struct_sigma $a (Struct_sigma $b $u))
    (Struct_sigma $a (Struct_sigma $b $u))
    (@one_cat_arrow_universal_transf _ _)
    (@id $K (Struct_sigma $a (Struct_sigma $b $u)))
  ↪ $u;

// The admitted universal arrow has the original components. Keep its whole
// strict view stable: only this named constructor's component is projected.
rule @tapp0_fapp0 _ _ _ _ $x
      (@strict_transfor _ _ _ _
        (@make_strict_transfor _ _ _ _
          (@one_cat_arrow_universal_transf $C $C1) _))
  ↪ @tapp0_fapp0 (@LaxArrow_cat $C) $C
      (@cubical_src_func $C) (@cubical_tgt_func $C) $x
      (@one_cat_arrow_universal_transf $C $C1);

// Cartesian evaluation now computes at the walking-arrow introduction
// owner. Keep the original path observation as a derived view of that cut.
symbol cart_arrow_diagram_point_path
  [K C : Cat] [F G : τ (Functor K C)]
  (U : τ (@StrictTransfor K C F G)) (x : τ (Obj K))
  : τ (@= (Functor WalkingArrow_cat C)
      (@sym_fapp0_func WalkingArrow_cat K C
        (@walking_arrow_func (Functor_cart_cat K C) F G U) x)
      (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
        (@tapp0_fapp0 K C F G x (@strict_transfor K C F G U))))
≔ @eq_refl (Functor WalkingArrow_cat C)
    (@sym_fapp0_func WalkingArrow_cat K C
      (@walking_arrow_func (Functor_cart_cat K C) F G U) x);

// The existing Cartesian construction, shared by its ordinary and oplax views.
// This is a semantic definition; it adds no new action or computation rule.
symbol one_cat_arrow_cart_diagram_func
  [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C))
≔ @sym_func WalkingArrow_cat (@LaxArrow_cat C) C
      (@walking_arrow_func (Functor_cart_cat (@LaxArrow_cat C) C)
        (@cubical_src_func C) (@cubical_tgt_func C)
        (@one_cat_strict_transfor (@LaxArrow_cat C) C C1
          (@cubical_src_func C) (@cubical_tgt_func C)
          (@one_cat_arrow_universal_transf C C1)));

symbol one_cat_arrow_diagram_func
  [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (@LaxArrow_cat C) (Functor_cat WalkingArrow_cat C))
// OneCat(C) supplies the existing strict-transfor admission. Cartesian
// exchange then constructs the same ordinary diagram interface, through its
// actual inclusion; the default ambient transformations remain lax.
≔ @comp_cat_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
    (Functor_cat WalkingArrow_cat C) (Functor_cart_include WalkingArrow_cat C)
    (@one_cat_arrow_cart_diagram_func C C1);

// The existing whole square action, viewed at its introduced endpoints.
// Endpoint comparison uses the established diagram-point unifier.
symbol one_cat_square_diagram_transf
  [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [X0 X1 Y0 Y1 : τ (Obj C)]
  (u : τ (Hom C X0 Y0)) (v : τ (Hom C X1 Y1))
  (a : τ (Hom C X0 X1)) (b : τ (Hom C Y0 Y1))
  (alpha : τ (Obj (@homdc_square_fibre C X0 X1 Y0 Y1 u v a b)))
  : τ (@Transf WalkingArrow_cat C
      (@walking_arrow_func C X0 Y0 u) (@walking_arrow_func C X1 Y1 v))
≔ @fapp1_fapp0 (@LaxArrow_cat C) (Functor_cat WalkingArrow_cat C)
    (@one_cat_arrow_diagram_func C C1)
    (@lax_edge C X0 Y0 u) (@lax_edge C X1 Y1 v)
    (@lax_square C X0 X1 Y0 Y1 u v a b alpha);
