// The general evaluation has the opposite transformation profile.
// Read its encoded lax component; I/C and the shape arrow remain arbitrary.
/* Actual normalized sym-evaluation consumer of the scoped comparison. */
require open emdash.emdash3_2_walking_arrow_native_observation;

assert [I C : Cat] [i j : τ (Obj I)] (u : τ (Hom I i j))
  (p : τ (@IsLaxTransfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
    (@diagram_evaluation_transf I C i j u)))
  (d : τ (Functor I C)) ⊢
  @eq_refl (Hom C (@fapp0 I C d i) (@fapp0 I C d j)) (@tapp0_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i)) d
      (@lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
        (@make_lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
          (@diagram_evaluation_transf I C i j u) p)))
  : τ (@= (Hom C (@fapp0 I C d i) (@fapp0 I C d j)) (@tapp0_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i)) d
      (@lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
        (@make_lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
          (@diagram_evaluation_transf I C i j u) p))) (@fapp1_fapp0 I C d i j u));

assertnot [I C : Cat] [i j : τ (Obj I)] (u : τ (Hom I i j))
  (p : τ (@IsLaxTransfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
    (@diagram_evaluation_transf I C i j u)))
  (d : τ (Functor I C)) ⊢
  (@tapp0_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i)) d
      (@lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
        (@make_lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
          (@diagram_evaluation_transf I C i j u) p))) ≡ @fapp1_fapp0 I C d i j u;

assertnot [I C : Cat] [i j : τ (Obj I)] (u : τ (Hom I i j))
  (p : τ (@IsLaxTransfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
    (@diagram_evaluation_transf I C i j u)))
  (d : τ (Functor I C)) (v : τ (Hom I i j)) ⊢
  @eq_refl (Hom C (@fapp0 I C d i) (@fapp0 I C d j)) (@tapp0_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i)) d
      (@lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
        (@make_lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
          (@diagram_evaluation_transf I C i j u) p)))
  : τ (@= (Hom C (@fapp0 I C d i) (@fapp0 I C d j)) (@tapp0_fapp0 (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i)) d
      (@lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
        (@make_lax_transfor (OddDual_cat (Functor_cat I C)) (OddDual_cat C)
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C j))
      (@OddDual_func (Functor_cat I C) C (@diagram_evaluation_at_func I C i))
          (@diagram_evaluation_transf I C i j u) p))) (@fapp1_fapp0 I C d i j v));
