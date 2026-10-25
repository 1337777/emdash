/*
  Reviewer example: the fixed-boundary square total and its six-face next
  action. The top and bottom coordinates vary; the fixed vertical boundary
  produces two intentionally degenerate side faces.
*/

require open emdash.emdash3_2_cubical_square_total;
// The two varying line observations compute from whole Sigma projections.
assert [K1 K2 : Cat]
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
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))) ⊢
  @fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Hom_cat K1 x1 y1)
    (@homdc_square_top_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
  ≡ a;

assert [K1 K2 : Cat]
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
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))) ⊢
  @piapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_bottom_catd
      K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_bottom_sec K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
  ≡ b;

assert [K1 K2 : Cat]
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
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))) ⊢
  @fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)
    (@homdc_square_left_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
  ≡ u;

assert [K1 K2 : Cat]
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
    (@homdc_fibre K1 K2 E x1 y1 x2 y2 u v a b))) ⊢
  @fapp0
    (@homdc_square_cat K1 K2 E x1 y1 x2 y2 u v)
    (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)
    (@homdc_square_right_func K1 K2 E x1 y1 x2 y2 u v)
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a b alpha)
  ≡ v;

// The next-hom owner takes a volume theta between two constructor-visible
// square objects. Its ordinary source and target are the first two faces; the
// four operations below are the remaining side-face observations.
type @homdc_cube_top_face;
type @homdc_cube_bottom_face;
type @homdc_cube_left_face;
type @homdc_cube_right_face;

// The two fixed-boundary side faces compute to identities rather than being
// postulated opaque fillers.
assert [K1 K2 : Cat]
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
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta))) ⊢
  @homdc_cube_left_face
    K1 K2 E x1 y1 x2 y2 u v a a' b b' alpha beta theta
  ≡ @id
      (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E x1) x2)
      u;

assert [K1 K2 : Cat]
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
    (@homdc_square_obj K1 K2 E x1 y1 x2 y2 u v a' b' beta))) ⊢
  @homdc_cube_right_face
    K1 K2 E x1 y1 x2 y2 u v a a' b b' alpha beta theta
  ≡ @id
      (Fibre_cat (@fapp0 (Op_cat K1) (Catd_cat K2) E y1) y2)
      v;

// The canonical whole projection retains an arbitrary nonidentity inner base arrow.
assert [K A : Cat]
  (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
  [x y : τ (Obj K)] (p : τ (Hom K x y))
  [a b : τ (Obj A)]
  (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)))
  (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)))
  (q : τ (Hom A a b))
  (beta : τ (Hom
    (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)
    (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)
      (@catd_transport_func A (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a b q)
      (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (@Fibre_func A
        (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
        (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
        (@strict_transfor A Cat_cart
          (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
          (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
          (@fapp1_fapp0 K (Functor_cart_cat A Cat_cart) G x y p))
        a)
      u))
    v)) ⊢
  @fdapp1_int_hom_fapp0 K
    (@comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) Cat_cart (@Sigma_coeff_func A) G)
    (@Const_catd K A)
    (@strict_transfor K Cat_cart
      (@comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) Cat_cart (@Sigma_coeff_func A) G)
      (@Const_catd K A)
      (@sigma_proj1_family_funcd K A G))
    x y p (Struct_sigma a u) (Struct_sigma b v)
    (@sigma_arrow A (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a b
      (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (@Fibre_func A
        (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
        (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
        (@strict_transfor A Cat_cart
          (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
          (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
          (@fapp1_fapp0 K (Functor_cart_cat A Cat_cart) G x y p))
        a)
      u)
      v q beta)
  ≡ q;

// Changing the projected inner base arrow is not a valid computation.
assertnot [K A : Cat]
  (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
  [x y : τ (Obj K)] (p : τ (Hom K x y))
  [a b : τ (Obj A)]
  (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)))
  (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)))
  (q : τ (Hom A a b))
  (beta : τ (Hom
    (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)
    (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)
      (@catd_transport_func A (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a b q)
      (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (@Fibre_func A
        (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
        (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
        (@strict_transfor A Cat_cart
          (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
          (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
          (@fapp1_fapp0 K (Functor_cart_cat A Cat_cart) G x y p))
        a)
      u))
    v))
  (q_other : τ (Hom A a b)) ⊢
  @fdapp1_int_hom_fapp0 K
    (@comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) Cat_cart (@Sigma_coeff_func A) G)
    (@Const_catd K A)
    (@strict_transfor K Cat_cart
      (@comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) Cat_cart (@Sigma_coeff_func A) G)
      (@Const_catd K A)
      (@sigma_proj1_family_funcd K A G))
    x y p (Struct_sigma a u) (Struct_sigma b v)
    (@sigma_arrow A (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a b
      (@fapp0
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)
      (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) a)
      (@Fibre_func A
        (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
        (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
        (@strict_transfor A Cat_cart
          (@fapp0 K (Functor_cart_cat A Cat_cart) G x)
          (@fapp0 K (Functor_cart_cat A Cat_cart) G y)
          (@fapp1_fapp0 K (Functor_cart_cat A Cat_cart) G x y p))
        a)
      u)
      v q beta)
  ≡ q_other;

// Readable aliases for the existing whole constructions; no supplied data.
protected symbol cstd_review_sigma_family [K A : Cat]
 (G : τ (Functor K (Functor_cart_cat A Cat_cart))) : τ (Catd K)
≔ @comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) Cat_cart (@Sigma_coeff_func A) G;
protected symbol cstd_review_total_dual_sigma [K A : Cat]
 (G : τ (Functor K (Functor_cart_cat A Cat_cart))) : τ (Catd (CoAbove2_cat K))
≔ @TotalOp_catd K (@cstd_review_sigma_family K A G);
protected symbol cstd_review_total_dual_projection [K A : Cat]
 (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
 : τ (@Functord (CoAbove2_cat K)
   (@cstd_review_total_dual_sigma K A G)
   (@TotalOp_catd K (@Const_catd K A)))
≔ @strict_transfor _ _ _ _
  (@TotalOp_funcd K _ _ (@sigma_proj1_family_funcd K A G));

// The corrected counterpart of the first former same-base Op point rule.
assert [K A : Cat] (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)))
 (alpha : τ (Hom
   (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
   (@fapp0
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) x)
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
     (@catd_transport_func (CoAbove2_cat K)
       (@cstd_review_total_dual_sigma K A G) x y p)
     (Struct_sigma a u))
   (Struct_sigma b v))) ⊢
 @fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A G) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A G)
  x y p (Struct_sigma a u) (Struct_sigma b v)
   (Struct_sigma (sigma_Fst alpha) (sigma_Snd alpha))
 ≡ sigma_Fst alpha;

// Included parameter families and their existing whole Sigma image.
protected symbol cstd_review_parameter_family [K A : Cat]
 (E : τ (Functor K (Functor_cart_cat A Cat_cart)))
 : τ (Functor K (Catd_cat A))
≔ @comp_cat_fapp0 K (Functor_cart_cat A Cat_cart) (Catd_cat A)
   (Functor_cart_include A Cat_cart) E;
protected symbol cstd_review_total_dual_parameter [K A : Cat]
 [E D : τ (Functor K (Functor_cart_cat A Cat_cart))]
 (U : τ (Hom (Functor_cart_cat K (Catd_cat A))
   (@cstd_review_parameter_family K A E) (@cstd_review_parameter_family K A D)))
 : τ (@Functord (CoAbove2_cat K)
   (@cstd_review_total_dual_sigma K A E) (@cstd_review_total_dual_sigma K A D))
≔ @strict_transfor _ _ _ _
  (@TotalOp_funcd K _ _ (@Sigma_parameter_funcd K A E D U));

// Corrected counterpart of projection after the fibrewise Sigma parameter map.
assert [K A : Cat] [E D : τ (Functor K (Functor_cart_cat A Cat_cart))]
 (U : τ (Hom (Functor_cart_cat K (Catd_cat A))
   (@cstd_review_parameter_family K A E) (@cstd_review_parameter_family K A D)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) E x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) E y) b)))
 (alpha : τ (Hom
   (Fibre_cat (@cstd_review_total_dual_sigma K A E) y)
   (@fapp0
     (Fibre_cat (@cstd_review_total_dual_sigma K A E) x)
     (Fibre_cat (@cstd_review_total_dual_sigma K A E) y)
     (@catd_transport_func (CoAbove2_cat K)
       (@cstd_review_total_dual_sigma K A E) x y p)
     (Struct_sigma a u))
   (Struct_sigma b v))) ⊢
@fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A D) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A D)
  x y p
 (@fapp0
  (Fibre_cat (@cstd_review_total_dual_sigma K A E) x)
  (Fibre_cat (@cstd_review_total_dual_sigma K A D) x)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A E)
    (@cstd_review_total_dual_sigma K A D) (@cstd_review_total_dual_parameter K A E D U) x) (Struct_sigma a u))
 (@fapp0
  (Fibre_cat (@cstd_review_total_dual_sigma K A E) y)
  (Fibre_cat (@cstd_review_total_dual_sigma K A D) y)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A E)
    (@cstd_review_total_dual_sigma K A D) (@cstd_review_total_dual_parameter K A E D U) y) (Struct_sigma b v))
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A E) (@cstd_review_total_dual_sigma K A D) (@cstd_review_total_dual_parameter K A E D U)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
 ≡ @fdapp1_int_hom_fapp0 (CoAbove2_cat K)
   (@cstd_review_total_dual_sigma K A E) (@TotalOp_catd K (@Const_catd K A))
   (@cstd_review_total_dual_projection K A E)
   x y p (Struct_sigma a u) (Struct_sigma b v) alpha;

// Reindexing and the canonical whole parameter refinement of total base change.
protected symbol cstd_review_inner_pullback [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 : τ (Functor K (Functor_cart_cat A Cat_cart))
≔ @comp_cat_fapp0 K (Functor_cart_cat B Cat_cart) (Functor_cart_cat A Cat_cart)
   (@comp_cat_con_cart_func A B Cat_cart F) H;
protected symbol cstd_review_total_dual_basechange [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 : τ (@Functord (CoAbove2_cat K)
   (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
   (@cstd_review_total_dual_sigma K B H))
≔ @strict_transfor _ _ _ _
  (@TotalOp_funcd K _ _
    (@hom_precomp_along_fapp1_fapp0 Cat_cart Cat_cart (@id_func Cat_cart)
      Cat_cart K (Functor_cart_cat B Cat_cart) H
      (@Sigma_pullback_coeff_source A B F) (@Sigma_coeff_func B)
      (@sigma_pullback_coeff_transf A B F)));

// Corrected counterpart of inner-base projection after total base change.
// Canonical source of the actual base-change map.
assert [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢
@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K B H)
  (@TotalOp_catd K (@Const_catd K B)) (@cstd_review_total_dual_projection K B H)
  x y p
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K B H) x)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) x) (Struct_sigma a u))
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y) (Fibre_cat (@cstd_review_total_dual_sigma K B H) y)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) y) (Struct_sigma b v))
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
  ≡ @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) a b
  (@fapp1_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F))) (TotalOp_cat A)
    (@TotalOp_func (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)) A (@Sigma_proj1_func A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)))
    (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
  (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p) (Struct_sigma a u)) (Struct_sigma b v) alpha);

// Type the two presentations before recording their conversion boundary.
assert [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢
@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K B H)
  (@TotalOp_catd K (@Const_catd K B)) (@cstd_review_total_dual_projection K B H)
  x y p
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K B H) x)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) x) (Struct_sigma a u))
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y) (Fibre_cat (@cstd_review_total_dual_sigma K B H) y)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) y) (Struct_sigma b v))
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
  : τ (Obj (Hom_cat (TotalOp_cat B) (@fapp0 A B F a) (@fapp0 A B F b)));

assert [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢ @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) a b
   (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
     (@TotalOp_catd K (@Const_catd K A)) (@cstd_review_total_dual_projection K A (@cstd_review_inner_pullback K A B F H))
     x y p (Struct_sigma a u) (Struct_sigma b v) alpha) : τ (Obj (Hom_cat (TotalOp_cat B) (@fapp0 A B F a) (@fapp0 A B F b)));

// The source-family presentation agrees at proof time below; its runtime form stays distinct.
assertnot [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢
@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K B H)
  (@TotalOp_catd K (@Const_catd K B)) (@cstd_review_total_dual_projection K B H)
  x y p
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K B H) x)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) x) (Struct_sigma a u))
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y) (Fibre_cat (@cstd_review_total_dual_sigma K B H) y)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) y) (Struct_sigma b v))
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
  ≡  @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) a b
   (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
     (@TotalOp_catd K (@Const_catd K A)) (@cstd_review_total_dual_projection K A (@cstd_review_inner_pullback K A B F H))
     x y p (Struct_sigma a u) (Struct_sigma b v) alpha);

// Projection retains its actual inner base arrow.
assertnot [K A : Cat] (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)))
 (alpha : τ (Hom
   (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
   (@fapp0
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) x)
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
     (@catd_transport_func (CoAbove2_cat K)
       (@cstd_review_total_dual_sigma K A G) x y p)
     (Struct_sigma a u))
   (Struct_sigma b v)))
 (q_other : τ (Obj (Hom_cat (TotalOp_cat A) a b))) ⊢
 @fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A G) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A G)
  x y p (Struct_sigma a u) (Struct_sigma b v)
   (Struct_sigma (sigma_Fst alpha) (sigma_Snd alpha))
 ≡ q_other;

// Whole-composite and capped-first orders of the ordinary Sigma-map law.
assert [K : Cat] (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 [x y : τ (Obj K)]
 (u : τ (Obj (Fibre_cat E x))) (v : τ (Obj (Fibre_cat E y)))
 (alpha : τ (Hom (@Sigma_cat K E) (Struct_sigma x u) (Struct_sigma y v))) ⊢
 @fapp1_fapp0 (@Sigma_cat K E) K
   (@comp_cat_fapp0 (@Sigma_cat K E) (@Sigma_cat K D) K
     (@Sigma_proj1_func K D) (@sigma_map_func K E D FF))
   (Struct_sigma x u) (Struct_sigma y v) alpha
 ≡ @fapp1_fapp0 (@Sigma_cat K E) K (@Sigma_proj1_func K E)
   (Struct_sigma x u) (Struct_sigma y v) alpha;

// The whole base-change composite retains the same actual F and source projection.
assert [A K : Cat] (F : τ (Functor A K)) (D : τ (Catd K))
 [x y : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@Pullback_catd A K D F) x)))
 (v : τ (Obj (Fibre_cat (@Pullback_catd A K D F) y)))
 (alpha : τ (Hom (@Sigma_cat A (@Pullback_catd A K D F))
   (Struct_sigma x u) (Struct_sigma y v))) ⊢
 @fapp1_fapp0 (@Sigma_cat A (@Pullback_catd A K D F)) K
   (@comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K D F)) (@Sigma_cat K D) K
     (@Sigma_proj1_func K D) (@sigma_pullback_total_func A K F D))
   (Struct_sigma x u) (Struct_sigma y v) alpha
 ≡ @fapp1_fapp0 A K F x y
   (@fapp1_fapp0 (@Sigma_cat A (@Pullback_catd A K D F)) A
     (@Sigma_proj1_func A (@Pullback_catd A K D F))
     (Struct_sigma x u) (Struct_sigma y v) alpha);

// First compare the same source projection before applying the base functor.
assert [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢ @eq_refl (Obj (Hom_cat (TotalOp_cat A) a b)) (@fapp1_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F))) (TotalOp_cat A)
  (@TotalOp_func (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)) A (@Sigma_proj1_func A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)))
  (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
  (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p) (Struct_sigma a u)) (Struct_sigma b v) alpha)
 : τ (@= (Obj (Hom_cat (TotalOp_cat A) a b)) (@fapp1_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F))) (TotalOp_cat A)
  (@TotalOp_func (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)) A (@Sigma_proj1_func A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)))
  (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
  (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p) (Struct_sigma a u)) (Struct_sigma b v) alpha) (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
     (@TotalOp_catd K (@Const_catd K A)) (@cstd_review_total_dual_projection K A (@cstd_review_inner_pullback K A B F H))
     x y p (Struct_sigma a u) (Struct_sigma b v) alpha));

// Map that existing comparison through the actual first Hom of TotalOp(F).
assert [K A B : Cat] (F : τ (Functor A B))
 (H : τ (Functor K (Functor_cart_cat B Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) (@cstd_review_inner_pullback K A B F H) y) b)))
 (alpha : τ (Hom (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
   (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
     (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p)
     (Struct_sigma a u)) (Struct_sigma b v))) ⊢ @eq_ap (Obj (Hom_cat (TotalOp_cat A) a b)) (Obj (Hom_cat (TotalOp_cat B) (@fapp0 A B F a) (@fapp0 A B F b)))
 (λ h : τ (Obj (Hom_cat (TotalOp_cat A) a b)), @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) a b h)
 (@fapp1_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F))) (TotalOp_cat A)
  (@TotalOp_func (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)) A (@Sigma_proj1_func A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)))
  (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
  (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p) (Struct_sigma a u)) (Struct_sigma b v) alpha)
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
     (@TotalOp_catd K (@Const_catd K A)) (@cstd_review_total_dual_projection K A (@cstd_review_inner_pullback K A B F H))
     x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
 (@eq_refl (Obj (Hom_cat (TotalOp_cat A) a b)) (@fapp1_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F))) (TotalOp_cat A)
  (@TotalOp_func (@Sigma_cat A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)) A (@Sigma_proj1_func A (@Pullback_catd A B (@fapp0 K (Functor_cart_cat B Cat_cart) H y) F)))
  (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y)
  (@catd_transport_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x y p) (Struct_sigma a u)) (Struct_sigma b v) alpha))
 : τ (@= (Obj (Hom_cat (TotalOp_cat B) (@fapp0 A B F a) (@fapp0 A B F b))) (
@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K B H)
  (@TotalOp_catd K (@Const_catd K B)) (@cstd_review_total_dual_projection K B H)
  x y p
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) x) (Fibre_cat (@cstd_review_total_dual_sigma K B H) x)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) x) (Struct_sigma a u))
 (@fapp0 (Fibre_cat (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) y) (Fibre_cat (@cstd_review_total_dual_sigma K B H) y)
  (@Fibre_func (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H) y) (Struct_sigma b v))
 (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H)) (@cstd_review_total_dual_sigma K B H) (@cstd_review_total_dual_basechange K A B F H)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
 ) ( @fapp1_fapp0 (TotalOp_cat A) (TotalOp_cat B) (@TotalOp_func A B F) a b
   (@fdapp1_int_hom_fapp0 (CoAbove2_cat K) (@cstd_review_total_dual_sigma K A (@cstd_review_inner_pullback K A B F H))
     (@TotalOp_catd K (@Const_catd K A)) (@cstd_review_total_dual_projection K A (@cstd_review_inner_pullback K A B F H))
     x y p (Struct_sigma a u) (Struct_sigma b v) alpha)));

// Source-frame congruence must not equate observations of unrelated arrows.
assertnot [K A : Cat] (G : τ (Functor K (Functor_cart_cat A Cat_cart)))
 [x y : τ (Obj K)] (p : τ (Hom (CoAbove2_cat K) x y))
 [a b : τ (Obj A)]
 (u : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G x) a)))
 (v : τ (Obj (Fibre_cat (@fapp0 K (Functor_cart_cat A Cat_cart) G y) b)))
 (alpha : τ (Hom
   (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
   (@fapp0
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) x)
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
     (@catd_transport_func (CoAbove2_cat K)
       (@cstd_review_total_dual_sigma K A G) x y p)
     (Struct_sigma a u))
   (Struct_sigma b v)))
 (beta : τ (Hom
   (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
   (@fapp0
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) x)
     (Fibre_cat (@cstd_review_total_dual_sigma K A G) y)
     (@catd_transport_func (CoAbove2_cat K)
       (@cstd_review_total_dual_sigma K A G) x y p)
     (Struct_sigma a u))
   (Struct_sigma b v)))
⊢ @eq_refl (Obj (Hom_cat (TotalOp_cat A) a b)) (@fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A G) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A G)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha)
 : τ (@= (Obj (Hom_cat (TotalOp_cat A) a b)) (@fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A G) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A G)
  x y p (Struct_sigma a u) (Struct_sigma b v) alpha) (@fdapp1_int_hom_fapp0 (CoAbove2_cat K)
  (@cstd_review_total_dual_sigma K A G) (@TotalOp_catd K (@Const_catd K A))
  (@cstd_review_total_dual_projection K A G)
  x y p (Struct_sigma a u) (Struct_sigma b v) beta));
