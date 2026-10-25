/* Derived whole arrow-family isomorphism from an invertible modification.
   All parameter action is in existing whole maps. The original inverse is
   retained; ordinary diagram reflection supplies the inverse-law evidence. */
require open emdash.emdash3_2_one_cat_diagram_family_reflection;
require open emdash.emdash3_2_one_cat_arrow_diagrams;

require open emdash.emdash3_2_strict_functor_actions;

// Name the original two square maps before applying ordinary exchange.
// These definitions keep the selected modifications explicit and shared.

symbol one_cat_arrow_family_square_to [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (Hom (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k))
≔ @one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
    F F G G h k (@id (Functor_cat B C) F) (@id (Functor_cat B C) G)
    (@iso_evidence_to (Hom_cat (Functor_cat B C) F G) h k i);

symbol one_cat_arrow_family_square_from [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (Hom (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G h))
≔ @one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
    F F G G k h (@id (Functor_cat B C) F) (@id (Functor_cat B C) G)
    (@iso_evidence_from (Hom_cat (Functor_cat B C) F G) h k i);

// Reflect whole source diagrams, using the same endpoint identity facts.
symbol one_cat_arrow_family_square_left_law [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@= (Hom (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G h)) (@comp_fapp0 (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G h) (@one_cat_arrow_family_square_from B C C1 F G h k i) (@one_cat_arrow_family_square_to B C C1 F G h k i)) (@id (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h)))
≔ @one_cat_diagram_map_path (Functor_cat B C) (@one_cat_functor_category B C C1)
    (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G h) (@comp_fapp0 (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G h) (@one_cat_arrow_family_square_from B C C1 F G h k i) (@one_cat_arrow_family_square_to B C C1 F G h k i)) (@id (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h))
    (@eq_refl (Hom (Functor_cat B C) F F) (@id (Functor_cat B C) F))
    (@eq_refl (Hom (Functor_cat B C) G G) (@id (Functor_cat B C) G));

// Reflect whole source diagrams, using the same endpoint identity facts.
symbol one_cat_arrow_family_square_right_law [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@= (Hom (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G k)) (@comp_fapp0 (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k) (@one_cat_arrow_family_square_to B C C1 F G h k i) (@one_cat_arrow_family_square_from B C C1 F G h k i)) (@id (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k)))
≔ @one_cat_diagram_map_path (Functor_cat B C) (@one_cat_functor_category B C C1)
    (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G k) (@comp_fapp0 (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k) (@one_cat_arrow_family_square_to B C C1 F G h k i) (@one_cat_arrow_family_square_from B C C1 F G h k i)) (@id (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G k))
    (@eq_refl (Hom (Functor_cat B C) F F) (@id (Functor_cat B C) F))
    (@eq_refl (Hom (Functor_cat B C) G G) (@id (Functor_cat B C) G));

// Package only the original maps and their derived laws.
symbol one_cat_arrow_family_source_evidence [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (IsoEvidence (Functor_cat WalkingArrow_cat (Functor_cat B C)) (@walking_arrow_func (Functor_cat B C) F G h) (@walking_arrow_func (Functor_cat B C) F G k))
≔ Struct_sigma (@one_cat_arrow_family_square_to B C C1 F G h k i) (Struct_sigma (@one_cat_arrow_family_square_from B C C1 F G h k i) (Struct_sigma
    (@one_cat_arrow_family_square_left_law B C C1 F G h k i)
    (@one_cat_arrow_family_square_right_law B C C1 F G h k i)));

// Whole diagram action on the selected to modification.
symbol one_cat_arrow_family_comparison_to [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_transf_arrow_diagram_func B C C1 F G k))
≔ @one_cat_family_exchange_map WalkingArrow_cat B C C1
    (@walking_arrow_func (Functor_cat B C) F G h)
    (@walking_arrow_func (Functor_cat B C) F G k)
    (@one_cat_arrow_family_square_to B C C1 F G h k i);

// Whole diagram action on the selected from modification.
symbol one_cat_arrow_family_comparison_from [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1 F G k) (@one_cat_transf_arrow_diagram_func B C C1 F G h))
≔ @one_cat_family_exchange_map WalkingArrow_cat B C C1
    (@walking_arrow_func (Functor_cat B C) F G k)
    (@walking_arrow_func (Functor_cat B C) F G h)
    (@one_cat_arrow_family_square_from B C C1 F G h k i);

// The endpoints are identities; use existing whole-map reflection.
symbol one_cat_arrow_family_comparison_left_law [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@= (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_transf_arrow_diagram_func B C C1 F G h)) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_transf_arrow_diagram_func B C C1 F G k) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_arrow_family_comparison_from B C C1 F G h k i) (@one_cat_arrow_family_comparison_to B C C1 F G h k i)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1 F G h)))
≔ @iso_evidence_left
    (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_transf_arrow_diagram_func B C C1 F G h)
    (@one_cat_transf_arrow_diagram_func B C C1 F G k)
    (@iso_evidence_fmap
      (Functor_cat WalkingArrow_cat (Functor_cat B C))
      (Functor_cat B (Functor_cat WalkingArrow_cat C))
      (@one_cat_family_exchange_func WalkingArrow_cat B C C1)
      (@walking_arrow_func (Functor_cat B C) F G h)
      (@walking_arrow_func (Functor_cat B C) F G k)
      (@one_cat_arrow_family_source_evidence B C C1 F G h k i));

// The endpoints are identities; use existing whole-map reflection.
symbol one_cat_arrow_family_comparison_right_law [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (@= (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1 F G k) (@one_cat_transf_arrow_diagram_func B C C1 F G k)) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1 F G k) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_transf_arrow_diagram_func B C C1 F G k) (@one_cat_arrow_family_comparison_to B C C1 F G h k i) (@one_cat_arrow_family_comparison_from B C C1 F G h k i)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1 F G k)))
≔ @iso_evidence_right
    (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_transf_arrow_diagram_func B C C1 F G h)
    (@one_cat_transf_arrow_diagram_func B C C1 F G k)
    (@iso_evidence_fmap
      (Functor_cat WalkingArrow_cat (Functor_cat B C))
      (Functor_cat B (Functor_cat WalkingArrow_cat C))
      (@one_cat_family_exchange_func WalkingArrow_cat B C C1)
      (@walking_arrow_func (Functor_cat B C) F G h)
      (@walking_arrow_func (Functor_cat B C) F G k)
      (@one_cat_arrow_family_source_evidence B C C1 F G h k i));

// Keep the actual forward/inverse transformations in the existing isomorphism package.
symbol one_cat_arrow_family_comparison_evidence [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (IsoEvidence (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1 F G h) (@one_cat_transf_arrow_diagram_func B C C1 F G k))
≔ Struct_sigma (@one_cat_arrow_family_comparison_to B C C1 F G h k i) (Struct_sigma (@one_cat_arrow_family_comparison_from B C C1 F G h k i)
    (Struct_sigma (@one_cat_arrow_family_comparison_left_law B C C1 F G h k i)
      (@one_cat_arrow_family_comparison_right_law B C C1 F G h k i)));

// Native oplax view of the same original square maps and their inverse data.
// The source evidence already exists; only the whole exchange target changes.
symbol one_cat_oplax_arrow_family_comparison_evidence [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [F G : τ (Functor B C)] [h k : τ (@Transf B C F G)]
  (i : τ (IsoEvidence (Hom_cat (Functor_cat B C) F G) h k))
  : τ (IsoEvidence (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
      (@transf_arrow_diagram_func B C F G h) (@transf_arrow_diagram_func B C F G k))
≔ @iso_evidence_fmap (Functor_cat WalkingArrow_cat (Functor_cat B C))
    (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@one_cat_family_oplax_exchange_func WalkingArrow_cat B C C1)
    (@walking_arrow_func (Functor_cat B C) F G h)
    (@walking_arrow_func (Functor_cat B C) F G k)
    (@one_cat_arrow_family_source_evidence B C C1 F G h k i);
