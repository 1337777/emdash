/* The original arbitrary D and selected reconstruction maps are retained. */
require open emdash.emdash3_2_one_cat_diagram_family_reconstruction;
// catalog-area: Whole arrow-family categorical isomorphisms

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D
        walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
    (@one_cat_diagram_family_reconstruction_to B C C1 D) walking_arrow_src
  ≡ @id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src);

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D
        walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
    (@one_cat_diagram_family_reconstruction_to B C C1 D) walking_arrow_tgt
  ≡ @id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt);

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D
        walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@one_cat_diagram_family_reconstruction_from B C C1 D) walking_arrow_src
  ≡ @id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src);

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D
        walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@one_cat_diagram_family_reconstruction_from B C C1 D) walking_arrow_tgt
  ≡ @id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt);

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @iso_evidence_to (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
    (@one_cat_diagram_family_reconstruction_evidence B C C1 D) ≡ (@one_cat_diagram_family_reconstruction_to B C C1 D);

assert [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C))) ⊢
  @iso_evidence_from (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
    (@one_cat_diagram_family_reconstruction_evidence B C C1 D) ≡ (@one_cat_diagram_family_reconstruction_from B C C1 D);
