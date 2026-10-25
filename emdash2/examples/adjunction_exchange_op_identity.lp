// General family, exchanged through the existing opposite transformation profile.
require open emdash.emdash3_2_diagram_evaluation;
assert [A B C : Cat] (H : τ (Functor A (Functor_cat (TotalOp_cat B) C))) (b : τ (Obj B)) ⊢
  @diagram_family_transf A (TotalOp_cat B) C H b b (@id B b)
  ≡ @id (Functor_oplax_cat A C)
      (@OddDual_func A C (@diagram_family_at_func A (TotalOp_cat B) C H b));
assert [A B C : Cat] (H : τ (Functor A (Functor_cat (TotalOp_cat B) C))) (b : τ (Obj B)) ⊢
  @fapp1_fapp0 (TotalOp_cat B) (Functor_oplax_cat A C)
    (@diagram_family_shape_func A (TotalOp_cat B) C H) b b (@id (TotalOp_cat B) b)
  ≡ @id (Functor_oplax_cat A C)
      (@OddDual_func A C (@diagram_family_at_func A (TotalOp_cat B) C H b));
assert [A B C : Cat] (H : τ (Functor A (Functor_cat (TotalOp_cat B) C))) (b : τ (Obj B)) (a : τ (Obj A)) ⊢
  @tapp0_fapp0 _ _ _ _ a (@diagram_family_transf A (TotalOp_cat B) C H b b (@id B b))
  ≡ @id C (@fapp0 (TotalOp_cat B) C (@fapp0 A (Functor_cat (TotalOp_cat B) C) H a) b);
assertnot [A B C : Cat] (H : τ (Functor A (Functor_cat (TotalOp_cat B) C))) (b : τ (Obj B)) (q : τ (Hom (TotalOp_cat B) b b)) ⊢
  @diagram_family_transf A (TotalOp_cat B) C H b b q
  ≡ @id (Functor_oplax_cat A C)
      (@OddDual_func A C (@diagram_family_at_func A (TotalOp_cat B) C H b));

// The direct Cartesian owner retains its own erased-identity and noncollapse checks.
// The selected sym_func owner is Cartesian; general lax exchange has a separate profile.
/* Source identity normalization must not erase the exchanged-action cut. */
require open emdash.emdash3_2;
assert [A B C : Cat] (H : τ (Functor A (Functor_cart_cat (TotalOp_cat B) C))) (b : τ (Obj B)) ⊢
  @sym_tapp1_fapp0_transf A (TotalOp_cat B) C H b b (@id B b)
  ≡ @id (Functor_cart_cat A C) (@sym_fapp0_func A (TotalOp_cat B) C H b);
assert [A B C : Cat] (H : τ (Functor A (Functor_cart_cat (TotalOp_cat B) C))) (b : τ (Obj B)) ⊢
  @fapp1_fapp0 (TotalOp_cat B) (Functor_cart_cat A C) (@sym_func A (TotalOp_cat B) C H) b b (@id (TotalOp_cat B) b)
  ≡ @id (Functor_cart_cat A C) (@sym_fapp0_func A (TotalOp_cat B) C H b);
assert [A B C : Cat] (H : τ (Functor A (Functor_cart_cat (TotalOp_cat B) C))) (b : τ (Obj B)) (a : τ (Obj A)) ⊢
  @tapp0_fapp0 A C (@sym_fapp0_func A (TotalOp_cat B) C H b) (@sym_fapp0_func A (TotalOp_cat B) C H b) a (@strict_transfor A C (@sym_fapp0_func A (TotalOp_cat B) C H b) (@sym_fapp0_func A (TotalOp_cat B) C H b) (@sym_tapp1_fapp0_transf A (TotalOp_cat B) C H b b (@id B b)))
  ≡ @id C (@fapp0 (TotalOp_cat B) C (@fapp0 A (Functor_cart_cat (TotalOp_cat B) C) H a) b);
assertnot [A B C : Cat] (H : τ (Functor A (Functor_cart_cat (TotalOp_cat B) C))) (b : τ (Obj B)) (q : τ (Hom (TotalOp_cat B) b b)) ⊢
  @sym_tapp1_fapp0_transf A (TotalOp_cat B) C H b b q
  ≡ @id (Functor_cart_cat A C) (@sym_fapp0_func A (TotalOp_cat B) C H b);
