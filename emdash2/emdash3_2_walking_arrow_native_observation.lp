/* Whole ordinary-target native observation of walking-arrow diagrams.
   The existing evaluation transformation has an existing native arrow graph.
   This defined functor retains its complete action; no diagram inverse or
   faithfulness law is asserted here. The ordinary realization functor is
   separately owned by one_cat_arrow_diagrams. */
require open emdash.emdash3_2_gray_transformation_graph;
require open emdash.emdash3_2_diagram_evaluation;
require open emdash.emdash3_2_one_cat_transfor_profiles;

// Scoped proof-time evaluation after visible admission of identity exchange.
// The raw observation may already have reduced beyond its fapp1 head. Pass
// that same computed observation to the residual instead of matching an
// unevaluated RHS shape. No runtime decoding or arbitrary admission is added.
unif_rule
  @tapp0_fapp0 $A $C $F $G $d
    (@lax_transfor $A $C $F $G
      (@make_lax_transfor $A $C $F $G
        (@fapp1_fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j $u) _))
  ≡ $observed
  ↪ [ $A ≡ Functor_cat $I $C;
      @fapp1_fapp0 $I $C $d $i $j $u ≡ $observed ];

// General evaluation has the opposite transformation profile. Its admitted
// encoded lax view has the same component, without a general native-arrow
// graph or an ordinary-target assumption. Keep both runtime presentations.
unif_rule
  @tapp0_fapp0 $A $B $F $G $d
    (@lax_transfor $A $B $F $G
      (@make_lax_transfor $A $B $F $G
        (@diagram_evaluation_transf $I $C $i $j $u) _))
  ≡ $observed
  ↪ [ $A ≡ OddDual_cat (Functor_cat $I $C);
      $B ≡ OddDual_cat $C;
      $F ≡ @OddDual_func (Functor_cat $I $C) $C
        (@diagram_evaluation_at_func $I $C $j);
      $G ≡ @OddDual_func (Functor_cat $I $C) $C
        (@diagram_evaluation_at_func $I $C $i);
      @fapp1_fapp0 $I $C $d $i $j $u ≡ $observed ];

// The existing ordinary-target guard selects ordinary evaluation.
// Its native lax admission and subsequent graph keep the original interface.
symbol diagram_native_arrow_lax_transfor [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (@LaxTransfor (Functor_cat WalkingArrow_cat C) C
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
≔ @one_cat_lax_transfor (Functor_cat WalkingArrow_cat C) C C1
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
    (@one_cat_diagram_evaluation_transf WalkingArrow_cat C C1 walking_arrow_src walking_arrow_tgt walking_arrow_generator);

// The actual evaluation transformation, observed as a native arrow graph.
symbol diagram_native_arrow_func [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cat WalkingArrow_cat C) (@LaxArrow_cat C))
≔ @gray_transf_graph_func (Functor_cat WalkingArrow_cat C) C
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
    (@diagram_native_arrow_lax_transfor C C1);

// The arrow component is an observation of that same classified transfor.
symbol diagram_native_arrow_value [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (d : τ (Functor WalkingArrow_cat C))
  : τ (Hom C (@fapp0 WalkingArrow_cat C d walking_arrow_src)
      (@fapp0 WalkingArrow_cat C d walking_arrow_tgt))
≔ @tapp0_fapp0 (Functor_cat WalkingArrow_cat C) C
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
    (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d
    (@lax_transfor (Functor_cat WalkingArrow_cat C) C
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@diagram_native_arrow_lax_transfor C C1));

// Raw input observation is a path; the stable view keeps its profile.
symbol diagram_native_arrow_value_path [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (d : τ (Functor WalkingArrow_cat C))
  : τ (@= (Hom C (@fapp0 WalkingArrow_cat C d walking_arrow_src)
      (@fapp0 WalkingArrow_cat C d walking_arrow_tgt))
      (@diagram_native_arrow_value C C1 d)
      (@fapp1_fapp0 WalkingArrow_cat C d walking_arrow_src walking_arrow_tgt walking_arrow_generator))
≔ @eq_ap
    (@Transf (Functor_cat WalkingArrow_cat C) C
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt))
    (Hom C (@fapp0 WalkingArrow_cat C d walking_arrow_src)
      (@fapp0 WalkingArrow_cat C d walking_arrow_tgt))
    (λ e : τ (@Transf (Functor_cat WalkingArrow_cat C) C
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)),
      @tapp0_fapp0 (Functor_cat WalkingArrow_cat C) C
        (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
        (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d e)
    _ _ (@make_lax_transfor_carrier_path (Functor_cat WalkingArrow_cat C) C
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
      (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
      (@one_cat_diagram_evaluation_transf WalkingArrow_cat C C1 walking_arrow_src walking_arrow_tgt walking_arrow_generator)
      (@one_cat_pre_strict (Functor_cat WalkingArrow_cat C) C C1
        (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src)
        (@diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)
        (@one_cat_diagram_evaluation_transf WalkingArrow_cat C C1 walking_arrow_src walking_arrow_tgt walking_arrow_generator)));
