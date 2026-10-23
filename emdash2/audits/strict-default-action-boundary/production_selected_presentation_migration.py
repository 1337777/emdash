"""Replay original selected kernel/cokernel presentations on the corrected owners.

This module is source authoring, not a proof checker. Qualification belongs to
its emitted LP, complete original consumers and recorded interaction gates.
"""
from pathlib import Path
import hashlib
import re

from production_diagram_observation_migration import _point_readings, _atom

AUDIT = Path(__file__).resolve().parent
B = '(Functor_oplax_cat WalkingArrow_cat C)'
IW = '(OddDual_cat WalkingArrow_cat)'
CW = '(OddDual_cat C)'

SOURCE_SHA256 = {'emdash3_2_kernel_adjunction_presentations.lp': '41fd84012db3dc2383e22446da6781e830504f3880c89565c8dbc376b2bc5c42', 'emdash3_2_cokernel_adjunction_presentations.lp': 'cfeb34961938aade615acba9f50bc209a48eff19433b76dd0d1777f045f26d6e', 'examples/chain_pair_homology_actions.lp': '505c559e35df15ef64d6a91f9e8a97c45bb422808f15bdf2ec869522c775a227', 'emdash3_2_chain_pair_homology_actions.lp': '250200629635f54b709005f5b7c26950a3aa916bd885007e4aed30469a217f6d', 'emdash3_2_homology_family_map_factors.lp': 'd77557b08dc66ec7c8e679e42537d523907834ec611dda9217797293615aea2d', 'emdash3_2_homology_family_records.lp': '5c8d0b6e871094a3e731d5ef4086623fdd69510b90b01bf702a2851a0a3e8f8f', 'emdash3_2_kernel_adjunction_records.lp': '25d11727ee3d400d6ca7cce4430830d0f4b726dde1fd1ec14cbcf0bfff3bec37', 'emdash3_2_kernel_adjunction_unmate_paths.lp': '8f43cc0aa3a4c774397d1e92093f0ba7f7e788e1b1abf6856130e6ed977e0204', 'emdash3_2_kernel_adjunction_unmates.lp': '7800c025727b0aad3067bc821d5f33d3eb94f8fb71fa07695bb05694fd66a67e', 'emdash3_2_kernel_adjunction_mates.lp': '79b2cb208098862f8f0c049ee107e409ac92cb0ed9039a4143f53c15ebe83fb0', 'emdash3_2_cokernel_adjunction_records.lp': 'aced63accc0b06ff27ef05feca5453e6cd428fc8a47886af2f4e2ebf6aeb4b1b', 'emdash3_2_cokernel_adjunction_mates.lp': '753f249b1ac3582ae3776e71b1a58d2b2507e4a008c3caca55c360e037d8f3a3', 'emdash3_2_homology_families.lp': '7fd504316b769c3afd702f35025f2a084762ef084da07ae91957407bcd644a53', 'emdash3_2_chain_pair_zero_cone_maps.lp': 'dbba92d305ecbfbb9c3f3fe342202e7c548da035085f70b111626db3cdd90a4d', 'emdash3_2_kernel_presentation_boundary_naturality.lp': '541bfc9e3f7ccf9453d24376b35c966792005c837569bb957540a2f57f7a17c0', 'emdash3_2_kernel_presentation_inclusion_properties.lp': '66df8e6760c67dc600f7bc6553c6997708ce0c1fc8c383d093f6580864245dae', 'emdash3_2_zero_arrow_cone_map_introduction.lp': 'fc37893f62b43b8f2d60e6d55a54f71c5fac936fd351cf55b175bc867bf5a3b6', 'emdash3_2_chain_pair_zero_cones.lp': '34e6e94776d2daf930c5b053205ed7b9b45e1ce3497a60d83724b1d28b759482', 'emdash3_2_chain_pair_homology_records.lp': 'ea229412a8bb954f02e31ffdbc1a58aa05446e15ebafc4ec5baae0c0b514d56d', 'emdash3_2_chain_pair_zero_cone_comparisons.lp': 'cce3b9d88bba0aaa47111b463386d71044322eb468414849b446f617cce41b63', 'emdash3_2_zero_arrow_cone_homology.lp': 'bea4c952794ce40860f7309aa672a6d64a082f004949180b70e2998eee161491', 'emdash3_2_homology_family_selected_views.lp': '45bfcac35009a7d6d119b893e624090345a9fd8949567bee90e920c76cda95fd', 'examples/chain_pair_homology_records.lp': '985b4b8a5c90977c936dc7cc6a6a536afc04f9b5c953a69a000dcbcb0394119a', 'examples/chain_pair_zero_cones.lp': '567729a138e94c9bb78052294257bf3c0310257c5f1d97328f6b1006a9da9937', 'examples/chain_pair_zero_cone_comparisons.lp': 'b32ec6f97c6f02d7cd47b19bfa3b15319e7a734d6920d734a1136ecca09e5bec', 'examples/chain_pair_zero_cone_maps.lp': 'f820d7cc6f060a7d8c122e56614d4a1afee7303898ea5f24a33aa8e09feca7c7', 'examples/kernel_adjunction_presentations.lp': '4b6dfe8d6f9a742c605902a47902aa3016caef5c47d257ef60b9418d92ac5894', 'examples/cokernel_adjunction_presentations.lp': '620fa318f2eb9da4cbef5d506df5b5195506bc94da07f97706a763414af2d463', 'examples/kernel_adjunction_mates.lp': '96196d0bece16f56af97062e9ca3be235b91f8a3a97580d55b395b249ec8f866', 'examples/cokernel_adjunction_mates.lp': '9cd97dd0c1c896933700f08f3e8ff4255673adc06dc94d41d5d2402521dfa844', 'examples/kernel_adjunction_records.lp': 'af3803aeee5b432c5459a6594ca7587724c8ea9959c4c996f775f1f536fd3c36', 'examples/cokernel_adjunction_records.lp': 'e32afd21b19fa1ef6523d41a91f3f984f06785d684670e586d9233c1d124a16b', 'examples/kernel_presentation_metadata_comparisons.lp': '991cdbe944cb34c391965d140f8a253f9eda7751d160ad8cb5cb03af6a0260f7', 'examples/cokernel_presentation_metadata_comparisons.lp': '8605102f789495e1e99b88c2c0895179753d62a3c5d3ca671d1f622878eb2823', 'examples/homology_families.lp': '35569646c9e3328df72d8c5ca98bf350c47958a8527ab390db5b8a58d65a3d9f', 'examples/homology_family_records.lp': 'e5f1ac28825b3e522e1e33fc232c144fb111b6351bb474bd101564693f15a793', 'examples/homology_family_map_factors.lp': 'dbefd23ca1e80ddbeb4e0800d574364cbf8d0025f9a1fb461a9bdaa8cbc50b5a', 'examples/zero_arrow_cone_map_introduction.lp': 'ca8559e7a22ca37940fa9231b9250dd8ec8b761070572ac7b20e7b627ce6fbfb'}

NATIVE_VIEWS = {'emdash3_2_chain_pair_zero_cone_maps.lp': {'nativeMapImport': True}, 'emdash3_2_chain_pair_zero_cones.lp': {'nativeMapImport': False}, 'emdash3_2_chain_pair_homology_records.lp': {'nativeMapImport': False}, 'emdash3_2_chain_pair_zero_cone_comparisons.lp': {'nativeMapImport': False}, 'examples/chain_pair_zero_cones.lp': {'nativeMapImport': False}, 'examples/chain_pair_zero_cone_comparisons.lp': {'nativeMapImport': False}, 'examples/chain_pair_zero_cone_maps.lp': {'nativeMapImport': True}}

def map_calls(s,head,n,build):
 pat=r'@'+head+r'\s+WalkingArrow_cat\s+C\b';count=0
 while hits:=list(re.finditer(pat,s)):
  m=hits[-1];i=m.end();args=[]
  for _ in range(n):a,i=_atom(s,i);args.append(a)
  s=s[:m.start()]+build(args)+s[i:];count+=1
 return s,count

def migrate_selected_presentation(name,s):
 if name not in SOURCE_SHA256:return None
 assert hashlib.sha256(s.encode()).hexdigest()==SOURCE_SHA256[name],name
 counts={}
 s=re.sub(r'Functor_cat(?=\s+WalkingArrow_cat\s+\$?C\b)','Functor_oplax_cat',s)
 s=s.replace('(Functor WalkingArrow_cat C)',f'(Obj {B})')
 s=re.sub(r'@Transf\s+WalkingArrow_cat\s+C\b','@Hom '+B,s)
 s=s.replace('(Op_cat C)','(TotalOp_cat C)')
 s=s.replace('@diagram_evaluation_at_func','@diagram_oplax_evaluation_at_func')
 s=re.sub(r'@one_cat_functor_category(?=\s+WalkingArrow_cat\s+C\b)','@one_cat_oplax_functor_category',s)
 point_counts=tuple(len(re.findall(r'@'+head+r'\s+WalkingArrow_cat\s+C\b',s)) for head in ['fapp0','tapp0_fapp0']);s=_point_readings(s,point_counts);counts['points']=point_counts
 def arrow(args):
  d,x,y,f=args
  return f'@tapp0_fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {x}) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {y}) {d} (@diagram_oplax_evaluation_transf WalkingArrow_cat C {x} {y} {f})'
 s,counts['arrows']=map_calls(s,'fapp1_fapp0',4,arrow)
 s,counts['strictProfiles']=map_calls(s,'IsStrictTransfor',3,lambda a:f'@IsStrictTransfor {IW} {CW} {a[1]} {a[0]} {a[2]}')
 def natural(a):
  f,g,eta,pe,x,y,h=a
  carrier=f'(Obj (Hom_cat C (@fapp0 {IW} {CW} {f} {x}) (@fapp0 {IW} {CW} {g} {y})))'
  return f'@eq_sym {carrier} _ _ (@strict_component_naturality_path {IW} {CW} {g} {f} {eta} {pe} {y} {x} {h})'
 s,counts['naturality']=map_calls(s,'strict_component_naturality_path',7,natural)
 # Reuse the original OneCat witness through the explicit dual closure.
 s,counts['ordinaryProfiles']=map_calls(s,'one_cat_transfor_is_strict',4,lambda a:f'@one_cat_transfor_is_strict {IW} {CW} (@one_cat_odd_dual C {a[0]}) {a[2]} {a[1]} {a[3]}')
 if name in ['emdash3_2_kernel_adjunction_presentations.lp','emdash3_2_cokernel_adjunction_presentations.lp']:
  kind='kernel' if name=='emdash3_2_kernel_adjunction_presentations.lp' else 'cokernel'
  mark=('// Proof-time comparison of the same two arrows after the source object' if kind=='kernel' else '// Same-arrow composition comparison at the named presentation target.')
  a=s.index(mark);u=s.index('unif_rule',a);b=s.index('];',u)+2;s=s[:a]+'/* Audit: the existing generic same-arrow congruence is being tested\n   in place of this selected metadata instance.\n'+(AUDIT/f'production_selected_{kind}_metadata.lpfragment').read_text().rstrip()+'\n*/'+s[b:]
 if name in ['examples/kernel_adjunction_presentations.lp','examples/cokernel_adjunction_presentations.lp']:
  def strict_default(block):
   t=block.group()
   if 'd0 d1 d2' in t and '@comp_fapp0' in t and '@fapp1_fapp0' in t:return t.replace('assertnot','assert',1)
   return t
  s=re.sub(r'(?m)^assertnot[\s\S]*?;',strict_default,s)

 if name in ['examples/kernel_adjunction_presentations.lp','examples/cokernel_adjunction_presentations.lp']:
  kind='kernel' if name=='examples/kernel_adjunction_presentations.lp' else 'cokernel'
  edits=[];n=0
  for m in re.finditer(r'(?m)^assert[\s\S]*?;',s):
   if 'unit_adj_transf' not in m[0] or 'counit_adj_transf' not in m[0]:continue
   cat=(B if kind=='kernel' else 'C') if n==0 else ('C' if kind=='kernel' else B)
   new,count=re.subn(r'(?<![@\w])comp_fapp0\b','@comp_fapp0 '+cat+' _ _ _',m[0]);assert count==2
   edits.append((m.start(),m.end(),new));n+=1
  assert n==2
  for a,b,new in reversed(edits):s=s[:a]+new+s[b:]
 if name in ['emdash3_2_kernel_adjunction_mates.lp','emdash3_2_cokernel_adjunction_mates.lp']:
  kind='kernel' if name=='emdash3_2_kernel_adjunction_mates.lp' else 'cokernel';side='to' if kind=='kernel' else 'from'
  old=f'@fapp0 _ _ (@defiso_at_{side} _ _ _ _'
  new=f'@fapp0 _ _ (@defiso_fmap_{side} _ _ Cat_cart_include _ _\n    (@defiso_at _ Cat_cart _ _'
  assert s.count(old)==1;a=s.index(old);b=s.index('];',a)+2;block=s[a:b].replace(old,new,1)
  pair='(Struct_sigma $X $d)' if kind=='kernel' else '(Struct_sigma $d $X)'
  assert block.count(pair+') $h')==1;block=block.replace(pair+') $h',pair+')) $h');s=s[:a]+block+s[b:]
  s=s.replace('// Same selected interpretation through the stable evaluated-inverse owner.','// Same selected interpretation through the actual mapped coefficient inverse.\n// Retain selected data and the arrow; ignore only the annihilation proof payload.')
 if name=='emdash3_2_homology_family_map_factors.lp':
  a=s.index('symbol homology_family_projection_naturality');b=s.index(';',a)+1
  s=s[:a]+(AUDIT/'production_selected_projection_naturality.lpfragment').read_text().rstrip()+s[b:]
 native=NATIVE_VIEWS
 if name in native:
  from production_freyd_entry_migration import _native_review
  s=_native_review(s)
  if native[name]['nativeMapImport']:
   s='require open emdash.emdash3_2_one_cat_chain_pair_native_maps;\n'+s
 if name=='emdash3_2_zero_arrow_cone_map_introduction.lp':
  old='≔ Struct_sigma a (Struct_sigma b\n'
  new='≔ @zero_cone_native_map C t T A0 A1 d0 d1\n    (@fapp0 _ _ (@kernel_presentation_unlift_func C S t T W P A0 d0) h0)\n    (@fapp0 _ _ (@kernel_presentation_unlift_func C S t T W P A1 d1) h1)\n    a b\n'
  assert s.count(old)==1;s=s.replace(old,new,1)
  assert s.rstrip().endswith('p)));');s=s.rstrip()[:-5]+'p));\n'
  s='require open emdash.emdash3_2_zero_arrow_cone_maps;\n'+s
 if name=='examples/homology_families.lp':
  s=s.replace('// Normal identity computes; generic H composition is not an ambient strict cut.', '// Identity and composition use the default strict-functor laws.')
  a=s.index('assertnot ');b=s.index(';',a);block=s[a:b]
  assert '@comp_fapp0 C' in block;block=block.replace('assertnot','assert',1);s=s[:a]+block+s[b:]
  assert s.count('@diagram_family_transf')==1;s=s.replace('@diagram_family_transf','@diagram_oplax_family_transf')
 return s



def finish_selected_core(text):
    """Refine existing comparison/action owners after the older pinned replays."""
    old = '''// Sufficient congruence when the two actual arrows are identical.
// Compare every endpoint; this is not injectivity of composition.
unif_rule @comp_fapp0 (Functor_cat $B $C) $X $Y $Z $g $f
  ≡ @comp_fapp0 (Functor_cat $B0 $C0) $X0 $Y0 $Z0 $g $f
  ↪ [ $B ≡ $B0; $C ≡ $C0; $X ≡ $X0; $Y ≡ $Y0; $Z ≡ $Z0 ];'''
    assert text.count(old) == 1
    text = text.replace(old, (AUDIT / 'production_composition_metadata_congruence.lpfragment').read_text().rstrip(), 1)
    start = text.index('symbol tapp1_fapp0 :')
    end = text.index(';', start)
    signature = text[start:end]
    old_result = 'τ (Hom B (fapp0 F X) (fapp0 G Y))'
    assert signature.count(old_result) == 1
    signature = signature.replace(old_result, 'τ (Obj (Hom_cat B (fapp0 F X) (fapp0 G Y)))')
    text = text[:start] + signature + text[end:]
    marker = '// Proof-time duality between covariant postcomposition and contravariant'
    assert text.count(marker) == 1
    text = text.replace(marker, (AUDIT / 'production_prewhisker_action_composition.lpfragment').read_text() + '\n' + marker, 1)
    text = text.replace(marker, (AUDIT / 'production_prewhisker_metadata_congruence.lpfragment').read_text() + '\n' + marker, 1)
    marker = '// Cat-valued capped precomposition exposes ordinary transfor projections.'
    start = text.index(marker)
    end = text.index(';', text.index('rule ', start)) + 1
    return text[:start] + (AUDIT / 'production_prewhisker_projection_rules.lpfragment').read_text() + text[end:]


def finish_selected_diagram(text):
    """Install qualified dual-cut joins at their existing semantic owners."""
    old = '≔ @comp_cat_fapp0 K (Functor_cat I C) C (@diagram_evaluation_at_func I C i) D;'
    new = '≔ @hom_precomp_along_fapp0 Cat_cat Cat_cat (@id_func Cat_cat)\n    C K (Functor_cat I C) D (@diagram_evaluation_at_func I C i);'
    assert text.count(old) == 1
    text = text.replace(old, new, 1)
    marker = '// Read represented postcomposition in Odd(A)'
    assert text.count(marker) == 1
    text = text.replace(marker, (AUDIT / 'production_odd_dual_precomposition.lpfragment').read_text() + '\n' + marker, 1)
    for marker, fragment in (
        ('// The same strict functor on the alternating duals, with whole Hom action.',
         'production_odd_dual_adjunction_cuts.lpfragment'),
        ('// Original shape-reindex comparison at its new actual projection owner.',
         'production_oplax_exchange_adjunction_cuts.lpfragment'),
        ('// Structural ordinary-category closure for the corrected oplax diagram',
         'production_odd_dual_ordinary_profile.lpfragment'),
    ):
        assert text.count(marker) == 1, marker
        text = text.replace(marker, (AUDIT / fragment).read_text() + '\n' + marker, 1)
    start = text.index('// Original shape-reindex comparison at its new actual projection owner.')
    end = text.index('];', start) + 2
    text = text[:start] + (AUDIT / 'production_stable_prewhisker_reindex.lpfragment').read_text().rstrip() + text[end:]
    marker = 'symbol diagram_oplax_evaluation_transf'
    assert text.count(marker) == 1
    text = text.replace(marker, (AUDIT / 'production_precomposition_composite_view.lpfragment').read_text() + '\n' + marker, 1)
    return text


def finish_selected_family_views(s):
    """Use the existing whole prewhiskering comparison in the mate proofs."""
    assert hashlib.sha256(s.encode()).hexdigest() == '9036a99fbdd225f0be135b760da34245273647e6b0b64c4264897baa0b7219a8'
    for direction in ['untranspose','transpose']:
     nm='one_cat_adjunction_family_'+direction+'_agrees';a=s.index('symbol '+nm+' ');b=s.index('≔',a);c=s.index(';',b);old=s[b+1:c].strip()
     if direction=='transpose':
      C='R';source='A';mid='(@comp_cat_fapp0 B R R (@comp_cat_fapp0 R L R G F) A)';target='(@comp_cat_fapp0 B L R G D)'
      P='(@comp_cat_fapp0 B R L F A)'
      left=f'(@fapp0 _ _ (@comp_cat_cov_fapp1_func B L R G {P} D) h)'
      action=f'(@hom_precomp_along_fapp1_comp_prod_path Cat_cat Cat_cat (@id_func Cat_cat) R B R A (@id_func R) (@comp_cat_fapp0 R L R G F) (@unit_adj_transf R L F G J))'
      U=f'(Obj (Hom_cat (Functor_cat B R) {source} {mid}))'
      lam=f'(λ v : τ {U}, @comp_fapp0 (Functor_cat B R) {source} {mid} {target} {left} v)'
     else:
      C='L';source='(@comp_cat_fapp0 B R L F A)';mid='(@comp_cat_fapp0 B L L (@comp_cat_fapp0 L R L F G) D)';target='D'
      P='(@comp_cat_fapp0 B L R G D)'
      right=f'(@fapp0 _ _ (@comp_cat_cov_fapp1_func B R L F A {P}) h)'
      action=f'(@hom_precomp_along_fapp1_comp_prod_path Cat_cat Cat_cat (@id_func Cat_cat) L B L D (@comp_cat_fapp0 L R L F G) (@id_func L) (@counit_adj_transf R L F G J))'
      U=f'(Obj (Hom_cat (Functor_cat B L) {mid} {target}))'
      lam=f'(λ v : τ {U}, @comp_fapp0 (Functor_cat B L) {source} {mid} {target} v {right})'
     T=f'(Obj (Hom_cat (Functor_cat B {C}) {source} {target}))'
     new=f'''≔ @eq_trans {T} _ _ _
        ({old})
        (@eq_ap {U} {T} {lam} _ _
          (@eq_sym _ _ _ {action}))'''
     s=s[:b]+new+s[c:]
    return s


def finish_selected_homology_comparison(s):
    """Keep actual whole exchange images and derive the same inverse laws."""
    # The source itself is emitted by the earlier exactly pinned replay.
    assert hashlib.sha256(s.encode()).hexdigest() == '23952fa1d52fd64dc1eaf3cd88b9521467a008c266f5787499c569b3d3764778'
    marker = 'protected symbol homology_family_comparison_mapped_boundary_evidence'
    a = s.index(marker)
    b = s.index('≔', a)
    signature = s[a:b]
    atom = '@diagram_family_shape_func WalkingArrow_cat B C'
    edits = []
    for match in re.finditer(re.escape(atom), signature):
        H, end = _atom(signature, match.end())
        view = ('@fapp0 (Functor_cat WalkingArrow_cat (Functor_cat B C)) '
                '(Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) '
                '(@one_cat_family_oplax_exchange_func WalkingArrow_cat B C C1) ' + H)
        edits.append((match.start(), end, view))
    assert len(edits) == 2
    for start, end, view in reversed(edits):
        signature = signature[:start] + view + signature[end:]
    s = s[:a] + signature + s[b:]

    def arguments(term):
        if term.startswith('('):
            term = term[1:-1]
        result, cursor = [], 0
        while cursor < len(term):
            value, cursor = _atom(term, cursor)
            result.append(value)
        return result

    for side in ('right', 'left'):
        name = 'homology_family_comparison_diagram_' + side + '_law'
        start = s.index('protected symbol ' + name + ' ')
        body = s.index('≔', start)
        end = s.index(';', body)
        signature = s[start:body]
        formula = signature[signature.index(': τ (@=') + len(': τ (@='):].strip()
        carrier, cursor = _atom(formula, 0)
        lhs, cursor = _atom(formula, cursor)
        rhs, cursor = _atom(formula, cursor)
        terms = arguments(carrier)
        assert terms[:2] == ['@Transf', 'B']
        F, G = terms[-2:]
        proof = (f'≔ @one_cat_oplax_diagram_family_map_path B C C1\n'
                 f'    {F} {G} {lhs} {rhs}\n'
                 f'    (@homology_family_comparison_diagram_{side}_source_law B C C1 t T A D h S P)\n'
                 f'    (@homology_family_comparison_diagram_{side}_target_law B C C1 t T A D h S P)')
        # Intentional newlines in the LP body, not escaped shell text.
        proof = proof.replace('\\n', '\n')
        s = s[:body] + proof + s[end:]
    return s


def finish_selected_prewhisker_check(text):
    """Retain whole comparison while checking the stable runtime boundary."""
    needle = '@hom_precomp_along_fapp1_fapp0 K Cat_cat E Z x y f G H eta'
    matches = [m for m in re.finditer(r'(?m)^assert\s+\[K : Cat\][\s\S]*?;', text)
               if needle in m[0]]
    assert len(matches) == 1
    match = matches[0]
    context, formula = match[0][:-1].split('⊢', 1)
    if '≡' not in formula:
        # Some diagnostic projections are carried by earlier exact replay
        # stages. Accept only this exact already-produced form, not drift.
        assert '@hom_precomp_along_fapp1_comp_prod_path K Cat_cat E Z x y f G H eta' in formula
        negatives = [m for m in re.finditer(r'(?m)^assertnot\s+\[K : Cat\][\s\S]*?;', text)
                     if needle in m[0]]
        assert len(negatives) == 1
        original = negatives[0][0].replace('assertnot ', 'assert ', 1)
        expected = finish_selected_prewhisker_check(original)
        assert text.count(expected) == 1, 'changed stable-prewhiskering diagnostic'
        return text
    lhs, rhs = [part.strip() for part in formula.split('≡', 1)]
    carrier = '''(Obj (Hom_cat (Functor_cat (@fapp0 K Cat_cat E x) Z)
      (@hom_precomp_along_fapp0 K Cat_cat E Z x y f G)
      (@hom_precomp_along_fapp0 K Cat_cat E Z x y f H)))'''
    typed = (context + '⊢\n  @hom_precomp_along_fapp1_comp_prod_path K Cat_cat E Z x y f G H eta\n'
             '  : τ (@= ' + carrier + '\n    (' + lhs + ')\n    (' + rhs + '));')
    negative = match[0].replace('assert ', 'assertnot ', 1)
    replacement = ('// The retained action has the same whole horizontal interpretation.\n'
                   '// Its runtime head remains stable until a tapp projection observes it.\n'
                   + typed + '\n\n'
                   '// An unconditional runtime fold would lose identity endpoints.\n'
                   + negative)
    return text[:match.start()] + replacement + text[match.end():]


def finish_selected_arrow_diagram(text):
    """Retarget the existing point comparison after the duality join."""
    assert hashlib.sha256(text.encode()).hexdigest() == '3f176a96d6d285f81ba0f768c76ba33d63e6d46c2525206221ed1832e540051c'
    start = text.index('unif_rule\n')
    end = text.index('];', start) + 2
    before = text[start:end]
    assert before.count('unif_rule') == 1 and '@OddDual_func' in before
    replacement = (AUDIT / 'production_walking_point_precomposition.lpfragment').read_text().rstrip()
    return text[:start] + replacement + text[end:]


def finish_selected_adjunction_reviewer(text):
    """Retain whole component equations at their existing proof-time owner."""
    assert hashlib.sha256(text.encode()).hexdigest() == '4fad703e2496b7bc18451d6d0df68a6d2ca8c5564e75cf2e867a097cb3f1e844'
    edits = []
    for match in re.finditer(r'(?m)^assert\s[\s\S]*?;', text):
        if '@comp_cat_con_fapp1_func' not in match[0]:
            continue
        context, formula = match[0][:-1].split('⊢', 1)
        lhs, rhs = [part.strip() for part in formula.split('≡', 1)]
        if '@unit_adj_transf R L F G J' in rhs:
            Z, u = 'R', 'A'
            f, g = '(@id_func R)', '(@comp_cat_fapp0 R L R G F)'
            eta = '(@unit_adj_transf R L F G J)'
        else:
            assert '@counit_adj_transf R L F G J' in rhs
            Z, u = 'L', 'D'
            f, g = '(@comp_cat_fapp0 L R L F G)', '(@id_func L)'
            eta = '(@counit_adj_transf R L F G J)'
        def point(h):
            return f'(@hom_postcomp_fapp0 Cat_cat Cat_cat (@id_func Cat_cat) B {Z} {Z} {h} {u})'
        carrier = f'(Obj (Hom_cat (Functor_cat B {Z}) {point(f)} {point(g)}))'
        proof = f'@hom_postcomp_tele_tapp0_component_eq Cat_cat Cat_cat (@id_func Cat_cat) B {Z} {Z} {f} {g} {eta} {u}'
        new = (context + '⊢\n  ' + proof + '\n  : τ (@= ' + carrier
               + '\n    (' + lhs + ')\n    (' + rhs + '));\n\n'
               + '// The whole presentations remain distinct runtime owners.\n'
               + match[0].replace('assert ', 'assertnot ', 1))
        edits.append((match.start(), match.end(), new))
    assert len(edits) == 2
    for start, end, new in reversed(edits):
        text = text[:start] + new + text[end:]
    return text.replace('// A component is one whole prewhiskered original cell.',
                        '// The existing theorem gives the whole prewhiskering presentation;\n'
                        '// nested components below retain their runtime computations.')
