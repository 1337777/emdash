#!/usr/bin/env python3
"""Finite strict 2-category audit of Cartesian versus lax walking-arrow Homs."""
from dataclasses import dataclass
from itertools import product
import json

@dataclass(frozen=True)
class Arrow:
    name: str
    source: int
    target: int
    path: tuple[str, ...]

arrows = [Arrow(f'id{i}', i, i, ()) for i in range(4)] + [
    Arrow('u',0,1,('u',)), Arrow('v',2,3,('v',)),
    Arrow('a',0,2,('a',)), Arrow('b',1,3,('b',)),
    Arrow('bu',0,3,('u','b')), Arrow('va',0,3,('a','v')),
]
by_name = {f.name:f for f in arrows}
by_path = {(f.source,f.path):f for f in arrows}

def compose(g, f):
    assert f.target == g.source
    return by_path[(f.source, f.path + g.path)]

# The only nonidentity 2-cell is chi : v a => b u. This is the ordinary
# default-lax comparison G[p] eta[x] => eta[y] F[p] used by the core.
cells = {(f,f) for f in arrows} | {(by_name['va'], by_name['bu'])}

def vertical(beta, alpha):
    assert alpha[1] == beta[0]
    cell = (alpha[0], beta[1]); assert cell in cells
    return cell

def horizontal(beta, alpha):
    assert alpha[0].target == beta[0].source
    cell = (compose(beta[0],alpha[0]), compose(beta[1],alpha[1]))
    assert cell in cells
    return cell

# Verify the complete finite 2-category, not just one drawing.
for f in arrows:
    assert compose(by_name[f'id{f.target}'],f) == f
    assert compose(f,by_name[f'id{f.source}']) == f
for f,g,h in product(arrows, repeat=3):
    if f.target == g.source and g.target == h.source:
        assert compose(h,compose(g,f)) == compose(compose(h,g),f)
for alpha in cells:
    assert alpha[0].source == alpha[1].source and alpha[0].target == alpha[1].target
    assert vertical((alpha[1],alpha[1]),alpha) == alpha
    assert vertical(alpha,(alpha[0],alpha[0])) == alpha
    src = by_name[f'id{alpha[0].source}']; tgt = by_name[f'id{alpha[0].target}']
    assert horizontal((tgt,tgt),alpha) == alpha
    assert horizontal(alpha,(src,src)) == alpha
for alpha,beta,gamma in product(cells, repeat=3):
    if alpha[1] == beta[0] and beta[1] == gamma[0]:
        assert vertical(gamma,vertical(beta,alpha)) == vertical(vertical(gamma,beta),alpha)
    if alpha[0].target == beta[0].source and beta[0].target == gamma[0].source:
        assert horizontal(gamma,horizontal(beta,alpha)) == horizontal(horizontal(gamma,beta),alpha)
for a1,a2,b1,b2 in product(cells, repeat=4):
    if a1[1] == a2[0] and b1[1] == b2[0] and a1[0].target == b1[0].source:
        assert horizontal(vertical(b2,b1),vertical(a2,a1)) == vertical(horizontal(b2,a2),horizontal(b1,a1))

strict = []; lax = []
for f,g,a,b in product(arrows, repeat=4):
    if (a.source,a.target,b.source,b.target) != (f.source,g.source,f.target,g.target):
        continue
    lhs, rhs = compose(g,a), compose(b,f)
    square = (f.name,g.name,a.name,b.name)
    if lhs == rhs: strict.append(square)
    if (lhs,rhs) in cells: lax.append(square)

witness=('u','v','a','b')
assert witness not in strict and witness in lax
assert len(lax) > len(strict)
assert not any(f.source == f.target and f.path for f in arrows)
# Representable-family specialization: the lax under-category of the free
# 2-globe p => q has a triangle with rho: V P => Q. This keeps the same
# failure for R = Hom_K(x,-), not only for an arbitrary constant fibre.
triangle = [Arrow(f'tid{i}',i,i,()) for i in range(3)] + [
    Arrow('P',0,1,('P',)), Arrow('V',1,2,('V',)),
    Arrow('VP',0,2,('P','V')), Arrow('Q',0,2,('Q',)),
]
tnames = {f.name:f for f in triangle}
tpaths = {(f.source,f.path):f for f in triangle}
def tcompose(g,f):
    assert f.target == g.source
    return tpaths[(f.source,f.path+g.path)]
tcells = {(f,f) for f in triangle} | {(tnames['VP'],tnames['Q'])}
F = {f:by_name[{'tid0':'id0','tid1':'id0','tid2':'id1','P':'id0','V':'u','VP':'u','Q':'u'}[f.name]] for f in triangle}
G = {f:by_name[{'tid0':'id2','tid1':'id2','tid2':'id3','P':'id2','V':'v','VP':'v','Q':'v'}[f.name]] for f in triangle}
for H in [F,G]:
    for f,g in product(triangle,repeat=2):
        if f.target == g.source: assert H[tcompose(g,f)] == compose(H[g],H[f])
    for f,g in tcells: assert (H[f],H[g]) in cells
def tvertical(beta,alpha):
    assert alpha[1] == beta[0]
    cell=(alpha[0],beta[1]); assert cell in tcells
    return cell
def thorizontal(beta,alpha):
    assert alpha[0].target == beta[0].source
    cell=(tcompose(beta[0],alpha[0]),tcompose(beta[1],alpha[1])); assert cell in tcells
    return cell
for alpha,beta in product(tcells,repeat=2):
    for H in [F,G]:
        image=lambda cell:(H[cell[0]],H[cell[1]])
        if alpha[1] == beta[0]: assert image(tvertical(beta,alpha)) == vertical(image(beta),image(alpha))
        if alpha[0].target == beta[0].source: assert image(thorizontal(beta,alpha)) == horizontal(image(beta),image(alpha))
components = {0:by_name['a'],1:by_name['a'],2:by_name['b']}
comparison = {f:(compose(G[f],components[f.source]),compose(components[f.target],F[f])) for f in triangle}
assert all(c in cells for c in comparison.values())
for f,g in product(triangle,repeat=2):
    if f.target == g.source:
        assert comparison[tcompose(g,f)] == vertical(
            horizontal(comparison[g],(F[f],F[f])),
            horizontal((G[g],G[g]),comparison[f]))
for f,g in tcells:
    assert vertical(horizontal((components[f.target],components[f.target]),(F[f],F[g])),comparison[f]) == vertical(
        comparison[g],horizontal((G[f],G[g]),(components[f.source],components[f.source])))
assert comparison[tnames['V']][0] != comparison[tnames['V']][1]

print(json.dumps({
 'model':'free directed diamond with one 2-cell chi: va => bu',
 'strict_2_category_laws':'all finite unit, associativity and interchange cases verified',
 'objects':4,'arrows':len(arrows),'two_cells':len(cells),
 'walking_arrow_functor_objects':len(arrows),
 'strict_natural_transformations':len(strict),
 'lax_natural_transformations':len(lax),
 'witness':{'F':'u','G':'v','components':['a','b'],'lax_cell':'chi: va => bu',
            'strict':False,'lax':True},
 'added_lax_squares':[s for s in lax if s not in strict],
 'representable_family_witness':'triangle functors and all lax coherence checked; restriction to vertical V has the same non-strict chi',
 'boundary':'semantic profile audit; not a Lambdapi theorem or a native nerve inverse'
},indent=2))
