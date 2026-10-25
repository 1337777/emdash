/* API-04 feasibility candidate: no runtime or unification rules.
   Reuse the existing discrete-category path readback and its retraction.
   The discrete_functor_category model obligation remains explicit. */
require open emdash.emdash3_2_gray_profiles;
require open emdash.emdash3_2_discrete_functor_paths;

symbol discrete_cell_is_strict [C : Cat]
  (C0 : τ (IsDiscreteCat C)) [x y : τ (Obj C)]
  (cell : τ (Hom C x y)) : τ (@IsStrictCell C x y cell)
≔ Struct_sigma
    (@hom_to_path C C0 x y cell)
    (@eq_sym (Hom C x y)
      (@path_to_hom C x y (@hom_to_path C C0 x y cell)) cell
      (@path_to_hom_hom_to_path_path C C0 x y cell));

symbol functor_into_one_cat_is_strict [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  (F : τ (Functor A B)) : τ (@IsStrictFunctor A B F)
≔ λ X : τ (Obj A), λ Y : τ (Obj A), λ Z : τ (Obj A),
  λ g : τ (Hom A Y Z),
    @discrete_cell_is_strict
      (@Functor_cat (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
      (@discrete_functor_category
        (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z))
        (B1 (@fapp0 A B F X) (@fapp0 A B F Z)))
      (@strict_functor_compositor_lhs_func A B F X Y Z g)
      (@strict_functor_compositor_rhs_func A B F X Y Z g)
      (@strict_functor_compositor_transf A B F X Y Z g);

// The ordinary map itself is the default strict carrier.

assert [A B : Cat] (B1 : τ (IsNCat (cat_succ cat_zero) B))
  (F : τ (Functor A B)) ⊢
  F
  ≡ F;

assert [A B : Cat] (B1 : τ (IsNCat (cat_succ cat_zero) B))
  (F : τ (Functor A B)) (X : τ (Obj A)) ⊢
  @fapp0 A B (F) X
  ≡ @fapp0 A B F X;

// A discrete category is also a one-category. Transfer the discrete Path
// model along the already-derived, fixed-forward core Hom equivalence.
// This property proof introduces no runtime rule or extra caller witness.
symbol discrete_cat_is_one_cat [C : Cat] (C0 : τ (IsDiscreteCat C))
  : τ (IsNCat (cat_succ cat_zero) C)
≔ λ x : τ (Obj C), λ y : τ (Obj C),
  let A : Grpd ≔ @= (Obj C) x y in
  let P : Cat ≔ Path_cat A in
  let Q : Cat ≔ Hom_cat C x y in
  @ind_eq (Obj Cat_cat) Q P
    (@eq_sym (Obj Cat_cat) P Q
      (@omega_cast_to_object_path Cat_cat P Q
        (@omega_equiv_pack Cat_cat P Q (@core_incl_hom_func C x y)
          (@discrete_core_homwise C C0 x y))))
    (λ D : Cat, IsDiscreteCat D)
    (@discrete_cat_intro P
      (@prop_is_trunc_succ trunc_minus_one A ((@is_discrete_cat_obj_set C C0) x y))
      (@path_cat_is_groupoidal A));
