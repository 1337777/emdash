/* Naturally varying arrows with the corrected two-profile exchange.
   A default-lax eta:F⇒G produces oplax walking-arrow diagrams. The whole
   source/target/differential observations use ordinary-lax evaluation of
   those diagrams and recover F, G and eta through double exchange. */
require open emdash.emdash3_2_walking_arrow_introduction;
require open emdash.emdash3_2_diagram_evaluation;

// The same walking-diagram introduction followed by correctly profiled exchange.
symbol transf_arrow_diagram_func
  [K C : Cat] [F G : τ (Functor K C)] (eta : τ (@Transf K C F G))
  : τ (Functor K (Functor_oplax_cat WalkingArrow_cat C))
≔ @diagram_family_shape_func WalkingArrow_cat K C
    (@walking_arrow_func (Functor_cat K C) F G eta);

// Decode a single diagram object through the actual involutive duality.
// This is an object projection, not a same-profile map on all transformations.
symbol transf_arrow_diagram_at_func
  [K C : Cat] [F G : τ (Functor K C)]
  (eta : τ (@Transf K C F G)) (x : τ (Obj K))
  : τ (Functor WalkingArrow_cat C)
≔ @OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C)
    (@fapp0 K (Functor_oplax_cat WalkingArrow_cat C)
      (@transf_arrow_diagram_func K C F G eta) x);

// The former point-introduction comparison at its corrected semantic owner.
// Both Terminal domains identify the actual walking-arrow constructor.
// Existing point-introduction comparison after the whole duality join.
unif_rule
  @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) _ _ _
    (@join_elim_func Terminal_cat Terminal_cat _
      (@Const_func _ _ $F) (@Const_func _ _ $G) (@Const_func _ _ $eta))
    (@fapp0_func $K $C $x)
  ≡ @join_elim_func $A $B $E
      (@Const_func _ _ $Fx) (@Const_func _ _ $Gx) (@Const_func _ _ $etax)
  ↪ [ $A ≡ Terminal_cat; $B ≡ Terminal_cat; $E ≡ $C;
      $Fx ≡ @fapp0 $K $C $F $x; $Gx ≡ @fapp0 $K $C $G $x;
      $etax ≡ @tapp0_fapp0 $K $C $F $G $x $eta ];

// Encoded point counterpart of the ordinary walking-arrow comparison.
// Both terminal domains and the fixed evaluator retain the actual F,G,eta,x.
unif_rule
  @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) _ _ _
    (@OddDual_func _ _ (@join_elim_func Terminal_cat Terminal_cat _
      (@Const_func _ _ $F) (@Const_func _ _ $G) (@Const_func _ _ $eta)))
    (@OddDual_func _ _ (@fapp0_func $K $C $x))
  ≡ @OddDual_func $A0 $C0 (@join_elim_func $A $B $E
      (@Const_func _ _ $Fx) (@Const_func _ _ $Gx) (@Const_func _ _ $etax))
  ↪ [ $A0 ≡ WalkingArrow_cat; $C0 ≡ $C;
      $A ≡ Terminal_cat; $B ≡ Terminal_cat; $E ≡ $C;
      $Fx ≡ @fapp0 $K $C $F $x; $Gx ≡ @fapp0 $K $C $G $x;
      $etax ≡ @tapp0_fapp0 $K $C $F $G $x $eta ];

// Same point theorem on the decoded object; no equality data enters the graph.
symbol transf_arrow_diagram_point_path
  [K C : Cat] [F G : τ (Functor K C)]
  (eta : τ (@Transf K C F G)) (x : τ (Obj K))
  : τ (@= (Functor WalkingArrow_cat C)
      (@transf_arrow_diagram_at_func K C F G eta x)
      (@walking_arrow_func C (@fapp0 K C F x) (@fapp0 K C G x)
        (@tapp0_fapp0 K C F G x eta)))
≔ @eq_refl (Functor WalkingArrow_cat C) (@transf_arrow_diagram_at_func K C F G eta x);
