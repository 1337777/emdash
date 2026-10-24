"""Pinned complete original algebra/geometry reviewers; no mathematical edits.
Qualification is established by the emitted LP receipt, not this pin recipe.
"""
import hashlib

SOURCES = {'examples/commutative_ring_affine_atlas.lp': 'b4fa8310921165fc3b5bde27c8a466f3a90ef0314887e962134fb642bd38ea5e',
 'examples/commutative_ring_affine_glue.lp': 'fc49fae59768dbfa2b40da4c455a735d4b74fac2098fbf3598d8054e9bee6706',
 'examples/commutative_ring_affine_spec.lp': '3e8541748b10d3970a6efba4562bfb216f75c1e1953bb5768150af296511f4f8',
 'examples/commutative_ring_finite_covers.lp': 'd4be01bc54496ff62e5611ddd2f89f3391ae89a5acace410e7851cf13b774db8',
 'examples/commutative_ring_finite_free_direct_sums.lp': 'cbbab688dab038905bc679218d1049d65cf6a03b3c4dda2a0dd55f5d6fbb052b',
 'examples/commutative_ring_idempotent_localization.lp': 'cf0ac7b43ade569af5e39ca95245ee4d5e0df2211792ef851ff50426703bd70b',
 'examples/commutative_ring_localization.lp': '351a4060a151ae3ae247b044e7465fbe523a0356716546e4a11e8b1928a1ae91',
 'examples/commutative_ring_localization_comparison.lp': '7569745cb561f385ab62d25e65aead18489573abe4c2fcfbef9e789941914c00',
 'examples/commutative_ring_localization_overlap.lp': 'b2db4b029ba0262abb37dcea64d8fa979d9898ff1ac8713645a8003fe1e389f0',
 'examples/commutative_ring_matrix_blocks.lp': '6f540fea0d1b182258f8ad4705eb17eecab1d6c77add55d1aa8ddf7a9f5f6dcf',
 'examples/commutative_ring_morphisms.lp': 'b9924a7c9a80a6b15f8d86ac974c5df273cb8aa2a21d2f2f87f836fd11744457',
 'examples/commutative_ring_objects.lp': '4567a2c3d122373c69089b5d2dc29b4c9f344ac5f7949923f3457056d79325c2',
 'examples/commutative_ring_polynomial_algebra.lp': '0f03fe680a1209229f4b498973739867696cc614a97427ab369be75a3f67d1d6',
 'examples/commutative_ring_presentation_direct_sum_agreements.lp': '242a2cd939c7884410318b7c34cb2e049c857986a7b30332f4490a1b60b47f32',
 'examples/commutative_ring_presentation_direct_sums.lp': '2dfd7bd3fce57690fdf6161d6425f4309ea0bca600e63a8e6378d15291dd0163',
 'examples/commutative_ring_presheaf_glue.lp': 'd7043d32bd344e28cd4e0af878a0920e1dc48fbcfb3e29343b847c9fc5186721',
 'examples/commutative_ring_presheaf_locality.lp': '15f89a30d259f1bb0f255b1cbe47356f9ca42f88ca4be649c9ced73565dd94b1',
 'examples/commutative_ring_presheaf_matching.lp': '586bb7605e21abc62596c4de04c0a92eee2d1d400f20b6f6f792a2da69e22011',
 'examples/commutative_ring_split_idempotent_localization.lp': '130014f83b1a41ae26ed0c547cc893ae7d12ee5e7608f3da65fe819c240793ce',
 'examples/commutative_ring_unit_localization.lp': '2b5ee0ab3d2c4351eb76b1c450b189cc105192a853bd2d37633c7ab86bc1cd46',
 'examples/commutative_ring_zariski_basic_opens.lp': '25d298449db4d6fb3c2667aa491f1683985fbfa4247dce854a45bcb0d69966fc',
 'examples/commutative_ring_zariski_compatible_topology.lp': '87f332c10dec90f513b004ac68b9725e1e9be280b5d83bf648c2fdb0d846508e',
 'examples/commutative_ring_zariski_finite_containment.lp': '6569af30706410e0f5ec574de8c3db020af243868105f705483902c52722cc9f',
 'examples/commutative_ring_zero_localization.lp': '03d42029830f4bf060b40ef7a92ebd6ec2fc118c7e37565c9dbc17fa3e850293',
 'examples/commutative_ringed_sites.lp': '7556c9be6a93849c77ef0a521684792bb20b66eb21d06b81a67247ca47da6018',
 'examples/emdash3_2_commutative_algebra_bounded_free_chain_maps_example.lp': '86b130ee4e1293a5e6054495479938ba608cbd60e4b7b1ff1af114ce95f770ff',
 'examples/emdash3_2_commutative_algebra_bounded_free_complexes_example.lp': 'f6d1c0bc750a348d8696602dce58afd87ce03b71528bca4d47478a78c8aac6a1',
 'examples/emdash3_2_commutative_algebra_finite_free_category_example.lp': '249b6732f66c2539c7e18bf813734df7f002f0ed7730efb01723546193160886',
 'examples/emdash3_2_commutative_algebra_finite_modules_example.lp': 'b2dbd3ec3cf7829e3a3bc41f194b7ef904b13799149a944511ced206218f9915',
 'examples/emdash3_2_commutative_algebra_presentation_agreement_operations_example.lp': '7a85a7709eff49989d5bc5868bc71b1850767327aa53784771d95aeea4d48f2e',
 'examples/emdash3_2_commutative_algebra_presentation_operations_example.lp': '61bdfc9c56de708ab46e10d72aa5e0069c1009cbc4455096b752ea6fb911fa9c',
 'examples/emdash3_2_commutative_algebra_presentation_subtractive_operations_example.lp': '9508565af31ff01caca5045c9a71d9817b76fa50a5686342cfd13d1a987c575f',
 'examples/emdash3_2_commutative_algebra_presentations_example.lp': '18b49756b826c43b0f714b971452eba8377f32566674471ac53ecf3b1b8f35df',
 'examples/integer_localization.lp': 'f53a3fea4862c5f35b40b7b84e302560dea50191adb048e7baebb622b90851f5'}


def migrate_algebra_reviewer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest() == SOURCES[name], name
    return original
