// Non-library native conformance for ordinary prewhiskering.
// Replay when the transferred precomposition ladder or composition definition changes.
require open emdash.emdash3_2;
symbol X : Cat;
symbol A : Cat;
symbol B : Cat;
symbol L : τ (Functor X A);
symbol F : τ (Functor A B);
symbol G : τ (Functor A B);
symbol eta : τ (@Transf A B F G);
symbol x : τ (Obj X);
symbol a : τ (Obj A);
symbol b : τ (Obj A);
symbol p : τ (Hom A a b);
symbol FL : τ (Functor X B) ≔ @comp_cat_fapp0 X A B F L;
symbol GL : τ (Functor X B) ≔ @comp_cat_fapp0 X A B G L;
symbol whiskered : τ (@Transf X B FL GL)
≔ @fapp0 (@Transf_cat A B F G) (@Transf_cat X B FL GL)
    (@comp_cat_con_fapp1_func X A B L F G) eta;
assert ⊢ @tapp0_fapp0 X B FL GL x whiskered
  ≡ @tapp0_fapp0 A B F G (@fapp0 X A L x) eta;
assertnot ⊢ @comp_fapp0 B (@fapp0 A B F a) (@fapp0 A B G a) (@fapp0 A B G b)
    (@fapp1_fapp0 A B G a b p) (@tapp0_fapp0 A B F G a eta)
  ≡ @comp_fapp0 B (@fapp0 A B F a) (@fapp0 A B F b) (@fapp0 A B G b)
    (@tapp0_fapp0 A B F G b eta) (@fapp1_fapp0 A B F a b p);
