/* Automatic coherence for object paths into a genuinely discrete target. */
require open emdash.emdash3_2_groupoidal_object_maps;
require open emdash.emdash3_2_set_path_pointwise_transformation;

// Explicit structural/model obligation, not a new equivalence theorem.
// Functors into a zero-category form a zero-category.
constant symbol discrete_functor_category [A B : Cat]
  (B0 : τ (IsDiscreteCat B))
  : τ (IsDiscreteCat (Functor_cat A B));

// Structural closure, parallel to discrete_functor_category above: maps
// into a fibrewise discrete family have discrete modifications. All laxity
// data then lies in proposition-valued cells. This is a model obligation,
// not a theorem derived from component beta or an ambient strictness rule.
constant symbol discrete_functord_category [K : Cat]
  (E D : τ (Catd K))
  (D0 : Π y : τ (Obj K), τ (IsDiscreteCat (Fibre_cat D y)))
  : τ (IsDiscreteCat (@Functord_cat K E D));

// Core reflection, set-valued pointwise assembly, then the original core law.
symbol discrete_pointwise_transf [A B : Cat] (B0 : τ (IsDiscreteCat B)) (F G : τ (Functor A B))
  (p : Π x : τ (Obj A), τ (@= (Obj B) (@fapp0 A B F x) (@fapp0 A B G x)))
  : τ (@Transf A B F G)
≔ @comp_fapp0 (Functor_cat A B) F (@comp_cat_fapp0 A B B (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B)
  (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0))) G) G (@fapp0 _ _ (@comp_cat_con_fapp1_func
  A B B G (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B) (@groupoidal_core_retraction B
  (@is_discrete_cat_core_equiv B B0))) (@id_func B)) (@path_to_hom (Functor_cat B B) (@comp_cat_fapp0 B (Core_cat B) B
  (Core_incl_func B) (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0))) (@id_func B)
  (@omega_equiv_left_as_right_law Cat_cat (Core_cat B) B (Core_incl_func B) (@is_discrete_cat_core_equiv B B0))))
    (@comp_fapp0 (Functor_cat A B) F (@comp_cat_fapp0 A B B (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B)
      (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0))) F) (@comp_cat_fapp0 A B B
      (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B) (@groupoidal_core_retraction B
      (@is_discrete_cat_core_equiv B B0))) G) (@fapp0 _ _ (@comp_cat_cov_fapp1_func A (Core_cat B) B (Core_incl_func
      B) (@comp_cat_fapp0 A B (Core_cat B) (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0)) F)
      (@comp_cat_fapp0 A B (Core_cat B) (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0)) G))
      (@set_path_pointwise_transf A (Obj B) (@is_discrete_cat_obj_set B B0) (@comp_cat_fapp0 A B (Core_cat B)
      (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0)) F) (@comp_cat_fapp0 A B (Core_cat B)
      (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0)) G) (λ x : τ (Obj A), @eq_ap (Obj B)
      (Obj B)
  (λ b : τ (Obj B), @fapp0 B (Core_cat B) (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0)) b)
  (@fapp0 A B F x) (@fapp0 A B G x) (p x)))) (@fapp0 _ _ (@comp_cat_con_fapp1_func A B B F (@id_func B)
    (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B) (@groupoidal_core_retraction B
    (@is_discrete_cat_core_equiv B B0)))) (@path_to_hom (Functor_cat B B) (@id_func B) (@comp_cat_fapp0 B (Core_cat B)
    B (Core_incl_func B) (@groupoidal_core_retraction B (@is_discrete_cat_core_equiv B B0))) (@eq_sym (Functor B
    B) (@comp_cat_fapp0 B (Core_cat B) B (Core_incl_func B) (@groupoidal_core_retraction B
    (@is_discrete_cat_core_equiv B B0))) (@id_func B) (@omega_equiv_left_as_right_law Cat_cat (Core_cat B) B
    (Core_incl_func B) (@is_discrete_cat_core_equiv B B0))))));

// The target's genuine zero-dimensional profile turns that cell into a path.
symbol discrete_functor_path [A B : Cat] (B0 : τ (IsDiscreteCat B)) (F G : τ (Functor A B))
  (p : Π x : τ (Obj A), τ (@= (Obj B) (@fapp0 A B F x) (@fapp0 A B G x)))
  : τ (@= (Functor A B) F G)
≔ @hom_to_path (Functor_cat A B) (@discrete_functor_category A B B0) F G (@discrete_pointwise_transf A B
  B0 F G p);
