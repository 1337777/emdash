"""Source-pinned finite-free additive prerequisites.

Retain the original products, terminal zero and additive proof bodies.
This helper adds no declaration, rule or source adaptation.
"""
import hashlib

SOURCES = {'emdash3_2_commutative_algebra_finite_free_additive.lp': '8f813437f3dde513356be185fd4f50bf45359506660ac3842689b3945e5e7a16',
 'emdash3_2_commutative_algebra_finite_free_binary_products.lp': '475c753d0c5c071c02351758fa418c53ae3e8ccf782234db28dd4c6c1dc9e4c0',
 'emdash3_2_commutative_algebra_finite_free_cartesian.lp': '82845df1a699db7c76b7aa8c868301d27d25ed65af577414c190c31ba0a31f5b',
 'emdash3_2_commutative_algebra_finite_free_preadditive.lp': '81dcfbe62c091fb2a9838cf2b29301f66b704c981747cd825052571e564def03',
 'emdash3_2_commutative_algebra_finite_free_terminal_zero.lp': '8afcc370fdeb3836bdc5bcf1281f52aad3bf905c96c7eac3c0d356b4a2701a6c',
 'examples/commutative_ring_finite_free_additive.lp': '8e364f3f21ebb34628beefb3211a3ef36b82e145e6aaaed988419e7ec0f80500',
 'examples/commutative_ring_finite_free_preadditive.lp': '096d111bb04dfbcb23ca9f88b9da0f91601f08ee8f8a0c8a65e9d43e31634a99'}

def migrate_finite_free_additive_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    return original
