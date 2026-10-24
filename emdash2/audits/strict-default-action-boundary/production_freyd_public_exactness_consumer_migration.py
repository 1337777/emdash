"""Source-pinned original public Freyd exactness and certificate views.

Retain actual native inputs, maps, inverses and original all-test contracts.
"""
import hashlib
import re
from pathlib import Path
from production_diagram_observation_migration import _atom

SOURCES = {'emdash3_2_commutative_algebra_freyd_native_delta_comparison.lp': {'initialOp': 0,
                                                                    'sha256': '5e9ed8ff1a6658f47158394ed66a830f197532ac7dc33c57e005f24daab7ab4e',
                                                                    'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_diagram_exactness.lp': {'initialOp': 0,
                                                                     'sha256': 'ef84612915758222488bd3d6dd83610f1938cac42000adb72f9472f9b7d866f0',
                                                                     'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_les_certificate_views.lp': {'initialOp': 0,
                                                                         'sha256': 'd96b3a21f2dbbd11a6f8f781359aadadfb88cbb630ea0b88cea3914b75e6379b',
                                                                         'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_middle_pair_exactness.lp': {'initialOp': 0,
                                                                         'sha256': '355b8dc98a93073fdfcd23cb66ce43ba74d9ed219450672bec6bd707e7ebf367',
                                                                         'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_middle_public_exactness.lp': {'initialOp': 0,
                                                                           'sha256': '7aa745ab5d5639d915c6a3c77c371238ec952b2dbe8f499653886a85666ccc76',
                                                                           'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_source_pair_exactness.lp': {'initialOp': 0,
                                                                         'sha256': '044559094696d58637a616020b9224a5fbafebec3c20026869cf9b03fd1dfc31',
                                                                         'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_source_public_exactness.lp': {'initialOp': 0,
                                                                           'sha256': 'bd7e478d0edbc06417bd1b3b7af680cc6013b507f404c2e92ca822b4f3ef1e5a',
                                                                           'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_target_pair_exactness.lp': {'initialOp': 0,
                                                                         'sha256': '7bc861ea61ccd14f1826a85919e5f03f707c726a7c8c79f430d06e125ebc0179',
                                                                         'walkingArrowOplax': 0},
 'emdash3_2_commutative_algebra_freyd_native_target_public_exactness.lp': {'initialOp': 0,
                                                                           'sha256': '5e78bf5f2968bf9492e0257817d15f3e4d144a5e89b7e69e70c258e194a768ad',
                                                                           'walkingArrowOplax': 0},
 'emdash3_2_one_cat_family_public_pair_exactness.lp': {'initialOp': 3,
                                                       'sha256': '8c9bca4fa6f086574eb7e50c67cedfb33cb71ac67404b2d091ec6259b68b9e4f',
                                                       'walkingArrowOplax': 9},
 'emdash3_2_one_cat_native_exact_diagrams.lp': {'initialOp': 3,
                                                'sha256': '2ce5b12de450b762271690d7da8e7fec92eec2739dc9e21797d18f3e3c2d4baa',
                                                'walkingArrowOplax': 0},
 'examples/freyd_native_diagram_exactness.lp': {'initialOp': 0,
                                                'sha256': '9ce1ac0b80c269b7c8c16a747f56cb5f6357f535a345d30529fbf6b8215061e6',
                                                'walkingArrowOplax': 0},
 'examples/freyd_native_middle_pair_exactness.lp': {'initialOp': 0,
                                                    'sha256': '9ae6ef0be9c220b6f2e02314e37f7f3511cc606a482239e5662e55265cda1e9e',
                                                    'walkingArrowOplax': 0},
 'examples/freyd_native_middle_public_exactness.lp': {'initialOp': 0,
                                                      'sha256': '36bc3f8338a61cae9191b780e324eee5a0f7b1a4136d81ebd46a83d6633453a2',
                                                      'walkingArrowOplax': 1},
 'examples/freyd_native_source_pair_exactness.lp': {'initialOp': 0,
                                                    'sha256': '081c5bd3a95387baecdb87430a0efcd0c4c0ed6ac3f9b09fb002966b1b64e849',
                                                    'walkingArrowOplax': 0},
 'examples/freyd_native_source_public_exactness.lp': {'initialOp': 0,
                                                      'sha256': 'b392bbb7807294f0c46ab7a54bf97c2c6ce228547a59c520bb8b4730b49edc25',
                                                      'walkingArrowOplax': 0},
 'examples/freyd_native_target_pair_exactness.lp': {'initialOp': 0,
                                                    'sha256': '8b6d2128ef907ccc9017aa8aa57d3c4ec756366cf81acfc11b2ffd42bc751f50',
                                                    'walkingArrowOplax': 0},
 'examples/freyd_native_target_public_exactness.lp': {'initialOp': 0,
                                                      'sha256': '50833c0e0cc944bf83193e7ffb92cda9732e7fca7749f294119a90a77465bc3e',
                                                      'walkingArrowOplax': 0},
 'examples/freyd_whole_homology_family_comparison.lp': {'initialOp': 0,
                                                        'sha256': 'dde2d9fe56ed0a5855305886cfb1ef132f38a980f931134920b06eb8972eb136',
                                                        'walkingArrowOplax': 9},
 'examples/native_exact_diagrams.lp': {'initialOp': 4,
                                       'sha256': '74995e8db1e673c28563ee7e5ec965d31392b76bdc1c5c154eed8237899c6487',
                                       'walkingArrowOplax': 0}}

def migrate_freyd_public_exactness_consumer(name, original):
    if name not in SOURCES:
        return None
    spec = SOURCES[name]
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256'], name
    text, count = re.subn(r'\bOp_cat(?=\s+C\b)', 'TotalOp_cat', original)
    assert count == spec['initialOp'] and len(re.findall(r'\bOp_cat\b', original)) == count, name
    text, count = re.subn(r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+(?:C\b|\(@CommRingFreydPresentation_cat\s+R\)))', 'Functor_oplax_cat', text)
    assert count == spec['walkingArrowOplax'], name
    if name == 'emdash3_2_commutative_algebra_freyd_native_middle_public_exactness.lp':
        marker = 'symbol freyd_native_middle_public_exact '
        assert text.count(marker) == 1
        before, tail = text.split(marker, 1)
        old_head = '@one_cat_row_triple_homology_exact_omega'
        assert tail.count(old_head) == 1
        tail = tail.replace(old_head, '@one_cat_row_triple_homology_exact_family_view')
        view = (Path(__file__).resolve().parent / 'production_freyd_middle_exact_family_view.lpfragment').read_text()
        text = before + view + '\n' + marker + tail
    if name == 'emdash3_2_commutative_algebra_freyd_native_source_public_exactness.lp':
        starts = list(re.finditer(r'(?m)^symbol\s+(freyd_native_source_public_\w+)\b', text))
        assert len(starts) == 3
        parts = []
        for k, match in enumerate(starts):
            end = starts[k + 1].start() if k + 1 < len(starts) else len(text)
            part = text[match.start():end]
            definition = part.index('≔')
            head, cursor = _atom(part, definition + 1)
            args = []
            while True:
                while part[cursor].isspace():
                    cursor += 1
                if part[cursor] == ';':
                    break
                arg, cursor = _atom(part, cursor)
                args.append(arg)
            assert head in ('@native_family_public_pair_input', '@native_family_public_pair_equiv', '@native_family_public_pair_exact')
            assert args[23].startswith('(@eq_sym _ _ _ (@freyd_native_column_outgoing_homology_path')
            projection = args[10][1:-1]
            phead, pos = _atom(projection, 0)
            assert phead == '@one_cat_native_window_homology_projection'
            window = []
            while projection[pos:].strip():
                arg, pos = _atom(projection, pos)
                window.append(arg)
            assert len(window) == 23
            view_args = window + [args[13], args[14], args[15], args[19], args[20], args[17], args[23]]
            args[23] = '(@one_cat_native_window_projection_comparison_view ' + ' '.join(view_args) + ')'
            if head == '@native_family_public_pair_exact':
                assert len(args) == 31 and args[30].startswith('(@freyd_raw_native_window_source_exact ')
                args[30] = '(@one_cat_native_window_source_exact_family_view ' + ' '.join(window) + ')'
            parts.append(part[:definition] + '≔ ' + head + '\n  ' + '\n  '.join(args) + ';' + part[cursor + 1:])
        views = '\n'.join((Path(__file__).resolve().parent / fragment).read_text() for fragment in (
            'production_freyd_source_projection_comparison_view.lpfragment',
            'production_freyd_source_exact_family_view.lpfragment'))
        text = text[:starts[0].start()] + views + '\n' + ''.join(parts)
    if name == 'emdash3_2_commutative_algebra_freyd_native_target_public_exactness.lp':
        starts = list(re.finditer(r'(?m)^symbol\s+(freyd_native_target_public_\w+)\b', text))
        assert len(starts) == 3
        parts = []
        for k, match in enumerate(starts):
            end = starts[k + 1].start() if k + 1 < len(starts) else len(text)
            part = text[match.start():end]
            definition = part.index('≔')
            head, cursor = _atom(part, definition + 1)
            args = []
            while True:
                while part[cursor].isspace():
                    cursor += 1
                if part[cursor] == ';':
                    break
                arg, cursor = _atom(part, cursor)
                args.append(arg)
            assert head in ('@native_family_public_pair_input', '@native_family_public_pair_equiv', '@native_family_public_pair_exact')
            assert args[24].startswith('(@eq_sym _ _ _ (@freyd_native_column_incoming_homology_path')
            projection = args[11][1:-1]
            phead, pos = _atom(projection, 0)
            assert phead == '@one_cat_native_window_homology_inclusion'
            window = []
            while projection[pos:].strip():
                arg, pos = _atom(projection, pos)
                window.append(arg)
            assert len(window) == 23
            view_args = window + [args[13], args[15], args[16], args[20], args[21], args[18], args[24]]
            args[24] = '(@one_cat_native_window_inclusion_comparison_view ' + ' '.join(view_args) + ')'
            if head == '@native_family_public_pair_exact':
                assert len(args) == 31 and args[30].startswith('(@freyd_raw_native_window_target_exact ')
                args[30] = '(@one_cat_native_window_target_exact_family_view ' + ' '.join(window) + ')'
            parts.append(part[:definition] + '≔ ' + head + '\n  ' + '\n  '.join(args) + ';' + part[cursor + 1:])
        views = '\n'.join((Path(__file__).resolve().parent / fragment).read_text() for fragment in (
            'production_freyd_target_inclusion_comparison_view.lpfragment',
            'production_freyd_target_exact_family_view.lpfragment'))
        text = text[:starts[0].start()] + views + '\n' + ''.join(parts)
    return text
