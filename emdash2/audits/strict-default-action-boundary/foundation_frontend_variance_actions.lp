// Non-library conformance consumer for the shared frontend variance actions.
// Status and replay boundary: foundation_frontend_pathind_internalized_review.md.
require open emdash.emdash3_2;
symbol A : Cat;
symbol B : Cat;
symbol F : τ (Functor A B);
symbol R : τ (Functor B A);
symbol x : τ (Obj A);
symbol y : τ (Obj A);
symbol p : τ (Hom A y x);
symbol u : τ (Obj B);
symbol v : τ (Obj B);
symbol q : τ (Hom B v u);
symbol left_hom : τ (Functor (Hom_cat A y x) (Hom_cat B (@fapp0 A B F y) (@fapp0 A B F x)))
≔ @fapp1_func (Op_cat A) (Op_cat B) (@Op_func A B F) x y;
symbol right_hom : τ (Functor (Hom_cat A y x) (Hom_cat B (@fapp0 A B F y) (@fapp0 A B F x)))
≔ @fapp1_func A B F y x;
assert ⊢ left_hom ≡ right_hom;
symbol left_arrow : τ (Hom B (@fapp0 A B F y) (@fapp0 A B F x))
≔ @fapp1_fapp0 (Op_cat A) (Op_cat B) (@Op_func A B F) x y p;
symbol right_arrow : τ (Hom B (@fapp0 A B F y) (@fapp0 A B F x))
≔ @fapp1_fapp0 A B F y x p;
assert ⊢ left_arrow ≡ right_arrow;
symbol left_precomp : τ (Functor (Hom_cat A (@fapp0 B A R u) x) (Hom_cat A (@fapp0 B A R v) x))
≔ @fapp1_fapp0 (Op_cat B) Cat_cart (@hom_con A x B R) u v q;
symbol right_precomp : τ (Functor (Hom_cat A (@fapp0 B A R u) x) (Hom_cat A (@fapp0 B A R v) x))
≔ @hom_precomp_along_func B A R x v u q;
assert ⊢ left_precomp ≡ right_precomp;
assertnot ⊢ left_hom : τ (Functor (Hom_cat A x y) (Hom_cat B (@fapp0 A B F x) (@fapp0 A B F y)));
