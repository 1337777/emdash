"""Source-pinned original native homology-quotient comparison and equivalence.

Original whole maps, inverse data and reviewers own qualification.
No new mathematical declaration, formal rule or caller assumption.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _point_readings, _body
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_one_cat_image_family_covers.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 79,
                                                         'initialOp': 5,
                                                         'shapeAction': 0,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0,
                                                         'walkingConstructor': 0},
                                              'sha256': '5ffe0187b09bba20b8450e9eaaf1ca0c6e7cf362e7a783ce0c7af5966c051b20',
                                              'wholeViews': {'diagram_evaluation_at_func': 6,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 27,
                                                             'diagram_family_transf': 1,
                                                             'one_cat_functor_category': 0,
                                                             'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_homology_quotient_comparison.lp': {'counts': {'fapp0': 0,
                                                                         'functorCarrier': 0,
                                                                         'functorCategory': 0,
                                                                         'initialOp': 9,
                                                                         'shapeAction': 0,
                                                                         'tapp0_fapp0': 0,
                                                                         'transforCarrier': 0,
                                                                         'walkingConstructor': 0},
                                                              'sha256': 'b0a08c9b9163c71e082d84b5d7b4828a767ebbdec68a56a688e7cf7bab4f9318',
                                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                             'diagram_evaluation_transf': 0,
                                                                             'diagram_family_at_func': 0,
                                                                             'diagram_family_transf': 0,
                                                                             'one_cat_functor_category': 0,
                                                                             'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_homology_quotient_cover_source.lp': {'counts': {'fapp0': 0,
                                                                           'functorCarrier': 0,
                                                                           'functorCategory': 0,
                                                                           'initialOp': 4,
                                                                           'shapeAction': 0,
                                                                           'tapp0_fapp0': 0,
                                                                           'transforCarrier': 0,
                                                                           'walkingConstructor': 0},
                                                                'sha256': '4f6838cb50efa348c49d5ae85f6f8782b9e3aa024768647a0fab6371b9a3be1e',
                                                                'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                               'diagram_evaluation_transf': 0,
                                                                               'diagram_family_at_func': 0,
                                                                               'diagram_family_transf': 0,
                                                                               'one_cat_functor_category': 0,
                                                                               'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_homology_quotient_covers.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 2,
                                                                     'initialOp': 3,
                                                                     'shapeAction': 0,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0,
                                                                     'walkingConstructor': 0},
                                                          'sha256': 'd94dac7316c26a2e3ee08813da5c7d5d8f7fb38bd8b53526d75d02698af51b81',
                                                          'wholeViews': {'diagram_evaluation_at_func': 1,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0,
                                                                         'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_homology_quotient_equivalence.lp': {'counts': {'fapp0': 0,
                                                                          'functorCarrier': 0,
                                                                          'functorCategory': 24,
                                                                          'initialOp': 7,
                                                                          'shapeAction': 0,
                                                                          'tapp0_fapp0': 0,
                                                                          'transforCarrier': 0,
                                                                          'walkingConstructor': 0},
                                                               'sha256': '672f23050d9e2066ad1d7b540f185a207e73236fceee358ba42c03874ec68db7',
                                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                              'diagram_evaluation_transf': 0,
                                                                              'diagram_family_at_func': 0,
                                                                              'diagram_family_transf': 0,
                                                                              'one_cat_functor_category': 0,
                                                                              'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_homology_quotient_image.lp': {'counts': {'fapp0': 0,
                                                                    'functorCarrier': 0,
                                                                    'functorCategory': 80,
                                                                    'initialOp': 8,
                                                                    'shapeAction': 0,
                                                                    'tapp0_fapp0': 0,
                                                                    'transforCarrier': 0,
                                                                    'walkingConstructor': 0},
                                                         'sha256': '1f78a77d9ccff4454a7f1a50a925c4edc1a3ce8a9a9dadef1e8583fef85cc845',
                                                         'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                        'diagram_evaluation_transf': 0,
                                                                        'diagram_family_at_func': 0,
                                                                        'diagram_family_transf': 0,
                                                                        'one_cat_functor_category': 0,
                                                                        'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_observed_exactness.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 0,
                                                               'initialOp': 2,
                                                               'shapeAction': 0,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0,
                                                               'walkingConstructor': 0},
                                                    'sha256': '33323f35cd8136a9f2ce3024dad06114c07b27a33182e5fa718350312b17d5b0',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0,
                                                                   'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_image_family_covers.lp': {'counts': {'fapp0': 0,
                                                        'functorCarrier': 0,
                                                        'functorCategory': 9,
                                                        'initialOp': 2,
                                                        'shapeAction': 0,
                                                        'tapp0_fapp0': 0,
                                                        'transforCarrier': 0,
                                                        'walkingConstructor': 0},
                                             'sha256': '34ca36ec0c44d02ff33e5e959ca53cf70b876d1b82bef5fbc2656f1f7b3ce213',
                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                            'diagram_evaluation_transf': 0,
                                                            'diagram_family_at_func': 7,
                                                            'diagram_family_transf': 1,
                                                            'one_cat_functor_category': 0,
                                                            'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_homology_quotient_equivalence.lp': {'counts': {'fapp0': 0,
                                                                         'functorCarrier': 0,
                                                                         'functorCategory': 0,
                                                                         'initialOp': 8,
                                                                         'shapeAction': 0,
                                                                         'tapp0_fapp0': 0,
                                                                         'transforCarrier': 0,
                                                                         'walkingConstructor': 0},
                                                              'sha256': 'bd9de47d31327f63a09feda86a017a2b8d8ef704f3d0c175f5cb8032c0bfd7f7',
                                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                             'diagram_evaluation_transf': 0,
                                                                             'diagram_family_at_func': 0,
                                                                             'diagram_family_transf': 0,
                                                                             'one_cat_functor_category': 0,
                                                                             'sym_transf_tapp0_transf': 0}}}

def image_family_inclusion_view(text):
    Arr='(Functor_oplax_cat WalkingArrow_cat C)'
    K='(@kernel_adjunction_func C S t T P)'
    Q='(@cokernel_adjunction_arrow_func C S t T0 Q)'
    Im='(@adjunction_image_func C S t T T0 P Q)'
    E0='(@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src)'
    E1='(@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)'
    k='(@kernel_adjunction_inclusion C S t T P)'
    QF=f'(@comp_cat_fapp0 B {Arr} {Arr} {Q} F)'
    local=f'(@kernel_adjunction_family_inclusion_transf B C S t T P {QF})'
    whole=f'(@kernel_adjunction_family_inclusion_transf {Arr} C S t T P {Q})'
    direct=f'(@fapp0 _ _ (@comp_cat_con_fapp1_func B {Arr} C {QF} {K} {E0}) {k})'
    qk=f'(@fapp0 _ _ (@comp_cat_con_fapp1_func {Arr} {Arr} C {Q} {K} {E0}) {k})'
    action=f'(@comp_cat_con_fapp1_func B {Arr} C F {Im} {E1})'
    restricted=f'(@fapp0 _ _ {action} {qk})'
    target=f'(@fapp0 _ _ {action} {whole})'
    carrier=f'(@Transf B C (@comp_cat_fapp0 B {Arr} C {Im} F) (@diagram_oplax_family_at_func B WalkingArrow_cat C F walking_arrow_tgt))'
    body=f'''@eq_trans {carrier} {local} {direct} {target}
      (@one_cat_kernel_family_inclusion_whisker_path B C S C1 t T P {QF})
      (@eq_trans {carrier} {direct} {restricted} {target}
        (@eq_sym {carrier} {restricted} {direct}
          (@prewhisker_assoc_path B {Arr} {Arr} C F {Q} {K} {E0} {k}))
        (@eq_ap (@Transf {Arr} C {Im} {E1}) {carrier}
          (λ u : τ (@Transf {Arr} C {Im} {E1}), @fapp0 _ _ {action} u)
          {qk} {whole}
          (@eq_sym (@Transf {Arr} C {Im} {E1}) {whole} {qk}
            (@one_cat_kernel_family_inclusion_whisker_path {Arr} C S C1 t T P {Q}))))'''
    return _body(text,'one_cat_image_family_inclusion_path',body)


def image_family_factor_view(text):
    Arr='(Functor_oplax_cat WalkingArrow_cat C)'
    Coim='(@adjunction_coimage_func C S t T T0 P Q)'
    Im='(@adjunction_image_func C S t T T0 P Q)'
    E1='(@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt)'
    rawIm=f'(@fapp0 (Functor_cat {Arr} {Arr}) (Functor_cat {Arr} C) (@comp_cat_cov_func {Arr} {Arr} C (@kernel_adjunction_func C S t T P)) (@cokernel_adjunction_arrow_func C S t T0 Q))'
    k=f'(@kernel_adjunction_family_inclusion_transf {Arr} C S t T P (@cokernel_adjunction_arrow_func C S t T0 Q))'
    alpha='(@one_cat_coimage_image_comparison C S C1 t T T0 P Q)'
    left=f'(@comp_fapp0 (Functor_cat {Arr} C) {Coim} {Im} {E1} {k} {alpha})'
    raw=f'(@comp_fapp0 (Functor_cat {Arr} C) {Coim} {rawIm} {E1} {k} {alpha})'
    target='(@one_cat_adjunction_coimage_to_target C S C1 t T T0 P Q)'
    start=text.index('symbol one_cat_image_family_comparison_factor_path ')
    end=text.index('symbol one_cat_image_family_source_factor_path ',start)
    part=text[start:end];edits=[]
    for m in re.finditer(r'@eq_ap\b',part):
        args=[];cursor=m.end()
        for _ in range(6):a,cursor=_atom(part,cursor);args.append(a)
        if not args[-1].startswith('(@one_cat_coimage_target_kernel_factor_path'):continue
        assert args[3:5]==['_','_']
        proof=f'(@eq_trans {args[0]} {left} {raw} {target} (@eq_refl {args[0]} {left}) {args[5]})'
        args[3:]=[left,target,proof]
        edits.append((m.start(),cursor,'@eq_ap '+ '\n        '.join(args)))
    assert len(edits)==1
    a,b,new=edits[0];part=part[:a]+new+part[b:]
    return text[:start]+part+text[end:]


def quotient_image_zero_view(text):
    Arr='(Functor_oplax_cat WalkingArrow_cat C)'
    d='(@transf_arrow_diagram_func K C A B f)'
    qd=f'(@comp_cat_fapp0 K {Arr} {Arr} (@cokernel_adjunction_arrow_func C S t T0 Q) {d})'
    Im=f'(@kernel_adjunction_family_func K C S t T P {qd})'
    Qf=f'(@cokernel_adjunction_family_func K C S t T0 Q {d})'
    pi=f'(@cokernel_adjunction_family_projection_transf K C S t T0 Q {d})'
    k=f'(@kernel_adjunction_family_inclusion_transf K C S t T P {qd})'
    outgoing='(@one_cat_native_homology_quotient_outgoing K C S C1 t T T0 P Q A B D f g z)'
    composed=f'(@comp_fapp0 (Functor_cat K C) B {Qf} D {outgoing} {pi})'
    pik=f'(@comp_fapp0 (Functor_cat K C) {Im} B {Qf} {pi} {k})'
    zero=f'(@zero_arrow_family_zero_transf K C t T T0 {Im} {Qf})'
    kraw=f'(@comp_cat_fapp0 K {Arr} C (@kernel_adjunction_func C S t T P) {qd})'
    src=f'(@diagram_oplax_family_at_func K WalkingArrow_cat C {qd} walking_arrow_src)'
    tgt=f'(@diagram_oplax_family_at_func K WalkingArrow_cat C {qd} walking_arrow_tgt)'
    kd=f'(@comp_cat_fapp0 K {Arr} {Arr} (@kernel_adjunction_arrow_func C S t T P) {qd})'
    shape=lambda a:f'(@diagram_oplax_family_transf K WalkingArrow_cat C {a} walking_arrow_src walking_arrow_tgt walking_arrow_generator)'
    raw=f'(@comp_fapp0 (Functor_cat K C) {kraw} {src} {tgt} {shape(qd)} {shape(kd)})'
    rawzero=f'(@zero_arrow_family_zero_transf K C t T T0 {kraw} {tgt})'
    const='(@Const_func K C t)'
    initial=lambda y:shape(f'(@comp_cat_fapp0 K C {Arr} (@initial_arrow_diagram_func C t T0) {y})')
    terminal=shape(f'(@comp_cat_fapp0 K C {Arr} (@terminal_arrow_diagram_func C t T) {kraw})')
    zeroview=f'''(@eq_ap (@Transf K C {const} {Qf}) (@Transf K C {Im} {Qf})
      (λ u : τ (@Transf K C {const} {Qf}), @comp_fapp0 (Functor_cat K C) {Im} {const} {Qf} u {terminal})
      {initial(tgt)} {initial(Qf)}
      (@one_cat_initial_family_arrow_path K C C1 t T0 {Qf} {initial(tgt)}))'''
    start=text.index('symbol one_cat_native_homology_quotient_image_zero ')
    end=text.index('symbol one_cat_native_homology_quotient_image_lift ',start)
    part=text[start:end];edits=[]
    for m in re.finditer(r'@eq_ap\b',part):
        args=[];cursor=m.end()
        for _ in range(6):a,cursor=_atom(part,cursor);args.append(a)
        assert args[3:5]==['_','_']
        if 'one_cat_native_homology_quotient_outgoing_reconstruction' in args[5]:args[3:5]=['g',composed]
        elif args[5].startswith('(@one_cat_kernel_family_annihilation_path'):
            args[3:5]=[pik,zero]
            args[5]=f'(@eq_trans {args[0]} {pik} {raw} {zero} (@eq_refl {args[0]} {pik}) (@eq_trans {args[0]} {raw} {rawzero} {zero} {args[5]} {zeroview}))'
        else:raise AssertionError(args[5])
        edits.append((m.start(),cursor,'@eq_ap '+ '\n    '.join(args)))
    assert len(edits)==2
    for a,b,new in reversed(edits):part=part[:a]+new+part[b:]
    return text[:start]+part+text[end:]


def quotient_kernel_lift_view(text):
    name='one_cat_native_homology_quotient_kernel_image_zero'
    start=text.index('symbol '+name+' ')
    definition=text.index('≔',start)
    cursor=text.rindex(' : τ (@=',start,definition)+len(' : τ (@=')
    eq=[]
    for _ in range(3):a,cursor=_atom(text,cursor);eq.append(a)
    carrier,left,zero=eq
    assert zero.startswith('(@zero_arrow_family_zero_transf ')
    cursor=len('(@zero_arrow_family_zero_transf');args=[]
    for _ in range(7):a,cursor=_atom(zero,cursor);args.append(a)
    assert args[:5]==['K','C','t','T','T0']
    X,Y=args[5:]
    assert X.startswith('(@kernel_adjunction_family_func ')
    assert Y.startswith('(@cokernel_adjunction_family_func ')
    Arr='(Functor_oplax_cat WalkingArrow_cat C)'
    qd=f'(@comp_cat_fapp0 K {Arr} {Arr} (@cokernel_adjunction_arrow_func C S t T0 Q) (@transf_arrow_diagram_func K C A B f))'
    rawY=f'(@diagram_oplax_family_at_func K WalkingArrow_cat C {qd} walking_arrow_tgt)'
    rawzero=f'(@zero_arrow_family_zero_transf K C t T T0 {X} {rawY})'
    const='(@Const_func K C t)'
    shape=lambda a:f'(@diagram_oplax_family_transf K WalkingArrow_cat C {a} walking_arrow_src walking_arrow_tgt walking_arrow_generator)'
    initial=lambda y:shape(f'(@comp_cat_fapp0 K C {Arr} (@initial_arrow_diagram_func C t T0) {y})')
    terminal=shape(f'(@comp_cat_fapp0 K C {Arr} (@terminal_arrow_diagram_func C t T) {X})')
    view=f'''(@eq_ap (@Transf K C {const} {rawY}) {carrier}
      (λ u : τ (@Transf K C {const} {rawY}), @comp_fapp0 (Functor_cat K C) {X} {const} {rawY} u {terminal})
      {initial(Y)} {initial(rawY)}
      (@one_cat_initial_family_arrow_path K C C1 t T0 {rawY} {initial(Y)}))'''
    proof=f'(@{name} K C S C1 t T T0 P Q A B D f g z)'
    replacement=f'(@eq_trans {carrier} {left} {zero} {rawzero} {proof} {view})'
    pattern=r'\(@'+name+r'\s+K\s+C\s+S\s+C1\s+t\s+T\s+T0\s+P\s+Q\s+A\s+B\s+D\s+f\s+g\s+z\)'
    text,count=re.subn(pattern,lambda m:replacement,text)
    assert count==2
    return text


def migrate_native_quotient_consumer(name,original):
 if name not in SOURCES:return None
 spec=SOURCES[name];assert hashlib.sha256(original.encode()).hexdigest()==spec['sha256']
 text=original;B='(Functor_oplax_cat WalkingArrow_cat C)'
 for pattern,replacement,key in (
  (r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)','Functor_oplax_cat','functorCategory'),
  (r'\(Functor\s+WalkingArrow_cat\s+C\s*\)','(Obj '+B+')','functorCarrier'),
  (r'@Transf\s+WalkingArrow_cat\s+C\b','@Hom '+B,'transforCarrier'),
  (r'\bOp_cat(?=\s+C\b)','TotalOp_cat','initialOp')):
  text,count=re.subn(pattern,replacement,text);assert count==spec['counts'][key],(name,key,count)
 text=_point_readings(text,(spec['counts']['fapp0'],spec['counts']['tapp0_fapp0']))
 for head,arity,corrected in (
  ('diagram_family_at_func',3,'diagram_oplax_family_at_func'),
  ('diagram_family_transf',3,'diagram_oplax_family_transf'),
  ('diagram_evaluation_at_func',2,'diagram_oplax_evaluation_at_func'),
  ('diagram_evaluation_transf',2,'diagram_oplax_evaluation_transf'),
  ('sym_transf_tapp0_transf',3,'diagram_oplax_family_map_at'),
  ('one_cat_functor_category',2,'one_cat_oplax_functor_category')):
  edits=[]
  for match in re.finditer(r'@'+head+r'\b',text):
   cursor,args=match.end(),[]
   for _ in range(arity):a,cursor=_atom(text,cursor);args.append(a)
   if args[-2:]!=['WalkingArrow_cat','C']:continue
   edits.append((match.start(),match.end()))
  assert len(edits)==spec['wholeViews'][head],(name,head)
  for lo,hi in reversed(edits):text=text[:lo]+'@'+corrected+text[hi:]
 def arrow(args):
  d,x,y,f=args
  return f'@tapp0_fapp0 {B} C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {x}) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {y}) {d} (@diagram_oplax_evaluation_transf WalkingArrow_cat C {x} {y} {f})'
 text,count=map_calls(text,'fapp1_fapp0',4,arrow);assert count==spec['counts']['shapeAction']
 text=enc_walk(text)
 if name == 'emdash3_2_one_cat_image_family_covers.lp':
  old='@one_cat_diagram_family_transf_reindex_path'
  assert text.count(old)==1
  text=image_family_inclusion_view(text)
  text=image_family_factor_view(text)
 if name == 'emdash3_2_one_cat_native_homology_quotient_image.lp':
  text=quotient_image_zero_view(text)
  text=quotient_kernel_lift_view(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
