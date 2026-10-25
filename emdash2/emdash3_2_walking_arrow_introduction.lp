/*
  An ordinary arrow, presented as a functor out of the existing walking arrow.

  The join cross datum is a constant section of a represented Hom family,
  not a new primitive arrow or a supplied commuting square. Ordinary
  generator action computes by the join recursor's whole cross beta.
  This module does not yet internalize variation of the supplied arrow and
  both endpoints into a whole inverse to diagram evaluation.
*/
require open emdash.emdash3_2_walking_arrow;

// Transparent internally natural cross datum selecting f at the terminal pair.
symbol walking_arrow_cross
  [C : Cat] [x y : τ (Obj C)] (f : τ (Hom C x y))
  : τ (Obj (@Prof_transf_cat
      C Terminal_cat C Terminal_cat
      (@Terminal_prof Terminal_cat Terminal_cat)
      (@Obj_func C x) (@Unit_prof C) (@Obj_func C y)))
≔ @Const_func (Product_cat (Op_cat Terminal_cat) Terminal_cat)
    (Hom_cat C x y) f;

// Transparent join-recursion introduction: [1] → C, sending 0→1 to f.
symbol walking_arrow_func
  [C : Cat] [x y : τ (Obj C)] (f : τ (Hom C x y))
  : τ (Functor WalkingArrow_cat C)
≔ @join_elim_func Terminal_cat Terminal_cat C
    (@Obj_func C x) (@Obj_func C y) (@walking_arrow_cross C x y f);

// Postcomposition of the free walking-arrow introduction. A strict functor
// maps its two endpoints and its generator; the result is the same join
// constructor. This cut is independent of ordinary-target admissions.
// lhs-audit: keep 1 -- composition of functors at this constructor cut.
rule @comp_fapp0 Cat_cat _ _ $D $H
    (@join_elim_func Terminal_cat Terminal_cat $C
      (@Const_func _ _ $x) (@Const_func _ _ $y) (@Const_func _ _ $f))
  ↪ @walking_arrow_func $D
      (@fapp0 $C $D $H $x) (@fapp0 $C $D $H $y)
      (@fapp1_fapp0 $C $D $H $x $y $f);

// Cartesian evaluation of that same constructor. The cross datum is an
// actual strict transformation; evaluating it gives the generator of the
// resulting walking-arrow functor. This replaces the former proof-time
// Cartesian point comparison with its constructor computation.
rule @sym_fapp0_func _ $K $C
    (@join_elim_func Terminal_cat Terminal_cat _
      (@Const_func _ _ $F) (@Const_func _ _ $G) (@Const_func _ _ $U)) $x
  ↪ @walking_arrow_func $C
      (@fapp0 $K $C $F $x) (@fapp0 $K $C $G $x)
      (@tapp0_fapp0 $K $C $F $G $x (@strict_transfor $K $C $F $G $U));
