"""Source-pinned original native-snake input and connecting constructions.

Original arbitrary outer maps, K/Q and inverse data retain their roles.
Qualification belongs to complete original owners/reviewers, not this replay.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _point_readings
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_native_snake_inputs.lp': {'counts': {'fapp0': 0,
                                                 'functorCarrier': 0,
                                                 'functorCategory': 3,
                                                 'initialOp': 3,
                                                 'shapeAction': 0,
                                                 'tapp0_fapp0': 0,
                                                 'transforCarrier': 0,
                                                 'walkingConstructor': 0},
                                      'rules': 0,
                                      'sha256': '62f7a919aad45931533096138b18ae87b3cfad47b71affe462f5846c8c87977e',
                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                     'diagram_evaluation_transf': 0,
                                                     'diagram_family_at_func': 0,
                                                     'diagram_family_transf': 0,
                                                     'one_cat_functor_category': 0,
                                                     'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_connecting.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 0,
                                                             'initialOp': 3,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0,
                                                             'walkingConstructor': 0},
                                                  'rules': 0,
                                                  'sha256': 'e76a1d5085df2eeabdfd99e988c44b376760c20903334785d4ac25e0c155742a',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_cover.lp': {'counts': {'fapp0': 0,
                                                        'functorCarrier': 0,
                                                        'functorCategory': 1,
                                                        'initialOp': 8,
                                                        'shapeAction': 0,
                                                        'tapp0_fapp0': 0,
                                                        'transforCarrier': 0,
                                                        'walkingConstructor': 0},
                                             'rules': 0,
                                             'sha256': '2173dccafa96b9fd0af922f55864f877a68c35b3059077144750bbe56ceab616',
                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                            'diagram_evaluation_transf': 0,
                                                            'diagram_family_at_func': 0,
                                                            'diagram_family_transf': 0,
                                                            'one_cat_functor_category': 0,
                                                            'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_covered_map.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 1,
                                                              'initialOp': 5,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'rules': 0,
                                                   'sha256': '3fa1f84b458b34e2c0c7fe8968af1d1a622eb5fe55b98c52b95517d46ed39f40',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_exact_inputs.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 8,
                                                               'initialOp': 12,
                                                               'shapeAction': 0,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0,
                                                               'walkingConstructor': 0},
                                                    'rules': 0,
                                                    'sha256': '7eca2f19f88cc280bdd2c30ada35579e273cd4dcfa6337eaa6042b9f22c6aa39',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0,
                                                                   'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_factors.lp': {'counts': {'fapp0': 0,
                                                          'functorCarrier': 0,
                                                          'functorCategory': 0,
                                                          'initialOp': 4,
                                                          'shapeAction': 0,
                                                          'tapp0_fapp0': 0,
                                                          'transforCarrier': 0,
                                                          'walkingConstructor': 0},
                                               'rules': 0,
                                               'sha256': '324ef7f666993931889df55cd84105af39be92be8873f40379a90ec0db6d7e0c',
                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                              'diagram_evaluation_transf': 0,
                                                              'diagram_family_at_func': 0,
                                                              'diagram_family_transf': 0,
                                                              'one_cat_functor_category': 0,
                                                              'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_image.lp': {'counts': {'fapp0': 0,
                                                        'functorCarrier': 0,
                                                        'functorCategory': 6,
                                                        'initialOp': 9,
                                                        'shapeAction': 0,
                                                        'tapp0_fapp0': 0,
                                                        'transforCarrier': 0,
                                                        'walkingConstructor': 0},
                                             'rules': 0,
                                             'sha256': '71afc4b3b9ebd6d61f34241609feddf91b3d5131b3699cf6d23a5f0c4c1e95ec',
                                             'wholeViews': {'diagram_evaluation_at_func': 0,
                                                            'diagram_evaluation_transf': 0,
                                                            'diagram_family_at_func': 0,
                                                            'diagram_family_transf': 0,
                                                            'one_cat_functor_category': 0,
                                                            'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_inner_zeros.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 0,
                                                              'initialOp': 2,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'rules': 0,
                                                   'sha256': '78a6baae5c4b72dfc6f140bf312cf8d1e72dee115f590e77012004a1cae647b8',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_kernel_annihilation.lp': {'counts': {'fapp0': 0,
                                                                      'functorCarrier': 0,
                                                                      'functorCategory': 4,
                                                                      'initialOp': 5,
                                                                      'shapeAction': 0,
                                                                      'tapp0_fapp0': 0,
                                                                      'transforCarrier': 0,
                                                                      'walkingConstructor': 0},
                                                           'rules': 0,
                                                           'sha256': '45139413971041e00e13f1e4d06aef686e26b6f683f9dcc01e7aa80e1fefa851',
                                                           'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                          'diagram_evaluation_transf': 0,
                                                                          'diagram_family_at_func': 0,
                                                                          'diagram_family_transf': 0,
                                                                          'one_cat_functor_category': 0,
                                                                          'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_middle_lifts.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 0,
                                                               'initialOp': 6,
                                                               'shapeAction': 0,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0,
                                                               'walkingConstructor': 0},
                                                    'rules': 0,
                                                    'sha256': 'a4119ab63670e0780aeb3b23e1fae04df6641b9085b58ab87fe87ccc91a1c8d2',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0,
                                                                   'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_outer_zeros.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 0,
                                                              'initialOp': 2,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'rules': 0,
                                                   'sha256': 'd6d1cdf0f1050f0803a074563f9e9f0e590beec5ad4a2e73ca6fb499b70f90bd',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_six_term_maps.lp': {'counts': {'fapp0': 0,
                                                                'functorCarrier': 0,
                                                                'functorCategory': 2,
                                                                'initialOp': 10,
                                                                'shapeAction': 0,
                                                                'tapp0_fapp0': 0,
                                                                'transforCarrier': 0,
                                                                'walkingConstructor': 0},
                                                     'rules': 0,
                                                     'sha256': '4966b5671281dada39edce85dd562782a0151bd100298f3edee6ae357c431c90',
                                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                    'diagram_evaluation_transf': 0,
                                                                    'diagram_family_at_func': 0,
                                                                    'diagram_family_transf': 0,
                                                                    'one_cat_functor_category': 0,
                                                                    'sym_transf_tapp0_transf': 0}},
 'examples/native_snake_inputs.lp': {'counts': {'fapp0': 0,
                                                'functorCarrier': 0,
                                                'functorCategory': 2,
                                                'initialOp': 1,
                                                'shapeAction': 0,
                                                'tapp0_fapp0': 0,
                                                'transforCarrier': 0,
                                                'walkingConstructor': 0},
                                     'rules': 0,
                                     'sha256': 'd9222a9ab2895403062c95d3ab11ae7a33de712dcc59aafcc9a4ce3ed9295fdf',
                                     'wholeViews': {'diagram_evaluation_at_func': 0,
                                                    'diagram_evaluation_transf': 0,
                                                    'diagram_family_at_func': 0,
                                                    'diagram_family_transf': 0,
                                                    'one_cat_functor_category': 0,
                                                    'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_connecting.lp': {'counts': {'fapp0': 0,
                                                            'functorCarrier': 0,
                                                            'functorCategory': 0,
                                                            'initialOp': 4,
                                                            'shapeAction': 0,
                                                            'tapp0_fapp0': 0,
                                                            'transforCarrier': 0,
                                                            'walkingConstructor': 0},
                                                 'rules': 0,
                                                 'sha256': 'a048e1150db650e70910803e8efea96ca09e8a7a1b231823b0c900e0830504a1',
                                                 'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                'diagram_evaluation_transf': 0,
                                                                'diagram_family_at_func': 0,
                                                                'diagram_family_transf': 0,
                                                                'one_cat_functor_category': 0,
                                                                'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_cover.lp': {'counts': {'fapp0': 0,
                                                       'functorCarrier': 0,
                                                       'functorCategory': 5,
                                                       'initialOp': 1,
                                                       'shapeAction': 0,
                                                       'tapp0_fapp0': 0,
                                                       'transforCarrier': 0,
                                                       'walkingConstructor': 0},
                                            'rules': 0,
                                            'sha256': '9e883e966b4c687134fbb72650b1b3d12609517256f106acad1777cf2bdbb44f',
                                            'wholeViews': {'diagram_evaluation_at_func': 0,
                                                           'diagram_evaluation_transf': 0,
                                                           'diagram_family_at_func': 0,
                                                           'diagram_family_transf': 0,
                                                           'one_cat_functor_category': 0,
                                                           'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_factors.lp': {'counts': {'fapp0': 0,
                                                         'functorCarrier': 0,
                                                         'functorCategory': 2,
                                                         'initialOp': 1,
                                                         'shapeAction': 0,
                                                         'tapp0_fapp0': 0,
                                                         'transforCarrier': 0,
                                                         'walkingConstructor': 0},
                                              'rules': 0,
                                              'sha256': '767956953a77dce30c2de2eace0eee8d12923bc6ce6bf2e607c553cce51c5c08',
                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                             'diagram_evaluation_transf': 0,
                                                             'diagram_family_at_func': 0,
                                                             'diagram_family_transf': 0,
                                                             'one_cat_functor_category': 0,
                                                             'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_kernel_annihilation.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 0,
                                                                     'initialOp': 5,
                                                                     'shapeAction': 0,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0,
                                                                     'walkingConstructor': 0},
                                                          'rules': 0,
                                                          'sha256': 'f620dab3f6ebfb6419716c27bb74de5f7d927e641c6177970beacbf56c1dd146',
                                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0,
                                                                         'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_six_term_maps.lp': {'counts': {'fapp0': 0,
                                                               'functorCarrier': 0,
                                                               'functorCategory': 0,
                                                               'initialOp': 8,
                                                               'shapeAction': 0,
                                                               'tapp0_fapp0': 0,
                                                               'transforCarrier': 0,
                                                               'walkingConstructor': 0},
                                                    'rules': 0,
                                                    'sha256': '0c930d4dfca233f647de3445e67b0cbfc294146af630febe61b78edf1b33982c',
                                                    'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                   'diagram_evaluation_transf': 0,
                                                                   'diagram_family_at_func': 0,
                                                                   'diagram_family_transf': 0,
                                                                   'one_cat_functor_category': 0,
                                                                   'sym_transf_tapp0_transf': 0}}}

def snake_image_zero_view(text):
    Arr='(Functor_oplax_cat WalkingArrow_cat C)'
    d='(@native_snake_incoming_diagram K C t T A B X D b c h)'
    qd=f'(@comp_cat_fapp0 K {Arr} {Arr} (@cokernel_adjunction_arrow_func C S t T0 Q) {d})'
    Im='(@one_cat_native_snake_image_func K C S C1 t T T0 P Q A B X D b c h)'
    Qf=f'(@cokernel_adjunction_family_func K C S t T0 Q {d})'
    pi='(@native_snake_quotient_transf K C S t T T0 Q A B X D b c h)'
    k='(@one_cat_native_snake_image_inclusion K C S C1 t T T0 P Q A B X D b c h)'
    outgoing='(@one_cat_native_snake_gamma K C S C1 t T T0 Q A B X D b c h)'
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
    start=text.index('symbol one_cat_native_snake_image_zero ')
    end=text.index('symbol one_cat_native_snake_image_lift ',start)
    part=text[start:end];edits=[]
    for m in re.finditer(r'@eq_ap\b',part):
        args=[];cursor=m.end()
        for _ in range(6):a,cursor=_atom(part,cursor);args.append(a)
        assert args[3:5]==['_','_']
        if 'one_cat_native_snake_gamma_reconstruction' in args[5]:args[3:5]=['(@comp_fapp0 (Functor_cat K C) B X D c b)',composed]
        elif args[5].startswith('(@one_cat_kernel_family_annihilation_path'):
            args[3:5]=[pik,zero]
            args[5]=f'(@eq_trans {args[0]} {pik} {raw} {zero} (@eq_refl {args[0]} {pik}) (@eq_trans {args[0]} {raw} {rawzero} {zero} {args[5]} {zeroview}))'
        else:raise AssertionError(args[5])
        edits.append((m.start(),cursor,'@eq_ap '+ '\n    '.join(args)))
    assert len(edits)==2
    for a,b,new in reversed(edits):part=part[:a]+new+part[b:]
    return text[:start]+part+text[end:]


def snake_kernel_lift_view(text):
    name='one_cat_native_snake_kernel_image_zero'
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
    qd=f'(@comp_cat_fapp0 K {Arr} {Arr} (@cokernel_adjunction_arrow_func C S t T0 Q) (@native_snake_incoming_diagram K C t T A B X D b c h))'
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
    proof=f'(@{name} K C S C1 t T T0 P Q A B X D b c h)'
    replacement=f'(@eq_trans {carrier} {left} {zero} {rawzero} {proof} {view})'
    pattern=r'\(@'+name+r'\s+K\s+C\s+S\s+C1\s+t\s+T\s+T0\s+P\s+Q\s+A\s+B\s+X\s+D\s+b\s+c\s+h\)'
    text,count=re.subn(pattern,lambda m:replacement,text)
    assert count==2
    return text


def migrate_native_snake_input_consumer(name,original):
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
 if name == 'emdash3_2_one_cat_native_snake_image.lp':
  text=snake_image_zero_view(text)
 if name == 'emdash3_2_one_cat_native_snake_kernel_annihilation.lp':
  text=snake_kernel_lift_view(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
