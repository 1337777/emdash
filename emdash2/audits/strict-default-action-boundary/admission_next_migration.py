#!/usr/bin/env python3
"""Emit the next existing-owner reindex prerequisite; never run Lambdapi.

No canonical strictness is postulated. Whole object/raw-map presentation and
generic inclusion compatibility are separately labelled candidates. The
actual Prof map agreement remains a consumer, not a rule supplied here.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    pins_path = audit / 'admission_next_inputs.json'
    pins = json.loads(pins_path.read_text())
    source_inputs = {}
    for name, expected in pins['sourceInputs'].items():
        if name == 'emdash3_2.lp':
            data = subprocess.check_output(
                ['git', 'show', pins['productionRevision'] + ':emdash2/' + name], cwd=root)
        else:
            data = (root / name).read_bytes()
        assert digest(data) == expected, (name, 'source pin changed')
        source_inputs[name] = data
    prior = json.loads(source_inputs['audits/strict-default-action-boundary/local_cart_prof_verification.json'])
    baseline_name = 'tmp/probes/local_cart_prof/composition_profile_consumer.lp'
    baseline = source_inputs[baseline_name].decode()
    assert digest(baseline.encode()) == prior['outputs']['composition_profile_consumer.lp']
    assert prior['checks']['composition_profile_consumer.lp']['outcome'] == 'passed-fresh'
    production = source_inputs['emdash3_2.lp'].decode()
    start_anchor = '// Full base-arrow action of reindexing.'
    end_anchor = '// 18d. Unit hom profunctor and readable representables'
    assert production.count(start_anchor) == production.count(end_anchor) == 1
    start = production.index(start_anchor)
    end = production.index(end_anchor, start)
    raw_action = production[start:end]
    assert 'symbol Prof_reindex_fapp1_func' not in baseline
    assert raw_action.count('(Functor_cat\n') == 1
    cart_action = raw_action.replace('(Functor_cat\n', '(Functor_cart_cat\n')
    owner_anchor = '// Unchanged raw production owner: identity endpoint reindexing\n'
    assert baseline.count(owner_anchor) == 1

    names = ('admission_next_reindex_view.lpfragment',
             'admission_next_reindex_action_controls.lpfragment',
             'admission_next_reindex_view_controls.lpfragment',
             'admission_next_reindex_map_boundary.lpfragment')
    fragments = {name: (audit / name).read_text() for name in names}
    view = fragments[names[0]]
    assert len(re.findall(r'(?m)^unif_rule\b', view)) == 1
    assert not re.search(r'(?m)^rule\b', view)
    assert not re.search(r'(?m)^(?:rule|unif_rule|(?:injective |constant )?symbol)\b',
                         '\n'.join(fragments[name] for name in names[1:]))
    raw_owner = baseline.replace(owner_anchor, raw_action + '\n' + owner_anchor)
    cart_owner = baseline.replace(owner_anchor, cart_action + '\n' + owner_anchor)
    view_owner = baseline.replace(owner_anchor, cart_action + '\n' + view + '\n' + owner_anchor)
    action_controls = fragments[names[1]]
    view_controls = fragments[names[2]]
    targets = {
        'old_action_owner.lp': raw_owner + '\n' + action_controls,
        'reindex_action.lp': cart_owner + '\n' + action_controls,
        'reindex_view.lp': view_owner + '\n' + action_controls + '\n' + view_controls,
        'reindex_map_boundary.lp': view_owner + '\n' + action_controls + '\n' +
                                   view_controls + '\n' + fragments[names[3]],
        'no_object_view.lp': cart_owner + '\n' + action_controls + '\n' + view_controls,
    }
    preserved_outputs = {
        'old_action_owner.lp': '3599c261b93d97bde0e05522d2023d98a7df3ab7bb3881be312a15ac981f2f8e',
        'reindex_action.lp': 'a6bc157c16b8afd79e22d27935e0a62f719b44985a844cd35fc7159907055f22',
        'reindex_view.lp': '35b7f271a389bccfbf8db3346469e924a7101fdebaa92920744894b4ef349bc6',
        'reindex_map_boundary.lp': 'c8a29bf6fb9613b3ffac191ceae0210e2fda74cf11c3103349e9deb612bfaa75',
        'no_object_view.lp': 'c154d23a08d3c443fdd9980caa10edae400df7f03f5f113bf32f9487907a7689',
    }
    for name, expected in preserved_outputs.items():
        assert digest(targets[name].encode()) == expected, (name, 'preserved predecessor changed')

    additional_names = (
        'admission_next_raw_map_view.lpfragment',
        'admission_next_raw_map_controls.lpfragment',
        'admission_next_raw_map_view_controls.lpfragment',
        'admission_next_precomp_inclusion_view.lpfragment',
        'admission_next_precomp_inclusion_controls.lpfragment',
        'admission_next_precomp_inclusion_boundary.lpfragment',
    )
    fragments.update({name: (audit / name).read_text() for name in additional_names})
    raw_map_view = fragments[additional_names[0]]
    raw_map_controls = fragments[additional_names[1]]
    raw_view_controls = fragments[additional_names[2]]
    inclusion_view = fragments[additional_names[3]]
    inclusion_controls = fragments[additional_names[4]]
    inclusion_boundary = fragments[additional_names[5]]
    for candidate in (raw_map_view, inclusion_view):
        assert len(re.findall(r'(?m)^unif_rule\b', candidate)) == 1
        assert not re.search(r'(?m)^rule\b', candidate)
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b', '\n'.join((
        raw_map_controls, raw_view_controls, inclusion_controls, inclusion_boundary)))

    # Complete the fixed-prewhiskering dependency ladder before testing it.
    # The independent full tapp1 assertion is deliberately before the new
    # whole-view clause; it cannot obtain its result from that comparison.
    inclusion_anchor = '''rule @tapp1_fapp0 $A $B $F $F $X $Y (@id _ $F) $p
  ↪ @fapp1_fapp0 $A $B $F $X $Y $p;'''
    raw_map_anchor = '// Unchanged raw production owner: implication endpoint reindexing\n'

    def add_inclusion(source, include_view):
        assert source.count(inclusion_anchor) == 1
        group = inclusion_controls
        if include_view:
            group += '\n' + inclusion_view + '\n' + inclusion_boundary
        return source.replace(inclusion_anchor, inclusion_anchor + '\n\n' + group)

    def add_raw_map(source, include_view):
        assert source.count(raw_map_anchor) == 1
        group = raw_map_controls
        if include_view:
            group += '\n' + raw_map_view + '\n' + raw_view_controls
        return source.replace(raw_map_anchor, group + '\n' + raw_map_anchor)

    targets['raw_map_action.lp'] = add_raw_map(targets['reindex_view.lp'], False)
    targets['raw_map_view.lp'] = add_raw_map(targets['reindex_view.lp'], True)
    targets['precomp_action.lp'] = add_inclusion(targets['reindex_view.lp'], False)
    targets['precomp_inclusion.lp'] = add_inclusion(targets['reindex_view.lp'], True)
    targets['full_bridge.lp'] = add_raw_map(add_inclusion(targets['reindex_map_boundary.lp'], True), True)
    assert targets['full_bridge.lp'].count(raw_map_view) == 1
    assert targets['full_bridge.lp'].count(inclusion_view) == 1
    targets['no_raw_map_view.lp'] = targets['full_bridge.lp'].replace(raw_map_view, '')
    targets['no_precomp_inclusion_view.lp'] = targets['full_bridge.lp'].replace(inclusion_view, '')
    assert targets['full_bridge.lp'].index(inclusion_controls) < targets['full_bridge.lp'].index(inclusion_view)
    assert targets['full_bridge.lp'].index(raw_map_controls) < targets['full_bridge.lp'].index(raw_map_view)
    assert targets['full_bridge.lp'].endswith(fragments[names[3]])

    preserved_map_stage_outputs = {
        'raw_map_action.lp': 'd42945e02884500f396b02439cef51eda732852d179a0c20f484422dc098fe3a',
        'raw_map_view.lp': '0113e7562a57736416865286717b02c69cef0ebb939e1e769bdcc32563716ce9',
        'precomp_action.lp': '3038b69e48db555089e8ce967cfaff0c4a0934a2c8af687a837af87dbdf8933f',
        'precomp_inclusion.lp': '55bd511d039293b773ecf2a05c47bffbf4a4933d217fbb794c1279f043bc938e',
        'full_bridge.lp': '483da15abc6bdb7c36e8235032ed0c0664d2b9be0a2b7c277f3dcbb791ef178c',
        'no_raw_map_view.lp': '692fdec2170f1b753b18e0c145f117d80f721494002ea1a218b2355f2a80b724',
        'no_precomp_inclusion_view.lp': '6d1786b106485dfac8017550d461df7abbfbd8fc781ef14d1212354cb6b8d989',
    }
    for name, expected in preserved_map_stage_outputs.items():
        assert digest(targets[name].encode()) == expected, (name, 'preserved map stage changed')
    raw_composition_name = 'admission_next_reindex_raw_composition_view.lpfragment'
    raw_composition_view = (audit / raw_composition_name).read_text()
    fragments[raw_composition_name] = raw_composition_view
    assert len(re.findall(r'(?m)^unif_rule\b', raw_composition_view)) == 1
    assert not re.search(r'(?m)^rule\b', raw_composition_view)
    for old, new in (
            ('raw_map_view.lp', 'raw_composition_map_view.lp'),
            ('full_bridge.lp', 'raw_composition_full_bridge.lp')):
        assert targets[old].count(view) == 1
        targets[new] = targets[old].replace(view, view + '\n' + raw_composition_view)
    final_bridge = targets['raw_composition_full_bridge.lp']
    for name, fragment in (
            ('raw_composition_without_object_view.lp', raw_composition_view),
            ('raw_composition_without_map_view.lp', raw_map_view),
            ('raw_composition_without_inclusion_view.lp', inclusion_view)):
        assert final_bridge.count(fragment) == 1
        targets[name] = final_bridge.replace(fragment, '')

    preserved_raw_composition_outputs = {
        'raw_composition_map_view.lp': 'ee86fc3abc7e4fff105e4c4deb4b1e69132eaa2a207197c09d82e04832603303',
        'raw_composition_full_bridge.lp': '77b13d4d6978daed8403f075718cae9ea5e66303d3d1e99f702deaf2c1cc9424',
        'raw_composition_without_object_view.lp': 'fa4298c5ffb07baf34fb2341dbbe88f1d9d9beff2ade9d2e424885da4005a599',
        'raw_composition_without_map_view.lp': '05927fe36b8dc2d0de149777c9715526ae075b4db3aa2ce4f47285c669514a11',
        'raw_composition_without_inclusion_view.lp': '2198e8249299a0059085105e5569922b81785ad3b087f9ffcf19146c8f8f1112',
    }
    for name, expected in preserved_raw_composition_outputs.items():
        assert digest(targets[name].encode()) == expected, (name, 'preserved raw-composition stage changed')
    staged_name = 'admission_next_reindex_map_staged.lpfragment'
    staged_bridge = (audit / staged_name).read_text()
    fragments[staged_name] = staged_bridge
    assert not re.search(r'(?m)^(?:rule|unif_rule)\b', staged_bridge)
    final_boundary = fragments[names[3]]
    assert final_bridge.endswith(final_boundary)
    targets['staged_full_bridge.lp'] = final_bridge[:-len(final_boundary)] + staged_bridge
    for name, fragment in (
            ('staged_without_raw_composition_view.lp', raw_composition_view),
            ('staged_without_raw_map_view.lp', raw_map_view),
            ('staged_without_precomp_inclusion.lp', inclusion_view)):
        assert targets['staged_full_bridge.lp'].count(fragment) == 1
        targets[name] = targets['staged_full_bridge.lp'].replace(fragment, '')

    authoring = [Path(__file__), pins_path, *(audit / n for n in names + additional_names),
                 audit / raw_composition_name, audit / staged_name,
                 audit / 'admission_next_source_closure.md']
    manifest = {
        'status': 'authoring replay only; no checker outcome recorded by this builder',
        'productionRevision': pins['productionRevision'],
        'sourceInputs': pins['sourceInputs'],
        'baselineReceipt': prior['checks']['composition_profile_consumer.lp']['id'],
        'preservedPredecessorOutputs': preserved_outputs,
        'preservedMapStageOutputs': preserved_map_stage_outputs,
        'preservedRawCompositionOutputs': preserved_raw_composition_outputs,
        'fullSourceContinuation': False,
        'existingOwnerImport': {
            'source': 'emdash3_2.lp', 'startLine': production.count('\n', 0, start) + 1,
            'endLine': production.count('\n', 0, end),
            'unmodifiedBlockSha256': digest(raw_action.encode()),
            'adaptedBlockSha256': digest(cart_action.encode()),
            'adaptation': 'Only Prof_reindex_fapp1_func target Functor_cat becomes Functor_cart_cat, as required by selected Hom_Cat; its inputs and three action clauses are unchanged.'},
        'qualification': {
            'rawPublicProfMap': 'unchanged; no global Cartesian retyping',
            'objectView': 'proposed proof-time semantic agreement of stable reindexing and actual precomposition; not derived from point equality',
            'rawCompositionObjectView': 'separate direct proof-time view of the same reindex owner at raw composition endpoints; retains P,F,G and both base categories without runtime collapse',
            'rawMapView': 'proposed semantic presentation of Prof_reindex_transf by actual ambient constant-section prewhiskering; preserves arbitrary raw input and higher action',
            'precompInclusion': 'separate generic structural compatibility between included Cartesian and ambient fixed prewhiskering; independent full tapp1 check precedes the clause',
            'mapAgreement': 'full_bridge ends with the original required Prof map consumer; no Prof-specific comparison or inverse is supplied for its conclusion',
            'stagedMapAgreement': 'separate proof-time theorem composes independently typed inclusion/raw-owner comparisons through the actual ambient operation using eq_trans; no operational proof argument or new conversion rule',
            'canonicalAdmission': 'not postulated or derived in this replay',
            'seedDecision': 'co-Yoneda(Unit), lambda at that seed and evaluation at its reindex require explicit canonical-owner profile qualification',
            'presentationInverse': 'previous separate failed action obligation remains open',
        },
        'authoringInputs': {str(path.relative_to(root)): digest(path.read_bytes()) for path in authoring},
        'outputs': {name: digest(source.encode()) for name, source in targets.items()},
        'newControls': {name: {'positive': len(re.findall(r'(?m)^assert\b', text)),
                              'negative': len(re.findall(r'(?m)^assertnot\b', text))}
                        for name, text in fragments.items()},
    }
    return root, targets, source_inputs['lambdapi.pkg'], manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-authoring', action='store_true')
    args = parser.parse_args()
    root, targets, package, manifest = build()
    if args.check_authoring:
        print(json.dumps({'status': 'pins and authoring guards pass; Lambdapi not run',
                          'newControls': manifest['newControls']}, indent=2))
        return
    output = root / 'tmp/probes/admission_next'
    output.mkdir(parents=True, exist_ok=True)
    for name, source in targets.items():
        (output / name).write_text(source)
    (output / 'lambdapi.pkg').write_bytes(package)
    manifest['outputs']['lambdapi.pkg'] = digest(package)
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted existing-owner Cartesian reindex prerequisite; Lambdapi not run.')


if __name__ == '__main__':
    main()
