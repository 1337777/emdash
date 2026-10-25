/* Native represented-comma classification of a whole internal Hom action.
   The shared graph accepts Θ:Hom_K(−,−)⇒Hom_Y(JA−,D−). The original Γ
   interface supplies the native Hom action of h:J∘A⇒D. No objectwise square
   is caller data. Both interfaces retain the same projection inverse data.
   Protected helpers retain the original internal graph derivation. The whole
   target comparison is qualified for OneCat(Y); higher Op/profile repair
   remains outside this module. All declarations here are definitions. */

require open emdash.emdash3_2_gray_transformation_graph;

require open emdash.emdash3_2_zero_arrow_cones;

require open emdash.emdash3_2_iso_evidence_constructors;

require open emdash.emdash3_2_one_cat_adjunction_family_views;

require open emdash.emdash3_2_one_cat_pointwise_equivalences;
require open emdash.emdash3_2_one_cat_op;

require open emdash.emdash3_2_omega_equiv_composition;

require open emdash.emdash3_2_transfor_whiskering;
require open emdash.emdash3_2_identity_presented_iso_mapping;

// The inner total families are Cartesian; their ordinary views are used
// separately by the original internal-action input. Total fibre duality
// shifts the outer base from T(B) to O(B).
protected symbol comma_graph_source_raw_catd [B : Cat]
  : τ (Catd (Op_cat B))
≔ @homdc_edge_catd B B (@hom_int B B (@id_func B));

protected symbol comma_graph_source_catd [B : Cat]
  : τ (Catd (TotalOp_cat B))
≔ @hom_identity_graph_catd B;

protected symbol comma_graph_middle_inner_cart [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Functor (Op_cat B) (Functor_cart_cat B Cat_cart))
≔ @comp_cat_fapp0 (Op_cat B) (Op_cat C) (Functor_cart_cat B Cat_cart)
    (@hom_int C B G) (@Op_func B C F);

// Same whole family after the existing inclusion; no new comparison data.
protected symbol comma_graph_middle_inner_catd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Functor (Op_cat B) (Catd_cat B))
≔ @comp_cat_fapp0 (Op_cat B) (Functor_cart_cat B Cat_cart) (Catd_cat B)
    (Functor_cart_include B Cat_cart) (@comma_graph_middle_inner_cart B C F G);

protected symbol comma_graph_middle_raw_catd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Catd (Op_cat B))
≔ @comp_cat_fapp0 (Op_cat B) (Functor_cart_cat B Cat_cart) Cat_cart
    (@Sigma_coeff_func B) (@comma_graph_middle_inner_cart B C F G);

protected symbol comma_graph_middle_catd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Catd (TotalOp_cat B))
≔ @TotalOp_catd (Op_cat B) (@comma_graph_middle_raw_catd B C F G);

protected symbol comma_graph_target_base_catd [C : Cat]
  : τ (Catd (TotalOp_cat C))
≔ @homdc_op_edge_catd C C (@hom_int C C (@id_func C));

protected symbol comma_graph_target_catd [B C : Cat]
  (F : τ (Functor B C))
  : τ (Catd (TotalOp_cat B))
≔ @Pullback_catd (TotalOp_cat B) (TotalOp_cat C)
    (@comma_graph_target_base_catd C) (@TotalOp_func B C F);

// Fibrewise Sigma of the existing whole internal action.
// Sigma sends the original whole internal action to an ordinary Cat-valued
// transformation. This declaration does not claim Cartesian admission of
// that transformation or supply its subsequent fibrewise dual.
protected symbol comma_graph_sigma_transf [B C : Cat]
  [F G : τ (Functor B C)]
  (epsilon : τ (@Transf (Op_cat B) (Catd_cat B)
    (@hom_int_view B B (@id_func B))
    (@comp_cat_fapp0 (Op_cat B) (Op_cat C) (Catd_cat B)
      (@hom_int_view C B G) (@Op_func B C F))))
  : τ (@Transf (Op_cat B) Cat_cat
      (@comp_cat_fapp0 (Op_cat B) (Catd_cat B) Cat_cat
        (@Sigma_func B) (@hom_int_view B B (@id_func B)))
      (@comp_cat_fapp0 (Op_cat B) (Catd_cat B) Cat_cat
        (@Sigma_func B) (@comma_graph_middle_inner_catd B C F G)))
≔ @fapp0
    (@Transf_cat (Op_cat B) (Catd_cat B)
      (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G))
    (@Transf_cat (Op_cat B) Cat_cat
      (@comp_cat_fapp0 (Op_cat B) (Catd_cat B) Cat_cat
        (@Sigma_func B) (@hom_int_view B B (@id_func B)))
      (@comp_cat_fapp0 (Op_cat B) (Catd_cat B) Cat_cat
        (@Sigma_func B) (@comma_graph_middle_inner_catd B C F G)))
    (@comp_cat_cov_fapp1_func (Op_cat B) (Catd_cat B) Cat_cat (@Sigma_func B)
      (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G))
    epsilon;

// Pointwise opposite turns that whole transformation into the displayed map
// Admitted internal actions are strict in x, with the original generally
// lax displayed y-components. Arbitrary two-direction lax Theta is excluded.
protected symbol comma_graph_sigma_parameter_funcd [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (Hom (Functor_cart_cat (Op_cat B) Cat_cart)
      (@comma_graph_source_raw_catd B) (@comma_graph_middle_raw_catd B C F G))
≔ @Sigma_parameter_funcd (Op_cat B) B (@hom_int B B (@id_func B))
    (@comma_graph_middle_inner_cart B C F G) theta;

// Total fibre duality now consumes the actual admitted whole map.
protected symbol comma_graph_sigma_op_funcd [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (@Functord (TotalOp_cat B)
      (@comma_graph_source_catd B) (@comma_graph_middle_catd B C F G))
≔ @strict_transfor _ _ _ _
    (@TotalOp_funcd (Op_cat B)
      (@comma_graph_source_raw_catd B) (@comma_graph_middle_raw_catd B C F G)
      (@comma_graph_sigma_parameter_funcd B C F G theta));

protected symbol comma_graph_identity_sec [B : Cat]
  : τ (Obj (@Pi_cat (TotalOp_cat B) (@comma_graph_source_catd B)))
≔ @hom_identity_graph_sec B;

protected symbol comma_graph_middle_sec [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (Obj (@Pi_cat (TotalOp_cat B) (@comma_graph_middle_catd B C F G)))
≔ @section_postcomp_sec (TotalOp_cat B)
    (@comma_graph_source_catd B) (@comma_graph_middle_catd B C F G)
    (@comma_graph_sigma_op_funcd B C F G theta) (@comma_graph_identity_sec B);

// The represented C-family at the varying source F[x].
// Cartesian represented family, with its existing ordinary input view.
protected symbol comma_graph_rep_cart [B C : Cat] (F : τ (Functor B C))
  : τ (Functor (Op_cat B) (Functor_cart_cat C Cat_cart))
≔ @comp_cat_fapp0 (Op_cat B) (Op_cat C) (Functor_cart_cat C Cat_cart)
    (@hom_int C C (@id_func C)) (@Op_func B C F);

protected symbol comma_graph_rep_catd [B C : Cat] (F : τ (Functor B C))
  : τ (Functor (Op_cat B) (Catd_cat C))
≔ @comp_cat_fapp0 (Op_cat B) (Functor_cart_cat C Cat_cart) (Catd_cat C)
    (Functor_cart_include C Cat_cart) (@comma_graph_rep_cart B C F);

// Retain the original ordinary source functor for its whole ambient view.
protected symbol comma_graph_basechange_source_func [B C : Cat] (G : τ (Functor B C))
  : τ (Functor (Catd_cat C) Cat_cat)
≔ @comp_cat_fapp0 (Catd_cat C) (Catd_cat B) Cat_cat
    (@Sigma_func B) (@Pullback_catd_func B C G);

protected symbol comma_graph_basechange_source_catd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Catd (Op_cat B))
≔ @comp_cat_fapp0 (Op_cat B) (Functor_cart_cat C Cat_cart) Cat_cart
    (@Sigma_pullback_coeff_source B C G) (@comma_graph_rep_cart B C F);

protected symbol comma_graph_target_raw_catd [B C : Cat] (F : τ (Functor B C))
  : τ (Catd (Op_cat B))
≔ @comp_cat_fapp0 (Op_cat B) (Op_cat C) Cat_cart
    (@homdc_edge_catd C C (@hom_int C C (@id_func C))) (@Op_func B C F);

// Existing Cartesian prewhiskering of the admitted base-change map.
protected symbol comma_graph_basechange_transf [B C : Cat]
  (F G : τ (Functor B C))
  : τ (Hom (Functor_cart_cat (Op_cat B) Cat_cart)
      (@comma_graph_basechange_source_catd B C F G) (@comma_graph_target_raw_catd B C F))
≔ @hom_precomp_along_fapp1_fapp0 Cat_cart Cat_cart (@id_func Cat_cart)
    Cat_cart (Op_cat B) (Functor_cart_cat C Cat_cart) (@comma_graph_rep_cart B C F)
    (@Sigma_pullback_coeff_source B C G) (@Sigma_coeff_func C)
    (@sigma_pullback_coeff_transf B C G);

protected symbol comma_graph_basechange_op_raw_funcd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (@Functord (TotalOp_cat B)
      (@TotalOp_catd (Op_cat B) (@comma_graph_basechange_source_catd B C F G))
      (@TotalOp_catd (Op_cat B) (@comma_graph_target_raw_catd B C F)))
≔ @strict_transfor _ _ _ _
    (@TotalOp_funcd (Op_cat B)
      (@comma_graph_basechange_source_catd B C F G) (@comma_graph_target_raw_catd B C F)
      (@comma_graph_basechange_transf B C F G));

protected symbol comma_graph_basechange_source_reframe_funcd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (@Functord (TotalOp_cat B)
      (@comma_graph_middle_catd B C F G)
      (@TotalOp_catd (Op_cat B) (@comma_graph_basechange_source_catd B C F G)))
≔ @id_funcd (TotalOp_cat B) (@comma_graph_middle_catd B C F G);

protected symbol comma_graph_basechange_target_reframe_funcd [B C : Cat]
  (F : τ (Functor B C))
  : τ (@Functord (TotalOp_cat B)
      (@TotalOp_catd (Op_cat B) (@comma_graph_target_raw_catd B C F))
      (@comma_graph_target_catd B C F))
≔ @id_funcd (TotalOp_cat B) (@TotalOp_catd (Op_cat B) (@comma_graph_target_raw_catd B C F));

protected symbol comma_graph_basechange_op_funcd [B C : Cat]
  (F G : τ (Functor B C))
  : τ (@Functord (TotalOp_cat B)
      (@comma_graph_middle_catd B C F G) (@comma_graph_target_catd B C F))
// The two reframings above are identities of proof-time-equal families.
// Keep the same actual map without inserting those identities as runtime cuts.
≔ @comma_graph_basechange_op_raw_funcd B C F G;

// Complete the original section/base-change/total-duality pipeline.
protected symbol comma_graph_target_sec [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (Obj (@Pi_cat (TotalOp_cat B) (@comma_graph_target_catd B C F)))
≔ @section_postcomp_sec (TotalOp_cat B)
    (@comma_graph_middle_catd B C F G) (@comma_graph_target_catd B C F)
    (@comma_graph_basechange_op_funcd B C F G)
    (@comma_graph_middle_sec B C F G theta);

protected symbol comma_graph_underlying_func [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (Functor (TotalOp_cat B)
      (@Sigma_cat (TotalOp_cat C) (@comma_graph_target_base_catd C)))
≔ @comp_cat_fapp0 (TotalOp_cat B)
    (@Sigma_cat (TotalOp_cat B) (@comma_graph_target_catd B C F))
    (@Sigma_cat (TotalOp_cat C) (@comma_graph_target_base_catd C))
    (@sigma_pullback_total_func (TotalOp_cat B) (TotalOp_cat C)
      (@TotalOp_func B C F) (@comma_graph_target_base_catd C))
    (@section_total_func (TotalOp_cat B) (@comma_graph_target_catd B C F)
      (@comma_graph_target_sec B C F G theta));

protected symbol comma_graph_internal_func [B C : Cat]
  [F G : τ (Functor B C)]
  (theta : τ (Hom (Functor_cart_cat (Op_cat B) (Catd_cat B))
    (@hom_int_view B B (@id_func B)) (@comma_graph_middle_inner_catd B C F G)))
  : τ (Functor B (@LaxArrow_cat C))
≔ @TotalOp_func (TotalOp_cat B)
    (@Sigma_cat (TotalOp_cat C) (@comma_graph_target_base_catd C))
    (@comma_graph_underlying_func B C F G theta);

// The actual whole input classifier.

// The original represented-comma family, over its corrected total-dual base.
protected symbol represented_comma_family_catd [X Y : Cat] (J : τ (Functor X Y))
  : τ (Catd (TotalOp_cat X))
≔ @Pullback_catd (TotalOp_cat X) (TotalOp_cat Y)
    (@comma_graph_target_base_catd Y) (@TotalOp_func X Y J);

protected symbol represented_comma_family_reframe [X Y : Cat] (J : τ (Functor X Y))
  : τ (@Functord (TotalOp_cat X) (@represented_comma_family_catd X Y J)
      (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J)))
≔ @id_funcd (TotalOp_cat X) (@represented_comma_family_catd X Y J);

protected symbol represented_comma_family_target [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X))
  : τ (Catd (TotalOp_cat K))
≔ @Pullback_catd (TotalOp_cat K) (TotalOp_cat X)
    (@represented_comma_family_catd X Y J) (@TotalOp_func K X A);

protected symbol represented_comma_family_section [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (Hom (Functor_cart_cat (Op_cat K) (Catd_cat K))
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  : τ (Obj (@Pi_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)))
≔ @comma_graph_target_sec K Y (@comp_cat_fapp0 K X Y J A) D h;

protected symbol represented_comma_family_underlying_func [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (Hom (Functor_cart_cat (Op_cat K) (Catd_cat K))
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  : τ (Functor (TotalOp_cat K)
      (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J)))
≔ @comp_cat_fapp0 (TotalOp_cat K)
    (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))
    (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J))
    (@sigma_pullback_total_func (TotalOp_cat K) (TotalOp_cat X) (@TotalOp_func K X A)
      (@represented_comma_family_catd X Y J))
    (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
      (@represented_comma_family_section K X Y J A D h));

// A valid internal-Hom input is strict in x; its displayed y-maps can be lax.
// Ordinary eta supplies this profile through tapp1_int_cart without extra input.
symbol represented_comma_hom_action_func [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (Hom (Functor_cart_cat (Op_cat K) (Catd_cat K))
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  : τ (Functor K (@RepresentedComma_cat X Y J))
≔ @TotalOp_func (TotalOp_cat K)
    (@Sigma_cat (TotalOp_cat X) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J)))
    (@represented_comma_family_underlying_func K X Y J A D h);

// Whole source projection with its original inverse data.
// Total/section duality is O; the admitted internal Hom remains over T(K).

protected symbol comma_source_op_total_projection [K : Cat] (E : τ (Catd K)) (s : τ (Obj (@Pi_cat K E)))
 : τ (Functor (TotalOp_cat K) (TotalOp_cat K))
≔ @comp_cat_fapp0 (TotalOp_cat K) (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)
 (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E))
 (@TotalOp_func K (@Sigma_cat K E) (@section_total_func K E s));

protected symbol comma_source_op_map_projection [K : Cat] (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (Functor (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K))
≔ @comp_cat_fapp0 (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat (@Sigma_cat K D)) (TotalOp_cat K)
 (@TotalOp_func (@Sigma_cat K D) K (@Sigma_proj1_func K D))
 (@TotalOp_func (@Sigma_cat K E) (@Sigma_cat K D) (@sigma_map_func K E D FF));

protected symbol comma_source_op_basechange_projection [A K : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 : τ (Functor (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
≔ @comp_cat_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)
 (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E))
 (@TotalOp_func (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K E) (@sigma_pullback_total_func A K F E));

protected symbol comma_source_op_basechange_projected [A K : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 : τ (Functor (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
≔ @comp_cat_fapp0 (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat A) (TotalOp_cat K)
 (@TotalOp_func A K F) (@TotalOp_func (@Sigma_cat A (@Pullback_catd A K E F)) A (@Sigma_proj1_func A (@Pullback_catd A
   K E F)));

protected symbol comma_source_op_total_evidence [K : Cat] (E : τ (Catd K)) (s : τ (Obj (@Pi_cat K E)))
 : τ (IsoEvidence (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K)))
≔ @iso_evidence_intro (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func
  (TotalOp_cat K))
 (@id (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s)) (@id (Functor_cat (TotalOp_cat K)
   (TotalOp_cat K)) (@id_func (TotalOp_cat K)))
 (eq_refl (@id (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s))) (eq_refl (@id
   (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@id_func (TotalOp_cat K))));

// Certify the identity data before argument normalization erases a view head.
protected symbol comma_source_op_total_evidence_identity_data_path [K : Cat] (E : τ (Catd K)) (s : τ (Obj (@Pi_cat K E)))
 : τ (@= (ArrowPairData (Functor_cat (TotalOp_cat K) (TotalOp_cat K)))
      (@arrow_pair_data (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K))
      (@iso_evidence_to (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K)) (@comma_source_op_total_evidence K E s))
      (@iso_evidence_from (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K)) (@comma_source_op_total_evidence K E s))) (@identity_arrow_pair (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s)))
≔ @eq_refl (ArrowPairData (Functor_cat (TotalOp_cat K) (TotalOp_cat K))) (@arrow_pair_data (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K))
      (@iso_evidence_to (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K)) (@comma_source_op_total_evidence K E s))
      (@iso_evidence_from (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_source_op_total_projection K E s) (@id_func (TotalOp_cat
   K)) (@comma_source_op_total_evidence K E s)));

protected symbol comma_source_op_map_evidence [K : Cat] (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (IsoEvidence (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF)
   (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)))
≔ @iso_evidence_intro (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF)
  (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E))
 (@id (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF)) (@id
   (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)))
 (eq_refl (@id (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF)))
   (eq_refl (@id (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@TotalOp_func (@Sigma_cat K E) K
   (@Sigma_proj1_func K E))));

// Certify the identity data before argument normalization erases a view head.
protected symbol comma_source_op_map_evidence_identity_data_path [K : Cat] (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (@= (ArrowPairData (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)))
      (@arrow_pair_data (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E))
      (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)) (@comma_source_op_map_evidence K E D FF))
      (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)) (@comma_source_op_map_evidence K E D FF))) (@identity_arrow_pair (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF)))
≔ @eq_refl (ArrowPairData (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K))) (@arrow_pair_data (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E))
      (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)) (@comma_source_op_map_evidence K E D FF))
      (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat K E)) (TotalOp_cat K)) (@comma_source_op_map_projection K E D FF) (@TotalOp_func (@Sigma_cat K E) K (@Sigma_proj1_func K E)) (@comma_source_op_map_evidence K E D FF)));

protected symbol comma_source_op_basechange_evidence [A K : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 : τ (IsoEvidence (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
   (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E))
≔ @iso_evidence_intro (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
  (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E)
 (@id (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
   (@comma_source_op_basechange_projection A K F E)) (@id (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E
   F))) (TotalOp_cat K)) (@comma_source_op_basechange_projected A K F E))
 (eq_refl (@id (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))
   (@comma_source_op_basechange_projection A K F E))) (eq_refl (@id (Functor_cat (TotalOp_cat (@Sigma_cat A
   (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projected A K F E)));

// Certify the identity data before argument normalization erases a view head.
protected symbol comma_source_op_basechange_evidence_identity_data_path [A K : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 : τ (@= (ArrowPairData (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)))
      (@arrow_pair_data (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E)
      (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E) (@comma_source_op_basechange_evidence A K F E))
      (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E) (@comma_source_op_basechange_evidence A K F E))) (@identity_arrow_pair (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E)))
≔ @eq_refl (ArrowPairData (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K))) (@arrow_pair_data (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E)
      (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E) (@comma_source_op_basechange_evidence A K F E))
      (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat A (@Pullback_catd A K E F))) (TotalOp_cat K)) (@comma_source_op_basechange_projection A K F E) (@comma_source_op_basechange_projected A K F E) (@comma_source_op_basechange_evidence A K F E)));

// The actual source projection p∘Γ.
symbol represented_comma_hom_action_source_func [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K X)
≔ (@comp_cat_fapp0 K (@RepresentedComma_cat X Y J) X (@represented_comma_source_func X Y J)
  (@represented_comma_hom_action_func K X Y J A D h));

protected symbol comma_source_gamma_source1 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K X)
≔ (@comp_cat_fapp0 K (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X
  (@comp_cat_fapp0 (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) (TotalOp_cat
  (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J))) X (@TotalOp_func (@Sigma_cat (TotalOp_cat X)
  (@represented_comma_family_catd X Y J)) (TotalOp_cat X) (@Sigma_proj1_func (TotalOp_cat X)
  (@represented_comma_family_catd X Y J))) (@TotalOp_func (@Sigma_cat (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A)) (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y
  J)) (@sigma_pullback_total_func (TotalOp_cat K) (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y
  J)))) (@TotalOp_func (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))
  (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
  (@represented_comma_family_section K X Y J A D h))));

protected symbol comma_source_gamma_source2 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K X)
≔ (@comp_cat_fapp0 K (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X
  (@comp_cat_fapp0 (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) K X A
  (@TotalOp_func (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (TotalOp_cat K)
  (@Sigma_proj1_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)))) (@TotalOp_func (TotalOp_cat K)
  (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (@section_total_func (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h))));

// The constructor now uses its underlying map directly at the checked
// target type. This first comparison therefore only reassociates its source
// projection. The old proof reinserted the removed sigma_map(id_reframe).
// Its selected forward and reverse maps were mapped identities; retain those
// identities directly, with the same comparison endpoints and public owner.
protected symbol comma_source_gamma_step1 [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@StrictTransfor (Op_cat K) (Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  : τ (IsoEvidence (Functor_cat K X)
      (@represented_comma_hom_action_source_func K X Y J A D h)
      (@comma_source_gamma_source1 K X Y J A D h))
≔ @iso_evidence_intro (Functor_cat K X)
    (@represented_comma_hom_action_source_func K X Y J A D h)
    (@comma_source_gamma_source1 K X Y J A D h)
    (@id (Functor_cat K X) (@represented_comma_hom_action_source_func K X Y J A D h))
    (@id (Functor_cat K X) (@comma_source_gamma_source1 K X Y J A D h))
    (eq_refl (@id (Functor_cat K X) (@represented_comma_hom_action_source_func K X Y J A D h)))
    (eq_refl (@id (Functor_cat K X) (@comma_source_gamma_source1 K X Y J A D h)));

protected symbol comma_source_gamma_step2 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (IsoEvidence (Functor_cat K X) (@comma_source_gamma_source1 K X Y J A D h) (@comma_source_gamma_source2 K X Y J A D h))
≔ @iso_evidence_from_identity_pair (Functor_cat K X) (@comma_source_gamma_source1 K X Y J A D h) (@comma_source_gamma_source2 K X Y J A D h)
  (@transf_prewhisker K (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X (@TotalOp_func (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))
  (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
  (@represented_comma_family_section K X Y J A D h))) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))
    (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_evidence (TotalOp_cat K)
  (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))))
  (@transf_prewhisker K (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X (@TotalOp_func (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))
  (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
  (@represented_comma_family_section K X Y J A D h))) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))
    (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_evidence (TotalOp_cat K)
  (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))))
  (@identity_pair_map_path (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (Functor_cat K X) (@comp_cat_con_func K (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X (@TotalOp_func (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))
  (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
  (@represented_comma_family_section K X Y J A D h))))
      (@arrow_pair_data (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))
      (@iso_evidence_to (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_evidence (TotalOp_cat K)
  (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)))
      (@iso_evidence_from (Functor_cat (TotalOp_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A))) X) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_projected (TotalOp_cat K) (TotalOp_cat
  X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)) (@comma_source_op_basechange_evidence (TotalOp_cat K)
  (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)))) (@comma_source_op_basechange_projection (TotalOp_cat K) (TotalOp_cat X)
  (@TotalOp_func K X A) (@represented_comma_family_catd X Y J))
      (@comma_source_op_basechange_evidence_identity_data_path (TotalOp_cat K) (TotalOp_cat X) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)));

protected symbol comma_source_gamma_step3 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (IsoEvidence (Functor_cat K X) (@comma_source_gamma_source2 K X Y J A D h) A)
≔ @iso_evidence_from_identity_pair (Functor_cat K X) (@comma_source_gamma_source2 K X Y J A D h) A
  (@transf_postwhisker K K X A (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K)
    (@iso_evidence_to (Functor_cat K K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K) (@comma_source_op_total_evidence (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h))))
  (@transf_postwhisker K K X A (@id_func K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h))
    (@iso_evidence_from (Functor_cat K K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K) (@comma_source_op_total_evidence (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h))))
  (@identity_pair_map_path (Functor_cat K K) (Functor_cat K X) (@comp_cat_cov_func K K X A)
      (@arrow_pair_data (Functor_cat K K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K)
      (@iso_evidence_to (Functor_cat K K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K) (@comma_source_op_total_evidence (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h)))
      (@iso_evidence_from (Functor_cat K K) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h)) (@id_func K) (@comma_source_op_total_evidence (TotalOp_cat K)
  (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h)))) (@comma_source_op_total_projection (TotalOp_cat K) (@represented_comma_family_target K X Y J
  A) (@represented_comma_family_section K X Y J A D h))
      (@comma_source_op_total_evidence_identity_data_path (TotalOp_cat K) (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D h)));

// Retained whole source comparison p∘Γ≅A, with both selected maps and laws.
symbol represented_comma_hom_action_source_evidence [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (IsoEvidence (Functor_cat K X) (@represented_comma_hom_action_source_func K X Y J A D h) A)
≔ @iso_evidence_comp (Functor_cat K X) (@represented_comma_hom_action_source_func K X Y J A D h) (@comma_source_gamma_source1 K X Y J A D
  h) A
 (@iso_evidence_comp (Functor_cat K X) (@comma_source_gamma_source1 K X Y J A D h) (@comma_source_gamma_source2 K X Y J A D
   h) A (@comma_source_gamma_step3 K X Y J A D h) (@comma_source_gamma_step2 K X Y J A D h))
 (@comma_source_gamma_step1 K X Y J A D h);

// Forward transformation of that same source comparison.
symbol represented_comma_hom_action_source_to [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf K X (@represented_comma_hom_action_source_func K X Y J A D h) A)
≔ @iso_evidence_to (Functor_cat K X) (@represented_comma_hom_action_source_func K X Y J A D h) A (@represented_comma_hom_action_source_evidence K X
  Y J A D h);

protected symbol comma_source_gamma_source_to_arrow [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 (x y : τ (Obj K)) (g : τ (Hom K x y))
 : τ (Hom X (@fapp0 K X (@represented_comma_hom_action_source_func K X Y J A D h) x) (@fapp0 K X A y))
≔ @tapp1_fapp0 K X (@represented_comma_hom_action_source_func K X Y J A D h) A x y
    (@represented_comma_hom_action_source_to K X Y J A D h) g;

// Original ordinary-lax constructor and source comparison.
symbol represented_comma_family_func [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D))
  : τ (Functor K (@RepresentedComma_cat X Y J))
≔ @represented_comma_hom_action_func K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h);

symbol represented_comma_family_source_func [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y)) (h
  : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D)) : τ (Functor K X)
≔ @represented_comma_hom_action_source_func K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h);

symbol represented_comma_family_source_evidence [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D))
 : τ (IsoEvidence (Functor_cat K X) (@represented_comma_family_source_func K X Y J A D h) A)
≔ @represented_comma_hom_action_source_evidence K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h);

symbol represented_comma_family_source_to [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D))
 : τ (@Transf K X (@represented_comma_family_source_func K X Y J A D h) A)
≔ @represented_comma_hom_action_source_to K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h);


// Extract the actual target section before taking the outer opposite.

protected symbol comma_section_section_observed [K A : Cat] (E : τ (Catd K))
 (FF : τ (@Functord K E (@Const_catd K A))) (s : τ (Obj (@Pi_cat K E)))
 : τ (Functor K A)
≔ @comp_cat_fapp0 K (Product_cat K A) A (@Product_projR_func K A)
   (@section_total_mapped_func K E (@Const_catd K A) FF s);

protected symbol comma_section_section_observation_target [K A : Cat] (E : τ (Catd K))
 (FF : τ (@Functord K E (@Const_catd K A))) (s : τ (Obj (@Pi_cat K E)))
 : τ (Functor K A)
≔ @section_postcomp_sec K E (@Const_catd K A) FF s;

protected symbol comma_section_section_observation_transf [K A : Cat] (E : τ (Catd K))
 (FF : τ (@Functord K E (@Const_catd K A))) (s : τ (Obj (@Pi_cat K E)))
 : τ (@Transf K A (@comma_section_section_observed K A E FF s)
     (@comma_section_section_observation_target K A E FF s))
≔ @fapp0 _ _
   (@comp_cat_cov_fapp1_func K (Product_cat K A) A (@Product_projR_func K A)
     (@section_total_mapped_func K E (@Const_catd K A) FF s)
     (@section_total_postcomp_func K E (@Const_catd K A) FF s))
   (@section_total_postcomp_transf K E (@Const_catd K A) FF s);

protected symbol comma_section_section_observation_equiv [K A : Cat]
 (A1 : τ (IsNCat (cat_succ cat_zero) A)) (E : τ (Catd K))
 (FF : τ (@Functord K E (@Const_catd K A))) (s : τ (Obj (@Pi_cat K E)))
 : τ (@OmegaEquivAlong (Functor_cat K A)
     (@comma_section_section_observed K A E FF s) (@comma_section_section_observation_target K A E FF s)
     (@comma_section_section_observation_transf K A E FF s))
≔ @one_cat_transf_pointwise_omega_along K A A1
   (@comma_section_section_observed K A E FF s) (@comma_section_section_observation_target K A E FF s)
   (@comma_section_section_observation_transf K A E FF s)
   (λ x : τ (Obj K), @omega_equiv_along_refl A
     (@fapp0 K A (@comma_section_section_observation_target K A E FF s) x));

protected symbol comma_section_section_observation_iso [K A : Cat]
 (A1 : τ (IsNCat (cat_succ cat_zero) A)) (E : τ (Catd K))
 (FF : τ (@Functord K E (@Const_catd K A))) (s : τ (Obj (@Pi_cat K E)))
 : τ (IsoEvidence (Functor_cat K A) (@comma_section_section_observed K A E FF s)
     (@comma_section_section_observation_target K A E FF s))
≔ @omega_equiv_along_iso_evidence (Functor_cat K A)
   (@comma_section_section_observed K A E FF s) (@comma_section_section_observation_target K A E FF s)
   (@comma_section_section_observation_transf K A E FF s)
   (@comma_section_section_observation_equiv K A A1 E FF s);

protected symbol comma_section_gamma_target_family_map [X Y : Cat] (J : τ (Functor X Y))
 : τ (@Functord (TotalOp_cat X) (@represented_comma_family_catd X Y J)
     (@Const_catd (TotalOp_cat X) (TotalOp_cat Y)))
≔ @comp_catd_fapp0 (TotalOp_cat X)
    (@represented_comma_family_catd X Y J)
    (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
    (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
    (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J)))
    (@represented_comma_family_reframe X Y J);

protected symbol comma_section_gamma_target_section_map [K X Y : Cat]
 (J : τ (Functor X Y)) (A : τ (Functor K X))
 : τ (@Functord (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
     (@Const_catd (TotalOp_cat K) (TotalOp_cat Y)))
≔ @fapp1_fapp0 (@Catd_cat (TotalOp_cat X)) (@Catd_cat (TotalOp_cat K))
   (@Pullback_catd_func (TotalOp_cat K) (TotalOp_cat X) (@TotalOp_func K X A))
   (@represented_comma_family_catd X Y J)
   (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
   (@comma_section_gamma_target_family_map X Y J);

protected symbol comma_section_gamma_target_section [K X Y : Cat] (J : τ (Functor X Y))
 (A : τ (Functor K X)) (D : τ (Functor K Y))
 (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @comma_section_section_observation_target (TotalOp_cat K) (TotalOp_cat Y)
   (@represented_comma_family_target K X Y J A)
   (@comma_section_gamma_target_section_map K X Y J A)
   (@represented_comma_family_section K X Y J A D h);

protected symbol comma_section_gamma_target_extraction [K X Y : Cat]
 (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
 (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y)
   (@comma_section_section_observed (TotalOp_cat K) (TotalOp_cat Y)
     (@represented_comma_family_target K X Y J A)
     (@comma_section_gamma_target_section_map K X Y J A)
     (@represented_comma_family_section K X Y J A D h))
   (@comma_section_gamma_target_section K X Y J A D h))
≔ @comma_section_section_observation_transf (TotalOp_cat K) (TotalOp_cat Y)
   (@represented_comma_family_target K X Y J A)
   (@comma_section_gamma_target_section_map K X Y J A)
   (@represented_comma_family_section K X Y J A D h);

protected symbol comma_section_gamma_target_section_op [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K Y)
≔ @TotalOp_func (TotalOp_cat K) (TotalOp_cat Y) (@comma_section_gamma_target_section K X Y J A D h);

protected symbol comma_section_gamma_target_observed_op [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K Y)
≔ @TotalOp_func (TotalOp_cat K) (TotalOp_cat Y) (@comma_section_section_observed (TotalOp_cat K) (TotalOp_cat Y)
  (@represented_comma_family_target K X Y J A) (@comma_section_gamma_target_section_map K X Y J A)
  (@represented_comma_family_section K X Y J A D h));

protected symbol comma_section_gamma_target_extraction_op [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf K Y (@comma_section_gamma_target_section_op K X Y J A D h)
     (@comma_section_gamma_target_observed_op K X Y J A D h))
≔ @TotalOp_transf (TotalOp_cat K) (TotalOp_cat Y) (@comma_section_section_observed (TotalOp_cat K) (TotalOp_cat Y)
  (@represented_comma_family_target K X Y J A) (@comma_section_gamma_target_section_map K X Y J A)
  (@represented_comma_family_section K X Y J A D h)) (@comma_section_gamma_target_section K X Y J A D h)
   (@comma_section_gamma_target_extraction K X Y J A D h);

protected symbol comma_section_gamma_target_extraction_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y)
     (@comma_section_gamma_target_section_op K X Y J A D h)
     (@comma_section_gamma_target_observed_op K X Y J A D h)
     (@comma_section_gamma_target_extraction_op K X Y J A D h))
≔ @one_cat_transf_pointwise_omega_along K Y Y1
   (@comma_section_gamma_target_section_op K X Y J A D h)
   (@comma_section_gamma_target_observed_op K X Y J A D h)
   (@comma_section_gamma_target_extraction_op K X Y J A D h)
   (λ x : τ (Obj K), @omega_equiv_along_refl Y (@fapp0 K Y D x));

protected symbol comma_section_constant_section_projection [K A : Cat]
 (s : τ (Obj (@Pi_cat K (@Const_catd K A))))
 : τ (Functor K A)
≔ @comp_cat_fapp0 K (Product_cat K A) A
   (@Product_projR_func K A) (@section_total_func K (@Const_catd K A) s);

protected symbol comma_section_constant_section_arrow_agrees [K A : Cat]
 (s : τ (Obj (@Pi_cat K (@Const_catd K A))))
 (x y : τ (Obj K)) (p : τ (Hom K x y))
 : τ (@= (Hom A (@fapp0 K A s x) (@fapp0 K A s y))
   (@fapp1_fapp0 K A (@comma_section_constant_section_projection K A s) x y p)
   (@fapp1_fapp0 K A s x y p))
≔ @piapp1_const_fapp0_eq K A s x y p;

// Link that section to the original total base change.

protected symbol comma_basechange_sigma_basechange_source [A K : Cat] (F : τ (Functor A K))
 : τ (Functor (@Catd_cat K) Cat_cat)
≔ @comp_cat_fapp0 (@Catd_cat K) (@Catd_cat A) Cat_cat
   (@Sigma_func A) (@Pullback_catd_func A K F);

protected symbol comma_basechange_sigma_basechange_left [A K : Cat] (F : τ (Functor A K))
 (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K D))
≔ @comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K E) (@Sigma_cat K D)
   (@sigma_map_func K E D FF) (@sigma_pullback_total_func A K F E);

protected symbol comma_basechange_sigma_basechange_right [A K : Cat] (F : τ (Functor A K))
 (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K D))
≔ @comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K E F))
   (@Sigma_cat A (@Pullback_catd A K D F)) (@Sigma_cat K D)
   (@sigma_pullback_total_func A K F D)
   (@sigma_map_func A (@Pullback_catd A K E F) (@Pullback_catd A K D F)
     (@fapp1_fapp0 (@Catd_cat K) (@Catd_cat A) (@Pullback_catd_func A K F) E D FF));

// Retain both raw laxity cells and their common off-diagonal target.
protected symbol comma_basechange_sigma_basechange_middle [A K : Cat] (F : τ (Functor A K))
 (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K D))
≔ @tapp1_fapp0 (@Catd_cat K) Cat_cat
    (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K) E D
    (@sigma_pullback_total_transf A K F) FF;

protected symbol comma_basechange_sigma_basechange_post [A K : Cat] (F : τ (Functor A K))
 (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (@Transf (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K D)
     (@comma_basechange_sigma_basechange_left A K F E D FF)
     (@comma_basechange_sigma_basechange_middle A K F E D FF))
≔ @tapp1_post_laxity_cell (@Catd_cat K) Cat_cat
   (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
   (@sigma_pullback_total_transf A K F) E E D FF (@id (@Catd_cat K) E);

protected symbol comma_basechange_sigma_basechange_pre [A K : Cat] (F : τ (Functor A K))
 (E D : τ (Catd K)) (FF : τ (@Functord K E D))
 : τ (@Transf (@Sigma_cat A (@Pullback_catd A K E F)) (@Sigma_cat K D)
     (@comma_basechange_sigma_basechange_right A K F E D FF)
     (@comma_basechange_sigma_basechange_middle A K F E D FF))
≔ @tapp1_pre_laxity_cell (@Catd_cat K) Cat_cat
   (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
   (@sigma_pullback_total_transf A K F) E D D FF (@id (@Catd_cat K) D);

// Strict-default proof adaptation for the original comma target comparison.
// These are derived inverse-evidence helpers, not new operational owners.
protected symbol comma_strict_compositor_omega [A B : Cat]
  (F : τ (Functor A B)) [x y z : τ (Obj A)]
  (g : τ (Hom A y z)) (f : τ (Hom A x y))
  : τ (@OmegaEquivAlong (Hom_cat B (fapp0 F x) (fapp0 F z))
    (fapp0 (@functord_transport_lhs_func A
      (@hom_ A A (@id_func A) x) (@hom_ B A F (fapp0 F x))
      (@fapp1_at_transf A B F x) y z g) f)
    (fapp0 (@functord_transport_rhs_func A
      (@hom_ A A (@id_func A) x) (@hom_ B A F (fapp0 F x))
      (@fapp1_at_transf A B F x) y z g) f)
    (@fapp1_compositor A B F x y z g f))
≔ @omega_equiv_along_refl (Hom_cat B (fapp0 F x) (fapp0 F z))
    (fapp0 (@functord_transport_lhs_func A
      (@hom_ A A (@id_func A) x) (@hom_ B A F (fapp0 F x))
      (@fapp1_at_transf A B F x) y z g) f);

// The now-default pre/right cell has the same identity inverse evidence.
protected symbol comma_pre_cell_omega [A B : Cat]
  [F G : τ (Functor A B)] (epsilon : τ (Transf F G))
  [w x y : τ (Obj A)] (h : τ (Hom A w x)) (q : τ (Hom A x y))
  : τ (@OmegaEquivAlong (Hom_cat B (fapp0 F w) (fapp0 G y))
    (fapp0 (@functord_transport_lhs_func (Op_cat A)
      (@hom_con A y A (@id_func A)) (@hom_con B (fapp0 G y) A F)
      (@tapp1_con_at_transf A B F G epsilon y) x w h) q)
    (fapp0 (@functord_transport_rhs_func (Op_cat A)
      (@hom_con A y A (@id_func A)) (@hom_con B (fapp0 G y) A F)
      (@tapp1_con_at_transf A B F G epsilon y) x w h) q)
    (@tapp1_pre_laxity_cell A B F G epsilon w x y h q))
≔ @omega_equiv_along_refl (Hom_cat B (fapp0 F w) (fapp0 G y))
    (fapp0 (@functord_transport_lhs_func (Op_cat A)
      (@hom_con A y A (@id_func A)) (@hom_con B (fapp0 G y) A F)
      (@tapp1_con_at_transf A B F G epsilon y) x w h) q);

// Default strict functor action maps the existing two inverse laws.
// Equality is only theorem evidence here, never an operational map argument.
protected symbol comma_strict_omega_map [A B : Cat] (F : τ (Functor A B))
  [x y : τ (Obj A)] [f : τ (Hom A x y)]
  (e : τ (@OmegaEquivAlong A x y f))
  : τ (@OmegaEquivAlong B (fapp0 F x) (fapp0 F y)
    (@fapp1_fapp0 A B F x y f))
≔ @omega_equiv_along_intro B (fapp0 F x) (fapp0 F y)
    (@fapp1_fapp0 A B F x y f)
    (@fapp1_fapp0 A B F y x (@omega_equiv_along_left_inv A x y f e))
    (@fapp1_fapp0 A B F y x (@omega_equiv_along_right_inv A x y f e))
    (@eq_ap (Hom A x x) (Hom B (fapp0 F x) (fapp0 F x))
      (λ p : τ (Hom A x x), @fapp1_fapp0 A B F x x p)
      (@comp_fapp0 A x y x (@omega_equiv_along_left_inv A x y f e) f)
      (@id A x) (@omega_equiv_along_left_law A x y f e))
    (@eq_ap (Hom A y y) (Hom B (fapp0 F y) (fapp0 F y))
      (λ p : τ (Hom A y y), @fapp1_fapp0 A B F y y p)
      (@comp_fapp0 A y x y f (@omega_equiv_along_right_inv A x y f e))
      (@id A y) (@omega_equiv_along_right_law A x y f e));

// Map evidence successively through the two original fixed whiskerings.
protected symbol comma_whiskered_omega [K A B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (H : τ (Functor K A)) (P : τ (Functor B C))
  [F G : τ (Functor A B)] (eta : τ (@Transf A B F G))
  (e : τ (@OmegaEquivAlong (Functor_cat A B) F G eta))
  : τ (@OmegaEquivAlong (Functor_cat K C)
    (@comp_cat_fapp0 K B C P (@comp_cat_fapp0 K A B F H))
    (@comp_cat_fapp0 K B C P (@comp_cat_fapp0 K A B G H))
    (@transf_postwhisker K B C P
      (@comp_cat_fapp0 K A B F H) (@comp_cat_fapp0 K A B G H)
      (@transf_prewhisker K A B H F G eta)))
≔ let pre : τ (@OmegaEquivAlong (Functor_cat K B)
      (@comp_cat_fapp0 K A B F H) (@comp_cat_fapp0 K A B G H)
      (@transf_prewhisker K A B H F G eta))
    ≔ @comma_strict_omega_map (Functor_cat A B) (Functor_cat K B)
      (@comp_cat_con_func K A B H) F G eta e in
  @comma_strict_omega_map (Functor_cat K B) (Functor_cat K C)
    (@comp_cat_cov_func K B C P)
    (@comp_cat_fapp0 K A B F H) (@comp_cat_fapp0 K A B G H)
    (@transf_prewhisker K A B H F G eta) pre;

// Reversing an ordinary comparison exchanges its two retained inverse laws.
protected symbol comma_total_op_omega_along [C : Cat] [x y : τ (Obj C)]
  (f : τ (Hom (TotalOp_cat C) x y))
  (e : τ (@OmegaEquivAlong (TotalOp_cat C) x y f))
  : τ (@OmegaEquivAlong C y x f)
≔ @omega_equiv_along_intro C y x f
    (@omega_equiv_along_right_inv (TotalOp_cat C) x y f e)
    (@omega_equiv_along_left_inv (TotalOp_cat C) x y f e)
    (@omega_equiv_along_right_law (TotalOp_cat C) x y f e)
    (@omega_equiv_along_left_law (TotalOp_cat C) x y f e);

// Evidence for the actual selected inverse, without replacing that map.
protected symbol comma_left_inverse_omega [C : Cat] [x y : τ (Obj C)]
  (f : τ (Hom C x y)) (e : τ (@OmegaEquivAlong C x y f))
  : τ (@OmegaEquivAlong C y x (@omega_equiv_along_left_inv C x y f e))
≔ @omega_equiv_along_intro C y x (@omega_equiv_along_left_inv C x y f e)
    f f (@omega_equiv_left_as_right_law C x y f e)
    (@omega_equiv_along_left_law C x y f e);

protected symbol comma_basechange_sigma_map_composition [K : Cat] (E M D : τ (Catd K))
 (FF : τ (@Functord K E M)) (GG : τ (@Functord K M D))
 : τ (@Transf (@Sigma_cat K E) (@Sigma_cat K D)
   (@comp_cat_fapp0 (@Sigma_cat K E) (@Sigma_cat K M) (@Sigma_cat K D)
     (@sigma_map_func K M D GG) (@sigma_map_func K E M FF))
   (@sigma_map_func K E D (@comp_catd_fapp0 K E M D GG FF)))
≔ @fapp1_compositor (@Catd_cat K) Cat_cat (@Sigma_func K) E M D GG FF;

protected symbol comma_basechange_reindexed_observation [A K C : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 (P : τ (@Functord K E (@Const_catd K C)))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat A C))
≔ @sigma_map_func A (@Pullback_catd A K E F) (@Const_catd A C)
   (@fapp1_fapp0 (@Catd_cat K) (@Catd_cat A) (@Pullback_catd_func A K F)
     E (@Const_catd K C) P);

protected symbol comma_basechange_observation_outer [A K C : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 (P : τ (@Functord K E (@Const_catd K C)))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) C)
≔ @comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C) C
   (@Product_projR_func K C) (@comma_basechange_sigma_basechange_left A K F E (@Const_catd K C) P);

protected symbol comma_basechange_observation_inner [A K C : Cat] (F : τ (Functor A K)) (E : τ (Catd K))
 (P : τ (@Functord K E (@Const_catd K C)))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) C)
≔ @comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat A C) C
   (@Product_projR_func A C) (@comma_basechange_reindexed_observation A K C F E P);

protected symbol comma_basechange_observation_middle [A K C : Cat]
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (Functor (@Sigma_cat A (@Pullback_catd A K E F)) C)
≔ @comp_cat_fapp0 (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C) C
    (@Product_projR_func K C)
    (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P);

protected symbol comma_basechange_observation_post [A K C : Cat]
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@Transf (@Sigma_cat A (@Pullback_catd A K E F)) C
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_middle A K C F E P))
≔ @transf_postwhisker (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C) C
    (@Product_projR_func K C)
    (@comma_basechange_sigma_basechange_left A K F E (@Const_catd K C) P)
    (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
    (@comma_basechange_sigma_basechange_post A K F E (@Const_catd K C) P);

protected symbol comma_basechange_observation_pre [A K C : Cat]
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@Transf (@Sigma_cat A (@Pullback_catd A K E F)) C
    (@comma_basechange_observation_inner A K C F E P) (@comma_basechange_observation_middle A K C F E P))
≔ @transf_postwhisker (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C) C
    (@Product_projR_func K C)
    (@comma_basechange_sigma_basechange_right A K F E (@Const_catd K C) P)
    (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
    (@comma_basechange_sigma_basechange_pre A K F E (@Const_catd K C) P);

// The selected component inverse data are identities on the same original objects.
protected symbol comma_basechange_observation_pre_points [A K C : Cat]
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@StrictTransfPointwiseOmegaAlong (@Sigma_cat A (@Pullback_catd A K E F)) C
    (@comma_basechange_observation_inner A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P))
≔ λ z : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
  let pre : τ (@OmegaEquivAlong
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P))
    ≔ @comma_strict_omega_map
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C))
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comp_cat_cov_func (@Sigma_cat A (@Pullback_catd A K E F))
        (Product_cat K C) C (@Product_projR_func K C))
      (@comma_basechange_sigma_basechange_right A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_pre A K F E (@Const_catd K C) P)
      (@comma_pre_cell_omega (@Catd_cat K) Cat_cat
        (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
        (@sigma_pullback_total_transf A K F)
        E (@Const_catd K C) (@Const_catd K C) P (@id (@Catd_cat K) (@Const_catd K C))) in
  @comma_strict_omega_map
    (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C) C
    (@fapp0_func (@Sigma_cat A (@Pullback_catd A K E F)) C z)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P) pre;

protected symbol comma_basechange_observation_post_points [A K C : Cat]
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@StrictTransfPointwiseOmegaAlong (@Sigma_cat A (@Pullback_catd A K E F)) C
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_post A K C F E P))
≔ λ z : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
    @sigma_ind (Obj A) (λ a : τ (Obj A), Obj (@Fibre_cat A (@Pullback_catd A K E F) a))
      (λ w : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
        @OmegaEquivAlong C
          (@fapp0 _ _ (@comma_basechange_observation_outer A K C F E P) w)
          (@fapp0 _ _ (@comma_basechange_observation_middle A K C F E P) w)
          (@tapp0_fapp0 _ _ _ _ w (@comma_basechange_observation_post A K C F E P)))
      (λ a : τ (Obj A), λ u : τ (Obj (@Fibre_cat A (@Pullback_catd A K E F) a)),
        @omega_equiv_along_refl C
          (@fapp0 (@Fibre_cat K E (@fapp0 A K F a)) C
            (@Fibre_func K E (@Const_catd K C) P (@fapp0 A K F a)) u)) z;

protected symbol comma_basechange_observation_pre_equiv [A K C : Cat]
 (C1 : τ (IsNCat (cat_succ cat_zero) C))
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@OmegaEquivAlong (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
    (@comma_basechange_observation_inner A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P))
≔ @one_cat_transf_pointwise_omega_along (@Sigma_cat A (@Pullback_catd A K E F)) C C1
    (@comma_basechange_observation_inner A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P) (@comma_basechange_observation_pre_points A K C F E P);

protected symbol comma_basechange_observation_post_equiv [A K C : Cat]
 (C1 : τ (IsNCat (cat_succ cat_zero) C))
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@OmegaEquivAlong (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_post A K C F E P))
≔ @one_cat_transf_pointwise_omega_along (@Sigma_cat A (@Pullback_catd A K E F)) C C1
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_post A K C F E P) (@comma_basechange_observation_post_points A K C F E P);

// Ordinary comparison uses the actual post cell and the retained inverse of
// the pre cell. Neither cell nor its whole functors are collapsed or cast.
protected symbol comma_basechange_observation_basechange [A K C : Cat]
 (C1 : τ (IsNCat (cat_succ cat_zero) C))
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 : τ (@Transf (@Sigma_cat A (@Pullback_catd A K E F)) C
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_inner A K C F E P))
≔ @comp_fapp0 (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
    (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_inner A K C F E P)
    (@omega_equiv_along_left_inv (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P) (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P) (@comma_basechange_observation_pre_equiv A K C C1 F E P))
    (@comma_basechange_observation_post A K C F E P);

// Preserve the existing comparison inverse(pre) o post and its chosen maps.
protected symbol comma_basechange_observation_basechange_equiv [A K C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
  : τ (@OmegaEquivAlong (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
    (@comma_basechange_observation_outer A K C F E P)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_basechange A K C C1 F E P))
≔ @omega_equiv_along_comp (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
    (@comma_basechange_observation_outer A K C F E P)
    (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_post A K C F E P)
    (@omega_equiv_along_left_inv (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P)
      (@comma_basechange_observation_pre_equiv A K C C1 F E P))
    (@comma_basechange_observation_post_equiv A K C C1 F E P)
    (@comma_left_inverse_omega (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P)
      (@comma_basechange_observation_pre_equiv A K C C1 F E P));

protected symbol comma_basechange_observation_basechange_component [A K C : Cat]
 (C1 : τ (IsNCat (cat_succ cat_zero) C))
 (F : τ (Functor A K)) (E : τ (Catd K)) (P : τ (@Functord K E (@Const_catd K C)))
 (a : τ (Obj A)) (u : τ (Obj (@Fibre_cat K E (@fapp0 A K F a))))
 : τ (Hom C
   (@fapp0 (@Fibre_cat K E (@fapp0 A K F a)) C (@Fibre_func K E (@Const_catd K C) P (@fapp0 A K F a)) u)
   (@fapp0 (@Fibre_cat K E (@fapp0 A K F a)) C (@Fibre_func K E (@Const_catd K C) P (@fapp0 A K F a)) u))
≔ @tapp0_fapp0 (@Sigma_cat A (@Pullback_catd A K E F)) C
   (@comma_basechange_observation_outer A K C F E P) (@comma_basechange_observation_inner A K C F E P)
   (Struct_sigma a u) (@comma_basechange_observation_basechange A K C C1 F E P);

protected symbol comma_basechange_gamma_target_raw0 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @comp_cat_fapp0 (TotalOp_cat K) (@Sigma_cat (TotalOp_cat X) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y
  J))) (TotalOp_cat Y)
   (@homdc_total_target_underlying_func X Y (@represented_comma_prof X Y J))
   (@comp_cat_fapp0 (TotalOp_cat K) (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J)) (@Sigma_cat
     (TotalOp_cat X) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))) (@sigma_map_func (TotalOp_cat X)
     (@represented_comma_family_catd X Y J) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
     (@represented_comma_family_reframe X Y J)) (@represented_comma_family_underlying_func K X Y J A D h));

protected symbol comma_basechange_gamma_target_raw1 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @comp_cat_fapp0 (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (TotalOp_cat Y)
   (@comma_basechange_observation_outer (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y) (@TotalOp_func K X A)
     (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J)) (@section_total_func
     (TotalOp_cat K) (@represented_comma_family_target K X Y J A) (@represented_comma_family_section K X Y J A D
     h));

protected symbol comma_basechange_gamma_target_raw2 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @comma_section_section_observed (TotalOp_cat K) (TotalOp_cat Y) (@represented_comma_family_target K X Y J A)
   (@comma_section_gamma_target_section_map K X Y J A)
   (@represented_comma_family_section K X Y J A D h);

protected symbol comma_basechange_gamma_target_step1 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y)
  (@comma_basechange_gamma_target_raw0 K X Y J A D h) (@comma_basechange_gamma_target_raw1 K X Y J A D h))
≔ @transf_postwhisker (TotalOp_cat K) (Product_cat (TotalOp_cat X) (TotalOp_cat Y)) (TotalOp_cat Y) (@Product_projR_func (TotalOp_cat X)
  (TotalOp_cat Y)) (@comp_cat_fapp0 (TotalOp_cat K) (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J))
  (Product_cat (TotalOp_cat X) (TotalOp_cat Y)) (@comp_cat_fapp0 (@Sigma_cat (TotalOp_cat X)
  (@represented_comma_family_catd X Y J)) (@Sigma_cat (TotalOp_cat X) (@homdc_op_edge_catd X Y
  (@represented_comma_prof X Y J))) (Product_cat (TotalOp_cat X) (TotalOp_cat Y)) (@sigma_map_func (TotalOp_cat X)
  (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J)) (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
  (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J)))) (@sigma_map_func (TotalOp_cat X)
  (@represented_comma_family_catd X Y J) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
  (@represented_comma_family_reframe X Y J))) (@represented_comma_family_underlying_func K X Y J A D h))
  (@comp_cat_fapp0 (TotalOp_cat K) (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J)) (Product_cat
  (TotalOp_cat X) (TotalOp_cat Y)) (@sigma_map_func (TotalOp_cat X) (@represented_comma_family_catd X Y J) (@Const_catd
  (TotalOp_cat X) (TotalOp_cat Y)) (@comma_section_gamma_target_family_map X Y J)) (@represented_comma_family_underlying_func K
  X Y J A D h))
   (@transf_prewhisker (TotalOp_cat K) (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J)) (Product_cat (TotalOp_cat
     X) (TotalOp_cat Y)) (@represented_comma_family_underlying_func K X Y J A D h) (@comp_cat_fapp0 (@Sigma_cat
     (TotalOp_cat X) (@represented_comma_family_catd X Y J)) (@Sigma_cat (TotalOp_cat X) (@homdc_op_edge_catd X Y
     (@represented_comma_prof X Y J))) (Product_cat (TotalOp_cat X) (TotalOp_cat Y)) (@sigma_map_func (TotalOp_cat X)
     (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J)) (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
     (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J)))) (@sigma_map_func (TotalOp_cat X)
     (@represented_comma_family_catd X Y J) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
     (@represented_comma_family_reframe X Y J))) (@sigma_map_func (TotalOp_cat X) (@represented_comma_family_catd
     X Y J) (@Const_catd (TotalOp_cat X) (TotalOp_cat Y)) (@comma_section_gamma_target_family_map X Y J))
     (@comma_basechange_sigma_map_composition (TotalOp_cat X) (@represented_comma_family_catd X Y J) (@homdc_op_edge_catd X Y
     (@represented_comma_prof X Y J)) (@Const_catd (TotalOp_cat X) (TotalOp_cat Y)) (@represented_comma_family_reframe
     X Y J) (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J)))));

protected symbol comma_basechange_gamma_target_step2 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y)
  (@comma_basechange_gamma_target_raw1 K X Y J A D h) (@comma_basechange_gamma_target_raw2 K X Y J A D h))
≔ @transf_prewhisker (TotalOp_cat K) (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (TotalOp_cat Y)
  (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
  (@represented_comma_family_section K X Y J A D h))
   (@comma_basechange_observation_outer (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y) (@TotalOp_func K X A)
     (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J))
   (@comma_basechange_observation_inner (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y) (@TotalOp_func K X A)
     (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J))
   (@comma_basechange_observation_basechange (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y) (@one_cat_total_op Y Y1) (@TotalOp_func K X A)
     (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J));

protected symbol comma_basechange_gamma_target_raw_link [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y)
  (@comma_basechange_gamma_target_raw0 K X Y J A D h) (@comma_basechange_gamma_target_raw2 K X Y J A D h))
≔ @comp_fapp0 (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (@comma_basechange_gamma_target_raw0 K X Y J A D h)
  (@comma_basechange_gamma_target_raw1 K X Y J A D h) (@comma_basechange_gamma_target_raw2 K X Y J A D h)
   (@comma_basechange_gamma_target_step2 K X Y J A D h Y1) (@comma_basechange_gamma_target_step1 K X Y J A D h);

// The actual target projection q∘Γ.
symbol represented_comma_hom_action_target_func [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor K Y)
≔ @comp_cat_fapp0 K (@RepresentedComma_cat X Y J) Y
   (@represented_comma_target_func X Y J) (@represented_comma_hom_action_func K X Y J A D h);

// Proof-time target observation after an identity family reframe. The two
// sides retain the specific product projection, displayed map and final map.
// Compare the actual families before removing the identity Sigma map. This
// view belongs at the comma consumer, not in every importing kernel module.
unif_rule @comp_fapp0 Cat_cat _ _ _
    (@comp_fapp0 Cat_cat _ _ _
      (@comp_fapp0 Cat_cat _ _ _
        (@CoAbove2_func _ _ (@Op_func _ _ (@Product_projR_func $A $B)))
        (@CoAbove2_func _ _ (@Op_func _ _ (@sigma_map_func $K $D $C $FF))))
      (@CoAbove2_func _ _ (@Op_func _ _
        (@sigma_map_func $K $E $D (@id (@Catd_cat $K0) $E0))))) $H
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@comp_fapp0 Cat_cat _ _ _
      (@CoAbove2_func _ _ (@Op_func _ _ (@Product_projR_func $A1 $B1)))
      (@CoAbove2_func _ _ (@Op_func _ _ (@sigma_map_func $K1 $D1 $C1 $FF1)))) $H1
  ↪ [ $K0 ≡ $K; $E0 ≡ $E; $D ≡ $E;
      $A1 ≡ $A; $B1 ≡ $B; $K1 ≡ $K; $D1 ≡ $D; $C1 ≡ $C;
      $FF1 ≡ $FF; $H1 ≡ $H ];

protected symbol comma_basechange_gamma_target_link [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@Transf K Y (@comma_section_gamma_target_observed_op K X Y J A D h)
     (@represented_comma_hom_action_target_func K X Y J A D h))
≔ @TotalOp_transf (TotalOp_cat K) (TotalOp_cat Y) (@comma_basechange_gamma_target_raw0 K X Y J A D h) (@comma_basechange_gamma_target_raw2 K X Y J
  A D h) (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1);

// The original Sigma compositor, retaining its actual forward arrow.
protected symbol comma_sigma_compositor_omega [K : Cat] (E M D : τ (Catd K))
  (FF : τ (@Functord K E M)) (GG : τ (@Functord K M D))
  : τ (@OmegaEquivAlong (Functor_cat (@Sigma_cat K E) (@Sigma_cat K D))
    (@comp_cat_fapp0 (@Sigma_cat K E) (@Sigma_cat K M) (@Sigma_cat K D)
      (@sigma_map_func K M D GG) (@sigma_map_func K E M FF))
    (@sigma_map_func K E D (@comp_catd_fapp0 K E M D GG FF))
    (@comma_basechange_sigma_map_composition K E M D FF GG))
≔ @comma_strict_compositor_omega (@Catd_cat K) Cat_cat (@Sigma_func K) E M D GG FF;

// Keep the original whole first comparison, and map its inverse evidence.
protected symbol comma_basechange_gamma_target_step1_equiv [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
  : τ (@OmegaEquivAlong (Functor_cat (TotalOp_cat K) (TotalOp_cat Y))
    (@comma_basechange_gamma_target_raw0 K X Y J A D h)
    (@comma_basechange_gamma_target_raw1 K X Y J A D h)
    (@comma_basechange_gamma_target_step1 K X Y J A D h))
≔ @comma_whiskered_omega (TotalOp_cat K)
    (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J))
    (Product_cat (TotalOp_cat X) (TotalOp_cat Y)) (TotalOp_cat Y) (@one_cat_total_op Y Y1)
    (@represented_comma_family_underlying_func K X Y J A D h)
    (@Product_projR_func (TotalOp_cat X) (TotalOp_cat Y))
    (@comp_cat_fapp0
      (@Sigma_cat (TotalOp_cat X) (@represented_comma_family_catd X Y J))
      (@Sigma_cat (TotalOp_cat X) (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J)))
      (Product_cat (TotalOp_cat X) (TotalOp_cat Y))
      (@sigma_map_func (TotalOp_cat X)
        (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
        (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
        (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J))))
      (@sigma_map_func (TotalOp_cat X) (@represented_comma_family_catd X Y J)
        (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
        (@represented_comma_family_reframe X Y J)))
    (@sigma_map_func (TotalOp_cat X) (@represented_comma_family_catd X Y J)
      (@Const_catd (TotalOp_cat X) (TotalOp_cat Y)) (@comma_section_gamma_target_family_map X Y J))
    (@comma_basechange_sigma_map_composition (TotalOp_cat X)
      (@represented_comma_family_catd X Y J)
      (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
      (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
      (@represented_comma_family_reframe X Y J)
      (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J))))
    (@comma_sigma_compositor_omega (TotalOp_cat X)
      (@represented_comma_family_catd X Y J)
      (@homdc_op_edge_catd X Y (@represented_comma_prof X Y J))
      (@Const_catd (TotalOp_cat X) (TotalOp_cat Y))
      (@represented_comma_family_reframe X Y J)
      (@strict_transfor _ _ _ _ (@homdc_total_target_funcd X Y (@represented_comma_prof X Y J))));

// Restrict the whole base-change comparison with its actual inverse data.
protected symbol comma_basechange_gamma_target_step2_equiv [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
  : τ (@OmegaEquivAlong (Functor_cat (TotalOp_cat K) (TotalOp_cat Y))
    (@comma_basechange_gamma_target_raw1 K X Y J A D h)
    (@comma_basechange_gamma_target_raw2 K X Y J A D h)
    (@comma_basechange_gamma_target_step2 K X Y J A D h Y1))
≔ @comma_strict_omega_map
    (Functor_cat (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (TotalOp_cat Y))
    (Functor_cat (TotalOp_cat K) (TotalOp_cat Y))
    (@comp_cat_con_func (TotalOp_cat K)
      (@Sigma_cat (TotalOp_cat K) (@represented_comma_family_target K X Y J A)) (TotalOp_cat Y)
      (@section_total_func (TotalOp_cat K) (@represented_comma_family_target K X Y J A)
        (@represented_comma_family_section K X Y J A D h)))
    (@comma_basechange_observation_outer (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y)
      (@TotalOp_func K X A) (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J))
    (@comma_basechange_observation_inner (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y)
      (@TotalOp_func K X A) (@represented_comma_family_catd X Y J) (@comma_section_gamma_target_family_map X Y J))
    (@comma_basechange_observation_basechange (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y)
      (@one_cat_total_op Y Y1) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)
      (@comma_section_gamma_target_family_map X Y J))
    (@comma_basechange_observation_basechange_equiv (TotalOp_cat K) (TotalOp_cat X) (TotalOp_cat Y)
      (@one_cat_total_op Y Y1) (@TotalOp_func K X A) (@represented_comma_family_catd X Y J)
      (@comma_section_gamma_target_family_map X Y J));

// Compose the two actual whole comparisons with their retained inverses.
protected symbol comma_basechange_gamma_target_raw_link_equiv [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
  (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
  (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
  : τ (@OmegaEquivAlong (Functor_cat (TotalOp_cat K) (TotalOp_cat Y))
    (@comma_basechange_gamma_target_raw0 K X Y J A D h)
    (@comma_basechange_gamma_target_raw2 K X Y J A D h)
    (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1))
≔ @omega_equiv_along_comp (Functor_cat (TotalOp_cat K) (TotalOp_cat Y))
    (@comma_basechange_gamma_target_raw0 K X Y J A D h)
    (@comma_basechange_gamma_target_raw1 K X Y J A D h)
    (@comma_basechange_gamma_target_raw2 K X Y J A D h)
    (@comma_basechange_gamma_target_step1 K X Y J A D h)
    (@comma_basechange_gamma_target_step2 K X Y J A D h Y1)
    (@comma_basechange_gamma_target_step1_equiv K X Y J A D h Y1)
    (@comma_basechange_gamma_target_step2_equiv K X Y J A D h Y1);

protected symbol comma_basechange_gamma_target_link_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y) (@comma_section_gamma_target_observed_op K X Y J A D h)
   (@represented_comma_hom_action_target_func K X Y J A D h) (@comma_basechange_gamma_target_link K X Y J A D h Y1))
≔ @one_cat_transf_pointwise_omega_along K Y Y1
    (@comma_section_gamma_target_observed_op K X Y J A D h)
    (@represented_comma_hom_action_target_func K X Y J A D h)
    (@comma_basechange_gamma_target_link K X Y J A D h Y1)
    (λ x : τ (Obj K), @comma_total_op_omega_along Y
      (@fapp0 (TotalOp_cat K) (TotalOp_cat Y) (@comma_basechange_gamma_target_raw0 K X Y J A D h) x)
      (@fapp0 (TotalOp_cat K) (TotalOp_cat Y) (@comma_basechange_gamma_target_raw2 K X Y J A D h) x)
      (@tapp0_fapp0 (TotalOp_cat K) (TotalOp_cat Y)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h) x
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1))
      (@comma_strict_omega_map (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (TotalOp_cat Y)
        (@fapp0_func (TotalOp_cat K) (TotalOp_cat Y) x)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h)
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1)
        (@comma_basechange_gamma_target_raw_link_equiv K X Y J A D h Y1)));

protected symbol comma_basechange_gamma_target_section_to_native [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ
  (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ cat_zero) Y))
 : τ (@Transf K Y
  (@comma_section_gamma_target_section_op K X Y J A D h) (@represented_comma_hom_action_target_func K X Y J A D h))
≔ @comp_fapp0 (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
  (@comma_section_gamma_target_observed_op K X Y J A D h) (@represented_comma_hom_action_target_func K X Y J A D h)
  (@comma_basechange_gamma_target_link K X Y J A D h Y1) (@comma_section_gamma_target_extraction_op K X Y J A D h);

protected symbol comma_basechange_gamma_target_section_to_native_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
  (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
   (@represented_comma_hom_action_target_func K X Y J A D h)
     (@comma_basechange_gamma_target_section_to_native K X Y J A D h Y1))
≔ @omega_equiv_along_comp (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
  (@comma_section_gamma_target_observed_op K X Y J A D h) (@represented_comma_hom_action_target_func K X Y J A D h)
  (@comma_section_gamma_target_extraction_op K X Y J A D h) (@comma_basechange_gamma_target_link K X Y J A D h Y1)
  (@comma_section_gamma_target_extraction_equiv K X Y J A D h Y1) (@comma_basechange_gamma_target_link_equiv K X Y J A D h Y1);

// Group the original mapped graph section.

protected symbol comma_grouped_graph_section_stage1 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @section_postcomp_sec (TotalOp_cat K) (@comma_graph_middle_catd K Y (@comp_cat_fapp0 K X Y J A) D)
  (@Const_catd (TotalOp_cat K) (TotalOp_cat Y)) (@comp_catd_fapp0 (TotalOp_cat K) (@comma_graph_middle_catd K Y
  (@comp_cat_fapp0 K X Y J A) D) (@represented_comma_family_target K X Y J A) (@Const_catd (TotalOp_cat K)
  (TotalOp_cat Y)) (@comma_section_gamma_target_section_map K X Y J A) (@comma_graph_basechange_op_funcd K Y
  (@comp_cat_fapp0 K X Y J A) D)) (@comma_graph_middle_sec K Y (@comp_cat_fapp0 K X Y J A) D h);

protected symbol comma_grouped_graph_section_stage2 [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor
  K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @section_postcomp_sec (TotalOp_cat K) (@comma_graph_source_catd K) (@Const_catd (TotalOp_cat K) (TotalOp_cat Y))
  (@comp_catd_fapp0 (TotalOp_cat K) (@comma_graph_source_catd K) (@comma_graph_middle_catd K Y
  (@comp_cat_fapp0 K X Y J A) D) (@Const_catd (TotalOp_cat K) (TotalOp_cat Y)) (@comp_catd_fapp0 (TotalOp_cat K)
  (@comma_graph_middle_catd K Y (@comp_cat_fapp0 K X Y J A) D) (@represented_comma_family_target K X
  Y J A) (@Const_catd (TotalOp_cat K) (TotalOp_cat Y)) (@comma_section_gamma_target_section_map K X Y J A)
  (@comma_graph_basechange_op_funcd K Y (@comp_cat_fapp0 K X Y J A) D))
  (@comma_graph_sigma_op_funcd K Y (@comp_cat_fapp0 K X Y J A) D h)) (@hom_identity_graph_sec K);

// Classify the target section and retain the whole target inverse.

protected symbol comma_classification_target_projection [K X Y : Cat]
  (J : τ (Functor X Y)) (A : τ (Functor K X))
  : τ (@Functord (TotalOp_cat K)
      (@represented_comma_family_target K X Y J A)
      (@Const_catd (TotalOp_cat K) (TotalOp_cat Y)))
≔ @strict_transfor _ _ _ _
    (@TotalOp_funcd (Op_cat K)
      (@comma_graph_target_raw_catd K Y (@comp_cat_fapp0 K X Y J A))
      (@Const_catd (Op_cat K) Y)
      (@sigma_proj1_family_funcd (Op_cat K) Y
        (@comma_graph_rep_cart K Y (@comp_cat_fapp0 K X Y J A))));

protected symbol comma_classification_target_section_canonical [K X Y : Cat]
 (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
 (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @section_postcomp_sec (TotalOp_cat K)
   (@represented_comma_family_target K X Y J A)
   (@Const_catd (TotalOp_cat K) (TotalOp_cat Y))
   (@comma_classification_target_projection K X Y J A)
   (@represented_comma_family_section K X Y J A D h);

protected symbol comma_classification_middle_projection [K Y : Cat]
  (F D : τ (Functor K Y))
  : τ (@Functord (TotalOp_cat K) (@comma_graph_middle_catd K Y F D)
      (@Const_catd (TotalOp_cat K) (TotalOp_cat K)))
≔ @strict_transfor _ _ _ _
    (@TotalOp_funcd (Op_cat K) (@comma_graph_middle_raw_catd K Y F D)
      (@Const_catd (Op_cat K) K)
      (@sigma_proj1_family_funcd (Op_cat K) K (@comma_graph_middle_inner_cart K Y F D)));

protected symbol comma_classification_middle_section_projected [K X Y : Cat]
 (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
 (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (Functor (TotalOp_cat K) (TotalOp_cat K))
≔ @section_postcomp_sec (TotalOp_cat K)
   (@comma_graph_middle_catd K Y (@comp_cat_fapp0 K X Y J A) D)
   (@Const_catd (TotalOp_cat K) (TotalOp_cat K))
   (@comma_classification_middle_projection K Y (@comp_cat_fapp0 K X Y J A) D)
   (@comma_graph_middle_sec K Y (@comp_cat_fapp0 K X Y J A) D h);

protected symbol comma_classification_target_section_after_basechange [K X Y : Cat]
 (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K Y))
 (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (Functor (TotalOp_cat K) (TotalOp_cat Y))
≔ @comp_cat_fapp0 (TotalOp_cat K) (TotalOp_cat K) (TotalOp_cat Y)
   (@TotalOp_func K Y D) (@comma_classification_middle_section_projected K X Y J A D h);

protected symbol comma_classification_identity_section_projected (K : Cat)
  : τ (Functor (TotalOp_cat K) (TotalOp_cat K))
≔ @section_postcomp_sec (TotalOp_cat K) (@comma_graph_source_catd K)
    (@Const_catd (TotalOp_cat K) (TotalOp_cat K))
    (@strict_transfor _ _ _ _
      (@TotalOp_funcd (Op_cat K) (@comma_graph_source_raw_catd K)
        (@Const_catd (Op_cat K) K)
        (@sigma_proj1_family_funcd (Op_cat K) K (@hom_int K K (@id_func K)))))
    (@hom_identity_graph_sec K);

protected symbol comma_classification_raw_reindex [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y) (@comma_classification_target_section_canonical K X Y J A D h)
  (@comma_section_gamma_target_section K X Y J A D h))
≔ @id (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (@comma_classification_target_section_canonical K X Y J A D h);

protected symbol comma_classification_raw_basechange [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y) (@comma_classification_target_section_after_basechange K X Y J A D h)
  (@comma_classification_target_section_canonical K X Y J A D h))
≔ @id (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (@comma_classification_target_section_after_basechange K X Y J A D h);

protected symbol comma_classification_raw_sigma [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat K) (@comma_classification_identity_section_projected K) (@comma_classification_middle_section_projected K
  X Y J A D h))
≔ @id (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@comma_classification_identity_section_projected K);

protected symbol comma_classification_raw_identity [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat K) (@id_func (TotalOp_cat K)) (@comma_classification_identity_section_projected K))
≔ @id (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@id_func (TotalOp_cat K));

protected symbol comma_classification_raw_middle [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat K) (@id_func (TotalOp_cat K)) (@comma_classification_middle_section_projected K X Y J A D h))
≔ @comp_fapp0 (Functor_cat (TotalOp_cat K) (TotalOp_cat K)) (@id_func (TotalOp_cat K)) (@comma_classification_identity_section_projected
  K) (@comma_classification_middle_section_projected K X Y J A D h)
   (@comma_classification_raw_sigma K X Y J A D h) (@comma_classification_raw_identity K X Y J A D h);

protected symbol comma_classification_raw_post [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y) (@TotalOp_func K Y D) (@comma_classification_target_section_after_basechange K X Y J A D
  h))
≔ @transf_postwhisker (TotalOp_cat K) (TotalOp_cat K) (TotalOp_cat Y) (@TotalOp_func K Y D) (@id_func (TotalOp_cat K))
  (@comma_classification_middle_section_projected K X Y J A D h)
   (@comma_classification_raw_middle K X Y J A D h);

protected symbol comma_classification_raw_classification [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf (TotalOp_cat K) (TotalOp_cat Y) (@TotalOp_func K Y D) (@comma_section_gamma_target_section K X Y J A D h))
≔ @comp_fapp0 (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (@TotalOp_func K Y D) (@comma_classification_target_section_canonical K X Y J
  A D h) (@comma_section_gamma_target_section K X Y J A D h)
   (@comma_classification_raw_reindex K X Y J A D h)
   (@comp_fapp0 (Functor_cat (TotalOp_cat K) (TotalOp_cat Y)) (@TotalOp_func K Y D)
  (@comma_classification_target_section_after_basechange K X Y J A D h) (@comma_classification_target_section_canonical K X Y J A D h)
     (@comma_classification_raw_basechange K X Y J A D h) (@comma_classification_raw_post K X Y J A D h));

protected symbol comma_classification_target_section_to_supplied [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A)))))
 : τ (@Transf K Y (@comma_section_gamma_target_section_op K X Y J A D h) D)
≔ @TotalOp_transf (TotalOp_cat K) (TotalOp_cat Y) (@TotalOp_func K Y D) (@comma_section_gamma_target_section K X Y J A D h)
   (@comma_classification_raw_classification K X Y J A D h);

protected symbol comma_classification_target_section_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h) D
  (@comma_classification_target_section_to_supplied K X Y J A D h))
≔ @one_cat_transf_pointwise_omega_along K Y Y1 (@comma_section_gamma_target_section_op K X Y J A D h) D
  (@comma_classification_target_section_to_supplied K X Y J A D h)
   (λ x : τ (Obj K), @omega_equiv_along_refl Y (@fapp0 K Y D x));

// The original whole target comparison q∘Γ⇒D for OneCat(Y).
symbol one_cat_represented_comma_hom_action_target_to [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@Transf K Y (@represented_comma_hom_action_target_func K X Y J A D h) D)
≔ @comp_fapp0 (Functor_cat K Y) (@represented_comma_hom_action_target_func K X Y J A D h) (@comma_section_gamma_target_section_op K X
  Y J A D h) D (@comma_classification_target_section_to_supplied K X Y J A D h)
   (@omega_equiv_along_left_inv (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
  (@represented_comma_hom_action_target_func K X Y J A D h) (@comma_basechange_gamma_target_section_to_native K X Y J A D h Y1)
  (@comma_basechange_gamma_target_section_to_native_equiv K X Y J A D h Y1));

// Its fixed-forward equivalence retains the selected inverse and whole laws.
symbol one_cat_represented_comma_hom_action_target_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@StrictTransfor (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y) (@represented_comma_hom_action_target_func K X Y J A D h) D
  (@one_cat_represented_comma_hom_action_target_to K X Y J A D h Y1))
≔ @iso_evidence_omega_along (Functor_cat K Y) (@represented_comma_hom_action_target_func K X Y J A D h) D
   (@iso_evidence_comp (Functor_cat K Y) (@represented_comma_hom_action_target_func K X Y J A D h)
  (@comma_section_gamma_target_section_op K X Y J A D h) D
     (@omega_equiv_along_iso_evidence (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h) D
  (@comma_classification_target_section_to_supplied K X Y J A D h) (@comma_classification_target_section_equiv K X Y J A D h Y1))
     (@iso_evidence_sym (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
  (@represented_comma_hom_action_target_func K X Y J A D h)
       (@omega_equiv_along_iso_evidence (Functor_cat K Y) (@comma_section_gamma_target_section_op K X Y J A D h)
  (@represented_comma_hom_action_target_func K X Y J A D h) (@comma_basechange_gamma_target_section_to_native K X Y J A D h Y1)
  (@comma_basechange_gamma_target_section_to_native_equiv K X Y J A D h Y1))));


// Original Γ interface, specialized to the native Hom action of h.

symbol represented_comma_family_target_func [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X)) (D : τ (Functor K
  Y)) (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D)) : τ (Functor K Y)
≔ @represented_comma_hom_action_target_func K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h);

symbol one_cat_represented_comma_family_target_to [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D)) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@Transf K Y (@represented_comma_family_target_func K X Y J A D h) D)
≔ @one_cat_represented_comma_hom_action_target_to K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h) Y1;

symbol one_cat_represented_comma_family_target_equiv [K X Y : Cat] (J : τ (Functor X Y)) (A : τ (Functor K X))
 (D : τ (Functor K Y)) (h : τ (@Transf K Y (@comp_cat_fapp0 K X Y J A) D)) (Y1 : τ (IsNCat (cat_succ
  cat_zero) Y))
 : τ (@OmegaEquivAlong (Functor_cat K Y) (@represented_comma_family_target_func K X Y J A D h) D
  (@one_cat_represented_comma_family_target_to K X Y J A D h Y1))
≔ @one_cat_represented_comma_hom_action_target_equiv K X Y J A D (@tapp1_int_cart K Y (@comp_cat_fapp0 K X Y J A) D h) Y1;
