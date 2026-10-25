/*
  NON-LIBRARY varying-shape evaluation, at the original extension boundary.
  Fixed evaluation is ordinary postcomposition. Shape variation uses the
  opposite transformation profile; it is not Cartesian exchange on lax maps.
  Odd/Even refer to dimensions 1,3,... / 2,4,..., not the existing Op_cat.
*/
require open emdash.emdash3_2;

// Alternating dualities: the Hom recursion exchanges odd and even dimensions.
injective symbol OddDual_cat (A : Cat) : Cat;
injective symbol EvenDual_cat (A : Cat) : Cat;
rule OddDual_cat (OddDual_cat $A) ↪ $A;
rule EvenDual_cat (EvenDual_cat $A) ↪ $A;
rule Obj (OddDual_cat $A) ↪ Obj $A;
rule Obj (EvenDual_cat $A) ↪ Obj $A;
rule Hom_cat (OddDual_cat $A) $x $y ↪ EvenDual_cat (Hom_cat $A $y $x);
rule Hom_cat (EvenDual_cat $A) $x $y ↪ OddDual_cat (Hom_cat $A $x $y);
rule @id (OddDual_cat $A) $x ↪ @id $A $x;
rule @id (EvenDual_cat $A) $x ↪ @id $A $x;

// Strict-functor identity after the source identity has lost its dual tag.
// These are the alternating-duality counterparts of the existing T/R joins.
// lhs-audit: keep 1 -- the Odd source determines the erased identity's actual category.
rule @fapp1_fapp0 (OddDual_cat $A) $B $F $x $x (@id $A $x)
  ↪ @id $B (@fapp0 (OddDual_cat $A) $B $F $x);
// lhs-audit: keep 1 -- the Even source occurs at the next Hom of an oplax diagram.
rule @fapp1_fapp0 (EvenDual_cat $A) $B $F $x $x (@id $A $x)
  ↪ @id $B (@fapp0 (EvenDual_cat $A) $B $F $x);

// The same source-identity join for a normal transfor component. Native
// prewhiskering reaches this after OddDual has erased the identity's tag.
// lhs-audit: keep 1 -- measured odd-dual source/identity projection overlap.
rule @tapp1_fapp0 (OddDual_cat $A) $B $F $G $x $x $eta (@id $A $x)
  ↪ @tapp0_fapp0 (OddDual_cat $A) $B $F $G $x $eta;

rule @comp_fapp0 (OddDual_cat $A) $x $y $z $g $f
  ↪ @comp_fapp0 $A $z $y $x $f $g;
rule @comp_fapp0 (EvenDual_cat $A) $x $y $z $g $f
  ↪ @comp_fapp0 $A $x $y $z $g $f;

// Triangle cuts after odd-dual composition reverses its two arrows.
// Explicit encoded action types are subject-reduction guards; the same
// adjunction witness, its actual functors and both input arrows are retained.
// lhs-audit: keep 1 -- erased odd-dual composition carrier.
rule @comp_fapp0 $L _ _ _
      (@fapp1_fapp0 $R (OddDual_cat $L) $F $X
        (@fapp0 (OddDual_cat $L) $R $G (@fapp0 $R (OddDual_cat $L) $F $X'))
        (@tapp1_fapp0 $R $R (@id Cat_cat $R)
          (@comp_fapp0 Cat_cat $R (OddDual_cat $L) $R $G $F) $X $X'
          (@unit_adj_transf $R (OddDual_cat $L) $F $G $J) $g))
      (@tapp1_fapp0 (OddDual_cat $L) (OddDual_cat $L)
        (@comp_fapp0 Cat_cat (OddDual_cat $L) $R (OddDual_cat $L) $F $G)
        (@id Cat_cat (OddDual_cat $L))
        (@fapp0 $R (OddDual_cat $L) $F $X') $Y
        (@counit_adj_transf $R (OddDual_cat $L) $F $G $J) $f)
  ↪ @comp_fapp0 $L $Y (@fapp0 $R (OddDual_cat $L) $F $X') (@fapp0 $R (OddDual_cat $L) $F $X)
      (@fapp1_fapp0 $R (OddDual_cat $L) $F $X $X' $g) $f;

// lhs-audit: keep 1 -- the dual source category has erased its outer tag.
rule @comp_fapp0 $R _ _ _
      (@tapp1_fapp0 (OddDual_cat $R) (OddDual_cat $R)
        (@id Cat_cat (OddDual_cat $R))
        (@comp_fapp0 Cat_cat (OddDual_cat $R) $L (OddDual_cat $R) $G $F)
        $X (@fapp0 $L (OddDual_cat $R) $G $Y')
        (@unit_adj_transf (OddDual_cat $R) $L $F $G $J) $f)
      (@fapp1_fapp0 $L (OddDual_cat $R) $G
        (@fapp0 (OddDual_cat $R) $L $F (@fapp0 $L (OddDual_cat $R) $G $Y')) $Y
        (@tapp1_fapp0 $L $L
          (@comp_fapp0 Cat_cat $L (OddDual_cat $R) $L $F $G) (@id Cat_cat $L) $Y' $Y
          (@counit_adj_transf (OddDual_cat $R) $L $F $G $J) $g))
  ↪ @comp_fapp0 $R (@fapp0 $L (OddDual_cat $R) $G $Y) (@fapp0 $L (OddDual_cat $R) $G $Y') $X
      $f (@fapp1_fapp0 $L (OddDual_cat $R) $G $Y' $Y $g);

// The same strict functor on the alternating duals, with whole Hom action.
injective symbol OddDual_func [A B : Cat] (F : τ (Functor A B))
  : τ (Functor (OddDual_cat A) (OddDual_cat B));
injective symbol EvenDual_func [A B : Cat] (F : τ (Functor A B))
  : τ (Functor (EvenDual_cat A) (EvenDual_cat B));
rule @OddDual_func _ _ (@OddDual_func _ _ $F) ↪ $F;
rule @EvenDual_func _ _ (@EvenDual_func _ _ $F) ↪ $F;
rule @fapp0 _ _ (@OddDual_func $A $B $F) $x ↪ @fapp0 $A $B $F $x;
rule @fapp0 _ _ (@EvenDual_func $A $B $F) $x ↪ @fapp0 $A $B $F $x;
rule @fapp1_func _ _ (@OddDual_func $A $B $F) $x $y
  ↪ @EvenDual_func (Hom_cat $A $y $x)
      (Hom_cat $B (fapp0 $F $y) (fapp0 $F $x))
      (@fapp1_func $A $B $F $y $x);
rule @fapp1_func _ _ (@EvenDual_func $A $B $F) $x $y
  ↪ @OddDual_func (Hom_cat $A $x $y)
      (Hom_cat $B (fapp0 $F $x) (fapp0 $F $y))
      (@fapp1_func $A $B $F $x $y);
rule @fapp1_fapp0 _ _ (@OddDual_func $A $B $F) $x $y $u
  ↪ @fapp1_fapp0 $A $B $F $y $x $u;
rule @fapp1_fapp0 _ _ (@EvenDual_func $A $B $F) $x $y $u
  ↪ @fapp1_fapp0 $A $B $F $x $y $u;
rule @OddDual_func _ _ (@id Cat_cat $A) ↪ @id_func (OddDual_cat $A);
rule @EvenDual_func _ _ (@id Cat_cat $A) ↪ @id_func (EvenDual_cat $A);
rule @OddDual_func _ _ (@comp_fapp0 Cat_cat $A $B $C $G $F)
  ↪ @comp_cat_fapp0 (OddDual_cat $A) (OddDual_cat $B) (OddDual_cat $C)
      (@OddDual_func $B $C $G) (@OddDual_func $A $B $F);
rule @EvenDual_func _ _ (@comp_fapp0 Cat_cat $A $B $C $G $F)
  ↪ @comp_cat_fapp0 (EvenDual_cat $A) (EvenDual_cat $B) (EvenDual_cat $C)
      (@EvenDual_func $B $C $G) (@EvenDual_func $A $B $F);

// Duality acts on the retained precomposition presentation of a strict
// composite. Preserve its owner rather than unfold it to raw composition.
rule @OddDual_func _ _
      (@hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        $C $A $B $F $G)
  ↪ @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
      (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat $B)
      (@OddDual_func $A $B $F) (@OddDual_func $B $C $G);

// Read represented postcomposition in Odd(A) after ordinary composition
// has reversed its arguments. Preserve both runtime owners and all data.
unif_rule
  @hom_postcomp_fapp0 _ _ (@OddDual_func $B $A $F) $W $X $Y $p $g
  ≡ @comp_fapp0 $A1 $a $b $c $g1 $p1
  ↪ [ $A1 ≡ $A; $a ≡ @fapp0 $B $A $F $Y;
      $b ≡ @fapp0 $B $A $F $X; $c ≡ $W; $g1 ≡ $g;
      $p1 ≡ @fapp1_fapp0 $B $A $F $Y $X $p ];

// Opposite transformation profile, using the conventional omega-lax Hom.
// Objects encode F by OddDual_func(F); no object-classifier identification.
symbol Functor_oplax_cat (A B : Cat) : Cat
≔ OddDual_cat (Functor_cat (OddDual_cat A) (OddDual_cat B));
symbol Transf_oplax_cat [A B : Cat] (F G : τ (Functor A B)) : Cat
≔ Hom_cat (Functor_oplax_cat A B) (@OddDual_func A B F) (@OddDual_func A B G);
symbol Transf_oplax [A B : Cat] (F G : τ (Functor A B)) : Grpd
≔ Obj (@Transf_oplax_cat A B F G);

// General fixed evaluation and family evaluation need no exchange operation.
symbol diagram_evaluation_at_func [I C : Cat] (i : τ (Obj I))
  : τ (Functor (Functor_cat I C) C)
≔ @fapp0_func I C i;
symbol diagram_family_evaluation_func [K I C : Cat] (i : τ (Obj I))
  : τ (Functor (Functor_cat K (Functor_cat I C)) (Functor_cat K C))
≔ @comp_cat_cov_func K (Functor_cat I C) C (@diagram_evaluation_at_func I C i);
symbol diagram_family_at_func [K I C : Cat]
  (D : τ (Functor K (Functor_cat I C))) (i : τ (Obj I))
  : τ (Functor K C)
≔ @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id_func Cat_cat)
    C K (Functor_cat I C) D (@diagram_evaluation_at_func I C i);

// Whole mixed action in eta, obtained from the existing internal action by
// two component evaluations. Only this Cartesian-valued family is exchanged.
symbol diagram_evaluation_mixed_family [I C : Cat]
  (F G : τ (Functor I C)) (i j : τ (Obj I))
  : τ (Functor (@Transf_cat I C F G)
      (Functor_cart_cat (Hom_cat I i j)
        (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))))
≔ @comp_cat_fapp0 _ _ _
    (@tapp0_func I Cat_cart
      (@hom_ I I (@id_func I) i)
      (@hom_ C I G (@fapp0 I C F i)) j)
    (@comp_cat_fapp0 _ _ _
      (@tapp0_func (Op_cat I) (Catd_cat I)
        (@hom_int_view I I (@id_func I))
        (@comp_cat_fapp0 _ _ _ (@hom_int_view C I G) (@Op_func I C F)) i)
      (@tapp1_int_func_transf I C F G));
protected symbol diagram_evaluation_mixed_body [I C : Cat]
  [i j : τ (Obj I)] (u : τ (Hom I i j)) (F G : τ (Functor I C))
  : τ (Functor (@Transf_cat I C F G)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j)))
≔ @sym_fapp0_func (@Transf_cat I C F G) (Hom_cat I i j)
    (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
    (@diagram_evaluation_mixed_family I C F G i j) u;

// Stable projection of the derived mixed action. The old exchange-of-composite
// rule distributes the body before whole endpoint comparison can recognize it.
// Its object and complete Hom action still use the original internal action.
injective symbol diagram_evaluation_mixed_func [I C : Cat]
  [i j : τ (Obj I)] (u : τ (Hom I i j)) (F G : τ (Functor I C))
  : τ (Functor (@Transf_cat I C F G)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j)));
rule fapp0 (@diagram_evaluation_mixed_func $I $C $i $j $u $F $G) $eta
  ↪ @tapp1_fapp0 $I $C $F $G $i $j $eta $u;
rule @fapp1_func _ _ (@diagram_evaluation_mixed_func $I $C $i $j $u $F $G) $eta $theta
  ↪ @fapp1_func (@Transf_cat $I $C $F $G)
      (Hom_cat $C (@fapp0 $I $C $F $i) (@fapp0 $I $C $G $j))
      (@diagram_evaluation_mixed_body $I $C $i $j $u $F $G) $eta $theta;
rule @fapp1_fapp0 _ _ (@diagram_evaluation_mixed_func $I $C $i $j $u $F $G) $eta $theta $m
  ↪ @fapp1_fapp0 (@Transf_cat $I $C $F $G)
      (Hom_cat $C (@fapp0 $I $C $F $i) (@fapp0 $I $C $G $j))
      (@diagram_evaluation_mixed_body $I $C $i $j $u $F $G) $eta $theta $m;

// Structural whole evaluation owner. Its oplax direction is essential.
// Qualification requires the extracted comparison as well as these projections.
injective symbol diagram_evaluation_func [I C : Cat]
  : τ (Functor I (Functor_oplax_cat (Functor_cat I C) C));
injective symbol diagram_evaluation_hom_func [I C : Cat] (i j : τ (Obj I))
  : τ (Functor (Hom_cat I i j)
      (@Transf_oplax_cat (Functor_cat I C) C
        (@diagram_evaluation_at_func I C i) (@diagram_evaluation_at_func I C j)));
injective symbol diagram_evaluation_transf [I C : Cat]
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf_oplax (Functor_cat I C) C
      (@diagram_evaluation_at_func I C i) (@diagram_evaluation_at_func I C j));
rule @fapp0 _ _ (@diagram_evaluation_func $I $C) $i
  ↪ @OddDual_func (Functor_cat $I $C) $C (@diagram_evaluation_at_func $I $C $i);
rule @fapp1_func _ _ (@diagram_evaluation_func $I $C) $i $j
  ↪ @diagram_evaluation_hom_func $I $C $i $j;
rule fapp0 (@diagram_evaluation_hom_func $I $C $i $j) $u
  ↪ @diagram_evaluation_transf $I $C $i $j $u;
rule @fapp1_fapp0 _ _ (@diagram_evaluation_func $I $C) $i $j $u
  ↪ @diagram_evaluation_transf $I $C $i $j $u;
// The root functor's identity/composition laws after its action has projected.
rule @diagram_evaluation_transf $I $C $i $i (@id _ $i)
  ↪ @id (Functor_cat (OddDual_cat (Functor_cat $I $C)) (OddDual_cat $C))
      (@OddDual_func (Functor_cat $I $C) $C (@diagram_evaluation_at_func $I $C $i));
// lhs-audit: keep 1 -- the encoded mapping category is the measured SR guard.
rule @comp_fapp0 (Functor_cat (OddDual_cat (Functor_cat $I $C)) (OddDual_cat $C)) _ _ _
      (@diagram_evaluation_transf $I $C $i $j $u)
      (@diagram_evaluation_transf $I $C $j $k $v)
  ↪ @diagram_evaluation_transf $I $C $i $k (@comp_fapp0 $I $i $j $k $v $u);
rule @tapp0_fapp0 _ _ _ _ $F (@diagram_evaluation_transf $I $C $i $j $u)
  ↪ @fapp1_fapp0 $I $C $F $i $j $u;
// In the encoded lax transformation the two diagram endpoints are reversed.
rule @tapp1_func _ _ _ _ $G $F (@diagram_evaluation_transf $I $C $i $j $u)
  ↪ @EvenDual_func (@Transf_cat $I $C $F $G)
      (Hom_cat $C (@fapp0 $I $C $F $i) (@fapp0 $I $C $G $j))
      (@diagram_evaluation_mixed_func $I $C $i $j $u $F $G);
// Capped companion joins projection-first and whole-functor-first evaluation.
rule @tapp1_fapp0 _ _ _ _ $G $F (@diagram_evaluation_transf $I $C $i $j $u) $eta
  ↪ @tapp1_fapp0 $I $C $F $G $i $j $eta $u;
// Whole shape-Hom component: decode the Even-dual component functor,
// then evaluate the root Hom action. This preserves every further Hom action.
// The typed whole mapping categories determine the encoded component slots.
rule @comp_fapp0 Cat_cat _ _ _
      (@EvenDual_func _ _
        (@tapp0_func _ _ _ _ $F))
      (@diagram_evaluation_hom_func $I $C $i $j)
  ↪ @fapp1_func $I $C $F $i $j;

// Reindexing in the opposite transformation profile is ordinary
// precomposition on the encoded lax mapping category, then its odd dual.
symbol oplax_precomp_func [A B C : Cat] (D : τ (Functor A B))
  : τ (Functor (Functor_oplax_cat B C) (Functor_oplax_cat A C))
≔ @OddDual_func
    (Functor_cat (OddDual_cat B) (OddDual_cat C))
    (Functor_cat (OddDual_cat A) (OddDual_cat C))
    (@comp_cat_con_func (OddDual_cat A) (OddDual_cat B) (OddDual_cat C)
      (@OddDual_func A B D));

// Whole shape evaluation of a parameterized family; no pointwise assembly.
symbol diagram_family_shape_func [K I C : Cat]
  (D : τ (Functor K (Functor_cat I C)))
  : τ (Functor I (Functor_oplax_cat K C))
≔ @comp_cat_fapp0 I (Functor_oplax_cat (Functor_cat I C) C)
    (Functor_oplax_cat K C)
    (@oplax_precomp_func K (Functor_cat I C) C D)
    (@diagram_evaluation_func I C);
symbol diagram_family_transf [K I C : Cat]
  (D : τ (Functor K (Functor_cat I C)))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf_oplax K C
      (@diagram_family_at_func K I C D i) (@diagram_family_at_func K I C D j))
≔ @fapp1_fapp0 I (Functor_oplax_cat K C) (@diagram_family_shape_func K I C D) i j u;

// Oplax exchange instances of the existing two adjunction triangle cuts.
// The shape-action projection retains the existing prewhiskering head. Match
// that actual owner; retain the whole exchange inside the adjunction witness.
// No equality evidence or separately supplied comparison enters the operation.
// The explicit encoded categories and projection endpoints are SR guards:
// leaving them inferred produced raw-versus-Odd category constraints. The
// The existing action head retains the actual functor and transformation.

// Left triangle.
// lhs-audit: keep 1,3,4 -- normalized dual category and actual image endpoints are measured SR guards.
rule @comp_fapp0 (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) $Y (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $G (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X'))))))) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X)))
      (@hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $G (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X')))))) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X)) (@diagram_evaluation_transf $B $C $X (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $G (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X'))))
      (@tapp1_fapp0 $B $B _ _ $X $X'
        (@unit_adj_transf $B (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@comp_fapp0 Cat_cat $B (OddDual_cat (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@OddDual_func (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C)) (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_func Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H))) (@diagram_evaluation_func $B $C)) $G $J) $g)))
      (@tapp1_fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) _ _ (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X'))) $Y
        (@counit_adj_transf $B (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@comp_fapp0 Cat_cat $B (OddDual_cat (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@OddDual_func (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C)) (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_func Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H))) (@diagram_evaluation_func $B $C)) $G $J) $f)
  ↪ @comp_fapp0 (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) $Y (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X'))) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X)))
      (@hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X')) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $X)) (@diagram_evaluation_transf $B $C $X $X' $g)) $f;

// Right triangle.
// lhs-audit: keep 1,2,3 -- retain the independent endpoint and normalized dual image guards.
rule @comp_fapp0 (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y))) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $F (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y'))))))) $X
      (@tapp1_fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) _ _ $X (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y')))
        (@unit_adj_transf (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $F (@comp_fapp0 Cat_cat $B (OddDual_cat (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@OddDual_func (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C)) (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_func Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H))) (@diagram_evaluation_func $B $C)) $J) $f)
      (@hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y)) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $F (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y')))))) (@diagram_evaluation_transf $B $C (@fapp0 (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $F (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y')))) $Y
      (@tapp1_fapp0 $B $B _ _ $Y' $Y
        (@counit_adj_transf (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) $B $F (@comp_fapp0 Cat_cat $B (OddDual_cat (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C))) (OddDual_cat (Functor_cat (OddDual_cat $A) (OddDual_cat $C))) (@OddDual_func (Functor_cat (OddDual_cat (Functor_cat $B $C)) (OddDual_cat $C)) (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_func Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H))) (@diagram_evaluation_func $B $C)) $J) $g)))
  ↪ @comp_fapp0 (Functor_cat (OddDual_cat $A) (OddDual_cat $C)) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y))) (@hom_precomp_along_fapp0 Cat_cat Cat_cat (id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y'))) $X $f
      (@hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) (OddDual_cat $C) (OddDual_cat $A) (OddDual_cat (Functor_cat $B $C)) (@OddDual_func $A (Functor_cat $B $C) $H) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y)) (@OddDual_func (Functor_cat $B $C) $C (@fapp0_func $B $C $Y')) (@diagram_evaluation_transf $B $C $Y' $Y $g));

// The same shape-reindex comparison at the retained prewhiskering action head.
// Fixed precomposition composes contravariantly. All functors, endpoint views
// and the original transformation remain explicit constraints.
unif_rule
  @hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $C $A $B (@comp_fapp0 Cat_cat $A $M $B $G $F) $s $t $alpha
  ≡ @hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $C1 $A1 $M1 $F1 $s1 $t1 $beta
  ↪ [ $C1 ≡ $C; $A1 ≡ $A; $M1 ≡ $M; $F1 ≡ $F;
      $s1 ≡ @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        $C $M $B $G $s;
      $t1 ≡ @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        $C $M $B $G $t;
      $beta ≡ @hom_precomp_along_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        $C $M $B $G $s $t $alpha ];

// Odd duality on Cartesian mapping categories. This is the strict-transfor
// counterpart of the existing Even action, with the first Hom reversed.
injective symbol OddDual_cart_func_func (A B : Cat)
  : τ (Functor (OddDual_cat (Functor_cart_cat A B))
      (Functor_cart_cat (OddDual_cat A) (OddDual_cat B)));
rule @fapp0 _ _ (OddDual_cart_func_func $A $B) $F ↪ @OddDual_func $A $B $F;

injective symbol OddDual_transf [A B : Cat] [F G : τ (Functor A B)]
  (U : τ (@StrictTransfor A B F G))
  : τ (@StrictTransfor (OddDual_cat A) (OddDual_cat B)
      (@OddDual_func A B G) (@OddDual_func A B F));
rule @fapp1_fapp0 _ _ (OddDual_cart_func_func $A $B) $G $F $U
  ↪ @OddDual_transf $A $B $F $G $U;
rule @OddDual_transf $A $B $F $F (@id _ $F)
  ↪ @id (Functor_cart_cat (OddDual_cat $A) (OddDual_cat $B)) (@OddDual_func $A $B $F);
// lhs-audit: keep 1 -- actual Cartesian image category after reversing composition.
rule @comp_fapp0 (Functor_cart_cat (OddDual_cat $A) (OddDual_cat $B)) _ _ _
      (@OddDual_transf $A $B $F $G $U) (@OddDual_transf $A $B $G $H $V)
  ↪ @OddDual_transf $A $B $F $H
      (@comp_fapp0 (Functor_cart_cat $A $B) $F $G $H $V $U);
rule @tapp0_fapp0 _ _ _ _ $x
      (@strict_transfor _ _ _ _ (@OddDual_transf $A $B $F $G $U))
  ↪ @tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $U);
rule @tapp1_func _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@OddDual_transf $A $B $F $G $U))
  ↪ @EvenDual_func (Hom_cat $A $y $x)
      (Hom_cat $B (@fapp0 $A $B $F $y) (@fapp0 $A $B $G $x))
      (@tapp1_func $A $B $F $G $y $x (@strict_transfor $A $B $F $G $U));
rule @tapp1_fapp0 _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@OddDual_transf $A $B $F $G $U)) $p
  ↪ @tapp1_fapp0 $A $B $F $G $y $x (@strict_transfor $A $B $F $G $U) $p;

// Whole inclusion of strict transformations into the opposite profile.
// Its object map is OddDual_func; it supplies no comparison-cell argument.
symbol Functor_cart_oplax_include (A B : Cat)
  : τ (Functor (Functor_cart_cat A B) (Functor_oplax_cat A B))
≔ @OddDual_func (OddDual_cat (Functor_cart_cat A B))
    (Functor_cat (OddDual_cat A) (OddDual_cat B))
    (@comp_cat_fapp0 (OddDual_cat (Functor_cart_cat A B))
      (Functor_cart_cat (OddDual_cat A) (OddDual_cat B))
      (Functor_cat (OddDual_cat A) (OddDual_cat B))
      (Functor_cart_include (OddDual_cat A) (OddDual_cat B))
      (OddDual_cart_func_func A B));

// Fixed evaluation after Cartesian exchange and its actual oplax inclusion.
// The whole functor returns F[a], retaining the B-action. All derived dual
// classifier slots stay inferred; OddDual_cart_func_func retains A and C.
rule @comp_fapp0 Cat_cat _ _ _
    (@comp_fapp0 Cat_cat _ _ _
      (@comp_fapp0 Cat_cat _ _ _
        (@OddDual_func _ _ (@fapp0_func _ _ $a))
        (@OddDual_func _ _ (Functor_cart_include _ _)))
      (@OddDual_func _ _ (OddDual_cart_func_func $A $C)))
    (@sym_func $A $B $C $F)
  ↪ @fapp0 $A (Functor_cart_cat $B $C) $F $a;

// The strict Cartesian exchange is the restriction of opposite-profile
// evaluation along the actual inclusion, as whole functors. No arbitrary
// lax transformation is admitted to a Cartesian mapping category.
unif_rule
  @comp_fapp0 Cat_cat _ _ _
    (@comp_fapp0 Cat_cat _ _ _
      (@OddDual_func _ _ (Functor_cart_include (OddDual_cat $A) (OddDual_cat $C)))
      (@OddDual_func _ _ (OddDual_cart_func_func $A $C)))
    (@sym_func $A $B $C $F)
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@OddDual_func _ _
      (@hom_precomp_along_func _ _ (@id Cat_cat Cat_cat) _ _ _
        (@OddDual_func $A1 _ $D)))
    (@diagram_evaluation_func $B1 $C1)
  ↪ [ $A1 ≡ $A; $B1 ≡ $B; $C1 ≡ $C;
      $D ≡ @comp_cat_fapp0 $A (Functor_cart_cat $B $C)
        (Functor_cat $B $C) (Functor_cart_include $B $C) $F ];

/* Native comparison for the opposite-profile evaluation owner.
   The candidate body uses eta's existing extracted cell and canonical
   precomposition. It supplies no comparison or strictness input. */

// Even duality on Cartesian mapping categories, needed by this strict Hom
// action. This does not give a same-profile action on arbitrary lax transfors.
injective symbol EvenDual_cart_func_func (A B : Cat)
  : τ (Functor (EvenDual_cat (Functor_cart_cat A B))
      (Functor_cart_cat (EvenDual_cat A) (EvenDual_cat B)));
rule fapp0 (EvenDual_cart_func_func $A $B) $F ↪ @EvenDual_func $A $B $F;
injective symbol EvenDual_transf [A B : Cat] [F G : τ (Functor A B)]
  (U : τ (@StrictTransfor A B F G))
  : τ (@StrictTransfor (EvenDual_cat A) (EvenDual_cat B)
      (@EvenDual_func A B F) (@EvenDual_func A B G));
rule @fapp1_fapp0 _ _ (EvenDual_cart_func_func $A $B) $F $G $U
  ↪ @EvenDual_transf $A $B $F $G $U;
// Projected identity/composition joins of that same whole mapping functor.
rule @EvenDual_transf $A $B $F $F (@id _ $F)
  ↪ @id (Functor_cart_cat (EvenDual_cat $A) (EvenDual_cat $B)) (@EvenDual_func $A $B $F);
// lhs-audit: keep 1 -- measured SR guard for the Cartesian image category.
rule @comp_fapp0 (Functor_cart_cat (EvenDual_cat $A) (EvenDual_cat $B)) _ _ _
      (@EvenDual_transf $A $B $G $H $V) (@EvenDual_transf $A $B $F $G $U)
  ↪ @EvenDual_transf $A $B $F $H
      (@comp_fapp0 (Functor_cart_cat $A $B) $F $G $H $V $U);
rule @tapp0_fapp0 _ _ _ _ $x
      (@strict_transfor _ _ _ _ (@EvenDual_transf $A $B $F $G $U))
  ↪ @tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $U);
rule @tapp1_func _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@EvenDual_transf $A $B $F $G $U))
  ↪ @OddDual_func (Hom_cat $A $x $y)
      (Hom_cat $B (@fapp0 $A $B $F $x) (@fapp0 $A $B $G $y))
      (@tapp1_func $A $B $F $G $x $y (@strict_transfor $A $B $F $G $U));
rule @tapp1_fapp0 _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@EvenDual_transf $A $B $F $G $U)) $p
  ↪ @tapp1_fapp0 $A $B $F $G $x $y (@strict_transfor $A $B $F $G $U) $p;

// Readable source of eta's existing naturality cell at u.
protected symbol diagram_evaluation_square_src [I C : Cat]
  [F G : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (Hom C (@fapp0 I C F i) (@fapp0 I C G j))
≔ @comp_fapp0 C (@fapp0 I C F i) (@fapp0 I C G i) (@fapp0 I C G j)
    (@fapp1_fapp0 I C G i j u) (@tapp0_fapp0 I C F G i eta);

// Actual internal-action extraction; this is not a separately declared cell.
protected symbol diagram_evaluation_square_cell [I C : Cat]
  [F G : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (Hom (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
      (@diagram_evaluation_square_src I C F G eta i j u)
      (@tapp1_fapp0 I C F G i j eta u))
≔ @tapp1_post_laxity_cell I C F G eta i i j u (@id I i);

// For theta:G⇒H, the two functors send theta to theta[j] composed with
// the source/target of eta's square. They are whole in theta.
protected symbol diagram_evaluation_naturality_src [I C : Cat]
  [F G H : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (Functor (@Transf_cat I C G H)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C H j)))
≔ @comp_cat_fapp0 _ _ _
    (@hom_precomp_along_func C C (@id_func C) (@fapp0 I C H j)
      (@fapp0 I C F i) (@fapp0 I C G j)
      (@diagram_evaluation_square_src I C F G eta i j u))
    (@tapp0_func I C G H j);
protected symbol diagram_evaluation_naturality_tgt [I C : Cat]
  [F G H : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (Functor (@Transf_cat I C G H)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C H j)))
≔ @comp_cat_fapp0 _ _ _
    (@hom_precomp_along_func C C (@id_func C) (@fapp0 I C H j)
      (@fapp0 I C F i) (@fapp0 I C G j) (@tapp1_fapp0 I C F G i j eta u))
    (@tapp0_func I C G H j);

// Canonical Hom action is strict in theta, even though eta is arbitrary lax.
// Prewhisker that action by the existing component functor theta↦theta[j].
protected symbol diagram_evaluation_naturality_cart [I C : Cat]
  [F G H : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@StrictTransfor (@Transf_cat I C G H)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C H j))
      (@diagram_evaluation_naturality_src I C F G H eta i j u)
      (@diagram_evaluation_naturality_tgt I C F G H eta i j u))
≔ @fapp1_fapp0 _ _
    (@comp_cat_con_cart_func (@Transf_cat I C G H)
      (Hom_cat C (@fapp0 I C G j) (@fapp0 I C H j))
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C H j)) (@tapp0_func I C G H j))
    (@hom_precomp_along_func C C (@id_func C) (@fapp0 I C H j)
      (@fapp0 I C F i) (@fapp0 I C G j)
      (@diagram_evaluation_square_src I C F G eta i j u))
    (@hom_precomp_along_func C C (@id_func C) (@fapp0 I C H j)
      (@fapp0 I C F i) (@fapp0 I C G j) (@tapp1_fapp0 I C F G i j eta u))
    (@hom_precomp_along_tele_fapp1_fapp0 C C (@id_func C) (@fapp0 I C H j)
      (@fapp0 I C F i) (@fapp0 I C G j)
      (@diagram_evaluation_square_src I C F G eta i j u)
      (@tapp1_fapp0 I C F G i j eta u)
      (@diagram_evaluation_square_cell I C F G eta i j u));

// The same retained whole cell in evaluation's Even-dual Hom presentation.
symbol diagram_evaluation_naturality_transf [I C : Cat]
  [F G H : τ (Functor I C)] (eta : τ (@Transf I C F G))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf (EvenDual_cat (@Transf_cat I C G H))
      (EvenDual_cat (Hom_cat C (@fapp0 I C F i) (@fapp0 I C H j)))
      (@EvenDual_func _ _ (@diagram_evaluation_naturality_src I C F G H eta i j u))
      (@EvenDual_func _ _ (@diagram_evaluation_naturality_tgt I C F G H eta i j u)))
≔ @strict_transfor _ _ _ _
    (@EvenDual_transf _ _ _ _ (@diagram_evaluation_naturality_cart I C F G H eta i j u));

// Whole source reading: theta[j] composed with G[u] composed with eta[i].
// Compare the actual two endpoint presentations without runtime reassociation.
unif_rule
  @comp_fapp0 Cat_cat _ _ _
    (@hom_postcomp_func _ _ (@OddDual_func _ _ (@fapp0_func $I $C $i)) $z $G $F $eta)
    (@EvenDual_func _ _ (@diagram_evaluation_mixed_func $I $C $i $j $u $G $H))
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@EvenDual_func _ _ (@hom_precomp_along_func _ _ (@id Cat_cat $C0) $z0 $a $b $h))
    (@EvenDual_func _ _ (@tapp0_func $I0 $C1 $G0 $H0 $j0))
  ↪ [ $I0 ≡ $I; $C0 ≡ $C; $C1 ≡ $C; $G0 ≡ $G; $H0 ≡ $H; $j0 ≡ $j;
      $z ≡ @fapp0 $I $C $H $j; $z0 ≡ $z;
      $a ≡ @fapp0 $I $C $F $i; $b ≡ @fapp0 $I $C $G $j;
      $h ≡ @diagram_evaluation_square_src $I $C $F $G $eta $i $j $u ];

// Whole target reading: (theta composed with eta)[u] is theta[j] composed
// with eta[u], by the selected pre/right convention and strict evaluation.
unif_rule
  @comp_fapp0 Cat_cat _ _ _
    (@EvenDual_func _ _ (@diagram_evaluation_mixed_func $I $C $i $j $u $F $H))
    (@hom_postcomp_func _ _ (@id Cat_cat (OddDual_cat (Functor_cat $I $C))) $H $G $F $eta)
  ≡ @comp_fapp0 Cat_cat _ _ _
    (@EvenDual_func _ _ (@hom_precomp_along_func _ _ (@id Cat_cat $C0) $z $a $b $h))
    (@EvenDual_func _ _ (@tapp0_func $I0 $C1 $G0 $H0 $j0))
  ↪ [ $I0 ≡ $I; $C0 ≡ $C; $C1 ≡ $C; $G0 ≡ $G; $H0 ≡ $H; $j0 ≡ $j;
      $z ≡ @fapp0 $I $C $H $j;
      $a ≡ @fapp0 $I $C $F $i; $b ≡ @fapp0 $I $C $G $j;
      $h ≡ @tapp1_fapp0 $I $C $F $G $i $j $eta $u ];

// Constructor beta at the existing whole intrinsic projection owner. The
// internal action must be the canonical one of this very evaluation transfor.
rule @fdapp1_comma_projection_transf _ _ _
      (@tapp1_at_transf _ _ _ _ $H (@diagram_evaluation_transf $I $C $i $j $u))
      (@fdapp1_int_transfd _ _ _
        (@tapp1_at_transf _ _ _ _ $H (@diagram_evaluation_transf $I $C $i $j $u)))
      $G $F $eta
  ↪ @diagram_evaluation_naturality_transf $I $C $F $G $H $eta $i $j $u;

require open emdash.emdash3_2_one_cat_action_paths;
require open emdash.emdash3_2_one_cat_functor_closure;

// Whole evaluation after precomposition: (D∘F)(−)[i] = D(−)[i]∘F.
// This preserves the whole remaining parameter action.
rule @sym_fapp0_func _ $I $C
      (@comp_fapp0 Cat_cat $A $B _ $D $F) $i
  ↪ @comp_cat_fapp0 $A $B $C (@sym_fapp0_func $B $I $C $D $i) $F;

// Constant diagrams evaluate to an actual constant parameter functor.
// Keep the whole functor as owner, with the original diagram and shape point.
rule @sym_fapp0_func $K $I $C (@Const_func _ _ $D) $i
  ↪ @Const_func $K $C (@fapp0 $I $C $D $i);

// The same evaluation fold after its Hom projection has already occurred.
// A measured preprojected consumer otherwise retains a different whole head.
rule @sym_fapp0_fapp1_func _ $I $C
      (@comp_fapp0 Cat_cat $A $B _ $D $F) $i $x $y
  ↪ @fapp1_func $A $C
      (@comp_cat_fapp0 $A $B $C (@sym_fapp0_func $B $I $C $D $i) $F) $x $y;

// Companion after projection to Hom: reuse the original constant-functor action.
rule @sym_fapp0_fapp1_func $K $I $C (@Const_func _ _ $D) $i $x $y
  ↪ @fapp1_func $K $C (@Const_func $K $C (@fapp0 $I $C $D $i)) $x $y;

// Proof-time whole evaluation comparison; retain both runtime owners.
unif_rule
  @sym_fapp0_func _ $I $C $F $i
  ≡ @comp_fapp0 Cat_cat _ _ _
      (@sym_fapp0_func _ $I1 $C1 (@id Cat_cat _) $i1) $F1
  ↪ [ $I1 ≡ $I; $C1 ≡ $C; $F1 ≡ $F; $i1 ≡ $i ];

// Whole transformation evaluation, after the Cat-specialized postwhiskering
// projection has exposed product composition. The identity second component
// is the genuine postwhiskering discriminator.
unif_rule
  @sym_transf_tapp0_transf _ $I $C $F $G $h $i
  ≡ @comp_prod_fapp1_fapp0 Cat_cat _ _ _
      (@Struct_sigma _ _ $F1
        (@sym_fapp0_func _ $I1 $C1 (@id Cat_cat _) $i1))
      (@Struct_sigma _ _ $G1 _)
      (@Struct_sigma _ _ $h1 (@id _ _))
  ↪ [ $I1 ≡ $I; $C1 ≡ $C; $F1 ≡ $F; $G1 ≡ $G; $h1 ≡ $h; $i1 ≡ $i ];

// Proof-time shape-arrow evaluation through prewhiskering by the same family.
// Compare both factors, their endpoint evaluations, and the original shape arrow.
unif_rule
  @sym_tapp1_fapp0_transf $A $I $C $E $i $j $u
  ≡ @comp_prod_fapp1_fapp0 Cat_cat $A1 $B $C1
      (@Struct_sigma _ _ $F1 $Ei)
      (@Struct_sigma _ _ $F2 $Ej)
      (@Struct_sigma _ _ (@id _ $F3)
        (@sym_tapp1_fapp0_transf $B1 $I1 $C2 $D $i1 $j1 $u1))
  ↪ [ $A1 ≡ $A; $B1 ≡ $B; $I1 ≡ $I; $C1 ≡ $C; $C2 ≡ $C;
      $F2 ≡ $F1; $F3 ≡ $F1; $i1 ≡ $i; $j1 ≡ $j; $u1 ≡ $u;
      $E ≡ (@comp_cat_fapp0 $A $B (Functor_cat $I $C) $D $F1);
      $Ei ≡ (@sym_fapp0_func $B $I $C $D $i);
      $Ej ≡ (@sym_fapp0_func $B $I $C $D $j) ];

// Ordinary-target evaluation is a guarded whole construction. A diagram
// transformation into a OneCat has commuting naturality squares, so shape
// evaluation has the ordinary transformation profile. The general evaluator
// above retains its oplax profile; no equality of those classifiers is used.
require open emdash.emdash3_2_discrete_functor_paths;

injective symbol one_cat_diagram_evaluation_func [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (Functor I (Functor_cat (Functor_cat I C) C));

rule @fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i
  ↪ @diagram_evaluation_at_func $I $C $i;

symbol one_cat_diagram_evaluation_hom_func [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (i j : τ (Obj I))
  : τ (Functor (Hom_cat I i j)
    (@Transf_cat (Functor_cat I C) C
      (@diagram_evaluation_at_func I C i) (@diagram_evaluation_at_func I C j)))
≔ @fapp1_func I (Functor_cat (Functor_cat I C) C)
    (@one_cat_diagram_evaluation_func I C C1) i j;

symbol one_cat_diagram_evaluation_transf [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf (Functor_cat I C) C
    (@diagram_evaluation_at_func I C i) (@diagram_evaluation_at_func I C j))
≔ @fapp1_fapp0 I (Functor_cat (Functor_cat I C) C)
    (@one_cat_diagram_evaluation_func I C C1) i j u;

// The projected action remains at fapp1_func/fapp1_fapp0, so generic
// functor identity and composition own every observation order.
rule @tapp0_fapp0 _ _ _ _ $F (@fapp1_fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j $u)
  ↪ @fapp1_fapp0 $I $C $F $i $j $u;

// The default ordinary pre/right action: alpha maps to G[u] o alpha[i].
// This is a composition of the existing evaluation and fixed Hom action.
symbol one_cat_diagram_evaluation_mixed_func [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [i j : τ (Obj I)] (u : τ (Hom I i j)) (F G : τ (Functor I C))
  : τ (Functor (@Transf_cat I C F G)
    (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j)))
≔ @comp_cat_fapp0 (@Transf_cat I C F G)
    (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G i))
    (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
    (@hom_postcomp_func C C (@id_func C)
      (@fapp0 I C F i) (@fapp0 I C G i) (@fapp0 I C G j) (@fapp1_fapp0 I C G i j u))
    (@tapp0_func I C F G i);

rule @tapp1_func _ _ _ _ $F $G (@fapp1_fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j $u)
  ↪ @one_cat_diagram_evaluation_mixed_func $I $C $C1 $i $j $u $F $G;
rule @tapp1_fapp0 _ _ _ _ $F $G (@fapp1_fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j $u) $alpha
  ↪ fapp0 (@one_cat_diagram_evaluation_mixed_func $I $C $C1 $i $j $u $F $G) $alpha;

// Whole observation of shape-Hom action, retaining all further Hom levels.
rule @comp_fapp0 Cat_cat _ _ _ (@tapp0_func _ _ _ _ $F)
    (@fapp1_func _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j)
  ↪ @fapp1_func $I $C $F $i $j;

// Agreement with the general mixed evaluator uses the actual existing
// naturality cell and OneCat(C), rather than declaring a reverse cell.
symbol one_cat_diagram_evaluation_mixed_path [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  (F G : τ (Functor I C)) (alpha : τ (@Transf I C F G))
  : τ (@= (Hom C (@fapp0 I C F i) (@fapp0 I C G j))
    (fapp0 (@one_cat_diagram_evaluation_mixed_func I C C1 i j u F G) alpha)
    (fapp0 (@diagram_evaluation_mixed_func I C i j u F G) alpha))
≔ @one_cat_component_naturality_path I C C1 F G alpha i j u;

// Both mixed actions are whole functors into the same genuinely discrete
// Hom category. Reuse its existing comparison theorem; no profile equality
// or pointwise assembly of the evaluation constructor is asserted.
symbol one_cat_diagram_evaluation_mixed_func_path [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [i j : τ (Obj I)] (u : τ (Hom I i j)) (F G : τ (Functor I C))
  : τ (@= (Functor (@Transf_cat I C F G)
      (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j)))
    (@one_cat_diagram_evaluation_mixed_func I C C1 i j u F G)
    (@diagram_evaluation_mixed_func I C i j u F G))
≔ @discrete_functor_path (@Transf_cat I C F G)
    (Hom_cat C (@fapp0 I C F i) (@fapp0 I C G j))
    (C1 (@fapp0 I C F i) (@fapp0 I C G j))
    (@one_cat_diagram_evaluation_mixed_func I C C1 i j u F G)
    (@diagram_evaluation_mixed_func I C i j u F G)
    (λ alpha : τ (@Transf I C F G),
      @one_cat_diagram_evaluation_mixed_path I C C1 i j u F G alpha);
// Structural discrete-category closure, parallel to discrete_total_op.
// Even duality preserves object truncation and groupoidality. This is a
// declared classifier closure, not a derivation of Core-inclusion inverse
// data from the currently available dual-functor projection rules.
symbol discrete_even_dual [C : Cat] (C0 : τ (IsDiscreteCat C))
  : τ (IsDiscreteCat (EvenDual_cat C));

// Hom(Odd(C),x,y)=Even(Hom(C,y,x)); the original OneCat hypothesis
// therefore supplies the profile needed by encoded oplax-map observations.
symbol one_cat_odd_dual [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (IsNCat (cat_succ cat_zero) (OddDual_cat C))
≔ λ x : τ (Obj C), λ y : τ (Obj C),
    @discrete_even_dual (Hom_cat C y x) (C1 y x);

// Structural ordinary-category closure for the corrected oplax diagram
// profile. As for one_cat_functor_category, the actual target OneCat witness
// is required; this does not identify ordinary and oplax mapping categories.
constant symbol one_cat_oplax_functor_category [I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  : τ (IsNCat (cat_succ cat_zero) (Functor_oplax_cat I C));

// The old ordinary-target observation now uses actual postcomposition action.
symbol one_cat_diagram_family_evaluation_comp_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (i : τ (Obj I))
  (F G H : τ (Functor B (Functor_cat I C)))
  (g : τ (@Transf B (Functor_cat I C) G H))
  (f : τ (@Transf B (Functor_cat I C) F G))
  : τ (@= (@Transf B C (@diagram_family_at_func B I C F i) (@diagram_family_at_func B I C H i))
      (@fapp1_fapp0 _ _ (@diagram_family_evaluation_func B I C i) F H
        (@comp_fapp0 (Functor_cat B (Functor_cat I C)) F G H g f))
      (@comp_fapp0 (Functor_cat B C)
        (@diagram_family_at_func B I C F i) (@diagram_family_at_func B I C G i) (@diagram_family_at_func B I C H i)
        (@fapp1_fapp0 _ _ (@diagram_family_evaluation_func B I C i) G H g)
        (@fapp1_fapp0 _ _ (@diagram_family_evaluation_func B I C i) F G f)))
≔ @one_cat_composition_path (Functor_cat B (Functor_cat I C)) (Functor_cat B C)
    (@one_cat_functor_category B C C1)
    (@diagram_family_evaluation_func B I C i) F G H g f;

// Reindex the actual opposite-profile transformation. The original ordinary
// guard is retained for compatibility; this comparison itself is general.
symbol one_cat_diagram_family_transf_whisker_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@= (@Transf_oplax B C (@diagram_family_at_func B I C D i) (@diagram_family_at_func B I C D j))
      (@diagram_family_transf B I C D i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func B (Functor_cat I C) C D)
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C i))
        (@OddDual_func _ _ (@diagram_evaluation_at_func I C j))
        (@diagram_evaluation_transf I C i j u)))
≔ eq_refl (@diagram_family_transf B I C D i j u);

// The same prewhiskering comparison after restricting the parameter family.
symbol one_cat_diagram_family_transf_reindex_path [A B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_cat I C))) (F : τ (Functor A B))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@= (@Transf_oplax A C
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D i) F)
      (@comp_cat_fapp0 A B C (@diagram_family_at_func B I C D j) F))
      (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u)
      (@fapp1_fapp0 _ _ (@oplax_precomp_func A B C F)
        (@OddDual_func _ _ (@diagram_family_at_func B I C D i))
        (@OddDual_func _ _ (@diagram_family_at_func B I C D j))
        (@diagram_family_transf B I C D i j u)))
≔ eq_refl (@diagram_family_transf A I C (@comp_cat_fapp0 A B (Functor_cat I C) D F) i j u);

// Evaluation of oplax diagrams has ordinary lax shape action. It is the
// alternating dual of the already qualified opposite-profile evaluator.
symbol diagram_oplax_evaluation_func [I C : Cat]
  : τ (Functor I (Functor_cat (Functor_oplax_cat I C) C))
≔ @OddDual_func _ _ (@diagram_evaluation_func (OddDual_cat I) (OddDual_cat C));
symbol diagram_oplax_evaluation_at_func [I C : Cat] (i : τ (Obj I))
  : τ (Functor (Functor_oplax_cat I C) C)
≔ @fapp0 _ _ (@diagram_oplax_evaluation_func I C) i;
// Whole oplax-diagram evaluation of a literal precomposition. Match the
// actual evaluator head, rather than an arbitrary postcomposing functor.
// J,D are the evaluator's encoded parameters; no reducible Odd-pattern is
// used to recover an unencoded base. Both factors and the point are retained.
unif_rule
  @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat)
    $C $A $B (@comp_fapp0 Cat_cat $A $M $B $G $F)
    (@OddDual_func _ _ (@fapp0_func $J $D $i))
  ≡ $view
  ↪ [ $B ≡ OddDual_cat (Functor_cat $J $D); $C ≡ OddDual_cat $D;
      @comp_fapp0 Cat_cat $A $B $C
        (@diagram_oplax_evaluation_at_func (OddDual_cat $J) (OddDual_cat $D) $i)
        (@comp_fapp0 Cat_cat $A $M $B $G $F) ≡ $view ];

// The same evaluation comparison after represented postcomposition has split.
// Retain the actual evaluator, all three maps and their complete composite.
// This is proof-time only; the represented runtime cuts remain unchanged.
unif_rule
  @comp_fapp0 Cat_cat $A $B $C
    (@OddDual_func _ _ (@fapp0_func $J $D $i))
    (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $A $N $B $q
      (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $A $M $N $p $g))
  ≡ $view
  ↪ [ $B ≡ OddDual_cat (Functor_cat $J $D); $C ≡ OddDual_cat $D;
      @comp_fapp0 Cat_cat $A $B $C
        (@OddDual_func _ _ (@fapp0_func $J $D $i))
        (@comp_fapp0 Cat_cat $A $M $B
          (@comp_fapp0 Cat_cat $M $N $B $q $p) $g) ≡ $view ];

symbol diagram_oplax_evaluation_transf [I C : Cat]
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf (Functor_oplax_cat I C) C
      (@diagram_oplax_evaluation_at_func I C i) (@diagram_oplax_evaluation_at_func I C j))
≔ @fapp1_fapp0 _ _ (@diagram_oplax_evaluation_func I C) i j u;

// Whole parameter action is ordinary precomposition of the whole evaluator.
symbol diagram_oplax_family_shape_func [K I C : Cat]
  (D : τ (Functor K (Functor_oplax_cat I C)))
  : τ (Functor I (Functor_cat K C))
≔ @comp_cat_fapp0 I (Functor_cat (Functor_oplax_cat I C) C) (Functor_cat K C)
    (@comp_cat_con_func K (Functor_oplax_cat I C) C D)
    (@diagram_oplax_evaluation_func I C);
symbol diagram_oplax_family_evaluation_func [K I C : Cat] (i : τ (Obj I))
  : τ (Functor (Functor_cat K (Functor_oplax_cat I C)) (Functor_cat K C))
≔ @comp_cat_cov_func K (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i);
symbol diagram_oplax_family_at_func [K I C : Cat]
  (D : τ (Functor K (Functor_oplax_cat I C))) (i : τ (Obj I))
  : τ (Functor K C)
≔ @fapp0 I (Functor_cat K C) (@diagram_oplax_family_shape_func K I C D) i;
symbol diagram_oplax_family_transf [K I C : Cat]
  (D : τ (Functor K (Functor_oplax_cat I C)))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@Transf K C
      (@comp_cat_fapp0 K (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) D)
      (@comp_cat_fapp0 K (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C j) D))
≔ @fapp1_fapp0 I (Functor_cat K C) (@diagram_oplax_family_shape_func K I C D) i j u;

// Double exchange at its actual composition owner. This is the corrected
// two-profile counterpart of the original whole symmetry involution.
// No Cartesian exchange is applied to a general lax mapping category.
rule @comp_fapp0 Cat_cat _ _ _
      (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $C $B _
        (@comp_fapp0 Cat_cat _ _ _
          (@OddDual_func _ _
            (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
              (OddDual_cat $C) _ _ (@OddDual_func $A _ $D)))
          (@diagram_evaluation_func $B $C)))
      (@OddDual_func _ _ (@diagram_evaluation_func (OddDual_cat $A) (OddDual_cat $C)))
  ↪ $D;

// Fixed-component projection of the same double exchange, after Cat
// composition has selected its existing left-associated normal form.
rule @comp_fapp0 Cat_cat _ _ _
      (@comp_fapp0 Cat_cat _ _ _
        (@OddDual_func _ _ (@fapp0_func _ _ $a))
        (@OddDual_func _ _
          (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
            _ _ _ (@OddDual_func $A _ $D))))
      (@diagram_evaluation_func $B $C)
  ↪ @fapp0 $A (Functor_cat $B $C) $D $a;

// Object-first companion: the established represented postcomposition cut
// expands a composed functor into consecutive cuts. Preserve those owners
// while observing this literal exchange constructor at the fixed component.
rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $P _ $C
      (@OddDual_func _ _ (@fapp0_func _ _ $a))
      (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $P _ _
        (@OddDual_func _ _
          (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
            _ _ _ (@OddDual_func $A _ $D)))
        (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $P $B _
          (@diagram_evaluation_func $B $C) $X))
  ↪ @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $P $B $C
      (@fapp0 $A (Functor_cat $B $C) $D $a) $X;

// The existing fixed-component double-exchange projection when object
// evaluation has exposed one represented cut, but its family is still a
// whole composition. Retain the actual family D and component a.
rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B _ $C
    (@OddDual_func _ _ (@fapp0_func _ _ $a))
    (@comp_fapp0 Cat_cat _ _ _
      (@OddDual_func _ _
        (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
          _ _ _ (@OddDual_func $A _ $D)))
      (@diagram_evaluation_func $B $C))
  ↪ @fapp0 $A (Functor_cat $B $C) $D $a;

// The odd-dual image of the existing whole double-exchange projection.
// This is the opposite starting profile: D already takes values in oplax
// diagrams. Retain the entire D, including all of its higher action.
rule @comp_fapp0 Cat_cat _ _ _
    (@OddDual_func _ _
      (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat)
        (OddDual_cat $C) (OddDual_cat $B) _
        (@comp_fapp0 Cat_cat _ _ _
          (@OddDual_func _ _
            (@hom_precomp_along_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $C $A _ $D))
          (@diagram_evaluation_func (OddDual_cat $B) (OddDual_cat $C)))))
    (@diagram_evaluation_func $A $C)
  ↪ $D;

// Fixed-index observation of a whole map between native oplax families.
// This is the original accessor outline, using the actual evaluation functor.
symbol diagram_oplax_family_map_at [B I C : Cat]
  [F G : τ (Functor B (Functor_oplax_cat I C))]
  (eta : τ (@Transf B (Functor_oplax_cat I C) F G)) (i : τ (Obj I))
  : τ (@Transf B C
      (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F)
      (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) G))
≔ @fapp1_fapp0 _ _ (@diagram_oplax_family_evaluation_func B I C i) F G eta;

symbol one_cat_oplax_family_evaluation_comp_path [B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) (i : τ (Obj I))
  (F G H : τ (Functor B (Functor_oplax_cat I C)))
  (g : τ (@Transf B (Functor_oplax_cat I C) G H))
  (f : τ (@Transf B (Functor_oplax_cat I C) F G))
  : τ (@= (@Transf B C (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F)
      (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) H))
      (@diagram_oplax_family_map_at B I C F H
        (@comp_fapp0 (Functor_cat B (Functor_oplax_cat I C)) F G H g f) i)
      (@comp_fapp0 (Functor_cat B C)
        (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F)
        (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) G)
        (@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) H)
        (@diagram_oplax_family_map_at B I C G H g i)
        (@diagram_oplax_family_map_at B I C F G f i)))
≔ @one_cat_composition_path (Functor_cat B (Functor_oplax_cat I C))
    (Functor_cat B C) (@one_cat_functor_category B C C1)
    (@diagram_oplax_family_evaluation_func B I C i) F G H g f;

// Shape action after restriction of a native oplax family. The result is an
// ordinary lax transformation, so its actual reindexing uses ordinary
// precomposition; the existing OneCat guard is retained at this library view.
symbol one_cat_oplax_family_transf_reindex_path [A B I C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (D : τ (Functor B (Functor_oplax_cat I C))) (F : τ (Functor A B))
  [i j : τ (Obj I)] (u : τ (Hom I i j))
  : τ (@= (@Transf A C
      (@comp_cat_fapp0 A B C (@diagram_oplax_family_at_func B I C D i) F)
      (@comp_cat_fapp0 A B C (@diagram_oplax_family_at_func B I C D j) F))
      (@diagram_oplax_family_transf A I C
        (@comp_cat_fapp0 A B (Functor_oplax_cat I C) D F) i j u)
      (@fapp1_fapp0 _ _ (@comp_cat_con_func A B C F)
        (@diagram_oplax_family_at_func B I C D i)
        (@diagram_oplax_family_at_func B I C D j)
        (@diagram_oplax_family_transf B I C D i j u)))
≔ eq_refl (@diagram_oplax_family_transf A I C
    (@comp_cat_fapp0 A B (Functor_oplax_cat I C) D F) i j u);
