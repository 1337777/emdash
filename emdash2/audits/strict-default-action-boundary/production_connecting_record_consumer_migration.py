"""Source-pinned original connecting-record consumers.

Keep actual whole universal data and original derived proof bodies.
"""
import hashlib
import re
from production_diagram_observation_migration import _atom

SOURCES = {'emdash3_2_homology_connecting_characterization.lp': {'diagramCategory': 0,
                                                       'encodedDiagram': 0,
                                                       'initialOp': 0,
                                                       'sha256': '8d87d14509f1005ffac447333e4909cd13a1907e28c58c1e9977a05021040a28'},
 'emdash3_2_homology_connecting_cover.lp': {'diagramCategory': 0,
                                            'encodedDiagram': 0,
                                            'initialOp': 0,
                                            'sha256': 'a14286d5b9085847f6b1efd9214501fe00d7b237f2bb0093fd8afb49daaeb076'},
 'emdash3_2_homology_connecting_cover_kernel.lp': {'diagramCategory': 0,
                                                   'encodedDiagram': 0,
                                                   'initialOp': 0,
                                                   'sha256': '6893b2a81913969813bd58f5ded0f4a7546d30c18d0de0bd1daffaf9f21911f8'},
 'emdash3_2_homology_connecting_cover_kernel_boundary.lp': {'diagramCategory': 0,
                                                            'encodedDiagram': 0,
                                                            'initialOp': 0,
                                                            'sha256': 'c468888a47b815ffd703739791b2222da3fe144fbbc96544d98e2be1ed73c8d8'},
 'emdash3_2_homology_connecting_cover_kernel_lift.lp': {'diagramCategory': 0,
                                                        'encodedDiagram': 0,
                                                        'initialOp': 0,
                                                        'sha256': '4db6f513367d330df442e33a7ad8d6b0ce53cb17c0088fd2074340a1546b7bae'},
 'emdash3_2_homology_connecting_cover_quotient.lp': {'diagramCategory': 0,
                                                     'encodedDiagram': 0,
                                                     'initialOp': 0,
                                                     'sha256': '2f680cdba53c27949c6d4cbdaceede150c3bd0b1906b95c67f734930d4191924'},
 'emdash3_2_homology_connecting_cycles_descent.lp': {'diagramCategory': 0,
                                                     'encodedDiagram': 0,
                                                     'initialOp': 0,
                                                     'sha256': 'cd80a546fca9ae4482eaafec877e00c8eddd0f268617c613ef4622897ae9b695'},
 'emdash3_2_homology_connecting_inclusion_zero.lp': {'diagramCategory': 0,
                                                     'encodedDiagram': 0,
                                                     'initialOp': 1,
                                                     'sha256': '8e5d3e8e4b1a23efc51a652026f271840ab5cd3bf9bc90a290e2fa065accdfe2'},
 'emdash3_2_homology_connecting_left_lift.lp': {'diagramCategory': 0,
                                                'encodedDiagram': 0,
                                                'initialOp': 0,
                                                'sha256': '715ee0e44f6fdf419db17c3882e2908205575fe91034794662c7a3debdf50d72'},
 'emdash3_2_homology_connecting_projection_zero.lp': {'diagramCategory': 0,
                                                      'encodedDiagram': 0,
                                                      'initialOp': 1,
                                                      'sha256': '2533201a500203f2fdf2d3fb58e4885812a3e6d21a5c1a7d0c2ef738ddabd0f5'},
 'emdash3_2_homology_connecting_source_boundary_cover.lp': {'diagramCategory': 0,
                                                            'encodedDiagram': 0,
                                                            'initialOp': 0,
                                                            'sha256': 'f50062edb82c1a5b3531ed6a1ca21cefa2f73d90dcf30df884ca03cb4e9c5d47'},
 'emdash3_2_homology_connecting_source_boundary_descent.lp': {'diagramCategory': 0,
                                                              'encodedDiagram': 0,
                                                              'initialOp': 0,
                                                              'sha256': '4a8ce85ecfed2bde250d642314c8868c5aa3ddfede5aaded534e880d530a74bb'},
 'emdash3_2_homology_connecting_source_boundary_zero.lp': {'diagramCategory': 0,
                                                           'encodedDiagram': 0,
                                                           'initialOp': 0,
                                                           'sha256': '764b9f0d23b83cfd2b47edb8e0898614be541d646fdeafa8503ecb34a7aa8b7f'},
 'emdash3_2_homology_connecting_target_cycles.lp': {'diagramCategory': 0,
                                                    'encodedDiagram': 0,
                                                    'initialOp': 0,
                                                    'sha256': '167d171d6eea16e22ad1d3fa645f3c20b662a7490d88ad354133acd482254c02'},
 'emdash3_2_homology_record_connecting.lp': {'diagramCategory': 0,
                                             'encodedDiagram': 0,
                                             'initialOp': 0,
                                             'sha256': '41ccdacbb1ba57fcacd6319827d13912b1cf916f32edb2d69855a25c39941ffe'},
 'emdash3_2_homology_record_zero.lp': {'diagramCategory': 0,
                                       'encodedDiagram': 0,
                                       'initialOp': 0,
                                       'sha256': 'b26b365b7cedd7f658e6e72b07860cd8b11a72352c18d9ea54089a4138adfe1b'},
 'examples/homology_connecting_characterization.lp': {'diagramCategory': 0,
                                                      'encodedDiagram': 0,
                                                      'initialOp': 0,
                                                      'sha256': 'dddc648d3efef4cf66ea7a9c80bc0a0fcf1086b101f7011eeead19df25a37531'},
 'examples/homology_connecting_cover_quotient.lp': {'diagramCategory': 0,
                                                    'encodedDiagram': 0,
                                                    'initialOp': 0,
                                                    'sha256': '52d4000c58ffcd87f1527f86653b83bf989108854e146f83f1da9038315931da'},
 'examples/homology_connecting_cover_whole.lp': {'diagramCategory': 2,
                                                 'encodedDiagram': 2,
                                                 'initialOp': 2,
                                                 'sha256': '15837d42d4f6b3fec1f9963b20816124569d57dbccd43f084d6d2f94a8f2f57f'},
 'examples/homology_record_connecting.lp': {'diagramCategory': 0,
                                            'encodedDiagram': 0,
                                            'initialOp': 0,
                                            'sha256': 'e08bba183cea97c3d9699f32b5566af79dd8812003b65227ab3a594b4fe85de6'},
 'examples/homology_record_connecting_whole.lp': {'diagramCategory': 0,
                                                  'encodedDiagram': 0,
                                                  'initialOp': 1,
                                                  'sha256': '00df6d69035d793dc2c3046b61bd9c2b3f23910ec0295358d5acb2b2f5d1f0ed'}}

def migrate_connecting_record_consumer(name, original):
    if name not in SOURCES:
        return None
    spec = SOURCES[name]
    assert hashlib.sha256(original.encode()).hexdigest() == spec['sha256'], name
    text, count = re.subn(r'\bOp_cat(?=\s+C\b)', 'TotalOp_cat', original)
    assert count == spec['initialOp'] and len(re.findall(r'\bOp_cat\b', original)) == count, name
    text, count = re.subn(r'\bFunctor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', text)
    assert count == spec['diagramCategory'], name
    encoded = 0
    if name == 'examples/homology_connecting_cover_whole.lp':
        matches = list(re.finditer(r'\(@chain_pair_outgoing_diagram\b', text))
        for match in reversed(matches):
            diagram, end = _atom(text, match.start())
            text = text[:match.start()] + '(@OddDual_func WalkingArrow_cat C ' + diagram + ')' + text[end:]
            encoded += 1
    assert encoded == spec['encodedDiagram'], name
    return text
