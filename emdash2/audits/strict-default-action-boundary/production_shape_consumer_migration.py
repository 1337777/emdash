"""Original cubical/Gray shape consumers at the strict default; no new nerve theorem."""
from pathlib import Path
import hashlib
from production_strict_wrapper_finish import calls, rename_code, remove_decl, ALIASES, RENAMES
AUDIT=Path(__file__).resolve().parent
SOURCES = {'emdash3_2_cubical_arrow_composition.lp': '6f7f20fd141de7478cbd028b6ee257506ae0149128e35a629c4822ebc4708fb1',
 'emdash3_2_cubical_arrow_functor.lp': '833091cc2e17b7089c7bf9caf59c090232752165c1c48b1e4dda36a1a2d57ddc',
 'emdash3_2_cubical_levels.lp': '956003355c38ae379a81dca2ae458c6c559c399332e5e11394307ea3f5e30242',
 'emdash3_2_cubical_square_level.lp': 'b6ad8254211f6913a81d7e88b39a57f16db73cd4bb219d241f0de16ff945ce11',
 'emdash3_2_finite_arrow_tail_init.lp': '1f0c84ec6f986444e0c38a024df8166dcbf864a755e64f7e95da912001340442',
 'emdash3_2_gray_cube_decoder.lp': 'db19c63d890a371eac7fc841b607c83a27d3c9e2187feff8c04cf7e0a77074a9',
 'emdash3_2_gray_cube_dimension2.lp': 'db6782cb7a8d111e0f972e701024808f39c406a192289bb3a1ad3859145e86fa',
 'emdash3_2_gray_cubes.lp': '49728a469917bc1b48426b8e52f3c7f9494a63e1154bc28f2227b5120cf6035d',
 'emdash3_2_gray_transformation_graph_profile.lp': '03299f9dff2e2569fbc4399d9ad894fc780da4dfd99f03296558a85fff7a2aea',
 'emdash3_2_readable_pseudofunctors.lp': 'afbe9bf67dd2c9455e6420a3deca249c9d5a96aff4a65bf71947ac5ee6d3a44d',
 'emdash3_2_semicubical_face_action.lp': '3d45aaac54551aa32c586e56a2c7487ca4104c5aea51fa89480666b26eb8a7c9',
 'emdash3_2_semicubical_face_codes.lp': 'ec1b56e3a6dc533f3706259c2c836cfad49d9ff90630096507dd5ed3bd280ec4',
 'emdash3_2_semicubical_frames.lp': '712e1639d497e5b138765f7317fe22cdf09926619ebeedd6ab545d4439ab510a',
 'emdash3_2_semicubical_index.lp': 'e6c9b09697ef1da5d1f35ac76d1b3d8bc325d88346283f1038699d7fbbe9b50e',
 'emdash3_2_semicubical_nerve.lp': '7c65373ddf136c5c3a92d64438ce3135645fb3f4b28838c01b7523409001560f',
 'examples/cubical_arrow_composition.lp': '17446f6c278161887236aa1e4e80c49da8ed69ada06388684b6e6722ed4e694c',
 'examples/cubical_arrow_functor.lp': '0b6b7073dafba039ec752f49e7e3896a169231167861eb6e4e356edb92dfc7d6',
 'examples/cubical_levels.lp': '4e58c42bfd1c58cd23a5f698dbe17255cb8822b6a684384265b633bc908fa5a2',
 'examples/cubical_square_level.lp': '4b353fb93a5f97c0204df1576590f4df9e38a6d3492d8a128874b901a77904f2',
 'examples/finite_arrow_tail_init.lp': '15341186900c22bc64d1e314a5eed76cc779bb1fb6d86e8718c3ddf67058a155',
 'examples/gray_cube_decoder.lp': 'e70e48fe9d4d3a270fafcdc44c06e1f7ccfda425df68f8cf61f5d2ec6cd84127',
 'examples/gray_cube_dimension2.lp': 'be1a0958d0dc2114edd097020868d9e7ff7e86fb56e37ec7a703ee84c7cbaf30',
 'examples/gray_cubes.lp': '45f37f5a978fa7f521c039082c38f861e4a4283fb15094989be138dfb44e4fe9',
 'examples/gray_transformation_graph_profile.lp': 'cc250c6b7b1ababc9b706339be5446bc3a2c84d3f8be69821917ee715f6d89ba',
 'examples/semicubical_face_action.lp': '81f793b28340e670eedd5d0c709e6b511f9aeea73b84befedf056cfb0b9ea660',
 'examples/semicubical_face_codes.lp': '974b30ea15c389f55ee6b2a824a0f22e31dd8ba72c2ba1e9822b73777bfd429f',
 'examples/semicubical_frames.lp': '07932016ddc0bc90d72c6e0845bb3ab07927a6e912b729ce20e71d9d27889b21',
 'examples/semicubical_index.lp': 'd64155a9b27ef82e63414e59c73202bad8118437f26690f5b802bf44c4e48f8d',
 'examples/semicubical_nerve.lp': '41c613e191579f69d33019ff771062c4a23aaef8a466ecec88097d2ee0ac9b0c'}

def migrate_shape_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest()==SOURCES[name], name
    old=original
    text = old
    counts = {}
    if name == 'emdash3_2_gray_transformation_graph_profile.lp':
        for symbol in ['gray_transf_graph_is_strict', 'strict_gray_transf_graph']:
            text, removed = remove_decl(text, symbol)
            assert removed
        text = "/* Default strict functors already classify the existing whole graph.\n   The former strict object wrapper and its unused supplied admission proof\n   are retired. LaxTransfor and the graph's noninvertible cell are unchanged.\n   This import facade preserves the original module boundary. */\nrequire open emdash.emdash3_2_gray_cubes;\n"
    for symbol in ['strict_functor', 'strict_functor_underlying']:
        text, n = calls(text, symbol, 3, 1, lambda args, explicit: args[-1])
        counts[symbol] = n
    text, n = calls(text, 'make_strict_functor', 4, 2, lambda args, explicit: args[-2])
    counts['make_strict_functor'] = n
    mapping = {**ALIASES, **RENAMES, 'strict_gray_transf_graph': 'gray_transf_graph_func'}
    text = rename_code(text, mapping)
    if name == 'emdash3_2_readable_pseudofunctors.lp':
        anchor = 'require open emdash.emdash3_2_gray_profiles;'
        assert text.count(anchor) == 1
        text = text.replace(anchor, anchor + '\nrequire open emdash.emdash3_2_strict_functor_actions;', 1)
        start = text.index('symbol readable_pseudo_post_source_path')
        end = text.index(';', start) + 1
        decl = text[start:end]
        head = decl.split('≔', 1)[0]
        text = text[:start] + head + '≔' + (AUDIT / 'production_shape_pseudo_source_path.lpfragment').read_text() + text[end:]
        first = text.index('/*')
        last = text.index('*/', first) + 2
        text = text[:first] + '/*\n  Emdash v3.2: retained fixed-forward pseudofunctor data for default functors.\n\n  Public Functor is strict; its existing extracted compositor computes to the\n  strict default. The readable endpoint paths use the established stable\n  postcomposition views and default functor-composition path.\n\n  IsPseudoFunctor remains the existing dependent property with actual selected\n  OmegaEquivAlong inverse data. This migration does not replace that inverse,\n  add a compositor, or introduce a lax-functor carrier. Existing supplied\n  identity/composition property constructors retain their original status.\n*/' + text[last:]
        text = text.replace('Neither path identifies\n  those two endpoints with each other.', 'The strict default also supplies their existing composition agreement.')
        text = text.replace('current ambient normal-lax convention.', 'default strict-functor convention.')
    if name == 'emdash3_2_readable_pseudofunctors.lp':
        start = text.index('/*\n  Direct endpoint observations after whole ambient functoriality migration.')
        end = text.index('*/', start) + 2
        text = text[:start] + '/*\n  Readable endpoint views under the strict default. The stable postcomposition\n  owners need not share a runtime normal form. Their existing endpoint paths\n  and the generic functor-composition path compare the intrinsic action with\n  the readable mapped composite, without a new unification rule.\n*/' + text[end:]
    if name == 'examples/gray_transformation_graph_profile.lp':
        assert text.count('assertnot ') == 1
        text = text.replace('assertnot ', 'assert ', 1)
        text = text.replace('// The explicit raw graph observation computes through hom action; the stable\n// strict view checked below deliberately remains at runtime.', '// Default functors expose the original whole graph and its action directly.')
        text = text.replace('// The classified graph reconstructs strictness canonically; its admission\n// certificate is not projected from the opaque object.', '// Canonical strictness is derived for the actual default graph functor.')
    if name == 'examples/gray_cube_decoder.lp':
        text = text.replace("// The successor graph's classified carrier compares proof-time with the whole\n// graph; the strict discriminator remains at runtime.", '// The successor graph is the existing whole graph at the default functor carrier.')
    if name == 'emdash3_2_gray_cube_decoder.lp':
        text = text.replace('StrictFunctor(GrayCubePos_R(n),C)', 'Functor(GrayCubePos_R(n),C)').replace('strict graph package', 'whole graph').replace('strict codes', 'default functors')
    if name=='emdash3_2_semicubical_nerve.lp':
        start=text.index('// Named direct strict composition')
        end=text.index('symbol semicubical_nerve_composition_path',start)
        assert text[start:end].count('rule @comp_fapp0')==1
        text=text[:start]+'// Composition is now supplied by the public strict-functor default.\n// Keep the original whole comparison and recursive-action distinction.\n\n'+text[end:]
        text=text.replace('  This module adds the nerve object beta and one guarded named composition\n  owner.', '  This module adds the nerve object beta; composition uses the strict default.')
    return text
