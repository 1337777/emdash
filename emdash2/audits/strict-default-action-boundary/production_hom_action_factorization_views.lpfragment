/* Next-Hom views of the two existing Hom_func factorizations.
   These are sufficient congruence/projection comparisons; all original
   endpoint arrows and both input objects are retained. No runtime fold. */
require open emdash.emdash3_2;

// The next-Hom projection now computes to pre-then-post whiskering.
// Compare its two complete existing factorizations at those stable owners.
// Shared arrows and all four derived endpoints remain explicit constraints;
// this is fixed whiskering, not interchange of two varying lax transforms.
// lhs-audit: keep 1 -- actual functor-composition category of both next-Hom factorizations.
unif_rule @comp_fapp0 Cat_cat _ _ _
    (@hom_postcomp_fapp1_func $A $A (@id Cat_cat $A) $x' $y $y' $f $qh $qk)
    (@hom_precomp_along_fapp1_func $A $A (@id Cat_cat $A) $y $x' $x $g $h $k)
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@hom_precomp_along_fapp1_func $A $A (@id Cat_cat $A) $y' $x' $x $g $ph $pk)
    (@hom_postcomp_fapp1_func $A $A (@id Cat_cat $A) $x $y $y' $f $h $k)
  ↪ [ $qh ≡ @hom_precomp_along_fapp0 $A $A (@id Cat_cat $A) $y $x' $x $g $h;
      $qk ≡ @hom_precomp_along_fapp0 $A $A (@id Cat_cat $A) $y $x' $x $g $k;
      $ph ≡ @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $x $y $y' $f $h;
      $pk ≡ @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $x $y $y' $f $k ];

// Raw Cat composition is the third presentation of the same rigid point.
// Keep the established left-associated functor-composition normal form.
unif_rule @Hom_fapp0 Cat_cat $A $B $E $C $D $V $F
  ≡ @comp_fapp0 Cat_cat $B $A $C
      (@comp_fapp0 Cat_cat $A $E $C $V $F) $D
  ↪ [ tt ≡ tt ];

// The identity middle functor erases one factor of the raw triple.
// This is the existing Hom middle-identity degeneration at its raw view.
unif_rule @Hom_fapp0 Cat_cat $A $B $A $C $D $V (@id Cat_cat $A)
  ≡ @comp_fapp0 Cat_cat $B $A $C $V $D
  ↪ [ tt ≡ tt ];
