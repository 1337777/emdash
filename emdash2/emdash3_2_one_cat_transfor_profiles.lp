/* Whole ordinary-target transfor evidence from the existing two cells. */
require open emdash.emdash3_2_one_cat_functor_profiles;

symbol one_cat_post_strict [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@IsPostStrictTransfor A B F G epsilon)
≔ λ X : τ (Obj A), λ Y : τ (Obj A), λ Z : τ (Obj A),
  λ g : τ (Hom A Y Z),
    @discrete_cell_is_strict
      (Functor_cat (Hom_cat A X Y) (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z)))
      (@discrete_functor_category (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B G Z))
        (B1 (@fapp0 A B F X) (@fapp0 A B G Z)))
      (@strict_transfor_naturality_lhs_func A B F G epsilon X Y Z g)
      (@strict_transfor_naturality_rhs_func A B F G epsilon X Y Z g)
      (@strict_transfor_naturality_transf A B F G epsilon X Y Z g);

symbol one_cat_pre_strict [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@IsPreStrictTransfor A B F G epsilon)
≔ λ Y : τ (Obj A), λ W : τ (Obj A), λ X : τ (Obj A),
  λ h : τ (Hom A W X),
    @discrete_cell_is_strict
      (Functor_cat (Hom_cat A X Y) (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
      (@discrete_functor_category (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (B1 (@fapp0 A B F W) (@fapp0 A B G Y)))
      (@strict_transfor_pre_naturality_lhs_func A B F G epsilon Y W X h)
      (@strict_transfor_pre_naturality_rhs_func A B F G epsilon Y W X h)
      (@strict_transfor_pre_naturality_transf A B F G epsilon Y W X h);

symbol one_cat_transfor_is_strict [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@IsStrictTransfor A B F G epsilon)
≔ @strict_transfor_strictness_intro A B F G epsilon
    (@one_cat_post_strict A B B1 F G epsilon)
    (@one_cat_pre_strict A B B1 F G epsilon);

symbol one_cat_strict_transfor [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@StrictTransfor A B F G)
≔ @make_strict_transfor A B F G epsilon
    (@one_cat_transfor_is_strict A B B1 F G epsilon);

assert [A B : Cat] (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G)) ⊢
  @strict_transfor_underlying A B F G (@one_cat_strict_transfor A B B1 F G epsilon)
  ≡ epsilon;

// Ordinary target supplies the conventional pre/right admission as well.
symbol one_cat_lax_transfor [A B : Cat]
  (B1 : τ (IsNCat (cat_succ cat_zero) B))
  [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@LaxTransfor A B F G)
≔ @make_lax_transfor A B F G epsilon
    (@one_cat_pre_strict A B B1 F G epsilon);

// Structural ordinary-target comparison of the two mapping profiles.
// Under OneCat(C), every ordinary transfor has the existing strict admission.
// This declares the whole canonical comparison, not an inference of category
// equality from object coincidence. Keep both DefIso map heads for inversion.
injective symbol one_cat_mapping_comparison [A C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (@DefIso Cat_cat (Functor_cat A C) (Functor_cart_cat A C));

symbol one_cat_mapping_to_cart_func [A C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cat A C) (Functor_cart_cat A C))
≔ @defiso_to Cat_cat (Functor_cat A C) (Functor_cart_cat A C)
    (@one_cat_mapping_comparison A C C1);

symbol one_cat_mapping_from_cart_func [A C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor (Functor_cart_cat A C) (Functor_cat A C))
≔ @defiso_from Cat_cat (Functor_cat A C) (Functor_cart_cat A C)
    (@one_cat_mapping_comparison A C C1);

rule @fapp0 _ _ (@defiso_to _ _ _ (@one_cat_mapping_comparison _ _ _)) $F
  ↪ $F;
rule @fapp0 _ _ (@defiso_from _ _ _ (@one_cat_mapping_comparison _ _ _)) $F
  ↪ $F;

// The chosen inverse is the existing inclusion, at the whole-functor level.
// Keep this as a comparison so generic DefIso cancellation retains its owner.
unif_rule @defiso_from _ _ _ (@one_cat_mapping_comparison $A $C _)
  ≡ Functor_cart_include $A $C
  ↪ [ tt ≡ tt ];

// Read the classified action as the existing derived admission. Expanding
// its evidence in runtime rules makes critical-pair normalization enormous;
// the selected action stays stable and its ordinary view retains epsilon.
unif_rule @fapp1_fapp0 _ _
    (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C _)) $F $G $epsilon
  ≡ @make_strict_transfor $A $C $F $G $epsilon1 _
  ↪ [ $epsilon ≡ $epsilon1 ];
rule @fapp1_fapp0 _ _
    (@defiso_from _ _ _ (@one_cat_mapping_comparison $A $C _)) $F $G $U
  ↪ @strict_transfor $A $C $F $G $U;

rule @strict_transfor_underlying _ _ _ _
    (@fapp1_fapp0 _ _
      (@defiso_to _ _ _ (@one_cat_mapping_comparison _ _ _)) _ _ $epsilon)
  ↪ $epsilon;

// Direct whole ordinary reading after classified action has projected.
// As for make_strict_transfor, keep the strict view available at runtime.
unif_rule @strict_transfor _ _ _ _
    (@fapp1_fapp0 _ _
      (@defiso_to _ _ _ (@one_cat_mapping_comparison _ _ _)) _ _ $epsilon)
  ≡ $theta
  ↪ [ $theta ≡ $epsilon ];

// First-Hom projection of the two actual inverse laws. Expanding the
// composite's Hom action first otherwise loses the literal DefIso cut.
// Keep these whole comparisons scoped to this canonical comparison and
// retain both endpoint functors; no arbitrary admission/retraction law.
// lhs-audit: keep 1 -- composition of the two first-Hom functors is in Cat_cat.
unif_rule @comp_fapp0 Cat_cat _ _ _
    (@fapp1_func _ _
      (@defiso_from _ _ _ (@one_cat_mapping_comparison $A $C $C1)) $F $G)
    (@fapp1_func _ _
      (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C $C1)) $F $G)
  ≡ @id Cat_cat $H
  ↪ [ $H ≡ @Transf_cat $A $C $F $G ];

// lhs-audit: keep 1 -- the other inverse order has the Cartesian Hom target.
unif_rule @comp_fapp0 Cat_cat _ _ _
    (@fapp1_func _ _
      (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C $C1)) $F $G)
    (@fapp1_func _ _
      (@defiso_from _ _ _ (@one_cat_mapping_comparison $A $C $C1)) $F $G)
  ≡ @id Cat_cat $H
  ↪ [ $H ≡ Hom_cat (Functor_cart_cat $A $C) $F $G ];

// The same canonical inverse law after its inverse action has projected to
// the ordinary strict view. Keep the classified map U, not its certificate.
rule @fapp1_fapp0 _ _
    (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C _)) $F $G
    (@strict_transfor $A $C $F $G $U)
  ↪ $U;

// The two inverse laws under existing Cartesian postcomposition, after
// its first-Hom action caps. Whole postcomposition already cancels these
// exact to/from functors; these joins retain that result after projection.
// lhs-audit: keep 1,2,3,5,6 -- share the actual classifier endpoints with
// the primitive DefIso maps. Their values may already have distributed
// over a product; no reducible mapping expression is a pattern guard.
rule @hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
    $K $Raw $Cart
    (@defiso_to Cat_cat $Raw $Cart
      (@one_cat_mapping_comparison $A $C $C1)) _ _
    (@hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
      $K $Cart $Raw
      (@defiso_from Cat_cat $Raw $Cart
        (@one_cat_mapping_comparison $A $C $C1)) _ _ $U)
  ↪ $U;

// lhs-audit: keep 1,2,3,5,6 -- the reverse order needs the same SR guards.
rule @hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
    $K $Cart $Raw
    (@defiso_from Cat_cat $Raw $Cart
      (@one_cat_mapping_comparison $A $C $C1)) _ _
    (@hom_postcomp_fapp1_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart)
      $K $Raw $Cart
      (@defiso_to Cat_cat $Raw $Cart
        (@one_cat_mapping_comparison $A $C $C1)) _ _ $U)
  ↪ $U;

// Component beta of the canonical admission. Its whole strict view remains
// stable, while this actual observation returns the original component.
rule @tapp0_fapp0 _ _ _ _ $a
    (@strict_transfor _ _ _ _
      (@fapp1_fapp0 _ _
        (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C _)) $F $G $epsilon))
  ↪ @tapp0_fapp0 $A $C $F $G $a $epsilon;

// Existing inverse law after its inverse has been read as ordinary inclusion.
unif_rule @comp_fapp0 Cat_cat _ _ _ (Functor_cart_include $A $C)
    (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C $C1))
  ≡ @id Cat_cat $H
  ↪ [ $H ≡ Functor_cat $A $C ];

// Canonical admission preserves fixed-point evaluation as a whole functor.
// The literal mapping comparison supplies OneCat(C); its inverse and
// arbitrary raw/Cartesian mapping categories remain distinct.
rule @sym_fapp0_func _ _ _
    (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C _)) $a
  ↪ @fapp0_func $A $C $a;

// The same first-Hom projection when exchange has already projected.
// Its existing capped/component beta then reads the original transfor.
rule @sym_fapp0_fapp1_func _ _ _
    (@defiso_to _ _ _ (@one_cat_mapping_comparison $A $C _)) $a $F $G
  ↪ @tapp0_func $A $C $F $G $a;
