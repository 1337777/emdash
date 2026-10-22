/* The default conventional pre leg supports a whole proof-time comparison.
   Raw composition stays visible to intrinsic owners; guarded runtime folds
   and the post-leg/mixed profile boundaries are retained. */
require open emdash.emdash3_2_gray_profiles;

assert [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢
  @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y eta) (@tapp1_fapp0 A B F G X Y epsilon p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y eta) (@tapp1_fapp0 A B F G X Y epsilon p)) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta epsilon) p));

assertnot [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢
  @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X epsilon)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X epsilon)) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta epsilon) p));

assertnot [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢
  @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z eta q) (@tapp1_fapp0 A B F G X Y epsilon p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z eta q) (@tapp1_fapp0 A B F G X Y epsilon p)) (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H eta epsilon) (@comp_fapp0 A X Y Z q p)));

assert [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (V : τ (@LaxTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@lax_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) ≡ (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H (@lax_transfor A B G H V) epsilon) p);

assert [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (V : τ (@LaxTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@lax_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@lax_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H (@lax_transfor A B G H V) epsilon) p));

assert [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (V : τ (@StrictTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@strict_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) ≡ (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H (@strict_transfor A B G H V) epsilon) p);

assert [A B : Cat] [F G H : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) (V : τ (@StrictTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@strict_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y) (@tapp0_fapp0 A B G H Y (@strict_transfor A B G H V)) (@tapp1_fapp0 A B F G X Y epsilon p)) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H (@strict_transfor A B G H V) epsilon) p));

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X (@strict_transfor A B F G U))) ≡ (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta (@strict_transfor A B F G U)) p);

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X (@strict_transfor A B F G U))) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X (@strict_transfor A B F G U))) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta (@strict_transfor A B F G U)) p));

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (V : τ (@LaxTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@lax_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) ≡ (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H (@lax_transfor A B G H V) (@strict_transfor A B F G U)) (@comp_fapp0 A X Y Z q p));

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (V : τ (@LaxTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@lax_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@lax_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H (@lax_transfor A B G H V) (@strict_transfor A B F G U)) (@comp_fapp0 A X Y Z q p)));

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (V : τ (@StrictTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@strict_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) ≡ (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H (@strict_transfor A B G H V) (@strict_transfor A B F G U)) (@comp_fapp0 A X Y Z q p));

assert [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@StrictTransfor A B F G)) (V : τ (@StrictTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@strict_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@strict_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@strict_transfor A B F G U) p)) (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H (@strict_transfor A B G H V) (@strict_transfor A B F G U)) (@comp_fapp0 A X Y Z q p)));

assertnot [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@LaxTransfor A B F G)) (eta : τ (@Transf A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X (@lax_transfor A B F G U))) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Y)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G X) (@fapp0 A B H Y) (@tapp1_fapp0 A B G H X Y eta p) (@tapp0_fapp0 A B F G X (@lax_transfor A B F G U))) (@tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta (@lax_transfor A B F G U)) p));

assertnot [A B : Cat] [F G H : τ (Functor A B)] (U : τ (@LaxTransfor A B F G)) (V : τ (@LaxTransfor A B G H)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@lax_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@lax_transfor A B F G U) p)) : τ (@= (Hom B (@fapp0 A B F X) (@fapp0 A B H Z)) (@comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Z) (@tapp1_fapp0 A B G H Y Z (@lax_transfor A B G H V) q) (@tapp1_fapp0 A B F G X Y (@lax_transfor A B F G U) p)) (@tapp1_fapp0 A B F H X Z (@comp_fapp0 (Functor_cat A B) F G H (@lax_transfor A B G H V) (@lax_transfor A B F G U)) (@comp_fapp0 A X Y Z q p)));

// The raw forms remain distinct so intrinsic composite cuts keep their input.
assertnot [A B : Cat] [F G H : τ (Functor A B)]
  (epsilon : τ (@Transf A B F G)) (eta : τ (@Transf A B G H))
  [X Y : τ (Obj A)] (p : τ (Hom A X Y)) ⊢
  @comp_fapp0 B (@fapp0 A B F X) (@fapp0 A B G Y) (@fapp0 A B H Y)
    (@tapp0_fapp0 A B G H Y eta) (@tapp1_fapp0 A B F G X Y epsilon p)
  ≡ @tapp1_fapp0 A B F H X Y (@comp_fapp0 (Functor_cat A B) F G H eta epsilon) p;

// An opposite outer composition must not commute arbitrary loop components.
assertnot [A B : Cat] (z : τ (Obj B)) [X Y : τ (Obj A)] (p : τ (Hom A X Y))
  (epsilon eta : τ (@Transf A B (@Const_func A B z) (@Const_func A B z))) ⊢
  @eq_refl (Hom B z z)
    (@comp_fapp0 (Op_cat B) z z z
      (@tapp0_fapp0 A B (@Const_func A B z) (@Const_func A B z) Y eta)
      (@tapp1_fapp0 A B (@Const_func A B z) (@Const_func A B z) X Y epsilon p))
  : τ (@= (Hom B z z)
    (@comp_fapp0 (Op_cat B) z z z
      (@tapp0_fapp0 A B (@Const_func A B z) (@Const_func A B z) Y eta)
      (@tapp1_fapp0 A B (@Const_func A B z) (@Const_func A B z) X Y epsilon p))
    (@tapp1_fapp0 A B (@Const_func A B z) (@Const_func A B z) X Y
      (@comp_fapp0 (Functor_cat A B) (@Const_func A B z) (@Const_func A B z) (@Const_func A B z) eta epsilon) p));
