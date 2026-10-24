"""Source-pinned original witnessed Freyd homology and matrix consumers.

Retain witnessed normality, selected homology and actual raw matrix inputs.
The complete original source is unchanged.
"""
import hashlib

SOURCES = {'emdash3_2_commutative_algebra_freyd_bounded_complexes.lp': '804d20edfe5710d3b9b9ea88e20f6963d51e0b394e764903cee74d615c320545',
 'emdash3_2_commutative_algebra_freyd_explicit_spines.lp': 'a6f5a863d0eac2f1cadb10254ed396c5ae14e8123d26f6ae7bd504c4db59bfe2',
 'emdash3_2_commutative_algebra_freyd_functorial_homology.lp': '25832692e42deb56b95c338f220cb3812d9ee0dd16d12d831c341211b8a01e56',
 'emdash3_2_commutative_algebra_freyd_homology.lp': '6999e9cea9ad59473ca1b9d3b05902033c241398db7ad7c49623021b9939fb01',
 'emdash3_2_commutative_algebra_freyd_native_snake_matrices.lp': 'd10d621bffb707ee6e415d9bc81ec6f2abb8bcb03b6b3c658d385ba5d8d3175a',
 'emdash3_2_commutative_algebra_freyd_normal_epimorphisms.lp': 'b05060e7820b851b011586c5e36c2be542baf1046659b8dae6b2721d1bd9d60b',
 'emdash3_2_commutative_algebra_freyd_normal_monomorphisms.lp': '9be6597f4f61367f7c623dbcac1bf8dea43b7dc94a65b462454ccb30822e2cc0',
 'emdash3_2_commutative_algebra_freyd_selected_homology.lp': '2c47435a6a213a94c370789fac49c1f0a4a64df9faa531a8bee1743730af789e',
 'emdash3_2_commutative_algebra_freyd_witnessed_abelian.lp': '7e2bd183fc9ce9eeb7699f7fc2ee04df333367aa71460eea46bb75d352a6ecf6',
 'examples/commutative_ring_freyd_bounded_complexes.lp': '29682cdb7be5d3453d45a8e23b05d1c022b1fd36556bc5342d0afd39f9aa63ed',
 'examples/commutative_ring_freyd_explicit_spines.lp': 'f089efcfb77e4b7decbb2fc053bd0dc283ec2fe6c8071c1358739c5f41676023',
 'examples/commutative_ring_freyd_functorial_homology.lp': 'e512f8971717eb259c68d752a6c5299c9c6718f0c82b8da7ee407b0319b1053d',
 'examples/commutative_ring_freyd_homology.lp': '34cff64380f03e3a76c3f28909a3bc249aa9cc771363c3134a4aa4c0453d2a96',
 'examples/commutative_ring_freyd_normal_epimorphisms.lp': '73bbe2386bdd5d803b2d4bf3dc05bcb3a8b5a8b6e2cfebce4e1dbb8b351a90ac',
 'examples/commutative_ring_freyd_normal_monomorphisms.lp': '2c3a14c8c0cfb1ede1f009b189e987a309c2b7474d8fd8a3b47c70e473a44450',
 'examples/commutative_ring_freyd_raw_witnesses.lp': 'c262efdd602b930167264f4ad49f3a4089f3b343be6f18562384db1786089d42',
 'examples/commutative_ring_freyd_selected_homology.lp': '95c184d0e4229c3e5beddfe93c21b3ccfd95ae3d0fbbdc819a0cb390767acb66',
 'examples/commutative_ring_freyd_witnessed_abelian.lp': 'd536891510c5fe8332eaf07e07606a662cc422be5ffbf58fd8bd910fb761ac0a',
 'examples/freyd_native_snake_matrices.lp': '068b67460a12396e5de9523b8e95ba1de161ad84ef7f46f6c8c2cb1e51f5a046'}

def migrate_freyd_witnessed_homology_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    return original
