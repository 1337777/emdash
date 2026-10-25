/*
  Reviewer example: the two-sided cubical internal hom and lax-arrow category
  are derived from ordinary Sigma, shifted total fibre duality, and homd_int.

  The canonical projection order is target edge, source edge, then the first
  side arrow.  The remaining Sigma-Hom object is (b,alpha), where

    alpha : b o u ==> v o a.

  No primitive cubical category, two-sided Sigma, square, rule, or unifier is
  introduced by the construction.
*/

require open emdash.emdash3_2_cubical_internalization;

// The internal owner is the existing homd_int of the total-dual inner
// edge family over O(K1).
assert [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart))) ⊢
  @homdc_int K1 K2 E
  ≡ @homd_int
      (TotalOp_cat K1)
      (@homdc_op_edge_catd K1 K2 E)
      (@homdc_op_edge_catd K1 K2 E)
      (@id_funcd
        (TotalOp_cat K1)
        (@homdc_op_edge_catd K1 K2 E));

// At a fixed first side arrow, total-duality cancellation gives the
// ordinary inner-total Hom. Its Sigma-Hom is the corrected negative total.
assert [K1 K2 : Cat]
  (E : τ (Functor (Op_cat K1) (Functor_cart_cat K2 Cat_cart)))
  (x1 y1 : τ (Obj K1))
  (x2 y2 : τ (Obj K2))
  (u : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1)
    x2)))
  (v : τ (Obj (Fibre_cat
    (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1)
    y2)))
  (a : τ (Hom K1 x1 y1)) ⊢
  @homdc_at K1 K2 E y1 y2 v x1 x2 u a
  ≡ Hom_cat
      (@Sigma_cat K2 (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1))
      (Struct_sigma x2 u)
      (Struct_sigma y2
        (@fapp0
          (Fibre_cat (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1) y2)
          (Fibre_cat (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1) y2)
          (@Fibre_func K2
            (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1)
            (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1)
            (@strict_transfor K2 Cat_cart
              (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1)
              (@fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E x1)
              (@fapp1_fapp0 (Op_cat K1) (Functor_cart_cat K2 Cat_cart) E y1 x1 a))
            y2)
          v));

// The selected ordinary specialization has the expected lax-square object.
assert [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2))
  (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1))
  (b : τ (Hom C x2 y2))
  (alpha : τ (Hom
    (Hom_cat C x1 y2)
    (@comp_fapp0 C x1 x2 y2 b u)
    (@comp_fapp0 C x1 y1 y2 v a))) ⊢
  @lax_square C x1 y1 x2 y2 u v a b alpha
  : τ (Hom
      (@LaxArrow_cat C)
      (@lax_edge C x1 x2 u)
      (@lax_edge C y1 y2 v));

// Both endpoint projections compute on edge objects.
assert [C : Cat]
  (x y : τ (Obj C))
  (u : τ (Hom C x y)) ⊢
  @fapp0
    (@LaxArrow_cat C)
    C
    (@homdc_total_source_func
      C C (@hom_int C C (@id_func C)))
    (@lax_edge C x y u)
  ≡ x;

assert [C : Cat]
  (x y : τ (Obj C))
  (u : τ (Hom C x y)) ⊢
  @fapp0
    (@LaxArrow_cat C)
    C
    (@homdc_total_target_func
      C C (@hom_int C C (@id_func C)))
    (@lax_edge C x y u)
  ≡ y;

// Source and target action compute to the two visible side arrows.
assert [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2))
  (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1))
  (b : τ (Hom C x2 y2))
  (alpha : τ (Hom
    (Hom_cat C x1 y2)
    (@comp_fapp0 C x1 x2 y2 b u)
    (@comp_fapp0 C x1 y1 y2 v a))) ⊢
  @fapp1_fapp0
    (@LaxArrow_cat C)
    C
    (@homdc_total_source_func
      C C (@hom_int C C (@id_func C)))
    (@lax_edge C x1 x2 u)
    (@lax_edge C y1 y2 v)
    (@lax_square C x1 y1 x2 y2 u v a b alpha)
  ≡ a;

assert [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2))
  (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1))
  (b : τ (Hom C x2 y2))
  (alpha : τ (Hom
    (Hom_cat C x1 y2)
    (@comp_fapp0 C x1 x2 y2 b u)
    (@comp_fapp0 C x1 y1 y2 v a))) ⊢
  @fapp1_fapp0
    (@LaxArrow_cat C)
    C
    (@homdc_total_target_func
      C C (@hom_int C C (@id_func C)))
    (@lax_edge C x1 x2 u)
    (@lax_edge C y1 y2 v)
    (@lax_square C x1 y1 x2 y2 u v a b alpha)
  ≡ b;

// The whole endpoint hom actions remain available for another dimension.
type @homdc_int;
type @homdc_total_source_func;
type @homdc_total_target_func;

// The corrected total rejects a filler pointing against the selected square.
assertnot [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2)) (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1)) (b : τ (Hom C x2 y2))
  (wrong : τ (Hom (Hom_cat C x1 y2)
    (@comp_fapp0 C x1 y1 y2 v a)
    (@comp_fapp0 C x1 x2 y2 b u))) ⊢
  Struct_sigma a (Struct_sigma b wrong)
  : τ (Hom (@LaxArrow_cat C)
      (@lax_edge C x1 x2 u) (@lax_edge C y1 y2 v));

// The actual forward filler is retained; two independent fillers do not
// become the same square when their side arrows agree.
assertnot [C : Cat]
  [x1 y1 x2 y2 : τ (Obj C)]
  (u : τ (Hom C x1 x2)) (v : τ (Hom C y1 y2))
  (a : τ (Hom C x1 y1)) (b : τ (Hom C x2 y2))
  (alpha beta : τ (Obj (@homdc_square_fibre C x1 y1 x2 y2 u v a b))) ⊢
  @lax_square C x1 y1 x2 y2 u v a b alpha
  ≡ @lax_square C x1 y1 x2 y2 u v a b beta;
