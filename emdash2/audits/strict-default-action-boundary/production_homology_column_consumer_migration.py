"""Source-pinned original column and whole-transformation migration.

Retain the existing projection ladder and full original higher-action consumers.
"""
from pathlib import Path
import hashlib
import re
from production_diagram_observation_migration import _atom

SOURCES = {'emdash3_2_homology_window_column_usability.lp': {'diagramCategory': 122,
                                                   'fixedPointValue': 0,
                                                   'initialOp': 0,
                                                   'sha256': '4936fbda35942e785a9e752317dfde3f859a7224459bd00daa6addc14a581f6d'},
 'emdash3_2_homology_window_columns.lp': {'diagramCategory': 31,
                                          'fixedPointValue': 31,
                                          'initialOp': 0,
                                          'sha256': 'e6963d497b9a084c5ab93e454f398efe94f8a8a02032b96d787b93ee3dca1661'},
 'emdash3_2_homology_window_connecting_transformation.lp': {'diagramCategory': 11,
                                                            'fixedPointValue': 11,
                                                            'initialOp': 4,
                                                            'sha256': 'dbd9c292d76543aee32d5e246d3856319e4344e4ba7db853649b7beb35828b37'},
 'examples/homology_window_column_usability.lp': {'diagramCategory': 92,
                                                  'fixedPointValue': 0,
                                                  'initialOp': 0,
                                                  'sha256': '62e4ff294a32dc05185ff43c38f46d89db5742f37ccc7ae882c552a85bc2f682'},
 'examples/homology_window_connecting_transformation.lp': {'diagramCategory': 2,
                                                           'fixedPointValue': 0,
                                                           'initialOp': 9,
                                                           'sha256': '790de413964424daafb2e6ef4554e5404c72a52e7e56e744464126873419b652'}}


def migrate_homology_column_consumer(name, original):
    if name not in SOURCES:
        return None
    spec = SOURCES[name]
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256'], name
    text, count = re.subn(r'(?<=TerminalObject \()Op_cat(?= C\))', 'TotalOp_cat', original)
    assert count == spec['initialOp'], name
    text, count = re.subn(r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+\$?C\b)', 'Functor_oplax_cat', text)
    assert count == spec['diagramCategory'], name
    count = 0
    while hits := list(re.finditer(r'@fapp0\s+WalkingArrow_cat\s+C\b', text)):
        match = hits[-1]
        diagram, cursor = _atom(text, match.end())
        point, cursor = _atom(text, cursor)
        assert point in ('walking_arrow_src', 'walking_arrow_tgt'), (name, point)
        value = f'@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C {point}) {diagram}'
        text = text[:match.start()] + value + text[cursor:]
        count += 1
    assert count == spec['fixedPointValue'], name
    if name == 'emdash3_2_homology_window_columns.lp':
        old = '(@Op_func _ _ (@Sigma_proj1_func _ _))'
        assert text.count(old) == 2
        text = text.replace(old, '(@CoAbove2_func _ _ (@Op_func _ _ (@Sigma_proj1_func _ _)))')
        old_lhs = """rule @comp_fapp0 Cat_cat _ _ (@Functor_cat (@Join_cat Terminal_cat Terminal_cat) $C)
  (@comp_fapp0 Cat_cat _ _ _
    (@Op_func _ _ (@Product_projR_func _ _))
    (@Op_func _ _ (@sigma_map_func _ _ _
      (@Op_funcd _ _ _ (@sigma_proj1_family_funcd _ _ _)))))"""
        new_lhs = """rule @comp_fapp0 Cat_cat _ _
  (OddDual_cat (Functor_cat (OddDual_cat (@Join_cat Terminal_cat Terminal_cat)) (OddDual_cat $C)))
  (@comp_fapp0 Cat_cat _ _ _
    (@CoAbove2_func _ _ (@Op_func _ _ (@Product_projR_func _ _)))
    (@CoAbove2_func _ _ (@Op_func _ _ (@sigma_map_func _ _ _
      (@strict_transfor _ _ _ _
        (@TotalOp_funcd _ _ _ (@sigma_proj1_family_funcd _ _ _)))))))"""
        assert text.count(old_lhs) == 2
        text = text.replace(old_lhs, new_lhs)
        text = text.replace('// Native second projection, after Op/composition expose its two factors.',
                            '// Native second projection after total duality exposes its two factors.')
        text, count = re.subn(r'// lhs-audit: keep 4 -- SR cannot recover.*?// Hom_cat Cat_cat would reduce away before this pattern can discriminate.\n',
                             '// lhs-audit: keep 4 -- SR needs the actual OddDual/Functor target head of the oplax diagram classifier.\n', text, flags=re.S)
        assert count == 1
        text = text.replace('// lhs-audit: keep 4 -- same measured arrow-diagram target reconstruction guard.\n',
                            '// lhs-audit: keep 4 -- same measured oplax-diagram target guard, with the original left-column discriminator.\n')
    if name == 'emdash3_2_homology_window_column_usability.lp':
        begin = text.index('unif_rule\n')
        end = text.index('/* Expanded first Hom-action comparison')
        assert text[begin:end].count('unif_rule') == 4
        views = (Path(__file__).parent / 'production_homology_column_hom_views.lpfragment').read_text() + '\n\n\n'
        assert views.count('unif_rule') == 4
        text = text[:begin] + views + text[end:]
    return text


ENCODED_POINT_PREDECESSOR_SHA = 'd0f3988a7568b3dd9ccd79adc8a54a90f6b3265c40c4593d8c38bc3f312294d4'

def add_encoded_arrow_point_view(text):
    assert hashlib.sha256(text.encode()).hexdigest() == ENCODED_POINT_PREDECESSOR_SHA
    marker = '// Same point theorem on the decoded object; no equality data enters the graph.'
    assert text.count(marker) == 1
    view = (Path(__file__).parent / 'production_encoded_arrow_point_view.lpfragment').read_text() + '\n'
    return text.replace(marker, view + marker, 1)
