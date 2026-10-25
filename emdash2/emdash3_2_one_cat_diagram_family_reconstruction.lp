/* Whole reconstruction at the actual supplied walking-arrow family D.
   The two existing maps are unchanged. They inherit the declared ordinary
   reconstruction at Functor_cat(B,C) and exchange its parameter axis.
   No terminal-family normalization or kernel/cokernel choices are inputs. */
require open emdash.emdash3_2_one_cat_diagram_family_reflection;
require open emdash.emdash3_2_one_cat_diagram_reconstruction;

// Apply the existing forward reconstruction to Sym(D), then exchange back.
symbol one_cat_diagram_family_reconstruction_to [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_cat WalkingArrow_cat C)))
  : τ (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1 (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
    (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D)
≔ @one_cat_family_exchange_map WalkingArrow_cat B C C1 (@walking_arrow_func (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
  (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
  (@one_cat_family_exchange B WalkingArrow_cat C C1 D)
    (@one_cat_diagram_reconstruction_to (Functor_cat B C) (@one_cat_functor_category B C C1) (@one_cat_family_exchange B WalkingArrow_cat C C1 D));

// Reconstruct Sym(D) in Functor_cat(B,C), then exchange back, retaining D.
symbol one_cat_diagram_family_reconstruction_from [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_cat WalkingArrow_cat C)))
  : τ (@Transf B (Functor_cat WalkingArrow_cat C) D
      (@one_cat_transf_arrow_diagram_func B C C1
        (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
        (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
        (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
≔ @one_cat_family_exchange_map WalkingArrow_cat B C C1
    (@one_cat_family_exchange B WalkingArrow_cat C C1 D)
    (@walking_arrow_func (Functor_cat B C)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@one_cat_diagram_reconstruction_from (Functor_cat B C) (@one_cat_functor_category B C C1)
      (@one_cat_family_exchange B WalkingArrow_cat C C1 D));


// Existing reconstruction maps are inverse as whole diagram transformations.
symbol one_cat_diagram_family_reconstruction_left_law [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B (Functor_cat WalkingArrow_cat C) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))))
≔ @one_cat_diagram_family_map_path B C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
    (@eq_trans (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D)) walking_arrow_src) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))) walking_arrow_src)
      (@one_cat_diagram_family_exchange_comp_path B WalkingArrow_cat C C1 walking_arrow_src (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D))
      (@eq_sym (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))) walking_arrow_src) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@fapp1_id_path (Functor_cat B (Functor_cat WalkingArrow_cat C)) (Functor_cat B C) (@one_cat_diagram_family_evaluation_func B WalkingArrow_cat C C1 walking_arrow_src) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)))))
    (@eq_trans (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D)) walking_arrow_tgt) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))) walking_arrow_tgt)
      (@one_cat_diagram_family_exchange_comp_path B WalkingArrow_cat C C1 walking_arrow_tgt (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_family_reconstruction_from B C C1 D) (@one_cat_diagram_family_reconstruction_to B C C1 D))
      (@eq_sym (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator))) walking_arrow_tgt) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@fapp1_id_path (Functor_cat B (Functor_cat WalkingArrow_cat C)) (Functor_cat B C) (@one_cat_diagram_family_evaluation_func B WalkingArrow_cat C C1 walking_arrow_tgt) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)))));

// Existing reconstruction maps are inverse as whole diagram transformations.
symbol one_cat_diagram_family_reconstruction_right_law [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B (Functor_cat WalkingArrow_cat C) D D) (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D))
≔ @one_cat_diagram_family_map_path B C C1 D D (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D)) (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D)
    (@eq_trans (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D)) walking_arrow_src) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D) walking_arrow_src)
      (@one_cat_diagram_family_exchange_comp_path B WalkingArrow_cat C C1 walking_arrow_src D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D))
      (@eq_sym (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D) walking_arrow_src) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)) (@fapp1_id_path (Functor_cat B (Functor_cat WalkingArrow_cat C)) (Functor_cat B C) (@one_cat_diagram_family_evaluation_func B WalkingArrow_cat C C1 walking_arrow_src) D)))
    (@eq_trans (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@comp_fapp0 (Functor_cat B (Functor_cat WalkingArrow_cat C)) D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D)) walking_arrow_tgt) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D) walking_arrow_tgt)
      (@one_cat_diagram_family_exchange_comp_path B WalkingArrow_cat C C1 walking_arrow_tgt D (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D (@one_cat_diagram_family_reconstruction_to B C C1 D) (@one_cat_diagram_family_reconstruction_from B C C1 D))
      (@eq_sym (@Transf B C (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 D D (@id (Functor_cat B (Functor_cat WalkingArrow_cat C)) D) walking_arrow_tgt) (@id (Functor_cat B C) (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)) (@fapp1_id_path (Functor_cat B (Functor_cat WalkingArrow_cat C)) (Functor_cat B C) (@one_cat_diagram_family_evaluation_func B WalkingArrow_cat C C1 walking_arrow_tgt) D)));

// Retain both original maps; equality fields certify laws, not operational casts.
symbol one_cat_diagram_family_reconstruction_evidence [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat WalkingArrow_cat C)))
  : τ (IsoEvidence (Functor_cat B (Functor_cat WalkingArrow_cat C)) (@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D)
≔ Struct_sigma (@one_cat_diagram_family_reconstruction_to B C C1 D) (Struct_sigma (@one_cat_diagram_family_reconstruction_from B C C1 D)
    (Struct_sigma (@one_cat_diagram_family_reconstruction_left_law B C C1 D)
      (@one_cat_diagram_family_reconstruction_right_law B C C1 D)));

require open emdash.emdash3_2_iso_evidence_constructors;
require open emdash.emdash3_2_strict_functor_actions;

// Retain the original ordinary reconstruction maps. Their endpoint
// components are identities, so the existing walking-diagram reflection
// derives their inverse laws without any new universality assumption.
symbol one_cat_diagram_reconstruction_evidence [C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (d : τ (Functor WalkingArrow_cat C))
  : τ (IsoEvidence (Functor_cat WalkingArrow_cat C)
      (@walking_arrow_func C (fapp0 d walking_arrow_src) (fapp0 d walking_arrow_tgt)
        (@fapp1_fapp0 WalkingArrow_cat C d walking_arrow_src walking_arrow_tgt walking_arrow_generator)) d)
≔ let S : Cat ≔ Functor_cat WalkingArrow_cat C in
  let r : τ (Functor WalkingArrow_cat C) ≔ @walking_arrow_func C
    (fapp0 d walking_arrow_src) (fapp0 d walking_arrow_tgt)
    (@fapp1_fapp0 WalkingArrow_cat C d walking_arrow_src walking_arrow_tgt walking_arrow_generator) in
  let t : τ (@Transf WalkingArrow_cat C r d) ≔ @one_cat_diagram_reconstruction_to C C1 d in
  let s : τ (@Transf WalkingArrow_cat C d r) ≔ @one_cat_diagram_reconstruction_from C C1 d in
  @iso_evidence_intro S r d t s
    (@one_cat_diagram_map_path C C1 r r (@comp_fapp0 S r d r s t) (@id S r)
      (@eq_refl (Hom C (fapp0 d walking_arrow_src) (fapp0 d walking_arrow_src))
        (@id C (fapp0 d walking_arrow_src)))
      (@eq_refl (Hom C (fapp0 d walking_arrow_tgt) (fapp0 d walking_arrow_tgt))
        (@id C (fapp0 d walking_arrow_tgt))))
    (@one_cat_diagram_map_path C C1 d d (@comp_fapp0 S d r d t s) (@id S d)
      (@eq_refl (Hom C (fapp0 d walking_arrow_src) (fapp0 d walking_arrow_src))
        (@id C (fapp0 d walking_arrow_src)))
      (@eq_refl (Hom C (fapp0 d walking_arrow_tgt) (fapp0 d walking_arrow_tgt))
        (@id C (fapp0 d walking_arrow_tgt))));

// Native oplax-family reconstruction is the image of that same ordinary
// source evidence. The whole double exchange retains the actual family D.
symbol one_cat_oplax_diagram_family_reconstruction_evidence [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (IsoEvidence (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
      (@transf_arrow_diagram_func B C
        (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
          (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D)
        (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C
          (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D)
        (@diagram_oplax_family_transf B WalkingArrow_cat C D
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D)
≔ let E : τ (Functor WalkingArrow_cat (Functor_cat B C)) ≔
    @diagram_oplax_family_shape_func B WalkingArrow_cat C D in
  let r : τ (Functor WalkingArrow_cat (Functor_cat B C)) ≔
    @walking_arrow_func (Functor_cat B C) (fapp0 E walking_arrow_src) (fapp0 E walking_arrow_tgt)
      (@fapp1_fapp0 WalkingArrow_cat (Functor_cat B C) E
        walking_arrow_src walking_arrow_tgt walking_arrow_generator) in
  @iso_evidence_fmap (Functor_cat WalkingArrow_cat (Functor_cat B C))
    (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@one_cat_family_oplax_exchange_func WalkingArrow_cat B C C1) r E
    (@one_cat_diagram_reconstruction_evidence (Functor_cat B C)
      (@one_cat_functor_category B C C1) E);

// Maps of the existing whole native reconstruction evidence.
symbol one_cat_oplax_diagram_family_reconstruction_to [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D)
≔ @one_cat_family_oplax_exchange_map WalkingArrow_cat B C C1 (@walking_arrow_func (Functor_cat B C) (@fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_src) (@fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_tgt) (@fapp1_fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) (@one_cat_diagram_reconstruction_to (Functor_cat B C) (@one_cat_functor_category B C C1) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D));
symbol one_cat_oplax_diagram_family_reconstruction_from [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) D (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
≔ @one_cat_family_oplax_exchange_map WalkingArrow_cat B C C1 (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) (@walking_arrow_func (Functor_cat B C) (@fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_src) (@fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_tgt) (@fapp1_fapp0 WalkingArrow_cat (Functor_cat B C) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D) walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_diagram_reconstruction_from (Functor_cat B C) (@one_cat_functor_category B C C1) (@diagram_oplax_family_shape_func B WalkingArrow_cat C D));

// Whole endpoint laws of the same native reconstruction maps.
symbol one_cat_oplax_reconstruction_to_src_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
      (@one_cat_oplax_diagram_family_reconstruction_to B C C1 D) walking_arrow_src)
    (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D)))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) in
  let alpha : τ (@Transf B C X X) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
      (@one_cat_oplax_diagram_family_reconstruction_to B C C1 D) walking_arrow_src) in
  let beta : τ (@Transf B C X X) ≔ (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D)) in
  @hom_to_path (@Transf_cat B C X X) ((@one_cat_functor_category B C C1) X X) alpha beta
    (@one_cat_modification B C C1 X X alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (@fapp0 B C X b) (@fapp0 B C X b))
        (@tapp0_fapp0 B C X X b alpha) (@tapp0_fapp0 B C X X b beta)
        (@eq_refl (Hom C (@fapp0 B C X b) (@fapp0 B C X b)) (@tapp0_fapp0 B C X X b beta))));
symbol one_cat_oplax_reconstruction_to_tgt_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
      (@one_cat_oplax_diagram_family_reconstruction_to B C C1 D) walking_arrow_tgt)
    (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D)))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) in
  let alpha : τ (@Transf B C X X) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) D
      (@one_cat_oplax_diagram_family_reconstruction_to B C C1 D) walking_arrow_tgt) in
  let beta : τ (@Transf B C X X) ≔ (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D)) in
  @hom_to_path (@Transf_cat B C X X) ((@one_cat_functor_category B C C1) X X) alpha beta
    (@one_cat_modification B C C1 X X alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (@fapp0 B C X b) (@fapp0 B C X b))
        (@tapp0_fapp0 B C X X b alpha) (@tapp0_fapp0 B C X X b beta)
        (@eq_refl (Hom C (@fapp0 B C X b) (@fapp0 B C X b)) (@tapp0_fapp0 B C X X b beta))));
symbol one_cat_oplax_reconstruction_from_src_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D) walking_arrow_src)
    (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D)))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) in
  let alpha : τ (@Transf B C X X) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D) walking_arrow_src) in
  let beta : τ (@Transf B C X X) ≔ (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D)) in
  @hom_to_path (@Transf_cat B C X X) ((@one_cat_functor_category B C C1) X X) alpha beta
    (@one_cat_modification B C C1 X X alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (@fapp0 B C X b) (@fapp0 B C X b))
        (@tapp0_fapp0 B C X X b alpha) (@tapp0_fapp0 B C X X b beta)
        (@eq_refl (Hom C (@fapp0 B C X b) (@fapp0 B C X b)) (@tapp0_fapp0 B C X X b beta))));
symbol one_cat_oplax_reconstruction_from_tgt_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D))
    (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D) walking_arrow_tgt)
    (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D)))
≔ let X : τ (Functor B C) ≔ (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) in
  let alpha : τ (@Transf B C X X) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C D (@transf_arrow_diagram_func B C (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) D) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D) walking_arrow_tgt) in
  let beta : τ (@Transf B C X X) ≔ (@id (Functor_cat B C) (@comp_cat_fapp0 B (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) D)) in
  @hom_to_path (@Transf_cat B C X X) ((@one_cat_functor_category B C C1) X X) alpha beta
    (@one_cat_modification B C C1 X X alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (@fapp0 B C X b) (@fapp0 B C X b))
        (@tapp0_fapp0 B C X X b alpha) (@tapp0_fapp0 B C X X b beta)
        (@eq_refl (Hom C (@fapp0 B C X b) (@fapp0 B C X b)) (@tapp0_fapp0 B C X X b beta))));
