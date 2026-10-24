"""Pinned original site/locally-ringed-space consumers already fit the migrated foundation."""
import hashlib
SOURCES = {'emdash3_2_commutative_algebra_affine_basis.lp': 'e16807681c90f0b8032f95f902cc0d587322737f8e52409698f75c2298065ed6',
 'emdash3_2_commutative_algebra_affine_cover_charts.lp': '69981b2b3affb123f3adc47b3e9c4fa0ac2a2163bbffceefe28e9c8fee07df26',
 'emdash3_2_commutative_algebra_affine_cover_presentations.lp': 'f32d0b15fb1181fe158deb391890a0fe87363ee0a69e832f5dc3df115bc5e636',
 'emdash3_2_commutative_algebra_affine_locality.lp': '6b101a547db8a016f02c327f093ee2aa9a30d7a5bb77764b3909895bccd87eef',
 'emdash3_2_commutative_algebra_affine_points.lp': 'c160f97b4528082e0e6b1d6691322e7831867f07c9978fc817ab202166ffa0ec',
 'emdash3_2_commutative_algebra_affine_ringed_sites.lp': '4b414830909c35053b054dfa78cfc4881fd7e7c149190d6f055bdfbf6af70c8b',
 'emdash3_2_commutative_algebra_affine_schemes.lp': 'c39401996c59d67c36017c6a1ab1e9808dfa600418b89efbc0bf14b4240c6a40',
 'emdash3_2_commutative_algebra_affine_zariski.lp': '05f3a2823c0e9aef38e390fdf15ebc49949c15423ff57706022ecc522784d22c',
 'emdash3_2_commutative_algebra_binary_covers.lp': 'f9aacbe3a7ad4c8dbee5b0aee418a5a6cda3dc0069979b2938404e6c076ef933',
 'emdash3_2_commutative_algebra_local_ringed_sites.lp': '7f80db02204d50c65ab01bdc5e2c0bd2c523da71803d855a3608c5aca507cd86',
 'emdash3_2_commutative_algebra_locally_ringed_space_presentations.lp': '901c851a6175029ecc0338bd4c433c64416add87ab1fc6fcea4e18f017077eaf',
 'emdash3_2_commutative_algebra_ringed_space_covers.lp': '1038eaec19a9af02d2054e71470df6f5ece68021c34dabe7a8e08cf12f36b47f',
 'emdash3_2_commutative_algebra_ringed_space_restrictions.lp': '32ffa092dc4260ecf1d1b88c414c98360824e041e42f3d7bf99fc6c2c0394d19',
 'emdash3_2_generated_topologies.lp': '82f2b2792e213c0f929ca6adc3dec7dd1786395a2d6e8642192b621cf5a5681b',
 'emdash3_2_site_basis.lp': '55cad0ea40cd2fc52a0e2f643415a457ecbe7483bda453ab873c0b8719c3dda1',
 'examples/commutative_ring_affine_basis.lp': 'bcae6e4b536772d1fa71fc728e152ff6d91415994e957b08a2768ad2b1ac57ed',
 'examples/commutative_ring_affine_cover_charts.lp': '558e49058a1983aceefe0adfd1ee58ccc81d0193a6b879470cf85eedae0cb951',
 'examples/commutative_ring_affine_cover_presentations.lp': '463dd451de4e540021626ff0bdfa42364b1f2e6bcf0cb62737f0c340c2499515',
 'examples/commutative_ring_affine_locality.lp': '3d2069aae1acdee0800816e6a42897c230ddcc3ecaf274fcbf5350719a252a9c',
 'examples/commutative_ring_affine_points.lp': '7a7ebc65e96a6b5d50551fc9fa728a5fd1b7ecf97e62b6122a8c24e5b2af2dc7',
 'examples/commutative_ring_affine_ringed_sites.lp': 'ce6cce11cd14463d874790b97af444d72f559856e4ef67c88fb261a148f49cf8',
 'examples/commutative_ring_affine_schemes.lp': '82bf9ad60646941fc6630fe3a56687bd35bf7e312b36de395c5644a5d20127c6',
 'examples/commutative_ring_affine_zariski.lp': '18fa32996e2d6c3e58de37860bbc99a14d95bbe8633ceef48420b261396a6026',
 'examples/commutative_ring_binary_covers.lp': '89a6171196690fd227296f67aaeac51563c81d954c254049ac630ec6eb9cb2c9',
 'examples/commutative_ring_local_ringed_sites.lp': 'efc3c1052967871c2cf8ae027059dd38fb48878219c1e9cd5f37c8a16868a395',
 'examples/commutative_ring_locally_ringed_space_presentations.lp': '62ac39baf3c781d97b85fc0858eb853469c0545b46ca933b77d66f3b05ed3cb4',
 'examples/commutative_ring_ringed_space_covers.lp': '6723dc211ce8ed176608166286c3734395076bb7312a7d001375f55e6ece7ae7',
 'examples/commutative_ring_ringed_space_restrictions.lp': 'fd4e38f665113bb7116f223668849c3fba2b9a0fe9e071194b600a80829654f6',
 'examples/generated_grothendieck_topologies.lp': '9762602f23f0ccf1e49bdde3d0c96c4d558991dc2bf699c3463e1c8f2eaa45a6',
 'examples/site_basis.lp': '4a9174b5f00ea9a6de5ff1b4e3625ab147b78aad1dc4cf0d4b8534e1d16b7d3a'}

def migrate_site_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest()==SOURCES[name], name
    return original
