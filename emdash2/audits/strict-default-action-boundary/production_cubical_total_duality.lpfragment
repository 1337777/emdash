/*
  Two-sided internal Hom and lax-arrow total with corrected duality.

  The admitted whole nested family is
    E : T(K1) -> Cart(K2,Cat_cart).
  The fixed-endpoint homdc_ construction separately retains its broader
  E:T(K1)->Catd(K2) input. Here Cartesian parameter maps let the inner
  total retain the coefficient required by the native Homd construction:

    Edge_E = Sigma_coeff_func(K2) o E : T(K1) -> Cat_cart,
    D_E = TotalOp_catd(Edge_E) : O(K1) -> Cat_cart,
    homdc_int(E) = homd_int(id_D_E),
    homdc_total_cat(E) = O(Sigma_(O(K1)) D_E).

  T=Op_cat reverses dimension one, R=CoAbove2_cat reverses dimensions at
  least two, and O=TotalOp_cat=R(T(-)). The shifted base R(T(K1)) is O(K1).
  The root is the existing identity Homd of D_E. Its target/source/index
  leaf is read through O to recover

    Hom_(Edge_E[x1])((x2,u), Edge_E[a](y2,v)).

  Its corrected Sigma-Hom exposes the same object pair (b,alpha), where
    alpha : E[x1][b](u) -> E[a][y2](v).
  The local comparison is with this Hom, not the former same-base opposite
  of an ordinary inner total. No independent two-sided Sigma, square,
  category, rewrite or unification rule is introduced by this module.
*/

require open emdash.emdash3_2_cubical_square_total;

// Inner K2-total, varying contravariantly with x1.
symbol homdc_edge_catd
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Catd (Op_cat K1))
≔ @comp_cat_fapp0
    (Op_cat K1)
    (Functor_cart_cat K2 Cat_cart)
    Cat_cart
    (@Sigma_coeff_func K2)
    E;

// Total fibre duality shifts T(K1) to O(K1); it retains the existing
// inner total and supplies the admitted family of the native Homd root.
symbol homdc_op_edge_catd
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Catd (TotalOp_cat K1))
≔ @TotalOp_catd
    (Op_cat K1)
    (@homdc_edge_catd K1 K2 E);

// Whole two-sided internal hom, derived from the existing homd_int owner.
// The source is D_E, as required by the corrected identity Homd interface.
symbol homdc_int
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Functord
      (@homdc_op_edge_catd K1 K2 E)
      (@Homd_target_catd
        (TotalOp_cat K1)
        (@homdc_op_edge_catd K1 K2 E)))
≔ @homd_int
    (TotalOp_cat K1)
    (@homdc_op_edge_catd K1 K2 E)
    (@homdc_op_edge_catd K1 K2 E)
    (@id_funcd
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E));

// Final target-edge/source-edge/a projection.  Its objects are the remaining
// pairs (b,alpha).  Writing the final homd_ projection transparently preserves
// the same normal form selected by homdc_int's existing projection ladder.
symbol homdc_at
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  (y1 : τ (Obj K1))
  (y2 : τ (Obj K2))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1)
    y2)))
  (x1 : τ (Obj K1))
  (x2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1)
    x2)))
  (a : τ (Hom K1 x1 y1))
  : Cat
≔ TotalOp_cat (@fapp0
    (Op_cat (Hom_cat (TotalOp_cat K1) y1 x1))
    Cat_cart
    (@homd_
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E)
      (@homdc_op_edge_catd K1 K2 E)
      (@id_funcd
        (TotalOp_cat K1)
        (@homdc_op_edge_catd K1 K2 E))
      y1
      (Struct_sigma y2 v)
      x1
      (Struct_sigma x2 u))
    a);

// Variance-correct two-sided Grothendieck total.  This is a transparent
// nested Sigma/opposite expression, not a primitive TwoSidedSigma theory.
symbol homdc_total_cat
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : Cat
≔ TotalOp_cat
    (@Sigma_cat
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E));

// Constructor-visible object (x1,(x2,u)) of the derived total.
symbol homdc_total_obj
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  (x1 : τ (Obj K1))
  (x2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1)
    x2)))
  : τ (Obj (@homdc_total_cat K1 K2 E))
≔ Struct_sigma x1 (Struct_sigma x2 u);

// First endpoint projection: opposite of the outer Sigma projection.
symbol homdc_total_source_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Functor (@homdc_total_cat K1 K2 E) K1)
≔ @TotalOp_func
    (@Sigma_cat
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E))
    (TotalOp_cat K1)
    (@Sigma_proj1_func
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E));

// Total-dual Cartesian inner projection over the shifted base O(K1).
symbol homdc_total_target_funcd
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Hom (Functor_cart_cat (TotalOp_cat K1) Cat_cart)
      (@homdc_op_edge_catd K1 K2 E)
      (@Const_catd (TotalOp_cat K1) (TotalOp_cat K2)))
≔ @TotalOp_funcd
    (Op_cat K1)
    (@homdc_edge_catd K1 K2 E)
    (@Const_catd (Op_cat K1) K2)
    (@sigma_proj1_family_funcd (Op_cat K1) K2 E);

// Totalize that displayed projection and retain only its K2 coordinate.
symbol homdc_total_target_underlying_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Functor
      (@Sigma_cat
        (TotalOp_cat K1)
        (@homdc_op_edge_catd K1 K2 E))
      (TotalOp_cat K2))
≔ @comp_cat_fapp0
    (@Sigma_cat
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E))
    (Product_cat (TotalOp_cat K1) (TotalOp_cat K2))
    (TotalOp_cat K2)
    (@Product_projR_func (TotalOp_cat K1) (TotalOp_cat K2))
    (@sigma_map_func
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E)
      (@Const_catd (TotalOp_cat K1) (TotalOp_cat K2))
      (@strict_transfor _ _ _ _ (@homdc_total_target_funcd K1 K2 E)));

// Second endpoint projection. Generic fapp1 retains its whole arrow action;
// the varying-Sigma projection owner computes constructor-visible square
// action to the second side arrow.
symbol homdc_total_target_func
  [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  : τ (Functor (@homdc_total_cat K1 K2 E) K2)
≔ @TotalOp_func
    (@Sigma_cat
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E))
    (TotalOp_cat K2)
    (@homdc_total_target_underlying_func K1 K2 E);

// Selected ordinary lax-arrow specialization.
symbol LaxArrow_cat
  (C : Cat)
  : Cat
≔ @homdc_total_cat
    C C
    (@hom_int C C (@id_func C));

symbol lax_edge
  [C : Cat]
  (x y : τ (Obj C))
  (u : τ (Hom C x y))
  : τ (Obj (@LaxArrow_cat C))
≔ @homdc_total_obj
    C C
    (@hom_int C C (@id_func C))
    x y u;

// Constructor-visible lax square.  The same nested pair is supplied by the
// generic Hom of homdc_total_cat; alpha is not a postulated square owner.
symbol lax_square
  [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2))
  (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1))
  (b : τ (Hom C x2 y2))
  (alpha : τ (Obj
    (@homdc_fibre
      C C
      (@hom_int_view C C (@id_func C))
      x1 y1 x2 y2 u v a b)))
  : τ (Hom
      (@LaxArrow_cat C)
      (@lax_edge C x1 x2 u)
      (@lax_edge C y1 y2 v))
≔ Struct_sigma a (Struct_sigma b alpha);
