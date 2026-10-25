/*
  Emdash v3.2: a fixed-boundary cubical square total and its next action.

  The fixed-endpoint homdc_ classifier is totalized first in its
  contravariant b coordinate and then in its covariant a coordinate. Objects
  are constructor-visible triples (a,(b,alpha)); the four variance-correct
  line observations are whole. An arrow between two such objects has the two
  endpoint squares and four projected side faces.

  The source and target vertical edges u,v are fixed parameters of this first
  bounded total. Consequently their two side faces are degenerate identities.
  The later `emdash3_2_cubical_internalization` module now supplies full
  endpoint variation by applying the existing `homd_int` to the total-dual
  inner edge family over its shifted outer base; no parameterized-hom primitive is required. The
  bottom face here deliberately remains a Pi-section action over the stable
  Sigma-projection pullback rather than being forced through a false
  strict-constant conversion.
*/

require open emdash.emdash3_2_cubical_dependent_hom;

// Whole first projection of a Cartesian-parameterized Sigma total.
// Total maps preserve the inner base strictly. The result is the canonical
// Cartesian map; ordinary displayed consumers use its existing inclusion.
// No naturality certificate or comparison cell is supplied as input.
injective symbol sigma_proj1_family_funcd
  [K A : Cat]
  (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
  : τ (Hom (Functor_cart_cat K Cat_cart)
      (@comp_cat_fapp0
        K (Functor_cart_cat A Cat_cart) Cat_cart
        (@Sigma_coeff_func A) G)
      (@Const_catd K A));

// The component at k is the ordinary first projection of Sigma(G[k]).
rule @tapp0_fapp0
      _ _ _ _ $k
      (@strict_transfor _ _ _ _ (@sigma_proj1_family_funcd $K $A $G))
  ↪ @Sigma_proj1_func
      $A
      (@fapp0 $K (Functor_cart_cat $A Cat_cart) $G $k);

// Higher displayed action is inherited from the Cartesian map profile,
// then from the existing Sigma_proj1_func Hom action.

// Reindex the canonical total-dual Sigma projection through its ordinary
// displayed view. The outer base changes by R; the inner total remains the
// same projection. An explicit identity reframe requires its actual source
// family to agree. This is the corrected whole form of the former Op view.
unif_rule @fapp1_fapp0 _ _ (@Pullback_catd_func $A $B $F) $E0 _
    (@comp_fapp0 _ $E0 _ _
      (@strict_transfor _ _ _ _
        (@TotalOp_funcd $L _ _ (@sigma_proj1_family_funcd $L $I $G)))
      (@id _ $E0))
  ≡ @strict_transfor _ _ _ _
    (@TotalOp_funcd $L0 _ _ (@sigma_proj1_family_funcd $L0 $I0 $G0))
  ↪ [ $B ≡ CoAbove2_cat $L; $L0 ≡ CoAbove2_cat $A; $I0 ≡ $I;
      $E0 ≡ @TotalOp_catd $L
        (@comp_cat_fapp0 $L (Functor_cart_cat $I Cat_cart) Cat_cart (@Sigma_coeff_func $I) $G);
      $G0 ≡ @comp_cat_fapp0 (CoAbove2_cat $A) $L (Functor_cart_cat $I Cat_cart)
        $G (@CoAbove2_func $A $B $F) ];

// Project canonical total base change on a section. The prewhiskering is the
// existing Cartesian Hom-action of sigma_pullback_coeff_transf; F survives
// as its total-dual base action and in the reindexed source family.
unif_rule @section_postcomp_sec $K _ _
    (@strict_transfor _ _ _ _
      (@TotalOp_funcd $L _ _ (@sigma_proj1_family_funcd $L $B $H)))
    (@section_postcomp_sec $K _ _
      (@strict_transfor _ _ _ _
        (@TotalOp_funcd $L _ _
          (@hom_precomp_along_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
            Cat_cart $L (Functor_cart_cat $B Cat_cart) $H _ _
            (@sigma_pullback_coeff_transf $A $B $F)))) $s)
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@CoAbove2_func _ _ (@Op_func _ _ $F0))
    (@section_postcomp_sec $K0 _ _
      (@strict_transfor _ _ _ _
        (@TotalOp_funcd $L0 _ _ (@sigma_proj1_family_funcd $L0 $A0 $H0))) $s0)
  ↪ [ $K ≡ CoAbove2_cat $L; $K0 ≡ $K; $L0 ≡ $L; $A0 ≡ $A;
      $F0 ≡ $F; $s0 ≡ $s;
      $H0 ≡ @comp_cat_fapp0 $L (Functor_cart_cat $B Cat_cart)
        (Functor_cart_cat $A Cat_cart) (@comp_cat_con_cart_func $A $B Cat_cart $F) $H ];

// Sigma of the actual strict parameter map preserves the inner base. Its
// displayed components can still be lax; U is not assumed to be an identity.
unif_rule @section_postcomp_sec $K _ _
    (@strict_transfor _ _ _ _
      (@TotalOp_funcd $L _ _ (@sigma_proj1_family_funcd $L $A $D)))
    (@section_postcomp_sec $K _ _
      (@strict_transfor _ _ _ _
        (@TotalOp_funcd $L _ _ (@Sigma_parameter_funcd $L $A $E $D _))) $s)
  ≡ @section_postcomp_sec $K0 _ _
    (@strict_transfor _ _ _ _
      (@TotalOp_funcd $L0 _ _ (@sigma_proj1_family_funcd $L0 $A0 $E0))) $s0
  ↪ [ $K ≡ CoAbove2_cat $L; $K0 ≡ $K; $L0 ≡ $L; $A0 ≡ $A;
      $E0 ≡ $E; $s0 ≡ $s ];

// The original identity graph projects to its whole identity base functor.
unif_rule @section_postcomp_sec _ _ _
    (@strict_transfor _ _ _ _
      (@TotalOp_funcd _ _ _
        (@sigma_proj1_family_funcd _ $K (@hom_int $K $K (@id Cat_cat $K)))))
    (@hom_identity_graph_sec $K)
  ≡ @id Cat_cat (CoAbove2_cat (Op_cat $K))
  ↪ [ tt ≡ tt ];

// The seven former same-base Op clauses are retired. The four whole
// comparisons above use TotalOp over the R-shifted base. Their point
// observations use the native Sigma projection, capped Sigma-map and
// base-change owners. Cartesian composition and named-pullback source views
// have a checked proof-time comparison, not a common runtime normal form.
// The pinned original block and all seven dispositions are recorded in
// audits/strict-default-action-boundary/production_cubical_projection_point_review.md.

// At a, totalize the b-indexed filler family.
symbol homdc_inner_total_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Functor (Hom_cat K1 x1 y1) Cat_cart)
≔ @comp_cat_fapp0
    (Hom_cat K1 x1 y1)
    (Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)
    Cat_cart
    (@Sigma_coeff_func (Op_cat (Hom_cat K2 x2 y2)))
    (@homdc_ K1 K2 E x1 y1 x2 y2 u v);

// Fixed vertical boundary; objects are (a,(b,alpha)).
symbol homdc_square_cat
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : Cat
≔ @Sigma_cat
    (Hom_cat K1 x1 y1)
    (@homdc_inner_total_func
      K1 K2 E x1 y1 x2 y2 u v);

// Variance-correct target family of the inner face section.
symbol homdc_square_bottom_catd
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Catd
      (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v))
≔ @Sigma_proj1_pullback_catd
    (Hom_cat K1 x1 y1)
    (@homdc_inner_total_func K1 K2 E x1 y1 x2 y2 u v)
    (@Const_catd
      (Hom_cat K1 x1 y1)
      (Op_cat (Hom_cat K2 x2 y2)));

// Outer/first-coordinate line face.
symbol homdc_square_top_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Functor
      (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
      (Hom_cat K1 x1 y1))
≔ @Sigma_proj1_func
    (Hom_cat K1 x1 y1)
    (@homdc_inner_total_func
      K1 K2 E x1 y1 x2 y2 u v);

// Fixed source and target vertical line faces. They remain whole constant
// functors; their action produces the two degenerate side faces in the first
// bounded cube test.
symbol homdc_square_left_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Functor
      (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
      (Fibre_cat
        (@fapp0 (Op_cat K1) (Catd_cat K2) E x1)
        x2))
≔ @Const_func
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat
      (@fapp0 (Op_cat K1) (Catd_cat K2) E x1)
      x2)
    u;

symbol homdc_square_right_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Functor
      (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
      (Fibre_cat
        (@fapp0 (Op_cat K1) (Catd_cat K2) E y1)
        y2))
≔ @Const_func
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat
      (@fapp0 (Op_cat K1) (Catd_cat K2) E y1)
      y2)
    v;

// Inner/second-coordinate line face. Its target is opposite because b is the
// contravariant coordinate of the selected source-to-target hom family.
symbol homdc_square_bottom_sec
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  : τ (Obj
      (@Pi_cat
        (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_bottom_catd
          K1 K2 E x1 y1 x2 y2 u v)))
≔ @sigma_functord_sec
    (Hom_cat K1 x1 y1)
    (@homdc_inner_total_func
      K1 K2 E x1 y1 x2 y2 u v)
    (@Const_catd
      (Hom_cat K1 x1 y1)
      (Op_cat (Hom_cat K2 x2 y2)))
    (@strict_transfor _ _ _ _
      (@sigma_proj1_family_funcd
        (Hom_cat K1 x1 y1)
        (Op_cat (Hom_cat K2 x2 y2))
        (@homdc_ K1 K2 E x1 y1 x2 y2 u v)));

// Constructor-visible square object.
symbol homdc_square_obj
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  [x1 y1 : τ (Obj K1)]
  [x2 y2 : τ (Obj K2)]
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  (a : τ (Hom K1 x1 y1))
  (b : τ (Hom K2 x2 y2))
  (alpha : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b)))
  : τ (Obj
      (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v))
≔ Struct_sigma a (Struct_sigma b alpha);

// A next-hom object theta between two square objects has six faces: its two
// ordinary endpoints plus the images below under the four whole line faces.
symbol homdc_cube_top_face
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  [x1 y1 : τ (Obj K1)]
  [x2 y2 : τ (Obj K2)]
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  [a a' : τ (Hom K1 x1 y1)]
  [b b' : τ (Hom K2 x2 y2)]
  [alpha : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))]
  [beta : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a' b'))]
  (theta : τ (Hom
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)))
  : τ (Hom (Hom_cat K1 x1 y1) a a')
≔ @fapp1_fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Hom_cat K1 x1 y1)
    (@homdc_square_top_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)
    theta;

symbol homdc_cube_bottom_face
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  [x1 y1 : τ (Obj K1)]
  [x2 y2 : τ (Obj K2)]
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  [a a' : τ (Hom K1 x1 y1)]
  [b b' : τ (Hom K2 x2 y2)]
  [alpha : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))]
  [beta : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a' b'))]
  (theta : τ (Hom
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)))
  : τ (Hom
      (Fibre_cat
        (@homdc_square_bottom_catd
          K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_obj
          K1 K2 E x1 y1 x2 y2 u v a' b' beta))
      (@piapp1_src_obj
        (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_bottom_catd
          K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_bottom_sec
          K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_obj
          K1 K2 E x1 y1 x2 y2 u v a b alpha)
        (@homdc_square_obj
          K1 K2 E x1 y1 x2 y2 u v a' b' beta)
        theta)
      (@piapp0
        (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_bottom_catd
          K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_bottom_sec
          K1 K2 E x1 y1 x2 y2 u v)
        (@homdc_square_obj
          K1 K2 E x1 y1 x2 y2 u v a' b' beta)))
≔ @piapp1_fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_bottom_catd
      K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_bottom_sec K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)
    theta;

symbol homdc_cube_left_face
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  [x1 y1 : τ (Obj K1)]
  [x2 y2 : τ (Obj K2)]
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  [a a' : τ (Hom K1 x1 y1)]
  [b b' : τ (Hom K2 x2 y2)]
  [alpha : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))]
  [beta : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a' b'))]
  (theta : τ (Hom
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)))
  : τ (Hom
      (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)
      u u)
≔ @fapp1_fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)
    (@homdc_square_left_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)
    theta;

symbol homdc_cube_right_face
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Catd_cat K2)))
  [x1 y1 : τ (Obj K1)]
  [x2 y2 : τ (Obj K2)]
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)))
  [a a' : τ (Hom K1 x1 y1)]
  [b b' : τ (Hom K2 x2 y2)]
  [alpha : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))]
  [beta : τ (Obj
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a' b'))]
  (theta : τ (Hom
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)))
  : τ (Hom
      (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)
      v v)
≔ @fapp1_fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)
    (@homdc_square_right_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta)
    theta;
