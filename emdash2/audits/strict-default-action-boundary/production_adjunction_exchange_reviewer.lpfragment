// Existing opposite-profile exchange, retaining the original general H.
require open emdash.emdash3_2_diagram_evaluation;
assert [A B C : Cat] (H : τ (Functor A (Functor_cat B C))) (a : τ (Obj A)) ⊢
  @comp_cat_fapp0 B (Functor_oplax_cat A C) C
    (@diagram_oplax_evaluation_at_func A C a)
    (@diagram_family_shape_func A B C H)
  ≡ @fapp0 A (Functor_cat B C) H a;
assert [A B X Y : Cat] (H : τ (Functor A (Functor_cat B (Product_cat X Y)))) (a : τ (Obj A)) ⊢
  @comp_cat_fapp0 B (Functor_oplax_cat A (Product_cat X Y)) (Product_cat X Y)
    (@diagram_oplax_evaluation_at_func A (Product_cat X Y) a)
    (@diagram_family_shape_func A B (Product_cat X Y) H)
  ≡ @fapp0 A (Functor_cat B (Product_cat X Y)) H a;

// The original unrestricted H retains arbitrary subsequent whole Hom action.
type λ A : Cat, λ B : Cat, λ C : Cat, λ H : τ (Functor A (Functor_cat B C)),
  λ a : τ (Obj A), λ x : τ (Obj B), λ y : τ (Obj B),
  @fapp1_func B C
    (@comp_cat_fapp0 B (Functor_oplax_cat A C) C
      (@diagram_oplax_evaluation_at_func A C a)
      (@diagram_family_shape_func A B C H)) x y;

// Retain the direct Cartesian owner's original computation/reducibility controls.
// The selected sym_func owner is Cartesian; general lax exchange has a separate profile.
require open emdash.emdash3_2;

// Whole evaluation after exchange, before point application.
assert [A B C : Cat] (H : τ (Functor A (Functor_cart_cat B C))) (a : τ (Obj A)) ⊢
  @comp_cat_fapp0 B (Functor_cart_cat A C) C
    (@sym_fapp0_func (Functor_cart_cat A C) A C (@id_func (Functor_cart_cat A C)) a)
    (@sym_func A B C H)
  ≡ @fapp0 A (Functor_cart_cat B C) H a;

// Reducible Functor_cart_cat(A,X×Y) must not be a redundant identity guard.
assert [A B X Y : Cat] (H : τ (Functor A (Functor_cart_cat B (Product_cat X Y)))) (a : τ (Obj A)) ⊢
  @comp_cat_fapp0 B (Functor_cart_cat A (Product_cat X Y)) (Product_cat X Y)
    (@sym_fapp0_func (Functor_cart_cat A (Product_cat X Y)) A (Product_cat X Y)
      (@id_func (Functor_cart_cat A (Product_cat X Y))) a)
    (@sym_func A B (Product_cat X Y) H)
  ≡ @fapp0 A (Functor_cart_cat B (Product_cat X Y)) H a;

// The whole equality retains arbitrary subsequent Hom action.
type λ A : Cat, λ B : Cat, λ C : Cat, λ H : τ (Functor A (Functor_cart_cat B C)),
  λ a : τ (Obj A), λ x : τ (Obj B), λ y : τ (Obj B),
  @fapp1_func B C
    (@comp_cat_fapp0 B (Functor_cart_cat A C) C
      (@sym_fapp0_func (Functor_cart_cat A C) A C (@id_func (Functor_cart_cat A C)) a)
      (@sym_func A B C H)) x y;
