/* Proof-time constant postcomposition at the canonical Cat horizontal head.
   Constants use their existing strict-transformation inclusion.
   General second-component lax action is not a constant-postcomposition case.
   No arbitrary pointwise extensionality or new functoriality axiom is added. */
require open emdash.emdash3_2_diagram_evaluation;

// Existing Cat-level postcomposition on a constant transformation.
// The identity second component distinguishes this from general horizontal action.
// lhs-audit: keep 1 -- the Cat horizontal-action carrier is the actual discriminator
unif_rule @comp_prod_fapp1_fapp0 Cat_cat $K $A $B
    (@Struct_sigma _ _ (@Const_func $K $A $x) $F)
    (@Struct_sigma _ _ (@Const_func $K $A $y) $F)
    (@Struct_sigma _ _ (@strict_transfor _ _ _ _ (@Const_transf $K $A $x $y $f)) (@id _ $F))
  ≡ @strict_transfor _ _ _ _ (@Const_transf $K1 $B1 $u $v $g)
  ↪ [ $K1 ≡ $K; $B1 ≡ $B;
      $u ≡ (@fapp0 $A $B $F $x); $v ≡ (@fapp0 $A $B $F $y);
      $g ≡ (@fapp1_fapp0 $A $B $F $x $y $f) ];

// The fixed-precomposition view of F o const(x) has the same whole constant
// value as raw Cat composition. Keep the stable action head at runtime;
// compare the exterior categories and actual F[x] at proof time.
// lhs-audit: keep 1,2,3 -- Cat/id selects ordinary represented composition
unif_rule @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $C $K $A (@Const_func _ _ $x) $F
  ≡ @Const_func $K1 $C1 $y
  ↪ [ $K1 ≡ $K; $C1 ≡ $C; $y ≡ (@fapp0 $A $C $F $x) ];
