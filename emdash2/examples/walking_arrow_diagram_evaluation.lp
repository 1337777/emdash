/* The differential of a walking-arrow diagram is a whole transformation.
   No strict/lax arrow-category identification or kernel structure is claimed. */
require open emdash.emdash3_2_diagram_evaluation;
require open emdash.emdash3_2_walking_arrow;

symbol arrow_diagram_source [C : Cat]
  : τ (Functor (Functor_cat WalkingArrow_cat C) C)
≔ @diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_src;

symbol arrow_diagram_target [C : Cat]
  : τ (Functor (Functor_cat WalkingArrow_cat C) C)
≔ @diagram_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt;

symbol arrow_diagram_differential [C : Cat]
  : τ (@Transf_oplax (Functor_cat WalkingArrow_cat C) C
      (@arrow_diagram_source C) (@arrow_diagram_target C))
≔ @diagram_evaluation_transf WalkingArrow_cat C
    walking_arrow_src walking_arrow_tgt walking_arrow_generator;

assert (C : Cat) (F : τ (Functor WalkingArrow_cat C))
  ⊢ @fapp0 (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_source C) F
    ≡ @fapp0 WalkingArrow_cat C F walking_arrow_src;

assert (C : Cat) (F : τ (Functor WalkingArrow_cat C))
  ⊢ @fapp0 (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_target C) F
    ≡ @fapp0 WalkingArrow_cat C F walking_arrow_tgt;

assert (C : Cat) (F : τ (Functor WalkingArrow_cat C))
  ⊢ @tapp0_fapp0 (OddDual_cat (Functor_cat WalkingArrow_cat C)) (OddDual_cat C) (@OddDual_func (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_target C)) (@OddDual_func (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_source C)) F (@arrow_diagram_differential C)
    ≡ @fapp1_fapp0 WalkingArrow_cat C F
      walking_arrow_src walking_arrow_tgt walking_arrow_generator;

// Decode the existing whole Even-dual action before its object projection.
// This keeps the runtime assertion at an explicit common Hom classifier.
assert (C : Cat) (F G : τ (Functor WalkingArrow_cat C))
  (eta : τ (@Transf WalkingArrow_cat C F G))
  ⊢ @fapp0 (@Transf_cat WalkingArrow_cat C F G)
      (Hom_cat C (@fapp0 WalkingArrow_cat C F walking_arrow_src) (@fapp0 WalkingArrow_cat C G walking_arrow_tgt))
      (@EvenDual_func (EvenDual_cat (@Transf_cat WalkingArrow_cat C F G)) (EvenDual_cat (Hom_cat C (@fapp0 WalkingArrow_cat C F walking_arrow_src) (@fapp0 WalkingArrow_cat C G walking_arrow_tgt)))
        (@tapp1_func (OddDual_cat (Functor_cat WalkingArrow_cat C)) (OddDual_cat C)
          (@OddDual_func (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_target C))
          (@OddDual_func (Functor_cat WalkingArrow_cat C) C (@arrow_diagram_source C))
          G F (@arrow_diagram_differential C))) eta
    ≡ @tapp1_fapp0 WalkingArrow_cat C F G
      walking_arrow_src walking_arrow_tgt eta walking_arrow_generator;

// A concrete nonidentity component: evaluation on the identity diagram
// returns the original directed generator, not a newly postulated arrow.
assert ⊢ @tapp0_fapp0 (OddDual_cat (Functor_cat WalkingArrow_cat WalkingArrow_cat)) (OddDual_cat WalkingArrow_cat) (@OddDual_func (Functor_cat WalkingArrow_cat WalkingArrow_cat) WalkingArrow_cat (@arrow_diagram_target WalkingArrow_cat)) (@OddDual_func (Functor_cat WalkingArrow_cat WalkingArrow_cat) WalkingArrow_cat (@arrow_diagram_source WalkingArrow_cat)) (@id_func WalkingArrow_cat) (@arrow_diagram_differential WalkingArrow_cat)
  ≡ walking_arrow_generator;

assertnot ⊢ @fapp0 (Functor_cat WalkingArrow_cat WalkingArrow_cat) WalkingArrow_cat
    (@arrow_diagram_source WalkingArrow_cat) (@id_func WalkingArrow_cat)
  ≡ @fapp0 (Functor_cat WalkingArrow_cat WalkingArrow_cat) WalkingArrow_cat
    (@arrow_diagram_target WalkingArrow_cat) (@id_func WalkingArrow_cat);
