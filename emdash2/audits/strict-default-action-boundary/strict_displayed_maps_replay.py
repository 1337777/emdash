#!/usr/bin/env python3
"""Emit a strict-displayed-map / ambient-section classifier comparison.

NON-LIBRARY. Probe-only classifier names do not change public Functord or
declare that the coupled public migration has been completed.
"""
import hashlib
import json
from pathlib import Path
import runpy
import subprocess


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def through_semicolon(source, marker):
    assert source.count(marker) == 1, marker
    start = source.index(marker)
    return source[start:source.index(';', start)+1] + '\n'


def without_clause(source, marker):
    assert source.count(marker) == 1, marker
    start = source.index(marker)
    return source[:start]+source[source.index(';',start)+1:]


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    evidence = audit / 'conventional_gray_eval_verification.json'
    donor = json.loads(evidence.read_text())
    for name, expected in donor['authoringInputs'].items():
        assert sha(root / name) == expected, name
    runpy.run_path(str(audit / 'conventional_gray_eval_replay.py'), run_name='__main__')
    source = root / 'tmp/probes/conventional_gray_eval/candidate.lp'
    assert sha(source) == donor['outputs']['candidate.lp']
    body = source.read_text()
    pin = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
    core = subprocess.check_output(['git','show',pin+':emdash2/emdash3_2.lp'],cwd=root,text=True)
    profiles = subprocess.check_output(['git','show',pin+':emdash2/emdash3_2_gray_profiles.lp'],cwd=root,text=True)
    carriers = (through_semicolon(profiles, 'injective symbol StrictTransfor\n')
        + through_semicolon(profiles, 'injective symbol strict_transfor\n'))
    constant = through_semicolon(core, 'injective symbol Const_catd (K : Cat)')
    start = core.index('// Proof-time terminal-to-constant object comparison in the ordinary transfor')
    end = core.index('// Direct proof-time terminal-to-constant object comparison in the displayed', start)
    constant += core[start:end]
    constant += through_semicolon(core, 'rule @fapp0 $K Cat_cat (@Const_catd $K $A)')
    constant += through_semicolon(core, 'rule @fapp1_func $K Cat_cat (@Const_catd $K $A)')
    constant += through_semicolon(core, 'rule @fapp1_fapp0 $K Cat_cat (@Const_catd $K $A)')
    constant += through_semicolon(core, '// Constant-family section evaluation follows ordinary functor application.')
    files = ('strict_displayed_maps.lpfragment','strict_displayed_sections.lpfragment',
             'strict_displayed_maps_controls.lpfragment')
    parts = {name:(audit/name).read_text() for name in files}
    carrier_owner = '// Controlled Obj-inversion for transformation categories.'
    comparison_owner = '// Native one-leg controls.'
    assert 'injective symbol StrictTransfor\n' not in body
    for marker in (carrier_owner, comparison_owner):
        assert body.count(marker) == 1, marker
    body = body.replace(carrier_owner,carriers+'\n'+carrier_owner)
    out=root/'tmp/probes/strict_displayed_maps'; out.mkdir(parents=True,exist_ok=True)
    maps=parts[files[0]]; sections=parts[files[1]]
    strict_sections=sections.replace(
        '≔ @Transf_cat K Cat_cat (@Const_catd K Terminal_cat) E;',
        '≔ @sf_family_map_cat K (@Const_catd K Terminal_cat) E;').replace(
        '(@tapp0_fapp0 K Cat_cat (@Const_catd K Terminal_cat) E x s) Terminal_obj;',
        '(@tapp0_fapp0 K Cat_cat (@Const_catd K Terminal_cat) E x\n'
        '      (@sf_family_map_view K (@Const_catd K Terminal_cat) E s)) Terminal_obj;')
    assert strict_sections != sections
    reverse='''// Deliberately invalid automatic reverse admission.
unif_rule @StrictTransfor $K Cat_cat $E $D
  ≡ Obj (@Transf_cat $K Cat_cat $E $D) ↪ [ tt ≡ tt ];
'''
    without_map_action=maps
    for marker in ('rule @fapp0 _ _ (@sf_family_map_include',
                   'rule @fapp1_func _ _ (@sf_family_map_include',
                   'rule @fapp1_fapp0 _ _ (@sf_family_map_include'):
        without_map_action=without_clause(without_map_action,marker)
    variants={
        'candidate.lp':(maps,sections,''),
        'no_strict_naturality.lp':(without_clause(maps,'rule @comp_fapp0 Cat_cat _ _ _'),sections,''),
        'no_map_object_projection.lp':(without_clause(maps,'rule @fapp0 _ _ (@sf_family_map_include'),sections,''),
        'no_map_action.lp':(without_map_action,sections,''),
        'no_higher_projection.lp':(without_clause(maps,'rule @fapp1_fapp0 _ _ (@sf_family_map_include'),sections,''),
        'no_identity_view.lp':(without_clause(maps,'rule @strict_transfor $K Cat_cat $E $E'),sections,''),
        'no_constant_view.lp':(without_clause(maps,'rule @strict_transfor _ _ _ _ (@sf_constant_section'),sections,''),
        'wrong_reverse_admission.lp':(maps,sections,reverse),
        'strict_sections.lp':(maps,strict_sections,''),
    }
    outputs={}
    for name,(m,s,extra) in variants.items():
        candidate=body.replace(comparison_owner,constant+'\n'+m+'\n'+s+'\n'+comparison_owner)
        candidate+='\n'+extra+parts[files[2]]
        target=out/name;target.write_text(candidate);outputs[name]=sha(target)
    (out/'lambdapi.pkg').write_bytes((root/'lambdapi.pkg').read_bytes())
    authors=[Path(__file__)]+[audit/name for name in files]
    (out/'manifest.json').write_text(json.dumps({
        'status':'unqualified strict displayed-map classifier comparison',
        'donorEvidence':str(evidence.relative_to(root)),'donorEvidenceSha256':sha(evidence),
        'nativeDeclarationSourcePin':pin,
        'nativeCarrierExcerptSha256':hashlib.sha256(carriers.encode()).hexdigest(),
        'nativeConstantSectionExcerptSha256':hashlib.sha256(constant.encode()).hexdigest(),
        'authoringInputs':{str(p.relative_to(root)):sha(p) for p in authors},
        'outputs':outputs,
        'scope':['Probe-only classifiers; public Catd/Functord migration is not claimed.',
                 'Ambient Transf-based sections remain separate.',
                 'No runtime proof payload or automatic reverse inclusion.',
                 'No corrected Homd/Sigma or global consistency certificate.']
    },indent=2)+'\n')
    print('Emitted strict displayed-map / ambient-section classifier comparison.')


if __name__=='__main__':
    main()
