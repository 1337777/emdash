"""Adapt the original terminal-family consumers to their oplax coefficient.

The emitted LP retains the old whole maps, inverse data and assertions.
This source adapter adds no formal rules; qualification belongs to the LP.
"""
from pathlib import Path
import re

from production_diagram_observation_migration import B, _atom, _point_readings

AUDIT = Path(__file__).resolve().parent


def _replace(text, replacements, counts):
    for (pattern, replacement), expected in zip(replacements, counts, strict=True):
        text, count = re.subn(pattern, replacement, text)
        assert count == expected, (pattern, count, expected)
    return text


def _declared_terminal_composite(text, expected):
    # Keep the exact source functor already declared for h:J∘A⇒D.
    # The old postcomposition presentation hides J's endpoint computation.
    marker = '(@fapp0 (Functor_cat B C)'
    assert text.count(marker) == expected
    while marker in text:
        start = text.rfind(marker)
        cursor = start + len('(@fapp0')
        args = []
        for _ in range(4):
            value, cursor = _atom(text, cursor)
            args.append(value)
        assert text[cursor] == ')'
        assert args[0] == '(Functor_cat B C)' and args[3] == 'A'
        assert re.sub(r'\s+', ' ', args[2]) == (
            f'(@comp_cat_cov_func B C {B} (@terminal_arrow_diagram_func C t T))')
        replacement = f'(@comp_cat_fapp0 B C {B} (@terminal_arrow_diagram_func C t T) A)'
        text = text[:start] + replacement + text[cursor + 1:]
    return text


def _incoming_reviewer(text):
    text = _replace(text, (
        (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
        (r'@diagram_family_at_func', '@diagram_oplax_family_at_func'),
        (r'@diagram_family_transf', '@diagram_oplax_family_transf'),
    ), (27, 5, 2))
    text = _point_readings(text, (0, 4))
    # Decode the same strict diagram object before observing its generator.
    # Arrows between diagrams above use whole fixed evaluation instead.
    matches = list(re.finditer(r'@fapp1_fapp0\s+WalkingArrow_cat\s+C\b', text))
    assert len(matches) == 1
    match = matches[0]
    cursor = match.end()
    args = []
    for _ in range(4):
        value, cursor = _atom(text, cursor)
        args.append(value)
    diagram, i, j, generator = args
    assert (i, j, generator) == ('walking_arrow_src', 'walking_arrow_tgt', 'walking_arrow_generator')
    replacement = ('@fapp1_fapp0 WalkingArrow_cat C '
                   f'(@OddDual_func (OddDual_cat WalkingArrow_cat) (OddDual_cat C) {diagram}) '
                   f'{i} {j} {generator}')
    text = text[:match.start()] + replacement + text[cursor:]
    return _declared_terminal_composite(text, 2)


def finish_terminal_family(path, text):
    if path == 'emdash3_2_one_cat_diagram_family_reflection.lp':
        # The existing exchange proof already imports this owner before the
        # appended family reflection. Preserve the entire prior module prefix.
        assert text.count('require open emdash.emdash3_2_one_cat_modifications;') == 1
        assert 'symbol one_cat_oplax_diagram_family_map_path' not in text
        return text + '\n' + (AUDIT / 'production_oplax_family_reflection.lpfragment').read_text()
    terminal_counts = {
        'emdash3_2_one_cat_terminal_family_universality.lp': (12, 8, 5, 0, 10),
        'examples/one_cat_terminal_family_universality.lp': (116, 16, 11, 0, 0),
        'emdash3_2_one_cat_terminal_family_paths.lp': (4, 0, 1, 4, 0),
    }
    if path in terminal_counts:
        return _replace(text, (
            (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
            (r'@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at'),
            (r'\(Op_cat C\)', '(TotalOp_cat C)'),
            (r'@diagram_family_transf', '@diagram_oplax_family_transf'),
            (r'@one_cat_(terminal|initial)_adjunction_family_presentation_',
             r'@one_cat_oplax_\1_adjunction_family_presentation_'),
        ), terminal_counts[path])
    family_counts = {
        'emdash3_2_zero_arrow_family_observations.lp': (9, 0, 1, 2, 0, 0),
        'emdash3_2_one_cat_diagram_family_paths.lp': (30, 14, 14, 0, 4, 2),
    }
    if path in family_counts:
        text = _replace(text, (
            (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
            (r'@sym_fapp0_func', '@diagram_oplax_family_at_func'),
            (r'@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at'),
            (r'@diagram_family_at_func', '@diagram_oplax_family_at_func'),
            (r'@diagram_family_transf', '@diagram_oplax_family_transf'),
            (r'\(Op_cat C\)', '(TotalOp_cat C)'),
        ), family_counts[path])
        if path == 'emdash3_2_one_cat_diagram_family_paths.lp':
            assert text.count('@one_cat_diagram_family_map_path') == 2
            text = text.replace('@one_cat_diagram_family_map_path', '@one_cat_oplax_diagram_family_map_path')
        if path == 'emdash3_2_zero_arrow_family_observations.lp':
            text = _declared_terminal_composite(text, 1)
        return text
    if path == 'examples/zero_arrow_family_observations.lp':
        return _incoming_reviewer(text)
    return None
