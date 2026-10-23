#!/usr/bin/env python3
"""Stage required upstream owners in a full copy of the pre-goal kernel.

This is an in-progress production migration, not another foundation model.
No original downstream section is truncated. Owner checks and consumer
migration determine qualification; successful emission does not.

Check imports with scripts/run_lambdapi.py --package-root pointing to the
emitted package. The outer probe wrapper checks the source but inventories
imports relative to the outer package, which is not this staged dependency
snapshot.
"""
import hashlib
import json
import difflib
from pathlib import Path
import re
import subprocess


PIN = 'f8af1fca472657ff1598c639eb29c0566e7b2ec0'
CORE_SHA = '6a980df34be718a23a6be121d170153650830a49f54b7e0eca415705ffb2068a'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def migrate_adjunction_family_view_reviewer(text):
    """Keep the original mate observations at their corrected diagram profiles."""
    marker = '// Existing associativity of whole transformations remains available.'
    assert text.count(marker) == 1
    prefix, tail = text.split(marker, 1)
    replacements = (
        (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', 154),
        (r'\(Op_cat C\)', '(TotalOp_cat C)', 9),
        (r'@one_cat_functor_category(?=\s+WalkingArrow_cat\s+C\s+C1\b)',
         '@one_cat_oplax_functor_category', 32),
        (r'@diagram_evaluation_at_func\b', '@diagram_oplax_evaluation_at_func', 20),
    )
    for pattern, replacement, count in replacements:
        prefix, actual = re.subn(pattern, replacement, prefix)
        assert actual == count, (pattern, actual)
    # The last shape-action comparisons start with an ordinary diagram
    # family. Its shape transformations are oplax; fixed evaluation stays
    # ordinary. Do not apply the zero-arrow replacements to these inputs.
    assert tail.count('assert (B I C : Cat)') == 1
    middle, shape = tail.split('assert (B I C : Cat)', 1)
    assert shape.count('Functor_cat B C') == 6
    assert shape.count('@Transf B C') == 2
    shape = shape.replace('Functor_cat B C', 'Functor_oplax_cat B C')
    shape = shape.replace('@Transf B C', '@Transf_oplax B C')
    starts = list(re.finditer(r'@comp_fapp0\s+\(Functor_oplax_cat B C\)', shape))
    assert len(starts) == 6
    edits = []
    for match in starts:
        cursor = match.end()
        for _ in range(3):
            while shape[cursor].isspace():
                cursor += 1
            start = cursor
            assert shape[start] == '('
            depth = 1
            cursor += 1
            while depth:
                depth += (shape[cursor] == '(') - (shape[cursor] == ')')
                cursor += 1
            atom = shape[start:cursor]
            assert atom.startswith(('(@diagram_family_at_func', '(@comp_cat_fapp0'))
            edits.append((start, cursor, '(@OddDual_func B C ' + atom + ')'))
    assert len(edits) == 18
    for start, end, replacement in reversed(edits):
        shape = shape[:start] + replacement + shape[end:]
    return (prefix + marker + middle
            + '// Ordinary diagram families have oplax shape action.\n'
            + '// Oplax mapping objects are the encoded OddDual_func views.\n\n'
            + 'assert (B I C : Cat)' + shape)


def ordinary_identity_observation_body(signature):
    """Derive the same whole identity claim from its actual native components."""
    def terms(expr):
        result, start, depth = [], 0, 0
        for i, char in enumerate(expr):
            depth += (char == '(') - (char == ')')
            if char.isspace() and depth == 0:
                if i > start:
                    result.append(expr[start:i])
                start = i + 1
        if start < len(expr):
            result.append(expr[start:])
        assert depth == 0
        return result
    formula = signature.split(': τ (@=', 1)[1].strip()
    assert formula.endswith(')')
    eqargs = terms(formula[:-1].strip())
    assert len(eqargs) == 3
    transfor, left, right = eqargs
    assert transfor.startswith('(@Transf ') and transfor.endswith(')')
    _, base, codomain, source, target = terms(transfor[1:-1])
    assert codomain == 'C' and source == target
    return f'''≔ let A : Cat ≔ {base} in
  let X : τ (Functor A C) ≔ {source} in
  let alpha : τ (@Transf A C X X) ≔ {left} in
  let beta : τ (@Transf A C X X) ≔ {right} in
  @hom_to_path (@Transf_cat A C X X) ((@one_cat_functor_category A C C1) X X)
    alpha beta (@one_cat_modification A C C1 X X alpha beta
      (λ a : τ (Obj A), @path_to_hom (Hom_cat C (fapp0 X a) (fapp0 X a))
        (@tapp0_fapp0 A C X X a alpha) (@tapp0_fapp0 A C X X a beta)
        (@eq_refl (Hom C (fapp0 X a) (fapp0 X a)) (@tapp0_fapp0 A C X X a beta))));'''


def migrate_homology_boundary_paths(text):
    """Retain the two original square bodies and adapt only their path observers."""
    def terms(expression):
        result, start, depth = [], None, 0
        for i, char in enumerate(expression):
            if start is None:
                if char.isspace():
                    continue
                start = i
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            if depth == 0 and char.isspace():
                result.append(expression[start:i])
                start = None
        assert depth == 0
        if start is not None:
            result.append(expression[start:])
        return result

    squares = {}
    for direction in ('to', 'from'):
        name = 'homology_family_comparison_boundary_diagram_' + direction
        pattern = r'protected symbol ' + name + r'\b.*?;'
        match = re.search(pattern, text, re.S)
        assert match is not None
        block = match.group()
        signature, body = block[:-1].rsplit('≔ ', 1)
        args = terms(body)
        assert args[:5] == ['@one_cat_family_oplax_exchange_map', 'WalkingArrow_cat', 'B', 'C', 'C1']
        assert len(args) == 8
        raw_source, raw_target, square = args[5:]
        assert square.startswith('(@one_cat_square_diagram_transf')
        square_name = 'homology_family_comparison_boundary_square_' + direction
        parameters, _ = signature.split('\n : τ', 1)
        helper = parameters.replace(name, square_name, 1)
        helper += '\n : τ (@Transf WalkingArrow_cat (Functor_cat B C)\n  ' + raw_source + '\n  ' + raw_target + ')\n≔ ' + square + ';\n\n'
        selected = '(@' + square_name + ' B C C1 t T A D h S P)'
        replacement = ('// Retained original square, shared by its whole image and path observations.\n'
                       + helper + signature + '≔ ' + ' '.join(args[:7] + [selected]) + ';')
        text = text[:match.start()] + replacement + text[match.end():]
        squares[direction] = (raw_source, raw_target)

    marker = '(@one_cat_oplax_family_evaluation_comp_path'
    count = 0
    while marker in text:
        start = text.index(marker)
        end, depth = start, 0
        while end < len(text):
            if text[end] == '(':
                depth += 1
            elif text[end] == ')':
                depth -= 1
                if depth == 0:
                    break
            end += 1
        args = terms(text[start + 1:end])
        assert len(args) == 11
        assert args[1:5] == ['B', 'WalkingArrow_cat', 'C', 'C1']
        a, g, f = args[5], args[9], args[10]
        gd = 'from' if g.startswith('(@homology_family_comparison_boundary_diagram_from') else 'to'
        fd = 'from' if f.startswith('(@homology_family_comparison_boundary_diagram_from') else 'to'
        assert g.startswith('(@homology_family_comparison_boundary_diagram_' + gd)
        assert f.startswith('(@homology_family_comparison_boundary_diagram_' + fd)
        assert re.sub(r'\s+', '', squares[fd][1]) == re.sub(r'\s+', '', squares[gd][0])
        raw_g = g.replace('boundary_diagram_' + gd, 'boundary_square_' + gd, 1)
        raw_f = f.replace('boundary_diagram_' + fd, 'boundary_square_' + fd, 1)
        replacement = ('(@one_cat_oplax_exchange_comp_at_path WalkingArrow_cat B C C1 ' + a + '\n'
                       + '\n'.join((squares[fd][0], squares[fd][1], squares[gd][1], raw_g, raw_f)) + ')')
        text = text[:start] + replacement + text[end + 1:]
        count += 1
    assert count == 4
    # Reflect the original two square maps before applying exchange. This
    # uses the existing ordinary diagram theorem and the same four inverse
    # paths; it does not introduce a general oplax reflection contract.
    def declaration(name):
        match = re.search(r'protected symbol ' + name + r'\b.*?;', text, re.S)
        assert match is not None
        return match

    def bracketed(expression, marker):
        start = expression.index(marker)
        depth = 0
        for end in range(start, len(expression)):
            if expression[end] == '(':
                depth += 1
            elif expression[end] == ')':
                depth -= 1
                if depth == 0:
                    return expression[start:end + 1]
        raise AssertionError('unclosed original inverse path')

    paths = {}
    for side in ('left', 'right'):
        for endpoint in ('source', 'target'):
            old = declaration('homology_family_comparison_diagram_' + side + '_' + endpoint + '_law').group()
            head = 'omega_equiv_along_left_law' if side == 'left' else 'omega_equiv_left_as_right_law'
            paths[side, endpoint] = bracketed(old, '(@' + head)
    original = declaration('homology_family_comparison_boundary_square_to').group()
    telescope = original.split('\n : τ', 1)[0]
    raw_name = 'homology_family_comparison_boundary_square_evidence'
    mapped_name = 'homology_family_comparison_mapped_boundary_evidence'
    params = 'B C C1 t T A D h S P'
    raw_source, raw_target = squares['to']
    U = '(@homology_family_comparison_boundary_square_to ' + params + ')'
    V = '(@homology_family_comparison_boundary_square_from ' + params + ')'
    raw_category = '(Functor_cat WalkingArrow_cat (Functor_cat B C))'
    target_category = '(Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))'
    left = ('(@one_cat_diagram_map_path (Functor_cat B C) (@one_cat_functor_category B C C1)\n'
            + raw_source + '\n' + raw_source + '\n'
            + '(@comp_fapp0 ' + raw_category + ' ' + raw_source + ' ' + raw_target + ' ' + raw_source + ' ' + V + ' ' + U + ')\n'
            + '(@id ' + raw_category + ' ' + raw_source + ')\n'
            + paths['left', 'source'] + '\n' + paths['left', 'target'] + ')')
    right = ('(@one_cat_diagram_map_path (Functor_cat B C) (@one_cat_functor_category B C C1)\n'
             + raw_target + '\n' + raw_target + '\n'
             + '(@comp_fapp0 ' + raw_category + ' ' + raw_target + ' ' + raw_source + ' ' + raw_target + ' ' + U + ' ' + V + ')\n'
             + '(@id ' + raw_category + ' ' + raw_target + ')\n'
             + paths['right', 'source'] + '\n' + paths['right', 'target'] + ')')
    addition = '\n// The original square maps and inverse paths, reflected in their ordinary source.\n'
    addition += telescope.replace('homology_family_comparison_boundary_square_to', raw_name, 1)
    addition += '\n : τ (IsoEvidence ' + raw_category + ' ' + raw_source + ' ' + raw_target + ')\n'
    addition += '≔ @iso_evidence_intro ' + raw_category + ' ' + raw_source + ' ' + raw_target + '\n' + U + '\n' + V + '\n' + left + '\n' + right + ';\n\n'
    addition += '// Apply the existing whole strict exchange to that retained evidence.\n'
    addition += telescope.replace('homology_family_comparison_boundary_square_to', mapped_name, 1)
    addition += '\n : τ (IsoEvidence ' + target_category + '\n'
    addition += '(@diagram_family_shape_func WalkingArrow_cat B C ' + raw_source + ')\n'
    addition += '(@diagram_family_shape_func WalkingArrow_cat B C ' + raw_target + '))\n'
    addition += '≔ @one_cat_iso_evidence_fmap ' + raw_category + ' ' + target_category + '\n'
    addition += '(@one_cat_functor_category B (Functor_oplax_cat WalkingArrow_cat C) (@one_cat_oplax_functor_category WalkingArrow_cat C C1))\n'
    addition += '(@one_cat_family_oplax_exchange_func WalkingArrow_cat B C C1)\n' + raw_source + '\n' + raw_target + '\n(@' + raw_name + ' ' + params + ');\n'
    owner = declaration('homology_family_comparison_boundary_diagram_from')
    text = text[:owner.end()] + '\n' + addition + text[owner.end():]
    for side in ('left', 'right'):
        owner = declaration('homology_family_comparison_diagram_' + side + '_law')
        signature = owner.group().rsplit('≔ ', 1)[0]
        body = '≔ @iso_evidence_' + side + ' ' + target_category + ' _ _\n(@' + mapped_name + ' ' + params + ');'
        text = text[:owner.start()] + signature + body + text[owner.end():]

    return text


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    original = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2.lp'], cwd=root, text=True)
    profiles = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2_gray_profiles.lp'], cwd=root, text=True)
    original_profiles = profiles
    assert sha(original) == CORE_SHA
    body = original
    inputs = {}
    changes = []
    from production_diagram_observation_migration import migrate_diagram_observation
    diagram_migration_source = audit / 'production_diagram_observation_migration.py'
    inputs[str(diagram_migration_source.relative_to(root))] = sha(diagram_migration_source.read_text())
    from production_selected_presentation_migration import (
        SOURCE_SHA256 as SELECTED_PRESENTATION_SOURCES,
        migrate_selected_presentation, finish_selected_core, finish_selected_diagram,
        finish_selected_family_views, finish_selected_homology_comparison,
        finish_selected_prewhisker_check,
        finish_selected_arrow_diagram,
        finish_selected_adjunction_reviewer,
    )
    from production_selected_record_view_migration import (
        SOURCES as SELECTED_RECORD_VIEW_SOURCES, migrate_selected_record_view,
    )
    from production_kernel_boundary_prerequisite_migration import (
        SOURCES as KERNEL_BOUNDARY_PREREQUISITE_SOURCES,
        migrate_kernel_boundary_prerequisite,
    )
    from production_kernel_additive_prerequisite_migration import (
        SOURCES as KERNEL_ADDITIVE_PREREQUISITE_SOURCES,
        migrate_kernel_additive_prerequisite,
    )
    from production_connecting_kernel_chain_migration import (
        SOURCES as CONNECTING_KERNEL_CHAIN_SOURCES,
        migrate_connecting_kernel_chain,
    )
    from production_native_connecting_consumer_migration import (
        SOURCES as NATIVE_CONNECTING_CONSUMER_SOURCES,
        migrate_native_connecting_consumer,
    )
    for name in ('production_native_connecting_consumer_migration.py',
                 'production_native_connecting_consumers_review.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    for name in ('production_connecting_kernel_chain_migration.py',
                 'production_connecting_kernel_chain_review.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    for name in ('production_kernel_additive_prerequisite_migration.py',
                 'production_kernel_additive_prerequisites_review.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    for name in ('production_kernel_boundary_prerequisite_migration.py',
                 'production_kernel_boundary_prerequisites_review.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    for name in ('production_selected_record_view_migration.py',
                 'production_selected_record_views_review.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    for name in ('production_selected_presentation_migration.py',
                 'production_selected_kernel_metadata.lpfragment',
                 'production_selected_cokernel_metadata.lpfragment',
                 'production_selected_projection_naturality.lpfragment',
                 'production_odd_dual_ordinary_profile.lpfragment',
                 'production_composition_metadata_congruence.lpfragment',
                 'production_odd_dual_adjunction_cuts.lpfragment',
                 'production_oplax_exchange_adjunction_cuts.lpfragment',
                 'production_prewhisker_projection_rules.lpfragment',
                 'production_prewhisker_action_composition.lpfragment',
                 'production_prewhisker_metadata_congruence.lpfragment',
                 'production_precomposition_composite_view.lpfragment',
                 'production_stable_prewhisker_reindex.lpfragment',
                 'production_odd_dual_precomposition.lpfragment',
                 'production_walking_point_precomposition.lpfragment',
                 'production_selected_identity_controls.lpfragment',
                 'production_selected_presentation_complete_regression.lpfragment',
                 'production_selected_presentation_reviewer_suffix.lpfragment',
                 'production_selected_presentation_controls.lpfragment',
                 'production_selected_presentation_regression.lpfragment',
                 'production_selected_presentation_core_regression.lpfragment',
                 'production_selected_presentation_library_regression.lpfragment',
                 'production_selected_presentation_residual_regression.lpfragment',
                 'production_action_remaining_core_regression.lpfragment',
                 'production_action_remaining_library_regression.lpfragment',
                 'production_simplex_dependency_residual_regression.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_simplex_dependency_migration import migrate_simplex_dependency
    for name in ('production_simplex_dependency_migration.py',
                 'production_triangle_family_action.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_zero_arrow_input_migration import migrate_zero_arrow_input, share_arrow_cart_owner
    zero_arrow_migration_source = audit / 'production_zero_arrow_input_migration.py'
    inputs[str(zero_arrow_migration_source.relative_to(root))] = sha(zero_arrow_migration_source.read_text())
    zero_arrow_reviewer_source = audit / 'production_zero_arrow_frame_reviewer.lpfragment'
    inputs[str(zero_arrow_reviewer_source.relative_to(root))] = sha(zero_arrow_reviewer_source.read_text())
    from production_introduced_input_migration import migrate_introduced_input
    for name in ('production_introduced_input_migration.py', 'production_introduced_input_reflection.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_freyd_entry_migration import finish_freyd_entry
    for name in ('production_freyd_entry_migration.py', 'production_one_cat_oplax_reflection.lpfragment',
                 'production_native_chain_pair_maps.lpfragment', 'production_hom_action_factorization_views.lpfragment',
                 'production_one_cat_family_naturality_paths.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_terminal_family_migration import finish_terminal_family
    for name in ('production_terminal_family_migration.py', 'production_oplax_family_reflection.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_cokernel_input_continuation import finish_cokernel_inputs
    for name in ('production_cokernel_input_continuation.py',
                 'production_native_reconstruction_map_views.lpfragment',
                 'production_native_reconstruction_endpoint_paths.lpfragment',
                 'production_cokernel_family_inputs.lpfragment',
                 'production_cokernel_family_inputs_reviewer.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_kernel_cokernel_path_migration import finish_kernel_cokernel_paths
    for name in ('production_kernel_cokernel_path_migration.py',
                 'production_component_view_congruence.lpfragment',
                 'production_kernel_cokernel_family_paths.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_cokernel_reconstruction_migration import finish_cokernel_reconstruction
    for name in ('production_cokernel_reconstruction_migration.py',
                 'production_application_classifier_congruence.lpfragment',
                 'production_cokernel_projection_paths.lpfragment',
                 'production_cokernel_reconstruction.lpfragment',
                 'production_cokernel_reconstruction_reviewer.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_native_row_laws_migration import finish_native_row_laws
    for name in ('production_native_row_laws_migration.py',
                 'production_prepost_composite_comparison.lpfragment',
                 'production_complete_outer_post_comparison.lpfragment',
                 'production_zero_family_paths.lpfragment',
                 'production_short_exact_families.lpfragment',
                 'production_kernel_family_restriction_paths.lpfragment',
                 'production_short_exact_families_reviewer.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_kernel_reconstruction_migration import finish_kernel_reconstruction
    for name in ('production_kernel_reconstruction_migration.py',
                 'production_kernel_projection_paths.lpfragment',
                 'production_kernel_family_inputs.lpfragment',
                 'production_kernel_family_lift.lpfragment',
                 'production_kernel_precomposition.lpfragment',
                 'production_kernel_reconstruction.lpfragment',
                 'production_kernel_lift_reviewer.lpfragment',
                 'production_kernel_precomposition_reviewer.lpfragment',
                 'production_kernel_reconstruction_reviewer.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_row_observations_migration import finish_row_observations
    for name in ('production_row_observations_migration.py',
                 'production_row_cancellation.lpfragment',
                 'production_zero_cone_rows.lpfragment',
                 'production_row_cancellation_reviewer.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_constant_row_migration import finish_constant_rows
    for name in ('production_constant_row_migration.py',
                 'production_constant_transformation_views.lpfragment',
                 'production_constant_transformation_reviewer.lpfragment',
                 'production_freyd_row_paths.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_constant_chain_migration import finish_constant_chain
    for name in ('production_constant_chain_migration.py',
                 'production_constant_chain_zeros.lpfragment',
                 'production_constant_chain_reviewer.lpfragment',
                 'production_freyd_row_zeros.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_kernel_columns_migration import finish_kernel_columns, SOURCES as KERNEL_COLUMNS
    for name in ('production_kernel_columns_migration.py',
                 *(fragment for _, fragment in KERNEL_COLUMNS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_native_column_entry_migration import finish_native_column_entry, SOURCES as NATIVE_COLUMN_ENTRY
    for name in ('production_native_column_entry_migration.py',
                 *(fragment for _, fragment in NATIVE_COLUMN_ENTRY.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_column_projection_migration import finish_column_projection, SOURCES as COLUMN_PROJECTION
    for name in ('production_column_projection_migration.py',
                 *(fragment for _, fragment in COLUMN_PROJECTION.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_family_actions_migration import finish_family_actions, SOURCES as FAMILY_ACTIONS
    for name in ('production_family_actions_migration.py',
                 *(fragment for _, fragment in FAMILY_ACTIONS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_column_homology_paths_migration import finish_column_homology_paths
    path = audit / 'production_column_homology_paths_migration.py'
    inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_homology_records_migration import finish_homology_records
    for name in ('production_homology_records_migration.py',
                 'production_zero_diagram_record_inputs.lpfragment'):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_factor_h_reviewers_migration import finish_factor_h_reviewers
    path = audit / 'production_factor_h_reviewers_migration.py'
    inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_diagram_mate_reviewers_migration import finish_diagram_mate_reviewers, SOURCES as DIAGRAM_MATE_REVIEWERS
    for name in ('production_diagram_mate_reviewers_migration.py',
                 *(spec['fragment'] for spec in DIAGRAM_MATE_REVIEWERS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_adjunction_reviewers_migration import finish_adjunction_reviewers, SOURCES as ADJUNCTION_REVIEWERS
    for name in ('production_adjunction_reviewers_migration.py',
                 *(spec['fragment'] for spec in ADJUNCTION_REVIEWERS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_ordinary_reviewers_migration import finish_ordinary_reviewers, SOURCES as ORDINARY_REVIEWERS
    for name in ('production_ordinary_reviewers_migration.py',
                 *(spec['fragment'] for spec in ORDINARY_REVIEWERS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())
    from production_action_controls_migration import finish_action_controls, add_default_vertical_comparison, SOURCES as ACTION_CONTROLS
    for name in ('production_action_controls_migration.py', 'production_default_vertical_clause.lpfragment',
                 *(spec['fragment'] for spec in ACTION_CONTROLS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())

    from production_precomp_telescope_migration import finish_precomp_telescope_reviewers, add_ordinary_telescope_identities, SOURCES as PRECOMP_TELESCOPE_REVIEWERS
    for name in ('production_precomp_telescope_migration.py', 'production_precomp_telescope_identity.lpfragment',
                 *(spec['fragment'] for spec in PRECOMP_TELESCOPE_REVIEWERS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())

    from production_action_remaining_migration import finish_remaining_action_reviewers, SOURCES as REMAINING_ACTION_REVIEWERS
    for name in ('production_action_remaining_migration.py', 'production_encoded_evaluation_comparison.lpfragment',
                 *(spec['fragment'] for spec in REMAINING_ACTION_REVIEWERS.values())):
        path = audit / name
        inputs[str(path.relative_to(root))] = sha(path.read_text())

    def fragment(name):
        path = audit / name
        text = path.read_text()
        inputs[str(path.relative_to(root))] = sha(text)
        return text

    def insert(marker, text, reason):
        nonlocal body
        assert body.count(marker) == 1, marker
        body = body.replace(marker, text + '\n' + marker, 1)
        changes.append({'anchor': marker, 'reason': reason,
                        'insertedSha256': sha(text)})

    def replace_once(old, new, owner, reason):
        nonlocal body
        assert body.count(old) == 1, owner
        body = body.replace(old, new, 1)
        changes.append({'owner': owner, 'reason': reason,
                        'oldSha256': sha(old), 'newSha256': sha(new)})

    capped_action_type = '''symbol fapp1_fapp0 : Π [A B : Cat], Π (F_AB : τ (Functor A B)),
  Π [X_A Y_A : τ (Obj A)],
  Π (f : τ (Hom A X_A Y_A)),
  τ (Hom B (fapp0 F_AB X_A) (fapp0 F_AB Y_A));'''
    replace_once(capped_action_type, '''// The result uses the whole action's canonical Hom category, so opposite
// endpoints compute before Hom-alias inversion. Keep the input classifier
// for domain inference when object-level duality erases carrier information.
symbol fapp1_fapp0 : Π [A B : Cat], Π (F_AB : τ (Functor A B)),
  Π [X_A Y_A : τ (Obj A)],
  Π (f : τ (Hom A X_A Y_A)),
  τ (Obj (Hom_cat B (fapp0 F_AB X_A) (fapp0 F_AB Y_A)));''',
        'capped functor action canonical Hom types',
        'Definitionally align the capped result with fapp0 of the whole Hom functor while retaining the input classifier for dual-domain inference; no new operation or computation rule')

    precomposition_raw_view = '''// Proof-time identity-family comparison with ordinary raw composition.
unif_rule @hom_precomp_along_fapp0 $A $A (@id Cat_cat $A) $Z $W $X $h $g
  ≡ @comp_fapp0
      $A
      _
      _
      $Z
      $g
      $h
  ↪ [ tt ≡ tt ];'''
    replace_once(precomposition_raw_view,
                 precomposition_raw_view + '\n' + fragment('production_precomposition_association.lpfragment'),
                 'Cat-valued composite-input precomposition reading',
                 'Retain the original generic comparison and all displayed owners; compare the complete Cat composite only for a literal composite input')

    insert('// Primitive join-recursion beta for the internally natural cross cell.',
           fragment('production_join_recursion_view.lpfragment'),
           'Expose sufficient constructor congruence so proof-time endpoint comparisons are available under a join introduction, retaining the cross datum')

    admission_marker = '// Transparent typed carrier comparison.\nsymbol make_strict_transfor_carrier_path'
    assert profiles.count(admission_marker) == 1
    admission_views = fragment('production_strict_admission_views.lpfragment')
    profiles = profiles.replace(admission_marker, admission_views + '\n' + admission_marker, 1)
    changes.append({'source': 'emdash3_2_gray_profiles.lp',
                    'owner': 'strict-transfor admission of Cartesian identity/composition',
                    'reason': 'The actual classified inverse laws require admission to agree with existing Cartesian constructors while retaining each ordinary operand',
                    'insertedSha256': sha(admission_views)})

    insert('/*\n  The former capped composition cut and detached all-components law are\n',
           fragment('composition_rule.lpfragment'), 'Strict default: existing capped functor action owner')
    precomposition_actions = fragment('production_cat_precomposition_actions.lpfragment')
    insert('// Hom-action functoriality for precomposition. The composition orientation is',
           precomposition_actions + '\n'
           + '// The same projection ladder for the selected Cartesian coefficient.\n'
           + '// Cat_cart and public Cat_cat share functor objects; their higher maps differ.\n'
           + precomposition_actions.replace('Cat_cat', 'Cat_cart'),
           'Cat-valued precomposition evaluator at both actual coefficient universes: preserve the whole owner and its object/whole-Hom/capped projections, without a whole semantic fold')
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           fragment('whole_rules.lpfragment') + '\n' + fragment('projected_rules.lpfragment')
           + '\n' + fragment('conventional_lax_projection_readings.lpfragment')
           + '\n' + fragment('production_conventional_pre_reading.lpfragment')
           + '\n' + fragment('conventional_lax_rules.lpfragment'),
           'Strict functor action and conventional-lax pre/right action at the existing whole/projection owners')
    replace_once('''rule @hom_postcomp_fapp0
      $A $A (@id Cat_cat $A) $W $Y $Z $q
      (@hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $W $X $Y $p $g)
  ↪ @hom_postcomp_fapp0
      $A $A (@id Cat_cat $A) $W $X $Z
      (@comp_fapp0 $A $X $Y $Z $q $p)
      $g;
''', fragment('production_postcomposition_inverse.lpfragment'),
                 'identity-family postcomposition on a composite',
                 'Keep consecutive represented cuts visible so the existing computational-inverse rules survive composition; reverse only this capped equation, retaining its whole functor owner')
    replace_once('''with @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $X $X $Y $f (@id $A $X) ↪ $f;''',
                 '''// The identity's inferred category may reduce through a duality first.
with @hom_postcomp_fapp0 $A $A (@id Cat_cat $A) $X $X $Y $f (@id _ $X) ↪ $f;''',
                 'identity input of represented postcomposition',
                 'Let the typed represented owner determine the identity category after duality normalization; do not discriminate on the erased category annotation')
    precomp_identity = '''rule @hom_precomp_along_fapp0
      $A
      $B
      $F
      _
      $W
      $X
      $h
      (@id $B _)
  ↪ @fapp1_fapp0 $A $B $F $W $X $h;'''
    replace_once(precomp_identity,
                 '// The identity category can normalize through duality before this cut.\n'
                 + precomp_identity.replace('(@id $B _)', '(@id _ _)'),
                 'identity input of represented precomposition',
                 'The typed precomposition owner determines the identity endpoints; allow its inferred category annotation to normalize through total duality')
    insert('// Path categories internalize HoTT equality as a groupoidal category.',
           fragment('co_above2_category.lpfragment') + '\n' + fragment('co_at2_category.lpfragment'),
           'Corrected duality: required category-level R, O and dimension-two action')
    above = fragment('co_above2_functor.lpfragment')
    cart_dualities = above[above.index('// Whole action on Cartesian mapping categories.'):]
    cart_dualities = (cart_dualities.replace('TotalOp_func_func', 'TotalOp_cart_func_func')
                     .replace('total_op', 'total_op_cart').replace('Cat_cat', 'Cat_cart'))
    above = above[:above.index('// Whole action on Cartesian mapping categories.')]
    at = fragment('co_at2_functor.lpfragment')
    public_total = fragment('conventional_total_op_mapping.lpfragment')
    public_total = public_total[:public_total.index('// Whole formation for any strict family')]
    insert('// Terminal category and points-as-functors are needed to derive unary homs from',
           above + '\n' + at + '\n' + cart_dualities + '\n' + public_total,
           'Corrected whole dualities: Cartesian transpose and total reversal, plus the distinct public conventional-lax total reversal')
    insert('// Point object as a functor from the terminal category.',
           fragment('production_terminal_composite_view.lpfragment'),
           'Whole terminal-source composite comparison retaining both functors and the stable runtime composition; no terminal-source eta rewrite')

    profile = fragment('cartesian_profile.lpfragment')
    early = profile[profile.index('injective symbol sf_cart_functor_cat'):profile.index('// Only the object classifier')]
    start = profile.index('constant symbol sf_cart_cat')
    early += profile[start:profile.index('// One whole inclusion', start)]
    early += '''
// Whole inclusion of the selected coefficient; category/functor objects agree.
injective symbol Cat_cart_include : τ (Functor Cat_cart Cat_cat);
rule fapp0 Cat_cart_include $A ↪ $A;
rule @fapp1_fapp0 _ _ Cat_cart_include _ _ $F ↪ $F;
rule @id Cat_cart $A ↪ @id Cat_cat $A;
// lhs-audit: keep 1 -- only composition inside the Cartesian coefficient.
rule @comp_fapp0 Cat_cart $A $B $C $G $F
  ↪ @comp_fapp0 Cat_cat $A $B $C $G $F;
'''
    names = {'sf_cart_functor_cat': 'Functor_cart_cat', 'sf_cart_cat': 'Cat_cart',
             'sf_cart_functor_include': 'Functor_cart_include'}

    def public(text):
        for old, new in names.items():
            text = text.replace(old, new)
        return text

    insert('/*\n  Internal path-category action.',
           '// Cartesian coefficient required by the selected Homd family type.\n' + public(early),
           'Homd coefficient: share strict functor objects while retaining public lax Hom(Cat)')

    carriers = ''
    relocated = []
    for marker in ('injective symbol StrictTransfor\n', 'injective symbol strict_transfor\n'):
        assert profiles.count(marker) == 1
        a = profiles.index(marker)
        b = profiles.index(';', a) + 1
        declaration = profiles[a:b]
        carriers += declaration + '\n\n'
        relocated.append({'symbol': marker.strip(), 'declarationSha256': sha(declaration)})
        profiles = profiles[:a] + '// Carrier/view relocated to the core owner.\n' + profiles[b:]
    post_start = '// Whole post/left strict naturality guarded by the evidence-bearing view.'
    post_end = '// Whole pre/right strict naturality guarded by the same full profile.'
    assert profiles.count(post_start) == profiles.count(post_end) == 1
    a, b = profiles.index(post_start), profiles.index(post_end)
    strict_post = profiles[a:b]
    profiles = profiles[:a] + '// Core-independent strict post action is owned by the nucleus.\n\n' + profiles[b:]
    insert('/*\n  The former whole post/left and pre/right strict-functoriality accumulation\n',
           strict_post + '''
// Identity specialization after the strict component has already projected.
rule @comp_fapp0 $B _ _ _
      (@fapp1_fapp0 $A $B $G $x $y $p)
      (@tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $U))
  ↪ @tapp1_fapp0 $A $B $F $G $x $y (@strict_transfor $A $B $F $G $U) $p;
''', 'Move existing strict-transfor post computation to the core Cartesian consumer; retain the later admission/property machinery')
    relocated.append({'owner': 'strict-transfor ordinary post action', 'bodySha256': sha(strict_post)})
    profile_tail = '// Profile-guarded whole target/right reading.'
    assert profiles.count(profile_tail) == 1
    begin = profiles.index(profile_tail)
    old = profiles[begin:]
    replacement = fragment('production_profile_readings.lpfragment')
    profiles = profiles[:begin] + replacement
    changes.append({'source': 'emdash3_2_gray_profiles.lp',
                    'owner': 'strict_functord_transport_rhs_tele_path / strict_functord_transport_rhs_path',
                    'reason': 'Use the admitted Cartesian family coefficient and derive the existing compatibility paths from the default pre/right comparison; retire its two redundant profile-only unifiers',
                    'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
    late = profile[profile.index('// Only the object classifier'):profile.index('// The corresponding strict coefficient universe')]
    start = profile.index('// One whole inclusion')
    late += profile[start:profile.index('// A Cartesian evaluator', start)]
    late += '''
// The whole first Hom of coefficient inclusion retains the strict profile.
rule @fapp1_func _ _ Cat_cart_include $A $B
  ↪ Functor_cart_include $A $B;

// Existing ordinary transfor observations of canonical Cartesian Hom action.
rule @strict_transfor _ _ _ _
      (@hom_postcomp_tele_fapp1_fapp0 $A $B $F $W $X $Y $f $g $alpha)
  ↪ @hom_postcomp_tele_transf $A $B $F $W $X $Y $f $g $alpha;
rule @strict_transfor _ _ _ _
      (@hom_precomp_along_tele_fapp1_fapp0 $A $B $F $Z $W $X $h $k $alpha)
  ↪ @hom_precomp_along_tele_transf $A $B $F $Z $W $X $h $k $alpha;

// Defined ordinary diagram views of the same canonical whole Hom packages.
// These admit general lax internal-action components without changing Hom.
symbol hom_int_view [A B : Cat] (F : τ (Functor B A))
  : τ (Functor (Op_cat A) (Catd_cat B))
≔ @comp_cat_fapp0 (Op_cat A) (Functor_cart_cat B Cat_cart)
    (Catd_cat B) (Functor_cart_include B Cat_cart) (@hom_int A B F);
symbol hom_con_int_view [A B : Cat] (F : τ (Functor B A))
  : τ (Functor A (Catd_cat (Op_cat B)))
≔ @comp_cat_fapp0 A (Functor_cart_cat (Op_cat B) Cat_cart)
    (Catd_cat (Op_cat B)) (Functor_cart_include (Op_cat B) Cat_cart)
    (@hom_con_int A B F);
'''
    insert('// Controlled Obj-inversion for transformation categories.',
           carriers, 'Relocate the existing strict-transfor carriers unchanged')
    hom_owner = 'rule Hom_cat (Functor_cat _ _) $F $G ↪ Transf_cat $F $G;'
    assert body.count(hom_owner) == 1
    body = body.replace(hom_owner, hom_owner + '\n\n' + public(late), 1)
    changes.append({'after': hom_owner,
                    'reason': 'Cartesian inclusion uses the original ordinary next-Hom projection',
                    'insertedSha256': sha(public(late))})

    replace_once('rule Obj (@Catd_cat $K)\n  ↪ Obj (Functor_cat $K Cat_cat);',
                 'rule Obj (@Catd_cat $K)\n  ↪ Obj (Functor_cat $K Cat_cart);',
                 'Catd_cat object classifier',
                 'Selected admitted families land in the Cartesian coefficient; Functord remains lax across the base')
    replace_once("unif_rule Functor_cat $K Cat_cat ≡ @Catd_cat $K'",
                 "unif_rule Functor_cat $K Cat_cart ≡ @Catd_cat $K'",
                 'Catd_cat whole classifier comparison',
                 'Match the selected coefficient at the existing displayed facade')
    a = body.index('// Internalized-x prerequisite: directed-family category formation as a')
    b = body.index('// Internalized pointwise opposite on directed families.', a)
    old_classifier = body[a:b]
    replace_once(old_classifier,
                 '// Varying-base family formation is defined after its canonical Hom owner.\n\n',
                 'Catd_cat_func / Catd_catd_con relocation',
                 'The whole Cartesian parameter family is derived from Hom(Cat_cart), not a lift of lax diagram categories')
    relocated.append({'symbols': ['Catd_cat_func', 'Catd_catd_con'],
                      'originalBlockSha256': sha(old_classifier),
                      'reason': 'Dependency-forced semantic definition after canonical Hom'})

    # Canonical Hom actions of strict categories have the Cartesian profile.
    # Keep every original covariant/contravariant owner and change its mapping
    # classifiers together, rather than introducing a parallel action API.
    section_start = '// 4. Ordinary internal hom and hom actions'
    section_end = '// 5. Ordinary binary products of categories'
    assert body.count(section_start) == body.count(section_end) == 1
    a, b = body.index(section_start), body.index(section_end)
    old_hom = body[a:b]
    new_hom = old_hom.replace('Functor_cat', 'Functor_cart_cat')
    new_hom = new_hom.replace(': τ (Functor B Cat_cat);', ': τ (Functor B Cat_cart);')
    new_hom = new_hom.replace(': τ (Functor (Op_cat B) Cat_cat);',
                              ': τ (Functor (Op_cat B) Cat_cart);')
    new_hom = re.sub(r'Cat_cat(\s+\(@hom_(?:con\b|\s))', r'Cat_cart\1', new_hom)
    for owner in ('hom_postcomp_tele', 'hom_precomp_along_tele'):
        marker = 'symbol ' + owner + '_transf '
        assert new_hom.count(marker) == 1
        start = new_hom.index(marker)
        end = new_hom.index(';', start) + 1
        ordinary_view = new_hom[start:end].replace('Functor_cart_cat', 'Functor_cat')
        new_hom = new_hom[:start] + ordinary_view + new_hom[end:]
        new_hom = new_hom.replace('↪ @' + owner + '_transf ',
                                   '↪ @' + owner + '_fapp1_fapp0 ')
    for old, new in (
            ('(Catd_cat B)', '(Functor_cart_cat B Cat_cart)'),
            ('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)'),
            ('(@Catd_cat $B)', '(Functor_cart_cat $B Cat_cart)'),
            ('(@Catd_cat (Op_cat B))', '(Functor_cart_cat (Op_cat B) Cat_cart)'),
            ('(Catd_cat (Op_cat B))', '(Functor_cart_cat (Op_cat B) Cat_cart)')):
        new_hom = new_hom.replace(old, new)
    replace_once(old_hom, new_hom, 'ordinary Hom owner block',
                 'Selected whole Cartesian Hom profile with the original public names and blended strict F argument')
    insert('// Applying the telescope at p yields the capped represented-object action.',
           '''// Unit after the canonical Hom source action has projected to its
// stable head. This is the identity law of the same strict Hom functor.
rule @hom_int_precomp_func $A $B $F $X $X (@id _ $X)
  ↪ @id (Functor_cart_cat $B Cat_cart) (@hom_ $A $B $F $X);
''', 'The actual Homd target-map identity consumes the stable native Hom projection')
    insert(section_end, fragment('production_family_classifier.lpfragment'),
           'Define the original varying-base family names by the actual Cartesian Hom owner')
    a = body.index('symbol Hom_tele_func ')
    b = body.index(';', a) + 1
    old_two_endpoint = body[a:b]
    replace_once(old_two_endpoint, old_two_endpoint.replace('Functor_cat', 'Functor_cart_cat'),
                 'Hom_tele_func',
                 'The original two-endpoint Hom action has the same Cartesian higher mapping profile as its curried observations')
    a = body.index('unif_rule @Hom_tele_func ')
    b = body.index(';', a) + 1
    old_factorization = body[a:b]
    assert old_factorization.count('Functor_cat') == 2
    new_factorization = old_factorization.replace('Functor_cat', 'Functor_cart_cat')
    new_factorization, count = re.subn(r'(@comp_prod_func\s+)Cat_cat', r'\1Cat_cart', new_factorization)
    assert count == 1
    replace_once(old_factorization, new_factorization,
                 'Existing two-endpoint Hom factorization comparison',
                 'Migrate the original comparison with its whole owner to Cartesian mapping categories; retain every endpoint and both represented actions')

    facade_start = '// Proof-time comparison only: ordinary Cat-valued transfors and displayed'
    facade_end = '// Product-valued transfors project componentwise.'
    assert body.count(facade_start) == body.count(facade_end) == 1
    a, b = body.index(facade_start), body.index(facade_end)
    old_facade = body[a:b]
    new_facade = re.sub(r'(\$K\s+)Cat_cat', r'\1Cat_cart', old_facade)
    replace_once(old_facade, new_facade, 'Functord and Transfd facade projections',
                 'Default lax transformations between the newly admitted Cartesian-coefficient families')
    insert('// Readable second Path action: a function equality induces a path-valued',
           fragment('production_cartesian_product_views.lpfragment'),
           'Join the Cartesian product-Hom classifier and expose the existing inclusion componentwise, preserving its whole strict head for naturality')

    observation_start = '// Component of a postcomposition-telescope action.'
    assert body.count(observation_start) == 1
    a = body.index(observation_start)
    old_observations = body[a:]
    new_observations = old_observations
    for owner in ('hom_postcomp_tele', 'hom_precomp_along_tele'):
        rule_start = 'rule @' + owner + '_fapp1_fapp0\n'
        assert new_observations.count(rule_start) == 1, owner
        start = new_observations.index(rule_start)
        end = new_observations.index(';', start) + 1
        old_rule = new_observations[start:end]
        new_observations = (new_observations[:start]
            + '// The former raw-to-ordinary telescope fold is replaced by\n'
              '// the Cartesian inclusion projection at the classifier owner.\n'
            + new_observations[end:])
        changes.append({'owner': owner + '_fapp1_fapp0 Cat specialization',
                        'reason': 'A Cartesian Hom arrow is not an ambient transfor until inclusion; the existing ordinary observation head is retained',
                        'retiredRuleSha256': sha(old_rule)})
        new_observations = new_observations.replace('@' + owner + '_fapp1_fapp0',
                                                    '@' + owner + '_transf')
    replace_once(old_observations, new_observations, 'ordinary observations of canonical Hom transfors',
                 'Retain existing tapp observations through their original ordinary-view heads after canonical action acquires the Cartesian profile')
    # The old raw capped action and its ordinary view had different tapp0
    # clauses. Identifying their observation heads must not retain competing
    # runtime results. Keep the original ordinary-view computation once.
    a = body.index('// Component of a postcomposition-telescope action.')
    b = body.index('// Reflexive theorem exposing the selected component formula', a)
    c = body.index('// Component of tele-postcomposition in an arbitrary ambient category.')
    d = body.index(';', c) + 1
    component_rule = body[c:d]
    assert body[a:b].count('rule @tapp0_fapp0') == component_rule.count('rule @tapp0_fapp0') == 1
    replace_once(component_rule,
                 '// The telescope component is computed once at its earlier projection owner.\n',
                 'Duplicate postcomposition component owner',
                 'Retire the duplicate created by redirecting the two old observation heads to the same ambient head')
    replace_once(body[a:b],
                 '// Component of a postcomposition-telescope action uses the original\n'
                 '// horizontal composition owner with its first argument fixed. The alternative\n'
                 '// stable precomposition reading below is proof-time, via its existing comparison.\n'
                 + component_rule[component_rule.index('rule @tapp0_fapp0'):] + '\n\n',
                 'Canonical postcomposition component computation',
                 'Preserve the original ordinary-view runtime computation without a new projection or comparison rule')
    a = body.index('symbol hom_postcomp_tele_tapp0_component_eq')
    b = body.index('≔ eq_refl', a)
    c = body.index(';', b) + 1
    replace_once(body[b:c], '''≔ eq_sym
    (@hom_precomp_along_fapp1_comp_prod_path
      A A (@id_func A) (@fapp0 B A F Y) W (@fapp0 B A F X) u
      (@fapp1_fapp0 B A F X Y f)
      (@fapp1_fapp0 B A F X Y g)
      (@fapp1_fapp0
        (Hom_cat B X Y)
        (Hom_cat A (@fapp0 B A F X) (@fapp0 B A F Y))
        (@fapp1_func B A F X Y) f g alpha));''',
                 'Existing precomposition component theorem',
                 'Derive the unchanged theorem from its existing typed comparison, avoiding fresh implicit product-classifier inference')
    replace_once('''rule @tapp0_fapp0 $K Cat_cat _ _ $Y (@id (@Catd_cat $K) $E)
  ↪ @id Cat_cat (@fapp0 $K Cat_cat $E $Y);''',
                 '''rule @tapp0_fapp0 $K Cat_cart _ _ $Y (@id (@Catd_cat $K) $E)
  ↪ @id Cat_cart (@fapp0 $K Cat_cart $E $Y);''',
                 'displayed identity component',
                 'The original displayed identity now has Cartesian-coefficient components')

    a = body.index('// 6b. Internalized hom endpoint actions and rigid two-sided projections')
    b = body.index('// Product-valued off-diagonal components project componentwise.', a)
    old_root_views = body[a:b]
    new_root_views = old_root_views
    replacements = []
    for match in re.finditer(r'(?m)^rule\b', old_root_views):
        end = old_root_views.index(';', match.start()) + 1
        old_rule = old_root_views[match.start():end]
        lhs, rhs = old_rule.split('↪', 1)
        if not any(name in lhs for name in ('@hom_int_precomp_func ', '@hom_con_int_postcomp_func ', '@hom_int $')):
            continue
        lhs = lhs.replace('Cat_cat', 'Cat_cart')
        lhs = re.sub(r'(\(@hom_(?:int_precomp|con_int_postcomp)_func[^\n)]+\))',
                     r'(@strict_transfor _ _ _ _ \1)', lhs)
        generic = '''(@fapp1_fapp0 (Op_cat $A) (@Catd_cat $B)
        (@hom_int $A $B $F) $Y $X $f)'''
        if generic in lhs:
            lhs = lhs.replace(generic, '''(@strict_transfor _ _ _ _
        (@fapp1_fapp0 (Op_cat $A) (Functor_cart_cat $B Cat_cart)
          (@hom_int $A $B $F) $Y $X $f))''')
        replacements.append((old_rule, lhs + '↪' + rhs.replace('Functor_cat', 'Functor_cart_cat')))
    assert len(replacements) == 7, len(replacements)
    for old, new in replacements:
        assert new_root_views.count(old) == 1
        new_root_views = new_root_views.replace(old, new, 1)
    replace_once(old_root_views, new_root_views, 'ordinary component observations of whole Hom',
                 'Project canonical Cartesian family maps through the existing strict-transfor inclusion before ordinary tapp observations')

    # The two-parameter Cartesian packages have Cartesian parameter Homs.
    # Fixed ordinary whiskering above still acts on general lax transfors.
    for variance, args, parameter, left, right, first, second in (
            ('cov', 'X Y Z', '(Functor_cart_cat Y Z)', '(Functor_cart_cat X Y)', '(Functor_cart_cat X Z)', 'G', 'H'),
            ('con', 'Z X Y', '(Functor_cart_cat X Y)', '(Functor_cart_cat Y Z)', '(Functor_cart_cat X Z)', 'F', 'K')):
        generic = 'hom_postcomp_tele' if variance == 'cov' else 'hom_precomp_along_tele'
        base = 'comp_cat_' + variance + '_func_func'
        start = body.index('symbol ' + base + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {base} [X Y Z : Cat]
  : τ (Functor {parameter} (Functor_cart_cat {left} {right}))
≔ @{generic}_func Cat_cart Cat_cart (@id_func Cat_cart) {args};''',
                     base + ' Cartesian profile',
                     'A parameterized Cartesian composition package must not silently make arbitrary lax squares commute')
        fixed = 'comp_cat_' + variance + '_cart_func'
        low = f'(@{fixed} X Y Z {first})'
        high = f'(@{fixed} X Y Z {second})'
        # Express the endpoints through the already-declared generic owner;
        # fixed Cart aliases are introduced later with closure, not forward references.
        if variance == 'cov':
            low = f'(@hom_postcomp_func Cat_cart Cat_cart (@id_func Cat_cart) X Y Z {first})'
            high = f'(@hom_postcomp_func Cat_cart Cat_cart (@id_func Cat_cart) X Y Z {second})'
            binders = '[G H : τ (Functor Y Z)]'
        else:
            low = f'(@hom_precomp_along_func Cat_cart Cat_cart (@id_func Cat_cart) Z X Y {first})'
            high = f'(@hom_precomp_along_func Cat_cart Cat_cart (@id_func Cat_cart) Z X Y {second})'
            binders = '[F K : τ (Functor X Y)]'
        owner = base + '_fapp1_func'
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {owner} [X Y Z : Cat] {binders}
  : τ (Functor (Hom_cat {parameter} {first} {second})
      (Hom_cat (Functor_cart_cat {left} {right}) {low} {high}))
≔ @{generic}_fapp1_func Cat_cart Cat_cart (@id_func Cat_cart) {args} {first} {second};''',
                     owner + ' Cartesian profile', 'The whole first Hom retains the actual Cartesian parameter profile')
        owner = base + '_transf'
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        replace_once(body[start:end], f'''symbol {owner} [X Y Z : Cat] {binders}
  (eta : τ (Hom {parameter} {first} {second}))
  : τ (Transf {low} {high})
≔ @{generic}_transf Cat_cart Cat_cart (@id_func Cat_cart) {args} {first} {second} eta;''',
                     owner + ' ordinary view', 'Observe the Cartesian parameter action as an ordinary transfor, without admitting a raw parameter')

    replace_once('constant symbol op : τ (Functor Cat_cat Cat_cat);',
                 'constant symbol op : τ (Functor (CoAt2_cat Cat_cart) Cat_cart);',
                 'op', 'Dimension-one transpose is whole on the Cartesian coefficient, with the required dimension-two shift')
    replace_once('rule @fapp0 Cat_cat Cat_cat op $A ↪ Op_cat $A;',
                 'rule @fapp0 (CoAt2_cat Cat_cart) Cat_cart op $A ↪ Op_cat $A;',
                 'op object action', 'Same category-level transpose with its corrected coefficient source')
    replace_once('rule @fapp1_fapp0 Cat_cat Cat_cat op $A $B $F ↪ @Op_func $A $B $F;',
                 '''rule @fapp1_func (CoAt2_cat Cat_cart) Cat_cart op $A $B
  ↪ Op_func_func $A $B;
rule @fapp1_fapp0 (CoAt2_cat Cat_cart) Cat_cart op $A $B $F ↪ @Op_func $A $B $F;''',
                 'op whole first Hom', 'Use the actual Cartesian mapping-category action, not a same-profile map on arbitrary lax transformations')
    replace_once('injective symbol Op_catd_func (Z : Cat) : τ (Functor (Catd_cat Z) (Catd_cat Z));',
                 '''injective symbol Op_catd_func (Z : Cat)
  : τ (Functor (CoAt2_cat (Functor_cart_cat Z Cat_cart))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cart));''',
                 'Op_catd_func', 'The shifted-family operator acts on Cartesian diagram maps; ordinary FF is not silently admitted')
    replace_once('''rule @hom_postcomp_func Cat_cat Cat_cat (@id Cat_cat Cat_cat) $Z Cat_cat Cat_cat op
  ↪ @Op_catd_func $Z;''', '''// Formation of the shifted family uses the original postcomposition owner.
rule @comp_fapp0 Cat_cat _ _ _
      (@hom_postcomp_func Cat_cart Cat_cart (@id Cat_cat Cat_cart)
        (CoAt2_cat $K) (CoAt2_cat Cat_cart) Cat_cart op)
      (CoAt2_func_func $K Cat_cart)
  ↪ Op_catd_func $K;''',
                 'Op_catd_func formation', 'Preserve the semantic composite of dimension-two functor action and coefficient postcomposition')

    a = body.index('injective symbol Op_transf\n')
    b = body.index('// 6b. Internalized hom endpoint actions', a)
    old_transpose = body[a:b]
    old_decl_end = old_transpose.index(';') + 1
    new_transpose = '''injective symbol Op_transf
  [A B : Cat] [F G : τ (Functor A B)]
  (eta : τ (Hom (Functor_cart_cat A B) F G))
  : τ (Hom (Functor_cart_cat (Op_cat A) (Op_cat B))
      (@Op_func A B G) (@Op_func A B F));

// First arrow projection of the whole Cartesian transpose.
rule @fapp1_fapp0 _ _ (Op_func_func $A $B) $G $F $eta
  ↪ @Op_transf $A $B $F $G $eta;
''' + old_transpose[old_decl_end:].replace('Functor_cat', 'Functor_cart_cat')
    new_transpose = new_transpose.replace('''      (@Op_transf $A $B $F $G $eta)
  ↪ @tapp0_fapp0 $A $B $F $G $x $eta;''', '''      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta))
  ↪ @tapp0_fapp0 $A $B $F $G $x (@strict_transfor $A $B $F $G $eta);''')
    replace_once(old_transpose, new_transpose, 'Op_transf Cartesian mapping action',
                 'Dimension-one transpose of strict transfors is the Cartesian whole-map projection; the public lax total-opposite operation is distinct')
    replace_once('''rule @tapp1_func
      _ _
      _ _
      $x $y
      (@Op_transf $A $B $F $G $eta)
  ↪ @tapp1_func $A $B $F $G $y $x $eta;''',
                 '''rule @tapp1_func
      _ _
      _ _
      $x $y
      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta))
  ↪ @tapp1_func $A $B $F $G $y $x (@strict_transfor $A $B $F $G $eta);''',
                 'Op_transf whole ordinary observation',
                 'Observe the Cartesian transpose through the existing inclusion, retaining its ordinary action')
    replace_once('''rule @tapp1_fapp0 _ _ _ _ $x $y
      (@Op_transf $A $B $F $G $eta) $p
  ↪ @tapp1_fapp0 $A $B $F $G $y $x $eta $p;''',
                 '''rule @tapp1_fapp0 _ _ _ _ $x $y
      (@strict_transfor _ _ _ _ (@Op_transf $A $B $F $G $eta)) $p
  ↪ @tapp1_fapp0 $A $B $F $G $y $x (@strict_transfor $A $B $F $G $eta) $p;''',
                 'Op_transf capped ordinary observation',
                 'The same Cartesian-profile correction after capping')
    insert("// Point component of Path_cat_func's second action.",
           fragment('conventional_total_op_transfors.lpfragment') + '\n'
           + fragment('conventional_total_op_offdiagonal.lpfragment'),
           'Retain the qualified total reversal of arbitrary conventional-lax transfors and its correct post-boundary off-diagonal action')

    insert('// Canonical off-diagonal equality action for h : f = g.',
           fragment('production_path_cartesian.lpfragment'),
           'Cartesian Path realization retains the original path-map objects and derives its whole higher action through the existing equality-core inclusion')

    for owner, old_type, new_type in (
            ('Product_cat_fapp1_func', '(Functord_cat\n', '(@Transf_cat Cat_cat Cat_cat\n'),
            ('Product_cat_fapp1_fapp0_functord', '(Functord\n', '(@Transf Cat_cat Cat_cat\n')):
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        old = body[start:end]
        assert old.count(old_type) == 1, owner
        replace_once(old, old.replace(old_type, new_type), owner,
                     'This original product-constructor parameter action is an ordinary public-Cat transformation, not a map between admitted Cartesian families')
    start = body.index('symbol Product_mapL_func_func ')
    end = body.index(';', start) + 1
    old = body[start:end]
    replace_once(old, old.replace('(@Functord_cat Cat_cat\n', '(@Transf_cat Cat_cat Cat_cat\n'),
                 'Product_mapL_func_func',
                 'Keep the same component-evaluation composition through the corrected ordinary product-constructor transformation classifier')

    a = body.index('/*\n  Opposite adjunction.')
    b = body.index('// 7e. Internal ordinary hom-action packages', a)
    old_adjunction = body[a:b]
    new_adjunction = (old_adjunction.replace('Op_cat', 'TotalOp_cat')
                      .replace('@Op_func', '@TotalOp_func')
                      .replace('Op_transf', 'TotalOp_transf'))
    new_adjunction = new_adjunction.replace('  Opposite adjunction.',
        '  Total-opposite adjunction (legacy public spelling Op_adjunction).')
    # TotalOp_cat is now a reducible alias. The inner Op_adjunction already
    # determines these inferred category/functor arguments; matching the alias
    # here breaks the canonical involution and unit/counit projections.
    old_adjunction_slots = '      (TotalOp_cat $B) (TotalOp_cat $A)\n      _\n      _\n'
    assert new_adjunction.count(old_adjunction_slots) == 3
    new_adjunction = new_adjunction.replace(old_adjunction_slots, '      _ _ _ _\n')
    replace_once(old_adjunction, new_adjunction, 'Op_adjunction',
                 'Preserve general lax unit/counit transformations by using the qualified total-duality profile; do not silently require strict units')

    a = body.index('// 7e. Internal ordinary hom-action packages')
    b = body.index('// 8. Directed Cat-valued family constructors', a)
    old_internal = body[a:b]
    new_internal = re.sub(r'@hom_int\b', '@hom_int_view', old_internal)
    # Fixed-source/target components still land in the admitted coefficient.
    new_internal = re.sub(r'(\$A\s+)Cat_cat', r'\1Cat_cart', new_internal)
    new_internal = new_internal.replace('_ Cat_cat _ _', '_ Cat_cart _ _')
    for owner, varying in (('tapp1_con_int_fapp0_transf', 'G'), ('fapp1_con_int_transf', 'F')):
        start = new_internal.index('injective symbol ' + owner + '\n')
        begin = new_internal.index('  : τ (Transf\n', start)
        end = new_internal.index(';', begin) + 1
        new_internal = new_internal[:begin] + f'''  : τ (Transf
      (@hom_con_int_view A A (@id_func A))
      (@comp_cat_fapp0 A B (@Catd_cat (Op_cat A))
        (@hom_con_int_view B A F) {varying}));''' + new_internal[end:]
    for owner in ('tapp1_con_int_fapp0_transf', 'tapp1_con_at_transf'):
        pattern = (r'(?m)^unif_rule\n  @tapp1_(?:int_fapp0_transf|at_transf)\n'
                   r'[\s\S]*?≡ @' + owner + r'[\s\S]*?\];')
        matches = list(re.finditer(pattern, new_internal))
        assert len(matches) == 1, owner
        old = matches[0][0]
        new = old.replace('$epsilon2\n', '(@strict_transfor $A $B $F $G $U)\n')
        new = new.replace('$epsilon2 $Y\n', '(@strict_transfor $A $B $F $G $U) $Y\n')
        new = new.replace('(@Op_transf $A $B $F $G $epsilon2)',
                          '''(@strict_transfor (Op_cat $A) (Op_cat $B)
      (@Op_func $A $B $G) (@Op_func $A $B $F) (@Op_transf $A $B $F $G $U))''')
        assert '$epsilon2' not in new, owner
        new_internal = new_internal.replace(old, new, 1)
    replace_once(old_internal, new_internal, 'ordinary internal-action ladders',
                 'Keep general lax epsilon through ordinary whole-Hom inclusion views and direct contravariant roots; use transpose comparisons only for actual Cartesian inputs')
    insert('// 7f. Target-internalized ordinary hom-action mirror',
           fragment('production_internal_x_profile.lpfragment'),
           'Canonical strict-x refinement of the pre/right-normal internal action, retaining its whole ordinary view and lax inner y-action')

    insert('// Product homs compute componentwise.',
           '''// Cartesian mapping categories preserve target products.
rule Functor_cart_cat $X (Product_cat $A $B)
  ↪ Product_cat (Functor_cart_cat $X $A) (Functor_cart_cat $X $B);
''', 'The existing paired-functor computation also applies to the Cartesian mapping profile')
    insert('// Generic projections of an arbitrary object of a Sigma total.',
           '''// Sufficient object-carrier congruence for the same Sigma constructor.
// Obj is not injective: this only compares the actual bases and whole families
// to propagate an already justified proof-time endpoint comparison.
unif_rule Obj (@Sigma_cat $K $E) ≡ Obj (@Sigma_cat $K0 $E0)
  ↪ [ $K0 ≡ $K; $E0 ≡ $E ];
''', 'Propagate proved family comparisons through the Sigma object facade without making Obj injective')
    start = body.index('symbol Product_pair_tele_func ')
    end = body.index(';', start) + 1
    old_pair = body[start:end]
    replace_once(old_pair, old_pair.replace('Functor_cat', 'Functor_cart_cat'),
                 'Product_pair_tele_func', 'Canonical pairing has strict naturality in its retained argument')
    insert('// Object projection ladder for the internalized product constructor.',
           '''// Cartesian parameter view of the original product constructor.
injective symbol Product_cat_cart_func
  : τ (Functor Cat_cat (Functor_cart_cat Cat_cat Cat_cat));
rule fapp0 Product_cat_cart_func $A ↪ Product_cat_fapp0_func $A;
// lhs-audit: keep 1 -- ordinary composition with the Cartesian mapping inclusion.
rule @comp_fapp0 Cat_cat _ _ _
      (Functor_cart_include Cat_cat Cat_cat) Product_cat_cart_func
  ↪ Product_cat_func;
''', 'Retain the original product constructor and partial actions while providing its required Cartesian parameter profile')
    insert('// 7b. Evaluation and fixed-object evaluation',
           fragment('production_cartesian_closure.lpfragment'),
           'Cartesian closure consumes canonical strict whiskering and product parameter actions')
    a = body.index('// 7b. Evaluation and fixed-object evaluation')
    b = body.index('// 7c. Ordinary curry and uncurry', a)
    old_eval = body[a:b]
    new_eval = old_eval.replace('Functor_cat', 'Functor_cart_cat')
    old_eval_point = 'rule fapp0 (@Eval_func $A $B) (Struct_sigma $F $x)\n  ↪ fapp0 $F $x;'
    assert new_eval.count(old_eval_point) == 1
    new_eval = new_eval.replace(old_eval_point,
        '// Evaluate the actual pair projections even when the argument is neutral.\n'
        '// This is local to Eval, not a global product/Sigma eta rule.\n'
        'rule fapp0 (@Eval_func $A $B) $z\n'
        '  ↪ @fapp0 $A $B (sigma_Fst $z) (sigma_Snd $z);')
    new_eval = new_eval.replace('(Transf_cat F G)', '(Hom_cat (Functor_cart_cat A B) F G)')
    new_eval = new_eval.replace('(@Transf_cat $A $B $F $G)',
                                '(Hom_cat (Functor_cart_cat $A $B) $F $G)')
    assert new_eval.count('↪ tapp1_fapp0 $eta $p;') == 2
    new_eval = new_eval.replace('↪ tapp1_fapp0 $eta $p;',
                               '↪ tapp1_fapp0 (@strict_transfor $A $B $F $G $eta) $p;')
    assert new_eval.count('↪ fapp0_func $x;') == 1
    new_eval = new_eval.replace('↪ fapp0_func $x;', '''↪ @comp_cat_fapp0
      (Functor_cart_cat $A $B) (Functor_cat $A $B) $B
      (@fapp0_func $A $B $x) (Functor_cart_include $A $B);''')
    replace_once(old_eval, new_eval, 'Cartesian evaluation ladder',
                 'Joint strict Cartesian evaluation accepts strict transfors; fixed ordinary evaluation remains available through inclusion')
    for owner in ('curry_func_func', 'curry_func', 'uncurry_func_func', 'uncurry_func'):
        start = body.index('symbol ' + owner + ' ')
        end = body.index(';', start) + 1
        old = body[start:end]
        new = old.replace('Functor_cat', 'Functor_cart_cat')
        new = re.sub(r'@comp_cat_(cov|con)_func\b', r'@comp_cat_\1_cart_func', new)
        new = new.replace('@Product_mapL_func_func', '@Product_mapL_cart_func_func')
        replace_once(old, new, owner,
                     'Keep the original Cartesian curry/uncurry composition body with its actual mapping profiles')
    product_uncurry = '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_func'
    count = body.count(product_uncurry)
    assert count > 0
    body = body.replace(product_uncurry,
                        '@uncurry_func Cat_cat Cat_cat Cat_cat Product_cat_cart_func')
    changes.append({'owner': 'existing uncurried product-formation consumers',
                    'reason': 'Use the canonical Cartesian parameter view required by the corrected uncurry signature',
                    'count': count})

    a = body.index('// 8a. Fibre notation, pullback, and base-arrow transport')
    b = body.index('// 8b. Constant, terminal, opposite, and displayed composition', a)
    old_fibres = body[a:b]
    new_fibres = re.sub(r'((?:\$?[ABK])\s+)Cat_cat', r'\1Cat_cart', old_fibres)
    new_fibres = new_fibres.replace('@fapp0 _ Cat_cat (@Pullback_catd',
                                    '@fapp0 _ Cat_cart (@Pullback_catd')
    new_fibres = new_fibres.replace('id Cat_cat Cat_cat) Cat_cat $A $B $F',
                                    'id Cat_cat Cat_cat) Cat_cart $A $B $F')
    new_fibres = new_fibres.replace('(@fapp0_func Cat_cat Cat_cat Cat_cat)',
                                    '(@fapp0_func Cat_cat Cat_cat Cat_cart)')
    # Retain the still-valid public-Cat projected strict action as well.
    start = old_fibres.index('rule fapp0\n')
    end = old_fibres.index(';', start) + 1
    public_transport = old_fibres[start:end]
    cart_transport = re.sub(r'((?:\$?[ABK])\s+)Cat_cat', r'\1Cat_cart', public_transport)
    assert new_fibres.count(cart_transport) == 1
    new_fibres = new_fibres.replace(cart_transport, cart_transport + '\n\n'
        + '// The same valid strict-functor point action in the public universe.\n' + public_transport, 1)
    new_fibres = new_fibres.replace('''      (@Pullback_catd_func $B $D $G)
      (@hom_int $C $D $H)''', '''      (@hom_precomp_along_func Cat_cart Cat_cart (@id Cat_cat Cat_cart)
        Cat_cart $B $D $G)
      (@hom_int $C $D $H)''')
    replace_once(old_fibres, new_fibres, 'family fibres, transport and pullback',
                 'Apply the selected coefficient to actual family observations; retain ordinary raw-Cat action and the canonical whole Cartesian Hom reindexing')
    a = body.index('// Arrow action of the internalized Catd constructor. `Catd_cat_func` is a')
    b = body.index('// Pointwise projection for the hom-action of family pullback.', a)
    replace_once(body[a:b],
                 '// The Cartesian varying-base constructor computes through hom_con;\n'
                 '// fixed lax-family pullback retains its separate existing owner.\n\n',
                 'Catd_cat_func legacy raw action fold',
                 'Do not equate Cartesian parameter reindexing with the larger lax diagram-map functor')
    insert('// The Cartesian varying-base constructor computes through hom_con;',
           '''// Direct proof-time reading of represented-family reindexing.
// The semantic comp/Pullback comparison and Pullback(hom_) accumulation
// already express this law; the checker does not chain those comparisons.
unif_rule @comp_fapp0 Cat_cat $K $C Cat_cart
      (@hom_ $C $C (@id Cat_cat $C) $w) $F
  ≡ @hom_ $C0 $K0 $F0 $w0
  ↪ [ $C ≡ $C0; $K ≡ $K0; $F ≡ $F0; $w ≡ $w0 ];
''', 'The actual Homd target index consumes both existing represented-family reindexing presentations')

    a = body.index('// 8b. Constant, terminal, opposite, and displayed composition')
    b = body.index('// Fixed-base layer: pointwise opposite of a directed family.', a)
    old_constants = body[a:b]
    new_constants = re.sub(r'(\$[ABK]\s+)Cat_cat', r'\1Cat_cart', old_constants)
    new_constants = new_constants.replace('(Functor_cat $A $A)', '(Functor_cart_cat $A $A)')
    replace_once(old_constants, new_constants, 'constant and terminal admitted families',
                 'Keep the existing object/transport computations with the Cartesian coefficient; constant Pi still uses default lax transformations')
    a = body.index('// Fixed-base layer: pointwise opposite of a directed family.')
    b = body.index('// Pointwise projection of displayed composition.', a)
    replace_once(body[a:b], fragment('production_cartesian_family_duality.lpfragment') + '\n',
                 'Op_catd and Op_funcd',
                 'The original family transpose uses the shifted base and Cartesian map profile; general lax FF is retained for the separate Homd-relative construction')

    a = body.index('// Pointwise projection of displayed composition.')
    b = body.index('// Fixed-base fibrewise-product structural owners.', a)
    old = body[a:b]
    new = re.sub(r'(\$K\s+)Cat_cat', r'\1Cat_cart', old)
    new = new.replace('↪ @comp_fapp0\n      Cat_cat', '↪ @comp_fapp0\n      Cat_cart')
    replace_once(old, new,
                 'displayed composition components',
                 'Vertical composition remains the original componentwise operation in the admitted coefficient')

    whole = fragment('conventional_total_op_whole_action.lpfragment')
    whole_rules = whole[whole.index('rule @fapp1_func'):].rstrip()
    assert body.count(whole_rules) == 1
    body = body.replace(whole_rules,
        '// Generic whole identity/composition action moved to the earlier composition owner.\n', 1)
    insert('// Ordinary category identity cuts: g ∘ id ↪ g and id ∘ f ↪ f.',
           whole, 'Relocate the unchanged original whole first-Hom action before the derived duality/family consumers')
    for projection in ('fapp0', 'fapp1_fapp0', 'fapp1_func'):
        original_lhs = f'rule @{projection} $A $C (@comp_fapp0 Cat_cat $A $B $C $F $G)'
        replace_once(original_lhs,
            '// The typed composite supplies its own source and target; caller\n'
            '// annotations may be a proof-time category facade.\n'
            + original_lhs.replace(f'@{projection} $A $C', f'@{projection} _ _', 1),
            projection + ' composite inferred annotations',
            'The ordinary Yoneda view is applied through Psh_cat rather than the literal Catd_cat target; recover inferred annotations from the visible composite')
    insert('/*\n   Typed equality view of the generic strict identity cut.',
           fragment('conventional_total_op_source_units.lpfragment') + '''
// The shifted family source likewise loses its dimension-two identity tag.
// lhs-audit: keep 1 -- CoAt2 is the erased-identity source discriminator.
rule @fapp1_fapp0 (CoAt2_cat $K) $D $F $x $x (@id $K $x)
  ↪ @id $D (@fapp0 (CoAt2_cat $K) $D $F $x);
''', 'Strict identity observations after duality has erased the original source tag')

    a = body.index('// Fixed-base fibrewise-product structural owners.')
    b = body.index('// 8c. Section categories and Pi action', a)
    old_products = body[a:b]
    new_products = old_products.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat')
    new_products = new_products.replace('Product_cat_cart_func', 'Product_cat_coeff_func')
    new_products = re.sub(r'@comp_cat_(cov|con)_func\b', r'@comp_cat_\1_cart_func', new_products)
    replace_once(old_products, fragment('production_cartesian_product.lpfragment') + '\n' + new_products,
                 'fibrewise products',
                 'Retain the original uncurry/product/pair construction and displayed owners with the admitted coefficient and its actual Cartesian fibre Homs')

    insert('// Semantic uncurry package through fixed-right product action and evaluation.',
           fragment('production_lax_curry.lpfragment'),
           'One-way lax currying for the original raw ProfMap consumer; object action reuses Cartesian curry and inclusion, without claiming an ambient Cartesian inverse')

    a = body.index('// 8c. Section categories and Pi action')
    b = body.index('// 8d. Fibre covariance and dependent-hom endpoint notation', a)
    old_sections = body[a:b]
    new_sections = old_sections.replace("@Transf_cat $K' Cat_cat", "@Transf_cat $K' Cat_cart")
    new_sections = new_sections.replace('(Op_cat Cat_cat)', '(Op_cat Cat_cart)')
    new_sections = new_sections.replace('//   Pi_int_funcd[K] = Pi_func(K)',
        '//   Pi_int_funcd[K] = Pi_func(K) after the Cartesian-diagram inclusion')
    new_sections = new_sections.replace('// The base is Op(Cat) because section categories pull back contravariantly\n// along functors.',
        '// The base is T(Cat_cart). The parameter fibres use Cartesian diagram\n'
        '// maps; their inclusion retains the existing lax section operation.')
    new_sections = new_sections.replace('// Base component of internal Pi: Pi_int_funcd[K] ↪ Pi_func(K).',
        '// Base component: restrict the existing Pi along its actual diagram inclusion.')
    new_sections = new_sections.replace('//   for G : K ⊢ Cat^op,',
        '//   for G : K ⊢ T(Cat_cart),')
    new_sections = new_sections.replace('//   Pi_pullback_funcd(G)[x] = Pi_func(G[x])',
        '//   Pi_pullback_funcd(G)[x] = Pi_func(G[x]) after Cartesian-diagram inclusion')
    new_sections = new_sections.replace('// Pointwise projection: Pi_pullback_funcd(G)[x] ↪ Pi_func(G[x]).',
        '// Component after base pullback, retaining the same inclusion before Pi.')
    new_sections = new_sections.replace('''      (Op_cat Cat_cart)
      Cat_cat
      _
      _
      $K
      Pi_int_funcd
  ↪ @Pi_func $K;''', '''      (Op_cat Cat_cart)
      Cat_cart
      _
      _
      $K
      Pi_int_funcd
  ↪ @comp_cat_fapp0 (Functor_cart_cat $K Cat_cart) (Catd_cat $K) Cat_cat
      (@Pi_func $K) (Functor_cart_include $K Cat_cart);''')
    new_sections = new_sections.replace('''      $K
      Cat_cat
      _
      _
      $x
      (@Pi_pullback_funcd $K $G)
  ↪ @Pi_func (@fapp0 $K (Op_cat Cat_cart) $G $x);''', '''      $K
      Cat_cart
      _
      _
      $x
      (@Pi_pullback_funcd $K $G)
  ↪ @comp_cat_fapp0
      (Functor_cart_cat (@fapp0 $K (Op_cat Cat_cart) $G $x) Cat_cart)
      (Catd_cat (@fapp0 $K (Op_cat Cat_cart) $G $x)) Cat_cat
      (@Pi_func (@fapp0 $K (Op_cat Cat_cart) $G $x))
      (Functor_cart_include (@fapp0 $K (Op_cat Cat_cart) $G $x) Cat_cart);''')
    new_sections = new_sections.replace('''≔ comp_cat_fapp0
     (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
     (@tapp0_func K Cat_cat (@Const_catd K Terminal_cat) E k);''', '''≔ @comp_cat_fapp0 (Pi_cat E)
    (Functor_cart_cat Terminal_cat (Fibre_cat E k)) (Fibre_cat E k)
    (@comp_cat_fapp0
      (Functor_cart_cat Terminal_cat (Fibre_cat E k))
      (Functor_cat Terminal_cat (Fibre_cat E k)) (Fibre_cat E k)
      (@fapp0_func Terminal_cat (Fibre_cat E k) Terminal_obj)
      (Functor_cart_include Terminal_cat (Fibre_cat E k)))
    (@tapp0_func K Cat_cart (@Const_catd K Terminal_cat) E k);''')
    # Pi is the terminal-source Hom of Catd(K), so its canonical formation
    # has the same Cartesian target as represented Hom. Its input maps and
    # section objects remain the ordinary lax displayed ones.
    new_sections = new_sections.replace('Cat_cat', 'Cat_cart')
    new_sections = new_sections.replace('injective symbol Pi_func (K : Cat)',
        '// The terminal-source Hom profile changes the formation target,\n'
        '// not the existing lax section or displayed-map classifiers.\n'
        'injective symbol Pi_func (K : Cat)')
    replace_once(old_sections, new_sections, 'Pi and varying-base section interface',
                 'Retain lax sections and fixed-base maps; use the canonical represented-Hom formation target and the existing Cartesian parameter inclusion')

    a = body.index('// 8d. Fibre covariance and dependent-hom endpoint notation')
    b = body.index('// 9. Directed Sigma categories and maps between totals', a)
    old_transport_leaf = body[a:b]
    new_transport_leaf = old_transport_leaf.replace('''≔ comp_cat_fapp0
     (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
     (@fapp1_func K Cat_cat E x y);''', '''≔ @comp_cat_fapp0 (Hom_cat K x y)
    (Functor_cart_cat (Fibre_cat E x) (Fibre_cat E y)) (Fibre_cat E y)
    (@comp_cat_fapp0
      (Functor_cart_cat (Fibre_cat E x) (Fibre_cat E y))
      (Functor_cat (Fibre_cat E x) (Fibre_cat E y)) (Fibre_cat E y)
      (@fapp0_func (Fibre_cat E x) (Fibre_cat E y) u)
      (Functor_cart_include (Fibre_cat E x) (Fibre_cat E y)))
    (@fapp1_func K Cat_cart E x y);''')
    new_transport_leaf = new_transport_leaf.replace(
        ': τ (Functor (Op_cat (Hom_cat Z x y)) Cat_cat)',
        ': τ (Functor (Op_cat (Hom_cat Z x y)) Cat_cart)')
    new_transport_leaf = new_transport_leaf.replace('@tapp0_fapp0 Z Cat_cat D E y FF',
                                                    '@tapp0_fapp0 Z Cat_cart D E y FF')
    replace_once(old_transport_leaf, new_transport_leaf, 'fibre transport and defined Homd leaf',
                 'Keep the existing evaluation/composition bodies through Cartesian coefficient inclusion; the defined relative leaf retains arbitrary lax FF')

    replace_once('rule Op_cat Terminal_cat ↪ Terminal_cat;',
                 'rule Op_cat Terminal_cat ↪ Terminal_cat;\nrule CoAbove2_cat Terminal_cat ↪ Terminal_cat;',
                 'total duality terminal category', 'The corrected negative Sigma also uses total reversal')
    replace_once('''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);''', '''rule Op_cat (Product_cat $A $B)
  ↪ Product_cat (Op_cat $A) (Op_cat $B);
rule CoAbove2_cat (Product_cat $A $B)
  ↪ Product_cat (CoAbove2_cat $A) (CoAbove2_cat $B);''',
                 'total duality product', 'Retain product normal forms in the explicit constant-family Sigma-Hom')
    total_family = (fragment('total_op_family.lpfragment')
                    .replace('TotalOp_func_func', 'TotalOp_cart_func_func')
                    .replace('total_op', 'total_op_cart').replace('Cat_cat', 'Cat_cart'))
    total_family = (total_family.replace('@comp_fapp0 Cat_cart', '@comp_fapp0 Cat_cat')
                    .replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart'))
    total_family += '''
// The same total-fibre object formation through ordinary fixed
// postcomposition. Its parameter profile remains distinct from Cart.
// lhs-audit: keep 1,2,3 -- named coefficient duality at its ordinary Hom owner.
rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) _ _ _ total_op_cart
      (@CoAbove2_func $K Cat_cart $E)
  ↪ @TotalOp_catd $K $E;
'''
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           total_family, 'Adapt the qualified total-fibre duality to the selected Cartesian coefficient')

    replace_once('''//     ↪ Op_cat(Σ (p : Hom_K(x,y)^op), homd_(id_E,x,u,y,v)[p]).
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ Op_cat
      (@Sigma_cat
        (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v));''', '''//     ↪ O(Σ (p : O(Hom_K(x,y))), O_fib(homd_(id_E,x,u,y,v))[p]).
// Total fibre duality followed by the outer total dual restores fibre directions.
rule Hom_cat (@Sigma_cat $K $E) (Struct_sigma $x $u) (Struct_sigma $y $v)
  ↪ TotalOp_cat
      (@Sigma_cat
        (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)));''',
                 'Sigma Hom', 'Use the qualified total-dual negative Sigma while retaining the original total and Homd leaf owners')
    a = body.index('// Keep the first Hom owner; refine its recursive next action.')
    b = body.index('// Capped next projection joins the whole route on a visible Sigma cell.', a)
    old_projection = body[a:b]
    old_body = '''      (@Op_func
      (@Sigma_cat (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))
      (Op_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (Op_cat (Hom_cat $K $x $y))
        (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))'''
    assert old_projection.count(old_body) == 1
    new_body = '''      (@TotalOp_func
      (@Sigma_cat (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v)))
      (TotalOp_cat (Hom_cat $K $x $y))
      (@Sigma_proj1_func (TotalOp_cat (Hom_cat $K $x $y))
        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))
          (@homd_ $K $E $E (@id_funcd $K $E) $x $u $y $v))))'''
    replace_once(old_projection, old_projection.replace(old_body, new_body),
                 'Sigma recursive first projection', 'Retain the first-Hom owner and refine its next action through the corrected negative total')
    start = body.index('symbol sigma_proj1_hom_fapp1_fapp0\n')
    end = body.index(';', start) + 1
    old_projection = body[start:end]
    replace_once(old_projection, old_projection.split('≔', 1)[0] + '≔ sigma_Fst theta;',
                 'Sigma second-cell projection facade', 'Infer the actual corrected nested Sigma carrier instead of spelling the former reversed fibre')

    a = body.index('// Stable head for the computationally important projection pullback.')
    b = body.index('// 9c. Families over Sigma totals and displayed-transfor uncurrying', a)
    old_sigma_families = body[a:b]
    new_sigma_families = re.sub(r'(\$?K\s+)Cat_cat', r'\1Cat_cart', old_sigma_families)
    new_sigma_families = new_sigma_families.replace(
        'Cat_cat\n      (@Sigma_proj1_pullback_catd',
        'Cat_cart\n      (@Sigma_proj1_pullback_catd')
    new_sigma_families = new_sigma_families.replace(
        '(@Sigma_cat $K $R)\n      Cat_cat',
        '(@Sigma_cat $K $R)\n      Cat_cart')
    new_sigma_families = new_sigma_families.replace(
        '(@Sigma_cat $K $R)\n        Cat_cat',
        '(@Sigma_cat $K $R)\n        Cat_cart')
    # The original total constructor consumes the ordinary diagram category;
    # the canonical Cartesian Hom enters it through its existing whole view.
    start = new_sigma_families.index('// Whole represented-Sigma base change accumulates')
    new_sigma_families = (new_sigma_families[:start]
        + re.sub(r'@hom_int\b', '@hom_int_view', new_sigma_families[start:]))
    replace_once(old_sigma_families, new_sigma_families, 'Sigma family observations and base change',
                 'Change only the admitted family coefficient and the existing whole Hom inclusion at the original total-map consumers')

    hom_view_pattern = '''      (@comp_fapp0
        Cat_cat _ _ Cat_cat
        (@comp_fapp0
          Cat_cat _ _ Cat_cat
          (@Sigma_func $B)
          (@Pullback_catd_func $B $D $G))
        (@hom_int_view $C $D $H))
      $F
  ↪'''
    replace_once(hom_view_pattern, '''      (@comp_fapp0 Cat_cat _ _ _
        (@comp_fapp0 Cat_cat _ _ _
          (@comp_fapp0 Cat_cat _ _ _
            (@Sigma_func $B)
            (@Pullback_catd_func $B $D $G))
          (Functor_cart_include $D Cat_cart))
        (@hom_int $C $D $H))
      $F
  ↪''', 'represented Sigma base change through the actual Hom inclusion',
                 'Match the normalized composition of the transparent Hom view: its existing inclusion associates to the left before the stable Hom owner; preserve the original reframe and outer F')
    replace_once('// Keeping F outside the fold preserves its whole higher action.  The rule is',
                 '// hom_int_view is transparent. Match its normalized whole inclusion and\n'
                 '// stable Hom owner, after the existing composition normalization.\n'
                 '// Keeping F outside the fold preserves its whole higher action.  The rule is',
                 'represented Sigma reframe pattern explanation',
                 'Record why the runtime pattern contains the actual inclusion rather than the readable alias')

    a = body.index('// 9c. Families over Sigma totals and displayed-transfor uncurrying')
    b = body.index('// 10. Mixed-variance family functor', a)
    old_sigma_uncurry = body[a:b]
    replace_once(old_sigma_uncurry, old_sigma_uncurry.replace('Cat_cat', 'Cat_cart'),
                 'families over Sigma totals',
                 'An admitted family over a total has the selected Cartesian coefficient in both its displayed input and its output')

    start = body.index('symbol Functor_comp_pair_func ')
    end = body.index(';', start) + 1
    old_pair_composition = body[start:end]
    replace_once(old_pair_composition,
                 old_pair_composition.replace('Functor_cat', 'Functor_cart_cat')
                     .replace('@comp_prod_func Cat_cat', '@comp_prod_func Cat_cart'),
                 'Cartesian pair composition',
                 'The original joint composition consumer now uses genuine Cartesian mapping inputs, while fixed ordinary whiskering remains lax')

    a = body.index('// 10. Mixed-variance family functor')
    b = body.index('// Mixed-variance hom family for two sections of a displayed family.', a)
    old_mixed = body[a:b]
    new_mixed = old_mixed.replace('Cat_cat', 'Cat_cart')
    new_mixed = new_mixed.replace('// Internalized constructor package for mixed-variance functor families.',
        '// Internalized mixed-family constructor. The negative parameter uses\n'
        '// Cartesian diagram maps; the positive parameter still admits lax FF.')
    new_mixed = (new_mixed.replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart')
                 .replace('Product_cat_cart_func', 'Product_cat_coeff_func'))
    fixed_end = new_mixed.index('// Coherent evaluation for a constant-domain displayed functor family.')
    new_mixed = (new_mixed[:fixed_end].replace('Functor_cat (', 'Functor_cart_cat (')
                  .replace('(Functor_cat\n', '(Functor_cart_cat\n') + new_mixed[fixed_end:])
    for variable in ('K', '$K'):
        old = f'(Op_cat (Catd_cat (Op_cat {variable})))'
        new = f'(Op_cat (Functor_cart_cat (Op_cat {variable}) Cat_cart))'
        assert new_mixed.count(old) == 1, variable
        new_mixed = new_mixed.replace(old, new)
    new_mixed = new_mixed.replace(
        "(@tapp0_fapp0 (Op_cat $K) Cat_cart $A' $A $k $L);",
        "(@tapp0_fapp0 (Op_cat $K) Cat_cart $A' $A $k\n"
        "        (@strict_transfor (Op_cat $K) Cat_cart $A' $A $L));")
    products_start = new_mixed.index('// Pointwise distribution of a pair of mixed functors into a product target.')
    new_mixed = (new_mixed[:products_start]
        + new_mixed[products_start:].replace('Functor_cat (', 'Functor_cart_cat (')
            .replace('(Functor_cat\n', '(Functor_cart_cat\n')
            .replace('@comp_cat_con_func', '@comp_cat_con_cart_func'))
    replace_once(old_mixed, new_mixed, 'mixed Functor_catd and its parameter action',
                 'Use Hom(Cat_cart) fibres; retain lax positive parameter maps and require the actual Cartesian negative parameter profile')

    a = body.index('// Mixed-variance hom family for two sections of a displayed family.')
    b = body.index('// 11. Representables and presheaf-family classifiers', a)
    old_mixed_hom = body[a:b]
    new_mixed_hom = old_mixed_hom.replace('Cat_cat', 'Cat_cart').replace('Op_catd', 'TotalOp_catd')
    new_mixed_hom = new_mixed_hom.replace('// Mixed-variance hom family for two sections of a displayed family.',
        '// Mixed-variance hom family. The negative section is over R(K), in\n'
        '// the total fibre dual O(E); the positive section is over K in E.')
    new_mixed_hom = new_mixed_hom.replace('@piapp0 $K (@TotalOp_catd',
                                         '@piapp0 (CoAbove2_cat $K) (@TotalOp_catd')
    new_mixed_hom = new_mixed_hom.replace('(@Op_func $K (Op_cat Cat_cart) $X)',
        '(@TotalOp_func (CoAbove2_cat $K) (TotalOp_cat Cat_cart) $X)')
    assert new_mixed_hom.count('  ↪ Transf_cat\n') == 1
    new_mixed_hom = new_mixed_hom.replace('  ↪ Transf_cat\n',
        '  ↪ Hom_cat\n      (Functor_cart_cat (Fibre_cat $A $k) (Fibre_cat $B $k))\n')
    replace_once(old_mixed_hom, new_mixed_hom, 'Hom_catd and Transf_catd negative sections',
                 'Retain the existing mixed section architecture with total fibre duality and the correct shifted negative-section base')

    a = body.index('// Constant-family section evaluation follows ordinary functor application.')
    b = body.index(';', a) + 1
    constant_section = body[a:b]
    replace_once(constant_section,
                 '// Constant-section evaluation is owned earlier with Pi and section evaluation.',
                 'constant-section evaluation relocation',
                 'The original computation is needed by constant negative sections before the Homd ladder')
    constant_section = constant_section.replace('      Cat_cat\n', '      Cat_cart\n')
    insert('// 8d. Fibre covariance and dependent-hom endpoint notation',
           constant_section, 'Keep the existing constant-section computation with its section owner')
    relocated.append({'owner': 'constant-section component', 'bodySha256': sha(constant_section)})

    replace_once('''symbol Rep_catd_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Catd_cat Z))
≔ @hom_int Z Z (@id Cat_cat Z);''', '''symbol Rep_catd_func [Z : Cat]
  : τ (Functor (Op_cat Z) (Catd_cat Z))
≔ @hom_int_view Z Z (@id Cat_cat Z);''',
                 'Rep_catd_func', 'Retain the existing lax diagram view of the canonical Cartesian representable root')
    replace_once('''≔ @hom_int_precomp_func Z Z (@id Cat_cat Z) y x p;''',
                 '''≔ @strict_transfor Z Cat_cart (@Rep_catd Z y) (@Rep_catd Z x)
    (@hom_int_precomp_func Z Z (@id Cat_cat Z) y x p);''',
                 'Rep_transport_func', 'Use the existing inclusion to observe canonical strict precomposition as a lax displayed map')

    replace_once('rule CoAt2_cat (CoAt2_cat $A) ↪ $A;',
                 'rule CoAt2_cat (CoAt2_cat $A) ↪ $A;\n'
                 'rule Op_cat (CoAt2_cat $A) ↪ CoAt2_cat (Op_cat $A);',
                 'transpose / dimension-two commutation',
                 'The existing shifted Edge/presheaf construction consumes this category-level duality comparison')
    a = body.index('symbol Edge_catd_func [Z : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol Edge_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat (Op_cat Z))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cart))
≔ @comp_cat_fapp0 (CoAt2_cat (Op_cat Z))
    (CoAt2_cat (Functor_cart_cat Z Cat_cart))
    (Functor_cart_cat (CoAt2_cat Z) Cat_cart)
    (@Op_catd_func Z)
    (@CoAt2_func (Op_cat Z) (Functor_cart_cat Z Cat_cart)
      (@hom_int Z Z (@id_func Z)));''',
                 'Edge_catd_func', 'The actual fibre transpose shifts the base and the whole represented parameter; no same-base coercion')
    a = body.index('symbol Presheaf_catd_func (K : Cat)')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol Presheaf_catd_func (K : Cat)
  : τ (Functor (Op_cat (Functor_cart_cat (Op_cat K) Cat_cart)) (Catd_cat K))
≔ comp_cat_fapp0
    (@fapp0_func (Catd_cat K) (Catd_cat K) (@Const_catd K Cat_cart))
    (@Functor_catd_func K);''',
                 'Presheaf_catd_func', 'Use the actual Cartesian negative parameter of the existing mixed-family constructor')
    a = body.index('symbol HomPresheaf_catd_func [Z : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], '''symbol HomPresheaf_catd_func [Z : Cat]
  : τ (Functor (CoAt2_cat Z) (Catd_cat (Op_cat (CoAt2_cat Z))))
≔ comp_cat_fapp0
    (@Presheaf_catd_func (Op_cat (CoAt2_cat Z)))
    (@Op_func (CoAt2_cat (Op_cat Z)) (Functor_cart_cat (CoAt2_cat Z) Cat_cart)
      (@Edge_catd_func Z));''',
                 'HomPresheaf_catd_func', 'Preserve the compositional presheaf construction at its actual shifted variance; Homd will use its Q-valued whole section')

    a = body.index('// 12. Directed homd target and internal homd functor')
    b = body.index('// 14. Section action over dependent homs', a)
    old_homd_core = body[a:b]
    replacement = ('// 12. Directed homd target and internal homd functor\n\n'
        + fragment('production_homd_index.lpfragment')
        + '\n' + fragment('production_homd_core.lpfragment')
        + '\n\n// 13. Dependent-hom projections and covariant fibre transport\n'
          '// The original names above now project the identity core and the\n'
          '// defined general-FF composition; no second primitive Homd theory.\n\n')
    replace_once(old_homd_core, replacement, 'native Q Homd and direct projection ladder',
                 'Replace the invalid ordinary-Pi target by the selected Q-valued transformation; reuse native Hom and original fibre-covariance owners')
    relocated.append({'symbols': ['FibCov_target_catd', 'FibCov_source_catd', 'fib_cov_int',
                                  'fib_cov_src_func', 'fib_cov_transf', 'homd_src_func',
                                  'homd_src_sec', 'homd_tgt_func'],
                      'originalBlockSha256': sha(old_homd_core),
                      'reason': 'Canonical covariance is required before the Q section and its root'})
    for name in ('homd_id_src_sec', 'homd_id_tgt_func'):
        matches = list(re.finditer(r'(?m)^symbol ' + name + r'\b[\s\S]*?;', body))
        assert len(matches) == 2, (name, len(matches))
        original_declaration = matches[-1][0]
        replace_once(original_declaration, '// ' + name + ' is now owned by the native identity Homd core.',
                     name + ' relocation', 'Reuse the original identity projection name in the corrected core')
        relocated.append({'symbol': name, 'originalDeclarationSha256': sha(original_declaration)})
    old_section = '(Pi_cat (Homd_target_section_catd E x))'
    occurrences = body.count(old_section)
    assert occurrences == 2, occurrences
    body = body.replace(old_section, '(@Homd_target_section_cat K E x)')
    changes.append({'owner': 'relative intrinsic section classifier views', 'count': occurrences,
                    'reason': 'The actual Q-valued section category replaces the defective former Pi target'})

    a = body.index('// 15. Internal displayed hom-action heads')
    b = body.index('// 16. Displayed components, displayed hom-action, and laxity extraction', a)
    old_intrinsic = body[a:b]
    new_intrinsic, count = re.subn(
        r'\((Transfd(?:_cat)?)\s+\(homd_int \(@id_funcd K E\)\)\s+'
        r'\(comp_catd_fapp0\s+\(homd_int (GG|FF)\)\s+\(Op_funcd FF\)\)\)',
        lambda m: '(' + m[1] + '\n        (comp_catd_fapp0 (homd_int ' + m[2] + ') FF)'
            + '\n        (homd_int (@id_funcd K E)))', old_intrinsic)
    assert count == 4, count
    new_intrinsic = new_intrinsic.replace('(homd_int (@id_funcd K E))',
        '(@strict_transfor K Cat_cart E (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K E)) (@homd_id_int K E))')
    new_intrinsic = new_intrinsic.replace('(@Transf_cat $K Cat_cat $E $D)',
                                          '(@Transf_cat $K Cat_cart $E $D)')
    comment_a = new_intrinsic.index('/*')
    comment_b = new_intrinsic.index('*/', comment_a) + 2
    new_intrinsic = new_intrinsic[:comment_a] + '/*\n  The corrected root target is transposed. Accordingly the intrinsic arrow\n  runs from homd_int(GG) o FF to homd_int(id_E), without transposing raw FF.\n  Its source-u component reverses again in T(S_E(x)), exposing the forward\n  dependent-Hom action. The weaker inner P index retains its directed cells.\n\n  Original ownership is preserved:\n    internal hom-action -> extracted laxity -> Sigma action consumes laxity.\n  No separate comparison argument is introduced, and Sigma is not used to\n  define the intrinsic action which its maps later consume.\n*/' + new_intrinsic[comment_b:]
    replace_once(old_intrinsic, new_intrinsic, 'corrected intrinsic Homd direction',
                 'Retarget the existing internal-action owners; retain lax FF and derive their projections through the directed Q index')

    # Constant transformations are canonically Cartesian. Strengthen these
    # existing owners, rather than introduce a parallel constant-map calculus.
    a = body.index('symbol Const_transf_func [K A : Cat]')
    b = body.index('/*\n  Pure Cat/Catd convenience helpers.', a)
    old_constants = body[a:b]
    new_constants = old_constants.replace(
        '(@Transf_cat K A (@Const_func K A x) (@Const_func K A y))',
        '(Hom_cat (Functor_cart_cat K A) (@Const_func K A x) (@Const_func K A y))')
    new_constants = new_constants.replace(
        ': τ (Transf (@Const_func K A x) (@Const_func K A y));',
        ': τ (@StrictTransfor K A (@Const_func K A x) (@Const_func K A y));')
    new_constants = new_constants.replace(
        '$k (@Const_transf $K $A $x $y $p)',
        '$k (@strict_transfor _ _ _ _ (@Const_transf $K $A $x $y $p))')
    new_constants = new_constants.replace(
        "$k $k' (@Const_transf $K $A $x $y $p)",
        "$k $k' (@strict_transfor _ _ _ _ (@Const_transf $K $A $x $y $p))")
    replace_once(old_constants, new_constants, 'canonical constant transformation profile',
                 'The original constant-map owners have Cartesian naturality; ordinary observations use the existing inclusion')

    a = body.index('// 16a. Fibre-level displayed components')
    b = body.index('// 16b. Identity-specialized displayed hom action and Sigma-map action', a)
    old_components = body[a:b]
    new_components = old_components.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat')
    # Generic composition of functors still belongs to the public Cat owner.
    new_components = new_components.replace('@comp_fapp0 Cat_cart', '@comp_fapp0 Cat_cat')
    new_components = new_components.replace('@comp_cat_con_func', '@comp_cat_con_cart_func')
    new_components = new_components.replace('@comp_cat_cov_func', '@comp_cat_cov_cart_func')
    new_components = new_components.replace(
        '(Transf_cat (Fibre_func FF z) (Fibre_func GG z))',
        '(Hom_cat (Functor_cart_cat (Fibre_cat E z) (Fibre_cat D z)) (Fibre_func FF z) (Fibre_func GG z))')
    begin = new_components.index('symbol tdapp0_fapp0')
    end = new_components.index(';', begin) + 1
    old_component_type = new_components[begin:end]
    new_components = new_components[:begin] + old_component_type.replace(
        ': τ (Transf (Fibre_func FF z) (Fibre_func GG z));',
        ': τ (@StrictTransfor (Fibre_cat E z) (Fibre_cat D z) (Fibre_func FF z) (Fibre_func GG z));') + new_components[end:]
    # The two horizontal component Homs have the actual Cartesian profile.
    new_components = re.sub(
        r'\(@Transf_cat\s+(\(Fibre_cat \$[A-Z] \$k\))\s+(\(Fibre_cat \$[A-Z] \$k\))',
        r'(Hom_cat (Functor_cart_cat \1 \2)', new_components)
    # Evaluation accepts the ordinary view of these classified components.
    new_components = re.sub(
        r'(\$r|\$u)\s+\(@tdapp0_fapp0 ([^;]*?)\)\)',
        r'\1\n        (@strict_transfor _ _ _ _ (@tdapp0_fapp0 \2)))',new_components)
    c = new_components.index('// Object-component projection for generic Sigma-total uncurrying.')
    d = new_components.index('// Point component of the totalized displayed transfor', c)
    observed = new_components[c:d]
    assert observed.count('(@tdapp0_fapp0') == 1
    observed = observed.replace('(@tdapp0_fapp0', '(@strict_transfor _ _ _ _ (@tdapp0_fapp0').replace('$eta);', '$eta));')
    new_components = new_components[:c] + observed + new_components[d:]
    new_components = new_components.replace(
        '≔ @tdapp0_fapp0 K E D FF GG z ϵ;',
        '≔ @strict_transfor _ _ _ _ (@tdapp0_fapp0 K E D FF GG z ϵ);')
    new_components = new_components.replace(
        '≔ tapp0_fapp0 Terminal_obj (tdapp0_fapp0 k eta);',
        '≔ tapp0_fapp0 Terminal_obj (strict_transfor (tdapp0_fapp0 k eta));')
    # Retire the false unconditional left/middle equation. The conventional
    # pre/right leg, not the post/left comparison, is strict.
    c = new_components.index('/*\n  Ambient lax source-action reading:')
    d = new_components.index('// First-class whole path', c)
    new_components = new_components[:c] + '// Conventional pre/right action: the selected middle is FF[y] o E[p].\n// The left/post route retains its directed comparison.\nunif_rule @tapp1_func $K Cat_cart $E $D $x $y $FF\n  ≡ @comp_fapp0 Cat_cat _ _ _\n      (@hom_postcomp_func Cat_cart Cat_cart (@id Cat_cat Cat_cart) _ _ _\n        (@tapp0_fapp0 $K Cat_cart $E $D $y $FF))\n      (@fapp1_func $K Cat_cart $E $x $y)\n  ↪ [ tt ≡ tt ];\n\n' + new_components[d:]
    new_components = new_components.replace('functord_transport_lhs_tele_agrees', 'functord_transport_rhs_tele_agrees')
    new_components = new_components.replace('functord_transport_lhs_agrees', 'functord_transport_rhs_agrees')
    for name in ('functord_transport_rhs_tele_agrees', 'functord_transport_rhs_agrees'):
        c = new_components.index('symbol ' + name)
        d = new_components.index(';', c) + 1
        new_components = new_components[:c] + new_components[c:d].replace(
            'functord_transport_lhs_', 'functord_transport_rhs_') + new_components[d:]
    new_components = new_components.replace('Full left strict-naturality route', 'Full left/post transport route')
    new_components = new_components.replace('Full right strict-naturality route', 'Full selected pre/right transport route')
    new_components = new_components.replace(
        '// The former generic target/right equality and derived strict-naturality path\n// are retired. Ambient code consumes `functord_laxity_transf`; strict code uses\n// the evidence-bearing paths in `emdash3_2_gray_profiles.lp`.',
        '// Only the pre/right route is the strict middle action. The post/left\n// route retains the comparison extracted by functord_laxity_transf; no\n// equality between the two routes is imposed for arbitrary FF.')
    new_components = new_components.replace('First-class whole path for the ambient left/source presentation.',
                                            'First-class whole path for the selected pre/right presentation.')
    new_components = new_components.replace('Evaluate the whole ambient left/source path at p.',
                                            'Evaluate the selected pre/right path at p.')
    new_components += '''
// The displayed specialization erases tapp0_hom_fapp0 before the existing
// canonical covariance cut can fire. Keep the same projection normal form.
rule @tdapp0_fapp0 $K _ $E _ _ $y
      (@fapp1_fapp0 _ _
        (@fapp1_func _ _ (Functor_cart_include $K Cat_cart) _ $E)
        _ _ (@fapp1_fapp0 _ _ (@fib_cov_src_func $K $E $x) $u $v $h))
  ↪ @fib_cov_tapp0_u_map $K $E $x $y $u $v $h;

'''
    replace_once(old_components, new_components, 'displayed component and transport profiles',
                 'Use actual Cartesian fibre Homs, retaining lax base action; replace the false left/middle comparison by the selected right/middle comparison')
    insert('/*\n  Runtime component projection for the existing functorial Sigma-section\n  owner:',
           fragment('production_displayed_component_accumulation.lpfragment') + '\n',
           'Recover the existing conventional pre/right accumulation after evaluation has projected to tdapp0_fapp0; retain the actual codomain and the non-strict post/left leg')

    a = body.index('// 16b. Identity-specialized displayed hom action and Sigma-map action')
    b = body.index('// 16c. Section action and displayed laxity cells', a)
    replace_once(body[a:b], fragment('production_intrinsic_projection.lpfragment') + '\n',
                 'intrinsic identity projection ladder',
                 'Retain the existing projection names through the actual Q section, Cartesian fibre Hom and directed index; total Hom uses the derived negative Sigma')

    a = body.index('symbol piapp1_func [K : Cat]')
    b = body.index(';', a) + 1
    replace_once(body[a:b], 'symbol piapp1_func [K : Cat] (E : τ (Catd K))\n  (s : τ (Obj (Pi_cat E))) (x y : τ (Obj K))\n  : τ (Obj (@Pi_cat (TotalOp_cat (Hom_cat K x y))\n      (@TotalOp_catd (Op_cat (Hom_cat K x y))\n        (@homd_ K E E (@id_funcd K E)\n          x (@piapp0 K E s x) y (@piapp0 K E s y)))))\n≔ @fapp1_fapp0 (CoAbove2_cat (Homd_index_cat (Hom_cat K x y)))\n    (Catd_cat (TotalOp_cat (Hom_cat K x y)))\n    (Homd_index_total_family_func (Hom_cat K x y))\n    (fapp0 (@homd_id_tgt_func K (@Const_catd K Terminal_cat) x Terminal_obj y) Terminal_obj)\n    (fapp0 (@homd_ff_tgt_func K (@Const_catd K Terminal_cat) E s x Terminal_obj y) Terminal_obj)\n    (@fdapp1_int_presheaf_arrow K (@Const_catd K Terminal_cat) E s\n      x Terminal_obj y Terminal_obj);',
                 'negative-index section action',
                 'Use the existing positive Pi over the actual total-dual index family; derive the section from the existing intrinsic P-arrow')

    a = body.index('// Totalizing the native Hom section retains the entire next action.')
    b = body.index('// Raw canonical-triangle cell extracted from the internal displayed hom-action.', a)
    replace_once(body[a:b], '// Totalizing the native Hom section retains its negative index presentation.\nrule @fapp1_func _ _ (@section_total_func $K $E $s) $x $y\n  ↪ @TotalOp_func\n      (TotalOp_cat (Hom_cat $K $x $y))\n      (@Sigma_cat (TotalOp_cat (Hom_cat $K $x $y))\n        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))\n          (@homd_ $K $E $E (@id_funcd $K $E)\n            $x (@piapp0 $K $E $s $x) $y (@piapp0 $K $E $s $y))))\n      (@section_total_func (TotalOp_cat (Hom_cat $K $x $y))\n        (@TotalOp_catd (Op_cat (Hom_cat $K $x $y))\n          (@homd_ $K $E $E (@id_funcd $K $E)\n            $x (@piapp0 $K $E $s $x) $y (@piapp0 $K $E $s $y)))\n        (@piapp1_func $K $E $s $x $y));\n\n', 'negative section totalization',
                 'The existing recursive totalization uses total reversal, matching the corrected Sigma Hom and Pi index')

    a = body.index('// 16c. Section action and displayed laxity cells')
    b = body.index('// 16d. Arbitrary displayed-transfor hom-action projections', a)
    old_section_action = body[a:b]
    new_section_action = old_section_action.replace('@fapp0 $K.[] Cat_cat $E.[]', '@fapp0 $K.[] Cat_cart $E.[]')
    new_section_action = new_section_action.replace('@tapp0_fapp0 _ Cat_cat _ _ $k', '@tapp0_fapp0 _ Cat_cart _ _ $k')
    new_section_action = new_section_action.replace('$K Cat_cat\n      (@Const_catd $K Terminal_cat)',
                                                    '$K Cat_cart\n      (@Const_catd $K Terminal_cat)')
    replace_once(old_section_action, new_section_action, 'section and Sigma family coefficient observations',
                 'Change only the admitted-family coefficient tags in existing section/base-change projections')

    a = body.index('// 16d. Arbitrary displayed-transfor hom-action projections')
    b = body.index('// 16e. Strict/cartesian and terminal-source specializations', a)
    replace_once(body[a:b], fragment('production_intrinsic_modification.lpfragment') + '\n\n',
                 'general displayed-transfor intrinsic projections',
                 'Use the same Q section, Cartesian fibre Hom and directed inner index as the identity specialization; retain epsilon and all original projection names')

    a = body.index('// 16e. Strict/cartesian and terminal-source specializations')
    b = body.index('// 17. Generic Sigma/Pi weakening, ordinary structural logic, and delayed projection helpers', a)
    old_specializations = body[a:b]
    represented = '(@hom_int_precomp_func $Z $Z (@id Cat_cat $Z) $y $x $p)'
    assert old_specializations.count(represented) == 2
    replace_once(old_specializations, old_specializations.replace(represented,
        '(@strict_transfor _ _ _ _ ' + represented + ')'),
        'canonical represented displayed specialization',
        'Use the ordinary displayed view of the existing Cartesian Hom source action; do not pass the classified strict transfor as a raw FF')

    constant_coherence = fragment('production_index_constant_coherence.lpfragment')
    marker2 = '// Part 2: constant coefficient formation, at Const_catd.'
    marker3 = '// Part 3: coefficient duality inverse, after TotalOp_catd.'
    postwhiskering, constant_tail = constant_coherence.split(marker2)
    constant_views, coefficient_inverse = constant_tail.split(marker3)
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           postwhiskering, 'Fixed postwhiskering composition and unit, with both other legs identity; no unrestricted lax-square interchange')
    insert('// A represented family along a constant diagram is pointwise Hom(w,u).',
           constant_views, 'Whole constant-family/strict-functor duality views needed by the actual constant-index constructor')
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           coefficient_inverse, 'Cartesian coefficient double duality, including its already-formed family head')

    insert('// Consumed object action of canonical total base change, preserving the whole tapp1 heads.',
           fragment('production_constant_section_index.lpfragment'),
           'Whole constant-family intrinsic action uses the ordinary strict functor Hom action through the actual constant-index constructor')
    a = body.index('// Proof-time comparison only: terminal-source displayed laxity agrees with')
    b = body.index('// Transparent theorem exposing the terminal-source proof-time comparison.', a)
    replace_once(body[a:b], '''// Constant-family section action now computes through the whole index
// constructor above. The former point-only proof-time rule is redundant.

''', 'constant section point comparison',
                 'The retained theorem follows the whole constant-index computation instead of an independent point agreement')

    body = body.replace(
        '// Transparent theorem exposing the terminal-source proof-time comparison.\n// Its reflexive body exercises the unification rule; this is not runtime beta.',
        '// Retained theorem for the terminal-source comparison. Its reflexive\n// body now follows the whole constant-index computation.')
    body = body.replace(
        '// Constant-section arrow action agrees propositionally with ordinary functor\n// action. The section projection computes to `fdapp1_int_cell`; the preceding\n// proof-time comparison supplies the final ordinary view.',
        '// The existing theorem records the constant section arrow computation.\n// The whole index specialization and its lower projections now retain the\n// ordinary functor action directly.')

    a = body.index('// 17a. Generic Sigma/Pi introduction and evaluation')
    b = body.index('// 17b. Constant sections and delayed product-pair telescope rules', a)
    replace_once(body[a:b], fragment('production_evaluation.lpfragment') + '\n\n',
                 'Sigma introduction and section-first Pi evaluation',
                 'Retain all lax sections through the actual Pi-to-Functord identity view; do not impose the invalid k-first Cartesian evaluation comparison')
    body = body.replace('    pi_eval_transf(E)                 : const(ΠE) ⊢ E\n'
                        '    pi_eval_transf(E)[k]              = piapp0_func(E,k) : ΠE ⊢ E[k]',
                        '    pi_eval_transf(E)                 : ΠE ⊢ (const(1) ⊢ E)\n'
                        '    pi_eval_transf(E)[s][k](*)        = s[k]')

    insert('// A canonical represented mate of a Cartesian whole map has a lax y-square.',
           fragment('production_q_reindex.lpfragment'),
           'Qualify whole right-represented composition by actual Cartesian source reindexing; retain the weaker inner index maps')

    a = body.index('// Stable weakening owner for ordinary functor categories.')
    b = body.index('// Direct displayed weakening for a mixed functor source slot.', a)
    old_weakening = body[a:b]
    new_weakening = old_weakening.replace('Functor_cat', 'Functor_cart_cat')
    replace_once(old_weakening,
                 '// The canonical Const_func_func owner is declared in 17b,\n'
                 '// before its product-pair telescope consumer.\n\n',
                 'constant functor owner relocation',
                 'The existing constant transformation is Cartesian; retain one owner and make it available at the first actual product consumer')
    insert('// Pairing telescope for products.\n//\n', new_weakening,
           'Canonical constant functors have Cartesian parameter action; ordinary lax sections remain separate')
    a = body.index('// Pairing telescope for products.\n//\n')
    b = body.index('// 17c. Ordinary functor structural logic', a)
    old_pairing = body[a:b]
    new_pairing = old_pairing.replace('@const_section_func $B $A', '@Const_func_func $B $A')
    new_pairing = new_pairing.replace('Functor_cat', 'Functor_cart_cat')
    new_pairing = new_pairing.replace('(@Transf_cat $B $B (@id_func $B) (@id_func $B))',
                                    '(Hom_cat (Functor_cart_cat $B $B) (@id_func $B) (@id_func $B))')
    replace_once(old_pairing, new_pairing, 'Cartesian product-pair telescope projections',
                 'Use the actual Cartesian constant-functor and constant-transfor owners instead of the larger lax Pi classifier')

    a = body.index('// 17c. Ordinary functor structural logic')
    b = body.index('// 17d. Generic ordinary functor hom-action', a)
    replace_once(body[a:b], fragment('production_ordinary_structural.lpfragment') + '\n\n\n',
                 'Cartesian ordinary structural logic and displayed weakening',
                 'Preserve the original exchange/diagonal ladders with the mapping profiles required by their interchange laws; default Transf and Functord remain lax')
    a = body.index('// 17d. Generic ordinary functor hom-action')
    b = body.index('// 17e. Section pullback and internal Pi action', a)
    replace_once(body[a:b], fragment('production_pullback_structural.lpfragment') + '\n\n\n',
                 'Pullback action and recursive negative-total base change',
                 'Keep the original first-Hom owner and next-Hom rules, with total-dual index/fibres and actual Cartesian structural consumers')
    insert('// The same total-fibre object formation through ordinary fixed',
           fragment('production_total_op_pullback.lpfragment'),
           'Commute total fibre duality with reindexing along the actual R-dual base functor, for recursive Sigma base change')
    a = body.index('// 17e. Section pullback and internal Pi action')
    b = body.index('// 18. Cat-valued profunctors', a)
    replace_once(body[a:b], fragment('production_section_pullback.lpfragment') + '\n\n'
                 + fragment('production_cartesian_intrinsic.lpfragment') + '\n\n',
                 'Section pullback and classified intrinsic action',
                 'Retain general lax section/evaluation computations; replace invalid raw same-base Op mirrors by actual Cartesian intrinsic observations on the corrected profile')
    insert('// The primitive Unit_prof projection keeps the Hom action rigid at runtime.',
           fragment('production_cartesian_hom_action.lpfragment'),
           'The actual Cartesian displayed evaluator consumes the rigid Hom action at an object, with the same shared strict-functor interpretation')
    insert('/*\n  Contravariant represented-family reindexing is runtime accumulation:',
           fragment('production_cartesian_reindex_view.lpfragment'),
           'Internal Pi consumes the existing represented precomposition and admitted pullback as the same whole family')
    insert('// Identity specialization after the strict component has already projected.',
           fragment('production_cartesian_naturality.lpfragment'),
           'Reuse the existing default pre/right and actual strict-view post/left consumed-object computations at Cat_cart')
    a = body.index('injective symbol Eval_funcd [K A : Cat]')
    b = body.index(';', a) + 1
    old_eval_map = body[a:b]
    replace_once(old_eval_map,
                 old_eval_map.replace(': τ (Functord\n', ': τ (Hom (Functor_cart_cat K Cat_cart)\n'),
                 'Canonical displayed evaluation profile',
                 'The existing Cartesian evaluator is strictly natural for admitted families; retain one constructor and its ordinary inclusion view')
    replace_once('rule @tapp0_fapp0 _ Cat_cart _ _ $k (@Eval_funcd _ $A $B)',
                 'rule @tapp0_fapp0 _ Cat_cart _ _ $k\n'
                 '      (@strict_transfor _ _ _ _ (@Eval_funcd _ $A $B))',
                 'Ordinary component of classified displayed evaluation',
                 'The same fibre Eval_func is observed through the actual Cartesian mapping inclusion')
    insert('// Target-internalized mirror of hom_int.',
           fragment('production_hom_source_composition.lpfragment'),
           'The target-map composition consumer needs strict Hom source action after its generic first-Hom projection has become a named transformation')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_fixed_postcomposition.lpfragment') + '\n'
           + fragment('production_fixed_precomposition.lpfragment'),
           'Fixed pre/postcomposition preserve vertical composition with the other legs identity; these are the consumed Homd target-map and corrected arrow-diagram projection joins')
    insert('// The old `comp_cat_con_transf` compatibility name has been removed; the Cat',
           fragment('production_precomposition_unit_view.lpfragment'),
           'The native zero-arrow family consumes the left unit across the existing stable-precomposition/raw-composite presentations; retain both actual functors and leave the general category-unit guards and whole horizontal-action interface unchanged')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_hom_next_action.lpfragment'),
           'The actual intrinsic-composite consumer requires the next Hom of two-sided whiskering and its existing component observations')
    insert('// 5d. Rigid two-endpoint Hom action',
           fragment('production_composition_identity_pair.lpfragment'),
           'The literal identity pair restores normality after displayed composition has projected to its first-Hom owner')
    insert('// 6c. Constant/opposite transfors and Cat-valued composition projections',
           fragment('production_displayed_unit_coherence.lpfragment'),
           'Whole intrinsic units require identity and associativity comparisons across the existing displayed/ordinary diagram facades; preserve actual operands and runtime Hom heads')
    insert('// 14. Section action over dependent homs',
           fragment('production_intrinsic_composite_views.lpfragment'),
           'Actual Homd target contravariance and associativity supply the whole whiskering endpoints without operational equality arguments')
    insert('// 16. Displayed components, displayed hom-action, and laxity extraction',
           fragment('production_intrinsic_composite.lpfragment'),
           'Compute the existing intrinsic action of a displayed composite by the checked whole modification, preserving both lax inputs')
    insert('// 18. Cat-valued profunctors',
           fragment('production_intrinsic_composite_projection.lpfragment'),
           'Join root-first and component-first observations of the same intrinsic composite; retain the actual first extracted cell inside the second intrinsic action')
    insert('// 18. Cat-valued profunctors',
           fragment('production_intrinsic_unit_projection.lpfragment'),
           'Join the intrinsic whole identity with the same existing section, y and index identity projections')

    # Canonical object-of-Hom result types avoid premature decomposition of
    # the injective Hom alias at the actual Cat_cart/total-opposite consumers.
    # These are definitionally the same types, not new component operations.
    for marker in ('symbol tapp0_fapp0 :', 'symbol fdapp1_int_cell ['):
        a = body.index(marker)
        b = body.index(';', a)
        old = body[a:b]
        start = old.rfind('τ (Hom')
        assert start >= 0, marker
        new = old[:start] + old[start:].replace('τ (Hom', 'τ (Obj (Hom_cat', 1) + ')'
        replace_once(old, new, marker,
                     'Expose the existing Obj(Hom_cat) result for coefficient inclusion and negative-section arrow typing; no type or computation is added')

    a = body.index('// 18b. Opposite profunctors and fixed-endpoint duality')
    b = body.index('// 18d. Unit hom profunctor and readable representables', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart').replace('Functor_cat', 'Functor_cart_cat'),
                 'Opposite profunctor and reindexing base action',
                 'Keep product-swap and product-map owners with the admitted family coefficient and its actual first Hom')

    # These original named strictness instances now duplicate the restored
    # generic strict-functor law. Keep projected/reindexing action rules:
    # their heads can erase the generic pattern and are a different case.
    for marker, name in (
            ('// Named direct strict composition owner for fixed-endpoint\n// profunctor duality.', 'Op_prof_func'),
            ('// Named direct strict composition owner for mixed-variance\n// profunctor implication.', 'Prof_imply_cov_func2'),
            ('// Named direct strict composition owner for the opaque\n// fixed-weight implication functor.', 'Prof_imply_cov_func')):
        assert body.count(marker) == 1, name
        start = body.index(marker)
        end = body.index(';', start) + 1
        redundant = body[start:end]
        assert redundant.count('rule @comp_fapp0') == 1, name
        replace_once(redundant,
                     '// Composition is inherited from the default strict-functor rule.',
                     name + ' redundant raw composition instance',
                     'Remove only the literal instance of the restored generic law; preserve the stable functor and every projected or higher-action owner')
    for old_comment, new_comment in (
            ('  Ambient normal-lax identity is inherited from the generic functor calculus;\n'
             '  composition is retained by the guarded named owner below.',
             '  Identity and composition are inherited from the default strict-functor\n'
             '  calculus.'),
            ('  direct product-domain presentation inherits ambient normal-lax identity\n'
             '  without requiring a visible Struct_sigma constructor. Its named composition\n'
             '  owner below preserves the intended strict mixed action.',
             '  direct product-domain presentation inherits default strict identity and\n'
             '  composition without requiring a visible Struct_sigma constructor.'),
            ('  normal-lax identity and guarded named composition owner remain visible before\n'
             '  the product pipeline unfolds.',
             '  generic strict identity and composition owners remain visible before\n'
             '  the product pipeline unfolds.')):
        replace_once(old_comment, new_comment, 'profunctor strict-default owner comments',
                     'Document the existing generic owner after retiring its redundant local instances')
    a = body.index('// 18d. Unit hom profunctor and readable representables')
    b = body.index('/*\n  Stable generic action of a displayed hom-family.', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Unit profunctor projections',
                 'The existing rigid Hom action lands in the admitted Cartesian coefficient')
    a = body.index('/*\n  Stable generic action of a displayed hom-family.')
    b = body.index('// Binary representable hom profunctor as endpoint reindexing of Unit_prof.', a)
    replace_once(body[a:b], fragment('production_hom_catd_action.lpfragment') + '\n',
                 'Existing Hom_catd action and semantic point comparison',
                 'Use the R-base total-dual negative section; retain both actual section cells and the transported positive source under the conventional-lax direction')
    a = body.index("// Proof-time comparison of curry's semantic telescope with the native Hom family.")
    b = body.index('// Right-representable hom profunctor,', a)
    old = body[a:b]
    replace_once(old, old.replace('(@id Cat_cat Cat_cat)', '(@id Cat_cat Cat_cart)')
                 .replace('$B _ Cat_cat $R', '$B _ Cat_cart $R'),
                 'Represented profunctor curry comparisons',
                 'Retain both actual endpoint functors and compare against the corrected Cartesian Hom package')
    a = body.index('// Component of the existing whole reindexed map:')
    b = body.index(';', a) + 1
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Reindexed profunctor-map component',
                 'General lax ProfMap components remain ordinary strict fibre functors at the admitted coefficient')
    a = body.index('// Component of a functor-induced shaped unit is the ordinary hom-action.')
    b = body.index('// 18h. Tensor, shaped introduction, and fixed-endpoint co-Yoneda maps', a)
    old = body[a:b]
    replace_once(old, old.replace('Cat_cat', 'Cat_cart').replace('@hom_int ', '@hom_int_view '),
                 'Functor-induced shaped unit action',
                 'Use the existing ordinary view of Cartesian Hom in the retained internal-action projection')
    a = body.index('// Ordinary whole hom action of a recursor on the generating cross functor.')
    b = body.index('// 18z. Late cross-section normalization bridges', a)
    old = body[a:b]
    replace_once(old, old.replace(') Cat_cat', ') Cat_cart'), 'Join cross component computations',
                 'Keep the original whole/point cross rules; canonical tapp0 result typing supplies the coefficient boundary without extra LHS guards')
    old = '''      $A
      $B
      Cat_cat
      (@Pullback_catd $B $C $E $F)'''
    replace_once(old, old.replace('Cat_cat', 'Cat_cart'), 'Late family pullback accumulation',
                 'Only the family codomain changes; ambient functor composition remains Cat_cat')

    insert('// Object action of a Sigma map:', fragment('production_sigma_coefficient.lpfragment')
           + '\n' + fragment('production_sigma_parameter_profile.lpfragment'),
           'The actual comma family needs the Cartesian restriction of existing totalization, with the same total categories and strict-map action')
    insert('// Fibrewise dimension-one transpose changes the base by CoAt2.',
           fragment('production_total_op_parameter.lpfragment'),
           'Expose total-dual strict family-map components at the existing whole TotalOp_catd_func owner')
    insert('// Whole represented-Sigma base change accumulates before a retained outer',
           fragment('production_sigma_basechange_coefficient.lpfragment'),
           'Canonical Cartesian parameter view of original total base change, with unchanged components and actual ordinary restriction')
    insert('// Whole represented-Sigma base change accumulates before a retained outer',
           fragment('production_sigma_constant_projection.lpfragment'),
           'Canonical second-projection owner and measured projection-order joins for constant-target Sigma maps; preserve the original whole and first-Hom views and the conventional pre/right base-change action')
    sigma_composition = '''// Stable Sigma-map / represented-composition proof-time join.
unif_rule @sigma_map_func $K _ _
    (@hom_postcomp_fapp0 (@Catd_cat $K) (@Catd_cat $K)
      (@id Cat_cat (@Catd_cat $K)) $E $M $D $GG $FF)
  ≡ @comp_fapp0 Cat_cat (@Sigma_cat $K $E) (@Sigma_cat $K $M) (@Sigma_cat $K $D)
      (@sigma_map_func $K $M $D $GG) (@sigma_map_func $K $E $M $FF)
  ↪ [ tt ≡ tt ];'''
    replace_once(sigma_composition, sigma_composition.replace(
        '// Stable Sigma-map / represented-composition proof-time join.',
        '// Stable Sigma-map / represented-composition proof-time join.\n'
        '// Composite endpoint tags are inferred from the actual Sigma maps;\n'
        '// they can carry proof-time-equal total-dual family presentations.').replace(
        '≡ @comp_fapp0 Cat_cat (@Sigma_cat $K $E) (@Sigma_cat $K $M) (@Sigma_cat $K $D)',
        '≡ @comp_fapp0 Cat_cat _ _ _'),
        'Sigma represented-composition comparison',
        'Remove measured inferred endpoint discrimination while preserving the actual base, all three families and both displayed maps')
    insert('rule @fapp0 _ _ (@section_total_func $K $E $s) $k',
           fragment('production_total_dual_projection_views.lpfragment'),
           'Total-dual instances of the existing Sigma projection comparisons, retaining section/map/base-change heads and all data')
    insert('// Direct proof-time reading of represented-family reindexing.',
           fragment('production_pullback_composite_view.lpfragment'),
           'Direct existing reindexing/associativity comparison at the whole family, preserving actual bases and maps under total duality')
    a = body.index('// 18zz. Whole comma projection and displayed laxity extraction')
    b = body.index('// 19. Applications:', a)
    replace_once(body[a:b], fragment('production_comma_projection.lpfragment') + '\n',
                 'Original comma identity sections and whole laxity projection',
                 'Use negative totals, the actual E-to-transposed-target Homd roots, and the existing Q/P projection ladder; keep arbitrary eta and general lax FF')
    insert('// The public whole laxity candidate is now an object projection, not an\n',
           fragment('intrinsic_rule.lpfragment'),
           'Strict default: retain the existing extracted functor-compositor rule at its migrated comma owner')
    insert('// Whole post/left ordinary laxity.', fragment('conventional_lax_intrinsic.lpfragment'),
           'Retain the conventional pre/right extracted identity at the same migrated owner; post/left laxity remains directed')
    insert('// Whole post/left ordinary laxity.', fragment('production_pre_laxity_projection.lpfragment') + '\n',
           'Join the existing intrinsic-cell projection with the conventional pre/right whole identity, including observation after identity specialization')
    replace_once('''  Its native signature deliberately retains the opposite hom_int owner.  The
  active proof-time hom_int/hom_con_int comparison supplies the readable view

    hom_con_int(id_A) => hom_con_int(F) o G.
''', '''  Its native signature uses the ordinary inclusion hom_con_int_view:

    hom_con_int_view(id_A) => hom_con_int_view(F) o G.

  The native owners admit general conventional-lax epsilon. The direct
  transpose comparison above applies to a strict-transfor input, using the
  ordinary inclusion on both that input and its Op_transf image.
''', 'Target-internalized action comment',
                 'Document the actual native signature and the narrower direct-transpose comparison without changing either interface')
    insert('// Whole post/left ordinary laxity.', fragment('production_represented_laxity_view.lpfragment'),
           'Whole canonical extraction after represented strict precomposition, constrained to the actual intrinsic modifications and retained fixed-slot Hom action')
    old = 'rule @tapp0_fapp0 $A $B $F $H $Y (@comp_fapp0 (Functor_cat $A $B) $F $G $H $η $ϵ)'
    replace_once(old, old.replace('$A $B $F $H $Y', '_ _ _ _ $Y', 1),
                 'Ordinary composite component inference slots',
                 'Recover endpoints from the actual composite; repeated inferred presentations prevented the arbitrary Homd-action projection')
    old = '''rule @tapp0_fapp0
      $K Cat_cart $E $C $x
      (@comp_fapp0 (@Catd_cat $K) $E $D $C $FF $GG)'''
    replace_once(old, old.replace('$K Cat_cart $E $C $x', '_ _ _ _ $x', 1),
                 'Displayed composite component inference slots',
                 'The displayed constructor supplies the same endpoints; preserve component composition across equivalent target presentations')
    insert('injective symbol Catd_cat (K : Cat) : Cat;',
           fragment('production_cartesian_path_identity.lpfragment') + '\n',
           'The original J/structured-transport comparison needs the existing literal path-reflexivity identity view at Cat_cart')
    insert('// 5d. Rigid two-endpoint Hom action',
           fragment('production_identity_whiskering.lpfragment'),
           'The original EH unit consumers require identity whiskering after the composition Hom action has projected; guard both identity dimensions by their actual category')
    a = body.index('// 19. Applications:')
    b = body.index('// 19g. Eckmann-Hilton first computation slice', a)
    replace_once(body[a:b], fragment('production_pathout.lpfragment') + '\n',
                 'Original moving PathOut, path-induction and nested telescope interfaces',
                 'Use Cartesian PathOut formation, the actual motive pullback, restricted moving components of the retained lax fixed-source theorem, and total-dual negative sections')
    insert('// Generic object projection for Cat-valued postcomposition:',
           fragment('production_hom_image_reading.lpfragment'),
           'Proof-time whole reading of postcomposition through its actual mapped arrow, required by the inverse whole-endpoint proof')
    insert('// Stable fibre component of an arbitrary total arrow.',
           fragment('production_sigma_projection_frame_comparison.lpfragment'),
           'Sufficient first-Hom projection congruence for the same endpoints and arrow; retain both complete families and type annotations when comparing reindexing presentations')
    insert('// Internalized-x prerequisite: canonical total arrow over a base arrow.',
           fragment('production_sigma_map_projection_hom.lpfragment'),
           'Complete the capped observation order of the existing whole Sigma-map projection law, at the original constructor-visible total endpoints')
    insert('// Whole family-natural base-change totalization.  Its component at D is the',
           fragment('production_sigma_basechange_projection_hom.lpfragment'),
           'Complete the capped observation of total base change, retaining the actual base functor and its canonical pullback source')
    insert('// Pointwise arrow form of the Core-inclusion/opposite square.',
           fragment('production_core_path_image_view.lpfragment'),
           'Native strict-cell certificates retain the same path across proof-time-equal endpoint presentations; constrain every endpoint and the path itself')
    insert('// Whole post/left strict naturality guarded by the evidence-bearing view.',
           fragment('production_transfor_whole_readings.lpfragment'),
           'Whole pre/right presentation of the selected conventional action; compare already-projected components without changing the retained post/left cell')
    insert('// Second projection of off-diagonal internal hom-action.',
           fragment('production_internal_composite_action_view.lpfragment'),
           'Fixed-source whole vertical action with a strict earlier factor, retaining the later lax transfor and the actual source component')
    insert('// Cartesian whiskering uses the same Hom owners in the selected coefficient.',
           fragment('production_mapped_hom_square_views.lpfragment'),
           'Use the existing rigid two-endpoint Hom action as the common endpoint of canonical represented precomposition, including a mapped target arrow')
    a = body.index('/* API-04P: the following generic-F folds')
    b = body.index('// Proof-time associative reading after the composite has split', a)
    replace_once(body[a:b], fragment('production_default_post_accumulation.lpfragment') + '\n',
                 'Default represented postcomposition accumulation',
                 'Migrate the required strict-view computation to all default functors, retaining nested point cuts for existing inverse cancellation rather than introducing a split/fold loop')
    a = body.index('// Identity-family nested postcomposition reassociates under the stable owner.')
    b = body.index('// Postcomposition commutes with precomposition', a)
    replace_once(body[a:b], fragment('production_default_post_reassociation.lpfragment') + '\n',
                 'Default represented base-composite reassociation',
                 'Keep the same inverse-visible nested cuts when a composite base arrow has already projected to its identity-family postcomposition owner')
    a = body.index('// Ordinary precomposition along the named identity functor stays strict.')
    b = body.index('// Precomposing the identity at F[X]', a)
    replace_once(body[a:b], fragment('production_default_pre_accumulation.lpfragment') + '\n',
                 'Default represented precomposition accumulation',
                 'Move the corresponding whole, capped and mapped-arrow strict-view computations to the existing contravariant owner for default functors')
    # Preserve the complete original tail. A separately emitted prefix
    # qualifies only its preceding source; full-core qualification requires
    # the complete target and its actual consumers.
    out = root / 'tmp/probes/production_owner_migration'
    package = out / 'package'
    package.mkdir(parents=True, exist_ok=True)
    baseline_package = out / 'baseline_package'
    baseline_package.mkdir(exist_ok=True)
    assert not list(package.rglob('*.lpo')), 'Source-only candidate contains compiled objects'
    assert not list(baseline_package.rglob('*.lpo')), 'Source-only baseline contains compiled objects'
    (baseline_package / 'emdash3_2.lp').write_text(original)
    (baseline_package / 'emdash3_2_gray_profiles.lp').write_text(original_profiles)
    (baseline_package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (out / 'baseline.lp').write_text(original)
    (out / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    (package / 'emdash3_2.lp').write_text(body)
    (package / 'emdash3_2_gray_profiles.lp').write_text(profiles)
    (package / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    controls = (fragment('production_owner_controls.lpfragment') + '\n'
                + fragment('whole_controls.lpfragment') + '\n'
                + fragment('intrinsic_controls.lpfragment').replace('assertnot ', 'assert ')
                + '\n' + fragment('conventional_lax_controls.lpfragment')
                + '\n' + fragment('conventional_lax_projection_controls.lpfragment'))
    (package / 'owner_controls.lp').write_text('require open emdash.emdash3_2;\n\n' + controls)
    foundation_boundary = '// 8c. Section categories and Pi action'
    assert body.count(foundation_boundary) == 1
    (package / 'foundations_prefix.lp').write_text(body[:body.index(foundation_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment'))
    section_boundary = '// 8d. Fibre covariance and dependent-hom endpoint notation'
    assert body.count(section_boundary) == 1
    (package / 'sections_prefix.lp').write_text(body[:body.index(section_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment'))
    sigma_boundary = '// 10. Mixed-variance family functor'
    assert body.count(sigma_boundary) == 1
    sigma_controls = fragment('sigma_total_op_controls.lpfragment').replace(
        '(Op_cat (Hom_cat K x y)) Cat_cat', '(Op_cat (Hom_cat K x y)) Cat_cart')
    (package / 'sigma_prefix.lp').write_text(body[:body.index(sigma_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls)
    mixed_boundary = '// 11. Representables and presheaf-family classifiers'
    assert body.count(mixed_boundary) == 1
    mixed_controls = fragment('mixed_family_controls.lpfragment').replace('Cat_cat', 'Cat_cart')
    mixed_controls = mixed_controls.replace('(@Eval_funcd K A B)',
        '(@strict_transfor _ _ _ _ (@Eval_funcd K A B))')
    mixed_parameters = fragment('mixed_family_parameter_controls.lpfragment')
    mixed_parameters = mixed_parameters.split('// Dependency-complete recovery candidate for ambient fixed precomposition.', 1)[0]
    mixed_parameters = (mixed_parameters.replace('Cat_cat', 'Cat_cart')
                        .replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart'))
    negative_sections = fragment('total_op_hom_family_controls.lpfragment').replace('Cat_cat', 'Cat_cart')
    (package / 'mixed_prefix.lp').write_text(body[:body.index(mixed_boundary)]
        + '\n' + fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls + '\n' + mixed_controls
        + '\n' + mixed_parameters + '\n' + negative_sections)
    homd_boundary = '// 14. Section action over dependent homs'
    assert body.count(homd_boundary) == 1
    homd_controls = (fragment('production_foundations_controls.lpfragment')
        + '\n' + fragment('production_sections_controls.lpfragment')
        + '\n' + sigma_controls + '\n' + mixed_controls
        + '\n' + mixed_parameters + '\n' + negative_sections
        + '\n' + fragment('production_homd_controls.lpfragment')
        + '\n' + fragment('production_q_reindex_controls.lpfragment'))
    (package / 'homd_prefix.lp').write_text(body[:body.index(homd_boundary)]
        + '\n' + homd_controls)
    index_boundary = '// 15. Internal displayed hom-action heads'
    assert body.count(index_boundary) == 1
    index_controls = fragment('production_homd_index_controls.lpfragment')
    (package / 'index_profile.lp').write_text(body[:body.index(index_boundary)]
        + '\n' + index_controls)
    intrinsic_boundary = '// 16c. Section action and displayed laxity cells'
    assert body.count(intrinsic_boundary) == 1
    (package / 'intrinsic_identity_prefix.lp').write_text(body[:body.index(intrinsic_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment'))
    section_boundary = '// 17. Generic Sigma/Pi weakening, ordinary structural logic, and delayed projection helpers'
    assert body.count(section_boundary) == 1
    (package / 'section_action_prefix.lp').write_text(body[:body.index(section_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment'))
    evaluation_boundary = '// 17b. Constant sections and delayed product-pair telescope rules'
    assert body.count(evaluation_boundary) == 1
    (package / 'evaluation_prefix.lp').write_text(body[:body.index(evaluation_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment'))
    structural_boundary = '// 17c. Ordinary functor structural logic'
    assert body.count(structural_boundary) == 1
    (package / 'structural_prefix.lp').write_text(body[:body.index(structural_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment'))
    ordinary_boundary = '// 17d. Generic ordinary functor hom-action'
    assert body.count(ordinary_boundary) == 1
    (package / 'ordinary_structural_prefix.lp').write_text(body[:body.index(ordinary_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment'))
    pullback_boundary = '// 17e. Section pullback and internal Pi action'
    assert body.count(pullback_boundary) == 1
    (package / 'pullback_structural_prefix.lp').write_text(body[:body.index(pullback_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment')
        + '\n' + fragment('production_pullback_structural_controls.lpfragment'))
    section_pullback_boundary = '// 18. Cat-valued profunctors'
    assert body.count(section_pullback_boundary) == 1
    (package / 'section_pullback_prefix.lp').write_text(body[:body.index(section_pullback_boundary)]
        + '\n' + homd_controls + '\n' + index_controls
        + '\n' + fragment('production_intrinsic_controls.lpfragment')
        + '\n' + fragment('production_section_action_controls.lpfragment')
        + '\n' + fragment('production_evaluation_controls.lpfragment')
        + '\n' + fragment('production_constant_map_controls.lpfragment')
        + '\n' + fragment('production_ordinary_structural_controls.lpfragment')
        + '\n' + fragment('production_pullback_structural_controls.lpfragment')
        + '\n' + fragment('production_section_pullback_controls.lpfragment'))
    (package / 'intrinsic_composite_prefix.lp').write_text(
        (package / 'section_pullback_prefix.lp').read_text()
        + '\n' + fragment('production_intrinsic_composite_controls.lpfragment'))
    (package / 'intrinsic_unit_prefix.lp').write_text(
        (package / 'intrinsic_composite_prefix.lp').read_text()
        + '\n' + fragment('production_intrinsic_unit_controls.lpfragment'))
    profunctor_boundary = '// 18zz. Whole comma projection and displayed laxity extraction'
    assert body.count(profunctor_boundary) == 1
    inherited_controls = (package / 'intrinsic_unit_prefix.lp').read_text()[
        len(body[:body.index(section_pullback_boundary)]):]
    (package / 'profunctor_prefix.lp').write_text(body[:body.index(profunctor_boundary)]
        + inherited_controls + '\n' + fragment('production_profunctor_controls.lpfragment'))
    comma_boundary = '// 19. Applications:'
    assert body.count(comma_boundary) == 1
    comma_inherited = (package / 'profunctor_prefix.lp').read_text()[len(body[:body.index(profunctor_boundary)]):]
    (package / 'comma_prefix.lp').write_text(body[:body.index(comma_boundary)]
        + comma_inherited + '\n' + fragment('production_comma_controls.lpfragment'))
    pathout_inherited = (package / 'comma_prefix.lp').read_text()[len(body[:body.index(comma_boundary)]):]
    (package / 'pathout_controls.lp').write_text(body + '\n' + pathout_inherited
        + '\n' + fragment('production_pathout_controls.lpfragment'))
    (package / 'rule_hygiene_full_controls.lp').write_text(
        (package / 'pathout_controls.lp').read_text() + '\n'
        + fragment('production_adjunction_guard_controls.lpfragment'))
    (package / 'inverse_core_controls.lp').write_text(
        (package / 'rule_hygiene_full_controls.lp').read_text() + '\n'
        + fragment('production_inverse_cut_controls.lpfragment'))
    # Stage the pre-goal reviewer and exactly its imported source closure.
    # Only the explicit strict-default proof/control adaptations below and
    # the upstream core/profile owners override those original inputs.
    dependencies = {}
    visited = set()

    def stage(path):
        if path in visited:
            return
        visited.add(path)
        if path == 'emdash3_2.lp':
            text = body
        elif path == 'emdash3_2_gray_profiles.lp':
            text = profiles
        else:
            text = subprocess.check_output(
                ['git', 'show', PIN + ':emdash2/' + path], cwd=root, text=True)
            dependencies[path] = sha(text)
            baseline_target = baseline_package / path
            baseline_target.parent.mkdir(parents=True, exist_ok=True)
            baseline_target.write_text(text)
            selected_presentation = migrate_selected_presentation(path, text)
            if selected_presentation is not None:
                changes.append({'source': path, 'owner': 'selected kernel/cokernel presentation continuation',
                                'reason': 'Retain selected data, original generality and whole computations at the corrected oplax evaluation, mapped inverse and typed native map owners',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(selected_presentation)})
                text = selected_presentation
            selected_record_view = migrate_selected_record_view(path, text)
            if selected_record_view is not None:
                changes.append({'source': path, 'owner': 'original selected record/evaluation views',
                                'reason': 'Use existing oplax diagram/evaluation and total-dual initial views while preserving all original declarations, proof bodies, hypotheses and assertion polarities',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(selected_record_view)})
                text = selected_record_view
            kernel_boundary = migrate_kernel_boundary_prerequisite(path, text)
            if kernel_boundary is not None:
                changes.append({'source': path, 'owner': 'original connecting-kernel prerequisites',
                                'reason': 'Retain original whole constructions and hypotheses at oplax diagram profiles; use native shape action, direct terminal endpoints and existing whole mate/associativity paths',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(kernel_boundary)})
                text = kernel_boundary
            kernel_additive = migrate_kernel_additive_prerequisite(path, text)
            if kernel_additive is not None:
                changes.append({'source': path, 'owner': 'original product/coimage/additive-family prerequisites',
                                'reason': 'Retain original maps, inverses and assertions at the corrected diagram profiles; use direct diagonal endpoints and native quotient/shape computation in existing proofs',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(kernel_additive)})
                text = kernel_additive
            connecting_chain = migrate_connecting_kernel_chain(path, text)
            if connecting_chain is not None:
                changes.append({'source': path, 'owner': 'original additive-to-connecting-kernel chain',
                                'reason': 'Retain the original native maps, inverses and hypotheses at corrected diagram/duality types; stage the whole copair mate comparison before its original object application',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(connecting_chain)})
                text = connecting_chain
            native_connecting = migrate_native_connecting_consumer(path, text)
            if native_connecting is not None:
                changes.append({'source': path, 'owner': 'original native connecting/projection-zero consumers',
                                'reason': 'Retain original maps/inverses and hypotheses at corrected profiles; use existing ordinary modification reflection for the whole zero proof and retain its actual complete native input in reconstruction',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(native_connecting)})
                text = native_connecting
            simplex_dependency = migrate_simplex_dependency(path, text)
            if simplex_dependency is not None:
                changes.append({'source': path, 'owner': 'existing dependent-simplex and chain-pair consumers',
                                'reason': 'Use the corrected total-dual Sigma/Hom presentation and actual whole index-to-family action; reuse represented transport and retire redundant strict join wrappers while preserving the original recursive higher observations',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(simplex_dependency)})
                text = simplex_dependency
            diagram_observation = migrate_diagram_observation(path, text)
            if diagram_observation is not None:
                changes.append({'source': path, 'owner': 'existing zero-arrow and homology point observations',
                                'reason': 'Use the established whole oplax evaluation owners, total-dual initial hypothesis and explicit ordinary point decoders; preserve original mates, selected inverse data and OneCat guards without new rules or proof inputs',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(diagram_observation)})
                text = diagram_observation
            zero_arrow_input = migrate_zero_arrow_input(path, text)
            if zero_arrow_input is not None:
                changes.append({'source': path, 'owner': 'existing zero-composite inputs and native chain-map observations',
                                'reason': 'Use the existing Cartesian square action and its oplax inclusion, whole fixed evaluation, and the actual included Homdc family; retain the original arrows, filler, zero equations and OneCat guards',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(zero_arrow_input)})
                text = zero_arrow_input
            introduced_input = migrate_introduced_input(path, text)
            if introduced_input is not None:
                changes.append({'source': path, 'owner': 'original introduced-terminal-input comparison',
                                'reason': 'Map the original ordinary diagram comparison and its actual inverse through the existing coefficient inclusion; derive oplax map reflection through whole exchange and retained inverse comparisons, without new rules or supplied data',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(introduced_input)})
                text = introduced_input
            comma_profiles = {
                'emdash3_2_zero_arrow_cones.lp': (2, 6, 1, 1),
                'emdash3_2_zero_arrow_cone_maps.lp': (0, 10, 1, 3),
                'examples/zero_arrow_cone_maps.lp': (0, 21, 2, 6),
            }
            if path in comma_profiles:
                old = text
                counts = tuple(text.count(s) for s in ('(@Catd_cat B)',
                    'Functor_cat WalkingArrow_cat C', 'Functor WalkingArrow_cat C',
                    '@Transf WalkingArrow_cat C'))
                assert counts == comma_profiles[path], (path, counts)
                # The original whole two-sided total consumes this Cartesian
                # Hom family; keep its actual profile instead of forgetting it.
                text = text.replace('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)')
                text = text.replace('Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
                text = text.replace('Functor WalkingArrow_cat C', 'Obj (Functor_oplax_cat WalkingArrow_cat C)')
                text = text.replace('@Transf WalkingArrow_cat C', '@Hom (Functor_oplax_cat WalkingArrow_cat C)')
                text = text.replace('@diagram_family_at_func', '@diagram_oplax_family_at_func')
                text = text.replace('@diagram_family_transf', '@diagram_oplax_family_transf')
                if path == 'emdash3_2_zero_arrow_cones.lp':
                    text = text.replace('// Hom_B(F[-],-), with the first coordinate contravariant as required by homdc.',
                        '// Hom_B(F[-],-), retaining the Cartesian inner family required by\n'
                        '// the corrected two-sided total. No ordinary-family coercion is needed.')
                    marker = '// The zero-cone\'s datum is an actual transformation J(A)⇒d of arrow diagrams.'
                    assert text.count(marker) == 1
                    text = text.replace(marker, fragment('production_represented_comma_map.lpfragment') + '\n' + marker, 1)
                if path == 'emdash3_2_zero_arrow_cone_maps.lp':
                    map_body = '≔ Struct_sigma u (Struct_sigma v alpha);'
                    assert text.count(map_body) == 1
                    text = text.replace(map_body, '≔ @represented_comma_map C (Functor_oplax_cat WalkingArrow_cat C)\n'
                        '    (@terminal_arrow_diagram_func C t T) a0 a1 d0 d1 h0 h1 u v alpha;', 1)
                changes.append({'source': path, 'owner': 'represented comma and zero-cone total/maps',
                                'reason': 'Keep the canonical Cartesian Hom family consumed by the existing two-sided total, and use the actual oplax arrow coefficient of the terminal embedding; preserve the original nested-Sigma and map bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            fibre_inclusion_profiles = {
                'emdash3_2_one_cat_zero_cone_fibre_inclusion.lp': (17, 1, 1, 0),
                'examples/one_cat_zero_cone_fibre_inclusion.lp': (6, 2, 2, 3),
            }
            if path in fibre_inclusion_profiles:
                old = text
                ordinary, objects, homs, transfors = fibre_inclusion_profiles[path]
                for pattern, replacement, count in (
                    (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', ordinary),
                    (r'\(Functor WalkingArrow_cat C\)', '(Obj (Functor_oplax_cat WalkingArrow_cat C))', objects),
                    (r'@Transf_cat\s+WalkingArrow_cat\s+C\b', '@Hom_cat (Functor_oplax_cat WalkingArrow_cat C)', homs),
                    (r'@Transf\s+WalkingArrow_cat\s+C\b', '@Hom (Functor_oplax_cat WalkingArrow_cat C)', transfors),
                ):
                    text, actual = re.subn(pattern, replacement, text)
                    assert actual == count, (path, pattern, actual)
                if not path.startswith('examples/'):
                    text, actual = re.subn(r'Catd_cat (\(Functor_oplax_cat\s+WalkingArrow_cat\s+C\))',
                        r'Functor_cart_cat \1 Cat_cart', text)
                    assert actual == 3
                    for before, after in (
                        ('@Op_func', '@TotalOp_func'),
                        ('@Sigma_cat (Op_cat C)', '@Sigma_cat (TotalOp_cat C)'),
                        ('@sigma_fibre_inclusion_func (Op_cat C)', '@sigma_fibre_inclusion_func (TotalOp_cat C)'),
                    ):
                        assert text.count(before) == 1
                        text = text.replace(before, after)
                    text = text.replace(
                        '// Whole fibre inclusion for the ordinary zero-cone consumer. Its original\n// homdc total is unchanged; no general higher duality extension is asserted.',
                        '// Whole fibre inclusion through the existing two-sided total. The outer\n// inclusion uses total duality O; the represented inner family remains over T(C).')
                else:
                    header = 'require open emdash.emdash3_2_one_cat_zero_cone_fibre_inclusion;\n'
                    assert text.startswith(header)
                    text = header + fragment('production_zero_cone_fibre_reviewer_helpers.lpfragment') + '\n' + text[len(header):]
                    args = 'C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) a d'
                    for before, after in (
                        ('sigma_Fst (sigma_Snd mapped)', '@probe_fibre_middle ' + args + ' h k alpha'),
                        ('sigma_Snd (sigma_Snd mapped)', '@probe_fibre_cell ' + args + ' h k alpha'),
                    ):
                        assert text.count(before) == 1
                        text = text.replace(before, after)
                    marker = '// Both bases remain fixed and the existing fibre cell is retained.'
                    assert text.count(marker) == 1
                    text = text.replace(marker,
                        '// The generic observations specialize to the actual whole public inclusion.\n'
                        + 'assert ⊢ inclusion ≡ @probe_fibre_inclusion ' + args + ';\n\n' + marker, 1)
                changes.append({'source': path, 'owner': 'existing Sigma fibre inclusion into the zero-cone total',
                                'reason': 'Retain both original whole fibre inclusions with total duality on the outer base, the Cartesian represented inner family and the oplax diagram coefficient; elaborate reviewer projections generically and compare the actual whole inclusion before specialization',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_adjunction_mates.lp':
                old = text
                dependency = 'require open emdash.emdash3_2_defiso_evaluation_points;'
                assert text.count(dependency) == 1
                text = text.replace(dependency,
                    'require open emdash.emdash3_2_strict_functor_actions;\n' + dependency, 1)
                old_unif = 'unif_rule @Prof_cat $A $B ≡ @Functor_cat $Base Cat_cat'
                assert text.count(old_unif) == 1
                text = text.replace(old_unif, old_unif.replace('Cat_cat', 'Cat_cart'), 1)
                component = '''≔ @defiso_at (Product_cat (Op_cat R) L) Cat_cat
    (@Hom_prof_along R L L F (@id_func L))
    (@Hom_prof_along R L R (@id_func R) G)
    (@Adjunction_hom_prof_comparison R L F G J)
    (@Product_pair (Op_cat R) L X Y);'''
                assert text.count(component) == 1
                text = text.replace(component, '''≔ @defiso_fmap Cat_cart Cat_cat Cat_cart_include
    (Hom_cat L (@fapp0 R L F X) Y) (Hom_cat R X (@fapp0 L R G Y))
    (@defiso_at (Product_cat (Op_cat R) L) Cat_cart
      (@Hom_prof_along R L L F (@id_func L))
      (@Hom_prof_along R L R (@id_func R) G)
      (@Adjunction_hom_prof_comparison R L F G J)
      (@Product_pair (Op_cat R) L X Y));''', 1)
                observation = 'symbol adjunction_transpose_semantic_path'
                assert text.count(observation) == 1
                text = text.replace(observation, fragment('production_cartesian_defiso_component.lpfragment') + '\n' + observation, 1)
                changes.append({'source': path, 'owner': 'adjunction_hom_component_iso',
                                'reason': 'Evaluate the original Hom comparison in its actual Cat_cart coefficient, then apply the existing whole Cat_cart inclusion to retain the public Cat_cat inverse package and its chosen maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_prof_defiso_evaluation_paths.lp',
                        'examples/action_profile_prof_defiso_controls.lp'):
                old = text
                expected = 104 if path.startswith('emdash3_2_') else 38
                assert text.count('Cat_cat') == expected, (path, text.count('Cat_cat'))
                text = text.replace('Cat_cat', 'Cat_cart')
                if path.startswith('emdash3_2_'):
                    text = text.replace('The stable owner is unchanged; these are proof-time category views only.',
                        'The actual profunctor coefficient is Cat_cart. The stable owner and\n'
                        '   the original selected inverse data are unchanged; these remain proof-time views.')
                changes.append({'source': path, 'owner': 'profunctor selected inverse evaluation',
                                'reason': 'Evaluate the original forward and inverse maps in the actual Cat_cart coefficient, preserving every selected comparison and original observation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_defiso_evaluation_points.lp':
                marker = 'symbol defiso_at_to_path '
                assert text.count(marker) == 1
                addition = fragment('production_cartesian_defiso_point_cuts.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'evaluated inverse point cancellation',
                                'reason': 'Instance the existing two functor-valued point cuts at Cat_cart, retaining the actual chosen inverse package and evaluation point',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_discrete_functor_paths.lp':
                anchor = '// Core reflection, set-valued pointwise assembly, then the original core law.'
                assert text.count(anchor) == 1
                addition = fragment('production_discrete_functord_closure.lpfragment')
                text = text.replace(anchor, addition + '\n' + anchor, 1)
                changes.append({'source': path, 'owner': 'discrete displayed mapping category',
                                'reason': 'Structural fibrewise-discrete closure required for the original ordinary-target Hom-action admission; no global strictness or new caller data',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_presheaves.lp':
                old = text
                yoneda = '≔ @hom_con_int K K (@id_func K);'
                assert text.count(yoneda) == 1
                text = text.replace(yoneda, '≔ @hom_con_int_view K K (@id_func K);', 1)
                arrow_family = '''symbol arrow_into_catd (K : Cat) : τ (Catd K)
≔ @comp_cat_fapp0
    K
    (@Catd_cat (Op_cat K))
    Cat_cat
    (@Sigma_func (Op_cat K))
    (@yoneda_psh_func K);'''
                assert text.count(arrow_family) == 1
                text = text.replace(arrow_family, '''symbol arrow_into_catd (K : Cat) : τ (Catd K)
≔ @comp_cat_fapp0 K (Functor_cart_cat (Op_cat K) Cat_cart) Cat_cart
    (@Sigma_coeff_func (Op_cat K)) (@hom_con_int K K (@id_func K));''', 1)
                pullback_coefficient = '(Op_cat K)\n    Cat_cat\n    (@HigherSieveClassifier K)'
                assert text.count(pullback_coefficient) == 1
                text = text.replace(pullback_coefficient, pullback_coefficient.replace('Cat_cat', 'Cat_cart'), 1)
                postcompose_coefficient = '@fapp1_fapp0 K Cat_cat (@arrow_into_catd K)'
                assert text.count(postcompose_coefficient) == 1
                text = text.replace(postcompose_coefficient, postcompose_coefficient.replace('Cat_cat', 'Cat_cart'), 1)
                old_comment = '''  The comparison with `Psh_cat(Slice_cat(U))` goes through the stable shared
  presentation `Catd_cat(Into_restr_cat(U))`; no direct conversion rule is
  installed merely to make unification transitive.'''
                assert text.count(old_comment) == 1
                text = text.replace(old_comment, '''  The varying-base classifier uses Cartesian diagram maps. Its objects
  are the same Cat-valued families as Psh_cat(Slice_cat(U)), while their
  mapping profiles differ. No category equality with the ordinary lax-map
  presheaf category is asserted.''', 1)
                inclusion_anchor = 'symbol HigherSieve\n'
                assert text.count(inclusion_anchor) == 1
                text = text.replace(inclusion_anchor, '''// Whole ordinary view through the existing fixed-base family facade.
// The target annotation supplies the established one-step Psh comparison.
symbol higher_sieve_include_func [K : Cat] (U : τ (Obj K))
  : τ (Functor (@HigherSieve_cat K U) (@Catd_cat (@Into_restr_cat K U)))
≔ Functor_cart_include (@Into_restr_cat K U) Cat_cart;

''' + inclusion_anchor, 1)
                changes.append({'source': path, 'owner': 'presheaf Yoneda and canonical Sigma family',
                                'reason': 'Use the ordinary Hom inclusion for the unchanged raw presheaf category, and the canonical Cartesian Hom/Sigma coefficient for the whole arrow family; retain the existing slice presentation pending its actual controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_sieves.lp':
                old = text
                family_action = '@fapp1_fapp0 K Cat_cat (@arrow_into_catd K)'
                assert text.count(family_action) == 1
                text = text.replace(family_action,
                    '@fapp1_fapp0 K Cat_cart (@arrow_into_catd K)', 1)
                changes.append({'source': path, 'owner': 'ordinary sieve pullback evidence',
                                'reason': 'Use the actual coefficient of the canonical arrow family; retain pointwise subterminal evidence and the original pullback body',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            fibrewise_family_coefficients = {
                'emdash3_2_fibrewise_sigma.lp': 6,
                'examples/fibrewise_sigma.lp': 2,
                'examples/sieve_extensions.lp': 2,
                'emdash3_2_direct_cover_questions.lp': 2,
                'emdash3_2_yoneda_precomposition_value.lp': 3,
            }
            if path in fibrewise_family_coefficients:
                old = text
                assert text.count('Cat_cat') == fibrewise_family_coefficients[path], path
                text = text.replace('Cat_cat', 'Cat_cart')
                if path == 'emdash3_2_fibrewise_sigma.lp':
                    text = text.replace('Given E : K -> Cat and D : Sigma(E) -> Cat,',
                        'Given E : K -> Cat_cart and D : Sigma(E) -> Cat_cart,', 1)
                changes.append({'source': path, 'owner': 'fibrewise Sigma and direct-cover family coefficients',
                                'reason': 'Use the actual Cat_cart family coefficient in the original fibre/transport/projection computation; retain the original constructor, all family arguments and ambient lax displayed-map type',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_sieve_extensions.lp':
                old = text
                member_section = '''≔ @fib_cov_transf
    (Op_cat K)
    (@ordinary_sieve_extension_psh K U R)
    V
    (Struct_sigma p member);'''
                assert text.count(member_section) == 1
                text = text.replace(member_section, '''≔ @strict_transfor (Op_cat K) Cat_cart
    (@FibCov_source_catd (Op_cat K) V)
    (@ordinary_sieve_extension_psh K U R)
    (@fib_cov_transf
      (Op_cat K)
      (@ordinary_sieve_extension_psh K U R)
      V
      (Struct_sigma p member));''', 1)
                changes.append({'source': path, 'owner': 'ordinary sieve member section',
                                'reason': 'Expose the existing ordinary view of the canonical Cartesian FibCov section in the unchanged raw Psh category; retain the sieve member and all higher action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_direct_cover_question_families.lp':
                old = text
                for source, target, expected in [
                    ('_ Cat_cat _ _', '_ Cat_cart _ _', 2),
                    ('(Op_cat K) Cat_cat', '(Op_cat K) Cat_cart', 4),
                ]:
                    assert text.count(source) == expected, (path, source)
                    text = text.replace(source, target)
                represented_member = '''(@fib_cov_transf
          (Op_cat K)
          (@direct_cover_question_extension_psh K T U q)
          V
          (Struct_sigma p member))'''
                assert text.count(represented_member) == 1
                text = text.replace(represented_member, '''(@ordinary_sieve_member_section K V U p
          (@direct_cover_question_sieve K T U q) member)''', 1)
                changes.append({'source': path, 'owner': 'direct-cover question family components',
                                'reason': 'Observe displayed maps in Cat_cart and reuse the actual ordinary sieve-member section view; preserve ordinary functor equality types and the original whole comparison contracts',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/direct_cover_question_families.lp':
                old = text
                assert text.count('Cat_cat') == 3
                text = text.replace('Cat_cat', 'Cat_cart')
                changes.append({'source': path, 'owner': 'original direct-cover family reviewer',
                                'reason': 'Project the original displayed maps in their actual coefficient; retain all original observations and the proof-time/runtime distinction',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_direct_cover_internal_sheaves.lp':
                old = text
                components = r'(@tapp0_fapp0\s+\(@DirectCoverQuestion_cat K T\)\s+)Cat_cat'
                assert len(re.findall(components, text)) == 2
                text = re.sub(components, r'\1Cat_cart', text)
                changes.append({'source': path, 'owner': 'internal direct-cover glue and silent components',
                                'reason': 'Use Cat_cart for the two displayed component projections; retain the ambient Functor equality, original internal sheaf structure and whole silent law',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_direct_cover_completion_retained_sections.lp':
                old = text
                components = r'(@tapp0_fapp0\s+\(Op_cat K\)\s+)Cat_cat'
                assert len(re.findall(components, text)) == text.count('Cat_cat') == 38
                text = re.sub(components, r'\1Cat_cart', text)
                member = '(@fib_cov_transf (Op_cat K) (@direct_cover_question_extension_psh K T U q) V (Struct_sigma p member))'
                assert text.count(member) == text.count('@fib_cov_transf') == 15
                text = text.replace(member,
                    '(@ordinary_sieve_member_section K V U p (@direct_cover_question_sieve K T U q) member)')
                changes.append({'source': path, 'owner': 'direct-cover retained section derivations',
                                'reason': 'Observe the same raw presheaf maps in Cat_cart and reuse the ordinary view of their canonical represented section; preserve all fifteen original derived bodies and their input data',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_direct_cover_completion_locality.lp':
                old = text
                components = r'(@tapp0_fapp0\s+\(Op_cat \$?K\)\s+)Cat_cat'
                assert len(re.findall(components, text)) == 4
                text = re.sub(components, r'\1Cat_cart', text)
                start = text.index('injective symbol direct_cover_completion_restriction_glue_fibre_transf')
                end = text.index('rule @tdapp0_fapp0', start)
                declaration = text[start:end]
                assert declaration.count(': τ (@Transf\n') == 1
                text = text[:start] + declaration.replace(': τ (@Transf\n', ': τ (@StrictTransfor\n', 1) + text[end:]
                component = '''(@direct_cover_completion_restriction_glue_fibre_transf
        $K $T $P $V $U $q $m)'''
                assert text.count(component) == 1
                text = text.replace(component, '(@strict_transfor _ _ _ _ ' + component + ')', 1)
                member = '''(@direct_cover_completion_restriction_glue_fibre_transf
          K T P V U q m)'''
                assert text.count(member) == 1
                text = text.replace(member, '(@strict_transfor _ _ _ _ ' + member + ')', 1)
                for indent, expected in ((8, 2), (6, 1)):
                    ordinary_view = '(@direct_cover_completion_restriction_glue_fibre_transf\n' + ' ' * indent + 'K T P V U q m)'
                    assert text.count(ordinary_view) == expected
                    text = text.replace(ordinary_view, '(@strict_transfor _ _ _ _ ' + ordinary_view + ')')
                fibre_start = text.index('symbol direct_cover_completion_restriction_glue_fibre_omega')
                fibre_end = text.index('// Fibrewise whole equivalences are the pointwise evidence for rho[m].', fibre_start)
                fibre = text[fibre_start:fibre_end]
                assert fibre.count('@Functor_cat') == 1
                assert fibre.count('@strict_transf_pointwise_omega_along') == 1
                included = r'\(@strict_transfor _ _ _ _ (\(@direct_cover_completion_restriction_glue_fibre_transf\n\s+K T P V U q m\))\)'
                assert len(re.findall(included, fibre)) == 2
                fibre = fibre.replace('@Functor_cat', '@Functor_cart_cat')
                fibre = fibre.replace('@strict_transf_pointwise_omega_along', '@pointwise_cart_omega_along')
                fibre = re.sub(included, r'\1', fibre)
                text = text[:fibre_start] + fibre + text[fibre_end:]
                changes.append({'source': path, 'owner': 'direct-cover locality retained-member observation',
                                'reason': 'Use the canonical Cartesian fibre transformation and its derived Cartesian pointwise equivalence; preserve the original outer lax matching map, retained-member input and inherited outer assembly',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_direct_cover_completion_hit.lp',
                        'examples/direct_cover_completion_hit.lp'):
                old = text
                component = (r'(@tapp0_fapp0\s+_) Cat_cat' if path.startswith('emdash3_2_')
                    else r'(@tapp0_fapp0\s+\(@DirectCoverQuestion_cat K T\)\s+)Cat_cat')
                assert len(re.findall(component, text)) == 1
                replacement = r'\1 Cat_cart' if path.startswith('emdash3_2_') else r'\1Cat_cart'
                text = re.sub(component, replacement, text)
                changes.append({'source': path, 'owner': 'direct-cover completion glue component',
                                'reason': 'Read the original recursive glue in its actual family coefficient; preserve its extracted strictness property and whole silent law',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_hom_comparison_data.lp':
                old = text
                assert text.count('Cat_cat') == 82
                assert text.count('@hom_int ') == 12
                assert text.count('@Product_pair_tele_func') == 43
                # Preserve the two generic ordinary-functor inverse helpers.
                # The live profunctor paths below use their own coefficient
                # evaluations; these helpers do not consume those packages.
                ordinary_start = text.index('protected symbol hom_comparison_defiso_point_left')
                ordinary_end = text.index('// Evaluate the supplied whole DefIso', ordinary_start)
                ordinary_helpers = text[ordinary_start:ordinary_end]
                assert ordinary_helpers.count('Cat_cat') == 14
                text = (text[:ordinary_start].replace('Cat_cat', 'Cat_cart')
                        + ordinary_helpers
                        + text[ordinary_end:].replace('Cat_cat', 'Cat_cart'))
                text = text.replace('@hom_int ', '@hom_int_view ')
                text = text.replace('@Product_pair_tele_func', '@hom_comparison_pair_tele_func')
                anchor = '// Reconstruct F⇒G from its whole internal Hom action using the shared graph.'
                assert text.count(anchor) == 1
                addition = fragment('production_one_cat_hom_action_admission.lpfragment')
                text = text.replace(anchor, addition + '\n' + anchor, 1)
                view_anchor = '// Curry the supplied whole represented map at its original hom_int owners.'
                assert text.count(view_anchor) == 1
                text = text.replace(view_anchor,
                    fragment('production_lax_curry_hom_views.lpfragment') + '\n' + view_anchor, 1)
                start = text.index('symbol one_cat_transf_from_hom_action')
                end = text.index('// The original forward comparison', start)
                original = text[start:end]
                replacement = original.replace('@hom_int ', '@hom_int_view ')
                signature, definition = replacement.split('≔', 1)
                definition = re.sub(r'\balpha\b', '(@one_cat_hom_action_cart B C C1 F G alpha)', definition)
                text = text[:start] + signature + '≔' + definition + text[end:]
                start = text.index('symbol profmap_internal_hom_action')
                end = text.index('// η:id_A⇒GF', start)
                original_curry = text[start:end]
                replacement_curry = original_curry.replace('@hom_int ', '@hom_int_view ')
                replacement_curry = replacement_curry.replace('Cat_cat', 'Cat_cart')
                replacement_curry = replacement_curry.replace('@curry_func_func', '@curry_lax_func_func')
                text = text[:start] + replacement_curry + text[end:]
                pair_path, component_path = fragment('production_hom_comparison_curry_paths.lpfragment').split('// COMPONENT PATH\n', 1)
                start = text.index('protected symbol hom_comparison_pair_tele_identity_path')
                end = text.index('// Stage transfor identity evaluation', start)
                text = text[:start] + pair_path + '\n' + text[end:]
                start = text.index('protected symbol hom_comparison_prof_hom_action_component_path')
                end = text.index('symbol one_cat_hom_comparison_unit_component_path', start)
                text = text[:start] + component_path + '\n' + fragment('production_hom_comparison_admitted_path.lpfragment') + '\n' + text[end:]
                for owner, next_owner, idx, cod, ordinary, ff, gg, rr in (
                    ('symbol one_cat_hom_comparison_unit_component_path', 'symbol one_cat_hom_comparison_counit_component_path',
                     'A', 'A', 'A1', '(@id_func A)', '(@comp_cat_fapp0 A B A G F)', '(@hom_comparison_unit_profmap A B F G i)'),
                    ('symbol one_cat_hom_comparison_counit_component_path', 'protected symbol hom_comparison_prof_cov_cell',
                     'B', 'B', 'B1', '(@comp_cat_fapp0 B A B F G)', '(@id_func B)', '(@hom_comparison_counit_profmap A B F G i)'),
                    ('protected symbol hom_comparison_reconstruction_component_path', 'symbol one_cat_profmap_reconstruction_action_path',
                     'A', 'C', 'C1', 'F', 'G', 'r')):
                    start = text.index(owner)
                    end = text.index(next_owner, start)
                    signature, definition = text[start:end].split('≔', 1)
                    action = f'(@profmap_internal_hom_action {idx} {cod} {ff} {gg} {rr})'
                    assert definition.count(action) == 1, owner
                    admitted = f'''(@strict_transfor (Op_cat {idx}) (Catd_cat {idx})
        (one_cat_hom_action_source {idx}) (@one_cat_hom_action_target {idx} {cod} {ff} {gg})
        (@one_cat_hom_action_cart {idx} {cod} {ordinary} {ff} {gg} {action}))'''
                    definition = definition.replace(action, admitted, 1)
                    assert definition.count('@hom_comparison_prof_hom_action_component_path') == 1, owner
                    definition = definition.replace('@hom_comparison_prof_hom_action_component_path',
                        '@hom_comparison_admitted_hom_action_component_path', 1)
                    text = text[:start] + signature + '≔' + definition + text[end:]
                changes.append({'source': path, 'owner': 'ordinary-target supplied Hom-action reconstruction',
                                'reason': 'Retag 68 coefficient uses, retaining the two generic ordinary inverse helpers; adapt 12 ordinary Hom views and 43 pair-telescope views, derive admission from original OneCat(C), and use one-way lax curry with the shared graph and actual selected maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_modifications.lp':
                old = text
                specialization = '(@one_cat_modification _ Cat_cat _ _ _ _ _ $m)'
                assert text.count(specialization) == 1
                text = text.replace(specialization,
                    '(@one_cat_modification _ Cat_cart _ _ _ _ _ $m)', 1)
                changes.append({'source': path, 'owner': 'ordinary modification displayed component',
                                'reason': 'Retag the existing displayed specialization at its actual Cat_cart coefficient; preserve the general modification, original OneCat premise and supplied components',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_hom_comparison_data.lp':
                old = text
                assert text.count('Cat_cat') == 4
                text = text.replace('Cat_cat', 'Cat_cart')
                changes.append({'source': path, 'owner': 'original Hom-comparison reviewer',
                                'reason': 'Retag the four original profunctor component observations with their actual coefficient; preserve all selected comparisons and inverse controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            adjunction_intro_coefficients = {
                'emdash3_2_one_cat_adjunction_introduction.lp': 20,
                'examples/one_cat_adjunction_introduction.lp': 6,
            }
            if path in adjunction_intro_coefficients:
                old = text
                expected = adjunction_intro_coefficients[path]
                pattern = r'(\(Product_cat \(Op_cat A\) [AB]\)\s+)Cat_cat'
                assert text.count('Cat_cat') == expected, path
                assert len(re.findall(pattern, text)) == expected, path
                text = re.sub(pattern, r'\1Cat_cart', text)
                if path == 'emdash3_2_one_cat_adjunction_introduction.lp':
                    base = '(Product_cat (Op_cat A) B)'
                    left = '(@Hom_prof_along A B B F (@id_func B))'
                    right = '(@Hom_prof_along A B A (@id_func A) G)'
                    adj = '(@one_cat_adjunction_from_hom_comparison A B A1 B1 F G i)'
                    comparison = f'(@Adjunction_hom_prof_comparison A B F G {adj})'
                    point = '(@Product_pair (Op_cat A) B x y)'
                    evaluated = f'(@defiso_at {base} Cat_cart {left} {right} {comparison} {point})'
                    for direction, projection in [('transpose', 'to'), ('untranspose', 'from')]:
                        marker = f'symbol one_cat_adjunction_from_hom_comparison_{direction}_path'
                        assert text.count(marker) == 1
                        start = text.index(marker)
                        end = text.index(';', start) + 1
                        signature, definition = text[start:end].split('≔', 1)
                        mate = f'(@adjunction_{direction}_func A B F G {adj} x y)'
                        assert definition.count(mate) == 1
                        raw = f'(@defiso_at_{projection} {base} Cat_cart {left} {right} {comparison} {point})'
                        original_proof = definition[:-1].strip().replace(mate, raw, 1)
                        included_view = f'''@defiso_fmap_{projection}_path Cat_cart Cat_cat Cat_cart_include
      (Hom_cat B (@fapp0 A B F x) y) (Hom_cat A x (@fapp0 B A G y))
      {evaluated}'''
                        definition = f'''≔ @eq_trans _ _ _ _
    ({included_view})
    ({original_proof});'''
                        text = text[:start] + signature + definition + text[end:]
                changes.append({'source': path, 'owner': 'ordinary Hom-comparison adjunction introduction',
                                'reason': 'Retag the original coefficient positions and observe the actual Cat_cart_include mapped inverse before the existing input agreement; preserve the constructor, seven scoped comparisons, whole unit/counit agreement and reviewer controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_arrow_diagrams.lp':
                old = text
                dep = 'require open emdash.emdash3_2_arrow_diagram_families;'
                assert text.count(dep) == 1
                text = text.replace(dep, dep + '\nrequire open emdash.emdash3_2_one_cat_transfor_profiles;', 1)
                identity = 'rule @tapp1_fapp0 (Op_cat $K) _ _ _'
                assert text.count(identity) == 1
                text = text.replace(identity, 'rule @tapp1_fapp0 (CoAbove2_cat (Op_cat $K)) _ _ _', 1)
                text = text.replace('after its opposite identity normalizes.', 'after its total-dual identity normalizes.')
                original_body = '''≔ @transf_arrow_diagram_func (@LaxArrow_cat C) C
    (@cubical_src_func C) (@cubical_tgt_func C)
    (@one_cat_arrow_universal_transf C C1);'''
                assert text.count(original_body) == 1
                replacement = '''// OneCat(C) supplies the existing strict-transfor admission. Cartesian
// exchange then constructs the same ordinary diagram interface, through its
// actual inclusion; the default ambient transformations remain lax.
≔ @comp_cat_fapp0 (@LaxArrow_cat C) (Functor_cart_cat WalkingArrow_cat C)
    (Functor_cat WalkingArrow_cat C) (Functor_cart_include WalkingArrow_cat C)
    (@sym_func WalkingArrow_cat (@LaxArrow_cat C) C
      (@walking_arrow_func (Functor_cart_cat (@LaxArrow_cat C) C)
        (@cubical_src_func C) (@cubical_tgt_func C)
        (@one_cat_strict_transfor (@LaxArrow_cat C) C C1
          (@cubical_src_func C) (@cubical_tgt_func C)
          (@one_cat_arrow_universal_transf C C1))));'''
                text = text.replace(original_body, replacement, 1)
                anchor = 'symbol one_cat_arrow_diagram_func\n'
                assert text.count(anchor) == 1
                text = text.replace(anchor, fragment('production_cartesian_arrow_point.lpfragment') + '\n' + anchor, 1)
                text = share_arrow_cart_owner(text)
                changes.append({'source': path, 'owner': 'ordinary-target arrow diagrams',
                                'reason': 'Correct the total-dual identity guard and reuse existing OneCat strict-transfor admission with Cartesian exchange; share that defined Cartesian body with the zero-input oplax view, preserving the public ordinary target and original square data',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_arrow_diagrams.lp':
                old = text
                assert text.count('@hom_int ') == 2
                text = text.replace('@hom_int ', '@hom_int_view ')
                changes.append({'source': path, 'owner': 'ordinary arrow reviewer coefficient',
                                'reason': 'Pass the existing ordinary Hom-family view to the local square-fibre interface; preserve all original observations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/adjunction_mates.lp':
                old = text
                carrier = '@Transf (Product_cat (Op_cat R) L) Cat_cat'
                assert text.count(carrier) == 1
                text = text.replace(carrier, carrier.replace('Cat_cat', 'Cat_cart'), 1)
                changes.append({'source': path, 'owner': 'adjunction mate negative control',
                                'reason': 'Keep the constant-source rejection well typed in the actual displayed-family coefficient Cat_cart',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_adjunction_families.lp',
                        'examples/one_cat_adjunction_families.lp'):
                old = text
                count = 2 if path.startswith('emdash3_2_') else 4
                assert text.count('@comp_cat_cov_func_func_transf') == count
                text = text.replace('@comp_cat_cov_func_func_transf',
                    '@hom_postcomp_tele_transf Cat_cat Cat_cat (@id_func Cat_cat)')
                if path.startswith('emdash3_2_'):
                    text = text.replace('// Whole unit/counit observations through existing tele-postcomposition.',
                        '// Whole unit/counit observations through existing ordinary tele-postcomposition.\n'
                        '// The short comp_cat_cov_func_func_transf alias now selects Cartesian\n'
                        '// mapping categories; these original endpoints are ordinary Functor_cat.')
                changes.append({'source': path, 'owner': 'ordinary-target postcomposition adjunction unit/counit',
                                'reason': 'Use the existing generic Cat_cat telescope directly at the original ordinary mapping endpoints; preserve the supplied J, existing OneCat hypotheses and every reviewer statement',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_strict_pointwise_equivalences.lp':
                old = text
                marker = '// Displayed fixed-forward pointwise evidence over one whole transformation.'
                assert text.count(marker) == 1
                start = text.index(marker)
                displayed = text[start:]
                assert displayed.count('@Functor_cat') == 3
                text = text[:start] + displayed.replace('@Functor_cat', '@Functor_cart_cat')
                text = text.replace(marker, marker + '\n'
                    '// The actual Cat_cart fibre Hom is Cartesian: retain the forward cell\n'
                    '// and both chosen inverse components in that same coefficient.\n'
                    '// Whole assembly remains the inherited primitive assumption above.')
                imported = 'require open emdash.emdash3_2;'
                assert text.count(imported) == 1
                text = text.replace(imported, imported + '\n'
                    'require open emdash.emdash3_2_gray_profiles;\n'
                    'require open emdash.emdash3_2_eq1_evidence_property;', 1)
                derived_parts = []
                for name, boundary in (
                    ('production_inverse_unit_profiles.lpfragment', None),
                    ('production_strict_cell_reflection.lpfragment', '// Reflection keeps the actual cell'),
                    ('production_internal_composite_action_controls.lpfragment', '// A general earlier lax transfor'),
                    ('production_inverse_represented_unit.lpfragment', None),
                    ('production_whiskering_equivalences.lpfragment', '\nassert '),
                    ('production_represented_laxity_boundary.lpfragment', None),
                    ('production_inverse_admission.lpfragment', '\nassert '),
                    ('production_cartesian_inverse_laws.lpfragment', None),
                ):
                    part = fragment(name)
                    if boundary:
                        assert boundary in part, name
                        part = part.split(boundary, 1)[0]
                    derived_parts.append(part.rstrip())
                derived = ('// Derived Cartesian assembly for a classified strict forward map.\n'
                    '// The original ordinary inverse choices and whole laws are retained.\n'
                    '// Their extracted-cell strictness and the Cartesian cancellation laws\n'
                    '// are proved below; no further assembly principle is supplied.\n\n'
                    + '\n\n'.join(derived_parts) + '\n\n')
                text = text.replace(marker, derived + marker, 1)
                changes.append({'source': path, 'owner': 'displayed pointwise-equivalence coefficient',
                                'reason': 'Use the actual Cartesian coefficient of tdapp0_fapp0 and derive the Cartesian whole equivalence for strict forward maps from the original retained ordinary inverse/law owners',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_adjunction_family_views.lp':
                begin = '// Same Cat horizontal-action shape. Every pair and endpoint is compared.'
                end = '// Associativity where the inner composite retains its represented owner.'
                assert text.count(begin) == text.count(end) == 1
                a, b = text.index(begin), text.index(end)
                broad = text[a:b]
                assert broad.count('unif_rule') == 1
                replacement = (fragment('production_horizontal_payload_congruence.lpfragment') + '\n'
                    '/* Inactive broad view: unrestricted horizontal-action\n'
                    '   congruence intercepts reindexing across different factorizations.\n'
                    '   Restore only with guards qualified against both whole adjunction\n'
                    '   observations and arbitrary-parameter diagram reindexing.\n\n'
                    + broad.rstrip() + '\n*/\n\n')
                text = text[:a] + replacement + text[b:]
                changes.append({'source': path, 'owner': 'horizontal-action congruence',
                                'reason': 'Guard congruence by the common category triple and both actual input cells; preserve adjunction endpoint comparisons without decomposing distinct reindexing factorizations',
                                'oldBodySha256': sha(broad), 'newBodySha256': sha(replacement)})
            if path == 'emdash3_2_represented_comma_families.lp':
                old = text
                start_marker = '// Source, middle, and target families for a transformation graph.'
                end_marker = '// Fibrewise Sigma of the existing whole internal action.'
                assert text.count(start_marker) == text.count(end_marker) == 1
                start, end = text.index(start_marker), text.index(end_marker)
                tail = text[end:]
                assert tail.count('@hom_int ') == 107
                tail = tail.replace('@hom_int ', '@hom_int_view ')
                # The single inner-total formation still consumes Cart,
                # unlike the surrounding ordinary internal-action inputs.
                canonical = '(@homdc_edge_catd C C (@hom_int_view C C (@id_func C)))'
                assert tail.count(canonical) == 1
                tail = tail.replace(canonical, canonical.replace('@hom_int_view ', '@hom_int '), 1)
                sigma_end = '// Pointwise opposite turns that whole transformation into the displayed map'
                assert tail.count(sigma_end) == 1
                tail = end_marker + '\n' + fragment('production_comma_graph_sigma.lpfragment') + '\n' + tail[tail.index(sigma_end):]
                admission_end = '// The represented C-family at the varying source F[x].'
                assert tail.count(admission_end) == 1
                begin, end_admission = tail.index(sigma_end), tail.index(admission_end)
                tail = tail[:begin] + sigma_end + '\n' + fragment('production_comma_graph_admitted.lpfragment') + '\n' + tail[end_admission:]
                basechange_end = 'protected symbol comma_graph_target_sec\n'
                assert tail.count(basechange_end) == 1
                begin, end_basechange = tail.index(admission_end), tail.index(basechange_end)
                tail = tail[:begin] + admission_end + '\n' + fragment('production_comma_graph_basechange.lpfragment') + '\n' + tail[end_basechange:]
                total_end = '// The actual whole input classifier.'
                assert tail.count(total_end) == 1
                begin, end_total = tail.index(basechange_end), tail.index(total_end)
                tail = tail[:begin] + fragment('production_comma_graph_total.lpfragment') + '\n' + tail[end_total:]
                constructor_end = '// Whole source projection with its original inverse data.'
                assert tail.count(constructor_end) == 1
                begin, end_constructor = tail.index(total_end), tail.index(constructor_end)
                tail = tail[:begin] + total_end + '\n\n' + fragment('production_represented_comma_constructor.lpfragment') + '\n' + tail[end_constructor:]
                # Original source-comparison proof, with its actual selected
                # inverse data. Only total/section duals become O here; protect
                # the nine internal-Hom T(K) classifiers before that change.
                source_end = '// Extract the actual target section before taking the outer opposite.'
                assert tail.count(source_end) == 1
                begin, end_source = tail.index(constructor_end), tail.index(source_end)
                source = tail[begin:end_source]
                theta_type = '''(@Transf (Op_cat K) (@Catd_cat K)
    (@hom_int_view K K (@id_func K))
    (@comp_cat_fapp0 (Op_cat K) (Op_cat Y) (@Catd_cat K)
      (@hom_int_view Y K D) (@Op_func K Y (@comp_cat_fapp0 K X Y J A))))'''
                assert source.count(theta_type) == 9
                source = source.replace(theta_type, 'COMMA_SOURCE_THETA_TYPE')
                assert source.count('Op_cat') == 396 and source.count('Op_func') == 80
                source = source.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                source = source.replace('COMMA_SOURCE_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                source = source.replace(constructor_end, constructor_end + '\n'
                    '// Total/section duality is O; the admitted internal Hom remains over T(K).')
                step1 = 'protected symbol comma_source_gamma_step1 '
                step2 = 'protected symbol comma_source_gamma_step2 '
                assert source.count(step1) == source.count(step2) == 1
                s1, s2 = source.index(step1), source.index(step2)
                source = source[:s1] + fragment('production_comma_source_reframe.lpfragment') + '\n' + source[s2:]
                tail = tail[:begin] + source + tail[end_source:]
                # Expose the unchanged ordinary-lax public source interface
                # at its dependency-ready position. Only its canonical
                # internal-action admission changes; eta gains no premise.
                ordinary_start = 'symbol represented_comma_family_func '
                ordinary_end = 'symbol represented_comma_family_target_func '
                assert tail.count(ordinary_start) == tail.count(ordinary_end) == 1
                o1, o2 = tail.index(ordinary_start), tail.index(ordinary_end)
                ordinary = tail[o1:o2]
                assert ordinary.count('@tapp1_int_fapp0_transf') == 4
                ordinary = ordinary.replace('@tapp1_int_fapp0_transf', '@tapp1_int_cart')
                tail = tail[:o1] + tail[o2:]
                tail = tail.replace(source_end, '// Original ordinary-lax constructor and source comparison.\n'
                    + ordinary + '\n' + source_end, 1)
                # Target section uses the same corrected total base and the
                # existing canonical projection's ordinary displayed view.
                target_start = 'protected symbol comma_section_gamma_target_family_map '
                target_end = '// Link that section to the original total base change.'
                assert tail.count(target_start) == tail.count(target_end) == 1
                t1, t2 = tail.index(target_start), tail.index(target_end)
                target_section = tail[t1:t2]
                assert target_section.count(theta_type) == 6
                target_section = target_section.replace(theta_type, 'COMMA_TARGET_THETA_TYPE')
                assert (target_section.count('Op_cat'), target_section.count('Op_func'), target_section.count('Op_transf')) == (35, 3, 1)
                target_section = (target_section.replace('Op_cat', 'TotalOp_cat')
                                  .replace('Op_func', 'TotalOp_func').replace('Op_transf', 'TotalOp_transf'))
                target_section = target_section.replace('COMMA_TARGET_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                target_projection = '(@homdc_total_target_funcd X Y (@represented_comma_prof X Y J))'
                assert target_section.count(target_projection) == 1
                target_section = target_section.replace(target_projection, '(@strict_transfor _ _ _ _ ' + target_projection + ')')
                tail = tail[:t1] + target_section + tail[t2:]
                text = text[:start] + fragment('production_comma_graph_families.lpfragment') + '\n' + tail
                changes.append({'source': path, 'owner': 'represented-comma graph family profiles',
                                'reason': 'Retain canonical strict-x admission, total-dual sections, corrected base change, derived graph and original source inverse data; the coupled target adaptation is recorded below',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/action_profile_inherited_assembly_controls.lp':
                old = text
                assert text.count('Functor_cat (@Fibre_cat') == 2
                text = text.replace('Functor_cat (@Fibre_cat', 'Functor_cart_cat (@Fibre_cat')
                old_negative = 'assertnot [A B : Cat] (F : τ (Functor A B)) [x y z : τ (Obj A)]'
                assert text.count(old_negative) == 1
                text = text.replace(old_negative, old_negative.replace('assertnot', 'assert'), 1)
                text = text.replace('// The inherited primitive does not install these generic reflexivity cuts.',
                    '// Default functors now preserve composition; ordinary transfors remain lax.')
                changes.append({'source': path, 'owner': 'inherited assembly controls',
                                'reason': 'Observe the selected displayed inverse in its actual Cartesian coefficient, and update only the former lax-functor negative to the strict-default positive',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            zero_profiles = {
                'emdash3_2_zero_arrow_diagrams.lp': (2, 10, 0),
                'emdash3_2_kernel_cokernel_adjunctions.lp': (38, 5, 0),
                'emdash3_2_kernel_cokernel_adjunction_mates.lp': (16, 2, 4),
                'emdash3_2_cokernel_adjunction_families.lp': (16, 4, 0),
                'emdash3_2_one_cat_image_coimage_factors.lp': (4, 2, 0),
                'examples/kernel_cokernel_adjunctions.lp': (100, 9, 14),
            }
            if path in zero_profiles:
                old = text
                counts = (text.count('Functor_cat WalkingArrow_cat C'), text.count('(Op_cat C)'),
                          text.count('τ (Functor WalkingArrow_cat C)'))
                assert counts == zero_profiles[path], (path, counts)
                text = text.replace('Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
                text = text.replace('(Op_cat C)', '(TotalOp_cat C)')
                text = text.replace('τ (Functor WalkingArrow_cat C)', 'τ (Obj (Functor_oplax_cat WalkingArrow_cat C))')
                text = text.replace('τ (Transf d0 d1)', 'τ (Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)')
                if path == 'emdash3_2_zero_arrow_diagrams.lp':
                    assert text.count('@Op_transf ') == 1
                    text = text.replace('@Op_transf ', '@TotalOp_transf ')
                    text = text.replace('TerminalObject(Op(C),t)', 'TerminalObject(TotalOp(C),t)')
                    text = text.replace('  Op_transf.', '  TotalOp_transf.')
                    text = text.replace('transparently via Op.', 'through total duality, which retains the default lax profile.')
                    text = text.replace('C→Arr(C)', 'C→Arr_oplax(C)')
                elif path == 'emdash3_2_kernel_cokernel_adjunctions.lp':
                    text = text.replace('diagram_evaluation_at_func', 'diagram_oplax_evaluation_at_func')
                    text = text.replace('/* Whole kernel/cokernel adjunction structures for the preadditive setting.',
                        '/* Whole kernel/cokernel adjunction structures for the preadditive setting.\n'
                        '   The corrected whole zero-arrow embeddings land in oplax diagrams;\n'
                        '   the supplied adjunctions and their actual unit/counit data use that profile.')
                elif path == 'emdash3_2_one_cat_image_coimage_factors.lp':
                    assert text.count('@diagram_evaluation_at_func') == 4
                    text = text.replace('@diagram_evaluation_at_func', '@diagram_oplax_evaluation_at_func')
                if path == 'examples/kernel_cokernel_adjunctions.lp':
                    component = '@tapp0_fapp0 WalkingArrow_cat C _ _'
                    assert text.count(component) == 2
                    text = text.replace(component,
                        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _')
                    assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert','assertnot')] == [16,2]
                changes.append({'source': path, 'owner': 'whole terminal/initial embeddings and supplied kernel/cokernel adjunctions',
                                'reason': 'Retain the existing general terminal transformation; use the corrected oplax arrow-diagram profile and total duality for the initial transformation, with its dual hypothesis explicit',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_adjunction_family_views.lp':
                old = text
                text = migrate_adjunction_family_view_reviewer(text)
                changes.append({'source': path, 'owner': 'existing whole kernel/cokernel mate observations',
                                'reason': 'Retain all original statements, selected data and proof bodies with the actual oplax zero-arrow coefficient and total-dual terminal hypothesis; generic ordinary diagrams retain fixed evaluation and expose oplax shape composition at its encoded endpoints',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/zero_arrow_diagrams.lp':
                old = text
                text = fragment('production_zero_arrow_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + k + r'\b', old)) for k in ('assert','assertnot')] == [18,2]
                assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert','assertnot')] == [18,2]
                changes.append({'source': path, 'owner': 'zero-arrow reviewer',
                                'reason': 'Retain all original observations using the actual oplax coefficient, decoded point functors and the explicit total-dual terminal hypothesis',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_arrow_diagram_families.lp':
                old = text
                text = fragment('production_arrow_diagram_families.lpfragment')
                for name in ('transf_arrow_diagram_func', 'transf_arrow_diagram_point_path'):
                    assert old.count('symbol ' + name + '\n') == text.count('symbol ' + name + '\n') == 1
                changes.append({'source': path, 'owner': 'transf_arrow_diagram_func',
                                'reason': 'Introduce the same walking diagram through the corrected two-profile exchange; preserve the whole eta and decode its point observation through actual duality',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/arrow_diagram_families.lp':
                old = text
                text = fragment('production_arrow_diagram_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + k + r'\b', old)) for k in ('assert', 'assertnot')] == [22, 2]
                assert [len(re.findall(r'(?m)^' + k + r'\b', text)) for k in ('assert', 'assertnot')] == [22, 2]
                changes.append({'source': path, 'owner': 'arrow diagram reviewer',
                                'reason': 'Retain the original whole observations with oplax diagram coefficients, decoded point functors and the corresponding opposite-profile evaluation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_diagram_evaluation.lp':
                old = text
                first = '// Whole evaluation after precomposition:'
                last = '// Existing generic composition evidence at the ordinary family target.'
                assert text.count(first) == text.count(last) == 1
                start = text.index(first)
                end = text.index(last)
                text = (fragment('production_diagram_evaluation_profile.lpfragment') + '\n'
                        + fragment('production_odd_cartesian_action.lpfragment') + '\n'
                        + fragment('production_diagram_evaluation_naturality.lpfragment') + '\n'
                        + 'require open emdash.emdash3_2_one_cat_action_paths;\n'
                        + 'require open emdash.emdash3_2_one_cat_functor_closure;\n\n'
                        + text[start:end]
                        + fragment('production_one_cat_evaluation.lpfragment') + '\n'
                        + fragment('production_diagram_evaluation_helpers.lpfragment') + '\n'
                        + fragment('production_oplax_diagram_evaluation.lpfragment') + '\n'
                        + fragment('production_oplax_family_component_join.lpfragment') + '\n'
                        + fragment('production_oplax_family_double_exchange.lpfragment') + '\n'
                        + fragment('production_oplax_family_observations.lpfragment'))
                declaration = r'(?m)^(?:(?:constant|injective|protected|private)\s+)?symbol\s+([A-Za-z0-9_]+)\b'
                old_names, new_names = re.findall(declaration, old), re.findall(declaration, text)
                assert len(old_names) == 9
                assert all(new_names.count(name) == 1 for name in old_names)
                changes.append({'source': path, 'owner': 'diagram evaluation',
                                'reason': 'Preserve general fixed evaluation by postcomposition; correct whole shape evaluation to its alternating-dual oplax profile and reindex that actual profile',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/diagram_evaluation.lp':
                old = text
                text = fragment('production_diagram_evaluation_reviewer.lpfragment')
                assert [len(re.findall(r'(?m)^' + kind + r'\b', old))
                        for kind in ('assert', 'assertnot')] == [10, 3]
                assert [len(re.findall(r'(?m)^' + kind + r'\b', text))
                        for kind in ('assert', 'assertnot')] == [10, 3]
                changes.append({'source': path, 'owner': 'diagram evaluation reviewer',
                                'reason': 'Retain every original observation with the corrected opposite transformation profile and existing postcomposition action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_walking_arrow_native_observation.lp':
                old = text
                evaluation = '@diagram_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator'
                assert text.count(evaluation) == 3
                text = text.replace(evaluation,
                    '@one_cat_diagram_evaluation_transf WalkingArrow_cat C C1 walking_arrow_src walking_arrow_tgt walking_arrow_generator')
                former_head = '(@sym_tapp1_fapp0_transf _ $I $C (@id Cat_cat _) $i $j $u)'
                assert text.count(former_head) == 1
                text = text.replace(former_head,
                    '(@fapp1_fapp0 _ _ (@one_cat_diagram_evaluation_func $I $C $C1) $i $j $u)', 1)
                text = text.replace('// Whole classified evaluation; the ordinary hypothesis supplies its evidence.',
                    '// The existing ordinary-target guard selects ordinary evaluation.\n'
                    '// Its native lax admission and subsequent graph keep the original interface.')
                changes.append({'source': path, 'owner': 'ordinary-target native walking-arrow observation',
                                'reason': 'Use actual ordinary evaluation under the existing OneCat guard; retain the input diagram category, native graph, generator value and original value-path proof',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_walking_arrow_introduction.lp':
                addition = fragment('production_walking_arrow_postcomposition.lpfragment')
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'walking-arrow constructor postcomposition',
                                'reason': 'Normalize strict postcomposition and Cartesian evaluation at the existing free-arrow introduction, retaining both endpoints and its actual generating arrow',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_one_cat_transfor_profiles.lp':
                addition = (fragment('production_one_cat_mapping_comparison.lpfragment')
                            + '\n' + fragment('production_one_cat_mapping_inverse_views.lpfragment')
                            + '\n' + fragment('production_one_cat_mapping_evaluation.lpfragment'))
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'ordinary-target whole mapping-profile comparison',
                                'reason': 'Internalize existing strict admission under OneCat while retaining actual forward/inverse maps and the original mapping inclusion as a whole view; no classifier equality',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_functor_reconstruction_paths.lp':
                addition = fragment('production_functor_inverse_reflection.lpfragment')
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'reflection from a whole left-inverse path',
                                'reason': 'Use the actual inverse functor and its whole path to reflect arrow equality without requiring a new ordinary-category closure premise',
                                'insertedSha256': sha(addition)})
            if path == 'emdash3_2_one_cat_diagram_family_reflection.lp':
                old = text
                new = fragment('production_one_cat_family_reflection.lpfragment')
                marker = 'symbol one_cat_diagram_family_map_path'
                assert new.count(marker) == 1
                text = new.replace(marker,
                    fragment('production_one_cat_family_exchange.lpfragment') + '\n' + marker, 1)
                text += '\n' + fragment('production_one_cat_arrow_family_presentation.lpfragment')
                text += '\n' + fragment('production_one_cat_family_observations.lpfragment')
                text += '\n' + fragment('production_one_cat_family_oplax_exchange.lpfragment')
                text += '\n' + fragment('production_one_cat_oplax_roundtrip_view.lpfragment')
                text += '\n' + fragment('production_one_cat_oplax_exchange_paths.lpfragment')
                changes.append({'source': path, 'owner': 'ordinary-target whole diagram-family reflection',
                                'reason': 'Reprofile both mapping levels through actual inverse maps, reuse Cartesian exchange and original diagram reflection, then reflect through the derived left inverses; retain raw inputs and whole endpoint premises',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_diagram_family_reconstruction.lp',
                        'examples/one_cat_diagram_family_reconstruction.lp'):
                old = text
                replacements = [
                    (r'@diagram_family_at_func\s+B\s+WalkingArrow_cat\s+C\s+D',
                     '@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D'),
                    (r'@diagram_family_transf\s+B\s+WalkingArrow_cat\s+C\s+D',
                     '@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D'),
                    (r'@transf_arrow_diagram_func\s+B\s+C',
                     '@one_cat_transf_arrow_diagram_func B C C1'),
                    (r'@sym_func\s+B\s+WalkingArrow_cat\s+C\s+D',
                     '@one_cat_family_exchange B WalkingArrow_cat C C1 D'),
                    (r'@sym_func_func_transf\s+WalkingArrow_cat\s+B\s+C',
                     '@one_cat_family_exchange_map WalkingArrow_cat B C C1'),
                    (r'@sym_transf_tapp0_transf\s+B\s+WalkingArrow_cat\s+C',
                     '@one_cat_family_exchange_map_at B WalkingArrow_cat C C1'),
                    (r'@diagram_family_evaluation_func\s+B\s+WalkingArrow_cat\s+C',
                     '@one_cat_diagram_family_evaluation_func B WalkingArrow_cat C C1'),
                    (r'@one_cat_diagram_family_evaluation_comp_path\b',
                     '@one_cat_diagram_family_exchange_comp_path'),
                ]
                changed = {}
                for pattern, replacement in replacements:
                    text, count = re.subn(pattern, lambda _: replacement, text)
                    changed[pattern] = count
                assert all(changed[p] > 0 for p, _ in replacements[:3])
                if path.startswith('examples/'):
                    reconstructed = '''(@one_cat_transf_arrow_diagram_func B C C1
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_src)
      (@one_cat_family_exchange_at_func B WalkingArrow_cat C C1 D walking_arrow_tgt)
      (@one_cat_diagram_family_transf B WalkingArrow_cat C C1 D
        walking_arrow_src walking_arrow_tgt walking_arrow_generator))'''
                    for direction, source, target in (('to', reconstructed, 'D'), ('from', 'D', reconstructed)):
                        observation = f'''@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 _ _
    (@one_cat_diagram_family_reconstruction_{direction} B C C1 D)'''
                        assert text.count(observation) == 2
                        text = text.replace(observation,
                            f'''@one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    {source} {target}
    (@one_cat_diagram_family_reconstruction_{direction} B C C1 D)''')
                if not path.startswith('examples/'):
                    text += '\n' + fragment('production_one_cat_oplax_family_reconstruction.lpfragment')
                changes.append({'source': path, 'owner': 'whole diagram-family reconstruction',
                                'reason': 'Use the guarded ordinary exchange for the original exchanged endpoints and shape action, preserving arbitrary D, both reconstruction maps and the original proof outline',
                                'replacementCounts': changed,
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_arrow_family_isomorphisms.lp':
                old = text
                text = text.replace('@transf_arrow_diagram_func B C F G',
                    '@one_cat_transf_arrow_diagram_func B C C1 F G')
                assert text.count('≔ @sym_func_func_transf WalkingArrow_cat B C') == 2
                text = text.replace('≔ @sym_func_func_transf WalkingArrow_cat B C',
                    '≔ @one_cat_family_exchange_map WalkingArrow_cat B C C1')
                for direction, source_arrow, target_arrow in (('to','h','k'),('from','k','h')):
                    square = f'''(@one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
      F F G G {source_arrow} {target_arrow} (@id (Functor_cat B C) F) (@id (Functor_cat B C) G)
      (@iso_evidence_{direction} (Hom_cat (Functor_cat B C) F G) h k i))'''
                    assert text.count(square) == 1
                    text = text.replace(square,
                        f'(@one_cat_arrow_family_square_{direction} B C C1 F G h k i)', 1)
                anchor = '// Whole diagram action on the selected to modification.'
                assert text.count(anchor) == 1
                text = text.replace(anchor,
                    'require open emdash.emdash3_2_strict_functor_actions;\n\n'
                    + fragment('production_one_cat_arrow_family_source_evidence.lpfragment')
                    + '\n' + anchor, 1)
                for direction in ('left', 'right'):
                    marker = 'symbol one_cat_arrow_family_comparison_' + direction + '_law'
                    assert text.count(marker) == 1
                    start = text.index(marker)
                    end = text.index(';', start) + 1
                    signature, _ = text[start:end].split('≔', 1)
                    arrow_law_body = f'''≔ @iso_evidence_{direction}
    (Functor_cat B (Functor_cat WalkingArrow_cat C))
    (@one_cat_transf_arrow_diagram_func B C C1 F G h)
    (@one_cat_transf_arrow_diagram_func B C C1 F G k)
    (@iso_evidence_fmap
      (Functor_cat WalkingArrow_cat (Functor_cat B C))
      (Functor_cat B (Functor_cat WalkingArrow_cat C))
      (@one_cat_family_exchange_func WalkingArrow_cat B C C1)
      (@walking_arrow_func (Functor_cat B C) F G h)
      (@walking_arrow_func (Functor_cat B C) F G k)
      (@one_cat_arrow_family_source_evidence B C C1 F G h k i));'''
                    text = text[:start] + signature + arrow_law_body + text[end:]
                text += '\n' + fragment('production_one_cat_oplax_arrow_family_evidence.lpfragment')
                changes.append({'source': path, 'owner': 'whole arrow-family isomorphism',
                                'reason': 'Preserve the original square maps and chosen modifications through guarded ordinary exchange; prove their source diagram inverse laws and map that evidence with the existing strict functor action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/one_cat_arrow_family_isomorphisms.lp':
                old = text
                assert text.count('@sym_transf_tapp0_transf B WalkingArrow_cat C') == 4
                text = text.replace('@sym_transf_tapp0_transf B WalkingArrow_cat C',
                    '@one_cat_family_exchange_map_at B WalkingArrow_cat C C1')
                text = text.replace('@transf_arrow_diagram_func B C F G',
                    '@one_cat_transf_arrow_diagram_func B C C1 F G')
                for direction, source_arrow, target_arrow in (('to','h','k'),('from','k','h')):
                    observation = f'''@one_cat_family_exchange_map_at B WalkingArrow_cat C C1 _ _
    (@one_cat_arrow_family_comparison_{direction} B C C1 F G h k i)'''
                    assert text.count(observation) == 2
                    text = text.replace(observation, f'''@one_cat_family_exchange_map_at B WalkingArrow_cat C C1
    (@one_cat_transf_arrow_diagram_func B C C1 F G {source_arrow})
    (@one_cat_transf_arrow_diagram_func B C C1 F G {target_arrow})
    (@one_cat_arrow_family_comparison_{direction} B C C1 F G h k i)''')
                changes.append({'source': path, 'owner': 'original arrow-family isomorphism reviewer',
                                'reason': 'Retain its four endpoint identity and two inverse-choice observations at the guarded ordinary family/exchange presentation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_zero_arrow_family_point_inputs.lp':
                old = text
                text, count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == 6
                changes.append({'source': path, 'owner': 'original zero-arrow family point input',
                                'reason': 'Keep the original A[x], D[x], h[x] and cone constructor at the already-migrated native oplax diagram profile',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('examples/one_cat_homology_family_comparison.lp',
                        'examples/one_cat_homology_family_comparison_points.lp'):
                old = text
                is_points = path.endswith('_points.lp')
                text, count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == (9 if is_points else 46)
                text, count = re.subn(r'\(@TerminalObject\s+\(Op_cat C\)\s+t\)',
                    '(@TerminalObject (TotalOp_cat C) t)', text)
                assert count == (2 if is_points else 4)
                text, count = re.subn(r'@one_cat_functor_category\s+WalkingArrow_cat\s+C\s+C1',
                    '@one_cat_oplax_functor_category WalkingArrow_cat C C1', text)
                assert count == (0 if is_points else 6)
                assert [len(re.findall(r'(?m)^' + kind + r'\b', text))
                        for kind in ('assert', 'assertnot')] == ([4, 1] if is_points else [6, 0])
                changes.append({'source': path, 'owner': 'original whole/point homology comparison reviewer',
                                'reason': 'Retain every original assertion with only the native diagram profile, its existing OneCat closure and total-dual initial choice adjusted',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_homology_family_comparison.lp',
                        'emdash3_2_one_cat_homology_family_comparison_points.lp'):
                old = text
                text, diagram_count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert diagram_count == (165 if path.endswith('_comparison.lp') else 3)
                text, initial_count = re.subn(r'\(@TerminalObject\s+\(Op_cat C\)\s+t\)',
                    '(@TerminalObject (TotalOp_cat C) t)', text)
                assert initial_count == 1
                text, closure_count = re.subn(r'@one_cat_functor_category\s+WalkingArrow_cat\s+C\s+C1',
                    '@one_cat_oplax_functor_category WalkingArrow_cat C C1', text)
                assert closure_count == (5 if path.endswith('_comparison.lp') else 0)
                for name in ('diagram_family_at_func', 'diagram_family_transf', 'diagram_family_evaluation_func'):
                    text = text.replace('@' + name, '@diagram_oplax_' + name.removeprefix('diagram_'))
                if path.endswith('_comparison.lp'):
                    text, count = re.subn(r'@sym_func_func_transf\s+WalkingArrow_cat\s+B\s+C',
                        '@one_cat_family_oplax_exchange_map WalkingArrow_cat B C C1', text)
                    assert count == 2
                    text = text.replace('@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at')
                    text = text.replace('@one_cat_diagram_family_evaluation_comp_path',
                        '@one_cat_oplax_family_evaluation_comp_path')
                    text = text.replace('@one_cat_diagram_family_transf_reindex_path',
                        '@one_cat_oplax_family_transf_reindex_path')
                    text = text.replace('@one_cat_arrow_family_comparison_evidence',
                        '@one_cat_oplax_arrow_family_comparison_evidence')
                    text = text.replace('@one_cat_diagram_family_reconstruction_evidence',
                        '@one_cat_oplax_diagram_family_reconstruction_evidence')
                    anchor = 'require open emdash.emdash3_2_one_cat_arrow_diagrams;'
                    assert text.count(anchor) == 1
                    text = text.replace(anchor, anchor + '\nrequire open emdash.emdash3_2_one_cat_diagram_family_reflection;')
                    text = migrate_homology_boundary_paths(text)
                changes.append({'source': path, 'owner': 'ordinary whole native homology comparison profile',
                                'reason': 'Align native profiles and keep the original maps and endpoint inverse data; derive whole source-square inverse evidence before applying exchange, then use the native observation/reconstruction views',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_homology_adjunction_families.lp':
                old = text
                text, count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                                      'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == 24
                assert text.count('(@TerminalObject (Op_cat C) t)') == 1
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                                    '(@TerminalObject (TotalOp_cat C) t)')
                changes.append({'source': path, 'owner': 'native kernel/cokernel homology family',
                                'reason': 'Use the corrected native oplax diagram profile and original total-dual initial-object data throughout the existing K/unit/boundary/Q compositions; preserve P, Q, A, D and h',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/homology_adjunction_families.lp':
                old = text
                text, count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                                      'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == 50
                assert text.count('(@TerminalObject (Op_cat C) t)') == 11
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                                    '(@TerminalObject (TotalOp_cat C) t)')
                text = text.replace('@diagram_family_at_func', '@diagram_oplax_family_at_func')
                text = text.replace('@diagram_family_transf', '@diagram_oplax_family_transf')
                point_pattern = (r'@tapp0_fapp0 WalkingArrow_cat C\s+'
                                 r'\(@fapp0 B .*?\) (walking_arrow_src|walking_arrow_tgt)\n')
                text, point_count = re.subn(point_pattern,
                    lambda m: '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _ ' + m[1] + '\n',
                    text, flags=re.S)
                assert point_count == 2
                old_composition = '// Ambient H retains its compositor; arbitrary composition does not collapse.\nassertnot'
                assert text.count(old_composition) == 1
                text = text.replace(old_composition,
                    '// H is a default-strict functor, including for the retained lax input h.\nassert', 1)
                text = text.replace('// In an ordinary target the existing lax compositor supplies an equality.',
                    '// The existing ordinary path view observes the same strict composition.')
                changes.append({'source': path, 'owner': 'original native homology family reviewer',
                                'reason': 'Use actual oplax evaluation and encoded transformation components; retain all eleven observations, with the former lax-functor composition negative changed to the required strict-default positive',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_zero_cones.lp',
                        'emdash3_2_one_cat_zero_arrow_family_classification.lp',
                        'examples/one_cat_zero_arrow_family_classification.lp'):
                old = text
                expected_diagram_types = {
                    'emdash3_2_one_cat_zero_cones.lp': 2,
                    'emdash3_2_one_cat_zero_arrow_family_classification.lp': 124,
                    'examples/one_cat_zero_arrow_family_classification.lp': 49,
                }
                text, diagram_count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                                             'Functor_oplax_cat WalkingArrow_cat C', text)
                assert diagram_count == expected_diagram_types[path], (path, diagram_count)
                text, closure_count = re.subn(r'@one_cat_functor_category\s+WalkingArrow_cat\s+C\s+C1',
                    '@one_cat_oplax_functor_category WalkingArrow_cat C C1', text)
                assert closure_count == (5 if path == 'emdash3_2_one_cat_zero_arrow_family_classification.lp' else 0)
                if path == 'emdash3_2_one_cat_zero_cones.lp':
                    identity_pattern = 'rule @tapp1_fapp0 (Op_cat $K) _ _ _'
                    assert text.count(identity_pattern) == 1
                    text = text.replace(identity_pattern, 'rule @tapp1_fapp0 _ _ _ _', 1)
                    text = text.replace('(@id $K (Struct_sigma $a (Struct_sigma $d $h)))',
                                        '(@id _ (Struct_sigma $a (Struct_sigma $d $h)))', 1)
                    text = text.replace('// lhs-audit: keep 1,5,6 -- retain the qualified opposite-source, constructor-visible identity endpoints.',
                        '// The whole universal head fixes its total-opposite source; let that\n'
                        '// inferred category normalize before matching the visible identity.\n'
                        '// lhs-audit: keep 5,6 -- retain the constructor-visible identity endpoints.')
                if path.startswith('examples/'):
                    assert text.count('(d : τ (Functor WalkingArrow_cat C))') == 3
                    assert text.count('(@Transf WalkingArrow_cat C') == 3
                    text = text.replace('(d : τ (Functor WalkingArrow_cat C))',
                                        '(d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))')
                    text = text.replace('(@Transf WalkingArrow_cat C',
                                        '(Hom (Functor_oplax_cat WalkingArrow_cat C)')
                    text = text.replace('(@id (Op_cat\n  (@ZeroArrowCone_cat',
                                        '(@id (TotalOp_cat\n  (@ZeroArrowCone_cat')
                changes.append({'source': path, 'owner': 'ordinary native zero-arrow family classification',
                                'reason': 'Use the existing native oplax walking-diagram category and its OneCat closure; preserve the actual comma, arbitrary A/D/h, both chosen modification maps and inverse laws',
                                'diagramTypeCount': diagram_count, 'closureCount': closure_count,
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_commutative_algebra_category.lp':
                old = text
                old_family = '''    CommRing_cat Grpd_cat Cat_cat
    Path_cat_func comm_ring_carrier_func;'''
                assert text.count(old_family) == 1
                text = text.replace(old_family, '''    CommRing_cat Grpd_cat Cat_cart
    Path_cat_cart_func comm_ring_carrier_func;''', 1)
                changes.append({'source': path, 'owner': 'comm_ring_carrier_catd',
                                'reason': 'Use the whole Cartesian Path realization for the admitted carrier family, retaining the original ring-carrier functor and its whole Hom action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_commutative_algebra_presheaves.lp':
                old = text
                represented_section = '''(@fib_cov_transf
        (Op_cat K)
        (@comm_ring_psh_carrier_catd K O)
        U s)'''
                assert text.count(represented_section) == 1
                text = text.replace(represented_section, '''(@strict_transfor (Op_cat K) Cat_cart
        (@FibCov_source_catd (Op_cat K) U)
        (@comm_ring_psh_carrier_catd K O)
        (@fib_cov_transf
          (Op_cat K)
          (@comm_ring_psh_carrier_catd K O)
          U s))''', 1)
                changes.append({'source': path, 'owner': 'ring-presheaf total restriction map',
                                'reason': 'Use the existing ordinary inclusion of the canonical Cartesian FibCov section at the unchanged Sigma-map consumer',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/commutative_ring_presheaf_invertibility.lp':
                old = text
                family_type = '(Functor (Op_cat K) Cat_cat)'
                assert text.count(family_type) == 2
                text = text.replace(family_type, '(Functor (Op_cat K) Cat_cart)')
                changes.append({'source': path, 'owner': 'original ring-presheaf invertibility reviewer',
                                'reason': 'Observe the existing represented-family comparison in its actual Cat_cart coefficient; retain public Cat identities and every original assertion',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_functor_profiles.lp':
                text += '\n\n' + fragment('production_discrete_one_cat.lpfragment')
                changes.append({'source': path, 'owner': 'discrete target dimension weakening',
                                'reason': 'Derive the OneCat property from the existing discrete core Hom equivalence, consumed by strict fibre-coherence admission of the original WalkingEnd spiral'})
            if path == 'emdash3_2_walking_interval_comparison.lp':
                old = text
                component = '      _ Cat_cat _ _ _\n      walking_interval_seg_cross'
                assert text.count(component) == 1
                text = text.replace(component,
                    '      _ _ _ _ _\n      walking_interval_seg_cross')
                changes.append({'source': path, 'owner': 'walking-interval profunctor-cell component',
                                'reason': 'Infer the actual coefficient from the unique named cross owner instead of retaining the obsolete Cat_cat classifier discriminator',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_groupoidification_composition.lp':
                old = text
                former = '''  For arbitrary composable arrows f and g in C, the whole unit carries the
  ordinary normal-lax compositor extracted by the existing internal-action
  calculus.  Its codomain is Path_cat(Groupoidify(C)), so this cell is
  groupoidal.  The historical strict endpoint cuts may make its displayed
  endpoints convertible, but they do not reduce this explicit cell to an
  identity.'''
                assert text.count(former) == 1
                text = text.replace(former, '''  For arbitrary composable arrows f and g in C, the unit uses the public
  strict-functor default. Its compositor is still extracted by the existing
  internal-action calculus; its endpoints agree and the extracted cell
  computes to identity. This does not impose strict naturality on arbitrary
  transformations.''')
                changes.append({'source': path, 'owner': 'groupoidification compositor contract comment',
                                'reason': 'Describe the restored strict default and retained intrinsic extraction; all declarations and bodies are unchanged',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_triangular_binary_products.lp':
                old = text
                assert text.count('Cat_cat') == 9
                assert text.count('Product_cat_func') == 1
                text = text.replace('Cat_cat', 'Cat_cart')
                text = text.replace('Product_cat_func', 'Product_cat_coeff_func')
                component = '      _ Cat_cart _ _ $X\n      (@binary_products_pair_transf'
                assert text.count(component) == 1
                text = text.replace(component,
                    '      _ _ _ _ $X\n      (@binary_products_pair_transf')
                changes.append({'source': path, 'owner': 'triangular product represented pairing families',
                                'reason': 'Use the existing Cat_cart product constructor for the two canonical Hom families and infer the component coefficient; retain the original pairing, inverse and triangular computation owners',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/triangular_binary_products.lp':
                old = text
                assert text.count('Cat_cat') == 3
                assert text.count('Functor_cat') == 1
                text = text.replace('Cat_cat', 'Cat_cart')
                text = text.replace('Functor_cat', 'Functor_cart_cat')
                changes.append({'source': path, 'owner': 'original whole pairing-action reviewer',
                                'reason': 'Read the existing next Hom action in its actual Cat_cart coefficient and Cartesian mapping Hom; preserve all original computations and negatives',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_finite_limits.lp':
                old = text
                assert text.count('Cat_cat') == 1
                text = text.replace('Cat_cat', 'Cat_cart')
                changes.append({'source': path, 'owner': 'weighted binary-product projection cell',
                                'reason': 'Evaluate the existing Prof_cell_apply result in its actual Cat_cart coefficient; preserve the original universal datum and projection body',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            pullback_views = {
                'emdash3_2_pullbacks.lp': 33,
                'examples/pullbacks.lp': 1,
            }
            if path in pullback_views:
                old = text
                starts = [m.start() for m in re.finditer(r'\(@hom_con_int_postcomp_func\b', text)]
                assert len(starts) == pullback_views[path]
                # The old consumers take an ambient displayed map. Its
                # canonical represented producer now has the strict carrier.
                # Keep the existing inclusion visible in runtime patterns.
                for start in reversed(starts):
                    depth = 0
                    for end in range(start, len(text)):
                        depth += (text[end] == '(') - (text[end] == ')')
                        if depth == 0:
                            break
                    assert depth == 0
                    term = text[start:end + 1]
                    text = text[:start] + '(@strict_transfor _ _ _ _ ' + term + ')' + text[end + 1:]
                if path == 'emdash3_2_pullbacks.lp':
                    sigma_family = '''symbol SliceSigma_catd
  (C : Cat)
  : τ (Catd C)
≔ @CommaFib_catd C C (@id_func C);'''
                    assert text.count(sigma_family) == 1
                    text = text.replace(sigma_family, '''// Fibrewise dimension-one transpose reverses the base two-cell action.
// This is the original restriction-opposite slice, not the opposite triangle
// convention of the core CommaFib family.
symbol SliceSigma_catd
  (C : Cat)
  : τ (Catd (CoAt2_cat C))
≔ @comp_cat_fapp0
    (CoAt2_cat C) (CoAt2_cat Cat_cart) Cat_cart op
    (@CoAt2_func C Cat_cart (@arrow_into_catd C));''')
                    assert text.count('C Cat_cat\n    (@SliceSigma_catd C)') == 1
                    text = text.replace('C Cat_cat\n    (@SliceSigma_catd C)',
                        '(CoAt2_cat C) Cat_cart\n    (@SliceSigma_catd C)')
                    assert text.count('rule @fapp0 _ Cat_cat') == 1
                    text = text.replace('rule @fapp0 _ Cat_cat', 'rule @fapp0 _ _')
                    assert text.count('(Op_cat $C) Cat_cat') == 1
                    text = text.replace('(Op_cat $C) Cat_cat', '(Op_cat $C) _')
                    assert text.count('C (Catd_cat (Op_cat C))') == 2
                    text = text.replace('C (Catd_cat (Op_cat C))',
                        'C (Functor_cart_cat (Op_cat C) Cat_cart)')
                    for owner in ('slice_base_change_gamma', 'slice_base_change_phi'):
                        marker = 'injective symbol ' + owner + '\n'
                        assert text.count(marker) == 1
                        first = text.index(marker)
                        last = text.index(';', first) + 1
                        block = text[first:last]
                        homs = [m.start() for m in re.finditer(r'\(Hom\s', block)]
                        assert len(homs) == 3
                        for start in reversed(homs):
                            depth = 0
                            for end in range(start, len(block)):
                                depth += (block[end] == '(') - (block[end] == ')')
                                if depth == 0:
                                    break
                            assert depth == 0
                            term = block[start:end + 1].replace('(Hom', '(Hom_cat', 1)
                            block = block[:start] + '(Obj ' + term + ')' + block[end + 1:]
                        text = text[:first] + '// Canonical Hom types expose the opposite endpoints before inversion.\n' + block + text[last:]
                    left_hom = '''(Hom_cat
      (@Sigma_cat (Op_cat C) (@hom_con C Y C (@id Cat_cat C)))
      b (@slice_sigma_obj C X Y f a))'''
                    right_hom = '''(Hom_cat
      (@Sigma_cat (Op_cat C) (@hom_con C X C (@id Cat_cat C)))
      (@slice_base_change_obj C PB X Y f b) a)'''
                    for owner, source_hom, target_hom in (
                        ('slice_base_change_transpose_func', left_hom, right_hom),
                        ('slice_base_change_untranspose_func', right_hom, left_hom),
                        ('slice_base_change_transpose_semantic_func', left_hom, right_hom),
                        ('slice_base_change_untranspose_semantic_func', right_hom, left_hom),
                    ):
                        marker = ('symbol ' if '_semantic_' in owner else 'injective symbol ') + owner + '\n'
                        assert text.count(marker) == 1
                        first = text.index(marker)
                        last = text.index(';', first) + 1
                        block = text[first:last]
                        assert block.count(': τ (Functor\n') == 1
                        body_suffix = '\n≔' + block.split('≔', 1)[1] if '≔' in block else ';'
                        block = block.split(': τ (Functor\n', 1)[0] \
                            + ': τ (Functor\n    ' + source_hom + '\n    ' + target_hom + ')' + body_suffix
                        text = text[:first] + '// Keep both whole mate endpoints in their canonical total-Hom form.\n' + block + text[last:]
                else:
                    assert text.count('C Cat_cat') == 1
                    assert text.count('(Op_cat C) Cat_cat') == 3
                    assert text.count('Functor_cat') == 1
                    text = text.replace('C Cat_cat', '(CoAt2_cat C) Cat_cart')
                    text = text.replace('(Op_cat C) Cat_cat', '(Op_cat C) Cat_cart')
                    text = text.replace('Functor_cat', 'Functor_cart_cat')
                changes.append({'source': path, 'owner': 'canonical slice-family and represented Sigma-map views',
                                'reason': 'Preserve the restriction-opposite slice via its CoAt2-based whole family, use the existing ambient view of canonical strict represented maps, and canonicalize conversion-sensitive Hom types while retaining the Sigma-map, triangle and mate operations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_slice_dependent_products.lp':
                old = text
                declaration = '''injective symbol SliceDependentProduct_catd
  [C : Cat]
  [PB : τ (@PullbackStructure C)]
  (DP : τ (@DependentProductStructure C PB))
  : τ (Catd C);'''
                assert text.count(declaration) == 1
                text = text.replace(declaration,
                    '// Right-adjoint variance returns the same CoAt2(C) base as Sigma.\n'
                    + declaration.replace('(Catd C)', '(Catd (CoAt2_cat C))'))
                assert text.count('rule @fapp0 _ Cat_cat') == 1
                assert text.count('rule @fapp1_fapp0 _ Cat_cat') == 1
                text = text.replace('rule @fapp0 _ Cat_cat', 'rule @fapp0 _ _')
                text = text.replace('rule @fapp1_fapp0 _ Cat_cat', 'rule @fapp1_fapp0 _ _')
                changes.append({'source': path, 'owner': 'dependent-product family projections',
                                'reason': 'Use the CoAt2(C) whole-family base matching right-adjoint variance and infer its Cat_cart coefficient; retain the original selected dependent-product action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/slice_dependent_products.lp':
                old = text
                assert text.count('C Cat_cat') == 3
                assert text.count('Functor_cat') == 1
                text = text.replace('C Cat_cat', '(CoAt2_cat C) Cat_cart')
                text = text.replace('Functor_cat', 'Functor_cart_cat')
                hom_source = '(Hom_cat C X Y)\n      (Functor_cart_cat (@Slice_cat C X) (@Slice_cat C Y))'
                assert text.count(hom_source) == 1
                text = text.replace(hom_source, hom_source.replace('(Hom_cat C X Y)',
                    '(Hom_cat (CoAt2_cat C) X Y)'))
                changes.append({'source': path, 'owner': 'original dependent-product family reviewer',
                                'reason': 'Observe the whole family over CoAt2(C) and its next Hom in Cat_cart; preserve all original assertions',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_monads.lp', 'examples/monads_comonads.lp'):
                old = text
                expected = (26, 23, 8) if path == 'emdash3_2_monads.lp' else (5, 3, 1)
                assert tuple(text.count(s) for s in ('Op_cat', 'Op_func', 'Op_transf')) == expected
                for name in ('Op_cat', 'Op_func', 'Op_transf'):
                    text = re.sub(r'\b' + name + r'\b', 'Total' + name, text)
                if path == 'emdash3_2_monads.lp':
                    body0 = '''≔ @kleisli_extend_func
    (TotalOp_cat A)
    (@TotalOp_func A A D)
    C
    Y X;'''
                    assert text.count(body0) == 1
                    text = text.replace(body0, '''≔ @TotalOp_func
    (TotalOp_cat (@Hom_cat A (@fapp0 A A D X) Y))
    (TotalOp_cat (@Hom_cat A (@fapp0 A A D X) (@fapp0 A A D Y)))
    (@kleisli_extend_func
      (TotalOp_cat A) (@TotalOp_func A A D) C Y X);''')
                    text = text.replace('A comonad on A is classified transparently as a monad on A^op.',
                        'A comonad on A is classified transparently as a monad on its total opposite.\n'
                        '  Total duality preserves the ambient lax transformation profile.')
                    text = text.replace('// A comonad on A is transparently a monad on A^op.',
                        '// A comonad on A is transparently a monad on TotalOp_cat(A).\n'
                        '// The historical Op_monad/Op_comonad names remain readability views.')
                    text = text.replace('Whole coextension is transparently endpoint-swapped monadic extension in\n  A^op.',
                        'Whole coextension applies total duality to endpoint-swapped monadic\n'
                        '  extension in TotalOp_cat(A), restoring the original Hom categories.\n ')
                    text = text.replace('Canonical Op terms', 'Canonical total-duality terms')
                    text = text.replace('after Op normalization', 'after total-duality normalization')
                    text = text.replace('whole Op fold', 'whole total-duality fold')
                    text = text.replace('Op-derived term', 'total-duality-derived term')
                    for observation in ('unit_monad_transf', 'mult_monad_transf'):
                        pattern = '(@' + observation + ' _ (@TotalOp_func $A $A $D) $C)'
                        assert text.count(pattern) == 1
                        text = text.replace(pattern,
                            '(@' + observation + ' _ (@CoAbove2_func _ _ (@Op_func $A $A $D)) $C)')
                    pattern = '_ (@TotalOp_func $A $A $D) $C $Y $X $f'
                    assert text.count(pattern) == 1
                    text = text.replace(pattern,
                        '_ (@CoAbove2_func _ _ (@Op_func $A $A $D)) $C $Y $X $f')
                    text = text.replace('TotalOp_func(D) avoids repeated reducible category and endpoint guards.',
                        'the native CoAbove2_func(Op_func(D)) constructors avoids a reducible\n'
                        '  TotalOp_func alias in the pattern and keeps category/endpoint guards inferred.')
                    marker = '// Direct opposite unit/multiplication components fold toward the stable'
                    assert text.count(marker) == 1
                    text = text.replace(marker,
                        '// TotalOp_func is an alias; its runtime pattern uses the native R(T(-)) heads.\n' + marker)
                    for observation in ('counit_comonad_transf', 'comult_comonad_transf'):
                        rule0 = 'rule @' + observation + '\n      _ _\n      (@adjunction_comonad $R $L $F $G $J)'
                        assert text.count(rule0) == 1
                        text = text.replace(rule0,
                            '// lhs-audit: keep 2 -- total duality normalizes the witness index;\n'
                            '// retain its actual FG endofunctor for subject reduction.\n'
                            'rule @' + observation + '\n'
                            '      _ (@comp_fapp0 Cat_cat $L $R $L $F $G)\n'
                            '      (@adjunction_comonad $R $L $F $G $J)')
                else:
                    text = text.replace('endpoint-swapped primary monadic whole owner.',
                        'total dual of the endpoint-swapped primary monadic whole owner.')
                    for observation in ('counit_comonad_transf', 'comult_comonad_transf'):
                        old_view = observation + ' (adjunction_comonad J)'
                        assert text.count(old_view) == 1
                        text = text.replace(old_view, '@' + observation
                            + ' L (@comp_cat_fapp0 L R L F G) (@adjunction_comonad R L F G J)')
                    marker = '// The existing adjunction constructs both exact structural instances.'
                    assert text.count(marker) == 1
                    text = text.replace(marker, '''// Object carriers agree, but the untransposed whole dual extension has
// total-opposite Hom categories. The outer TotalOp_func is required.
assertnot [A : Cat] [D : τ (Functor A A)]
  (C : τ (@Comonad A D)) (X Y : τ (Obj A)) ⊢
  @kleisli_extend_func (TotalOp_cat A) (@TotalOp_func A A D) C Y X
  : τ (Functor
      (Hom_cat A (@fapp0 A A D X) Y)
      (Hom_cat A (@fapp0 A A D X) (@fapp0 A A D Y)));

''' + marker)
                changes.append({'source': path, 'owner': 'total-duality monad/comonad computation',
                                'reason': 'Use the existing total-duality action on ambient lax transformations and restore whole coextension variance with TotalOp_func; preserve the original primary operations and witness data',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/generic_groupoidification.lp':
                old = text
                former = '''// The explicit compositor has distinct endpoints, so comparison with an
// identity is no longer a homogeneous judgment.
assertnot [C : Cat]'''
                assert text.count(former) == 1
                text = text.replace(former, '''// The strict-functor default identifies the composition endpoints.
assert [C : Cat]''')
                marker = '// Source and target parameters are not erased by the generic facade.'
                assert text.count(marker) == 1
                text = text.replace(marker, '''// The native extracted compositor itself has the required identity value.
assert [C : Cat] [x y z : τ (Obj C)]
  (g : τ (Hom C y z)) (f : τ (Hom C x y)) ⊢
  @groupoidify_unit_compositor C x y z g f
  ≡ @id
      (Hom_cat (Path_cat (Groupoidify C))
        (@fapp0 C (Path_cat (Groupoidify C)) (@groupoidify_unit_func C) x)
        (@fapp0 C (Path_cat (Groupoidify C)) (@groupoidify_unit_func C) z))
      (@fapp0 _ _ (@groupoidify_unit_compositor_lhs_func C x y z g) f);

''' + marker)
                changes.append({'source': path, 'owner': 'original groupoidification strict-default reviewer',
                                'reason': 'Replace the obsolete lax composition-endpoint negative by its strict positive and check the extracted identity cell; preserve the original parameter and nonconstructor negatives',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_direct_cover_sheafification.lp':
                old = text
                # Every literal Cat_cat in this specialized owner is the
                # presheaf value coefficient, including the supplied generic
                # capability's V parameter; none is a composition universe.
                assert text.count('Cat_cat') == 59
                text = text.replace('Cat_cat', 'Cat_cart')
                assert text.count('symbol direct_cover_sheafification_reflected_object\n') == 1
                reflected_start = text.index('symbol direct_cover_sheafification_reflected_object\n')
                reflected_end = text.index(';', reflected_start) + 1
                reflected = text[reflected_start:reflected_end]
                assert reflected.count('(@Psh_cat K)') == 2
                reflected = reflected.replace('(@Psh_cat K)',
                    '(@Functor_cat (Op_cat K) Cat_cart)')
                for selected, generic in (
                    ('direct_cover_sheafification_func', 'sheaf_adjunction_sheafify'),
                    ('cat_valued_sheaf_include_psh_func', 'sheaf_adjunction_include'),
                ):
                    old_selected = '(@' + selected + ' K T)'
                    assert reflected.count(old_selected) == 1
                    reflected = reflected.replace(old_selected,
                        '(@' + generic + ' K T Cat_cart\n'
                        '      (@direct_cover_sheafification_adjunction_data K T))')
                text = text[:reflected_start] + reflected + text[reflected_end:]
                assert text.count('symbol direct_cover_sheafification_counit_at\n') == 1
                counit_start = text.index('symbol direct_cover_sheafification_counit_at\n')
                counit_end = text.index(';', counit_start) + 1
                counit = text[counit_start:counit_end]
                assert counit.count('≔ @tapp0_fapp0') == 1
                counit = counit.split('≔', 1)[0] + '''≔ @sheaf_adjunction_counit_at K T Cat_cart
    (@direct_cover_sheafification_adjunction_data K T) Y;'''
                text = text[:counit_start] + counit + text[counit_end:]
                for indent in (6, 4):
                    padding = ' ' * indent
                    expanded = '(' + '@sheaf_adjunction_intro\n' + padding + '  K T Cat_cart\n' \
                        + padding + '  (@cat_valued_sheaf_include_psh_func K T)\n' \
                        + padding + '  (@direct_cover_sheafification_func K T)\n' \
                        + padding + '  (@direct_cover_sheafification_adjunction K T))'
                    assert text.count(expanded) == 1
                    text = text.replace(expanded, '(@direct_cover_sheafification_adjunction_data K T)')
                changes.append({'source': path, 'owner': 'direct-cover sheafification coefficient specialization',
                                'reason': 'Use the actual Cat_cart coefficient and the exact existing generic package projections at final reflector endpoints; preserve the chosen functors, inverse data, cancellation proofs and all original rules',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_checks.lp':
                facade_start = 'assert [K : Cat] ⊢\n  @eq_refl Cat_grpd (Catd_cat K)'
                hom_start = 'assert [A B : Cat] (F : τ (Functor B A)) (W : τ (Obj A)) (y : τ (Obj B)) ⊢'
                hom_end = '// Hom-action functoriality joins for postcomposition.'
                assert text.count(facade_start) == text.count(hom_start) == text.count(hom_end) == 1
                first, middle, last = text.index(facade_start), text.index(hom_start), text.index(hom_end)
                old = text[first:last]
                facade = text[first:middle]
                assert facade.count('Cat_cat') == 5
                facade = facade.replace('Cat_cat', 'Cat_cart')
                hom = text[middle:last]
                assert hom.count('Functor_cat') == 10
                hom = hom.replace('Functor_cat', 'Functor_cart_cat')
                for pattern, replacement, count in (
                    ('(Catd_cat B)', '(Functor_cart_cat B Cat_cart)', 2),
                    ('(@Catd_cat B)', '(Functor_cart_cat B Cat_cart)', 2),
                    ('(@Catd_cat (Op_cat B))', '(Functor_cart_cat (Op_cat B) Cat_cart)', 8),
                ):
                    assert hom.count(pattern) == count
                    hom = hom.replace(pattern, replacement)
                hom = re.sub(r'\bB(\s+)Cat_cat', r'B\1Cat_cart', hom)
                hom = re.sub(r'\(Op_cat B\)(\s+)Cat_cat', r'(Op_cat B)\1Cat_cart', hom)
                hom = re.sub(r'(_\s+)Cat_cat(\s+\(@hom_con\b)', r'\1Cat_cart\2', hom)
                for name in ('hom_int_precomp_func', 'hom_con_int_postcomp_func'):
                    starts = [m.start() for m in re.finditer(r'\(@' + name + r'\b', hom)]
                    assert len(starts) == 5
                    for start in reversed(starts):
                        depth = 0
                        for end in range(start, len(hom)):
                            depth += (hom[end] == '(') - (hom[end] == ')')
                            if depth == 0:
                                break
                        assert depth == 0
                        term = hom[start:end + 1]
                        hom = hom[:start] + '(@strict_transfor _ _ _ _ ' + term + ')' + hom[end + 1:]
                rep_view = '≡ @hom_int_precomp_func Z Z (@id_func Z) y x p;'
                assert hom.count(rep_view) == 1
                hom = hom.replace(rep_view,
                    '≡ @strict_transfor _ _ _ _ (@hom_int_precomp_func Z Z (@id_func Z) y x p);')
                replacement = facade + hom
                text = text[:first] + replacement + text[last:]
                changes.append({'source': path + '/family-and-represented-hom',
                                'owner': 'original family classifiers and whole represented-Hom ladder',
                                'reason': 'Use the actual Cat_cart family coefficient, Cartesian canonical Hom classifiers and existing ambient transfor views; keep public Hom(Cat)=Functor_cat and all original observations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
                marker = 'symbol hom_postcomp_opfunc_general_tele_visible_check\n'
                assert text.count(marker) == 1
                first = text.index(marker)
                last = text.index(';', first) + 1
                old = text[first:last]
                assert old.count('Functor_cat') == 1
                replacement = old.replace('Functor_cat', 'Functor_cart_cat')
                text = text[:first] + replacement + text[last:]
                changes.append({'source': path + '/opposite-hom-telescope',
                                'owner': 'original opposite postcomposition telescope type',
                                'reason': 'Retain its complete source/action comparison and use the actual Cartesian mapping category of the canonical Hom telescope',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
                composition_changes = []
                root_count, generic_tele_count, view_count, two_endpoint_count = 0, 0, 0, 0
                for match in reversed(list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', text, re.S))):
                    old = match.group()
                    block = old
                    composition_root = 'comp_cat_con_func_func' in block or 'comp_cat_cov_func_func' in block
                    generic_tele = bool(re.search(r'@fapp1_(?:func|fapp0)\b', block)) and (
                        '(@hom_postcomp_tele_func' in block or '(@hom_precomp_along_tele_func' in block)
                    if composition_root:
                        root_count += 1
                        block = block.replace('Functor_cat', 'Functor_cart_cat').replace('Cat_cat', 'Cat_cart')
                        block = block.replace('(Transf G H)', '(@StrictTransfor X Y G H)')
                        block = block.replace('(Transf F K)', '(@StrictTransfor X Y F K)')
                        block = block.replace('≡ @comp_cat_con_func X Y Z F;',
                            '≡ @comp_cat_con_cart_func X Y Z F;')
                    elif generic_tele:
                        generic_tele_count += 1
                        block = block.replace('Functor_cat', 'Functor_cart_cat')
                    elif '@Hom_tele_func' in block and '@Product_map_func' in block:
                        two_endpoint_count += 1
                        block = block.replace('Functor_cat', 'Functor_cart_cat')
                        block = re.sub(r'(@comp_prod_func\s+)Cat_cat', r'\1Cat_cart', block)
                    if '⊢' in block and '≡' in block:
                        telescope, equation = block.split('⊢', 1)
                        left, right = equation.rsplit('≡', 1)
                        left_head = left.strip().split()[0]
                        right_head = right.strip().split()[0]
                        if left_head in ('@fapp1_fapp0', 'fapp0', '@fapp0',
                                         '@hom_postcomp_tele_fapp1_fapp0', '@hom_precomp_along_tele_fapp1_fapp0') \
                            and right_head in ('@comp_cat_cov_func_func_transf', '@comp_cat_con_func_func_transf',
                                               '@hom_postcomp_tele_transf', '@hom_precomp_along_tele_transf'):
                            view_count += 1
                            block = telescope + '⊢\n  @strict_transfor _ _ _ _ (' + left.strip() + ')\n  ≡' + right
                    if block != old:
                        text = text[:match.start()] + block + text[match.end():]
                        composition_changes.append({'oldSha256': sha(old), 'newSha256': sha(block)})
                assert root_count == 11, root_count
                assert generic_tele_count == 4, generic_tele_count
                assert view_count == 8, view_count
                assert two_endpoint_count == 2, two_endpoint_count
                changes.append({'source': path + '/composition-parameter-profiles',
                                'owner': 'whole composition roots and canonical Hom telescope views',
                                'reason': 'Match the existing Cartesian whole-parameter roots and use their ambient transfor projections, while retaining raw fixed-whiskering and ordinary Cat-valued diagram tests',
                                'assertions': list(reversed(composition_changes))})
                marker = '// catalog-area: Internal groupoidality and structured J'
                end_marker = '// Phase 9 discrete-category core and homwise adequacy.'
                assert text.count(marker) == text.count(end_marker) == 1
                start, end = text.index(marker), text.index(end_marker)
                old = text[start:end]
                section = old
                assert section.count('Fibre_cat (@strict_functor C Cat_cat D)') == 4
                section = section.replace('Fibre_cat (@strict_functor C Cat_cat D)',
                    '@fapp0 C Cat_cat (@strict_functor C Cat_cat D)')
                assert section.count('≡ @fib_cov_transf C D x u;') == 1
                section = section.replace('≡ @fib_cov_transf C D x u;',
                    '≡ @strict_transfor _ _ _ _ (@fib_cov_transf C D x u);')
                assert section.count('(@fib_cov_transf (Path_cat A) D x u)') == 3
                section = section.replace('(@fib_cov_transf (Path_cat A) D x u)',
                    '(@strict_transfor _ _ _ _ (@fib_cov_transf (Path_cat A) D x u))')
                split = section.index('// The path-category identity join')
                section = section[:split] + section[split:].replace('Cat_cat', 'Cat_cart')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/internal-groupoidality',
                                'owner': 'original groupoidal transport and structured-J diagnostics',
                                'reason': 'Keep the raw Cat-valued diagram theorem at its object action, and observe Catd transport/fibre covariance through the actual coefficient and ambient inclusion; preserve every original assertion',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                marker = 'assert [K : Cat] (E D : τ (Catd K)) ⊢\n  @eq_refl Cat_grpd (Hom_cat (Catd_cat K) E D)'
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index(';', start) + 1) + 1
                old = text[start:end]
                assert old.count('Cat_cat') == 3
                text = text[:start] + old.replace('Cat_cat', 'Cat_cart') + text[end:]
                changes.append({'source': path + '/displayed-mapping-facade',
                                'owner': 'original Catd/Functord versus ordinary mapping category observations',
                                'reason': 'Observe the retained ambient lax Functord at its actual Cat_cart coefficient',
                                'oldBodySha256': sha(old)})
                old = '(@fapp1_fapp0 (Op_cat A) (@Catd_cat B) (@hom_int A B F) y x p)'
                assert text.count(old) == 1
                text = text.replace(old,
                    '(@strict_transfor _ _ _ _ (@fapp1_fapp0 (Op_cat A)\n'
                    '      (Functor_cart_cat B Cat_cart) (@hom_int A B F) y x p))')
                old = '(@Const_transf K A x y p)'
                assert text.count(old) == 3
                text = text.replace(old, '(@strict_transfor K A _ _ ' + old + ')')
                product_start = '// Transparent fibrewise product: no Product_catd owner is introduced.'
                product_end = '// catalog-area: Constant-domain displayed evaluation'
                assert text.count(product_start) == text.count(product_end) == 1
                start, end = text.index(product_start), text.index(product_end)
                old = text[start:end]
                # The negative about the original raw curried product remains
                # at that ambient interface; it is not the coefficient root.
                raw_start = old.index('// The shared base arrow is a real discriminator:')
                raw_end = old.index('// An opaque family is not identified', raw_start)
                raw_product_negative = old[raw_start:raw_end]
                section = old[:raw_start] + 'RAW_PRODUCT_NEGATIVE_PLACEHOLDER\n' + old[raw_end:]
                section = section.replace('Cat_cat', 'Cat_cart')
                section = section.replace('Product_cat_func', 'Product_cat_coeff_func')
                section = section.replace('@comp_cat_con_func', '@comp_cat_con_cart_func')
                section = re.sub(r'Functor_cat(\s+\((?:Fibre_cat|Product_cat)\b)',
                                 r'Functor_cart_cat\1', section)
                for helper, source, target in (
                    ('Product_projL_funcd_higher_check',
                     '(Fibre_cat (@Product_catd_transparent_check K B C) x)', '(Fibre_cat B y)'),
                    ('Product_projR_funcd_higher_check',
                     '(Fibre_cat (@Product_catd_transparent_check K B C) x)', '(Fibre_cat C y)'),
                    ('Product_pair_funcd_higher_check',
                     '(Fibre_cat E x)', '(Fibre_cat (@Product_catd_transparent_check K B C) y)'),
                ):
                    a = section.index('symbol ' + helper + '\n')
                    b = section.index('≔', a)
                    signature = section[a:b]
                    assert signature.count(': τ (Transf\n') == 1
                    signature = signature.replace(': τ (Transf\n',
                        ': τ (Obj (Hom_cat\n      (Functor_cart_cat ' + source + ' ' + target + ')\n')
                    signature = signature.rstrip() + ')\n'
                    section = section[:a] + signature + section[b:]
                section = section.replace('RAW_PRODUCT_NEGATIVE_PLACEHOLDER\n', raw_product_negative)
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/displayed-products',
                                'owner': 'original transparent product, displayed projections/pairing and higher-action reviewers',
                                'reason': 'Use the existing coefficient product and its Cartesian fibre-Homs; retain general lax FF/GG, all whole and higher projections, and the raw-product noncollapse control',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                eval_start = '// catalog-area: Constant-domain displayed evaluation'
                eval_end = '// catalog-area: Displayed dependent chain'
                assert text.count(eval_start) == text.count(eval_end) == 1
                start, end = text.index(eval_start), text.index(eval_end)
                old = text[start:end]
                assert old.count('Cat_cat') == 17 and old.count('(@Eval_funcd K A B)') == 8
                section = old.replace('Cat_cat', 'Cat_cart')
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', section)
                section = section.replace('Product_cat_func', 'Product_cat_coeff_func')
                section = section.replace('(@Eval_funcd K A B)',
                    '(@strict_transfor _ _ _ _ (@Eval_funcd K A B))')
                a = section.index('symbol Displayed_eval_higher_check')
                b = section.index('≔', a)
                signature = section[a:b]
                assert signature.count(': τ (Transf\n') == 1
                signature = signature.replace(': τ (Transf\n',
                    ': τ (Obj (Hom_cat\n'
                    '      (Functor_cart_cat (Fibre_cat (@Displayed_eval_source_check K A B) x)\n'
                    '        (Fibre_cat B y))\n')
                section = section[:a] + signature.rstrip() + ')\n' + section[b:]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/displayed-evaluation',
                                'owner': 'original constant-domain displayed evaluation and its direct varying/fixed consumers',
                                'reason': 'Retain the original transparent product and evaluation composites at the actual coefficient, observing the existing Cartesian evaluator through its ambient inclusion; canonicalize the next-Hom type',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: Displayed dependent chain')
                end = text.index('// catalog-area: auto', start)
                old = text[start:end]
                assert old.count('Cat_cat') == 3
                section = old.replace('Cat_cat', 'Cat_cart')
                starts = [m.start() for m in re.finditer(r'\(@tdapp0_fapp0\b', section)]
                assert len(starts) == 2
                for first in reversed(starts):
                    depth = 0
                    for last in range(first, len(section)):
                        depth += (section[last] == '(') - (section[last] == ')')
                        if depth == 0:
                            break
                    assert depth == 0
                    term = section[first:last + 1]
                    section = section[:first] + '(@strict_transfor _ _ _ _ ' + term + ')' + section[last + 1:]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/displayed-dependent-chain',
                                'owner': 'original dependent variables and recursively weakened Sigma-section consumers',
                                'reason': 'Retain every original construction and arbitrary lax displayed map; correct the coefficient and observe its strict fibre modifications through the existing ambient view',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: auto', text.index('// catalog-area: Displayed dependent chain'))
                end = text.index('// Indexed adjunction triangles, opposite, and operation-trust boundary.', start)
                old = text[start:end]
                section = old
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '@Eval_func' in block or 'uncurry_func' in block:
                        block = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', block)
                    if '(eta : τ (Transf F G))' in block and '@Eval_func' in block:
                        block = block.replace('(eta : τ (Transf F G))', '(eta : τ (@StrictTransfor A B F G))')
                        block = block.replace('@tapp1_fapp0 A B F G x y eta p',
                            '@tapp1_fapp0 A B F G x y (@strict_transfor A B F G eta) p')
                    if '@Eval_at_func' in block:
                        block = block.replace('≡ @fapp0_func A B x;',
                            '≡ @comp_cat_fapp0 (Functor_cart_cat A B) (Functor_cat A B) B\n'
                            '      (@fapp0_func A B x) (Functor_cart_include A B);')
                    if 'uncurry_func' in block:
                        block = re.sub(r'(@hom_postcomp_fapp0\s+)Cat_cat(\s+)Cat_cat(\s+\(@id Cat_cat )Cat_cat',
                            r'\1Cat_cart\2Cat_cart\3Cat_cart', block)
                    section = section[:match.start()] + block + section[match.end():]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/ordinary-cartesian-evaluation',
                                'owner': 'original joint evaluator, fixed evaluation and curry/uncurry observations',
                                'reason': 'State the actual Cartesian joint interface and its existing inclusion into ambient fixed evaluation; retain raw fixed-evaluator action on lax transfors',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Indexed adjunction triangles, opposite, and operation-trust boundary.')
                end = text.index('// Monad/Kleisli computation and opposite-derived comonads.', start)
                old = text[start:end]
                section = re.sub(r'\bOp_(cat|func|transf)\b', r'TotalOp_\1', old)
                marker = '// Stable capped action projects the already-existing whole Op-transfor beta.'
                a = section.index(marker)
                b = section.index('// Involution still fires', a)
                former = section[a:b]
                expected = '(@tapp1_fapp0 A B F G x y eta p));'
                assert former.count(expected) == 1
                corrected = former.replace(marker,
                    '// Total duality exchanges the naturality boundaries; its conventional\n'
                    '// pre/right action reads the original post/left endpoint.')
                corrected = corrected.replace(expected,
                    '(@fapp0 (Hom_cat A x y)\n'
                    '        (Hom_cat B (@fapp0 A B F x) (@fapp0 A B G y))\n'
                    '        (@tapp1_post_endpoint_func A B F G eta x y) p));')
                negative = former.replace(marker,
                    '// The old middle is not identified with that boundary for a general lax eta.')
                negative = negative.replace('assert [A B : Cat]', 'assertnot [A B : Cat]', 1)
                section = section[:a] + corrected + negative + section[b:]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/adjunction-total-duality',
                                'owner': 'original indexed adjunction and ambient transfor duality observations',
                                'reason': 'Use the existing total reversal on general lax unit/counit transformations and its actual post/left off-diagonal boundary; retain triangle computations and adjunction data, and add the old-middle noncollapse control',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Monad/Kleisli computation and opposite-derived comonads.')
                end = text.index('// catalog-area: auto', start)
                old = text[start:end]
                section = re.sub(r'\bOp_(cat|func|transf)\b', r'TotalOp_\1', old)
                whole_dual = '(@kleisli_extend_func\n        (TotalOp_cat A) (@TotalOp_func A A D) C Y X)'
                assert section.count(whole_dual) == 1
                section = section.replace(whole_dual,
                    '(@TotalOp_func\n'
                    '        (TotalOp_cat (Hom_cat A (@fapp0 A A D X) Y))\n'
                    '        (TotalOp_cat (Hom_cat A (@fapp0 A A D X) (@fapp0 A A D Y)))\n'
                    '        (@kleisli_extend_func\n'
                    '          (TotalOp_cat A) (@TotalOp_func A A D) C Y X))')
                for observation in ('counit_comonad_transf', 'comult_comonad_transf'):
                    old_view = observation + ' (adjunction_comonad J)'
                    assert section.count(old_view) == 1
                    section = section.replace(old_view, '@' + observation
                        + ' L (@comp_cat_fapp0 L R L F G) (@adjunction_comonad R L F G J)')
                section = section.replace('Monad evidence is definitionally Comonad evidence after one opposite.',
                    'Monad evidence is definitionally Comonad evidence after total reversal.')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/monad-comonad-observations',
                                'owner': 'original monad, Kleisli, dual comonad and adjunction-induced computation diagnostics',
                                'reason': 'Match the already qualified total-duality owner, restore the whole coextension Hom categories with TotalOp_func, and retain the two actual FG indices; preserve every original assertion',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: auto', text.index('// Monad/Kleisli computation and opposite-derived comonads.'))
                end = text.index('// Pre-configured four-cell interchange', start)
                old = text[start:end]
                hom_start = old.index('assert [A B : Cat] (F : τ (Functor A B)) (X : τ (Obj A)) ⊢')
                action_start = old.index('assertnot [A B : Cat] (F G : τ (Functor A B))', hom_start)
                prof = old[:hom_start]
                hom = old[hom_start:action_start]
                assert prof.count('Cat_cat') == 5
                assert hom.count('Cat_cat') == 5 and hom.count('@hom_int ') == 4
                prof = prof.replace('Cat_cat', 'Cat_cart')
                hom = hom.replace('Cat_cat', 'Cat_cart').replace('@hom_int ', '@hom_int_view ')
                actions = old[action_start:]
                pre_count, functor_count = 0, 0
                for match in reversed(list(re.finditer(r'(?m)^assertnot\b.*?;', actions, re.S))):
                    block = match.group()
                    pre = ('(@hom_precomp_along_func A B F (@fapp0 A B G Y)' in block
                           and 'τ (Transf F G)' in block) or (
                           '(@tapp1_fapp0 A B F G X Y ϵ f)' in block
                           and '(@fapp1_fapp0 A B F X0 X g)' in block)
                    functor = '(F : τ (Functor A B))' in block and (
                        '@fapp1_func' in block or (
                            '(@fapp1_fapp0 A B F Y Z g)' in block and '@hom_' not in block))
                    if pre or functor:
                        pre_count += bool(pre)
                        functor_count += bool(functor)
                        actions = actions[:match.start()] + block.replace('assertnot', 'assert', 1) + actions[match.end():]
                assert (pre_count, functor_count) == (3, 5), (pre_count, functor_count)
                actions = actions.replace('Whole pre/right naturality is no longer strict for an ambient transfor.',
                    'The conventional-lax pre/right leg computes for every ambient transfor.')
                actions = actions.replace('Whole post/left accumulation no longer collapses for an ambient functor.',
                    'Whole post/left accumulation computes for the strict public functor default.')
                actions = actions.replace('Whole pre/right accumulation likewise retains the ambient lax endpoint.',
                    'Whole pre/right accumulation also computes for the strict public functor default.')
                actions = actions.replace('Capped composition is not silently strict for an ambient functor.',
                    'Capped composition is part of the strict public functor contract.')
                actions = actions.replace('Generic accumulation stays distinct; the actual strict view computes.',
                    'The legacy stable-cut normalization boundary remains pending wrapper retirement;\n'
                    '// these runtime observations do not assert mathematical non-functoriality.')
                section = prof + hom + actions
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/ordinary-internal-action',
                                'owner': 'original profunctor swap, internal Hom action and strict/conventional-lax laws',
                                'reason': 'Use the actual Cat_cart profunctor coefficient and ambient Hom views; replace eight obsolete negatives by the selected strict-functor/pre-right positives while retaining post/left laxness and separate stable-cut controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Pre-configured four-cell interchange')
                intrinsic = text.index('  @Fibre_transf_app\n    K\n    (@Op_catd K E)', start)
                end = text.rfind('assert [', start, intrinsic)
                old = text[start:end]
                assert old.count('Cat_cat') == 31
                assert old.count('@hom_postcomp_tele_fapp1_fapp0') == 8
                section = old.replace('Cat_cat', 'Cat_cart')
                section = section.replace('@hom_postcomp_tele_fapp1_fapp0', '@hom_postcomp_tele_transf')
                old_target = 'Pi_cat (@Homd_target_section_catd Z E x)'
                assert section.count(old_target) == 1
                section = section.replace(old_target, 'Op_cat (@Homd_target_section_cat Z E x)')
                old_covariance = '≡ @fib_cov_transf Z D x u;'
                assert section.count(old_covariance) == 1
                section = section.replace(old_covariance,
                    '≡ @strict_transfor _ _ _ _ (@fib_cov_transf Z D x u);')
                # Moving-x path induction restricts motive maps through the
                # existing Cartesian inclusion; fixed-x induction stays raw.
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '@PathInd_transfd' in block:
                        block = re.sub(r'\(@Catd_cat \(@PathOut_cat Z x\)\)\s+Cat_cart\s+'
                            r'\(@PathInd_src_catd Z x\)\s+\(@PathInd_tgt_catd Z x\)',
                            '_ Cat_cart _ _', block)
                        if block.split('⊢', 1)[1].strip().startswith('@tdapp0_fapp0'):
                            telescope, equation = block.split('⊢', 1)
                            left, right = equation.split('≡', 1)
                            assert right.strip() == '@PathInd_func Z x;'
                            block = telescope + '⊢\n  @strict_transfor _ _ _ _ (' + left.strip() + ')\n'
                            block += '''  ≡ fapp0
      (@comp_cat_con_fapp1_func
        (Functor_cart_cat (@PathOut_cat Z x) Cat_cart)
        (Catd_cat (@PathOut_cat Z x)) Cat_cart
        (Functor_cart_include (@PathOut_cat Z x) Cat_cart)
        (@PathInd_src_catd Z x) (@PathInd_tgt_catd Z x))
      (@PathInd_func Z x);'''
                            section = section[:match.start()] + block + section[match.end():]
                            continue
                    starts = [m.start() for m in re.finditer(r'\(@tdapp0_fapp0\b', block)]
                    for first in reversed(starts):
                        depth = 0
                        for last in range(first, len(block)):
                            depth += (block[last] == '(') - (block[last] == ')')
                            if depth == 0:
                                break
                        assert depth == 0
                        term = block[first:last + 1]
                        block = block[:first] + '(@strict_transfor _ _ _ _ ' + term + ')' + block[last + 1:]
                    section = section[:match.start()] + block + section[match.end():]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/interchange-and-path-induction',
                                'owner': 'original profiled interchange, fixed/moving PathOut induction and transitivity diagnostics',
                                'reason': 'Use existing ambient Hom observations and the selected coefficient; retain fixed-x induction and every transitivity consumer, while explicitly observing the moving-x motive restriction and the corrected transposed Homd section target',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                intrinsic = text.index('  @Fibre_transf_app\n    K\n    (@Op_catd K E)')
                start = text.rfind('assert [', 0, intrinsic)
                end = text.index('assert [A B : Cat] (x : τ (Obj A)) (y : τ (Obj B)) ⊢\n  sigma_Fst', start)
                old = text[start:end]
                section = old.replace('Cat_cat', 'Cat_cart')
                projections = [
                    '''@Fibre_transf_app
    K E
    (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K E))
    (@comp_catd_fapp0 K E D
      (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K E))
      (@homd_int K E D GG) FF)
    (@strict_transfor K Cat_cart E
      (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K E))
      (@homd_id_int K E))
    (@tdapp1_int_fapp0_transfd K E D FF GG ϵ) x u''',
                    '''@tapp0_hom_fapp0 K Homd_coeff_cat
    (@Homd_coeff_diagram K E)
    (@Homd_coeff_diagram K (@hom_ K K (@id_func K) x))
    (@homd_id_src_sec K E x u)
    (@homd_tdapp1_src_sec K E D FF GG x u) y
    (@tdapp1_int_section_arrow K E D FF GG ϵ x u)''',
                    '''@tapp0_fapp0
    (Fibre_cat E y) (Homd_index_cat (Hom_cat K x y))
    (@homd_id_tgt_func K E x u y)
    (@homd_tdapp1_tgt_func K E D FF GG x u y) v
    (@strict_transfor _ _ _ _ (@tdapp1_int_tgt_arrow K E D FF GG ϵ x u y))''',
                    '''@fapp1_fapp0
    (Functor_cat (Hom_cat K x y) (Op_cat Cat_cart)) (Op_cat Cat_cart)
    (@fapp0_func (Hom_cat K x y) (Op_cat Cat_cart) p)
    (fapp0 (@homd_tdapp1_tgt_func K E D FF GG x u y) v)
    (fapp0 (@homd_id_tgt_func K E x u y) v)
    (@tdapp1_int_presheaf_arrow K E D FF GG ϵ x u y v)''',
                ]
                assertions = list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))
                assert len(assertions) == 13
                for match, projection in reversed(list(zip(assertions[:4], projections))):
                    telescope, equation = match.group().split('⊢', 1)
                    _, result = equation.split('≡', 1)
                    section = section[:match.start()] + telescope + '⊢\n  ' + projection + '\n  ≡' + result + section[match.end():]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/intrinsic-homd-projections',
                                'owner': 'original arbitrary-modification Homd ladder and displayed-identity extraction observations',
                                'reason': 'Retain the whole Fibre_transf_app observation using homd_int(GG) composed with raw FF, followed by the actual Q modification, Cartesian v component and reversed P-index evaluation; preserve arbitrary FF/GG/epsilon and every identity/filler observation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('assert [A B : Cat] (x : τ (Obj A)) (y : τ (Obj B)) ⊢\n  sigma_Fst', start)
                end = text.index('assert [A B C : Cat]\n  (F G : τ (Functor (Product_cat A B) C)) ⊢\n  @fapp1_func', start)
                old = text[start:end]
                section = old
                changed_blocks, view_count = 0, 0
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '@Product_pair_tele_func' not in block:
                        continue
                    changed_blocks += 1
                    block = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', block)
                    starts = [m.start() for m in re.finditer(r'\(@fapp1_fapp0 A \(Functor_cart_cat B \(Product_cat A B\)\)', block)]
                    for first in reversed(starts):
                        depth = 0
                        for last in range(first, len(block)):
                            depth += (block[last] == '(') - (block[last] == ')')
                            if depth == 0:
                                break
                        assert depth == 0
                        term = block[first:last + 1]
                        block = block[:first] + '''(@strict_transfor B (Product_cat A B)
        (@fapp0 A (Functor_cart_cat B (Product_cat A B)) (@Product_pair_tele_func A B) x)
        (@fapp0 A (Functor_cart_cat B (Product_cat A B)) (@Product_pair_tele_func A B) x')
        ''' + term + ')' + block[last + 1:]
                        view_count += 1
                    section = section[:match.start()] + block + section[match.end():]
                assert (changed_blocks, view_count) == (6, 4), (changed_blocks, view_count)
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/product-pair-telescope',
                                'owner': 'original product-pair telescope and generic composition observations',
                                'reason': 'Use the actual Cartesian pair telescope and its ambient transfor observations; preserve point, whole and capped actions and leave the following generic composition laws unchanged',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                curry_start = 'assert [A B C : Cat]\n  (F G : τ (Functor (Product_cat A B) C)) ⊢\n  @fapp1_func'
                curry_end = 'assert [Z : Cat] (x y : τ (Obj Z)) (p : τ (Hom Z x y))\n  (E : τ (Catd (@PathOut_cat Z x))) ⊢'
                start = text.index(curry_start)
                end = text.index(curry_end, start)
                old = text[start:end]
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', old)
                assert section.count('(eta : τ (Transf F G))') == 3
                section = section.replace('(eta : τ (Transf F G))',
                    '(eta : τ (@StrictTransfor (Product_cat A B) C F G))')
                profile_pattern = r'(@hom_(?:postcomp|precomp_along)[A-Za-z0-9_]*\s+)Cat_cat(\s+)Cat_cat(\s+\(@id Cat_cat )Cat_cat'
                section, count = re.subn(profile_pattern, r'\1Cat_cart\2Cat_cart\3Cat_cart', section)
                assert count == 42, count

                def curry_argument_spans(value, offset, count):
                    """Read only the explicit, parenthesized terms in this pinned block."""
                    result = []
                    for _ in range(count):
                        while value[offset].isspace():
                            offset += 1
                        first = offset
                        if value[offset] == '(':
                            depth = 0
                            while offset < len(value):
                                depth += (value[offset] == '(') - (value[offset] == ')')
                                offset += 1
                                if depth == 0:
                                    break
                            assert depth == 0
                        else:
                            while offset < len(value) and not value[offset].isspace() and value[offset] not in ');':
                                offset += 1
                        assert offset > first
                        result.append((first, offset))
                    return result

                starts = [m.start() for m in re.finditer(r'\(@Transf_cat\b', section)]
                assert len(starts) == 3
                for first in reversed(starts):
                    spans = curry_argument_spans(section, first + len('(@Transf_cat'), 4)
                    args = [section[a:b] for a,b in spans]
                    last = spans[-1][1]
                    while section[last].isspace():
                        last += 1
                    assert section[last] == ')'
                    replacement = '(@Hom_cat (Functor_cart_cat ' + args[0] + ' ' + args[1] + ') ' + args[2] + ' ' + args[3] + ')'
                    section = section[:first] + replacement + section[last + 1:]
                starts = [m.start() for m in re.finditer(r'@tapp0_fapp0\b', section)]
                assert len(starts) == 6
                for first in reversed(starts):
                    spans = curry_argument_spans(section, first + len('@tapp0_fapp0'), 6)
                    a,b = spans[-1]
                    section = section[:a] + '(@strict_transfor _ _ _ _ ' + section[a:b] + ')' + section[b:]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/cartesian-curry-higher-observations',
                                'owner': 'original seven whole/capped/two-component/point curry and uncurry expansion checks',
                                'reason': 'Retain the actual semantic expansion at Cartesian classifiers, with canonical higher Homs and existing ambient component views; the three transfor parameters use the required strict carrier, while general lax currying is qualified separately through its existing interface',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(curry_end, start)
                family_end = 'assert [K : Cat] (E : τ (Catd K)) ⊢\n  fapp1_fapp0 (Pi_func K)'
                end = text.index(family_end, start)
                old = text[start:end]
                assert old.count('Cat_cat') == 31
                section = old.replace('Cat_cat', 'Cat_cart')
                replacements = (
                    ('Op_catd (Const_catd K A) ≡ Const_catd K (Op_cat A);',
                     'Op_catd (Const_catd K A) ≡ Const_catd (CoAt2_cat K) (Op_cat A);'),
                    ('@Pullback_catd K Cat_cart op E',
                     '@Pullback_catd (CoAt2_cat K) (CoAt2_cat Cat_cart) op (@CoAt2_func K Cat_cart E)'),
                    ('      (Catd_cat K));', '      (Functor_cart_cat K Cat_cart));'),
                    ('    ≡ @Pullback_catd_func A B F;',
                     '    ≡ @comp_cat_con_cart_func A B Cat_cart F;'),
                    ('      (Catd_cat (Fibre_cat K l)));',
                     '      (Functor_cart_cat (Fibre_cat K l) Cat_cart));'),
                    ('''    ≡ @Pullback_catd_func
        (Fibre_cat K x)
        (Fibre_cat K y)
        (@fapp1_fapp0 L Cat_cart K x y p);''',
                     '''    ≡ @comp_cat_con_cart_func
        (Fibre_cat K x) (Fibre_cat K y) Cat_cart
        (@fapp1_fapp0 L Cat_cart K x y p);'''),
                    ('    ≡ @Pi_func (@fapp0 K (Op_cat Cat_cart) G x);',
                     '''    ≡ @comp_cat_fapp0
        (Functor_cart_cat (@fapp0 K (Op_cat Cat_cart) G x) Cat_cart)
        (Catd_cat (@fapp0 K (Op_cat Cat_cart) G x)) Cat_cart
        (@Pi_func (@fapp0 K (Op_cat Cat_cart) G x))
        (Functor_cart_include (@fapp0 K (Op_cat Cat_cart) G x) Cat_cart);'''),
                )
                for before, after in replacements:
                    assert section.count(before) == 1, before
                    section = section.replace(before, after)
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/family-constructor-observations',
                                'owner': 'original PathOut transport, family transpose/reindexing and internal Pi classifier observations',
                                'reason': 'Keep fixed-base lax family maps and raw pullback, while correctly observing the Cartesian varying-base classifier, its actual fixed-precomposition action, the CoAt2 transpose base and the existing inclusion before internal Pi',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(family_end, start)
                section_end = 'assert [A B C : Cat] (H : τ (Functor A (Functor_cat B C))) ⊢'
                end = text.index(section_end, start)
                old = text[start:end]
                assert old.count('Cat_cat') == 21
                section = old.replace('Cat_cat', 'Cat_cart')
                old_pi_component = '    ≡ @Pi_func K;'
                assert section.count(old_pi_component) == 1
                section = section.replace(old_pi_component,
                    '''    ≡ @comp_cat_fapp0 (Functor_cart_cat K Cat_cart) (Catd_cat K) Cat_cart
        (@Pi_func K) (Functor_cart_include K Cat_cart);''')
                structural_count, constant_views, eval_count = 0, 0, 0
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '@pi_eval_transf' in block:
                        eval_count += 1
                        telescope, equation = block.split('⊢', 1)
                        _, result = equation.split('≡', 1)
                        block = '''// Evaluate the existing section-first whole map at the fixed k.
''' + telescope + '''⊢
  @fapp0 (Pi_cat E) (Fibre_cat E k)
    (@comp_cat_fapp0 (Pi_cat E) (Pi_cat E) (Fibre_cat E k)
      (@piapp0_func K E k) (@pi_eval_transf K E)) s
  ≡''' + result
                    if '@Const_func_func' in block or '@Functor_catd_const_funcd' in block:
                        structural_count += 1
                        block = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', block)
                        block = block.replace('@comp_cat_cov_func', '@comp_cat_cov_cart_func')
                        starts = [m.start() for m in re.finditer(r'\(@fapp1_fapp0\s+B\s+\(Functor_cart_cat A B\)', block)]
                        for first in reversed(starts):
                            depth = 0
                            for last in range(first, len(block)):
                                depth += (block[last] == '(') - (block[last] == ')')
                                if depth == 0:
                                    break
                            assert depth == 0
                            term = block[first:last + 1]
                            block = block[:first] + '(@strict_transfor _ _ _ _ ' + term + ')' + block[last + 1:]
                            constant_views += 1
                    section = section[:match.start()] + block + section[match.end():]
                assert (structural_count, constant_views, eval_count) == (10, 2, 1)
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/sections-and-weakening',
                                'owner': 'original section postcomposition, Sigma-total comparisons, Pi interfaces and structural weakening observations',
                                'reason': 'Retain arbitrary lax FF/H and the original whole/point/arrow computations, with the actual coefficient, Cartesian constant/weakening classifiers and section-first Pi evaluation; keep Pi(const A) identified with the ambient Functor_cat(K,A)',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(section_end, start)
                exchange_end = 'assert [A B : Cat] (F : τ (Functor A B)) (E : τ (Catd B))\n  (s : τ (Obj (@Functord_cat'
                end = text.index(exchange_end, start)
                old = text[start:end]
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', old)
                count = 0
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '(eta : τ (Transf H K))' in block:
                        target = '(Functor_cart_cat B C)' if '[A B C : Cat]' in block else '(Functor_cart_cat A C)'
                        block = block.replace('(eta : τ (Transf H K))',
                            '(eta : τ (@StrictTransfor A ' + target + ' H K))')
                        count += 1
                        section = section[:match.start()] + block + section[match.end():]
                assert count == 3
                observations = list(re.finditer(r'@tapp([01])_fapp0\b', section))
                assert len(observations) == 13
                for match in reversed(observations):
                    arity, position = (6, 5) if match.group(1) == '0' else (8, 6)
                    spans = curry_argument_spans(section, match.end(), arity)
                    a,b = spans[position]
                    section = section[:a] + '(@strict_transfor _ _ _ _ ' + section[a:b] + ')' + section[b:]
                section = '// Migrated Cartesian exchange and diagonal observations.\n' + section
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/cartesian-exchange-diagonal',
                                'owner': 'original whole, object, arrow and transfor exchange/diagonal diagnostics',
                                'reason': 'Use the implemented Cartesian structural contracts and ambient views of their classified higher action; retain all thirteen original computations and their actual inputs',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(exchange_end, start)
                end = text.index('// Mixed-action foundation', start)
                old = text[start:end]
                section = old
                blocks = list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', section, re.S))
                assert len(blocks) == 24
                assert section.count('@hom_int ') == 2
                for match in reversed(blocks):
                    block = match.group()
                    # General totalization still lands in ambient Cat_cat.
                    # The other literal universe arguments here are family
                    # coefficients or Pi coefficients, which are Cat_cart.
                    if 'Sigma_func' not in block:
                        block = block.replace('Cat_cat', 'Cat_cart')
                    block = block.replace('@hom_int ', '@hom_int_view ')
                    component = '(@tdapp0_fapp0 K E D FF GG k eta)'
                    if component in block:
                        block = block.replace(component, '(@strict_transfor _ _ _ _ ' + component + ')')
                    section = section[:match.start()] + block + section[match.end():]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/section-reindexing-and-totalization',
                                'owner': 'original section pullback, totalized maps/modifications and Sigma-projection observations',
                                'reason': 'Correct the family/Pi coefficient while retaining the ambient Sigma codomain, use the existing ordinary Hom-family view and observe the Cartesian fibre modification through its inclusion; preserve all 22 positives and two runtime/proof-time boundary negatives',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Mixed-action foundation')
                end = text.index('// Direct recursive mixed displayed introduction', start)
                old = text[start:end]
                section = old
                family_count, opposite_count = 0, 0
                blocks = list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))
                for match in reversed(blocks):
                    block = match.group()
                    if '@Op_catd' in block or '@Functor_catd' in block:
                        family_count += 1
                        block = block.replace('Cat_cat', 'Cat_cart')
                        block = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', block)
                    if '@Op_catd' in block:
                        opposite_count += 1
                        block = block.replace('@fapp1_func K Cat_cart (@Op_catd',
                            '@fapp1_func (CoAt2_cat K) Cat_cart (@Op_catd')
                        block = block.replace('@fapp1_fapp0 K Cat_cart (@Op_catd',
                            '@fapp1_fapp0 (CoAt2_cat K) Cat_cart (@Op_catd')
                        if '@comp_cat_fapp0' in block:
                            telescope, equation = block.split('⊢', 1)
                            left, _ = equation.split('≡', 1)
                            block = telescope + '⊢' + left + '''≡ @comp_cat_fapp0
      (Op_cat (Hom_cat K x y))
      (Op_cat (Functor_cart_cat (Fibre_cat E x) (Fibre_cat E y)))
      (Functor_cart_cat (Op_cat (Fibre_cat E x)) (Op_cat (Fibre_cat E y)))
      (@fapp1_func (CoAt2_cat Cat_cart) Cat_cart op (Fibre_cat E x) (Fibre_cat E y))
      (@fapp1_func (CoAt2_cat K) (CoAt2_cat Cat_cart)
        (@CoAt2_func K Cat_cart E) x y);'''
                        elif '@fapp0' in block:
                            assert block.count('(Hom_cat K x y)') == 1
                            block = block.replace('(Hom_cat K x y)', '(Op_cat (Hom_cat K x y))')
                    section = section[:match.start()] + block + section[match.end():]
                assert (family_count, opposite_count) == (7, 3)
                boundary = '''// Object and arrow carriers agree, but the whole Hom input is transposed.
assertnot [K : Cat] (E : τ (Catd K)) (x y : τ (Obj K)) ⊢
  @fapp1_func (CoAt2_cat K) Cat_cart (@Op_catd K E) x y
  : τ (Functor (Hom_cat K x y)
      (Functor_cart_cat (Op_cat (Fibre_cat E x)) (Op_cat (Fibre_cat E y))));

'''
                section = section.rstrip() + '\n\n' + boundary
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/mixed-action-foundation',
                                'owner': 'original full/capped family transpose and mixed-family action observations',
                                'reason': 'Use CoAt2(K), the transposed Hom input and actual coefficient/Hom actions; preserve the mixed Unit_prof computation, ordinary ambient Hom object action and noncollapse control, and reject the old untransposed whole source',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Direct recursive mixed displayed introduction')
                end = text.index('// Direct mixed source-family action', start)
                old = text[start:end]
                assert old.count('Cat_cat') == 14
                section = old.replace('Cat_cat', 'Cat_cart').replace('@id Cat_cart Cat_cart', '@id Cat_cat Cat_cart')
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', section)
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/direct-mixed-target',
                                'owner': 'original direct postmap and recursively mapped binder consumers',
                                'reason': 'Use actual Cartesian fibre-Homs while retaining unrestricted lax positive maps F/G, all recursive object/arrow computations and intrinsic base-cell typing',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Direct mixed source-family action', start)
                end = text.index('// Direct mixed pointwise product distribution', start)
                old = text[start:end]
                assert old.count('Cat_cat') == 11
                section = old.replace('Cat_cat', 'Cat_cart')
                section = re.sub(r'\bFunctor_cat(\s+\(Fibre_cat)', r'Functor_cart_cat\1', section)
                source_classifier = '(Op_cat (Catd_cat (Op_cat K)))'
                assert section.count(source_classifier) == 1
                section = section.replace(source_classifier, '(Op_cat (Functor_cart_cat (Op_cat K) Cat_cart))')
                for source, target, name, declarations, components in (
                    ("A'", 'A', 'L', 4, 5), ('A0', 'A1', 'L1', 2, 1), ('A1', 'A2', 'L2', 2, 1),
                ):
                    before = '(' + name + ' : τ (Functord ' + source + ' ' + target + '))'
                    assert section.count(before) == declarations
                    section = section.replace(before, '(' + name + ' : τ (@StrictTransfor (Op_cat K) Cat_cart ' + source + ' ' + target + '))')
                    component = '@tapp0_fapp0 (Op_cat K) Cat_cart ' + source + ' ' + target + ' k ' + name
                    assert section.count(component) == components
                    section = section.replace(component,
                        '@tapp0_fapp0 (Op_cat K) Cat_cart ' + source + ' ' + target
                        + ' k (@strict_transfor (Op_cat K) Cat_cart ' + source + ' ' + target + ' ' + name + ')')
                section = section.replace('// Check-only source action assembled from the existing constructor action.',
                    '// Check-only source action assembled from the existing constructor action.\n'
                    '// Its negative parameter uses the constructor\'s Cartesian source-map classifier;\n'
                    '// positive target maps and public Functord remain lax.')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/direct-mixed-source',
                                'owner': 'original direct negative-family action and iterated source-map consumers',
                                'reason': 'Use the existing Cartesian negative-parameter classifier and ordinary component inclusion; retain all source maps, compositions and four original computations, without changing public Functord',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Direct mixed pointwise product distribution', start)
                end = text.index('// The following formation checks return to the general diagnostic inventory.', start)
                old = text[start:end]
                section = old.replace('Cat_cat', 'Cat_cart')
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', section)
                for helper, source, target in (
                    ('direct_mixed_product_higher_check',
                     '(Fibre_cat (@Product_catd_transparent_check K (@Functor_catd K A B) (@Functor_catd K A C)) x)',
                     '(Fibre_cat (@Functor_catd K A (@Product_catd_transparent_check K B C)) y)'),
                    ('direct_mixed_comp_higher_check',
                     '(Fibre_cat (@direct_mixed_comp_source_check K X A B) x)',
                     '(Fibre_cat (@Functor_catd K A B) y)'),
                ):
                    a = section.index('symbol ' + helper + '\n')
                    b = section.index('≔', a)
                    signature = section[a:b]
                    assert signature.count(': τ (Transf\n') == 1
                    signature = signature.replace(': τ (Transf\n',
                        ': τ (Obj (Hom_cat\n      (Functor_cart_cat ' + source + '\n        ' + target + ')\n')
                    section = section[:a] + signature.rstrip() + ')\n' + section[b:]
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/direct-mixed-product-composition',
                                'owner': 'original product distribution and constant-middle composition consumers',
                                'reason': 'Retain the transparent products, generic lax FF/GG and original whole/object/arrow/cell computations at the actual Cartesian fibre-Homs; give the two iterable higher-action helpers canonical Hom results',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// The following formation checks return to the general diagnostic inventory.', start)
                end = text.index('assert [Z : Cat] (x y : τ (Obj Z)) ⊢\n  Fibre_cat (@Rep_catd Z x) y', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 6
                section = old.replace('Cat_cat', 'Cat_cart').replace('Op_catd', 'TotalOp_catd')
                section = section.replace('≡ Functor_cat (Fibre_cat A k) (Fibre_cat B k);',
                    '≡ Functor_cart_cat (Fibre_cat A k) (Fibre_cat B k);')
                section = section.replace('(Op_cat (Catd_cat (Op_cat K)))',
                    '(Op_cat (Functor_cart_cat (Op_cat K) Cat_cart))')
                section = section.replace('@piapp0 K (@TotalOp_catd K',
                    '@piapp0 (CoAbove2_cat K) (@TotalOp_catd K')
                section = section.replace('≡ Transf_cat\n',
                    '≡ Hom_cat (Functor_cart_cat (Fibre_cat A k) (Fibre_cat B k))\n')
                old_op = '@Op_func K (Op_cat Cat_cart) X'
                assert section.count(old_op) == 1
                section = section.replace(old_op,
                    '@TotalOp_func (CoAbove2_cat K) (TotalOp_cat Cat_cart) X')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/mixed-formation',
                                'owner': 'original Functor_catd, Hom_catd and Transf_catd formation/fibre observations',
                                'reason': 'Use Cartesian fibre-Homs and the actual total-dual negative sections over R(K), including the existing total-dual constant-family conversion; preserve all six original observations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start_marker = 'assert [Z : Cat] (x y : τ (Obj Z)) ⊢\n  Fibre_cat (@Rep_catd Z x) y'
                end_marker = 'assert [Z : Cat] (x : τ (Obj (Op_cat Z))) (y : τ (Obj Z)) ⊢'
                assert text.count(start_marker) == 1
                start = text.index(start_marker)
                end = text.index(end_marker, start)
                old = text[start:end]
                assert old.count('Cat_cat') == 13
                section = old.replace('Cat_cat', 'Cat_cart')
                motive_fibre = '      (@Catd_cat (@PathOut_cat Z x)));'
                assert section.count(motive_fibre) == 1
                section = section.replace(motive_fibre,
                    '      (Functor_cart_cat (@PathOut_cat Z x) Cat_cart));')
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '(@fapp1_fapp0' in block and '(@PathOutMotives_catd Z)' in block:
                        for endpoint in ('x', 'y'):
                            carrier = '(@Catd_cat (@PathOut_cat Z ' + endpoint + '))'
                            assert block.count(carrier) == 1
                            block = block.replace(carrier,
                                '(Functor_cart_cat (@PathOut_cat Z ' + endpoint + ') Cat_cart)')
                    if ('@pathout_motive_transport_obj Z x y p E' in block
                            and '(@PathOutMotives_catd Z)' in block):
                        context, comparison = block.split('⊢', 1)
                        left, right = comparison.removesuffix(';').split('≡', 1)
                        block = (context + '⊢\n'
                            '  @eq_refl (Catd (@PathOut_cat Z y))\n'
                            '    (' + left.strip() + ')\n'
                            '  : τ (@= (Catd (@PathOut_cat Z y))\n'
                            '      (' + left.strip() + ')\n'
                            '      (' + right.strip() + '));')
                        block = ('// Whole Cartesian reindexing and the stable pullback are compared\n'
                                 '// at proof time; their object and Hom actions compute directly.\n'
                                 + block)
                    section = section[:match.start()] + block + section[match.end():]
                for former, action in (
                    ('@pathout_refl_eval_func Z x', '(@pathout_refl_eval_func Z x)'),
                    ('@Pi_func (@PathOut_cat Z x)', '(@Pi_func (@PathOut_cat Z x))'),
                ):
                    expected = '    ≡ ' + former + ';'
                    assert section.count(expected) == 1
                    section = section.replace(expected,
                        '    ≡ @comp_cat_fapp0\n'
                        '        (Functor_cart_cat (@PathOut_cat Z x) Cat_cart)\n'
                        '        (Catd_cat (@PathOut_cat Z x)) Cat_cart\n'
                        '        ' + action + '\n'
                        '        (Functor_cart_include (@PathOut_cat Z x) Cat_cart);')
                covariance_fibre = ('  Fibre_cat (@FibCov_target_catd Z D) x\n'
                                    '    ≡ @Functord_cat Z (@Rep_catd Z x) D;')
                assert section.count(covariance_fibre) == 1
                section = section.replace(covariance_fibre,
                    '  Fibre_cat (@FibCov_target_catd Z D) x\n'
                    '    ≡ Hom_cat (Functor_cart_cat Z Cat_cart) (@Rep_catd Z x) D;')
                section += fragment('production_pathout_motive_controls.lpfragment') + '\n'
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/pathout-motive-observations',
                                'owner': 'original repeated PathOut, motive reindexing, evaluation, Pi and covariance diagnostics',
                                'reason': 'Observe the existing Cartesian moving-motive classifier and its inclusions into fixed-source evaluation/Pi; retain original transport computations and general lax fixed-source maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(end_marker, start)
                end = text.index('// Generic component evaluation owns', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 28
                covariance_start = old.index('assert [K : Cat] (E : τ (Catd K)) (x : τ (Obj K)) ⊢')
                section = '''// The legacy edge/presheaf classifiers retain their corrected shifted bases.
assert [Z : Cat] (x : τ (Obj (CoAt2_cat (Op_cat Z))))
  (y : τ (Obj (CoAt2_cat Z))) ⊢
  @fapp0 (CoAt2_cat Z) Cat_cart
    (@fapp0 (CoAt2_cat (Op_cat Z))
      (Functor_cart_cat (CoAt2_cat Z) Cat_cart) (@Edge_catd_func Z) x) y
  ≡ Op_cat (Hom_cat Z x y);

assert [Z : Cat] (x : τ (Obj (CoAt2_cat Z)))
  (y : τ (Obj (Op_cat (CoAt2_cat Z)))) ⊢
  Fibre_cat
    (@fapp0 (CoAt2_cat Z) (Catd_cat (Op_cat (CoAt2_cat Z)))
      (@HomPresheaf_catd_func Z) x) y
  ≡ Functor_cart_cat (Op_cat (Hom_cat Z x y)) Cat_cart;

// The corrected whole Homd target uses the actual Q-diagram transformation
// category, replacing the former ordinary Pi/Functor_catd target.
assert [Z : Cat] (E : τ (Catd Z)) (x : τ (Obj Z)) ⊢
  @Homd_target_section_cat Z E x
  ≡ @Transf_cat Z Homd_coeff_cat (@Homd_coeff_diagram Z E)
      (@Homd_coeff_diagram Z (@hom_ Z Z (@id_func Z) x));

assert [Z : Cat] (E : τ (Catd Z)) (x : τ (Obj Z)) ⊢
  @fapp0 Z Cat_cart (@Homd_target_catd Z E) x
  ≡ Op_cat (@Homd_target_section_cat Z E x);

''' + old[covariance_start:].replace('Cat_cat', 'Cat_cart')
                section = section.replace(
                    'Fibre_cat (@FibCov_target_catd K E) x\n'
                    '    ≡ @Functord_cat K (@hom_ K K (@id_func K) x) E;',
                    'Fibre_cat (@FibCov_target_catd K E) x\n'
                    '    ≡ Hom_cat (Functor_cart_cat K Cat_cart) (@hom_ K K (@id_func K) x) E;')
                section = section.replace(
                    'Obj (Fibre_cat (@FibCov_target_catd K E) x)\n'
                    '    ≡ @Functord K (@hom_ K K (@id_func K) x) E;',
                    'Obj (Fibre_cat (@FibCov_target_catd K E) x)\n'
                    '    ≡ @StrictTransfor K Cat_cart (@hom_ K K (@id_func K) x) E;')
                section = section.replace('    (@fib_cov_transf K E x u)\n',
                    '    (@strict_transfor K Cat_cart (@hom_ K K (@id_func K) x) E\n'
                    '      (@fib_cov_transf K E x u))\n')
                section = section.replace(
                    '@Op_funcd K E E (@id_funcd K E)\n'
                    '    ≡ @id_funcd K (@Op_catd K E);',
                    '@Op_funcd K E E (@id (Functor_cart_cat K Cat_cart) E)\n'
                    '    ≡ @id (Functor_cart_cat (CoAt2_cat K) Cat_cart) (@Op_catd K E);')
                for match in reversed(list(re.finditer(r'(?m)^assert\b.*?;', section, re.S))):
                    block = match.group()
                    if '@Op_funcd' not in block:
                        continue
                    block = block.replace('(FF : τ (Functord E D))',
                        '(FF : τ (Hom (Functor_cart_cat K Cat_cart) E D))')
                    block = block.replace('@Op_funcd K (@Op_catd K E)',
                        '@Op_funcd (CoAt2_cat K) (@Op_catd K E)')
                    if '@tapp0_fapp0' in block:
                        block = block.replace('    K\n    Cat_cart\n',
                            '    (CoAt2_cat K)\n    Cat_cart\n', 1)
                        block = block.replace('    (@Op_funcd K E D FF)\n',
                            '    (@strict_transfor _ _ _ _ (@Op_funcd K E D FF))\n')
                        block = block.replace('(@tapp0_fapp0 K Cat_cart E D x FF)',
                            '(@tapp0_fapp0 K Cat_cart E D x (@strict_transfor K Cat_cart E D FF))')
                    section = section[:match.start()] + block + section[match.end():]
                assert len(re.findall(r'(?m)^assert\b', section)) == 28
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/homd-classifier-observations',
                                'owner': 'original edge/presheaf, Homd target, covariance, family duality and elementary displayed projection diagnostics',
                                'reason': 'Observe the shifted classifier bases and actual Q transformation target; retain ordinary lax Functord while using the already required Cartesian input only for Op_funcd',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Generic component evaluation owns', start)
                end_marker = ('assert [Z : Cat] (D E : τ (Catd Z)) (FF : τ (Functord D E))\n'
                              '  (x : τ (Obj Z)) ⊢\n  @tapp0_fapp0')
                end = text.index(end_marker, start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 36
                assert len(re.findall(r'(?m)^assertnot\b', old)) == 9
                section = old.replace('Cat_cat', 'Cat_cart')
                section = re.sub(r'\bFunctor_cat\b', 'Functor_cart_cat', section)
                # The extracted strict-cell property lives in the ordinary
                # transformation category, independently of the family coefficient.
                section = section.replace('@strict_cell_path\n    (@Functor_cart_cat',
                    '@strict_cell_path\n    (@Functor_cat')
                for match in reversed(list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', section, re.S))):
                    block = match.group()
                    if '@functord_transport_lhs_tele_agrees' in block:
                        block = block.replace('functord_transport_lhs_', 'functord_transport_rhs_')
                    if '@functord_transport_lhs_agrees' in block:
                        block = block.replace('functord_transport_lhs_', 'functord_transport_rhs_')
                    if (block.startswith('assertnot')
                            and '@functord_transport_rhs_func K E D FF x y p' in block
                            and '@fapp0' in block):
                        block = block.replace('assertnot', 'assert', 1)
                    if (block.startswith('assertnot') and '  comp_fapp0\n' in block
                            and ('(G : τ (Functor' in block or '(F : τ (Functor' in block)):
                        offset = block.index('(epsilon : τ (@Transf') + len('(epsilon : τ (@Transf')
                        spans = curry_argument_spans(block, offset, 4)
                        _, carrier, source_map, target_map = [block[a:b] for a,b in spans]
                        end_object = 'HH' if '(FF GG HH :' in block else 'GG'
                        if '(G : τ (Functor' in block:
                            middle_map, middle_object = source_map, 'GG'
                        else:
                            middle_map = target_map
                            middle_object = 'GG' if end_object == 'HH' else 'FF'
                        assert block.count('  comp_fapp0\n') == 1
                        block = block.replace('  comp_fapp0\n',
                            '  @comp_fapp0 ' + carrier + '\n'
                            '    (fapp0 ' + source_map + ' FF)\n'
                            '    (fapp0 ' + middle_map + ' ' + middle_object + ')\n'
                            '    (fapp0 ' + target_map + ' ' + end_object + ')\n')
                    if '@Op_funcd' in block:
                        block = block.replace('(FF : τ (Functord E D))',
                            '(FF : τ (Hom (Functor_cart_cat K Cat_cart) E D))')
                        block = block.replace('    K\n    (@Op_catd K E)',
                            '    (CoAt2_cat K)\n    (@Op_catd K E)')
                        block = block.replace('@Fibre_func K (@Op_catd K E)',
                            '@Fibre_func (CoAt2_cat K) (@Op_catd K E)')
                        block = block.replace('(@Op_funcd K E D FF)',
                            '(@strict_transfor _ _ _ _ (@Op_funcd K E D FF))')
                        block = block.replace('@Fibre_func K E D FF z',
                            '@Fibre_func K E D (@strict_transfor K Cat_cart E D FF) z')
                    if '@tapp0_fapp0\n      (Fibre_cat E z)' in block:
                        occurrences = [m.start() for m in re.finditer(r'\(@tdapp0_fapp0\b', block)]
                        assert len(occurrences) == 3
                        for first in reversed(occurrences):
                            spans = curry_argument_spans(block, first + len('(@tdapp0_fapp0'), 7)
                            last = spans[-1][1]
                            while block[last].isspace():
                                last += 1
                            assert block[last] == ')'
                            term = block[first:last+1]
                            block = block[:first] + '(@strict_transfor _ _ _ _ ' + term + ')' + block[last+1:]
                    if '≡ @tdapp0_fapp0 K E D FF GG z ϵ;' in block:
                        block = block.replace('≡ @tdapp0_fapp0 K E D FF GG z ϵ;',
                            '≡ @strict_transfor _ _ _ _ (@tdapp0_fapp0 K E D FF GG z ϵ);')
                    section = section[:match.start()] + block + section[match.end():]
                fibre_homs = 0
                for first in reversed([m.start() for m in re.finditer(r'\(@Transf_cat\b', section)]):
                    spans = curry_argument_spans(section, first + len('(@Transf_cat'), 4)
                    args = [section[a:b] for a,b in spans]
                    if not args[0].startswith('(Fibre_cat'):
                        continue
                    fibre_homs += 1
                    last = spans[-1][1]
                    while section[last].isspace():
                        last += 1
                    assert section[last] == ')'
                    replacement = ('(Hom_cat (Functor_cart_cat ' + args[0] + ' ' + args[1] + ')\n'
                                   '          ' + args[2] + '\n          ' + args[3] + ')')
                    section = section[:first] + replacement + section[last+1:]
                assert fibre_homs == 2
                section = section.replace('// Component evaluation does not silently impose pre/right naturality on an\n// arbitrary outer transfor.\nassertnot',
                    '// Projecting the component before accumulating the strict pre/right leg computes.\nassert')
                section = section.replace('// Product-valued target reduction does not restore that retired cut.\nassertnot',
                    '// The same component projection order with a product-valued target.\nassert')
                section = section.replace('// Normal-lax identity projection does not recreate pre/right strictness.\nassertnot',
                    '// Identity specialization after the off-diagonal action has projected.\nassert')
                section = section.replace('// The ambient left/source route remains the selected lax action.',
                    '// The ambient pre/right route is the selected conventional-lax action.')
                section = section.replace('// The right/target route is available only through a strict displayed profile.',
                    '// The old strict displayed wrapper observes that same selected route.')
                section = section.replace('// Evaluation at p retains the ambient left/source comparison.',
                    '// Evaluation at p retains the selected pre/right comparison.')
                assert len(re.findall(r'(?m)^assert\b', section)) == 40
                assert len(re.findall(r'(?m)^assertnot\b', section)) == 5
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/displayed-component-transport-observations',
                                'owner': 'original whole/higher displayed components, transport and Sigma-composition diagnostics',
                                'reason': 'Use actual Cartesian fibre-Homs and ordinary inclusion; the three projected pre/right cuts now compute at the native component owner while post/left laxness and general FF remain',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index(end_marker, start)
                end = text.index('// catalog-area: Categorical-universe direct equality-valued', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 17
                section = fragment('production_public_homd_controls.lpfragment') + '\n'
                assert len(re.findall(r'(?m)^assert\b', section)) == 19
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/public-homd-ladder-observations',
                                'owner': 'original public Homd x/u/y/v ladder and constant-family specializations',
                                'reason': 'Retain every original assertion at the actual Q/index types and add the whole relative component comparison; five whole terminal-source reductions remain explicit unqualified obligations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: Categorical-universe direct equality-valued', start)
                start = text.index('// catalog-area: auto', start)
                end = text.index('// Cat-valued profunctor facade and representable hom action.', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 13
                assert len(re.findall(r'(?m)^assertnot\b', old)) == 1
                section = fragment('production_central_homd_leaf_controls.lpfragment') + '\n\n'
                assert len(re.findall(r'(?m)^assert\b', section)) == 14
                assert len(re.findall(r'(?m)^assertnot\b', section)) == 1
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/public-homd-leaf-intrinsic-observations',
                                'owner': 'original Homd presheaf leaf, identity extraction and intrinsic projection ladder',
                                'reason': 'Use the actual index presheaf view, relative-to-identity root and Cartesian component inclusion; retain general FF and the full index action. The installed constant-index computation changes one old negative to positive; an arbitrary-loop control preserves noncollapse',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Cat-valued profunctor facade and representable hom action.', start)
                end = text.index('// Generic displayed Hom action: full/capped/point projection ladder.', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 15
                section = old.replace('Cat_cat', 'Cat_cart')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/profunctor-hom-observations',
                                'owner': 'original profunctor facade and represented Hom action diagnostics',
                                'reason': 'Retain the product-base convention, original maps and all full/capped/point observations at their actual Cat_cart coefficient',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// Generic displayed Hom action: full/capped/point projection ladder.', start)
                end = text.index('// General two-sided product maps used by profunctor reindexing.', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 12
                assert len(re.findall(r'(?m)^assertnot\b', old)) == 1
                section = fragment('production_central_homcatd_controls.lpfragment') + '\n\n'
                assert len(re.findall(r'(?m)^assert\b', section)) == 12
                assert len(re.findall(r'(?m)^assertnot\b', section)) == 1
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/hom-catd-action-observations',
                                'owner': 'original generic displayed Hom action, classifier folds and inline Unit_prof comparison',
                                'reason': 'Use total-dual negative sections over R(K), actual Cat_cart coefficients and the same Hom/profunctor values. Establish the generic inline comparison before specializing to the original strict section, without a new rule or operational proof argument',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// General two-sided product maps used by profunctor reindexing.', start)
                end = text.index('// catalog-area: Internal Path action and explicit Core-inclusion kappa', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 81
                assert not re.findall(r'(?m)^assertnot\b', old)
                split = old.index('// Stable profunctor reindexing and its representable fold.')
                prof_observations = old[split:]
                # Nine in the pinned input; the existing later Hom-annotation
                # pass already retags one of them in the previous emitted file.
                assert prof_observations.count('Cat_cat') == 9
                assert prof_observations.count('(@hom_int ') == 2
                later_hom_annotation = '≡ @tapp1_fapp0\n      A\n      Cat_cat\n      (@hom_'
                assert prof_observations.count(later_hom_annotation) == 1
                prof_observations = prof_observations.replace('Cat_cat', 'Cat_cart')
                # Leave the one annotation owned by the existing later
                # represented-Hom pass to that pass and its guarded count.
                prof_observations = prof_observations.replace(
                    later_hom_annotation.replace('Cat_cat', 'Cat_cart'), later_hom_annotation)
                section = old[:split] + prof_observations.replace('(@hom_int ', '(@hom_int_view ')
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/product-profunctor-operations-observations',
                                'owner': 'original product maps, Prof reindexing, tensor, co-Yoneda, weighted-colimit and join diagnostics',
                                'reason': 'Preserve ordinary product-map composition and the existing Prof convention; retag family coefficient annotations and use the two existing ordinary Hom inclusions in the internal-action observation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: Opaque walking endomorphism HIT and contextual elimination', start)
                end = text.index('// catalog-area: auto', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 89
                assert len(re.findall(r'(?m)^assertnot\b', old)) == 12
                section = old.replace('Cat_cat', 'Cat_cart')
                observations = {}
                for match in reversed(list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', section, re.S))):
                    block = match.group()
                    if '≡ @Transf\n' in block and '@walking_end_loop_coherence' in block:
                        block = block.replace('≡ @Transf\n', '≡ @StrictTransfor\n')
                        observations['coherence'] = observations.get('coherence', 0) + 1
                    if 'r sigma;' in block:
                        block = block.replace('r sigma;', 'r (@strict_transfor _ _ _ _ sigma);')
                        observations['loopComponent'] = observations.get('loopComponent', 0) + 1
                    if ('@tapp0_fapp0' in block or '@tapp1_func' in block):
                        block, count = re.subn(r'\bwalking_power_spiral(?:_coreincl)?\b',
                            lambda m: '(@strict_transfor _ _ _ _ ' + m.group() + ')', block)
                        if count:
                            observations['spiralViews'] = observations.get('spiralViews', 0) + count
                    if 'WalkingEnd_cat Cat_cart walking_Code_catd' in block:
                        block = block.replace('(Functor_cat\n        (Fibre_cat walking_Code_catd',
                            '(Functor_cart_cat\n        (Fibre_cat walking_Code_catd')
                        observations['codeHom'] = observations.get('codeHom', 0) + 1
                    if 'p q alpha\n' in block and 'WalkingEnd_cat Cat_cart walking_based_rep_catd' in block:
                        context, rest = block.split('⊢', 1)
                        value, typ = rest.rstrip(';').rsplit('\n  : ', 1)
                        value = value.replace('(Functor_cat\n      (Fibre_cat walking_based_rep_catd',
                            '(Functor_cart_cat\n      (Fibre_cat walking_based_rep_catd')
                        block = context + '⊢\n  @strict_transfor _ _ _ _\n    (' + value.strip() + ')\n  : ' + typ + ';'
                        observations['repHigherView'] = observations.get('repHigherView', 0) + 1
                    section = section[:match.start()] + block + section[match.end():]
                assert observations == {'coherence': 1, 'loopComponent': 1, 'spiralViews': 4,
                                        'codeHom': 1, 'repHigherView': 1}, observations
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/walking-end-code-decoder-observations',
                                'owner': 'original opaque WalkingEnd, Code/power/spiral, decoder and Hom-Nat diagnostics',
                                'reason': 'Use the existing strict fibre-comparison classifier and ordinary inclusion, actual Cat_cart Code action and Cartesian higher Hom; preserve the lax base map, opaque constructors, original inverse data and all negative observations',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                start = text.index('// catalog-area: auto', start)
                end = text.index('// catalog-area: Cat-valued presheaf facade and restriction', start)
                old = text[start:end]
                assert len(re.findall(r'(?m)^assert\b', old)) == 76
                assert len(re.findall(r'(?m)^assertnot\b', old)) == 3
                split = old.index('assert [K : Cat] (A : Cat)')
                prof_closed, section_part = old[:split], old[split:]
                assert len(re.findall(r'(?m)^assert\b', prof_closed)) == 43
                later_represented = r'Cat_cat(\s+)(\(@(?:hom_|hom_con|Rep_catd)\b)'
                assert len(re.findall(later_represented, section_part)) == 2
                section_part = section_part.replace('Cat_cat', 'Cat_cart')
                hom_index = '(Hom_cat K x y)'
                section_hom = '(@homd_ K E E (@id_funcd K E) x (@piapp0 K E s x) y (@piapp0 K E s y))'
                section_dual_family = '(@TotalOp_catd (Op_cat ' + hom_index + ') ' + section_hom + ')'
                section_base = '(TotalOp_cat ' + hom_index + ')'
                unit_family = '(@Const_catd K Terminal_cat)'
                relative_target = '(fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K ' + unit_family + '))'
                relative_root = '(@comp_catd_fapp0 K ' + unit_family + ' E ' + relative_target + ' (@homd_int K ' + unit_family + ' E s) s)'
                relative_point = '(@fapp0 Terminal_cat (Op_cat (@Homd_target_section_cat K ' + unit_family + ' x)) (@Fibre_func K ' + unit_family + ' ' + relative_target + ' ' + relative_root + ' x) Terminal_obj)'
                observations = {}
                for match in reversed(list(re.finditer(r'(?m)^assert(?:not)?\b.*?;', section_part, re.S))):
                    block = match.group()
                    context, rest = block.split('⊢', 1)
                    if '@piapp1_fapp0\n    (Op_cat (Hom_cat K x y))' in block:
                        context = context.replace('(Op_cat (Hom_cat K x y))', section_base)
                        block = (context + '⊢\n  @piapp1_fapp0 ' + section_base + '\n    '
                            + section_dual_family + '\n    (@piapp1_func K E s x y) f g alpha\n'
                            + '  ≡ @fdapp1_int_hom_fapp0 ' + section_base + '\n'
                            + '      (@Const_catd ' + section_base + ' Terminal_cat)\n      '
                            + section_dual_family + '\n      (@piapp1_func K E s x y) f g alpha\n'
                            + '      Terminal_obj Terminal_obj Terminal_obj;')
                        observations['higherSection'] = observations.get('higherSection', 0) + 1
                    elif 'Hom_cat (@Sigma_cat Z E)' in block:
                        block = context + '''⊢
  Hom_cat (@Sigma_cat Z E) (Struct_sigma x u) (Struct_sigma y v)
  ≡ TotalOp_cat (@Sigma_cat (TotalOp_cat (Hom_cat Z x y))
      (@TotalOp_catd (Op_cat (Hom_cat Z x y))
        (@homd_ Z E E (@id_funcd Z E) x u y v)));'''
                        observations['sigmaHom'] = observations.get('sigmaHom', 0) + 1
                    elif '@fapp1_func\n    (@Sigma_cat K E)' in block and '≡ @Op_func' in block:
                        value = rest.split('≡', 1)[0]
                        block = context + '⊢' + value + '''≡ @fapp1_fapp0 (Homd_index_cat (Hom_cat K x y)) Cat_cat
      (Homd_index_sigma_func (Hom_cat K x y))
      (fapp0 (@homd_id_tgt_func K E x u y) v)
      (fapp0 (@homd_ff_tgt_func K E D η x u y) v)
      (@fdapp1_int_presheaf_arrow K E D η x u y v);'''
                        observations['sigmaHigher'] = observations.get('sigmaHigher', 0) + 1
                    elif '(@Op_funcd K (@Const_catd K Terminal_cat) E s)' in block:
                        expected = rest.rstrip(';').split('≡', 1)[1]
                        if '@Homd_target_section_catd' in block:
                            value = '''@homd_index_presheaf (Hom_cat K x y)
    (fapp0 (@tapp0_fapp0 K Homd_coeff_cat
      (@Homd_coeff_diagram K (@Const_catd K Terminal_cat))
      (@Homd_coeff_diagram K (@hom_ K K (@id_func K) x)) y
      ''' + relative_point + ') Terminal_obj)'
                            observations['relativeLeaf'] = observations.get('relativeLeaf', 0) + 1
                        else:
                            value = relative_point
                            observations['relativeSection'] = observations.get('relativeSection', 0) + 1
                        block = context + '⊢\n  ' + value + '\n  ≡' + expected + ';'
                    elif block.startswith('assertnot') and '@piapp1_fapp0 K (@Const_catd K A)' in block:
                        block = block.replace('assertnot', 'assert', 1)
                        observations['constantAction'] = observations.get('constantAction', 0) + 1
                    section_part = section_part[:match.start()] + block + section_part[match.end():]
                assert observations == {'higherSection': 1, 'sigmaHom': 1, 'sigmaHigher': 1,
                                        'relativeLeaf': 1, 'relativeSection': 1, 'constantAction': 1}, observations
                section_part = section_part.replace(
                    '// First higher action of the section-action section.  Its runtime result\n'
                    '// stays in the generic displayed internal-hom projection cascade.',
                    '// First higher action uses the actual total-dual section family and index.\n'
                    '// Its runtime result stays in the existing intrinsic projection cascade.')
                # Preserve the two annotations owned by the later represented-Hom pass.
                section_part, count = re.subn(later_represented.replace('Cat_cat', 'Cat_cart'),
                    r'Cat_cat\1\2', section_part)
                assert count == 2
                section = prof_closed + section_part
                assert len(re.findall(r'(?m)^assert\b', section)) == 77
                assert len(re.findall(r'(?m)^assertnot\b', section)) == 2
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/prof-closed-pi-sigma-observations',
                                'owner': 'original closed/comparison Prof, section action, Sigma Hom/map and contextual-substitution diagnostics',
                                'reason': 'Retain the Prof comparison and inverse-data observations; use the native total-dual Pi/Sigma index and P(I) action, preserve general section/FF inputs, and replace obsolete Op_funcd(s) projections by the actual relative composite. Constant-section action already computes, so one former negative becomes positive',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
                marker = '// catalog-area: Constructed Cat-valued sheafification reflector'
                end_marker = '/* End of the CS-12s constructed Cat-valued sheafification diagnostics. */'
                assert text.count(marker) == text.count(end_marker) == 1
                start, end = text.index(marker), text.index(end_marker) + len(end_marker)
                old = text[start:end]
                section = old
                for pattern, count in (
                    ('@Sheaf_cat K T Cat_cat', 7),
                    ('@Functor_cat (Op_cat K) Cat_cat', 2),
                    ('@SheafificationCapability K T Cat_cat', 1),
                ):
                    assert section.count(pattern) == count
                    section = section.replace(pattern, pattern.replace('Cat_cat', 'Cat_cart'))
                text = text[:start] + section + text[end:]
                changes.append({'source': path + '/CS-12s', 'owner': 'original constructed sheafification diagnostics',
                                'reason': 'Observe the migrated coefficient specialization while preserving ambient Obj(Cat), the proof-time/runtime distinction and all nine original assertions',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(section)})
            ambient_postcomp_consumers = {
                'emdash3_2_profiled_interchange.lp': 13,
                'examples/action_profile_eckmann_hilton_one_hom.lp': 1,
            }
            if path in ambient_postcomp_consumers:
                old = text
                # These consumers take ambient transfors. The existing
                # ordinary telescope owner is exactly the strict_transfor
                # projection of the canonical Cartesian Hom action.
                assert text.count('@hom_postcomp_tele_fapp1_fapp0') == ambient_postcomp_consumers[path]
                text = text.replace('@hom_postcomp_tele_fapp1_fapp0',
                                    '@hom_postcomp_tele_transf')
                if path == 'emdash3_2_profiled_interchange.lp':
                    assert text.count('≔ @profiled_vertical_both_raw_path') == 1
                    start = text.index('≔ @profiled_vertical_both_raw_path')
                    end = text.index(';', start) + 1
                    text = text[:start] + fragment('production_profiled_interchange.lpfragment').rstrip() + text[end:]
                changes.append({'source': path, 'owner': 'profiled interchange and Eckmann-Hilton observations',
                                'reason': 'Use the existing ambient projection of canonical Cartesian Hom action; retain the original profiled vertical proof and join its final telescope by ordinary strict functoriality, with no new rule or hypothesis',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_walking_end_hit.lp':
                old = text
                text = text.replace('require open emdash.emdash3_2_eq1_hom_action;',
                    'require open emdash.emdash3_2_eq1_hom_action;\n'
                    'require open emdash.emdash3_2_one_cat_transfor_profiles;')
                coherence = '≔ @Transf\n    (Fibre_cat R walking_base)'
                assert text.count(coherence) == 1
                text = text.replace(coherence, '≔ @StrictTransfor\n    (Fibre_cat R walking_base)')
                text = text.replace('// Contextual loop coherence D[loop] o u => u o R[loop].',
                    '// Contextual loop coherence D[loop] o u => u o R[loop].\n'
                    '// Cat_cart-valued motives require strict naturality in the fibre\n'
                    '// variable; the loop comparison itself remains directed/noninvertible.')
                base_rule = '      WalkingEnd_cat Cat_cat\n      $R $D walking_base\n      (@walking_end_ind_funcd $R $D $u _)'
                assert text.count(base_rule) == 1
                text = text.replace(base_rule,
                    '      _ _\n      _ _ walking_base\n      (@walking_end_ind_funcd $R $D $u _)')
                assert text.count('$r $sigma;') == 1
                text = text.replace('$r $sigma;',
                    '$r (@strict_transfor (Fibre_cat $R walking_base) (Fibre_cat $D walking_base)\n'
                    '        (@walking_end_loop_lhs_func $R $D $u) (@walking_end_loop_rhs_func $R $D $u) $sigma);')
                assert text.count('r sigma)') == 2
                text = text.replace('r sigma)',
                    'r (@strict_transfor (Fibre_cat R walking_base) (Fibre_cat D walking_base)\n'
                    '        (@walking_end_loop_lhs_func R D u) (@walking_end_loop_rhs_func R D u) sigma))')
                # Every remaining universe tag is an observation of Code,
                # including its generator-prefix action and fapp1 view.
                assert text.count('Cat_cat') == 10
                text = text.replace('Cat_cat', 'Cat_cart')
                text = text.replace('// Code : WalkingEnd -> Cat, with base Path(Nat) and loop NatSucc.',
                    '// Code : WalkingEnd -> Cat_cart, with base Path(Nat) and loop NatSucc.')
                spiral_start = text.index('symbol walking_power_spiral_coreincl\n')
                spiral_end = text.index(';', spiral_start) + 1
                spiral = text[spiral_start:spiral_end]
                assert spiral.count(': τ (Transf\n') == 1
                spiral = spiral.replace(': τ (Transf\n',
                    ': τ (@StrictTransfor (Path_cat Nat_grpd)\n'
                    '      (Hom_cat WalkingEnd_cat walking_base walking_base)\n')
                original_spiral_body = spiral.split('≔', 1)[1].strip().removesuffix(';')
                spiral = spiral.split('≔', 1)[0] + '''≔ @one_cat_strict_transfor (Path_cat Nat_grpd)
    (Hom_cat WalkingEnd_cat walking_base walking_base)
    (@discrete_cat_is_one_cat (Hom_cat WalkingEnd_cat walking_base walking_base)
      (walking_end_hom_discrete walking_base walking_base)) _ _
    (''' + original_spiral_body + ');'
                text = text[:spiral_start] + spiral + text[spiral_end:]
                component = '    n\n    walking_power_spiral;'
                assert text.count(component) == 1
                text = text.replace(component,
                    '    n\n    (@strict_transfor (Path_cat Nat_grpd) (Hom_cat WalkingEnd_cat walking_base walking_base)\n'
                    '      (@walking_end_loop_lhs_func walking_Code_catd walking_based_rep_catd walking_power_func)\n'
                    '      (@walking_end_loop_rhs_func walking_Code_catd walking_based_rep_catd walking_power_func)\n'
                    '      walking_power_spiral);')
                encode_action = '''    (@fapp1_func
      WalkingEnd_cat Cat_cart walking_Code_catd
      walking_base walking_base);'''
                assert text.count(encode_action) == 1
                text = text.replace(encode_action, '''    (@comp_cat_fapp0 (Hom_cat WalkingEnd_cat walking_base walking_base)
      (Functor_cart_cat (Path_cat Nat_grpd) (Path_cat Nat_grpd))
      (Functor_cat (Path_cat Nat_grpd) (Path_cat Nat_grpd))
      (Functor_cart_include (Path_cat Nat_grpd) (Path_cat Nat_grpd))
      (@fapp1_func WalkingEnd_cat Cat_cart walking_Code_catd
        walking_base walking_base));''')
                rec_composition = '''rule @comp_fapp0
      $C _ _ _
      (@fapp1_fapp0
        WalkingEnd_cat $C (@walking_end_rec_func $C $x $a)
        $Y $Z $g)
      (@fapp1_fapp0
        WalkingEnd_cat $C (@walking_end_rec_func $C $x $a)
        $X $Y $f)
  ↪ @fapp1_fapp0
      WalkingEnd_cat $C (@walking_end_rec_func $C $x $a)
      $X $Z
      (@comp_fapp0 WalkingEnd_cat $X $Y $Z $g $f);'''
                assert text.count(rec_composition) == 1
                text = text.replace(rec_composition,
                    '// Composition is the existing generic default-strict functor cut.\n'
                    '// The former named instance is redundant and is retired.')
                text = text.replace('generator, and named strict-composition computations.',
                    'generator computations; composition uses the generic strict-functor owner.')
                text = text.replace('is protected and owns exactly its point, generator, and strict-composition\n  observations.',
                    'is protected and owns its point and generator observations. Composition\n  uses the generic default-strict functor owner.')
                text = text.replace('// One named component of the recursor\'s guarded composition computation.\n// This is a theorem over explicit arrows, not an all-components capability.',
                    '// Named theorem view of the default-strict functor composition law.')
                changes.append({'source': path, 'owner': 'walking-end contextual eliminator coefficient',
                                'reason': 'Use the existing strict fibre-transformation Hom of Cat_cart for loop coherence; retain the directed loop datum, its original component beta, section and recursor bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/walking_endomorphism_hit.lp':
                old = text
                assert text.count('r sigma;') == 1
                text = text.replace('r sigma;',
                    'r (@strict_transfor (Fibre_cat R walking_base) (Fibre_cat D walking_base)\n'
                    '        (@walking_end_loop_lhs_func R D u) (@walking_end_loop_rhs_func R D u) sigma);')
                changes.append({'source': path, 'owner': 'original contextual WalkingEnd reviewer',
                                'reason': 'Observe the selected strict fibre-coherence through its existing ambient inclusion; retain every constructor, model, normalization and noncollapse assertion',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/action_profile_walking_named_rec_controls.lp':
                old = text
                marker = 'assertnot [C : Cat] (F : τ (Functor WalkingEnd_cat C))'
                assert text.count(marker) == 1
                text = text.replace(marker, 'assert [C : Cat] (F : τ (Functor WalkingEnd_cat C))')
                text = text.replace('/* Named recursor computation remains separate from arbitrary functors. */',
                    '/* Default-strict functors share the composition law; distinct chosen loop maps remain distinct. */')
                changes.append({'source': path, 'owner': 'WalkingEnd default-strict functor observation',
                                'reason': 'The former arbitrary-lax functor composition negative becomes the required strict-default positive; retain the different-recursor negative',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_terminal_adjunctions.lp':
                old = text
                assert text.count('(@TerminalObject (Op_cat C) t)') == 5
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                    '(@TerminalObject (TotalOp_cat C) t)')
                changes.append({'source': path, 'owner': 'ordinary initial-object adjunction presentation',
                                'reason': 'Use the same total-dual initial-object input as the existing native initial-arrow and cokernel owners; preserve both structural presentations and their original evidence bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_terminal_adjunction_families.lp',
                        'emdash3_2_one_cat_terminal_adjunction_family_observations.lp'):
                old = text
                if path == 'emdash3_2_one_cat_terminal_adjunction_families.lp':
                    for kind in ('terminal', 'initial'):
                        name = kind + '_adjunction_presented_family'
                        marker = 'symbol ' + name + ' [B C : Cat]'
                        assert text.count(marker) == 1
                        start = text.index(marker)
                        end = text.index(';', start) + 1
                        original_presentation = text[start:end]
                        assert original_presentation.count('(Functor_cat WalkingArrow_cat C)') == 2
                        general_presentation = original_presentation.replace(
                            '(Functor_cat WalkingArrow_cat C)', '(Functor_oplax_cat WalkingArrow_cat C)')
                        ordinary_presentation = original_presentation.replace(marker,
                            'symbol one_cat_' + name + ' [B C : Cat]\n'
                            '  (C1 : τ (IsNCat (cat_succ cat_zero) C))')
                        ordinary_presentation = ordinary_presentation.replace(
                            '@transf_arrow_diagram_func C C', '@one_cat_transf_arrow_diagram_func C C C1')
                        text = (text[:start] + general_presentation
                                + '\n\n// Ordinary realization under the existing target hypothesis, retaining e and F.\n'
                                + ordinary_presentation + text[end:])
                ordinary_references = [
                    (r'@terminal_adjunction_presented_family\s+B\s+C',
                     '@one_cat_terminal_adjunction_presented_family B C C1'),
                    (r'@initial_adjunction_presented_family\s+B\s+C',
                     '@one_cat_initial_adjunction_presented_family B C C1'),
                    (r'@transf_arrow_diagram_func\s+B\s+C',
                     '@one_cat_transf_arrow_diagram_func B C C1'),
                    (r'@diagram_family_transf\s+B\s+WalkingArrow_cat\s+C',
                     '@one_cat_diagram_family_transf B WalkingArrow_cat C C1'),
                    (r'@sym_transf_tapp0_transf\s+B\s+WalkingArrow_cat\s+C',
                     '@one_cat_family_exchange_map_at B WalkingArrow_cat C C1'),
                    (r'@one_cat_diagram_family_evaluation_comp_path\b',
                     '@one_cat_diagram_family_exchange_comp_path'),
                ]
                ordinary_reference_counts = {}
                for pattern, replacement in ordinary_references:
                    text, count = re.subn(pattern, lambda _: replacement, text)
                    ordinary_reference_counts[pattern] = count
                assert all(ordinary_reference_counts[p] > 0 for p, _ in ordinary_references[:4])
                changes.append({'source': path, 'owner': 'terminal/initial family presentations and observations',
                                'reason': 'Retain the general helpers with corrected oplax outputs and their original e/F inputs; use defined ordinary presentations under existing OneCat hypotheses while preserving the original universality and endpoint proof bodies',
                                'replacementCounts': ordinary_reference_counts,
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
                if path == 'emdash3_2_one_cat_terminal_adjunction_families.lp':
                    for kind in ('terminal', 'initial'):
                        name = 'one_cat_' + kind + '_adjunction_family_presentation_evidence'
                        marker = 'symbol ' + name + ' [B C : Cat]'
                        assert text.count(marker) == 1
                        start = text.index(marker)
                        end = text.index(';', start) + 1
                        ordinary_evidence = text[start:end]
                        native = ordinary_evidence.replace(name, 'one_cat_oplax_' + kind + '_adjunction_family_presentation_evidence')
                        native = native.replace('Functor_cat WalkingArrow_cat C',
                            'Functor_oplax_cat WalkingArrow_cat C')
                        native = native.replace('@one_cat_transf_arrow_diagram_func B C C1',
                            '@transf_arrow_diagram_func B C')
                        native = native.replace('@one_cat_' + kind + '_adjunction_presented_family B C C1',
                            '@' + kind + '_adjunction_presented_family B C')
                        native = native.replace('@one_cat_diagram_family_transf B WalkingArrow_cat C C1',
                            '@diagram_oplax_family_transf B WalkingArrow_cat C')
                        native = native.replace('@one_cat_diagram_family_reconstruction_evidence',
                            '@one_cat_oplax_diagram_family_reconstruction_evidence')
                        native = native.replace('@one_cat_arrow_family_comparison_evidence',
                            '@one_cat_oplax_arrow_family_comparison_evidence')
                        text += ('\n\n// Native view of the same original universality, modification and inverse data.\n'
                                 + native + '\n')
                        changes.append({'source': path, 'owner': 'native ' + kind + ' family-presentation evidence',
                                        'reason': 'Reuse the original modification evidence and actual native arrow-family comparison/reconstruction maps; no new universal or inverse witness',
                                        'ordinaryBodySha256': sha(ordinary_evidence), 'nativeBodySha256': sha(native)})
                if path == 'emdash3_2_one_cat_terminal_adjunction_family_observations.lp':
                    for kind in ('terminal', 'initial'):
                        for direction in ('to', 'from'):
                            for endpoint in ('src', 'tgt'):
                                name = f'one_cat_{kind}_adjunction_family_presentation_{direction}_{endpoint}_path'
                                marker = 'symbol ' + name + ' [B C : Cat]'
                                assert text.count(marker) == 1
                                start = text.index(marker)
                                end = text.index(';', start) + 1
                                ordinary_observation = text[start:end]
                                native = ordinary_observation.replace(name,
                                    f'one_cat_oplax_{kind}_adjunction_family_presentation_{direction}_{endpoint}_path')
                                native = native.replace('Functor_cat WalkingArrow_cat C',
                                    'Functor_oplax_cat WalkingArrow_cat C')
                                native = native.replace('@one_cat_transf_arrow_diagram_func B C C1',
                                    '@transf_arrow_diagram_func B C')
                                native = native.replace('@one_cat_' + kind + '_adjunction_presented_family B C C1',
                                    '@' + kind + '_adjunction_presented_family B C')
                                native = native.replace('@one_cat_' + kind + '_adjunction_family_presentation_evidence',
                                    '@one_cat_oplax_' + kind + '_adjunction_family_presentation_evidence')
                                native = native.replace('@one_cat_diagram_family_transf B WalkingArrow_cat C C1',
                                    '@diagram_oplax_family_transf B WalkingArrow_cat C')
                                native = native.replace('@one_cat_family_exchange_map_at B WalkingArrow_cat C C1',
                                    '@diagram_oplax_family_map_at B WalkingArrow_cat C')
                                native = native.replace('@one_cat_diagram_family_reconstruction_evidence',
                                    '@one_cat_oplax_diagram_family_reconstruction_evidence')
                                native = native.replace('@one_cat_arrow_family_comparison_evidence',
                                    '@one_cat_oplax_arrow_family_comparison_evidence')
                                native = native.replace('@one_cat_diagram_family_exchange_comp_path',
                                    '@one_cat_oplax_family_evaluation_comp_path')
                                signature = native.split('≔', 1)[0]
                                left_end = 'F' if kind == 'terminal' else '(@Const_func B C t)'
                                right_end = '(@Const_func B C t)' if kind == 'terminal' else 'F'
                                graph = f'(@transf_arrow_diagram_func B C {left_end} {right_end} h)'
                                presented = f'(@{kind}_adjunction_presented_family B C t e F)'
                                source, target = (graph, presented) if direction == 'to' else (presented, graph)
                                selected = f'(@iso_evidence_{direction} _ _ _ (@one_cat_oplax_{kind}_adjunction_family_presentation_evidence B C C1 t J F e h))'
                                endpoint_functor = left_end if endpoint == 'src' else right_end
                                native = signature + f'''≔ let X : τ (Functor B C) ≔ {endpoint_functor} in
  let alpha : τ (@Transf B C X X) ≔
    @diagram_oplax_family_map_at B WalkingArrow_cat C {source} {target} {selected} walking_arrow_{endpoint} in
  let beta : τ (@Transf B C X X) ≔ @id (Functor_cat B C) X in
  @hom_to_path (@Transf_cat B C X X) ((@one_cat_functor_category B C C1) X X)
    alpha beta (@one_cat_modification B C C1 X X alpha beta
      (λ b : τ (Obj B), @path_to_hom (Hom_cat C (fapp0 X b) (fapp0 X b))
        (@tapp0_fapp0 B C X X b alpha) (@tapp0_fapp0 B C X X b beta)
        (@eq_refl (Hom C (fapp0 X b) (fapp0 X b)) (@tapp0_fapp0 B C X X b beta))));'''
                                text += '\n\n// Native endpoint view of the same chosen maps and inverse laws.\n' + native + '\n'
                                changes.append({'source': path, 'owner': 'native ' + name,
                                                'reason': 'Observe the same selected native maps; derive whole endpoint identity from their actual components using the existing ordinary modification/reflection interface',
                                                'ordinaryBodySha256': sha(ordinary_observation), 'nativeBodySha256': sha(native)})
            if path == 'examples/one_cat_terminal_adjunction_families.lp':
                old = text
                text, count = re.subn(r'\bFunctor_cat\s+WalkingArrow_cat\s+C\b',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == 54, count
                assert text.count('(@TerminalObject (Op_cat C) t)') == 11
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                    '(@TerminalObject (TotalOp_cat C) t)')
                for before, after in (
                    ('@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at'),
                    ('@diagram_family_transf', '@diagram_oplax_family_transf'),
                    ('@diagram_evaluation_at_func', '@diagram_oplax_evaluation_at_func'),
                    ('@one_cat_diagram_family_reconstruction_evidence', '@one_cat_oplax_diagram_family_reconstruction_evidence'),
                    ('@one_cat_terminal_adjunction_family_presentation_evidence', '@one_cat_oplax_terminal_adjunction_family_presentation_evidence'),
                    ('@one_cat_initial_adjunction_family_presentation_evidence', '@one_cat_oplax_initial_adjunction_family_presentation_evidence'),
                ):
                    assert before in text, (path, before)
                    text = text.replace(before, after)
                assert len(re.findall(r'^assert\b', text, re.M)) == 12
                changes.append({'source': path, 'owner': 'native selected terminal/initial presentations and zero-column reviewer',
                                'reason': 'Retain all twelve original observations, actual selected terminal/initial maps and K/Q zero columns in the native diagram profile; the ordinary evidence interfaces remain in the owner',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_adjunction_zero_column_observations.lp',
                        'emdash3_2_one_cat_adjunction_zero_column_views.lp',
                        'examples/one_cat_adjunction_zero_column_views.lp'):
                old = text
                counts = {
                    'emdash3_2_one_cat_adjunction_zero_column_observations.lp': (432, 8),
                    'emdash3_2_one_cat_adjunction_zero_column_views.lp': (46, 2),
                    'examples/one_cat_adjunction_zero_column_views.lp': (74, 8),
                }
                expected_arrows, expected_initials = counts[path]
                assert text.count('(@TerminalObject (Op_cat C) t)') == expected_initials
                text, count = re.subn(r'\bFunctor_cat\s+WalkingArrow_cat\s+C\b',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == expected_arrows, (path, count)
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                    '(@TerminalObject (TotalOp_cat C) t)')
                for before, after in (
                    ('@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at'),
                    ('@diagram_family_transf', '@diagram_oplax_family_transf'),
                    ('@diagram_evaluation_at_func', '@diagram_oplax_evaluation_at_func'),
                    ('@diagram_evaluation_transf', '@diagram_oplax_evaluation_transf'),
                    ('@one_cat_diagram_family_evaluation_comp_path', '@one_cat_oplax_family_evaluation_comp_path'),
                    ('@one_cat_diagram_family_reconstruction_evidence', '@one_cat_oplax_diagram_family_reconstruction_evidence'),
                ):
                    text = text.replace(before, after)
                for kind in ('terminal', 'initial'):
                    text = text.replace('@one_cat_' + kind + '_adjunction_family_presentation_',
                        '@one_cat_oplax_' + kind + '_adjunction_family_presentation_')
                if path == 'emdash3_2_one_cat_adjunction_zero_column_observations.lp':
                    matches = list(re.finditer(r'(?m)^symbol one_cat_(?:kernel_counit|cokernel_unit)_zero_column_(?:to|from)_(?:src|tgt)_path\b.*?;', text, re.S))
                    assert len(matches) == 8
                    for match in reversed(matches):
                        signature = match.group().split('≔', 1)[0]
                        text = text[:match.start()] + signature + ordinary_identity_observation_body(signature) + text[match.end():]
                if path == 'emdash3_2_one_cat_adjunction_zero_column_views.lp':
                    views = fragment('production_zero_column_mate_paths.lpfragment')
                    for name in ('one_cat_cokernel_unit_source_transf_path',
                                 'one_cat_kernel_counit_target_transf_path'):
                        pattern = r'(?m)^symbol ' + name + r'\b.*?;'
                        previous = re.findall(pattern, text, re.S)
                        replacement = re.findall(pattern, views, re.S)
                        assert len(previous) == len(replacement) == 1, name
                        assert previous[0].split('≔', 1)[0] == replacement[0].split('≔', 1)[0], name
                        text = text.replace(previous[0], replacement[0])
                if path == 'examples/one_cat_adjunction_zero_column_views.lp':
                    for pattern, replacement, expected in (
                        (r'\bFunctor\s+WalkingArrow_cat\s+C\b',
                         'Obj (Functor_oplax_cat WalkingArrow_cat C)', 6),
                        (r'@Transf\s+WalkingArrow_cat\s+C\s+d\s+e\b',
                         'Hom (Functor_oplax_cat WalkingArrow_cat C) d e', 2),
                        (r'@fapp0\s+WalkingArrow_cat\s+C\b',
                         '@fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C)', 24),
                        (r'@fapp1_fapp0\s+WalkingArrow_cat\s+C\s+d\s+walking_arrow_src\s+walking_arrow_tgt\s+walking_arrow_generator',
                         '@fapp1_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d walking_arrow_tgt walking_arrow_src walking_arrow_generator', 2),
                        (r'@tapp1_fapp0\s+WalkingArrow_cat\s+C\s+d\s+e\s+walking_arrow_src\s+walking_arrow_tgt\s+u\s+walking_arrow_generator',
                         '@tapp1_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) e d walking_arrow_tgt walking_arrow_src u walking_arrow_generator', 2),
                    ):
                        text, count = re.subn(pattern, replacement, text)
                        assert count == expected, (path, pattern, count)
                    assert len(re.findall(r'^assert\b', text, re.M)) == 8
                changes.append({'source': path, 'owner': 'native zero-column endpoint and mate observations',
                                'reason': 'Retain the original selected maps and claims in the native profile; reflect the actual identity endpoint components and keep the mate-view composition/endpoint proof outline with derived transpose endpoint paths',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_adjunction_zero_columns.lp':
                old = text
                assert text.count('Functor_cat WalkingArrow_cat C') == 34
                assert text.count('(@TerminalObject (Op_cat C) t)') == 4
                text = text.replace('Functor_cat WalkingArrow_cat C',
                    'Functor_oplax_cat WalkingArrow_cat C')
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                    '(@TerminalObject (TotalOp_cat C) t)')
                for kind in ('terminal', 'initial'):
                    before = '@one_cat_' + kind + '_adjunction_family_presentation_evidence'
                    assert text.count(before) == 1
                    text = text.replace(before, '@one_cat_oplax_' + kind + '_adjunction_family_presentation_evidence')
                text = text.replace('@one_cat_diagram_family_reconstruction_evidence',
                    '@one_cat_oplax_diagram_family_reconstruction_evidence')
                text = text.replace('@diagram_family_transf', '@diagram_oplax_family_transf')
                text = text.replace('@diagram_evaluation_at_func', '@diagram_oplax_evaluation_at_func')
                changes.append({'source': path, 'owner': 'original native zero-column comparisons and mate inputs',
                                'reason': 'Retain all original comparison/composition bodies and P/Q choices in the native diagram and total-dual profiles',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_image_coimage_adjunction_families.lp',
                        'examples/image_coimage_adjunction_families.lp'):
                old = text
                reviewer = path.startswith('examples/')
                text, count = re.subn(r'Functor_cat\s+WalkingArrow_cat\s+C',
                    'Functor_oplax_cat WalkingArrow_cat C', text)
                assert count == (74 if reviewer else 26), count
                text, count = re.subn(r'\(@TerminalObject\s+\(Op_cat C\)\s+t\)',
                    '(@TerminalObject (TotalOp_cat C) t)', text)
                assert count == (16 if reviewer else 6), count
                for name in ('diagram_family_at_func', 'diagram_family_transf', 'diagram_evaluation_at_func'):
                    text = text.replace('@' + name, '@diagram_oplax_' + name.removeprefix('diagram_'))
                if reviewer:
                    text, count = re.subn(r'Functor\s+WalkingArrow_cat\s+C',
                        'Obj (Functor_oplax_cat WalkingArrow_cat C)', text)
                    assert count == 12, count
                    text = text.replace('@Transf WalkingArrow_cat C d e',
                        '@Hom (Functor_oplax_cat WalkingArrow_cat C) d e')
                    text = text.replace('@tapp0_fapp0 WalkingArrow_cat C _ _',
                        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _')
                    text = text.replace('@tapp0_fapp0 WalkingArrow_cat C d e',
                        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) e d')
                changes.append({'source': path, 'owner': 'native image/coimage families and original observations',
                                'reason': 'Align the same K/Q compositions and whiskerings with their native oplax diagram category and whole evaluator; retain the actual chosen structures and arbitrary diagram maps',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_one_cat_kernel_cokernel_transposes.lp',
                        'examples/one_cat_kernel_cokernel_transposes.lp'):
                old = text
                reviewer = path.startswith('examples/')
                assert text.count('Functor_cat WalkingArrow_cat C') == 28
                text = text.replace('Functor_cat WalkingArrow_cat C',
                    'Functor_oplax_cat WalkingArrow_cat C')
                assert text.count('(@TerminalObject (Op_cat C) t)') == (5 if reviewer else 2)
                text = text.replace('(@TerminalObject (Op_cat C) t)',
                    '(@TerminalObject (TotalOp_cat C) t)')
                if reviewer:
                    assert text.count('Functor WalkingArrow_cat C') == 6
                    text = text.replace('Functor WalkingArrow_cat C',
                        'Obj (Functor_oplax_cat WalkingArrow_cat C)')
                    text = text.replace('@Transf_cat WalkingArrow_cat C',
                        'Hom_cat (Functor_oplax_cat WalkingArrow_cat C)')
                    text = text.replace('@diagram_family_at_func', '@diagram_oplax_family_at_func')
                    text = text.replace('@diagram_evaluation_at_func', '@diagram_oplax_evaluation_at_func')
                    text = text.replace('@tapp0_fapp0 WalkingArrow_cat C _ _',
                        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _')
                    before = '@fapp1_fapp0 WalkingArrow_cat C d walking_arrow_src walking_arrow_tgt walking_arrow_generator'
                    assert text.count(before) == 2
                    text = text.replace(before,
                        '@fapp1_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d walking_arrow_tgt walking_arrow_src walking_arrow_generator')
                else:
                    for name in ('column_func', 'transf'):
                        before = '@one_cat_diagram_transpose_' + name
                        assert text.count(before) == 2
                        text = text.replace(before, '@one_cat_oplax_diagram_transpose_' + name)
                changes.append({'source': path, 'owner': 'native K/Q unit and counit transposes',
                                'reason': 'Preserve the original counit/unit construction, chosen P/Q and all observations at their actual native diagram profiles and total-dual initial-object hypothesis',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_diagram_transpose.lp':
                old = text
                text = text.replace('require open emdash.emdash3_2_arrow_diagram_families;',
                    'require open emdash.emdash3_2_one_cat_diagram_family_reflection;')
                replacements = [
                    ('@sym_func_func WalkingArrow_cat B C', '@one_cat_family_exchange_func WalkingArrow_cat B C C1', 1),
                    ('@transf_arrow_diagram_func I (Functor_cat B C)', '@one_cat_transf_arrow_diagram_func I (Functor_cat B C) (@one_cat_functor_category B C C1)', 1),
                    ('@sym_func B I C', '@one_cat_family_exchange B I C C1', 2),
                    ('@sym_func_func_transf B I C', '@one_cat_family_exchange_map B I C C1', 1),
                ]
                for before, after, expected in replacements:
                    assert text.count(before) == expected, before
                    text = text.replace(before, after)
                changes.append({'source': path, 'owner': 'ordinary whole diagram transposition',
                                'reason': 'Follow the original exchange/arrow-family/exchange construction through the existing guarded ordinary mapping presentations, retaining h and whole shape action',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
                addition = fragment('production_one_cat_oplax_transpose.lpfragment')
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'native-input whole diagram transposition',
                                'reason': 'Use the same original outline with native evaluation, ordinary prewhiskering and the existing native exchange; keep the ordinary-target guard and original h',
                                'insertedSha256': sha(addition)})
            if path == 'examples/one_cat_diagram_transpose.lp':
                old = text
                for before, after in [
                    ('@transf_arrow_diagram_func B C', '@one_cat_transf_arrow_diagram_func B C C1'),
                    ('@diagram_family_at_func B I C', '@one_cat_family_exchange_at_func B I C C1'),
                    ('@diagram_family_at_func B WalkingArrow_cat C', '@one_cat_family_exchange_at_func B WalkingArrow_cat C C1'),
                    ('@diagram_family_transf B WalkingArrow_cat C', '@one_cat_diagram_family_transf B WalkingArrow_cat C C1'),
                    ('@sym_transf_tapp0_transf B I C', '@one_cat_family_exchange_map_at B I C C1'),
                ]:
                    assert before in text, before
                    text = text.replace(before, after)
                changes.append({'source': path, 'owner': 'original ordinary transposition reviewer',
                                'reason': 'Keep every original observation at the ordinary exchange and arrow-family presentation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_omega_evaluation_points.lp':
                old = text
                marker = 'symbol omega_equiv_catd_at [K : Cat]'
                assert text.count(marker) == 1
                first, displayed = text.split(marker, 1)
                displayed, count = re.subn(r'(@(?:fapp0|tapp0_fapp0) K) Cat_cat',
                    r'\1 Cat_cart', displayed)
                assert count == 14, count
                text = (first + '// Evaluate in Cat_cart and retain the original ambient equivalence observation.\n'
                        + marker + displayed)
                changes.append({'source': path, 'owner': 'displayed whole equivalence at a point',
                                'reason': 'Evaluate the same family data in Cat_cart and retain its ambient Cat_cat result, both original inverse components and the two mapped unit laws',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/categorical_contractions.lp':
                old = text
                text, count = re.subn(r'(@(?:tapp0_fapp0|tapp1_func) K) Cat_cat',
                    r'\1 Cat_cart', text)
                assert count == 3
                target = 'Functor_cat Terminal_cat (@Fibre_cat K E y)'
                assert text.count(target) == 1
                text = text.replace(target, 'Functor_cart_cat Terminal_cat (@Fibre_cat K E y)')
                changes.append({'source': path, 'owner': 'original categorical-contraction reviewer',
                                'reason': 'Retain all five observations and both supplied inverses, reading the family component and whole Hom action in their actual Cartesian coefficient',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path in ('emdash3_2_eq1_hom_action.lp', 'examples/groupoidal_structured_j_eq1.lp'):
                old = text
                facade = 'Fibre_cat (@strict_functor C Cat_cat D)'
                expected = 2 if path == 'emdash3_2_eq1_hom_action.lp' else 4
                assert text.count(facade) == expected, path
                text = text.replace(facade, '@fapp0 C Cat_cat (@strict_functor C Cat_cat D)')
                if path == 'emdash3_2_eq1_hom_action.lp':
                    text = text.replace(
                        '  The displayed family is supplied as one classified `StrictFunctor`, so its',
                        '  The ordinary Cat-valued diagram retains its legacy `StrictFunctor` input.\n'
                        '  Use its actual object action, without imposing Cat_cart-family admission. Its')
                else:
                    observation = '  ≡ @fib_cov_transf C D x u;'
                    assert text.count(observation) == 1
                    text = text.replace(observation,
                        '  ≡ @strict_transfor C Cat_cart (@FibCov_source_catd C x) D\n'
                        '      (@fib_cov_transf C D x u);')
                    text = text.replace(
                        '// Structured groupoidal J is the existing directed-family action.',
                        '// Structured groupoidal J observes the ambient view of canonical fibre covariance.')
                    action = '(Path_cat A) Cat_cat D x x (@eq_refl A x)'
                    assert text.count(action) == 2
                    text = text.replace(action, '(Path_cat A) Cat_cart D x x (@eq_refl A x)')
                    carrier = '(Hom Cat_cat (Fibre_cat D x) (Fibre_cat D x))'
                    assert text.count(carrier) == 2
                    text = text.replace(carrier, '(Functor (Fibre_cat D x) (Fibre_cat D x))')
                changes.append({'source': path, 'owner': 'groupoidal_fibre_transport_equiv',
                                'reason': 'Evaluate the existing general Cat-valued diagram directly instead of using the now-specialised admitted-family facade; keep its input, arrow action, chosen inverse and proof body',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_shaped_pathout.lp':
                old = text
                cart_pair = '(Functor_cat I (Product_cat (Op_cat I) I))'
                component = '(Product_cat (Op_cat I) I)\n    Cat_cat\n    (@Unit_prof I)'
                assert text.count(cart_pair) == text.count(component) == 1
                text = text.replace(cart_pair,
                    '(Functor_cart_cat I (Product_cat (Op_cat I) I))', 1)
                text = text.replace(component,
                    '(Product_cat (Op_cat I) I)\n    Cat_cart\n    (@Unit_prof I)', 1)
                changes.append({'source': path,
                                'owner': 'shaped_fixed_source_pair_func / shaped_pathout_component',
                                'reason': 'Follow the Cartesian product-pair and profunctor coefficient annotations; retain the original fixed-source, totalization and higher-action bodies',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_pathout_transformation_reframing.lp':
                old = text
                start = text.index('symbol pathout_lhs_tele\n')
                end = text.index('symbol pathout_lhs_tele_source\n', start)
                telescope = text[start:end]
                assert telescope.count('Functor_cat') == 2
                text = text[:start] + telescope.replace('Functor_cat', 'Functor_cart_cat') + text[end:]
                proofs = fragment('production_pathout_reframing.lpfragment')
                for name in ('pathout_general_pre_lhs_tele_path',
                             'pathout_lhs_tele_transport_path',
                             'pathout_top_lhs_transport_path'):
                    marker = 'symbol ' + name + '\n'
                    assert text.count(marker) == proofs.count(marker) == 1
                    start = text.index(marker)
                    end = text.index(';', text.index('≔', start)) + 1
                    begin = proofs.index(marker)
                    finish = proofs.index(';', proofs.index('≔', begin)) + 1
                    text = text[:start] + proofs[begin:finish] + text[end:]
                text = text.replace(
                    '// The cold whole Cat-precomposition comparison identifies the stable\n// precomposition component with the same telescope source.',
                    '// Cartesian precomposition now computes the telescope source directly.\n// The fixed-target action uses the selected pre/right convention.')
                text = text.replace('symbol pathout_lhs_tele_transport_path\n',
                    '// Fixed-target internalization has strict pre/right action for any epsilon.\n// Compare through the core right-leg path, not a general left-leg equality.\n'
                    'symbol pathout_lhs_tele_transport_path\n', 1)
                changes.append({'source': path, 'owner': 'PathOut pre/right source reframing',
                                'reason': 'Keep the original statements and arbitrary lax epsilon; derive the two transport paths from the conventional pre action and existing right-leg comparison instead of the retired general left-leg equality',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_cubical_dependent_hom.lp':
                old = text
                marker = 'symbol homdc_target_func\n'
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index('≔', start)) + 1
                text = text[:start] + fragment('production_cubical_hom_evaluation.lpfragment').rstrip() + text[end:]
                assert text.count('(@hom_con_int\n') == 1
                assert text.count('(@hom_int C C') == 2
                # Keep the actual Cartesian result of hom_con_int: its next
                # totalization consumes that whole profile, not just objects.
                text = text.replace('(Catd_cat (Op_cat (Hom_cat K2 x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)')
                text = text.replace('(Catd_cat (Op_cat (Hom_cat C x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat C x2 y2)) Cat_cart)')
                text = text.replace('(@hom_int C C', '(@hom_int_view C C')
                text = text.replace(': Hom_K1(x1,y1) -> Catd(Hom_K2(x2,y2)^op).',
                    ': Hom_K1(x1,y1) -> Cart(T(Hom_K2(x2,y2)),Cat_cart).')
                changes.append({'source': path, 'owner': 'fixed-endpoint cubical Hom evaluation',
                                'reason': 'Use existing whole Cartesian component evaluation, preserve the original broad E input, and expose the actual Cartesian Hom result needed by totalization',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/cubical_dependent_hom.lp':
                old = text
                start = text.index('// The outer and inner hom actions')
                end = text.index('// A direct unit-profunctor', start)
                observations = text[start:end]
                assert observations.count('Cat_cat') == 2
                text = text[:start] + observations.replace('Cat_cat', 'Cat_cart') + text[end:]
                text = text.replace('(Catd_cat (Op_cat (Hom_cat K2 x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)')
                text = text.replace('(Catd_cat (Op_cat (Hom_cat C x2 y2)))',
                    '(Functor_cart_cat (Op_cat (Hom_cat C x2 y2)) Cat_cart)')
                changes.append({'source': path, 'owner': 'inner cubical Hom action',
                                'reason': 'Observe the actual admitted family coefficient; retain original leaf, both higher actions and twisted-boundary negative control',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_cubical_square_total.lp':
                old = text
                start = text.index('// Whole family of first projections')
                opposite = text.index('// Pointwise opposite retains', start)
                end = text.index('// At a, totalize the b-indexed filler family.', opposite)
                legacy = text[opposite:end]
                assert len(re.findall(r'(?m)^rule ', legacy)) == 3
                assert len(re.findall(r'(?m)^unif_rule ', legacy)) == 4
                disposition = '''// The seven former same-base Op clauses are retired. The four whole
// comparisons above use TotalOp over the R-shifted base. Their point
// observations use the native Sigma projection, capped Sigma-map and
// base-change owners. Cartesian composition and named-pullback source views
// have a checked proof-time comparison, not a common runtime normal form.
// The pinned original block and all seven dispositions are recorded in
// audits/strict-default-action-boundary/production_cubical_projection_point_review.md.

'''
                text = (text[:start] + fragment('production_cubical_sigma_projection.lpfragment')
                        + '\n' + fragment('production_cubical_projection_views.lpfragment') + '\n' + disposition + text[end:])
                text = text.replace('(Functor (Hom_cat K1 x1 y1) Cat_cat)',
                                    '(Functor (Hom_cat K1 x1 y1) Cat_cart)')
                source = '''    (Catd_cat (Op_cat (Hom_cat K2 x2 y2)))
    Cat_cat
    (@Sigma_func (Op_cat (Hom_cat K2 x2 y2)))'''
                assert text.count(source) == 1
                text = text.replace(source, '''    (Functor_cart_cat (Op_cat (Hom_cat K2 x2 y2)) Cat_cart)
    Cat_cart
    (@Sigma_coeff_func (Op_cat (Hom_cat K2 x2 y2)))''', 1)
                projection = '''    (@sigma_proj1_family_funcd
      (Hom_cat K1 x1 y1)
      (Op_cat (Hom_cat K2 x2 y2))
      (@homdc_ K1 K2 E x1 y1 x2 y2 u v));'''
                assert text.count(projection) == 1
                text = text.replace(projection, '''    (@strict_transfor _ _ _ _
      (@sigma_proj1_family_funcd
        (Hom_cat K1 x1 y1)
        (Op_cat (Hom_cat K2 x2 y2))
        (@homdc_ K1 K2 E x1 y1 x2 y2 u v)));''', 1)
                text = text.replace('by applying the existing `homd_int` to the pointwise\n  opposite inner edge total;',
                    'by applying the existing `homd_int` to the total-dual\n  inner edge family over its shifted outer base;')
                changes.append({'source': path, 'owner': 'varying Sigma projection and fixed-boundary total',
                                'reason': 'Use canonical Cartesian projection/formation and inherited strict-map action; preserve the broader fixed-endpoint E input',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text),
                                'redundantDirectIntrinsicRuleRemoved': 1,
                                'pendingLegacyOppositeRules': 0,
                                'pendingLegacyOppositeUnifiers': 0,
                                'correctedWholeProjectionViews': 4,
                                'qualifiedPointProjectionCases': 3,
                                'sourcePresentationAgreement': 'Proof-time congruence followed by actual Hom action; canonical pullback-source computation remains runtime',
                                'retiredLegacyBlockSha256': sha(legacy)})
            if path == 'emdash3_2_cubical_internalization.lp':
                old = text
                text = fragment('production_cubical_total_duality.lpfragment')
                changes.append({'source': path, 'owner': 'two-sided Homd/Sigma total and endpoint projections',
                                'reason': 'Admit the nested Cartesian family, shift the total-dual family base to O(K1), and derive the existing total and projections with O rather than the invalid same-base fibre opposite',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_gray_interchanger_orientation.lp':
                old = text
                readings = fragment('production_interchanger_source_reading.lpfragment')
                for name in ('gray_interchanger_common_func',
                             'gray_interchanger_source_common_path',
                             'gray_interchanger_lhs_tele_common_func_path',
                             'gray_interchanger_lhs_tele_post_composite_path'):
                    marker = 'protected symbol ' + name + '\n'
                    assert text.count(marker) == readings.count(marker) == 1
                    start = text.index(marker)
                    end = text.index(';', text.index('≔', start)) + 1
                    begin = readings.index(marker)
                    finish = readings.index(';', readings.index('≔', begin)) + 1
                    text = text[:start] + readings[begin:finish] + text[end:]
                start = text.index('protected symbol gray_interchanger_lhs_tele_func\n')
                end = text.index('protected symbol gray_interchanger_lhs_tele_value\n', start)
                telescope = text[start:end]
                assert telescope.count('Functor_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat') == 2
                text = text[:start] + telescope.replace(
                    'Functor_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat',
                    'Functor_cart_cat GrayInterchangerDomain_cat GrayInterchangerCodomain_cat') + text[end:]
                text = text.replace('// Common fixed-generator internal action selected by both whole strict paths.',
                    '// Shared left-hand presentation of the source endpoint and its telescope.\n'
                    '// It is not the pre/right middle action or a common value of both endpoints.')
                text = text.replace('// The two formal endpoints meet at the common internal action by the existing\n// whole displayed strict-naturality paths.',
                    '// The source endpoint and this left-hand presentation are the same value.\n'
                    '// The target retains its separate pre/right reading below.')
                text = text.replace('  The `lax_transfor` head makes the selected pre/right target judgmental; no\n  evidence-derived endpoint adapter, inverse, or independent interchanger is\n  added.',
                    '  The default conventional-lax action fixes the pre/right leg. No supplied\n'
                    '  comparison, inverse, or independent interchanger is added.')
                changes.append({'source': path, 'owner': 'interchanger source endpoint reading',
                                'reason': 'Use the actual post/left source and Cartesian telescope instead of the retired general left-leg equality; retain every public endpoint, cell and coordinate-swapped square',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_strict_functor_actions.lp':
                old = text
                begin = text.index('// Classified strict functors preserve ordinary isomorphism evidence.')
                end = text.index('/*\n  Selected named strict packages', begin)
                text = text[:begin] + fragment('production_default_inverse_action.lpfragment') + text[end:]
                marker = '/*\n  Left adjoints preserve weighted colimits.'
                assert text.count(marker) == 1
                text = text[:text.index(marker)] + fragment('production_weighted_colimit.lpfragment')
                text = text.replace(
                    '  selected inverses remain computational, and the ambient lax carrier gains\n  no equality.',
                    '  selected inverses remain computational. This legacy classified API now\n'
                    '  coexists with strict default functors; its wrappers await consumer migration\n'
                    '  and retirement. No strictness of arbitrary transformations is added.')
                changes.append({'source': path, 'owner': 'left-adjoint weighted-colimit preservation',
                                'reason': 'Default inverse action takes the ordinary strict functor directly, with legacy names as defined views; transpose the existing Hom comparison and retain the original three-step T-weighted proof without a second adjunction or supplied strictness evidence',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/cubical_square_total.lp':
                text += '\n' + fragment('production_cubical_sigma_projection_controls.lpfragment')
                text += '\n' + fragment('production_cubical_projection_point_controls.lpfragment')
            if path == 'examples/cubical_internalization.lp':
                old = text
                text = text.replace('are derived from ordinary Sigma, pointwise opposite, and homd_int.',
                    'are derived from ordinary Sigma, shifted total fibre duality, and homd_int.')
                text = text.replace('// The internal owner is literally the existing homd_int of the pointwise\n// opposite inner edge family.',
                    '// The internal owner is the existing homd_int of the total-dual inner\n// edge family over O(K1).')
                text = text.replace('(Catd_cat K2)', '(Functor_cart_cat K2 Cat_cart)')
                start = text.index('assert [K1 K2')
                end = text.index('// At a fixed', start)
                text = text[:start] + text[start:end].replace(
                    '      (Op_cat K1)', '      (TotalOp_cat K1)') + text[end:]
                controls = fragment('production_cubical_total_controls.lpfragment')
                split = controls.index('// The corrected total rejects')
                start = text.index('// At a fixed first side arrow')
                end = text.index('// The selected ordinary', start)
                text = text[:start] + controls[:split] + text[end:]
                text += '\n' + controls[split:]
                changes.append({'source': path, 'owner': 'corrected total-dual Hom reading and retained endpoints',
                                'reason': 'Replace the invalid ordinary-opposite-total comparison by the actual inner Hom; retain square/endpoint observations and reject reversed or erased fillers',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_action_paths.lp':
                marker = 'symbol one_cat_composition_path '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @eq_refl (Hom B (@fapp0 A B F x) (@fapp0 A B F z))
    (@fapp1_fapp0 A B F x z (@comp_fapp0 A x y z g f));'''
                text = text[:begin] + replacement + text[end:]
                changes.append({'source': path, 'owner': 'one_cat_composition_path',
                                'reason': 'Existing lax-cell proof no longer joins after strict-default compositor normalization; preserve its statement and use strict computation',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
            if path == 'emdash3_2_represented_comma_families.lp':
                marker = 'protected symbol comma_basechange_sigma_map_composition '
                assert text.count(marker) == 1
                addition = fragment('production_comma_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'before': marker,
                                'reason': 'Map the actual identity-compositor inverse evidence through original whiskering instead of imposing additional runtime projection laws',
                                'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_observation_pre_points '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                post_points = text[start:end].replace('comma_basechange_observation_pre',
                                                      'comma_basechange_observation_post')
                post_points = post_points.replace('comma_basechange_observation_inner',
                                                  'comma_basechange_observation_outer')
                replacement = '''≔ λ z : τ (Obj (@Sigma_cat A (@Pullback_catd A K E F))),
  let pre : τ (@OmegaEquivAlong
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comma_basechange_observation_inner A K C F E P)
      (@comma_basechange_observation_middle A K C F E P)
      (@comma_basechange_observation_pre A K C F E P))
    ≔ @comma_strict_omega_map
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) (Product_cat K C))
      (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C)
      (@comp_cat_cov_func (@Sigma_cat A (@Pullback_catd A K E F))
        (Product_cat K C) C (@Product_projR_func K C))
      (@comma_basechange_sigma_basechange_right A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_middle A K F E (@Const_catd K C) P)
      (@comma_basechange_sigma_basechange_pre A K F E (@Const_catd K C) P)
      (@comma_pre_cell_omega (@Catd_cat K) Cat_cat
        (@comma_basechange_sigma_basechange_source A K F) (@Sigma_func K)
        (@sigma_pullback_total_transf A K F)
        E (@Const_catd K C) (@Const_catd K C) P (@id (@Catd_cat K) (@Const_catd K C))) in
  @comma_strict_omega_map
    (Functor_cat (@Sigma_cat A (@Pullback_catd A K E F)) C) C
    (@fapp0_func (@Sigma_cat A (@Pullback_catd A K E F)) C z)
    (@comma_basechange_observation_inner A K C F E P)
    (@comma_basechange_observation_middle A K C F E P)
    (@comma_basechange_observation_pre A K C F E P) pre;'''
                text = text[:begin] + replacement + '\n\n' + post_points + text[end:]
                changes.append({'source': path, 'owner': 'comma_basechange_observation_pre_points',
                                'reason': 'Map inverse evidence of the extracted default pre cell through the original projection, then evaluate at an arbitrary total object',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement),
                                'postPointsSha256': sha(post_points)})
                marker = 'protected symbol comma_basechange_observation_pre_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index(';', text.index('≔', start)) + 1
                post_equiv = text[start:end].replace('comma_basechange_observation_pre',
                                                     'comma_basechange_observation_post')
                post_equiv = post_equiv.replace('comma_basechange_observation_inner',
                                                'comma_basechange_observation_outer')
                text = text[:end] + '\n\n' + post_equiv + text[end:]
                marker = 'protected symbol comma_basechange_observation_basechange_component '
                assert text.count(marker) == 1
                addition = fragment('production_comma_basechange_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_observation_basechange_equiv',
                                'reason': 'The old second-step reflexivity no longer follows the newly mapped pre inverse; retain both comparison maps and compose their inverse evidence',
                                'postEquivSha256': sha(post_equiv), 'insertedSha256': sha(addition)})
                marker = 'protected symbol comma_basechange_gamma_target_link_equiv '
                assert text.count(marker) == 1
                start = text.index(marker)
                begin = text.index('≔', start)
                end = text.index(';', begin) + 1
                old = text[begin:end]
                replacement = '''≔ @one_cat_transf_pointwise_omega_along K Y Y1
    (@comma_section_gamma_target_observed_op K X Y J A D h)
    (@represented_comma_hom_action_target_func K X Y J A D h)
    (@comma_basechange_gamma_target_link K X Y J A D h Y1)
    (λ x : τ (Obj K), @comma_op_omega_along Y
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw0 K X Y J A D h) x)
      (@fapp0 (Op_cat K) (Op_cat Y) (@comma_basechange_gamma_target_raw2 K X Y J A D h) x)
      (@tapp0_fapp0 (Op_cat K) (Op_cat Y)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h) x
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1))
      (@comma_strict_omega_map (Functor_cat (Op_cat K) (Op_cat Y)) (Op_cat Y)
        (@fapp0_func (Op_cat K) (Op_cat Y) x)
        (@comma_basechange_gamma_target_raw0 K X Y J A D h)
        (@comma_basechange_gamma_target_raw2 K X Y J A D h)
        (@comma_basechange_gamma_target_raw_link K X Y J A D h Y1)
        (@comma_basechange_gamma_target_raw_link_equiv K X Y J A D h Y1)));'''
                text = text[:begin] + replacement + text[end:]
                addition = fragment('production_comma_target_equivalence.lpfragment')
                text = text.replace(marker, addition + '\n' + marker, 1)
                changes.append({'source': path, 'owner': 'comma_basechange_gamma_target_link_equiv',
                                'reason': 'Preserve the original comparison and construct its inverse evidence before evaluating components',
                                'insertedSha256': sha(addition),
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
                # The original target comparison and its selected inverses
                # run in O(K), O(Y). Internal-Hom inputs remain over T(K).
                target_before = text
                raw_start = 'protected symbol comma_basechange_gamma_target_raw0 '
                raw_end = '// Group the original mapped graph section.'
                assert text.count(raw_start) == text.count(raw_end) == 1
                r1, r2 = text.index(raw_start), text.index(raw_end)
                raw = text[r1:r2]
                assert raw.count(theta_type) == 11
                assert raw.count(theta_type.replace('@hom_int_view ', '@hom_int ')) == 3
                raw = raw.replace(theta_type.replace('@hom_int_view ', '@hom_int '), theta_type)
                raw = raw.replace(theta_type, 'COMMA_RAW_THETA_TYPE')
                assert (raw.count('Op_cat'), raw.count('Op_func'), raw.count('Op_transf')) == (151, 8, 1)
                raw = (raw.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                       .replace('Op_transf', 'TotalOp_transf').replace('@one_cat_op ', '@one_cat_total_op ')
                       .replace('@comma_op_omega_along ', '@comma_total_op_omega_along '))
                raw = raw.replace('COMMA_RAW_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                assert raw.count(target_projection) == 6
                raw = raw.replace(target_projection, '(@strict_transfor _ _ _ _ ' + target_projection + ')')
                link = 'protected symbol comma_basechange_gamma_target_link '
                assert raw.count(link) == 1
                raw = raw.replace(link, fragment('production_comma_target_reframe_view.lpfragment') + '\n' + link, 1)
                text = text[:r1] + raw + text[r2:]
                op_evidence = 'protected symbol comma_op_omega_along '
                oe = text.index(op_evidence); oe_end = text.index(';', text.index('≔', oe)) + 1
                old = text[oe:oe_end]
                text = text[:oe] + old.replace('comma_op_omega_along', 'comma_total_op_omega_along').replace('Op_cat', 'TotalOp_cat') + text[oe_end:]
                grouped_start = '// Group the original mapped graph section.'
                classify_start = '// Classify the target section and retain the whole target inverse.'
                ordinary_target = '// Original Γ interface, specialized to the native Hom action of h.'
                g1, g2 = text.index(grouped_start), text.index(classify_start)
                grouped = text[g1:g2]
                assert grouped.count(theta_type) == 2
                grouped = grouped.replace(theta_type, 'COMMA_GROUPED_THETA_TYPE')
                assert grouped.count('Op_cat') == 19 and grouped.count('Op_func') == 0
                grouped = grouped.replace('Op_cat', 'TotalOp_cat')
                grouped = grouped.replace('COMMA_GROUPED_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                text = text[:g1] + grouped + text[g2:]
                c1, c2 = text.index(classify_start), text.index(ordinary_target)
                classification = text[c1:c2]
                projections = fragment('production_comma_target_projections.lpfragment')
                projection_names = ('comma_classification_target_projection',
                                    'comma_classification_middle_projection',
                                    'comma_classification_identity_section_projected')
                for name in projection_names:
                    marker = 'protected symbol ' + name
                    assert classification.count(marker) == projections.count(marker) == 1
                    p1 = classification.index(marker); p2 = classification.index(';', classification.index('≔', p1)) + 1
                    classification = classification[:p1] + name.upper() + classification[p2:]
                assert classification.count(theta_type) == 14
                classification = classification.replace(theta_type, 'COMMA_CLASSIFICATION_THETA_TYPE')
                assert (classification.count('Op_cat'), classification.count('Op_func'), classification.count('Op_transf')) == (53, 7, 1)
                classification = (classification.replace('Op_cat', 'TotalOp_cat')
                                  .replace('Op_func', 'TotalOp_func').replace('Op_transf', 'TotalOp_transf'))
                classification = classification.replace('COMMA_CLASSIFICATION_THETA_TYPE', theta_type.replace('@Transf', '@StrictTransfor', 1))
                for name in projection_names:
                    p1 = projections.index('protected symbol ' + name); p2 = projections.index(';', projections.index('≔', p1)) + 1
                    classification = classification.replace(name.upper(), projections[p1:p2])
                text = text[:c1] + classification + text[c2:]
                ordinary = text[text.index(ordinary_target):]
                assert ordinary.count('@tapp1_int_fapp0_transf') == 3
                text = text[:text.index(ordinary_target)] + ordinary.replace('@tapp1_int_fapp0_transf', '@tapp1_int_cart')
                changes.append({'source': path, 'owner': 'whole represented-comma target comparison and classification',
                                'reason': 'Preserve the original selected inverse data and OneCat target premise, correct the total-dual bases and coefficient views, and retain the ordinary-lax public wrappers through canonical admission',
                                'oldBodySha256': sha(target_before), 'newBodySha256': sha(text)})
            if path == 'emdash3_2_one_cat_op.lp':
                addition = fragment('production_one_cat_total_dual.lpfragment')
                text += '\n' + addition
                changes.append({'source': path, 'owner': 'one_cat_total_op',
                                'reason': 'Ordinary-target comparison now uses total duality; retain the original ordinary-category premise through explicit discrete-profile closure',
                                'declaredBoundary': 'Discrete classifier closure under total duality; no operational chosen inverse or caller proof added',
                                'insertedSha256': sha(addition)})
            if path == 'examples/represented_comma_families.lp':
                old = text
                # The original arbitrary-section rejection observes the O
                # total projection; the seven Theta inputs still use T(K).
                pre, post = text.split('assert [A K : Cat]', 1)
                assert pre.count('Op_cat') == 11 and pre.count('Op_func') == 4
                pre = pre.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
                text = pre + 'assert [A K : Cat]' + post
                assert text.count('(theta : τ (@Transf (Op_cat K)') == 7
                text = text.replace('(theta : τ (@Transf (Op_cat K)', '(theta : τ (@StrictTransfor (Op_cat K)')
                assert text.count('@hom_int ') == 16
                text = text.replace('@hom_int ', '@hom_int_view ')
                assert text.count('@tapp0_fapp0 K Cat_cat') == 1
                text = text.replace('@tapp0_fapp0 K Cat_cat', '@tapp0_fapp0 K Cat_cart', 1)
                assert text.count(' x theta)) (@id K x)') == 1
                text = text.replace(' x theta)) (@id K x)', ' x (@strict_transfor _ _ _ _ theta))) (@id K x)', 1)
                fibre = '(@homdc_fibre X Y (@represented_comma_prof X Y J)'
                assert text.count(fibre) == 1
                text = text.replace(fibre, '(@homdc_fibre X Y\n'
                    '  (@comp_cat_fapp0 (Op_cat X) (Functor_cart_cat Y Cat_cart) (Catd_cat Y)\n'
                    '    (Functor_cart_include Y Cat_cart) (@represented_comma_prof X Y J))', 1)
                text = text.replace('// Whole internal-Hom input: it need not be presented as the action of h.',
                    '// Whole internal-Hom input with the admitted strict x-profile;\n'
                    '// its displayed y-components remain lax. It need not be presented\n'
                    '// as the canonical action of an ordinary transformation h.')
                changes.append({'source': path, 'owner': 'original represented-comma reviewer',
                                'reason': 'Retain all original observations with corrected total duality, valid Theta profile and actual coefficient views; ordinary eta inputs remain lax',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            if path == 'examples/gray_profiles.lp':
                old = '''assertnot [A B : Cat]
  [X Y Z : τ (Obj A)]
  (g : τ (Hom A Y Z))
  (f : τ (Hom A X Y)) ⊢
  @strict_functor_compositor_lhs
    A B (@example_unprofiled_functor A B) X Y Z g f
  ≡ @strict_functor_compositor_rhs
      A B (@example_unprofiled_functor A B) X Y Z g f;'''
                assert text.count(old) == 1
                replacement = old.replace('assertnot ', 'assert ', 1)
                text = text.replace(old, replacement, 1)
                text = text.replace('// Rigid ambient negative control, deliberately outside StrictFunctor.',
                                    '// Ambient functor: the strict default no longer requires a wrapper.')
                text = text.replace('// Composition is selected only by the stable evidence-bearing view.',
                                    '// The legacy stable view still computes during wrapper migration.')
                changes.append({'source': path, 'owner': 'unprofiled compositor endpoint comparison',
                                'reason': 'The default functor now preserves composition; retain all unrelated negative controls',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(replacement)})
                old = text
                text = text.replace('K Cat_cat E D', 'K Cat_cart E D')
                marker = '// The target/right reading is available only through the strict profile.'
                assert text.count(marker) == 1
                start = text.index(marker)
                end = text.index('// Every opaque classified object', start)
                section = text[start:end].replace(
                    '(Functor_cat (Fibre_cat E x) (Fibre_cat D y))',
                    '(Functor_cart_cat (Fibre_cat E x) (Fibre_cat D y))', 1)
                section = section.replace(marker,
                    '// The legacy strict-profile observation agrees with the default pre/right action.')
                text = text[:start] + section + text[end:]
                text = text.replace(
                    '// An ambient compositor is typed between its two retained endpoints; those\n// endpoints are no longer convertible, so a literal identity comparison is\n// not even the appropriate judgment.',
                    '// An ambient compositor has the same endpoints under the strict default.\n// Its native intrinsic extraction is retained.')
                changes.append({'source': path, 'owner': 'displayed-profile observations',
                                'reason': 'Retain the original assertions with the actual family coefficient and whole Hom target; ordinary extracted-cell properties keep Functor_cat',
                                'oldBodySha256': sha(old), 'newBodySha256': sha(text)})
            freyd_entry = finish_freyd_entry(path, text)
            if freyd_entry is not None:
                changes.append({'source': path, 'owner': 'native Freyd entry and shared whole OneCat comparisons',
                                'reason': 'Retain native input/map data through the actual coefficient inclusion and typed constructor; share existing derived reflection, preserve whole Hom factorization and use its actual normalization views without new runtime rules',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(freyd_entry)})
                text = freyd_entry
            terminal_family = finish_terminal_family(path, text)
            if terminal_family is not None:
                changes.append({'source': path, 'owner': 'whole terminal-family and native diagram reflection',
                                'reason': 'Use the existing oplax family presentation and fixed evaluation, retaining whole maps, inverse data and original observations; derive whole reflection without additional formal rules',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(terminal_family)})
                text = terminal_family
            cokernel_inputs = finish_cokernel_inputs(path, text)
            if cokernel_inputs is not None:
                changes.append({'source': path, 'owner': 'original whole cokernel inputs and native reconstruction views',
                                'reason': 'Use the actual native exchange and retained reconstruction maps; derive endpoint comparisons through existing ordinary-target modifications, and keep ordinary reconstruction tests on their original interface',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(cokernel_inputs)})
                text = cokernel_inputs
            kernel_cokernel_paths = finish_kernel_cokernel_paths(path, text)
            if kernel_cokernel_paths is not None:
                changes.append({'source': path, 'owner': 'native kernel/cokernel whole paths and component comparison',
                                'reason': 'Preserve the original whole statements and selected mates at the native coefficient; compare all parents and transfor data at a shared evaluation point without changing runtime action',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(kernel_cokernel_paths)})
                text = kernel_cokernel_paths
            cokernel_reconstruction = finish_cokernel_reconstruction(path, text)
            if cokernel_reconstruction is not None:
                changes.append({'source': path, 'owner': 'whole native cokernel projection and reconstruction',
                                'reason': 'Use the existing fixed-postcomposition Hom owner, retain literal mate classifiers at the whole comparison boundary, and preserve actual quotient and inverse data',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(cokernel_reconstruction)})
                text = cokernel_reconstruction
            native_row_laws = finish_native_row_laws(path, text)
            if native_row_laws is not None:
                changes.append({'source': path, 'owner': 'original whole zero and short-exact family laws',
                                'reason': 'Retain the selected row maps and inverses at native diagram coefficients; compare complete Cat composites before inferred middle categories',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(native_row_laws)})
                text = native_row_laws
            kernel_reconstruction = finish_kernel_reconstruction(path, text)
            if kernel_reconstruction is not None:
                changes.append({'source': path, 'owner': 'original whole kernel input and reconstruction chain',
                                'reason': 'Use native exchange and the selected inverse mate with literal Hom classifiers, preserving the whole lift, precomposition and reconstruction observations',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(kernel_reconstruction)})
                text = kernel_reconstruction
            row_observations = finish_row_observations(path, text)
            if row_observations is not None:
                changes.append({'source': path, 'owner': 'original row cancellation and zero-cone observations',
                                'reason': 'Reuse whole mate/whiskering comparisons and the existing partial Hom-action owner while retaining actual row maps and inverse witnesses',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(row_observations)})
                text = row_observations
            constant_rows = finish_constant_rows(path, text)
            if constant_rows is not None:
                changes.append({'source': path, 'owner': 'constant transformation inclusion and original whole Freyd row paths',
                                'reason': 'Use the existing strict-transformation inclusion in constant postcomposition and its original whole row consumers',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(constant_rows)})
                text = constant_rows
            constant_chain = finish_constant_chain(path, text)
            if constant_chain is not None:
                changes.append({'source': path, 'owner': 'original whole constant-chain and native row-zero proofs',
                                'reason': 'Use native diagram coefficients and the existing weakening/constant transformation inclusions without new rules',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(constant_chain)})
                text = constant_chain
            kernel_columns = finish_kernel_columns(path, text)
            if kernel_columns is not None:
                changes.append({'source': path, 'owner': 'original kernel pullback and zero-cone column construction',
                                'reason': 'Retain selected comparisons/inverses and use existing whole projection/associativity owners at corrected profiles',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(kernel_columns)})
                text = kernel_columns
            native_column_entry = finish_native_column_entry(path, text)
            if native_column_entry is not None:
                changes.append({'source': path, 'owner': 'kernel point recovery and original Freyd column inputs/comparisons',
                                'reason': 'Use native fixed evaluation and the existing ordinary-to-native inclusion before the same cokernel functor, retaining actual comparison/inverse data',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(native_column_entry)})
                text = native_column_entry
            column_projection = finish_column_projection(path, text)
            if column_projection is not None:
                changes.append({'source': path, 'owner': 'original homology-cover and whole column projection paths',
                                'reason': 'Use native evaluation and the existing included boundary comparison in the original cokernel-naturality proof',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(column_projection)})
                text = column_projection
            family_actions = finish_family_actions(path, text)
            if family_actions is not None:
                changes.append({'source': path, 'owner': 'original square and kernel/cokernel/homology family actions',
                                'reason': 'Reuse native whole exchange/evaluation and existing canonical/raw mate comparisons; keep product-path families in Cat_cart',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(family_actions)})
                text = family_actions
            column_paths = finish_column_homology_paths(path, text)
            if column_paths is not None:
                changes.append({'source': path, 'owner': 'original native column diagram and homology comparisons',
                                'reason': 'Use existing native mapping profiles, fixed evaluation and reflection while retaining the original whole proofs and data',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(column_paths)})
                text = column_paths
            homology_records = finish_homology_records(path, text)
            if homology_records is not None:
                changes.append({'source': path, 'owner': 'original adjunction and H-map record observations',
                                'reason': 'Retain selected mates and record data through native reflection, evaluation and actual reconstruction-map inclusion',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(homology_records)})
                text = homology_records
            factor_h_reviewers = finish_factor_h_reviewers(path, text)
            if factor_h_reviewers is not None:
                changes.append({'source': path, 'owner': 'original factor and whole H reviewers',
                                'reason': 'Retain original reconstruction/projection assertions at existing native diagram and Hom profiles',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(factor_h_reviewers)})
                text = factor_h_reviewers
            diagram_mate_reviewers = finish_diagram_mate_reviewers(path, text)
            if diagram_mate_reviewers is not None:
                changes.append({'source': path, 'owner': 'original diagram evaluation and whole-mate reviewers',
                                'reason': 'Use actual ordinary/oplax profiles and existing projection ladders, retaining original assertion kinds, polarities and data',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(diagram_mate_reviewers)})
                text = diagram_mate_reviewers
            adjunction_reviewers = finish_adjunction_reviewers(path, text)
            if adjunction_reviewers is not None:
                changes.append({'source': path, 'owner': 'original exchange and adjunction reviewers',
                                'reason': 'Retain general opposite-profile exchange and Cartesian controls, total duality and the original whole adjunction computations',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(adjunction_reviewers)})
                text = adjunction_reviewers
            ordinary_reviewers = finish_ordinary_reviewers(path, text)
            if ordinary_reviewers is not None:
                changes.append({'source': path, 'owner': 'ordinary terminal equivalence records and reviewers',
                                'reason': 'Retain the actual public mapped inverse in existing native records and preserve original ordinary observations',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(ordinary_reviewers)})
                text = ordinary_reviewers
            remaining_action = finish_remaining_action_reviewers(path, text)
            if remaining_action is not None:
                changes.append({'source': path, 'owner': 'remaining action-profile observations',
                                'reason': 'Retain general encoded oplax evaluation, selected inverses, strict-default laws and runtime distinctions',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(remaining_action)})
                text = remaining_action
            telescope_reviewers = finish_precomp_telescope_reviewers(path, text)
            if telescope_reviewers is not None:
                changes.append({'source': path, 'owner': 'precomposition and telescope observations',
                                'reason': 'Retain whole native Cartesian action and its ordinary included observations at the selected default',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(telescope_reviewers)})
                text = telescope_reviewers
            action_controls = finish_action_controls(path, text)
            if action_controls is not None:
                changes.append({'source': path, 'owner': 'legacy action controls under selected defaults',
                                'reason': 'Retain old assertions with explicit strict-functor and conventional-pre dispositions; preserve post-leg and mixed noncollapse controls',
                                'oldBodySha256': sha(text), 'newBodySha256': sha(action_controls)})
                text = action_controls
            target = package / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        for command in re.findall(r'(?m)^\s*require(?:\s+open)?\s+([^;]+);', text):
            for module in command.split():
                assert re.fullmatch(r'emdash(?:\.[A-Za-z0-9_]+)+', module), module
                stage(module.removeprefix('emdash.').replace('.', '/') + '.lp')

    stage('examples/gray_profiles.lp')
    stage('examples/cubical_dependent_hom.lp')
    stage('examples/cubical_square_total.lp')
    stage('examples/cubical_internalization.lp')
    stage('examples/cubical_internalization_composition.lp')
    stage('examples/gray_interchanger.lp')
    stage('examples/gray_interchanger_orientation.lp')
    stage('examples/profunctor_weighted_limits.lp')
    stage('examples/groupoidal_structured_j_eq1.lp')
    stage('examples/diagram_evaluation.lp')
    stage('examples/arrow_diagram_families.lp')
    stage('examples/zero_arrow_diagrams.lp')
    stage('examples/zero_arrow_cone_maps.lp')
    stage('examples/one_cat_zero_cone_fibre_inclusion.lp')
    stage('examples/one_cat_diagram_map_equivalences.lp')
    stage('examples/homology_family_point_diagrams.lp')
    stage('examples/kernel_cokernel_adjunction_observations.lp')
    stage('examples/one_cat_zero_cone_maps.lp')
    stage('examples/one_cat_zero_arrow_inputs.lp')
    stage('examples/one_cat_zero_cone_map_equivalences.lp')
    stage('examples/introduced_terminal_input_comparisons.lp')
    stage('examples/one_cat_chain_pair_native_maps.lp')
    stage('examples/freyd_native_inputs.lp')
    stage('examples/freyd_native_maps.lp')
    stage('examples/freyd_native_row_families.lp')
    stage('examples/one_cat_whiskering_paths.lp')
    stage('emdash3_2_commutative_algebra_freyd_adjunction_models.lp')
    stage('emdash3_2_one_cat_family_naturality_paths.lp')
    stage('examples/one_cat_terminal_family_universality.lp')
    stage('examples/zero_arrow_family_observations.lp')
    stage('emdash3_2_one_cat_diagram_family_paths.lp')
    stage('examples/one_cat_cokernel_family_inputs.lp')
    stage('emdash3_2_zero_arrow_family_action_paths.lp')
    stage('examples/action_profile_profile_action_path_controls.lp')
    stage('emdash3_2_adjunction_untranspose_naturality.lp')
    stage('examples/one_cat_cokernel_family_descent.lp')
    stage('examples/one_cat_cokernel_family_reconstruction.lp')
    stage('examples/one_cat_short_exact_families.lp')
    stage('emdash3_2_one_cat_kernel_family_restriction_paths.lp')
    stage('examples/one_cat_kernel_family_lift.lp')
    stage('examples/one_cat_kernel_precomposition.lp')
    stage('examples/one_cat_kernel_family_reconstruction.lp')
    stage('examples/one_cat_short_exact_family_cancellation.lp')
    stage('emdash3_2_one_cat_zero_cone_row_families.lp')
    stage('examples/one_cat_constant_transformation_views.lp')
    stage('emdash3_2_commutative_algebra_freyd_native_row_paths.lp')
    stage('examples/one_cat_constant_chain_zeros.lp')
    stage('emdash3_2_commutative_algebra_freyd_native_row_zeros.lp')
    stage('emdash3_2_commutative_algebra_freyd_native_row_short_exact.lp')
    stage('examples/one_cat_kernel_pullback_universality.lp')
    stage('examples/one_cat_zero_cone_column_inputs.lp')
    stage('emdash3_2_commutative_algebra_freyd_native_column_input_comparisons.lp')
    stage('emdash3_2_commutative_algebra_freyd_native_column_homology_comparisons.lp')
    stage('examples/homology_family_point_comparisons.lp')
    stage('examples/one_cat_homology_cover_maps.lp')
    stage('examples/freyd_native_column_comparisons.lp')
    stage('examples/one_cat_homology_family_maps.lp')
    stage('examples/functor_category_unit_views.lp')
    stage('examples/product_family_views.lp')
    stage('examples/product_family_action_views.lp')
    stage('examples/freyd_native_column_homology_paths.lp')
    stage('examples/freyd_native_middle_column_comparisons.lp')
    stage('examples/one_cat_zero_diagram_inputs.lp')
    stage('examples/one_cat_adjunction_records.lp')
    stage('examples/one_cat_chain_pair_homology_records.lp')
    stage('examples/freyd_adjunction_homology.lp')
    stage('examples/one_cat_chain_pair_homology_maps.lp')
    stage('examples/freyd_adjunction_homology_maps.lp')
    stage('examples/freyd_adjunction_model_observations.lp')
    stage('examples/one_cat_image_coimage_factor_reconstruction.lp')
    stage('examples/one_cat_chain_pair_inputs.lp')
    stage('examples/zero_arrow_cone_adjunction_homology.lp')
    stage('examples/zero_composite_adjunction_homology.lp')
    stage('examples/one_cat_image_coimage_factors.lp')
    stage('examples/walking_arrow_diagram_evaluation.lp')
    stage('examples/arrow_diagram_point_usability.lp')
    stage('examples/one_cat_adjunction_family_zero_inputs.lp')
    stage('examples/adjunction_exchange_computation.lp')
    stage('examples/adjunction_exchange_op_identity.lp')
    stage('examples/adjunction_family_constant_views.lp')
    stage('examples/adjunction_triangles.lp')
    stage('examples/one_cat_diagram_reconstruction.lp')
    stage('examples/one_cat_native_square_paths.lp')
    stage('examples/one_cat_slice_paths.lp')
    stage('examples/one_cat_terminal_adjunctions.lp')
    stage('examples/kernels_cokernels.lp')
    stage('examples/weak_kernels.lp')
    stage('examples/additive_categories.lp')
    stage('examples/abelian_categories.lp')
    stage('examples/abelian_fiber_pushout_stability.lp')
    stage('examples/computational_fiber_products_pushouts.lp')
    stage('examples/preabelian_bimorphism_lemmas.lp')
    stage('examples/commutative_ring_freyd_additive.lp')
    stage('examples/emdash3_2_commutative_algebra_freyd_preadditive_class_laws_example.lp')
    stage('examples/emdash3_2_commutative_algebra_freyd_preadditive_example.lp')
    stage('examples/emdash3_2_commutative_algebra_matrix_additive_laws_example.lp')
    stage('examples/emdash3_2_commutative_algebra_presentation_additive_operations_example.lp')
    stage('examples/commutative_ring_freyd_cartesian.lp')
    stage('examples/commutative_ring_freyd_terminal_zero.lp')
    stage('examples/commutative_ring_freyd_direct_sums.lp')
    stage('examples/commutative_ring_freyd_binary_products.lp')
    stage('examples/action_profile_canonical_pre_product_orders.lp')
    stage('examples/action_profile_canonical_pre_product_specializations.lp')
    stage('examples/action_profile_postcomp_profile_controls.lp')
    stage('examples/action_profile_vertical_profile_controls.lp')
    stage('examples/action_profile_vertical_ambient_category_control.lp')
    stage('examples/action_profile_vertical_identity_paths.lp')
    stage('examples/action_profile_vertical_terminal_controls.lp')
    stage('examples/action_profile_vertical_unit_controls.lp')
    stage('examples/action_profile_precomp_minimal_all_orders.lp')
    stage('examples/action_profile_precomp_minimal_mixed_controls.lp')
    stage('examples/action_profile_telescope_profile_paths.lp')
    stage('examples/action_profile_telescope_profile_controls.lp')
    stage('examples/action_profile_telescope_projection_controls.lp')
    stage('examples/action_profile_telescope_unit_overlap_controls.lp')
    stage('examples/action_profile_canonical_sigma_basechange_controls.lp')
    stage('examples/action_profile_circle_retained_inverse_controls.lp')
    stage('examples/action_profile_diagonal_pair_projection_view_controls.lp')
    stage('examples/action_profile_native_component_agreement_review.lp')
    stage('examples/action_profile_native_residual_view_controls.lp')
    stage('examples/action_profile_pointwise_profile_controls.lp')
    stage('examples/action_profile_sheaf_baseline_helper_controls.lp')
    stage('examples/action_profile_walking_cross_category_controls.lp')
    stage('emdash3_2_kernel_maps.lp')
    stage('emdash3_2_cokernel_maps.lp')
    stage('emdash3_2_hom_factor_zero_descent.lp')
    stage('emdash3_2_normal_mono_epic_factors.lp')
    stage('emdash3_2_cokernel_monic_factor_descent.lp')
    stage('emdash3_2_cokernel_composite_comparison.lp')
    stage('emdash3_2_equivalence_conjugation_paths.lp')
    stage('emdash3_2_omega_equiv_right_factor.lp')
    stage('emdash3_2_iso_comparison_reconstruction.lp')
    stage('examples/kernel_maps.lp')
    stage('examples/cokernel_maps.lp')
    stage('examples/cokernel_composite_comparison.lp')
    stage('examples/normal_mono_epic_factors.lp')
    stage('examples/cokernel_monic_factor_descent.lp')
    stage('examples/omega_equiv_right_factor.lp')
    stage('emdash3_2_computational_homology.lp')
    stage('emdash3_2_homology_map_isos.lp')
    stage('emdash3_2_homology_map_corrections.lp')
    stage('emdash3_2_homology_map_kernel_covers.lp')
    stage('emdash3_2_abelian_homology_cokernel_inclusion.lp')
    stage('examples/homology_maps.lp')
    stage('examples/homology_cokernel_inclusion.lp')
    stage('examples/abelian_image_bimorphisms.lp')
    stage('examples/abelian_images.lp')
    stage('examples/cokernel_record_covers.lp')
    stage('examples/computational_homology.lp')
    stage('examples/homology_map_corrections.lp')
    stage('examples/homology_record_boundary_factors.lp')
    stage('examples/homology_records.lp')
    stage('examples/short_exact_sequences.lp')
    stage('emdash3_2_chain_pair_cycle_factors.lp')
    stage('emdash3_2_exactness_reindex.lp')
    for reviewer in ('dependent_simplex_bridge', 'dependent_simplex_profiles',
                     'dependent_simplex_native_dimensions', 'dependent_simplex_path_associator',
                     'dependent_simplex_represented_source', 'simplex_shapes',
                     'chain_pair_native_triangles', 'chain_pair_map_cycle_lifts',
                     'computational_exactness_reindex'):
        stage('examples/' + reviewer + '.lp')
    # Existing Hom-factor and chain-map consumers qualify unchanged at the
    # corrected lax-arrow total and strict-default action owners.
    for reviewer in (
        'hom_factor_cubical', 'chain_pair_cubical_maps',
        'hom_factor_spaces', 'hom_factor_source_isos', 'hom_factor_views',
        'hom_factor_comparison_pasting', 'hom_factor_epic_descent',
        'hom_factor_chain_zero', 'hom_factor_universality',
        'chain_pair_maps', 'chain_pair_diagram_maps',
    ):
        stage('examples/' + reviewer + '.lp')
    stage('examples/kernel_cokernel_adjunctions.lp')
    stage('examples/adjunction_mates.lp')
    stage('examples/one_cat_adjunction_families.lp')
    stage('examples/action_profile_inherited_assembly_controls.lp')
    stage('examples/represented_comma_families.lp')
    stage('examples/action_profile_prof_defiso_controls.lp')
    stage('examples/one_cat_arrow_diagrams.lp')
    stage('examples/one_cat_arrow_family_isomorphisms.lp')
    stage('examples/one_cat_diagram_family_reconstruction.lp')
    stage('examples/commutative_ring_presheaf_invertibility.lp')
    stage('examples/one_cat_zero_arrow_family_classification.lp')
    stage('examples/homology_adjunction_families.lp')
    stage('examples/one_cat_homology_family_comparison.lp')
    stage('examples/one_cat_homology_family_comparison_points.lp')
    stage('emdash3_2_one_cat_terminal_adjunction_family_observations.lp')
    stage('examples/one_cat_modifications.lp')
    stage('examples/categorical_contractions.lp')
    stage('examples/one_cat_diagram_transpose.lp')
    stage('examples/image_coimage_adjunction_families.lp')
    stage('examples/one_cat_kernel_cokernel_transposes.lp')
    stage('examples/one_cat_adjunction_zero_column_views.lp')
    stage('examples/one_cat_terminal_adjunction_families.lp')
    stage('examples/walking_endomorphism_hit.lp')
    stage('examples/action_profile_walking_named_rec_controls.lp')
    stage('examples/action_profile_walking_named_overlap_controls.lp')
    stage('examples/walking_circle_completion.lp')
    stage('examples/walking_circle_groupoidification_restriction.lp')
    stage('examples/action_profile_eckmann_hilton_one_hom.lp')
    stage('examples/generic_groupoidification.lp')
    stage('examples/generic_groupoidification_interval.lp')
    stage('examples/walking_interval_groupoidification.lp')
    stage('examples/monads_comonads.lp')
    stage('examples/triangular_binary_products.lp')
    stage('examples/cartesian_categories.lp')
    stage('examples/triangular_binary_products_finite_limits.lp')
    stage('examples/pullbacks.lp')
    stage('examples/slice_dependent_products.lp')
    # Preserve the real production diagnostic dependency closure as the next
    # integration boundary. Its unchanged assertions are not automatically
    # qualified by the focused owner checks below.
    stage('emdash3_2_checks.lp')
    stage('examples/one_cat_adjunction_family_views.lp')
    stage('examples/walking_arrow_native_observation.lp')
    (package / 'one_cat_evaluation_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        + fragment('production_one_cat_evaluation_controls.lpfragment'))
    (package / 'one_cat_mapping_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        + fragment('production_one_cat_mapping_controls.lpfragment'))
    (package / 'mapping_evaluation_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        'require emdash.one_cat_mapping_controls;\n'
        + fragment('production_one_cat_mapping_evaluation_controls.lpfragment'))
    (package / 'walking_arrow_postcomposition_controls.lp').write_text(
        'require open emdash.emdash3_2_walking_arrow_introduction;\n'
        + fragment('production_walking_arrow_postcomposition_controls.lpfragment'))
    (package / 'one_cat_family_exchange.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        'require open emdash.emdash3_2_one_cat_functor_closure;\n'
        'require open emdash.emdash3_2_functor_reconstruction_paths;\n'
        + fragment('production_one_cat_family_exchange.lpfragment'))
    (package / 'one_cat_family_exchange_controls.lp').write_text(
        'require open emdash.one_cat_family_exchange;\n'
        'require emdash.one_cat_mapping_controls;\n'
        + fragment('production_one_cat_family_exchange_controls.lpfragment'))
    (package / 'one_cat_double_exchange_controls.lp').write_text(
        'require open emdash.one_cat_family_exchange;\n'
        'require emdash.one_cat_family_exchange_controls;\n'
        + fragment('production_one_cat_double_exchange_controls.lpfragment'))
    (package / 'one_cat_arrow_family_integration.lp').write_text(
        'require emdash.examples.one_cat_arrow_family_isomorphisms;\n'
        'require emdash.one_cat_double_exchange_controls;\n')
    (package / 'one_cat_evaluation_integration.lp').write_text(
        'require emdash.diagram_with_adjunction_views;\n'
        'require emdash.one_cat_evaluation_controls;\n'
        'require emdash.examples.walking_arrow_native_observation;\n')
    (package / 'diagram_with_adjunction_views.lp').write_text(
        'require open emdash.emdash3_2;\n'
        'require emdash.emdash3_2_one_cat_adjunction_family_views;\n'
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        'require emdash.examples.diagram_evaluation;\n'
        + fragment('production_diagram_import_controls.lpfragment'))
    (package / 'one_cat_arrow_profile_controls.lp').write_text(
        'require open emdash.examples.one_cat_arrow_diagrams;\n'
        + fragment('production_one_cat_arrow_controls.lpfragment'))
    stage('emdash3_2_one_cat_hom_comparison_data.lp')
    stage('examples/one_cat_hom_comparison_data.lp')
    stage('examples/one_cat_adjunction_introduction.lp')
    stage('examples/fibrewise_sigma.lp')
    stage('examples/sieve_extensions.lp')
    stage('examples/direct_cover_questions.lp')
    stage('examples/direct_cover_question_families.lp')
    stage('examples/direct_cover_internal_sheaves.lp')
    stage('examples/direct_cover_completion_hit.lp')
    stage('examples/direct_cover_completion_eliminator.lp')
    for path in SELECTED_PRESENTATION_SOURCES:
        stage(path)
    for path in SELECTED_RECORD_VIEW_SOURCES:
        stage(path)
    for path in KERNEL_BOUNDARY_PREREQUISITE_SOURCES:
        stage(path)
    for path in KERNEL_ADDITIVE_PREREQUISITE_SOURCES:
        stage(path)
    for path in CONNECTING_KERNEL_CHAIN_SOURCES:
        stage(path)
    for path in NATIVE_CONNECTING_CONSUMER_SOURCES:
        stage(path)
    (package / 'direct_cover_question_regression.lp').write_text(
        (package / 'examples/direct_cover_questions.lp').read_text() + '\n'
        + (package / 'examples/direct_cover_question_families.lp').read_text())
    original_checks = subprocess.check_output(
        ['git', 'show', PIN + ':emdash2/emdash3_2_checks.lp'], cwd=root, text=True)
    sheaf_start = '// catalog-area: Constructed Cat-valued sheafification reflector'
    sheaf_end = '/* End of the CS-12s constructed Cat-valued sheafification diagnostics. */'
    for target_package, checks_source in (
        (baseline_package, original_checks),
        (package, (package / 'emdash3_2_checks.lp').read_text()),
    ):
        assert checks_source.count(sheaf_start) == checks_source.count(sheaf_end) == 1
        selected = checks_source[checks_source.index(sheaf_start):checks_source.index(sheaf_end)+len(sheaf_end)]
        (target_package / 'direct_cover_sheafification_controls.lp').write_text(
            'require open emdash.emdash3_2_direct_cover_sheafification;\n' + selected + '\n')
    locality_start = '// catalog-area: Strict pointwise equivalences and direct-cover locality'
    locality_end = '/* End of the CS-12q conventional direct-cover locality diagnostics. */'
    assert original_checks.count(locality_start) == original_checks.count(locality_end) == 1
    locality_controls = original_checks[original_checks.index(locality_start):original_checks.index(locality_end)+len(locality_end)]
    displayed_hom = '(@Functor_cat (@Fibre_cat K E x) (@Fibre_cat K D x))'
    assert locality_controls.count(displayed_hom) == 1
    locality_controls = locality_controls.replace(displayed_hom,
        displayed_hom.replace('@Functor_cat', '@Functor_cart_cat'), 1)
    (package / 'locality_profile_controls.lp').write_text(
        (package / 'examples/action_profile_inherited_assembly_controls.lp').read_text()
        + '\n' + locality_controls + '\n')
    locality_source = (package / 'emdash3_2_direct_cover_completion_locality.lp').read_text()
    locality_boundary = '// Fibrewise whole equivalences are the pointwise evidence for rho[m].'
    assert locality_source.count(locality_boundary) == 1
    controls_boundary = '// The second inverse and whole locality have their conventional public types.'
    assert locality_controls.count(controls_boundary) == 1
    (package / 'locality_fibre_prefix.lp').write_text(
        locality_source[:locality_source.index(locality_boundary)] + '\n'
        + locality_controls[:locality_controls.index(controls_boundary)] + '\n'
        + fragment('production_pointwise_coefficient_control.lpfragment'))
    (package / 'inverse_endpoint_paths.lp').write_text(
        'require open emdash.emdash3_2_strict_pointwise_equivalences;\n'
        'require open emdash.emdash3_2_eq1_evidence_property;\n'
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_inverse_endpoint_paths.lpfragment'))
    (package / 'inverse_post_endpoint_paths.lp').write_text(
        (package / 'inverse_endpoint_paths.lp').read_text() + '\n'
        + fragment('production_inverse_post_endpoint_path.lpfragment'))
    (package / 'inverse_post_admission_boundary.lp').write_text(
        'require open emdash.inverse_post_endpoint_paths;\n'
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_inverse_post_admission_boundary.lpfragment'))
    (package / 'inverse_unit_profiles.lp').write_text(
        'require open emdash.emdash3_2_strict_pointwise_equivalences;\n'
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_inverse_unit_profiles.lpfragment'))
    (package / 'inverse_cell_reflection.lp').write_text(
        'require open emdash.inverse_unit_profiles;\n'
        'require open emdash.emdash3_2_eq1_hom_action;\n'
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_strict_cell_reflection.lpfragment'))
    (package / 'internal_composite_action_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_internal_composite_action_controls.lpfragment'))
    (package / 'inverse_represented_unit.lp').write_text(
        'require open emdash.inverse_cell_reflection;\n'
        'require open emdash.internal_composite_action_controls;\n'
        'require open emdash.emdash3_2_gray_profiles;\n'
        'require open emdash.emdash3_2_strict_pointwise_equivalences;\n'
        + fragment('production_inverse_represented_unit.lpfragment'))
    (package / 'represented_laxity_boundary.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_represented_laxity_boundary.lpfragment'))
    (package / 'represented_laxity_controls.lp').write_text(
        'require open emdash.represented_laxity_boundary;\n'
        + fragment('production_represented_laxity_controls.lpfragment'))
    (package / 'whiskering_equivalences.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_whiskering_equivalences.lpfragment'))
    (package / 'inverse_admission.lp').write_text(
        'require open emdash.inverse_represented_unit;\n'
        'require open emdash.whiskering_equivalences;\n'
        'require open emdash.emdash3_2_eq1_evidence_property;\n'
        'require open emdash.represented_laxity_boundary;\n'
        'require open emdash.represented_laxity_controls;\n'
        + fragment('production_inverse_admission.lpfragment'))
    (package / 'cartesian_inverse_laws.lp').write_text(
        'require open emdash.inverse_admission;\n'
        + fragment('production_cartesian_inverse_laws.lpfragment'))
    (package / 'cartesian_inverse_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_pointwise_equivalences;\n'
        'require emdash.examples.gray_profiles;\n'
        + fragment('production_cartesian_inverse_controls.lpfragment') + '\n'
        + fragment('production_pointwise_coefficient_control.lpfragment'))
    (package / 'inverse_locality_regression.lp').write_text(
        'require emdash.cartesian_inverse_controls;\n'
        'require emdash.locality_profile_controls;\n')
    psss_start = '// catalog-area: Cat-valued presheaf facade and restriction'
    psss_end = '/* End of the PSSS-02 higher-sieve diagnostics. */'
    assert original_checks.count(psss_start) == original_checks.count(psss_end) == 1
    psss = original_checks[original_checks.index(psss_start):original_checks.index(psss_end)+len(psss_end)]
    original_psss = psss
    psss = psss.replace('Cat_cat', 'Cat_cart')
    postcomp = '@hom_con_int_postcomp_func K K (@id_func K) V U p'
    assert psss.count(postcomp) == 2
    psss = psss.replace(postcomp, '@strict_transfor _ _ _ _ (' + postcomp + ')')
    higher_sieve_comparison = '''(@HigherSieve_cat K U)
      (@Catd_cat (@Into_restr_cat K U))'''
    assert psss.count(higher_sieve_comparison) == 1
    psss = psss.replace(higher_sieve_comparison, '''(@HigherSieve_cat K U)
      (Functor_cart_cat (@Into_restr_cat K U) Cat_cart)''', 1)
    psss = psss.replace('// Both higher-sieve presentations compare to this stable Catd intermediary.',
        '// The varying-base classifier has Cartesian diagram maps; the ordinary\n// presheaf facade retains its separate lax-map category.')
    psss = psss.replace('// Experimental unifiers are not transitively chained at runtime.',
        '// These categories have different mapping profiles, while their objects agree.')
    psss = psss.replace('// Restriction of higher sieves reuses Catd pullback along the arrow-total map.',
        '// Restriction of higher sieves is Cartesian precomposition along the arrow-total map.')
    pullback = '''@Pullback_catd_func
      (@Into_restr_cat K V)
      (@Into_restr_cat K U)
      (@fapp1_fapp0 K Cat_cart (@arrow_into_catd K) V U p)'''
    assert psss.count(pullback) == 1
    psss = psss.replace(pullback, '''@comp_cat_con_cart_func
      (@Into_restr_cat K V) (@Into_restr_cat K U) Cat_cart
      (@fapp1_fapp0 K Cat_cart (@arrow_into_catd K) V U p)''', 1)
    (package / 'presheaf_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_presheaves;\n' + psss + '\n'
        + fragment('production_presheaf_profile_controls.lpfragment'))
    changes.append({'source': 'emdash3_2_checks.lp/PSSS-01/PSSS-02',
                    'owner': 'original presheaf and higher-sieve diagnostics',
                    'reason': 'Preserve the raw presheaf facade; use actual Cartesian inclusion for Yoneda and the selected Cartesian higher-sieve classifier/restriction, with explicit ordinary inclusion and directed-filler controls',
                    'oldBodySha256': sha(original_psss), 'newBodySha256': sha(psss)})
    sieve_start = '// catalog-area: Ordinary subterminal sieves and pullback'
    sieve_end = '/* End of the PSSS-03a ordinary-sieve diagnostics. */'
    assert original_checks.count(sieve_start) == original_checks.count(sieve_end) == 1
    sieve_controls = original_checks[original_checks.index(sieve_start):original_checks.index(sieve_end)+len(sieve_end)]
    assert sieve_controls.count('Cat_cat') == 1
    sieve_controls = sieve_controls.replace('Cat_cat', 'Cat_cart')
    (package / 'sieve_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_sieves;\n' + psss + '\n' + sieve_controls + '\n'
        + fragment('production_presheaf_profile_controls.lpfragment'))
    # Reuse the original central sections already adapted and checked in
    # focused owners. The full diagnostic retains every original tail.
    central = (package / 'emdash3_2_checks.lp').read_text()
    for start_marker, end_marker, replacement in (
        (locality_start, locality_end, locality_controls),
        (psss_start, psss_end, psss),
        (sieve_start, sieve_end, sieve_controls),
    ):
        assert central.count(start_marker) == central.count(end_marker) == 1
        first = central.index(start_marker)
        last = central.index(end_marker, first) + len(end_marker)
        previous = central[first:last]
        assert previous == original_checks[original_checks.index(start_marker):
            original_checks.index(end_marker) + len(end_marker)]
        central = central[:first] + replacement + central[last:]
        changes.append({'source': 'emdash3_2_checks.lp',
                        'owner': start_marker.removeprefix('// catalog-area: '),
                        'reason': 'Integrate the exact previously adapted original section from its focused reviewer, without omitting assertions or changing its scope',
                        'oldBodySha256': sha(previous), 'newBodySha256': sha(replacement)})
    represented_coefficient = r'Cat_cat(\s+)(\(@(?:hom_|hom_con|Rep_catd)\b)'
    # Three former matches are now owned by the complete Homd-classifier block.
    assert len(list(re.finditer(represented_coefficient, central))) == 17
    before_represented_tags = central
    central = re.sub(represented_coefficient, r'Cat_cart\1\2', central)
    changes.append({'source': 'emdash3_2_checks.lp',
                    'owner': 'remaining direct represented-family coefficient observations',
                    'reason': 'Correct only coefficient arguments immediately followed by a known hom_/hom_con/Rep_catd family producer; retain ordinary Cat composition and unrelated Cat-valued diagrams',
                    'oldBodySha256': sha(before_represented_tags), 'newBodySha256': sha(central)})
    algebra_marker = '// catalog-area: Set-carrier commutative-ring objects'
    comma_marker = '// catalog-area: Whole comma projection and displayed laxity'
    assert central.count(algebra_marker) == central.count(comma_marker) == 1
    algebra_start = central.index(algebra_marker)
    algebra_end = central.index(comma_marker, algebra_start)
    algebra = central[algebra_start:algebra_end]
    old_algebra = algebra
    for old, new in (
        ('(Functor (Op_cat K) Cat_cat)', '(Functor (Op_cat K) Cat_cart)'),
        ('(Functor K Cat_cat)', '(Functor K Cat_cart)'),
        ('(Hom Cat_cat A (@Catd_cat (Op_cat B)))',
         '(Functor A (Functor_cart_cat (Op_cat B) Cat_cart))'),
    ):
        assert algebra.count(old) == 2, old
        algebra = algebra.replace(old, new)
    central = central[:algebra_start] + algebra + central[algebra_end:]
    changes.append({'source': 'emdash3_2_checks.lp',
                    'owner': 'original commutative-algebra represented-family comparisons',
                    'reason': 'Name the existing Cat_cart coefficient and the actual Cartesian target of the whole Hom owner; retain every algebra assertion, comparison body and negative runtime boundary',
                    'oldBodySha256': sha(old_algebra), 'newBodySha256': sha(algebra)})
    profiles_marker = '// catalog-area: Strict functor/transfor profiles and profiled Gray hom'
    assert central.count(profiles_marker) == 1
    comma_start = central.index(comma_marker)
    comma_end = central.index(profiles_marker, comma_start)
    old_comma = central[comma_start:comma_end]
    comma = fragment('production_central_comma_action_controls.lpfragment') + '\n'
    for block in (old_comma, comma):
        assert len(re.findall(r'^\s*assert\s', block, re.M)) == 33
        assert len(re.findall(r'^\s*assertnot\s', block, re.M)) == 3
    central = central[:comma_start] + comma + central[comma_end:]
    changes.append({'source': 'emdash3_2_checks.lp',
                    'owner': 'original whole comma and ordinary internal action diagnostics',
                    'reason': 'Use total-dual identity graphs, the actual intrinsic-modification direction, native contravariant Hom views and Cat_cart displayed coefficients; restrict only the two direct-transpose comparisons to their declared StrictTransfor input',
                    'oldBodySha256': sha(old_comma), 'newBodySha256': sha(comma)})
    structural_tail_marker = '// catalog-area: Enhanced triangular binary-product computation'
    assert central.count(structural_tail_marker) == 1
    profiles_start = central.index(profiles_marker)
    structural_tail_start = central.index(structural_tail_marker, profiles_start)
    profiles = central[profiles_start:structural_tail_start]
    old_profiles = profiles
    for old, new in (
        ('// Opaque strict functor objects carry the stable action view. GrayHom_lax\n// selects classified lax arrows over those objects.',
         '// Legacy strict-functor views remain until wrapper retirement. GrayHom_lax\n// still selects classified lax arrows over those admitted objects.'),
        ('// A Catd-valued codomain is not evidence that an arbitrary ambient functor\n// preserves composition.\nassertnot [A K : Cat]',
         '// Public functors preserve composition by default, also at a Catd-valued\n// codomain without an additional strict wrapper.\nassert [A K : Cat]'),
        ('// Composition computation is guarded by the strict-functor view.',
         '// The same default composition computation is observed through the legacy view.'),
        ('// The exact existing whole pre/right cell is identity only at the profile.',
         '// The classified lax view retains the default pre/right identity computation.'),
        ('// Ambient functors are not silently promoted into the strict object sort.',
         '// Until wrapper retirement, the legacy admitted object sort is still distinct\n// syntactically from the now-strict public Functor carrier.'),
        ('''assertnot [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  [W X Y : τ (Obj A)]
  (h : τ (Hom A W X)) ⊢
  @strict_transfor_pre_naturality_lhs_func''',
         '''// The conventional-lax default identifies this pre/right whole action.
assert [A B : Cat] [F G : τ (Functor A B)]
  (epsilon : τ (Transf F G))
  [W X Y : τ (Obj A)]
  (h : τ (Hom A W X)) ⊢
  @strict_transfor_pre_naturality_lhs_func'''),
    ):
        assert profiles.count(old) == 1, old
        profiles = profiles.replace(old, new)
    central = central[:profiles_start] + profiles + central[structural_tail_start:]
    changes.append({'source': 'emdash3_2_checks.lp',
                    'owner': 'original strict profiles, closure and groupoidification diagnostics',
                    'reason': 'Retain all existing declarations, profile/closure data and noncollapse controls; change only the two obsolete lax-default negatives explained by strict public functors and conventional pre/right action',
                    'oldBodySha256': sha(old_profiles), 'newBodySha256': sha(profiles)})
    structural_tail_start = central.index(structural_tail_marker)
    structural_tail = central[structural_tail_start:]
    old_structural_tail = structural_tail
    pairing_type = '''assert [C : Cat]
  [P : τ (Functor (Product_cat C C) C)]
  (BP : τ (@BinaryProducts C P))
  (X Y A0 A1 : τ (Obj C)) ⊢
  @tapp1_func'''
    assert structural_tail.count(pairing_type) == 1
    first = structural_tail.index(pairing_type)
    last = structural_tail.index(';', first) + 1
    pairing = structural_tail[first:last]
    assert pairing.count('(Op_cat C) Cat_cat') == 3
    assert pairing.count('(Functor_cat\n') == 1
    pairing = pairing.replace('(Op_cat C) Cat_cat', '(Op_cat C) Cat_cart')
    pairing = pairing.replace('(Functor_cat\n', '(Functor_cart_cat\n')
    structural_tail = structural_tail[:first] + pairing + structural_tail[last:]
    for old, new in (
        ('@fapp0 C Cat_cat (@SliceSigma_catd C) X',
         '@fapp0 (CoAt2_cat C) Cat_cart (@SliceSigma_catd C) X'),
        ('@fapp0 (Op_cat C) Cat_cat (@SliceBaseChange_catd C PB) X',
         '@fapp0 (Op_cat C) Cat_cart (@SliceBaseChange_catd C PB) X'),
        ('    (Op_cat C) Cat_cat\n    (@SliceBaseChange_catd C PB)',
         '    (Op_cat C) Cat_cart\n    (@SliceBaseChange_catd C PB)'),
        ('@fapp0 C Cat_cat (@SliceDependentProduct_catd C PB DP) X',
         '@fapp0 (CoAt2_cat C) Cat_cart (@SliceDependentProduct_catd C PB DP) X'),
        ('@fapp1_fapp0 C Cat_cat\n    (@SliceDependentProduct_catd C PB DP)',
         '@fapp1_fapp0 (CoAt2_cat C) Cat_cart\n    (@SliceDependentProduct_catd C PB DP)'),
        ('(@hom_con_int_postcomp_func C C (@id Cat_cat C) X Y f)',
         '''(@strict_transfor (Op_cat C) Cat_cart
            (@hom_con C X C (@id Cat_cat C))
            (@hom_con C Y C (@id Cat_cat C))
            (@hom_con_int_postcomp_func C C (@id Cat_cat C) X Y f))'''),
    ):
        assert structural_tail.count(old) == 1, old
        structural_tail = structural_tail.replace(old, new)
    central = central[:structural_tail_start] + structural_tail
    changes.append({'source': 'emdash3_2_checks.lp',
                    'owner': 'original product, pullback and dependent-product diagnostics',
                    'reason': 'Observe pairing in its actual Cartesian coefficient Hom, slice families on their declared bases, and the ordinary inclusion of represented postcomposition; retain all selected structures, whole inverse maps and assertions',
                    'oldBodySha256': sha(old_structural_tail), 'newBodySha256': sha(structural_tail)})
    (package / 'emdash3_2_checks.lp').write_text(central)
    groupoid_start = '// catalog-area: Internal groupoidality and structured J'
    groupoid_end = '// Phase 9 discrete-category core and homwise adequacy.'
    (package / 'central_groupoidality_controls.lp').write_text(
        'require open emdash.emdash3_2_eq1_hom_action;\n'
        + central[central.index(groupoid_start):central.index(groupoid_end)])
    early_start = '// Elementary decoded H0 classifiers, constructors, and dependent eliminators.'
    early_end = '// catalog-area: Groupoid-universe identity view'
    assert central.count(early_start) == central.count(early_end) == 1
    (package / 'central_early_controls.lp').write_text(
        central[:central.index('require open')]
        + 'require open emdash.emdash3_2_eq1_evidence_property;\n'
        + central[central.index(early_start):central.index(early_end)])
    action_end = '// catalog-area: Constant-domain displayed evaluation'
    assert central.count(action_end) == 1
    (package / 'central_action_controls.lp').write_text(
        central[:central.index('require open')]
        + 'require open emdash.emdash3_2_eq1_evidence_property;\n'
        + central[central.index(early_end):central.index(action_end)])
    hom_action_end = 'assert [K : Cat] (E D : τ (Catd K)) ⊢\n  @eq_refl Cat_grpd (Hom_cat (Catd_cat K) E D)'
    (package / 'central_displayed_products_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[central.index(hom_action_end):central.index(action_end)])
    displayed_eval_end = '// catalog-area: Displayed dependent chain'
    (package / 'central_displayed_evaluation_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[central.index(action_end):central.index(displayed_eval_end)])
    displayed_chain_end = central.index('// catalog-area: auto', central.index(displayed_eval_end))
    (package / 'central_displayed_chain_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[central.index(displayed_eval_end):displayed_chain_end])
    ordinary_adjunction_end = central.index('// Monad/Kleisli computation and opposite-derived comonads.', displayed_chain_end)
    (package / 'central_evaluation_adjunction_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[displayed_chain_end:ordinary_adjunction_end])
    monads_end = central.index('// catalog-area: auto', ordinary_adjunction_end)
    (package / 'central_monads_controls.lp').write_text(
        'require open emdash.emdash3_2_monads;\n'
        + central[ordinary_adjunction_end:monads_end])
    ordinary_action_end = central.index('// Pre-configured four-cell interchange', monads_end)
    (package / 'central_internal_action_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + central[monads_end:ordinary_action_end])
    intrinsic_start = central.index('  @Fibre_transf_app\n    K E\n', ordinary_action_end)
    path_induction_end = central.rfind('assert [', ordinary_action_end, intrinsic_start)
    (package / 'central_path_induction_controls.lp').write_text(
        'require open emdash.emdash3_2_profiled_interchange;\n'
        + central[ordinary_action_end:path_induction_end])
    intrinsic_end = central.index('assert [A B : Cat] (x : τ (Obj A)) (y : τ (Obj B)) ⊢\n  sigma_Fst', intrinsic_start)
    (package / 'central_intrinsic_projection_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[path_induction_end:intrinsic_end])
    pair_telescope_end = central.index('assert [A B C : Cat]\n  (F G : τ (Functor (Product_cat A B) C)) ⊢\n  @fapp1_func', intrinsic_end)
    (package / 'central_pair_telescope_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[intrinsic_end:pair_telescope_end])
    curry_end = central.index('assert [Z : Cat] (x y : τ (Obj Z)) (p : τ (Hom Z x y))\n  (E : τ (Catd (@PathOut_cat Z x))) ⊢', pair_telescope_end)
    (package / 'central_curry_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[pair_telescope_end:curry_end]
        + '\n' + fragment('production_lax_curry_controls.lpfragment').split(
            '// Both canonical whole objects agree with the original ordinary Hom views.', 1)[0])
    family_end = central.index('assert [K : Cat] (E : τ (Catd K)) ⊢\n  fapp1_fapp0 (Pi_func K)', curry_end)
    (package / 'central_family_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[curry_end:family_end])
    section_end = central.index('// Migrated Cartesian exchange and diagonal observations.', family_end)
    (package / 'central_sections_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[family_end:section_end])
    exchange_end = central.index('assert [A B : Cat] (F : τ (Functor A B)) (E : τ (Catd B))\n  (s : τ (Obj (@Functord_cat', section_end)
    (package / 'central_structural_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[section_end:exchange_end])
    reindex_end = central.index('// Mixed-action foundation', exchange_end)
    (package / 'central_reindex_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[exchange_end:reindex_end])
    mixed_action_end = central.index('// Direct recursive mixed displayed introduction', reindex_end)
    (package / 'central_mixed_action_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[reindex_end:mixed_action_end])
    mixed_source_end = central.index('// Direct mixed pointwise product distribution', mixed_action_end)
    (package / 'central_mixed_parameter_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[mixed_action_end:mixed_source_end])
    mixed_composition_end = central.index('// The following formation checks return to the general diagnostic inventory.', mixed_source_end)
    (package / 'central_mixed_composition_controls.lp').write_text(
        'require open emdash.central_displayed_products_controls;\n'
        + central[mixed_source_end:mixed_composition_end])
    mixed_formation_end = central.index('assert [Z : Cat] (x y : τ (Obj Z)) ⊢\n  Fibre_cat (@Rep_catd Z x) y', mixed_composition_end)
    (package / 'central_mixed_formation_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[mixed_composition_end:mixed_formation_end])
    (package / 'central_mixed_regression.lp').write_text(
        'require open emdash.central_mixed_action_controls;\n'
        'require open emdash.central_mixed_parameter_controls;\n'
        'require open emdash.central_mixed_composition_controls;\n'
        'require open emdash.central_mixed_formation_controls;\n')
    pathout_motives_end = central.index(
        '// The legacy edge/presheaf classifiers retain their corrected shifted bases.',
        mixed_formation_end)
    (package / 'central_pathout_motive_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[mixed_formation_end:pathout_motives_end])
    homd_classifiers_end = central.index('// Generic component evaluation owns', pathout_motives_end)
    (package / 'central_homd_classifier_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[pathout_motives_end:homd_classifiers_end])
    displayed_transport_end = central.index(
        '// Original public Homd ladder, at the selected Q/index types.', homd_classifiers_end)
    (package / 'central_displayed_transport_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + central[homd_classifiers_end:displayed_transport_end])
    public_homd_end = central.index('// catalog-area: Categorical-universe direct equality-valued', displayed_transport_end)
    public_homd = central[displayed_transport_end:public_homd_end]
    (package / 'central_public_homd_controls.lp').write_text(
        'require open emdash.emdash3_2;\n' + public_homd)
    public_homd_assertions = re.findall(r'(?m)^assert\b.*?;', public_homd, re.S)
    terminal_obligations = [block for block in public_homd_assertions if '≡ @Obj_func' in block]
    general_observations = [block for block in public_homd_assertions if '≡ @Obj_func' not in block]
    assert len(terminal_obligations) == 5 and len(general_observations) == 14
    (package / 'central_public_homd_general_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + '\n\n'.join(general_observations) + '\n')
    (package / 'central_public_homd_terminal_obligations.lp').write_text(
        '// Unqualified required normalization obligations; not a passing target.\n'
        'require open emdash.emdash3_2;\n'
        + '\n\n'.join(terminal_obligations) + '\n')
    (package / 'terminal_homd_comparison_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_terminal_homd_comparison_controls.lpfragment'))
    homcatd_action_start = central.index(
        '// Generic displayed Hom action: full/capped/point projection ladder.', public_homd_end)
    homcatd_action_end = central.index(
        '// General two-sided product maps used by profunctor reindexing.', homcatd_action_start)
    (package / 'central_homd_leaf_prof_controls.lp').write_text(
        'require open emdash.emdash3_2_eq1_evidence_property;\n'
        + central[public_homd_end:homcatd_action_start])
    (package / 'central_homcatd_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + central[homcatd_action_start:homcatd_action_end])
    product_prof_end = central.index(
        '// catalog-area: Internal Path action and explicit Core-inclusion kappa', homcatd_action_end)
    path_core_end = central.index(
        '// catalog-area: Opaque walking endomorphism HIT and contextual elimination', product_prof_end)
    (package / 'central_product_prof_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + central[homcatd_action_end:product_prof_end])
    (package / 'central_path_core_controls.lp').write_text(
        'require open emdash.emdash3_2_nat_arithmetic;\n'
        + central[product_prof_end:path_core_end])
    walking_end_end = central.index('// catalog-area: auto', path_core_end)
    (package / 'central_walking_end_controls.lp').write_text(
        'require open emdash.emdash3_2_walking_end_hit;\n'
        + central[path_core_end:walking_end_end])
    closed_sigma_end = central.index(
        '// catalog-area: Cat-valued presheaf facade and restriction', walking_end_end)
    (package / 'central_closed_sigma_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + central[walking_end_end:closed_sigma_end])
    presheaf_locality_end = central.index(
        '// catalog-area: Set-carrier commutative-ring objects', closed_sigma_end)
    (package / 'central_presheaf_locality_controls.lp').write_text(
        'require open emdash.emdash3_2_direct_cover_sheafification;\n'
        + central[closed_sigma_end:presheaf_locality_end])
    algebra_imports = list(dict.fromkeys(re.findall(
        r'emdash\.emdash3_2_commutative_algebra\w*',
        original_checks[:original_checks.index('// Elementary decoded')])))
    assert len(algebra_imports) == 22
    (package / 'central_algebra_controls.lp').write_text(
        'require open ' + ' '.join(algebra_imports) + ';\n'
        + central[central.index(algebra_marker):central.index(comma_marker)])
    (package / 'central_comma_action_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + central[central.index(comma_marker):central.index(profiles_marker)]
        + fragment('production_pre_laxity_projection_controls.lpfragment'))
    (package / 'central_profile_closure_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_interchanger;\n'
        'require open emdash.emdash3_2_walking_circle_restriction;\n'
        'require open emdash.emdash3_2_groupoidification_interval_recovery;\n'
        'require open emdash.emdash3_2_groupoidification_composition;\n'
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + central[central.index(profiles_marker):central.index(structural_tail_marker)])
    (package / 'central_structural_tail_controls.lp').write_text(
        'require open emdash.emdash3_2_cartesian_categories;\n'
        'require open emdash.emdash3_2_triangular_binary_products_finite_limits;\n'
        'require open emdash.emdash3_2_slice_dependent_products;\n'
        'require open emdash.emdash3_2_terminal_category_profile;\n'
        'require open emdash.emdash3_2_one_cat_adjunction_family_views;\n'
        + central[central.index(structural_tail_marker):])
    (package / 'central_curry_family_regression.lp').write_text(
        'require open emdash.central_curry_controls;\n'
        'require open emdash.central_family_controls;\n'
        'require open emdash.central_sections_controls;\n'
        'require open emdash.central_structural_controls;\n'
        'require open emdash.central_reindex_controls;\n')
    (package / 'central_projection_regression.lp').write_text(
        'require open emdash.central_intrinsic_projection_controls;\n'
        'require open emdash.central_pair_telescope_controls;\n'
        + fragment('production_cartesian_product_controls.lpfragment'))
    (package / 'central_migration_regression.lp').write_text(
        'require open emdash.central_owner_regression;\n'
        'require open emdash.central_displayed_regression;\n'
        'require open emdash.central_monads_controls;\n'
        'require open emdash.central_internal_action_controls;\n'
        'require open emdash.central_path_induction_controls;\n'
        'require open emdash.central_projection_regression;\n'
        'require open emdash.central_curry_family_regression;\n'
        'require open emdash.central_mixed_regression;\n'
        'require open emdash.central_pathout_motive_controls;\n'
        'require open emdash.central_homd_classifier_controls;\n'
        'require open emdash.central_displayed_transport_controls;\n'
        'require open emdash.central_public_homd_general_controls;\n'
        'require open emdash.terminal_homd_comparison_controls;\n'
        'require open emdash.central_homd_leaf_prof_controls;\n'
        'require open emdash.central_homcatd_controls;\n'
        'require open emdash.central_product_prof_controls;\n'
        'require open emdash.central_path_core_controls;\n'
        'require open emdash.central_walking_end_controls;\n'
        'require open emdash.central_closed_sigma_controls;\n'
        'require open emdash.central_presheaf_locality_controls;\n'
        'require open emdash.central_algebra_controls;\n'
        'require open emdash.central_comma_action_controls;\n'
        'require open emdash.central_profile_closure_controls;\n'
        'require open emdash.central_structural_tail_controls;\n')
    for folder, source in ((package, central), (baseline_package, original_checks)):
        assert source.count(hom_action_end) == 1
        header = source[:source.index('require open')] + 'require open emdash.emdash3_2_eq1_evidence_property;\n'
        (folder / 'central_early_controls.lp').write_text(
            header + source[source.index(early_start):source.index(early_end)])
        (folder / 'central_hom_action_controls.lp').write_text(
            header + source[source.index(early_end):source.index(hom_action_end)])
        (folder / 'central_owner_regression.lp').write_text(
            'require open emdash.central_early_controls;\n'
            'require open emdash.central_hom_action_controls;\n')
    (package / 'central_displayed_regression.lp').write_text(
        'require open emdash.central_displayed_products_controls;\n'
        'require open emdash.central_displayed_evaluation_controls;\n'
        'require open emdash.central_displayed_chain_controls;\n'
        'require open emdash.central_evaluation_adjunction_controls;\n')
    introduction_source = (package / 'emdash3_2_one_cat_adjunction_introduction.lp').read_text()
    prefix_end = 'protected symbol intro_unit_original_identity_path'
    assert introduction_source.count(prefix_end) == 1
    introduction_prefix = introduction_source[:introduction_source.index(prefix_end)]
    dependency = 'require open emdash.emdash3_2_one_cat_hom_comparison_data;'
    assert introduction_prefix.count(dependency) == 1
    (package / 'adjunction_introduction_views_prefix.lp').write_text(
        introduction_prefix.replace(dependency,
            'require open emdash.emdash3_2_prof_defiso_evaluation_paths;', 1))
    (package / 'hom_action_admission_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        + fragment('production_one_cat_hom_action_admission.lpfragment') + '\n'
        + fragment('production_one_cat_hom_action_controls.lpfragment'))
    (package / 'lax_curry_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + fragment('production_lax_curry_controls.lpfragment'))
    hom_comparison_source = (package / 'emdash3_2_one_cat_hom_comparison_data.lp').read_text()
    def source_slice(start, end):
        assert hom_comparison_source.count(start) == 1, start
        assert hom_comparison_source.count(end) == 1, end
        a = hom_comparison_source.index(start)
        return hom_comparison_source[a:hom_comparison_source.index(end, a)]
    (package / 'hom_comparison_curry_path_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + source_slice('protected symbol hom_comparison_pair_tele_func', 'protected symbol one_cat_hom_action_source')
        + source_slice('symbol profmap_internal_hom_action', '// η:id_A⇒GF')
        + source_slice('protected symbol hom_comparison_pair_tele_identity_path', 'protected symbol hom_comparison_admitted_hom_action_component_path'))
    (package / 'hom_comparison_admitted_path_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_transfor_profiles;\n'
        + fragment('production_one_cat_hom_action_admission.lpfragment') + '\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + source_slice('symbol profmap_internal_hom_action', '// η:id_A⇒GF')
        + source_slice('protected symbol hom_comparison_pair_tele_identity_path', 'symbol one_cat_hom_comparison_unit_component_path'))
    graph_source = (package / 'emdash3_2_represented_comma_families.lp').read_text()
    graph_boundary = '// Fibrewise Sigma of the existing whole internal action.'
    assert graph_source.count(graph_boundary) == 1
    (package / 'comma_graph_family_prefix.lp').write_text(graph_source[:graph_source.index(graph_boundary)])
    sigma_boundary = '// Pointwise opposite turns that whole transformation into the displayed map'
    assert graph_source.count(sigma_boundary) == 1
    (package / 'comma_graph_sigma_prefix.lp').write_text(graph_source[:graph_source.index(sigma_boundary)]
        + '\n' + fragment('production_comma_graph_sigma_control.lpfragment'))
    middle_boundary = '// The represented C-family at the varying source F[x].'
    assert graph_source.count(middle_boundary) == 1
    (package / 'comma_graph_middle_prefix.lp').write_text(graph_source[:graph_source.index(middle_boundary)]
        + '\n' + fragment('production_comma_graph_middle_controls.lpfragment'))
    basechange_boundary = 'protected symbol comma_graph_target_sec [B C : Cat]'
    assert graph_source.count(basechange_boundary) == 1
    (package / 'comma_graph_basechange_prefix.lp').write_text(graph_source[:graph_source.index(basechange_boundary)])
    total_boundary = '// The actual whole input classifier.'
    assert graph_source.count(total_boundary) == 1
    (package / 'comma_graph_total_prefix.lp').write_text(graph_source[:graph_source.index(total_boundary)]
        + '\n' + fragment('production_comma_graph_total_controls.lpfragment'))
    constructor_boundary = '// Whole source projection with its original inverse data.'
    assert graph_source.count(constructor_boundary) == 1
    (package / 'represented_comma_constructor_prefix.lp').write_text(graph_source[:graph_source.index(constructor_boundary)]
        + '\n' + fragment('production_represented_comma_constructor_controls.lpfragment'))
    source_boundary = '// Extract the actual target section before taking the outer opposite.'
    assert graph_source.count(source_boundary) == 1
    source_controls = (baseline_package / 'examples/represented_comma_families.lp').read_text()
    source_controls = source_controls.split('assert [A K : Cat]', 1)[0]
    source_controls = source_controls.replace('require open emdash.emdash3_2_represented_comma_families;', '')
    assert source_controls.count('Op_cat') == 11 and source_controls.count('Op_func') == 4
    # Only the original arbitrary-section negative has Op here: its total
    # projection is now O. All seven positive observations are unchanged.
    source_controls = source_controls.replace('Op_cat', 'TotalOp_cat').replace('Op_func', 'TotalOp_func')
    (package / 'represented_comma_source_prefix.lp').write_text(graph_source[:graph_source.index(source_boundary)]
        + '\n' + source_controls + '\n' + fragment('production_total_dual_projection_controls.lpfragment'))
    target_section_boundary = '// Link that section to the original total base change.'
    assert graph_source.count(target_section_boundary) == 1
    (package / 'represented_comma_target_section_prefix.lp').write_text(graph_source[:graph_source.index(target_section_boundary)])
    target_inverse_boundary = '// Group the original mapped graph section.'
    assert graph_source.count(target_inverse_boundary) == 1
    (package / 'represented_comma_target_inverse_prefix.lp').write_text(graph_source[:graph_source.index(target_inverse_boundary)])
    # These original assertions exercise the assembly owner itself. Keep the
    # full original downstream import closure staged as a separate obligation.
    assembly_controls = (package / 'examples/action_profile_inherited_assembly_controls.lp').read_text()
    imports = 'require open emdash.emdash3_2_direct_cover_completion_locality;\nrequire open emdash.emdash3_2_gray_profiles;'
    assert assembly_controls.count(imports) == 1
    (package / 'pointwise_assembly_controls.lp').write_text(assembly_controls.replace(
        imports, 'require open emdash.emdash3_2_strict_pointwise_equivalences;', 1)
        + '\n' + fragment('production_pointwise_coefficient_control.lpfragment'))
    (package / 'internal_x_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_internal_x_profile_controls.lpfragment'))
    (package / 'sigma_parameter_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_sigma_parameter_profile_controls.lpfragment'))
    (package / 'sigma_basechange_coefficient_controls.lp').write_text(
        'require open emdash.emdash3_2_gray_profiles;\n'
        + fragment('production_sigma_basechange_coefficient_controls.lpfragment'))
    (package / 'sigma_constant_projection_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        + fragment('production_sigma_constant_projection_controls.lpfragment'))
    (package / 'sigma_projection_regression_controls.lp').write_text(
        (package / 'inverse_core_controls.lp').read_text() + '\n'
        + fragment('production_sigma_constant_projection_controls.lpfragment'))
    (package / 'lax_curry_regression_controls.lp').write_text(
        (package / 'sigma_projection_regression_controls.lp').read_text() + '\n'
        + fragment('production_lax_curry_hom_views.lpfragment') + '\n'
        + fragment('production_lax_curry_controls.lpfragment'))
    (package / 'whole_reading_regression_controls.lp').write_text(
        (package / 'lax_curry_regression_controls.lp').read_text() + '\n'
        + fragment('production_whole_reading_controls.lpfragment'))
    (package / 'internal_composite_regression_controls.lp').write_text(
        (package / 'whole_reading_regression_controls.lp').read_text() + '\n'
        + fragment('production_internal_composite_action_controls.lpfragment'))
    (package / 'mapped_hom_regression_controls.lp').write_text(
        (package / 'internal_composite_regression_controls.lp').read_text() + '\n'
        + fragment('production_mapped_hom_square_controls.lpfragment'))
    (package / 'inverse_admission_regression_controls.lp').write_text(
        (package / 'mapped_hom_regression_controls.lp').read_text() + '\n'
        + fragment('production_core_path_image_controls.lpfragment'))
    (package / 'hygiene_full_controls.lp').write_text(
        (package / 'inverse_admission_regression_controls.lp').read_text() + '\n'
        + fragment('production_hygiene_controls.lpfragment'))
    (package / 'zero_family_core_controls.lp').write_text(
        (package / 'hygiene_full_controls.lp').read_text() + '\n'
        + fragment('production_precomposition_unit_controls.lpfragment'))
    (package / 'postcomposition_association_controls.lp').write_text(
        (package / 'zero_family_core_controls.lp').read_text() + '\n'
        + fragment('production_nested_postcomposition_controls.lpfragment'))
    (package / 'precomposition_association_controls.lp').write_text(
        (package / 'postcomposition_association_controls.lp').read_text() + '\n'
        + fragment('production_precomposition_association_controls.lpfragment'))
    (package / 'join_recursion_controls.lp').write_text(
        (package / 'precomposition_association_controls.lp').read_text() + '\n'
        + fragment('production_join_recursion_controls.lpfragment'))
    (package / 'ordinary_transposition_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_diagram_transpose;\n'
        'require emdash.examples.one_cat_diagram_transpose;\n'
        'require emdash.coefficient_inverse_view_controls;\n'
        + fragment('production_one_cat_arrow_point_controls.lpfragment'))
    native_transpose_controls = (baseline_package / 'examples/one_cat_diagram_transpose.lp').read_text()
    native_transpose_controls = native_transpose_controls.replace(
        'one_cat_diagram_transpose_', 'one_cat_oplax_diagram_transpose_')
    native_transpose_controls = native_transpose_controls.replace(
        'Functor_cat I C', 'Functor_oplax_cat I C').replace(
        'Functor_cat WalkingArrow_cat C', 'Functor_oplax_cat WalkingArrow_cat C')
    native_transpose_controls = native_transpose_controls.replace(
        '@diagram_family_at_func', '@diagram_oplax_family_at_func').replace(
        '@diagram_family_transf', '@diagram_oplax_family_transf')
    for variable in ('h', 'k'):
        before = f'@sym_transf_tapp0_transf B I C F G {variable} i'
        assert before in native_transpose_controls
        native_transpose_controls = native_transpose_controls.replace(before,
            f'@diagram_oplax_family_map_at B I C F G {variable} i')
    native_transpose_controls = native_transpose_controls.replace(
        '@tapp0_fapp0 WalkingArrow_cat C _ _',
        '@tapp0_fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) _ _')
    for variable in ('F', 'G'):
        before = f'@fapp1_fapp0 I C (@fapp0 B (Functor_oplax_cat I C) {variable} x) i j u'
        after = f'@fapp1_fapp0 (OddDual_cat I) (OddDual_cat C) (@fapp0 B (Functor_oplax_cat I C) {variable} x) j i u'
        assert native_transpose_controls.count(before) == 1
        native_transpose_controls = native_transpose_controls.replace(before, after)
    # Preserve the nontrivial observation of the actual whole I-functor.
    # The canonical column accessor must not make either comparison a test
    # of its own defining body; retain h versus k in the negative as well.
    point = '@one_cat_oplax_diagram_transpose_column_func B I C C1 F G h i'
    actual = ('@fapp0 I (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) '
              '(@one_cat_oplax_diagram_transpose_family_func B I C C1 F G h) i')
    split = '// The src of the whole column is the original evaluated diagram family.'
    first, rest = native_transpose_controls.split(split, 1)
    assert first.count(point) == 2
    first = first.replace(point, actual)
    split_last = '// The point comparison retains the chosen h, not an unrelated transformation.'
    middle, last = rest.split(split_last, 1)
    assert last.count(point) == 2
    last = last.replace(point, actual)
    native_transpose_controls = first + split + middle + split_last + last
    # The fixed-index column uses the existing covariant composition owner.
    # Observe that same whole value through its raw composition signature,
    # rather than the differently normalized varying-index accessor.
    for variable in ('F', 'G'):
        native_transpose_controls = native_transpose_controls.replace(
            f'@diagram_oplax_family_at_func B I C {variable} i',
            f'@comp_cat_fapp0 B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) {variable}')
    for variable in ('h', 'k'):
        native_transpose_controls = native_transpose_controls.replace(
            f'@diagram_oplax_family_map_at B I C F G {variable} i',
            f'@fapp0 _ _ (@comp_cat_cov_fapp1_func B (Functor_oplax_cat I C) C (@diagram_oplax_evaluation_at_func I C i) F G) {variable}')
    assert len(re.findall(r'^assert\b', native_transpose_controls, re.M)) == 8
    assert len(re.findall(r'^assertnot\b', native_transpose_controls, re.M)) == 1
    (package / 'one_cat_oplax_transpose_controls.lp').write_text(
        '// Native-profile adaptation of all original transposition observations.\n'
        + native_transpose_controls)
    (package / 'native_transpose_regression_controls.lp').write_text(
        'require emdash.one_cat_oplax_transpose_controls;\n'
        'require emdash.examples.one_cat_kernel_cokernel_transposes;\n'
        'require emdash.examples.one_cat_diagram_transpose;\n')
    (package / 'native_zero_column_regression_controls.lp').write_text(
        'require emdash.examples.one_cat_terminal_adjunction_families;\n'
        'require emdash.examples.one_cat_adjunction_zero_column_views;\n'
        'require emdash.native_transpose_regression_controls;\n'
        'require emdash.mapping_normalization_regression_controls;\n')
    (package / 'walking_end_migration_controls.lp').write_text(
        'require emdash.examples.walking_endomorphism_hit;\n'
        'require emdash.examples.action_profile_walking_named_rec_controls;\n'
        'require emdash.examples.action_profile_walking_named_overlap_controls;\n')
    (package / 'walking_circle_migration_controls.lp').write_text(
        'require emdash.examples.walking_circle_completion;\n'
        'require emdash.examples.walking_circle_groupoidification_restriction;\n')
    (package / 'profiled_interchange_migration_controls.lp').write_text(
        'require emdash.examples.action_profile_eckmann_hilton_one_hom;\n')
    (package / 'groupoidification_migration_controls.lp').write_text(
        'require emdash.examples.generic_groupoidification;\n'
        'require emdash.examples.generic_groupoidification_interval;\n'
        'require emdash.examples.walking_interval_groupoidification;\n')
    (package / 'monads_migration_controls.lp').write_text(
        'require emdash.examples.monads_comonads;\n')
    (package / 'product_pullback_migration_controls.lp').write_text(
        'require emdash.examples.triangular_binary_products;\n'
        'require emdash.examples.cartesian_categories;\n'
        'require emdash.examples.triangular_binary_products_finite_limits;\n'
        'require emdash.examples.pullbacks;\n'
        'require emdash.examples.slice_dependent_products;\n')
    foundation_reviewers = (
        'groupoidification_migration_controls.lp',
        'monads_migration_controls.lp',
        'product_pullback_migration_controls.lp',
        'walking_circle_migration_controls.lp',
        'profiled_interchange_migration_controls.lp',
    )
    for name in foundation_reviewers:
        (baseline_package / name).write_text((package / name).read_text())
    foundation_regression = ''.join(
        'require emdash.' + Path(name).stem + ';\n'
        for name in foundation_reviewers + ('direct_cover_sheafification_controls.lp',))
    foundation_regression += 'require emdash.examples.one_cat_arrow_diagrams;\n'
    for target_package in (package, baseline_package):
        (target_package / 'foundations_library_regression.lp').write_text(foundation_regression)
    (package / 'zero_column_dependency_controls.lp').write_text(
        'require emdash.walking_arrow_postcomposition_controls;\n'
        'require emdash.mapping_evaluation_controls;\n'
        'require emdash.ordinary_transposition_controls;\n'
        'require emdash.alternating_identity_controls;\n'
        'require emdash.examples.image_coimage_adjunction_families;\n')
    (package / 'coefficient_inverse_view_controls.lp').write_text(
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        'require open emdash.emdash3_2_defiso_evaluation_points;\n'
        'require emdash.examples.categorical_contractions;\n'
        + fragment('production_coefficient_inverse_view_controls.lpfragment'))
    (package / 'comma_target_guard_controls.lp').write_text(
        'require open emdash.emdash3_2_represented_comma_families;\n'
        'require emdash.examples.represented_comma_families;\n'
        + fragment('production_comma_target_guard_controls.lpfragment'))
    (package / 'prof_defiso_coefficient_controls.lp').write_text(
        'require open emdash.emdash3_2_prof_defiso_evaluation_paths;\n'
        'require emdash.examples.action_profile_prof_defiso_controls;\n'
        + fragment('production_cartesian_defiso_point_controls.lpfragment'))
    (package / 'path_cartesian_controls.lp').write_text(
        'require open emdash.emdash3_2_commutative_algebra_category;\n'
        + fragment('production_path_cartesian_controls.lpfragment'))
    (package / 'diagram_evaluation_profile_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        'require emdash.examples.diagram_evaluation;\n'
        + fragment('production_diagram_evaluation_controls.lpfragment'))
    (package / 'alternating_identity_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        'require emdash.diagram_evaluation_profile_controls;\n'
        + fragment('production_alternating_identity_controls.lpfragment'))
    (package / 'odd_cartesian_action_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        'require emdash.alternating_identity_controls;\n'
        + fragment('production_odd_cartesian_controls.lpfragment'))
    (package / 'one_cat_oplax_exchange_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_diagram_family_reflection;\n'
        + fragment('production_one_cat_oplax_exchange_controls.lpfragment'))
    (package / 'oplax_family_component_controls.lp').write_text(
        'require open emdash.emdash3_2_diagram_evaluation;\n'
        + fragment('production_oplax_family_component_controls.lpfragment'))
    (package / 'one_cat_oplax_roundtrip_controls.lp').write_text(
        'require open emdash.emdash3_2_one_cat_diagram_family_reflection;\n'
        + fragment('production_one_cat_oplax_roundtrip_controls.lpfragment'))
    (package / 'native_homology_comparison_reviewers.lp').write_text(
        'require emdash.native_exchange_regression_controls;\n'
        'require emdash.examples.one_cat_homology_family_comparison;\n'
        'require emdash.examples.one_cat_homology_family_comparison_points;\n')
    (package / 'mapping_normalization_regression_controls.lp').write_text(
        'require emdash.one_cat_arrow_profile_controls;\n'
        'require emdash.native_homology_comparison_reviewers;\n')
    (package / 'native_exchange_regression_controls.lp').write_text(
        'require emdash.odd_cartesian_action_controls;\n'
        'require emdash.oplax_family_component_controls;\n'
        'require emdash.one_cat_oplax_exchange_controls;\n'
        'require emdash.one_cat_oplax_roundtrip_controls;\n'
        'require emdash.one_cat_mapping_controls;\n'
        'require emdash.examples.one_cat_diagram_family_reconstruction;\n'
        'require emdash.examples.one_cat_arrow_family_isomorphisms;\n')
    (package / 'diagram_evaluation_naturality_controls.lp').write_text(
        (package / 'emdash3_2_diagram_evaluation.lp').read_text() + '\n'
        + fragment('production_diagram_evaluation_naturality_controls.lpfragment'))
    (package / 'arrow_diagram_migration_controls.lp').write_text(
        'require open emdash.emdash3_2_arrow_diagram_families;\n'
        + fragment('production_arrow_diagram_controls.lpfragment'))
    (package / 'zero_arrow_migration_controls.lp').write_text(
        'require open emdash.emdash3_2_zero_arrow_diagrams;\n'
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        + fragment('production_zero_arrow_controls.lpfragment'))
    (package / 'cubical_migration_controls.lp').write_text(''.join(
        'require open emdash.examples.' + name + ';\n' for name in (
            'cubical_dependent_hom', 'cubical_square_total',
            'cubical_internalization', 'cubical_internalization_composition')))
    (package / 'interchanger_controls.lp').write_text(
        'require open emdash.examples.gray_interchanger;\n'
        'require open emdash.examples.gray_interchanger_orientation;\n')
    # Use the actual byte-identical reviewer module. The former flattened
    # driver did not explain the runtime variability and is no longer needed.
    (package / 'weighted_migration_controls.lp').write_text(
        'require open emdash.emdash3_2;\n'
        'require open emdash.emdash3_2_strict_functor_actions;\n'
        'require emdash.examples.profunctor_weighted_limits;\n\n'
        + fragment('production_weighted_colimit_controls.lpfragment') + '\n'
        + fragment('production_default_inverse_legacy_controls.lpfragment') + '\n'
        + fragment('production_default_inverse_controls.lpfragment'))
    # Same original reviewer assertions, isolated at their actual profile
    # owner. The original broader import closure remains staged and required.
    profile_controls = (package / 'examples/gray_profiles.lp').read_text()
    assert profile_controls.count('require open emdash.emdash3_2_represented_comma_families;') == 1
    (package / 'profile_controls.lp').write_text(profile_controls.replace(
        'require open emdash.emdash3_2_represented_comma_families;',
        'require open emdash.emdash3_2_gray_profiles;', 1))
    delta = difflib.SequenceMatcher(None, original.splitlines(keepends=True),
                                   body.splitlines(keepends=True), autojunk=False).get_opcodes()
    original_lines_retained = all(kind in ('equal', 'insert') for kind, *_ in delta)
    declaration = r'(?m)^(?:(?:constant|injective|protected|private)\s+)?symbol\s+([A-Za-z0-9_]+)\b'
    original_names = re.findall(declaration, original)
    relocated_names = {'Catd_cat_func', 'Catd_catd_con', 'FibCov_target_catd',
                       'FibCov_source_catd', 'fib_cov_int', 'fib_cov_src_func',
                       'fib_cov_transf', 'homd_src_func', 'homd_src_sec', 'homd_tgt_func',
                       'homd_id_src_sec', 'homd_id_tgt_func', 'Const_func_func'}
    retired_names = {'Homd_target_section_catd': 'Homd_target_section_cat',
                     'functord_transport_lhs_tele_agrees': 'functord_transport_rhs_tele_agrees',
                     'functord_transport_lhs_agrees': 'functord_transport_rhs_agrees'}
    for name in relocated_names:
        assert re.findall(declaration, body).count(name) == 1, name
    for name, replacement in retired_names.items():
        assert not re.findall(r'(?m)^(?:injective |constant )?symbol ' + name + r'\b', body)
        assert re.findall(declaration, body).count(replacement) == 1
    original_names = [name for name in original_names if name not in relocated_names and name not in retired_names]
    candidate_names = iter(re.findall(declaration, body))
    assert all(any(candidate == name for candidate in candidate_names)
               for name in original_names), 'An original declaration was dropped or reordered'
    inputs[str(Path(__file__).resolve().relative_to(root))] = sha(Path(__file__).read_text())
    manifest = {
        'status': 'staged full-source migration; generation does not establish qualification',
        'sourcePin': PIN, 'originalCoreSha256': CORE_SHA,
        'originalCoreLines': len(original.splitlines()), 'candidateCoreLines': len(body.splitlines()),
        'originalDownstreamSectionsRetained': True,
        'originalCoreLineOrderVerified': original_lines_retained,
        'originalNamedDeclarationsRetained': not retired_names,
        'unretiredNamedDeclarationsRetained': True,
        'retiredNamesWithReplacements': retired_names,
        'originalNamedDeclarationSequenceVerified': not relocated_names,
        'unrelocatedNamedDeclarationSequenceVerified': True,
        'namedDeclarationSequenceExceptions': sorted(relocated_names),
        'originalDependencyInputs': dependencies,
        'changes': changes, 'relocatedDeclarations': relocated,
        'authoringInputs': inputs,
        'outputs': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [out / 'baseline.lp', package / 'emdash3_2.lp',
                              package / 'emdash3_2_gray_profiles.lp', package / 'owner_controls.lp',
                              package / 'foundations_prefix.lp',
                              package / 'sections_prefix.lp',
                              package / 'sigma_prefix.lp',
                              package / 'mixed_prefix.lp',
                              package / 'homd_prefix.lp',
                              package / 'index_profile.lp',
                              package / 'intrinsic_identity_prefix.lp',
                              package / 'section_action_prefix.lp',
                              package / 'evaluation_prefix.lp',
                              package / 'structural_prefix.lp',
                              package / 'ordinary_structural_prefix.lp',
                              package / 'pullback_structural_prefix.lp',
                              package / 'section_pullback_prefix.lp',
                              package / 'intrinsic_composite_prefix.lp',
                              package / 'intrinsic_unit_prefix.lp',
                              package / 'profunctor_prefix.lp',
                              package / 'comma_prefix.lp',
                              package / 'pathout_controls.lp',
                              package / 'rule_hygiene_full_controls.lp',
                              package / 'inverse_core_controls.lp',
                              package / 'profile_controls.lp',
                              package / 'cubical_migration_controls.lp',
                              package / 'interchanger_controls.lp',
                              package / 'weighted_migration_controls.lp',
                              package / 'path_cartesian_controls.lp',
                              package / 'diagram_evaluation_profile_controls.lp',
                              package / 'alternating_identity_controls.lp',
                              package / 'odd_cartesian_action_controls.lp',
                              package / 'diagram_evaluation_naturality_controls.lp',
                              package / 'arrow_diagram_migration_controls.lp',
                              package / 'zero_arrow_migration_controls.lp',
                              package / 'pointwise_assembly_controls.lp',
                              package / 'comma_graph_family_prefix.lp',
                              package / 'comma_graph_sigma_prefix.lp',
                              package / 'internal_x_profile_controls.lp',
                              package / 'sigma_parameter_profile_controls.lp',
                              package / 'comma_graph_middle_prefix.lp',
                              package / 'sigma_basechange_coefficient_controls.lp',
                              package / 'comma_graph_basechange_prefix.lp',
                              package / 'comma_graph_total_prefix.lp',
                              package / 'represented_comma_constructor_prefix.lp',
                              package / 'represented_comma_source_prefix.lp',
                              package / 'represented_comma_target_section_prefix.lp',
                              package / 'represented_comma_target_inverse_prefix.lp',
                              package / 'sigma_constant_projection_controls.lp',
                              package / 'sigma_projection_regression_controls.lp',
                              package / 'hom_action_admission_controls.lp',
                              package / 'lax_curry_controls.lp',
                              package / 'hom_comparison_curry_path_controls.lp',
                              package / 'hom_comparison_admitted_path_controls.lp',
                              package / 'lax_curry_regression_controls.lp',
                              package / 'adjunction_introduction_views_prefix.lp',
                              package / 'presheaf_profile_controls.lp',
                              package / 'sieve_profile_controls.lp',
                              package / 'direct_cover_question_regression.lp',
                              package / 'locality_profile_controls.lp',
                              package / 'locality_fibre_prefix.lp',
                              package / 'inverse_endpoint_paths.lp',
                              package / 'inverse_post_endpoint_paths.lp',
                              package / 'inverse_post_admission_boundary.lp',
                              package / 'inverse_unit_profiles.lp',
                              package / 'inverse_cell_reflection.lp',
                              package / 'internal_composite_action_controls.lp',
                              package / 'inverse_represented_unit.lp',
                              package / 'represented_laxity_boundary.lp',
                              package / 'represented_laxity_controls.lp',
                              package / 'whiskering_equivalences.lp',
                              package / 'inverse_admission.lp',
                              package / 'cartesian_inverse_laws.lp',
                              package / 'cartesian_inverse_controls.lp',
                              package / 'inverse_locality_regression.lp',
                              package / 'diagram_with_adjunction_views.lp',
                              package / 'one_cat_evaluation_controls.lp',
                              package / 'one_cat_mapping_controls.lp',
                              package / 'mapping_evaluation_controls.lp',
                              package / 'mapping_normalization_regression_controls.lp',
                              package / 'walking_arrow_postcomposition_controls.lp',
                              package / 'one_cat_family_exchange.lp',
                              package / 'one_cat_family_exchange_controls.lp',
                              package / 'one_cat_oplax_exchange_controls.lp',
                              package / 'one_cat_oplax_roundtrip_controls.lp',
                              package / 'native_exchange_regression_controls.lp',
                              package / 'native_homology_comparison_reviewers.lp',
                              package / 'oplax_family_component_controls.lp',
                              package / 'one_cat_double_exchange_controls.lp',
                              package / 'one_cat_arrow_family_integration.lp',
                              package / 'one_cat_evaluation_integration.lp',
                              package / 'whole_reading_regression_controls.lp',
                              package / 'internal_composite_regression_controls.lp',
                              package / 'mapped_hom_regression_controls.lp',
                              package / 'inverse_admission_regression_controls.lp',
                              package / 'hygiene_full_controls.lp',
                              package / 'zero_family_core_controls.lp',
                              package / 'postcomposition_association_controls.lp',
                              package / 'precomposition_association_controls.lp',
                              package / 'join_recursion_controls.lp',
                              package / 'coefficient_inverse_view_controls.lp',
                              package / 'ordinary_transposition_controls.lp',
                              package / 'one_cat_oplax_transpose_controls.lp',
                              package / 'native_transpose_regression_controls.lp',
                              package / 'native_zero_column_regression_controls.lp',
                              package / 'walking_end_migration_controls.lp',
                              package / 'walking_circle_migration_controls.lp',
                              package / 'profiled_interchange_migration_controls.lp',
                              package / 'direct_cover_sheafification_controls.lp',
                              package / 'groupoidification_migration_controls.lp',
                              package / 'monads_migration_controls.lp',
                              package / 'product_pullback_migration_controls.lp',
                              package / 'foundations_library_regression.lp',
                              baseline_package / 'foundations_library_regression.lp',
                              package / 'central_groupoidality_controls.lp',
                              package / 'central_early_controls.lp',
                              package / 'central_action_controls.lp',
                              package / 'central_displayed_products_controls.lp',
                              package / 'central_displayed_evaluation_controls.lp',
                              package / 'central_displayed_chain_controls.lp',
                              package / 'central_evaluation_adjunction_controls.lp',
                              package / 'central_monads_controls.lp',
                              package / 'central_internal_action_controls.lp',
                              package / 'central_path_induction_controls.lp',
                              package / 'central_intrinsic_projection_controls.lp',
                              package / 'central_pair_telescope_controls.lp',
                              package / 'central_curry_controls.lp',
                              package / 'central_family_controls.lp',
                              package / 'central_sections_controls.lp',
                              package / 'central_structural_controls.lp',
                              package / 'central_reindex_controls.lp',
                              package / 'central_mixed_action_controls.lp',
                              package / 'central_mixed_parameter_controls.lp',
                              package / 'central_mixed_composition_controls.lp',
                              package / 'central_mixed_formation_controls.lp',
                              package / 'central_mixed_regression.lp',
                              package / 'central_pathout_motive_controls.lp',
                              package / 'central_homd_classifier_controls.lp',
                              package / 'central_displayed_transport_controls.lp',
                              package / 'central_public_homd_controls.lp',
                              package / 'central_public_homd_general_controls.lp',
                              package / 'central_public_homd_terminal_obligations.lp',
                              package / 'terminal_homd_comparison_controls.lp',
                              package / 'central_homd_leaf_prof_controls.lp',
                              package / 'central_homcatd_controls.lp',
                              package / 'central_product_prof_controls.lp',
                              package / 'central_path_core_controls.lp',
                              package / 'central_walking_end_controls.lp',
                              package / 'central_closed_sigma_controls.lp',
                              package / 'central_presheaf_locality_controls.lp',
                              package / 'central_algebra_controls.lp',
                              package / 'central_comma_action_controls.lp',
                              package / 'central_profile_closure_controls.lp',
                              package / 'central_structural_tail_controls.lp',
                              package / 'central_curry_family_regression.lp',
                              package / 'central_projection_regression.lp',
                              package / 'central_migration_regression.lp',
                              package / 'central_displayed_regression.lp',
                              package / 'central_hom_action_controls.lp',
                              package / 'central_owner_regression.lp',
                              baseline_package / 'central_early_controls.lp',
                              baseline_package / 'central_hom_action_controls.lp',
                              baseline_package / 'central_owner_regression.lp',
                              package / 'zero_column_dependency_controls.lp',
                              package / 'comma_target_guard_controls.lp',
                              package / 'prof_defiso_coefficient_controls.lp',
                              baseline_package / 'emdash3_2.lp', baseline_package / 'emdash3_2_gray_profiles.lp']
                    + [package / path for path in dependencies]},
        'stillRequired': ['Coefficient/mixed-parameter compatibility at installed-rule overlaps and actual consumers, without requiring a general Q model',
                          'Five original whole terminal-source Homd reductions, preserving Q units and the actual relative maps',
                          'Profile-extension and original diagnostic/import-closure migration',
                          'Whole duality/adjunction and closure-consumer qualification',
                          'Full downstream qualification of default-functor interfaces and retained transformation profiles',
                          'Public promotion with catalog, health, CI and source-pin review'],
        'excluded': ['Auxiliary Sigma fibre-composition audit owner',
                     'Unrestricted Cartesian evaluation on lax transformations',
                     'Optional normalization redesign'],
    }
    # R11: retire the second functor object grammar after the original owner
    # migration. Keep transformation/displayed-map profiles separate.
    def wrapper_output(path, text, reason):
        target = package / path
        previous = target.read_text()
        if previous == text:
            return
        target.write_text(text)
        changes.append({'source': path, 'owner': 'strict-functor wrapper retirement',
                        'reason': reason, 'oldBodySha256': sha(previous),
                        'newBodySha256': sha(text)})
        manifest['outputs'][str(target.relative_to(root))] = sha(text)

    gray = (package / 'emdash3_2_gray_profiles.lp').read_text()
    first = gray.index('// Opaque full-image classifier of ambient carriers admitting strictness.')
    last = gray.index('// -----------------------------------------------------------------------------------------------\n// Whole strict-transfor property and stable ambient view', first)
    retired_functor_rules = re.findall(r'(?m)^(?:rule|unif_rule)\b[\s\S]*?;', gray[first:last])
    assert len(retired_functor_rules) == 22
    gray = gray[:first] + fragment('production_strict_functor_aliases.lpfragment') + '\n' + gray[last:]
    first = gray.index('/*')
    last = gray.index('*/', first) + 2
    gray = gray[:first] + '''/*
  Emdash v3.2: strict default functors and explicit transformation profiles.

  The former StrictFunctor object/view operations are transparent compatibility
  aliases of the public default. Their redundant guarded rules are retired.
  IsStrictFunctor still describes the existing extracted compositor, and the
  canonical proof is derived for default maps. Consumers will migrate off the
  legacy spellings before final retirement.

  StrictFunctor_cat has the same full Hom profile as Functor_cat. GrayHom_lax
  remains distinct: its Homs retain the existing LaxTransfor packages and their
  ambient higher cells. StrictTransfor and StrictFunctord remain meaningful
  refinements of the default conventional-lax transformations/displayed maps.
*/''' + gray[last:]
    wrapper_output('emdash3_2_gray_profiles.lp', gray,
                   'Use transparent ordinary functor/category/view aliases, derive identity strictness, and remove 22 obsolete object-profile rules; preserve actual transfor profiles')
    actions = (package / 'emdash3_2_strict_functor_actions.lp').read_text()
    retired_constructor_views = []
    def retire_constructor_view(match):
        if re.match(r'^rule @strict_functor\b', match[0]):
            retired_constructor_views.append(match[0])
            return '// The public-default alias computes through the constructor definition.'
        return match[0]
    actions = re.sub(r'(?m)^(?:rule|unif_rule)\b[\s\S]*?;', retire_constructor_view, actions)
    assert len(retired_constructor_views) == 2
    actions = actions.replace('''  A classified strict functor maps equality-valued equivalences without a
  detached composition-law record. The component comparison below is a
  theorem of the stable `strict_functor` head. Both cancellation proofs and
  selected inverses remain computational. This legacy classified API now
  coexists with strict default functors; its wrappers await consumer migration
  and retirement. No strictness of arbitrary transformations is added.''', '''  Default strict functors map equality-valued equivalences without a
  detached composition-law record. The legacy strict_* operation names now
  use transparent aliases of ordinary functor carriers. Both cancellation
  proofs and selected inverses remain computational. Remaining compatibility
  spellings await consumer cleanup; transformation profiles remain separate.''')
    assert actions.count('Default strict functors map equality-valued equivalences without a') == 1
    wrapper_output('emdash3_2_strict_functor_actions.lp', actions,
                   'Retire the constant/Path decoder rules on the newly transparent strict_functor alias; their constructor definitions compute directly')

    for path, type_count, view_count in (
        ('emdash3_2_eq1_hom_action.lp', 1, 3),
        ('examples/groupoidal_structured_j_eq1.lp', 2, 7),
    ):
        text = (package / path).read_text()
        old = '(D : τ (@StrictFunctor C Cat_cat))'
        view = '(@strict_functor C Cat_cat D)'
        assert text.count(old) == type_count
        assert text.count(view) == view_count
        text = text.replace(old, '(D : τ (Functor C Cat_cat))').replace(view, 'D')
        text = text.replace('The ordinary Cat-valued diagram retains its legacy `StrictFunctor` input.',
                            'The ordinary Cat-valued diagram uses the default strict Functor input.')
        wrapper_output(path, text,
                       'Accept the public ordinary Cat-valued diagram directly and preserve its chosen mapped inverse data; do not impose Cat_cart-family admission')
    text = (package / 'emdash3_2_commutative_algebra_presheaves.lp').read_text()
    for old, new in (
        ('≔ @StrictFunctor_cat (Op_cat K) CommRing_cat;', '≔ @CommRingPsh_cat K;'),
        ('≔ @StrictFunctor (Op_cat K) CommRing_cat;', '≔ @CommRingPsh K;'),
        ('≔ @strict_functor (Op_cat K) CommRing_cat O;', '≔ O;'),
    ):
        assert text.count(old) == 1, old
        text = text.replace(old, new)
    text = text.replace('// Classified conventional presheaves. The carrier remains an ordinary\n// CommRing-valued presheaf; strictness is internal package data.',
        '// Compatibility spellings: ordinary CommRing-valued presheaves already\n// use strict default functors, so no additional object package is needed.')
    wrapper_output('emdash3_2_commutative_algebra_presheaves.lp', text,
                   'Make the strict-ring-presheaf facade an identity compatibility view of the existing ordinary presheaf carrier/category')
    text = (package / 'emdash3_2_one_cat_functor_profiles.lp').read_text()
    old = '''  : τ (@StrictFunctor A B)
≔ @make_strict_functor A B F (@functor_into_one_cat_is_strict A B B1 F);'''
    assert text.count(old) == 1
    text = text.replace(old, '  : τ (Functor A B)\n≔ F;')
    text = text.replace('  @strict_functor_underlying A B (@one_cat_strict_admission A B B1 F)',
                        '  @one_cat_strict_admission A B B1 F')
    text = text.replace('(@strict_functor A B (@one_cat_strict_admission A B B1 F))',
                        '(@one_cat_strict_admission A B B1 F)')
    text = text.replace('symbol one_cat_strict_admission [A B : Cat]',
                        '// Compatibility adapter: the default functor is already strict.\nsymbol one_cat_strict_admission [A B : Cat]')
    wrapper_output('emdash3_2_one_cat_functor_profiles.lp', text,
                   'Keep the existing one-category adapter signature and observations while returning the already-strict public map directly')
    text = (package / 'examples/action_profile_walking_named_overlap_controls.lp').read_text()
    assert text.count('StrictFunctor_cat') == 21
    wrapper_output('examples/action_profile_walking_named_overlap_controls.lp',
                   text.replace('StrictFunctor_cat', 'Functor_cat'),
                   'Observe the same whole named walking action at the public mapping category with its unchanged higher-transformation profile')

    # Update only the emitted diagnostics in this manifest, never old probes.
    wrapper_diagnostic_paths = [root / name for name in list(manifest['outputs'])
        if (root / name).is_relative_to(package) and name.endswith('.lp')
        and ((root / name).name.startswith('central_')
             or (root / name).name == 'emdash3_2_checks.lp'
             or name.endswith('/examples/gray_profiles.lp'))]
    for target in wrapper_diagnostic_paths:
        text = target.read_text()
        text = text.replace('(D : τ (@StrictFunctor C Cat_cat))', '(D : τ (Functor C Cat_cat))')
        text = text.replace('(@strict_functor C Cat_cat D)', 'D')
        def wrapper_polarity(match):
            block = match[0]
            if ('@strict_functor A B (@make_strict_functor A B F p)' in block
                    or 'F : τ (Obj (@GrayHom_lax A B))' in block):
                return block.replace('assertnot', 'assert', 1)
            accumulation_heads = (
                '@hom_postcomp_func A B F W X Z (@comp_fapp0',
                '@hom_postcomp_fapp0 A B F W X Z (@comp_fapp0',
                '@hom_precomp_along_func A B F z w y (@comp_fapp0',
                '@hom_precomp_along_fapp0 A B F z w y (@comp_fapp0',
            )
            if any(head in block for head in accumulation_heads):
                return block.replace('assertnot', 'assert', 1)
            mapped_accumulation = (
                ('(@hom_postcomp_fapp0 A B F W X Y p g)',
                 '(@fapp1_fapp0 B A F Y Z q)'),
                ('(@hom_precomp_along_fapp0 A B F Z W X p g)',
                 '(@fapp1_fapp0 A B F V W q)'),
            )
            if any(left in block and right in block for left, right in mapped_accumulation):
                return block.replace('assertnot', 'assert', 1)
            return block
        text = re.sub(r'(?m)^assertnot\b[\s\S]*?;', wrapper_polarity, text)
        text = text.replace('// Until wrapper retirement, the legacy admitted object sort is still distinct\n// syntactically from the now-strict public Functor carrier.',
            '// The transparent object alias now admits every public default functor;\n// GrayHom_lax still has its distinct transformation profile.')
        text = text.replace('// Generic accumulation stays distinct; the explicit strict view computes.',
            '// Strict-default accumulation computes for both ordinary maps and compatibility views.')
        text = text.replace('// Generic accumulation stays distinct; the actual strict view computes.',
            '// Strict-default accumulation computes for both ordinary maps and compatibility views.')
        text = text.replace('// Adjacent hom-action accumulation is selected by an explicit profile.\n// Preserve both the raw noncollapse and the classified computation checks.',
            '// Adjacent hom-action accumulation belongs to the strict default.\n// Preserve both ordinary and compatibility-view observations.')
        text = text.replace('// The legacy stable-cut normalization boundary remains pending wrapper retirement;\n// these runtime observations do not assert mathematical non-functoriality.',
            '// The ordinary and compatibility-view computations now use the same native owner.')
        wrapper_output(str(target.relative_to(package)), text,
                       'Use public diagram carriers and the now-transparent strict object/view computation; retain distinct carriers and lax/strict-transfor noncollapse controls')
    wrapper_controls = package / 'strict_wrapper_consumers_controls.lp'
    wrapper_controls.write_text('''require open emdash.examples.gray_profiles;
require open emdash.examples.groupoidal_structured_j_eq1;
require open emdash.examples.action_profile_walking_named_overlap_controls;
require open emdash.emdash3_2_commutative_algebra_presheaves;

// Ordinary ring presheaves pass directly through the compatibility view.
assert [K : Cat] (O : τ (@CommRingPsh K)) ⊢
  @strict_comm_ring_psh K O ≡ O;
assert [K : Cat] ⊢ @StrictCommRingPsh_cat K ≡ @CommRingPsh_cat K;
''')
    accumulation_controls = package / 'default_hom_accumulation_controls.lp'
    accumulation_controls.write_text('require open emdash.emdash3_2;\n'
        + fragment('production_default_hom_accumulation_controls.lpfragment'))
    manifest['outputs'][str(accumulation_controls.relative_to(root))] = sha(accumulation_controls.read_text())
    manifest['outputs'][str(wrapper_controls.relative_to(root))] = sha(wrapper_controls.read_text())
    manifest['strictWrapperRetirement'] = {
        'status': 'transparent compatibility phase; consumer spelling/helper retirement still open',
        'retiredRuleCommands': 24,
        'defaultHomOwnerChanges': 'Five identity-only composition/reassociation clauses generalized and two mapped-arrow clauses restored; nested postcomposition cuts preserve actual inverse cancellation.',
        'preservedProfiles': ['StrictTransfor', 'StrictFunctord', 'GrayHom_lax higher Homs'],
    }
    # Complete the compatibility phase only after its original consumers have
    # been migrated. Keep the transformation profiles and native property API.
    from production_strict_wrapper_finish import finish_strict_wrapper_retirement
    finish_source = audit / 'production_strict_wrapper_finish.py'
    inputs[str(finish_source.relative_to(root))] = sha(finish_source.read_text())
    finished_wrappers = finish_strict_wrapper_retirement(root, package, manifest['outputs'])
    for change in finished_wrappers['changes']:
        target = package / change['file']
        manifest['outputs'][str(target.relative_to(root))] = sha(target.read_text())
        changes.append({'source': change['file'], 'owner': 'final strict-functor wrapper retirement',
                        'reason': 'Use public Functor and existing ordinary action owners; remove unused admission wrappers and migrate actual consumers while retaining transformation profiles and native compositor evidence',
                        'oldBodySha256': change['beforeSha256'], 'newBodySha256': change['afterSha256']})
    manifest['strictWrapperRetirement']['status'] = 'legacy wrappers removed from final emitted LP; descriptive compositor property and genuine transformation profiles retained'
    manifest['strictWrapperRetirement']['finalDisposition'] = finished_wrappers
    vertical_target = package / 'emdash3_2.lp'
    before_vertical = vertical_target.read_text()
    after_vertical = add_default_vertical_comparison(before_vertical)
    vertical_target.write_text(after_vertical)
    manifest['outputs'][str(vertical_target.relative_to(root))] = sha(after_vertical)
    changes.append({'source': 'emdash3_2.lp', 'owner': 'default conventional pre-leg vertical composition',
                    'reason': 'Compare the conventional pre-leg vertical action while preserving literal displayed composites for intrinsic Homd; all raw vertical folds remain disabled',
                    'oldBodySha256': sha(before_vertical), 'newBodySha256': sha(after_vertical)})
    before_telescope = vertical_target.read_text()
    after_telescope = add_ordinary_telescope_identities(before_telescope)
    vertical_target.write_text(after_telescope)
    manifest['outputs'][str(vertical_target.relative_to(root))] = sha(after_telescope)
    changes.append({'source': 'emdash3_2.lp', 'owner': 'ordinary telescope identity projections',
                    'reason': 'Join native-identity-first and ordinary-inclusion-first observations without collapsing nonidentity higher cells',
                    'oldBodySha256': sha(before_telescope), 'newBodySha256': sha(after_telescope)})
    # Apply this slice after the exactly pinned earlier owner replays, without
    # changing their historical input hashes or qualifying an untested prefix.
    before_simplex = vertical_target.read_text()
    after_simplex = before_simplex
    marker = '// The public whole laxity candidate is now an object projection, not an\n'
    assert after_simplex.count(marker) == 1
    after_simplex = after_simplex.replace(marker,
        fragment('production_covariant_compositor_cell.lpfragment') + '\n' + marker, 1)
    start = after_simplex.index('// The already-normalized identity-family presentation needs its own direct')
    end = after_simplex.index('// Fold-direction codomain accumulation for precomposition.', start)
    after_simplex = (after_simplex[:start]
        + fragment('production_represented_point_comparison.lpfragment') + '\n'
        + after_simplex[end:])
    vertical_target.write_text(after_simplex)
    manifest['outputs'][str(vertical_target.relative_to(root))] = sha(after_simplex)
    changes.append({'source': 'emdash3_2.lp', 'owner': 'covariant compositor projection and represented point comparison',
                    'reason': 'Join the capped default-strict compositor with its whole extracted identity; retain the original two-arrow pre/post comparison and add its three-arrow nested instance with all operands constrained, preserving runtime owners and arbitrary lax displayed action',
                    'oldBodySha256': sha(before_simplex), 'newBodySha256': sha(after_simplex)})
    # The selected-presentation owner changes follow earlier exact-pin replays.
    for name, finish in (('emdash3_2.lp', finish_selected_core),
                         ('emdash3_2_diagram_evaluation.lp', finish_selected_diagram),
                         ('emdash3_2_arrow_diagram_families.lp', finish_selected_arrow_diagram),
                         ('examples/one_cat_adjunction_families.lp', finish_selected_adjunction_reviewer),
                         ('emdash3_2_one_cat_adjunction_family_views.lp', finish_selected_family_views),
                         ('emdash3_2_one_cat_homology_family_comparison.lp', finish_selected_homology_comparison)):
        target = package / name
        before = target.read_text()
        after = finish(before)
        target.write_text(after)
        manifest['outputs'][str(target.relative_to(root))] = sha(after)
        changes.append({'source': name, 'owner': 'selected presentation action normalization',
                        'reason': 'Preserve canonical capped action endpoints, generic same-arrow metadata, actual dual triangles and stable Cat prewhiskering projections',
                        'oldBodySha256': sha(before), 'newBodySha256': sha(after)})
    for name, source in (
        ('selected_presentation_controls.lp', 'production_selected_presentation_controls.lpfragment'),
        ('selected_identity_controls.lp', 'production_selected_identity_controls.lpfragment'),
        ('selected_presentation_complete_regression.lp', 'production_selected_presentation_complete_regression.lpfragment'),
        ('selected_presentation_reviewer_suffix.lp', 'production_selected_presentation_reviewer_suffix.lpfragment'),
        ('selected_record_views_review.lp', 'production_selected_record_views_review.lpfragment'),
        ('kernel_boundary_wave1.lp', 'production_kernel_boundary_prerequisites_review.lpfragment'),
        ('kernel_boundary_wave2.lp', 'production_kernel_additive_prerequisites_review.lpfragment'),
        ('kernel_boundary_wave3.lp', 'production_connecting_kernel_chain_review.lpfragment'),
        ('kernel_boundary_wave4.lp', 'production_native_connecting_consumers_review.lpfragment'),
        ('selected_presentation_regression.lp', 'production_selected_presentation_regression.lpfragment'),
        ('selected_presentation_core_regression.lp', 'production_selected_presentation_core_regression.lpfragment'),
        ('selected_presentation_library_regression.lp', 'production_selected_presentation_library_regression.lpfragment'),
        ('selected_presentation_residual_regression.lp', 'production_selected_presentation_residual_regression.lpfragment'),
        ('action_remaining_core_regression.lp', 'production_action_remaining_core_regression.lpfragment'),
        ('action_remaining_library_regression.lp', 'production_action_remaining_library_regression.lpfragment'),
        ('simplex_dependency_residual_regression.lp', 'production_simplex_dependency_residual_regression.lpfragment'),
    ):
        target = package / name
        target.write_text(fragment(source))
        manifest['outputs'][str(target.relative_to(root))] = sha(target.read_text())
    # Update the full original diagnostic and its actual selected projections.
    # The five unrelated terminal runtime obligations retain their old status.
    for name in ('emdash3_2_checks.lp', 'central_full_context_except_terminal.lp',
                 'central_hom_action_controls.lp', 'central_action_controls.lp'):
        target = package / name
        before = target.read_text()
        after = finish_selected_prewhisker_check(before)
        target.write_text(after)
        manifest['outputs'][str(target.relative_to(root))] = sha(after)
        changes.append({'source': name, 'owner': 'stable whole prewhiskering diagnostic',
                        'reason': 'Preserve the original whole comparison at proof time and add the runtime noncollapse boundary after retiring the eager fold that broke strict identity computation',
                        'oldBodySha256': sha(before), 'newBodySha256': sha(after)})
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted full pre-goal baseline and upstream owner migration; no original tail omitted.')


if __name__ == '__main__':
    main()
