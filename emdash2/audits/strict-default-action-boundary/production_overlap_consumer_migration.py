"""Pinned original chart/Laurent/projective-presentation consumers; no formal edits."""
import hashlib
SOURCES = {'emdash3_2_commutative_algebra_affine_cover_refinements.lp': '6ab45db1dfac382f6a226ad58e22d1d2135088333f630d0fe2e51d08f3e15071',
 'emdash3_2_commutative_algebra_affine_intersections.lp': '8f2646314f954102faeb62c1d294e0dcc3424d95a5f9daa9fa9f1caed2726358',
 'emdash3_2_commutative_algebra_laurent.lp': '570b3e8f072b87aa0a393e3d25cf9c19eb25bfe75fd8e5a700dbdd7847045736',
 'emdash3_2_commutative_algebra_projective_line.lp': '96ff9a5575b97d005116a0b6add64f4a5153a0023e45d8c95ce41f9ca17986ee',
 'emdash3_2_commutative_algebra_scheme_chart_overlaps.lp': '33f5c593d7925d488b86f48c643450101f05bdd1f56a49d388c949dbfe006c46',
 'emdash3_2_commutative_algebra_scheme_laurent_overlaps.lp': '11ea7cb474fbc198eaa4ed55b02767eef888755c37a95493703b6c752371b47c',
 'emdash3_2_commutative_algebra_site_relative_schemes.lp': '229a52dfd0834e7933e73bde3bdb596a79316435cd893b96c23b0691ea6f91c8',
 'examples/commutative_ring_affine_cover_refinements.lp': '3fcbdbed6f85b9e9220434cff1f02b6e7f8da146dd5354a08ff6a97ca632f8c5',
 'examples/commutative_ring_affine_intersections.lp': '8250fd055ac2eb4b657960a85b34a2860044a8cfee21e90523fb4d2224f5e51d',
 'examples/commutative_ring_laurent.lp': 'fef4a53dbbd5a420c5f6faf70d3070ec75fccb67e732404e9b82b1a6693bd2dc',
 'examples/commutative_ring_projective_line.lp': '316513cbb1ef4fb7a94d88314afede6153dec61e7cfe28d988b00f565b1ef953',
 'examples/commutative_ring_scheme_chart_overlaps.lp': '08ad88cbec0542aab349eb4cb8994bdd44f26b72137e54c80437b1bc7e155c0a',
 'examples/commutative_ring_scheme_laurent_overlaps.lp': '8335d9ea48d8882ed078e74d46c25beefe8e0962036109114e01feddb5044207',
 'examples/commutative_ring_site_relative_schemes.lp': '13cd8569605a613301bfbcb69ef3894539c5c6be724901b36e67985af20729c1'}

def migrate_overlap_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest()==SOURCES[name], name
    return original
