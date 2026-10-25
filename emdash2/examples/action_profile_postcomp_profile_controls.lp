/* Default strict postcomposition, retaining the former guarded and identity cases.
   The three former lax-functor negatives are positive under the selected default. */
require open emdash.emdash3_2_gray_profiles;

assert [A B : Cat] (F : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Functor (Hom_cat B W (@fapp0 A B F X)) (Hom_cat B W (@fapp0 A B F Z))) (@comp_fapp0 Cat_cat (Hom_cat B W (@fapp0 A B F X)) (Hom_cat B W (@fapp0 A B F Y)) (Hom_cat B W (@fapp0 A B F Z)) (@hom_postcomp_func B A F W Y Z q) (@hom_postcomp_func B A F W X Y p)) : τ (@= (Functor (Hom_cat B W (@fapp0 A B F X)) (Hom_cat B W (@fapp0 A B F Z))) (@comp_fapp0 Cat_cat (Hom_cat B W (@fapp0 A B F X)) (Hom_cat B W (@fapp0 A B F Y)) (Hom_cat B W (@fapp0 A B F Z)) (@hom_postcomp_func B A F W Y Z q) (@hom_postcomp_func B A F W X Y p)) (@hom_postcomp_func B A F W X Z (@comp_fapp0 A X Y Z q p)));

assert [A B : Cat] (F : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B F X))) ⊢ @eq_refl (Hom B W (@fapp0 A B F Z)) (@hom_postcomp_fapp0 B A F W Y Z q (@hom_postcomp_fapp0 B A F W X Y p g)) : τ (@= (Hom B W (@fapp0 A B F Z)) (@hom_postcomp_fapp0 B A F W Y Z q (@hom_postcomp_fapp0 B A F W X Y p g)) (@hom_postcomp_fapp0 B A F W X Z (@comp_fapp0 A X Y Z q p) g));

assert [A B : Cat] (F : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B F X))) ⊢ @eq_refl (Hom B W (@fapp0 A B F Z)) (@comp_fapp0 B W (@fapp0 A B F Y) (@fapp0 A B F Z) (@fapp1_fapp0 A B F Y Z q) (@hom_postcomp_fapp0 B A F W X Y p g)) : τ (@= (Hom B W (@fapp0 A B F Z)) (@comp_fapp0 B W (@fapp0 A B F Y) (@fapp0 A B F Z) (@fapp1_fapp0 A B F Y Z q) (@hom_postcomp_fapp0 B A F W X Y p g)) (@hom_postcomp_fapp0 B A F W X Z (@comp_fapp0 A X Y Z q p) g));

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ (@comp_fapp0 Cat_cat (Hom_cat B W (@fapp0 A B S X)) (Hom_cat B W (@fapp0 A B S Y)) (Hom_cat B W (@fapp0 A B S Z)) (@hom_postcomp_func B A S W Y Z q) (@hom_postcomp_func B A S W X Y p)) ≡ (@hom_postcomp_func B A S W X Z (@comp_fapp0 A X Y Z q p));

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) ⊢ @eq_refl (Functor (Hom_cat B W (@fapp0 A B S X)) (Hom_cat B W (@fapp0 A B S Z))) (@comp_fapp0 Cat_cat (Hom_cat B W (@fapp0 A B S X)) (Hom_cat B W (@fapp0 A B S Y)) (Hom_cat B W (@fapp0 A B S Z)) (@hom_postcomp_func B A S W Y Z q) (@hom_postcomp_func B A S W X Y p)) : τ (@= (Functor (Hom_cat B W (@fapp0 A B S X)) (Hom_cat B W (@fapp0 A B S Z))) (@comp_fapp0 Cat_cat (Hom_cat B W (@fapp0 A B S X)) (Hom_cat B W (@fapp0 A B S Y)) (Hom_cat B W (@fapp0 A B S Z)) (@hom_postcomp_func B A S W Y Z q) (@hom_postcomp_func B A S W X Y p)) (@hom_postcomp_func B A S W X Z (@comp_fapp0 A X Y Z q p)));

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B S X))) ⊢ (@hom_postcomp_fapp0 B A S W Y Z q (@hom_postcomp_fapp0 B A S W X Y p g)) ≡ (@hom_postcomp_fapp0 B A S W X Z (@comp_fapp0 A X Y Z q p) g);

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B S X))) ⊢ @eq_refl (Hom B W (@fapp0 A B S Z)) (@hom_postcomp_fapp0 B A S W Y Z q (@hom_postcomp_fapp0 B A S W X Y p g)) : τ (@= (Hom B W (@fapp0 A B S Z)) (@hom_postcomp_fapp0 B A S W Y Z q (@hom_postcomp_fapp0 B A S W X Y p g)) (@hom_postcomp_fapp0 B A S W X Z (@comp_fapp0 A X Y Z q p) g));

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B S X))) ⊢ (@comp_fapp0 B W (@fapp0 A B S Y) (@fapp0 A B S Z) (@fapp1_fapp0 A B S Y Z q) (@hom_postcomp_fapp0 B A S W X Y p g)) ≡ (@hom_postcomp_fapp0 B A S W X Z (@comp_fapp0 A X Y Z q p) g);

assert [A B : Cat] (S : τ (Functor A B)) (W : τ (Obj B)) [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z)) (g : τ (Hom B W (@fapp0 A B S X))) ⊢ @eq_refl (Hom B W (@fapp0 A B S Z)) (@comp_fapp0 B W (@fapp0 A B S Y) (@fapp0 A B S Z) (@fapp1_fapp0 A B S Y Z q) (@hom_postcomp_fapp0 B A S W X Y p g)) : τ (@= (Hom B W (@fapp0 A B S Z)) (@comp_fapp0 B W (@fapp0 A B S Y) (@fapp0 A B S Z) (@fapp1_fapp0 A B S Y Z q) (@hom_postcomp_fapp0 B A S W X Y p g)) (@hom_postcomp_fapp0 B A S W X Z (@comp_fapp0 A X Y Z q p) g));

assert [B : Cat] (W X Y Z : τ (Obj B)) (p : τ (Hom B X Y)) (q : τ (Hom B Y Z)) (g : τ (Hom B W X)) ⊢ (@comp_fapp0 Cat_cat (Hom_cat B W X) (Hom_cat B W Y) (Hom_cat B W Z) (@hom_postcomp_func B B (@id_func B) W Y Z q) (@hom_postcomp_func B B (@id_func B) W X Y p)) ≡ (@hom_postcomp_func B B (@id_func B) W X Z (@comp_fapp0 B X Y Z q p));

assert [B : Cat] (W X Y Z : τ (Obj B)) (p : τ (Hom B X Y)) (q : τ (Hom B Y Z)) (g : τ (Hom B W X)) ⊢ (@hom_postcomp_fapp0 B B (@id_func B) W Y Z q (@hom_postcomp_fapp0 B B (@id_func B) W X Y p g)) ≡ (@hom_postcomp_fapp0 B B (@id_func B) W X Z (@comp_fapp0 B X Y Z q p) g);

assert [B : Cat] (W X Y Z : τ (Obj B)) (p : τ (Hom B X Y)) (q : τ (Hom B Y Z)) (g : τ (Hom B W X)) ⊢ (@fapp0 (Hom_cat B W X) (Hom_cat B W Z) (@comp_fapp0 Cat_cat (Hom_cat B W X) (Hom_cat B W Y) (Hom_cat B W Z) (@hom_postcomp_func B B (@id_func B) W Y Z q) (@hom_postcomp_func B B (@id_func B) W X Y p)) g) ≡ (@hom_postcomp_fapp0 B B (@id_func B) W X Z (@comp_fapp0 B X Y Z q p) g);

assert [B : Cat] (W X Y Z : τ (Obj B)) (p : τ (Hom B X Y)) (q : τ (Hom B Y Z)) (g : τ (Hom B W X)) ⊢ (@fapp0 (Hom_cat B W X) (Hom_cat B W Z) (@hom_postcomp_func B B (@id_func B) W X Z (@comp_fapp0 B X Y Z q p)) g) ≡ (@hom_postcomp_fapp0 B B (@id_func B) W X Z (@comp_fapp0 B X Y Z q p) g);

// The strict law retains the actual base composite and incoming arrow.
assertnot [A B : Cat] (F : τ (Functor A B)) (W : τ (Obj B))
  [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z))
  (other : τ (Hom A X Z)) (g : τ (Hom B W (@fapp0 A B F X))) ⊢
  @hom_postcomp_fapp0 B A F W X Z (@comp_fapp0 A X Y Z q p) g
  ≡ @hom_postcomp_fapp0 B A F W X Z other g;
assertnot [A B : Cat] (F : τ (Functor A B)) (W : τ (Obj B))
  [X Y Z : τ (Obj A)] (p : τ (Hom A X Y)) (q : τ (Hom A Y Z))
  (g other : τ (Hom B W (@fapp0 A B F X))) ⊢
  @hom_postcomp_fapp0 B A F W X Z (@comp_fapp0 A X Y Z q p) g
  ≡ @hom_postcomp_fapp0 B A F W X Z (@comp_fapp0 A X Y Z q p) other;
