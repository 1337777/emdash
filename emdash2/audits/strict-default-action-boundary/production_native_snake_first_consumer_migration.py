"""Source-pinned original first native-snake exactness chain.

Original maps, inverse data and complete reviewers own qualification.
No new formal declaration, rule or caller assumption.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom, _point_readings
from production_selected_presentation_migration import map_calls
from production_introduced_input_migration import enc_walk

SOURCES = {'emdash3_2_one_cat_native_snake_comparison_kernels.lp': {'counts': {'fapp0': 0,
                                                                     'functorCarrier': 0,
                                                                     'functorCategory': 0,
                                                                     'initialOp': 4,
                                                                     'shapeAction': 0,
                                                                     'tapp0_fapp0': 0,
                                                                     'transforCarrier': 0,
                                                                     'walkingConstructor': 0},
                                                          'sha256': '29715237324b0164184f7d85fc431d5820b9b2608a2f0fd2fe5691b65bd1e3fe',
                                                          'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                         'diagram_evaluation_transf': 0,
                                                                         'diagram_family_at_func': 0,
                                                                         'diagram_family_transf': 0,
                                                                         'one_cat_functor_category': 0,
                                                                         'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_first_cover.lp': {'counts': {'fapp0': 0,
                                                              'functorCarrier': 0,
                                                              'functorCategory': 0,
                                                              'initialOp': 9,
                                                              'shapeAction': 0,
                                                              'tapp0_fapp0': 0,
                                                              'transforCarrier': 0,
                                                              'walkingConstructor': 0},
                                                   'sha256': '79c57e697ae17619e366c128b24f2fc15efe476a8da00cd2300130fa0f4ccc84',
                                                   'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                  'diagram_evaluation_transf': 0,
                                                                  'diagram_family_at_func': 0,
                                                                  'diagram_family_transf': 0,
                                                                  'one_cat_functor_category': 0,
                                                                  'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_first_exactness.lp': {'counts': {'fapp0': 0,
                                                                  'functorCarrier': 0,
                                                                  'functorCategory': 55,
                                                                  'initialOp': 6,
                                                                  'shapeAction': 0,
                                                                  'tapp0_fapp0': 0,
                                                                  'transforCarrier': 0,
                                                                  'walkingConstructor': 0},
                                                       'sha256': 'e92c28f95d1ff7f6fd86ac0dca058a9bf29bc686c026654b6f999b03ba2a9507',
                                                       'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                      'diagram_evaluation_transf': 0,
                                                                      'diagram_family_at_func': 0,
                                                                      'diagram_family_transf': 0,
                                                                      'one_cat_functor_category': 0,
                                                                      'sym_transf_tapp0_transf': 0}},
 'emdash3_2_one_cat_native_snake_first_kernel_comparison.lp': {'counts': {'fapp0': 0,
                                                                          'functorCarrier': 0,
                                                                          'functorCategory': 6,
                                                                          'initialOp': 13,
                                                                          'shapeAction': 0,
                                                                          'tapp0_fapp0': 0,
                                                                          'transforCarrier': 0,
                                                                          'walkingConstructor': 0},
                                                               'sha256': 'b44a2e7210daf74aa6c234d09a7762666e2b0f8d4f48dfdbda23c97c68f89308',
                                                               'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                              'diagram_evaluation_transf': 0,
                                                                              'diagram_family_at_func': 0,
                                                                              'diagram_family_transf': 0,
                                                                              'one_cat_functor_category': 0,
                                                                              'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_comparison_kernels.lp': {'counts': {'fapp0': 0,
                                                                    'functorCarrier': 0,
                                                                    'functorCategory': 24,
                                                                    'initialOp': 8,
                                                                    'shapeAction': 0,
                                                                    'tapp0_fapp0': 0,
                                                                    'transforCarrier': 0,
                                                                    'walkingConstructor': 0},
                                                         'sha256': '2301141af863fa0e367887c2ee80b310a5f2bdc8b63323b4dcb4a0057edbcb5e',
                                                         'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                        'diagram_evaluation_transf': 0,
                                                                        'diagram_family_at_func': 0,
                                                                        'diagram_family_transf': 0,
                                                                        'one_cat_functor_category': 0,
                                                                        'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_first_cover.lp': {'counts': {'fapp0': 0,
                                                             'functorCarrier': 0,
                                                             'functorCategory': 0,
                                                             'initialOp': 3,
                                                             'shapeAction': 0,
                                                             'tapp0_fapp0': 0,
                                                             'transforCarrier': 0,
                                                             'walkingConstructor': 0},
                                                  'sha256': 'b16825adfbe9716c2cab238df4aa4954dd663142f9adc1c089f07a0ddcdd249f',
                                                  'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                 'diagram_evaluation_transf': 0,
                                                                 'diagram_family_at_func': 0,
                                                                 'diagram_family_transf': 0,
                                                                 'one_cat_functor_category': 0,
                                                                 'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_first_exactness.lp': {'counts': {'fapp0': 0,
                                                                 'functorCarrier': 0,
                                                                 'functorCategory': 5,
                                                                 'initialOp': 4,
                                                                 'shapeAction': 0,
                                                                 'tapp0_fapp0': 0,
                                                                 'transforCarrier': 0,
                                                                 'walkingConstructor': 0},
                                                      'sha256': 'be4f550f1d91c218e4e7248efef47ed1cd74ff1619528b1d0b74fe12416b5de1',
                                                      'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                     'diagram_evaluation_transf': 0,
                                                                     'diagram_family_at_func': 0,
                                                                     'diagram_family_transf': 0,
                                                                     'one_cat_functor_category': 0,
                                                                     'sym_transf_tapp0_transf': 0}},
 'examples/one_cat_native_snake_first_kernel_comparison.lp': {'counts': {'fapp0': 0,
                                                                         'functorCarrier': 0,
                                                                         'functorCategory': 0,
                                                                         'initialOp': 4,
                                                                         'shapeAction': 0,
                                                                         'tapp0_fapp0': 0,
                                                                         'transforCarrier': 0,
                                                                         'walkingConstructor': 0},
                                                              'sha256': '62b7379b9c0cc4140d18548904afe86ff9469d7f89a217ef914b129afa973d49',
                                                              'wholeViews': {'diagram_evaluation_at_func': 0,
                                                                             'diagram_evaluation_transf': 0,
                                                                             'diagram_family_at_func': 0,
                                                                             'diagram_family_transf': 0,
                                                                             'one_cat_functor_category': 0,
                                                                             'sym_transf_tapp0_transf': 0}}}

def snake_first_kernel_lift_view(text):
    name='one_cat_native_snake_first_kernel_image_zero'
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


def snake_first_second_zero_view(text):
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
    start=text.index('symbol one_cat_native_snake_first_image_kernel_second_zero ')
    end=text.index('symbol one_cat_native_snake_first_image_kernel_to_kernel ',start)
    part=text[start:end];edits=[]
    for m in re.finditer(r'@eq_ap\b',part):
        args=[];cursor=m.end()
        for _ in range(6):a,cursor=_atom(part,cursor);args.append(a)
        if not args[5].startswith('(@one_cat_kernel_family_annihilation_path'):continue
        assert args[3:5]==['_','_']
        if args[5].startswith('(@one_cat_kernel_family_annihilation_path'):
            args[3:5]=[pik,zero]
            args[5]=f'(@eq_trans {args[0]} {pik} {raw} {zero} (@eq_refl {args[0]} {pik}) (@eq_trans {args[0]} {raw} {rawzero} {zero} {args[5]} {zeroview}))'
        else:raise AssertionError(args[5])
        edits.append((m.start(),cursor,'@eq_ap '+ '\n    '.join(args)))
    assert len(edits)==1
    for a,b,new in reversed(edits):part=part[:a]+new+part[b:]
    return text[:start]+part+text[end:]


def migrate_native_snake_first_consumer(name,original):
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
 if name == 'emdash3_2_one_cat_native_snake_first_kernel_comparison.lp':
  text=snake_first_kernel_lift_view(text)
  text=snake_first_second_zero_view(text)
 decl=r'(?m)^(?:(?:protected|injective|constant) )?symbol\s+(\w+)'
 assert re.findall(decl,original)==re.findall(decl,text),name
 assert re.findall(r'(?m)^(assert(?:not)?)\b',original)==re.findall(r'(?m)^(assert(?:not)?)\b',text),name
 return text
