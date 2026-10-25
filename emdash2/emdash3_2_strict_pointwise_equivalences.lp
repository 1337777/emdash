/*
  Inherited pointwise-to-whole fixed-forward equivalence assembly.

  This module takes an existing whole ordinary Transf or displayed Transfd
  and pointwise OmegaEquivAlong evidence. It declares whole left and right
  inverse transformations, preserves both selected component inverse choices
  through beta rules, and assumes whole cancellation paths.

  The historical strict_* names do not impose an IsStrictTransfor premise.
  Assembly is a primitive assumption of the selected integration baseline,
  not a derivation from strict or lax naturality. Its interpretation is not
  established merely by the downstream checks; explicit-profile replacement
  research is deferred separately.

  Consumers supply no new component naturality square. This interface does
  not turn an arbitrary family of arrows into a transformation, identify all
  pointwise-equal functors, or add runtime extensionality or univalence.
*/

require open emdash.emdash3_2;
require open emdash.emdash3_2_gray_profiles;
require open emdash.emdash3_2_eq1_evidence_property;

// Fixed-forward pointwise equivalence evidence for one whole transformation.
symbol StrictTransfPointwiseOmegaAlong
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  : Grpd
≔ @Pi_grpd
    (Obj A)
    (λ x : τ (Obj A),
      @OmegaEquivAlong
        B
        (@fapp0 A B F x)
        (@fapp0 A B G x)
        (@tapp0_fapp0 A B F G x eta));

// Whole left inverse assembled from the selected component inverses.
injective symbol strict_transf_pointwise_left_inverse
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@Transf A B G F);

rule @tapp0_fapp0 _ _ _ _ $x
      (@strict_transf_pointwise_left_inverse $A $B $F $G $eta $u)
  ↪ @omega_equiv_along_left_inv
      $B
      (@fapp0 $A $B $F $x)
      (@fapp0 $A $B $G $x)
      (@tapp0_fapp0 $A $B $F $G $x $eta)
      ($u $x);

// Whole right inverse assembled from the selected component inverses.
injective symbol strict_transf_pointwise_right_inverse
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@Transf A B G F);

rule @tapp0_fapp0 _ _ _ _ $x
      (@strict_transf_pointwise_right_inverse $A $B $F $G $eta $u)
  ↪ @omega_equiv_along_right_inv
      $B
      (@fapp0 $A $B $F $x)
      (@fapp0 $A $B $G $x)
      (@tapp0_fapp0 $A $B $F $G $x $eta)
      ($u $x);

/*
  Primitive whole cancellation assembly.  These are generic strict-
  transformation structure, necessitated by the primitive `Transf`
  classifier; they are not consumer-supplied coherence and do not compute on
  arbitrary component families.
*/
constant symbol strict_transf_pointwise_left_law
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@=
      (Hom (@Functor_cat A B) F F)
      (@comp_fapp0
        (@Functor_cat A B)
        F G F
        (@strict_transf_pointwise_left_inverse A B F G eta u)
        eta)
      (@id (@Functor_cat A B) F));

constant symbol strict_transf_pointwise_right_law
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@=
      (Hom (@Functor_cat A B) G G)
      (@comp_fapp0
        (@Functor_cat A B)
        G F G
        eta
        (@strict_transf_pointwise_right_inverse A B F G eta u))
      (@id (@Functor_cat A B) G));

// Whole fixed-forward equivalence selected by strict pointwise evidence.
symbol strict_transf_pointwise_omega_along
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@OmegaEquivAlong (@Functor_cat A B) F G eta)
≔ @omega_equiv_along_intro
    (@Functor_cat A B)
    F G eta
    (@strict_transf_pointwise_left_inverse A B F G eta u)
    (@strict_transf_pointwise_right_inverse A B F G eta u)
    (@strict_transf_pointwise_left_law A B F G eta u)
    (@strict_transf_pointwise_right_law A B F G eta u);

// Equality observation obtained from the whole fixed-forward equivalence.
symbol strict_transf_pointwise_path
  [A B : Cat]
  [F G : τ (@Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@= (Obj (@Functor_cat A B)) F G)
≔ @omega_cast_to_object_path
    (@Functor_cat A B)
    F G
    (@omega_equiv_pack
      (@Functor_cat A B)
      F G eta
      (@strict_transf_pointwise_omega_along A B F G eta u));

// Derived Cartesian assembly for a classified strict forward map.
// The original ordinary inverse choices and whole laws are retained.
// Their extracted-cell strictness and the Cartesian cancellation laws
// are proved below; no further assembly principle is supplied.

// Transport a property of the identity along the original whole inverse law.
// No component law of u[x] is substituted for that whole path.
symbol inverse_left_unit_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@IsStrictTransfor A B F F
      (@comp_fapp0 (Functor_cat A B) F G F
        (@strict_transf_pointwise_left_inverse A B F G eta u) eta))
≔ @ind_eq (@Transf A B F F)
    (@comp_fapp0 (Functor_cat A B) F G F
      (@strict_transf_pointwise_left_inverse A B F G eta u) eta)
    (@id (Functor_cat A B) F)
    (@strict_transf_pointwise_left_law A B F G eta u)
    (λ alpha : τ (@Transf A B F F), @IsStrictTransfor A B F F alpha)
    (@strict_transfor_is_strict A B F F (@id (Functor_cart_cat A B) F));

symbol inverse_right_unit_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  : τ (@IsStrictTransfor A B G G
      (@comp_fapp0 (Functor_cat A B) G F G eta
        (@strict_transf_pointwise_right_inverse A B F G eta u)))
≔ @ind_eq (@Transf A B G G)
    (@comp_fapp0 (Functor_cat A B) G F G eta
      (@strict_transf_pointwise_right_inverse A B F G eta u))
    (@id (Functor_cat A B) G)
    (@strict_transf_pointwise_right_law A B F G eta u)
    (λ alpha : τ (@Transf A B G G), @IsStrictTransfor A B G G alpha)
    (@strict_transfor_is_strict A B G G (@id (Functor_cart_cat A B) G));

// The post/left field really constrains the composite's extracted whole cell.
symbol inverse_left_composite_post_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@Transf A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G eta))
  (X : τ (Obj A)) [Y Z : τ (Obj A)] (g : τ (Hom A Y Z))
  : τ (@IsStrictCell
      (Functor_cat (Hom_cat A X Y)
        (Hom_cat B (@fapp0 A B F X) (@fapp0 A B F Z)))
      (@strict_transfor_naturality_lhs_func A B F F
        (@comp_fapp0 (Functor_cat A B) F G F
          (@strict_transf_pointwise_left_inverse A B F G eta u) eta) X Y Z g)
      (@strict_transfor_naturality_rhs_func A B F F
        (@comp_fapp0 (Functor_cat A B) F G F
          (@strict_transf_pointwise_left_inverse A B F G eta u) eta) X Y Z g)
      (@strict_transfor_naturality_transf A B F F
        (@comp_fapp0 (Functor_cat A B) F G F
          (@strict_transf_pointwise_left_inverse A B F G eta u) eta) X Y Z g))
≔ (@strict_transfor_post_evidence A B F F
      (@comp_fapp0 (Functor_cat A B) F G F
        (@strict_transf_pointwise_left_inverse A B F G eta u) eta)
      (@inverse_left_unit_is_strict A B F G eta u)) X Y Z g;

// Functoriality of the existing path-image property. The agreement field
// follows by mapping the original agreement and the native Core action law.
symbol strict_cell_fmap
  [C D : Cat] (F : τ (Functor C D))
  [x y : τ (Obj C)] (cell : τ (Hom C x y))
  (e : τ (@IsStrictCell C x y cell))
  : τ (@IsStrictCell D (@fapp0 C D F x) (@fapp0 C D F y)
      (@fapp1_fapp0 C D F x y cell))
≔ let p : τ (@= (Obj C) x y) ≔ @strict_cell_path C x y cell e in
  @Struct_sigma
    (@= (Obj D) (@fapp0 C D F x) (@fapp0 C D F y))
    (λ q : τ (@= (Obj D) (@fapp0 C D F x) (@fapp0 C D F y)),
      @= (Hom D (@fapp0 C D F x) (@fapp0 C D F y))
        (@fapp1_fapp0 C D F x y cell)
        (@path_to_hom D (@fapp0 C D F x) (@fapp0 C D F y) q))
    (@eq_ap (Obj C) (Obj D) (λ z : τ (Obj C), @fapp0 C D F z) x y p)
    (@eq_trans (Hom D (@fapp0 C D F x) (@fapp0 C D F y))
      (@fapp1_fapp0 C D F x y cell)
      (@fapp1_fapp0 C D F x y (@path_to_hom C x y p))
      (@path_to_hom D (@fapp0 C D F x) (@fapp0 C D F y)
        (@eq_ap (Obj C) (Obj D) (λ z : τ (Obj C), @fapp0 C D F z) x y p))
      (@eq_ap (Hom C x y) (Hom D (@fapp0 C D F x) (@fapp0 C D F y))
        (λ c : τ (Hom C x y), @fapp1_fapp0 C D F x y c)
        cell (@path_to_hom C x y p) (@strict_cell_agreement C x y cell e))
      (@path_to_hom_fapp1_agrees C D F x y p));

// Reflect the same property through an actual equivalence. Its selected
// left inverse and whole cancellation path supply the proof. No new inverse,
// Core reflection axiom, or runtime equality payload is introduced.
symbol strict_cell_reflect_equivalence
  [C D : Cat] (F : τ (Functor C D))
  (u : τ (@OmegaEquivAlong Cat_cat C D F))
  [x y : τ (Obj C)] (cell : τ (Hom C x y))
  (image : τ (@IsStrictCell D (@fapp0 C D F x) (@fapp0 C D F y)
      (@fapp1_fapp0 C D F x y cell)))
  : τ (@IsStrictCell C x y cell)
≔ let L : τ (Functor D C) ≔ @omega_equiv_along_left_inv Cat_cat C D F u in
  @ind_eq (Functor C C)
    (@id_func C) (@comp_cat_fapp0 C D C L F)
    (@eq_sym (Functor C C) (@comp_cat_fapp0 C D C L F) (@id_func C)
      (@omega_equiv_along_left_law Cat_cat C D F u))
    (λ H : τ (Functor C C),
      @IsStrictCell C (@fapp0 C C H x) (@fapp0 C C H y)
        (@fapp1_fapp0 C C H x y cell))
    (@strict_cell_fmap D C L (@fapp0 C D F x) (@fapp0 C D F y)
      (@fapp1_fapp0 C D F x y cell) image);

// Typed whole computation view for vertical composition with a strict
// earlier transfor. This uses the selected whole view at the original owner;
// it is not inferred from the legacy scalar beta rules alone.
// This readable view is a defined composite, not another action constructor.
symbol strict_left_internal_composite_view
  [A B : Cat] [F G H : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (xi : τ (@Transf A B G H)) (X : τ (Obj A))
  : τ (@Functord A (@hom_ A A (@id_func A) X)
      (@hom_ B A H (@fapp0 A B F X)))
≔ @comp_catd_fapp0 A (@hom_ A A (@id_func A) X)
    (@hom_ B A H (@fapp0 A B G X)) (@hom_ B A H (@fapp0 A B F X))
    (@strict_transfor A Cat_cart _ _
      (@hom_int_precomp_func B A H (@fapp0 A B G X) (@fapp0 A B F X)
        (@tapp0_fapp0 A B F G X (@strict_transfor A B F G eta))))
    (@tapp1_at_transf A B G H X xi);

symbol strict_left_internal_composite_path
  [A B : Cat] [F G H : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (xi : τ (@Transf A B G H)) (X : τ (Obj A))
  : τ (@= (@Functord A
      (@hom_ A A (@id_func A) X)
      (@hom_ B A H (@fapp0 A B F X)))
    (@tapp1_at_transf A B F H X
      (@comp_fapp0 (Functor_cat A B) F G H xi
        (@strict_transfor A B F G eta)))
    (@strict_left_internal_composite_view A B F G H eta xi X))
≔ @eq_refl (@Functord A
    (@hom_ A A (@id_func A) X)
    (@hom_ B A H (@fapp0 A B F X)))
    (@tapp1_at_transf A B F H X
      (@comp_fapp0 (Functor_cat A B) F G H xi
        (@strict_transfor A B F G eta)));

// Its first projection is a whole functor in the retained source arrow.
symbol strict_left_internal_component_path
  [A B : Cat] [F G H : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (xi : τ (@Transf A B G H)) (X Y : τ (Obj A))
  : τ (@= (Functor (Hom_cat A X Y)
      (Hom_cat B (@fapp0 A B F X) (@fapp0 A B H Y)))
    (@tapp1_func A B F H X Y
      (@comp_fapp0 (Functor_cat A B) F G H xi (@strict_transfor A B F G eta)))
    (@comp_cat_fapp0 _ _ _
      (@hom_precomp_along_func B B (@id_func B) (@fapp0 A B H Y)
        (@fapp0 A B F X) (@fapp0 A B G X)
        (@tapp0_fapp0 A B F G X (@strict_transfor A B F G eta)))
      (@tapp1_func A B G H X Y xi)))
≔ @eq_ap
    (@Functord A (@hom_ A A (@id_func A) X) (@hom_ B A H (@fapp0 A B F X)))
    (Functor (Hom_cat A X Y) (Hom_cat B (@fapp0 A B F X) (@fapp0 A B H Y)))
    (λ FF : τ (@Functord A (@hom_ A A (@id_func A) X) (@hom_ B A H (@fapp0 A B F X))),
      @tapp0_fapp0 A Cat_cart _ _ Y FF)
    (@tapp1_at_transf A B F H X
      (@comp_fapp0 (Functor_cat A B) F G H xi (@strict_transfor A B F G eta)))
    (@strict_left_internal_composite_view A B F G H eta xi X)
    (@strict_left_internal_composite_path A B F G H eta xi X);

// The original whole cancellation path constrains the represented composite.
// This transports a proof, not a replacement comparison cell or inverse map.
symbol inverse_represented_composite_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G
      (@strict_transfor A B F G eta)))
  (X : τ (Obj A))
  : τ (@IsStrictFunctord A
      (@hom_ A A (@id_func A) X)
      (@hom_ B A F (@fapp0 A B F X))
      (@strict_left_internal_composite_view A B F G F eta
        (@strict_transf_pointwise_left_inverse A B F G
          (@strict_transfor A B F G eta) u) X))
≔ let xi : τ (@Transf A B G F) ≔ @strict_transf_pointwise_left_inverse A B F G
      (@strict_transfor A B F G eta) u in
  let alpha : τ (@Transf A B F F) ≔ @comp_fapp0 (Functor_cat A B) F G F
      xi (@strict_transfor A B F G eta) in
  let S : τ (Catd A) ≔ @hom_ A A (@id_func A) X in
  let D : τ (Catd A) ≔ @hom_ B A F (@fapp0 A B F X) in
  let view : τ (@Functord A S D) ≔ @strict_left_internal_composite_view A B F G F eta xi X in
  @ind_eq (@Functord A S D) view (@tapp1_at_transf A B F F X alpha)
    (@eq_sym (@Functord A S D) (@tapp1_at_transf A B F F X alpha) view
      (@strict_left_internal_composite_path A B F G F eta xi X))
    (λ FF : τ (@Functord A S D), @IsStrictFunctord A S D FF)
    ((@strict_transfor_post_evidence A B F F alpha
      (@inverse_left_unit_is_strict A B F G (@strict_transfor A B F G eta) u)) X);

// Fixed precomposition reflects the chosen scalar equivalence. Contravariance
// swaps the two inverse choices; neither is replaced or reconstructed.
symbol represented_precomp_equivalence
  [B : Cat] [P Q : τ (Obj B)] (e : τ (Hom B P Q))
  (u : τ (@OmegaEquivAlong B P Q e)) (Z : τ (Obj B))
  : τ (@OmegaEquivAlong Cat_cat (Hom_cat B Q Z) (Hom_cat B P Z)
      (@hom_precomp_along_func B B (@id_func B) Z P Q e))
≔ @omega_equiv_along_intro Cat_cat (Hom_cat B Q Z) (Hom_cat B P Z)
    (@hom_precomp_along_func B B (@id_func B) Z P Q e)
    (@hom_precomp_along_func B B (@id_func B) Z Q P
      (@omega_equiv_along_right_inv B P Q e u))
    (@hom_precomp_along_func B B (@id_func B) Z Q P
      (@omega_equiv_along_left_inv B P Q e u))
    (@eq_ap (Hom B Q Q) (Functor (Hom_cat B Q Z) (Hom_cat B Q Z))
      (λ a : τ (Hom B Q Q), @hom_precomp_along_func B B (@id_func B) Z Q Q a)
      (@comp_fapp0 B Q P Q e (@omega_equiv_along_right_inv B P Q e u))
      (@id B Q) (@omega_equiv_along_right_law B P Q e u))
    (@eq_ap (Hom B P P) (Functor (Hom_cat B P Z) (Hom_cat B P Z))
      (λ a : τ (Hom B P P), @hom_precomp_along_func B B (@id_func B) Z P P a)
      (@comp_fapp0 B P Q P (@omega_equiv_along_left_inv B P Q e u) e)
      (@id B P) (@omega_equiv_along_left_law B P Q e u));

// Fixed postcomposition acts on ordinary lax mapping categories. Only the
// supplied whole unit paths are mapped; no joint Cartesian action on two
// varying lax transformations or stronger coefficient universe is asserted.
symbol fixed_postcomp_equivalence
  (S : Cat) [C D : Cat] (F : τ (Functor C D))
  (u : τ (@OmegaEquivAlong Cat_cat C D F))
  : τ (@OmegaEquivAlong Cat_cat (Functor_cat S C) (Functor_cat S D)
      (@hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S C D F))
≔ @omega_equiv_along_intro Cat_cat (Functor_cat S C) (Functor_cat S D)
    (@hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S C D F)
    (@hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S D C
      (@omega_equiv_along_left_inv Cat_cat C D F u))
    (@hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S D C
      (@omega_equiv_along_right_inv Cat_cat C D F u))
    (@eq_ap (Functor C C) (Functor (Functor_cat S C) (Functor_cat S C))
      (λ V : τ (Functor C C),
        @hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S C C V)
      (@comp_cat_fapp0 C D C (@omega_equiv_along_left_inv Cat_cat C D F u) F)
      (@id_func C) (@omega_equiv_along_left_law Cat_cat C D F u))
    (@eq_ap (Functor D D) (Functor (Functor_cat S D) (Functor_cat S D))
      (λ V : τ (Functor D D),
        @hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S D D V)
      (@comp_cat_fapp0 D C D F (@omega_equiv_along_right_inv Cat_cat C D F u))
      (@id_func D) (@omega_equiv_along_right_law Cat_cat C D F u));

// Positive obligation: the extracted cell after canonical represented
// precomposition must be the actual functorial image of the original cell.
// The source map L remains general lax; e is a retained arrow of B.
symbol represented_precomp_laxity_path
  [K B : Cat] (H : τ (Functor K B))
  (P Q : τ (Obj B)) (e : τ (Hom B P Q))
  (E : τ (Catd K))
  (L : τ (@Functord K E (@hom_ B K H Q)))
  [x y : τ (Obj K)] (p : τ (Hom K x y))
  : let M : τ (Catd K) ≔ @hom_ B K H Q in
    let D : τ (Catd K) ≔ @hom_ B K H P in
    let A : τ (@Functord K M D) ≔ @strict_transfor K Cat_cart M D
      (@hom_int_precomp_func B K H Q P e) in
    let C : τ (@Functord K E D) ≔ @comp_catd_fapp0 K E M D A L in
    let S : Cat ≔ @Fibre_cat K E x in
    let Mx : Cat ≔ @Fibre_cat K M x in
    let Ey : Cat ≔ @Fibre_cat K E y in
    let My : Cat ≔ @Fibre_cat K M y in
    let Dy : Cat ≔ @Fibre_cat K D y in
    let Hy : τ (Functor My Dy) ≔
      @hom_precomp_along_func B B (@id_func B) (@fapp0 K B H y) P Q e in
    let sourceL : τ (Functor S My) ≔
      @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S Mx My
        (@catd_transport_func K M x y p) (@Fibre_func K E M L x) in
    let targetL : τ (Functor S My) ≔
      @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S Ey My
        (@Fibre_func K E M L y) (@catd_transport_func K E x y p) in
    let sourceC : τ (Functor S Dy) ≔ @comp_cat_fapp0 S Mx Dy
      (@Hom_func B Q P (@fapp0 K B H x) (@fapp0 K B H y) e (@fapp1_fapp0 K B H x y p))
      (@Fibre_func K E M L x) in
    let targetC : τ (Functor S Dy) ≔
      @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S My Dy Hy targetL in
    let post : τ (Functor (Functor_cat S My) (Functor_cat S Dy)) ≔
      @hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S My Dy Hy in
    τ (@= (@Transf S Dy sourceC targetC)
      (@functord_laxity_transf K E D C x y p)
      (@fapp1_fapp0 (Functor_cat S My) (Functor_cat S Dy) post
        sourceL targetL
        (@functord_laxity_transf K E M L x y p)))
≔ let M : τ (Catd K) ≔ @hom_ B K H Q in
  let D : τ (Catd K) ≔ @hom_ B K H P in
  let A : τ (@Functord K M D) ≔ @strict_transfor K Cat_cart M D
    (@hom_int_precomp_func B K H Q P e) in
  let C : τ (@Functord K E D) ≔ @comp_catd_fapp0 K E M D A L in
  let S : Cat ≔ @Fibre_cat K E x in
  let Mx : Cat ≔ @Fibre_cat K M x in
  let Ey : Cat ≔ @Fibre_cat K E y in
  let My : Cat ≔ @Fibre_cat K M y in
  let Dy : Cat ≔ @Fibre_cat K D y in
  let targetL : τ (Functor S My) ≔
    @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S Ey My
      (@Fibre_func K E M L y) (@catd_transport_func K E x y p) in
  @eq_refl (@Transf S Dy
      (@comp_cat_fapp0 S Mx Dy
        (@Hom_func B Q P (@fapp0 K B H x) (@fapp0 K B H y) e (@fapp1_fapp0 K B H x y p))
        (@Fibre_func K E M L x))
      (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S My Dy
        (@hom_precomp_along_func B B (@id_func B) (@fapp0 K B H y) P Q e) targetL))
    (@functord_laxity_transf K E D C x y p);

// Cancel the actual represented equivalence in the whole extracted cell.
// The only premise is strictness of the existing composite, already obtained
// from its original whole cancellation law at the inverse consumer.
symbol represented_precomp_reflect_strictness
  [K B : Cat] (H : τ (Functor K B))
  [P Q : τ (Obj B)] (e : τ (Hom B P Q))
  (equiv : τ (@OmegaEquivAlong B P Q e))
  (E : τ (Catd K)) (L : τ (@Functord K E (@hom_ B K H Q)))
  (strict : τ (@IsStrictFunctord K E (@hom_ B K H P)
    (@comp_catd_fapp0 K E (@hom_ B K H Q) (@hom_ B K H P)
      (@strict_transfor K Cat_cart _ _ (@hom_int_precomp_func B K H Q P e)) L)))
  : τ (@IsStrictFunctord K E (@hom_ B K H Q) L)
≔ λ x : τ (Obj K), λ y : τ (Obj K), λ p : τ (Hom K x y),
  let M : τ (Catd K) ≔ @hom_ B K H Q in
  let D : τ (Catd K) ≔ @hom_ B K H P in
  let S : Cat ≔ @Fibre_cat K E x in
  let Mx : Cat ≔ @Fibre_cat K M x in
  let My : Cat ≔ @Fibre_cat K M y in
  let Ey : Cat ≔ @Fibre_cat K E y in
  let Dy : Cat ≔ @Fibre_cat K D y in
  let Hy : τ (Functor My Dy) ≔
    @hom_precomp_along_func B B (@id_func B) (@fapp0 K B H y) P Q e in
  let sourceL : τ (Functor S My) ≔
    @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S Mx My
      (@catd_transport_func K M x y p) (@Fibre_func K E M L x) in
  let targetL : τ (Functor S My) ≔
    @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S Ey My
      (@Fibre_func K E M L y) (@catd_transport_func K E x y p) in
  let C : τ (@Functord K E D) ≔ @comp_catd_fapp0 K E M D
    (@strict_transfor K Cat_cart M D (@hom_int_precomp_func B K H Q P e)) L in
  let sourceC : τ (Functor S Dy) ≔ @comp_cat_fapp0 S Mx Dy
    (@Hom_func B Q P (@fapp0 K B H x) (@fapp0 K B H y) e (@fapp1_fapp0 K B H x y p))
    (@Fibre_func K E M L x) in
  let targetC : τ (Functor S Dy) ≔
    @hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) S My Dy Hy targetL in
  let post : τ (Functor (Functor_cat S My) (Functor_cat S Dy)) ≔
    @hom_postcomp_func Cat_cat Cat_cat (@id_func Cat_cat) S My Dy Hy in
  let image : τ (@Transf S Dy sourceC targetC) ≔
    @fapp1_fapp0 (Functor_cat S My) (Functor_cat S Dy) post sourceL targetL
      (@functord_laxity_transf K E M L x y p) in
  let image_strict : τ (@IsStrictCell (Functor_cat S Dy) sourceC targetC image) ≔
    @ind_eq (@Transf S Dy sourceC targetC)
      image (@functord_laxity_transf K E D C x y p)
      (@eq_sym (@Transf S Dy sourceC targetC)
        (@functord_laxity_transf K E D C x y p) image
        (@represented_precomp_laxity_path K B H P Q e E L x y p))
      (λ cell : τ (@Transf S Dy sourceC targetC),
        @IsStrictCell (Functor_cat S Dy) sourceC targetC cell)
      (strict x y p) in
  @strict_cell_reflect_equivalence
    (Functor_cat S My) (Functor_cat S Dy)
    post
    (@fixed_postcomp_equivalence S My Dy Hy
      (@represented_precomp_equivalence B P Q e equiv (@fapp0 K B H y)))
    sourceL targetL (@functord_laxity_transf K E M L x y p)
    image_strict;

// Apply reflection to the inherited inverse. No new inverse is selected and
// the component evidence is exactly u[X], with its original two choices.
symbol strict_inverse_is_post_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G
    (@strict_transfor A B F G eta)))
  : τ (@IsPostStrictTransfor A B G F
    (@strict_transf_pointwise_left_inverse A B F G
      (@strict_transfor A B F G eta) u))
≔ λ X : τ (Obj A),
  @represented_precomp_reflect_strictness A B F
    (@fapp0 A B F X) (@fapp0 A B G X)
    (@tapp0_fapp0 A B F G X (@strict_transfor A B F G eta))
    (u X) (@hom_ A A (@id_func A) X)
    (@tapp1_at_transf A B G F X
      (@strict_transf_pointwise_left_inverse A B F G
        (@strict_transfor A B F G eta) u))
    (@inverse_represented_composite_is_strict A B F G eta u X);

// The selected conventional default already makes the pre/right leg strict.
symbol conventional_transfor_is_pre_strict
  [A B : Cat] [F G : τ (Functor A B)] (epsilon : τ (@Transf A B F G))
  : τ (@IsPreStrictTransfor A B F G epsilon)
≔ λ Y : τ (Obj A), λ W : τ (Obj A), λ X : τ (Obj A),
  λ h : τ (Hom A W X),
  Struct_sigma
    (@eq_refl
      (Functor (Hom_cat A X Y) (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y)))
      (@strict_transfor_pre_naturality_lhs_func A B F G epsilon Y W X h))
    (@eq_refl
      (@Transf (Hom_cat A X Y) (Hom_cat B (@fapp0 A B F W) (@fapp0 A B G Y))
        (@strict_transfor_pre_naturality_lhs_func A B F G epsilon Y W X h)
        (@strict_transfor_pre_naturality_rhs_func A B F G epsilon Y W X h))
      (@strict_transfor_pre_naturality_transf A B F G epsilon Y W X h));

symbol strict_inverse_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G
    (@strict_transfor A B F G eta)))
  : τ (@IsStrictTransfor A B G F
    (@strict_transf_pointwise_left_inverse A B F G
      (@strict_transfor A B F G eta) u))
≔ @strict_transfor_strictness_intro A B G F
    (@strict_transf_pointwise_left_inverse A B F G (@strict_transfor A B F G eta) u)
    (@strict_inverse_is_post_strict A B F G eta u)
    (@conventional_transfor_is_pre_strict A B G F
      (@strict_transf_pointwise_left_inverse A B F G (@strict_transfor A B F G eta) u));

// The existing inverse-uniqueness theorem compares the two original whole
// choices. Transporting the proved property retains the chosen right inverse.
symbol strict_right_inverse_is_strict
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G
    (@strict_transfor A B F G eta)))
  : τ (@IsStrictTransfor A B G F
    (@strict_transf_pointwise_right_inverse A B F G
      (@strict_transfor A B F G eta) u))
≔ let forward : τ (@Transf A B F G) ≔ @strict_transfor A B F G eta in
  let linv : τ (@Transf A B G F) ≔ @strict_transf_pointwise_left_inverse A B F G forward u in
  let rinv : τ (@Transf A B G F) ≔ @strict_transf_pointwise_right_inverse A B F G forward u in
  @ind_eq (@Transf A B G F) rinv linv
    (@eq_sym (@Transf A B G F) linv rinv
      (@omega_equiv_candidate_left_to_right (Functor_cat A B) F G forward linv rinv
        (@strict_transf_pointwise_left_law A B F G forward u)
        (@strict_transf_pointwise_right_law A B F G forward u)))
    (λ inverse : τ (@Transf A B G F), @IsStrictTransfor A B G F inverse)
    (@strict_inverse_is_strict A B F G eta u);

// Classified views of the same maps, through the existing admission owner.
symbol pointwise_cart_left_inverse
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G (@strict_transfor A B F G eta)))
  : τ (@StrictTransfor A B G F)
≔ @make_strict_transfor A B G F
    (@strict_transf_pointwise_left_inverse A B F G (@strict_transfor A B F G eta) u)
    (@strict_inverse_is_strict A B F G eta u);

symbol pointwise_cart_right_inverse
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G (@strict_transfor A B F G eta)))
  : τ (@StrictTransfor A B G F)
≔ @make_strict_transfor A B G F
    (@strict_transf_pointwise_right_inverse A B F G (@strict_transfor A B F G eta) u)
    (@strict_right_inverse_is_strict A B F G eta u);

// Equality lifts between actual admitted constructors. Evidence choice is
// already unobservable; equality induction supplies the comparison of maps.
symbol strict_transfor_admission_path
  [A B : Cat] [F G : τ (Functor A B)]
  (epsilon theta : τ (@Transf A B F G))
  (pe : τ (@IsStrictTransfor A B F G epsilon))
  (pt : τ (@IsStrictTransfor A B F G theta))
  (path : τ (@= (@Transf A B F G) epsilon theta))
  : τ (@= (@StrictTransfor A B F G)
    (@make_strict_transfor A B F G epsilon pe)
    (@make_strict_transfor A B F G theta pt))
≔ (@ind_eq (@Transf A B F G) epsilon theta path
    (λ eta : τ (@Transf A B F G),
      @Pi_grpd (@IsStrictTransfor A B F G eta)
        (λ s : τ (@IsStrictTransfor A B F G eta),
          @= (@StrictTransfor A B F G)
            (@make_strict_transfor A B F G eta s)
            (@make_strict_transfor A B F G theta pt)))
    (λ s : τ (@IsStrictTransfor A B F G theta),
      @eq_refl (@StrictTransfor A B F G) (@make_strict_transfor A B F G theta pt))) pe;

// The required consumer is the actual Cartesian composite and identity,
// rather than only their separately admitted ordinary presentations.
symbol pointwise_cart_left_law
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G (@strict_transfor A B F G eta)))
  : τ (@= (Hom (Functor_cart_cat A B) F F)
    (@comp_fapp0 (Functor_cart_cat A B) F G F
      (@pointwise_cart_left_inverse A B F G eta u) eta)
    (@id (Functor_cart_cat A B) F))
≔ let forward : τ (@Transf A B F G) ≔ @strict_transfor A B F G eta in
  @strict_transfor_admission_path A B F F
    (@comp_fapp0 (Functor_cat A B) F G F
      (@strict_transf_pointwise_left_inverse A B F G forward u) forward)
    (@id (Functor_cat A B) F)
    (@inverse_left_unit_is_strict A B F G forward u)
    (@strict_transfor_is_strict A B F F (@id (Functor_cart_cat A B) F))
    (@strict_transf_pointwise_left_law A B F G forward u);

symbol pointwise_cart_right_law
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G (@strict_transfor A B F G eta)))
  : τ (@= (Hom (Functor_cart_cat A B) G G)
    (@comp_fapp0 (Functor_cart_cat A B) G F G
      eta (@pointwise_cart_right_inverse A B F G eta u))
    (@id (Functor_cart_cat A B) G))
≔ let forward : τ (@Transf A B F G) ≔ @strict_transfor A B F G eta in
  @strict_transfor_admission_path A B G G
    (@comp_fapp0 (Functor_cat A B) G F G
      forward (@strict_transf_pointwise_right_inverse A B F G forward u))
    (@id (Functor_cat A B) G)
    (@inverse_right_unit_is_strict A B F G forward u)
    (@strict_transfor_is_strict A B G G (@id (Functor_cart_cat A B) G))
    (@strict_transf_pointwise_right_law A B F G forward u);

symbol pointwise_cart_omega_along
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (@StrictTransfor A B F G))
  (u : τ (@StrictTransfPointwiseOmegaAlong A B F G (@strict_transfor A B F G eta)))
  : τ (@OmegaEquivAlong (Functor_cart_cat A B) F G eta)
≔ @omega_equiv_along_intro (Functor_cart_cat A B) F G eta
    (@pointwise_cart_left_inverse A B F G eta u)
    (@pointwise_cart_right_inverse A B F G eta u)
    (@pointwise_cart_left_law A B F G eta u)
    (@pointwise_cart_right_law A B F G eta u);

// Displayed fixed-forward pointwise evidence over one whole transformation.
// The actual Cat_cart fibre Hom is Cartesian: retain the forward cell
// and both chosen inverse components in that same coefficient.
// Whole assembly remains the inherited primitive assumption above.
symbol StrictTransfdPointwiseOmegaAlong
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  : Grpd
≔ @Pi_grpd
    (Obj K)
    (λ x : τ (Obj K),
      @OmegaEquivAlong
        (@Functor_cart_cat
          (@Fibre_cat K E x)
          (@Fibre_cat K D x))
        (@Fibre_func K E D FF x)
        (@Fibre_func K E D GG x)
        (@tdapp0_fapp0 K E D FF GG x eta));

// Whole displayed left inverse with selected fibre components.
injective symbol strict_transfd_pointwise_left_inverse
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  (u : τ (@StrictTransfdPointwiseOmegaAlong K E D FF GG eta))
  : τ (@Transfd K E D GG FF);

rule @tdapp0_fapp0 _ _ _ _ _ $x
      (@strict_transfd_pointwise_left_inverse
        $K $E $D $FF $GG $eta $u)
  ↪ @omega_equiv_along_left_inv
      (@Functor_cart_cat
        (@Fibre_cat $K $E $x)
        (@Fibre_cat $K $D $x))
      (@Fibre_func $K $E $D $FF $x)
      (@Fibre_func $K $E $D $GG $x)
      (@tdapp0_fapp0 $K $E $D $FF $GG $x $eta)
      ($u $x);

// Whole displayed right inverse with selected fibre components.
injective symbol strict_transfd_pointwise_right_inverse
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  (u : τ (@StrictTransfdPointwiseOmegaAlong K E D FF GG eta))
  : τ (@Transfd K E D GG FF);

rule @tdapp0_fapp0 _ _ _ _ _ $x
      (@strict_transfd_pointwise_right_inverse
        $K $E $D $FF $GG $eta $u)
  ↪ @omega_equiv_along_right_inv
      (@Functor_cart_cat
        (@Fibre_cat $K $E $x)
        (@Fibre_cat $K $D $x))
      (@Fibre_func $K $E $D $FF $x)
      (@Fibre_func $K $E $D $GG $x)
      (@tdapp0_fapp0 $K $E $D $FF $GG $x $eta)
      ($u $x);

// Generic whole cancellation assembly for displayed transformations.
constant symbol strict_transfd_pointwise_left_law
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  (u : τ (@StrictTransfdPointwiseOmegaAlong K E D FF GG eta))
  : τ (@=
      (Hom (@Functord_cat K E D) FF FF)
      (@comp_fapp0
        (@Functord_cat K E D)
        FF GG FF
        (@strict_transfd_pointwise_left_inverse K E D FF GG eta u)
        eta)
      (@id (@Functord_cat K E D) FF));

constant symbol strict_transfd_pointwise_right_law
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  (u : τ (@StrictTransfdPointwiseOmegaAlong K E D FF GG eta))
  : τ (@=
      (Hom (@Functord_cat K E D) GG GG)
      (@comp_fapp0
        (@Functord_cat K E D)
        GG FF GG
        eta
        (@strict_transfd_pointwise_right_inverse K E D FF GG eta u))
      (@id (@Functord_cat K E D) GG));

// Whole displayed fixed-forward equivalence.
symbol strict_transfd_pointwise_omega_along
  [K : Cat]
  [E D : τ (@Catd K)]
  [FF GG : τ (@Functord K E D)]
  (eta : τ (@Transfd K E D FF GG))
  (u : τ (@StrictTransfdPointwiseOmegaAlong K E D FF GG eta))
  : τ (@OmegaEquivAlong (@Functord_cat K E D) FF GG eta)
≔ @omega_equiv_along_intro
    (@Functord_cat K E D)
    FF GG eta
    (@strict_transfd_pointwise_left_inverse K E D FF GG eta u)
    (@strict_transfd_pointwise_right_inverse K E D FF GG eta u)
    (@strict_transfd_pointwise_left_law K E D FF GG eta u)
    (@strict_transfd_pointwise_right_law K E D FF GG eta u);
