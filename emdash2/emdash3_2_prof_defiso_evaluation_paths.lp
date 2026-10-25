/* Prof-indexed raw evaluation retains the original comparison metadata.
   The actual profunctor coefficient is Cat_cart. The stable owner and
   the original selected inverse data are unchanged; these remain proof-time views. */
require open emdash.emdash3_2_adjunction_mates;

unif_rule @defiso_at_to $Base Cat_cart $P $Q $I $z
  ≡ @tapp0_fapp0 $Base Cat_cart $P $Q $z
      (@defiso_to (Prof_cat $A $B) $P $Q $I)
  ↪ [ $Base ≡ Product_cat (Op_cat $A) $B ];

symbol prof_defiso_at_to_path [A B : Cat] [P Q : τ (Prof A B)]
 (I : τ (@DefIso (Prof_cat A B) P Q)) (z : τ (Obj (Product_cat (Op_cat A) B)))
 : τ (@= (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z))
    (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)))
≔ @eq_refl _ (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z);

unif_rule @defiso_at_from $Base Cat_cart $P $Q $I $z
  ≡ @tapp0_fapp0 $Base Cat_cart $Q $P $z
      (@defiso_from (Prof_cat $A $B) $P $Q $I)
  ↪ [ $Base ≡ Product_cat (Op_cat $A) $B ];

symbol prof_defiso_at_from_path [A B : Cat] [P Q : τ (Prof A B)]
 (I : τ (@DefIso (Prof_cat A B) P Q)) (z : τ (Obj (Product_cat (Op_cat A) B)))
 : τ (@= (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z))
    (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)))
≔ @eq_refl _ (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z);

symbol prof_defiso_raw_left_path [A B : Cat] [P Q : τ (Prof A B)]
 (I : τ (@DefIso (Prof_cat A B) P Q)) (z : τ (Obj (Product_cat (Op_cat A) B)))
 (u : τ (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z))) : τ (@= (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) u)) u)
≔ @eq_trans (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) u)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z) u)) u
  (@eq_ap (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)) (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z))
    (λ f : τ (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)), @fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) f u))
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@eq_sym _ _ _ (@prof_defiso_at_to_path A B P Q I z)))
  (@eq_ap (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)) (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z))
    (λ g : τ (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)), @fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) g (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z) u))
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@eq_sym _ _ _ (@prof_defiso_at_from_path A B P Q I z)));

symbol prof_defiso_raw_right_path [A B : Cat] [P Q : τ (Prof A B)]
 (I : τ (@DefIso (Prof_cat A B) P Q)) (z : τ (Obj (Product_cat (Op_cat A) B)))
 (u : τ (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z))) : τ (@= (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) u)) u)
≔ @eq_trans (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) u)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z) u)) u
  (@eq_ap (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)) (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z))
    (λ f : τ (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z)), @fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) f u))
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart Q P z (@defiso_from (Prof_cat A B) P Q I)) (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@eq_sym _ _ _ (@prof_defiso_at_from_path A B P Q I z)))
  (@eq_ap (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)) (Obj (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z))
    (λ g : τ (Functor (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z)), @fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) g (@fapp0 (@fapp0 (Product_cat (Op_cat A) B) Cat_cart Q z) (@fapp0 (Product_cat (Op_cat A) B) Cat_cart P z) (@defiso_at_from (Product_cat (Op_cat A) B) Cat_cart P Q I z) u))
    (@tapp0_fapp0 (Product_cat (Op_cat A) B) Cat_cart P Q z (@defiso_to (Prof_cat A B) P Q I)) (@defiso_at_to (Product_cat (Op_cat A) B) Cat_cart P Q I z)
    (@eq_sym _ _ _ (@prof_defiso_at_to_path A B P Q I z)));
