/** Existing native higher precomposition and its ordinary component ladder. */
import { binderMode } from './kernel';
import {
    CoreLfModuleSpec, CoreLfQualifiedSymbol, CoreLfTransferBuilderExpression as Expr,
    CoreLfTransferDeclaration, CoreLfTransferProofRule, CoreLfTransferRuntimeRule,
    CoreLfTransferScopedBuilder as Builder, coreLfQualifiedSymbol,
    coreLfTransferAbsentBody, createCoreLfModuleSpec, createCoreLfTransferPolicyOverlay
} from './lf_transfer';
import { compileCoreLfDeclarations, createCoreLfTransferDeclarationLinkage } from './lf_transfer_compiler';
import { CoreLfDeclarationEnvironment } from './lf_declarations';
import { CoreLfMixedDeclarationContext } from './lf_transfer_mixed';
import { CoreLfCompiledRuntimeFragment, compileCoreLfRuntimeFragment } from './lf_transfer_runtime';
import { compileCoreLfProofProgram } from './lf_transfer_proof';
import { CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE } from './categorical_displayed_nd_higher_foundation_transfer';
import { CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE } from './categorical_fibred_transfd_transfer';
import { CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE } from './categorical_fibred_product_transfer';
import { CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE } from './categorical_structural_transfer';
import { CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE } from './directed_continuation_transfer';
const moduleId = 'emdash.emdash3_2';
const sym = (name: string): CoreLfQualifiedSymbol => coreLfQualifiedSymbol(moduleId, name);
const source = (sourceFragment: string) => ({ authorityPath: 'emdash2/emdash3_2.lp', sourceFragment });
const sha = 'sha256:70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e';
const implicit = binderMode('implicit', 'functorial'), explicit = binderMode('explicit', 'functorial');
type Scope = Readonly<Record<string, Expr>>;
type Body = (b: Builder, s: Scope) => Expr;
type Param = readonly [
    string,
    'implicit' | 'explicit',
    Body
];
const call = (b: Builder, name: string, args: readonly Expr[], implicitCount = 0): Expr => b.call(b.global(sym(name)), args.map((value, i) => ({ value, plicity: i < implicitCount ? 'implicit' : 'explicit' })));
const cat: Body = b => b.global(sym('Cat'));
const universe = (b: Builder) => b.global(sym('Cat_cat'));
const obj = (b: Builder, A: Expr) => call(b, 'τ', [call(b, 'Obj', [A])]);
const hom = (b: Builder, A: Expr, x: Expr, y: Expr) => call(b, 'Hom_cat', [A, x, y]);
const fn = (b: Builder, A: Expr, B: Expr) => call(b, 'τ', [call(b, 'Functor', [A, B])]);
const fc = (b: Builder, A: Expr, B: Expr) => call(b, 'Functor_cat', [A, B]);
const cc = (b: Builder, A: Expr, B: Expr) => call(b, 'Functor_cart_cat', [A, B]);
const cart = (b:Builder) => b.global(sym('Cat_cart'));
const op = (b:Builder,A:Expr) => call(b,'Op_cat',[A]);
const represented = (b:Builder,A:Expr,B:Expr,F:Expr,W:Expr) => call(b,'hom_',[A,B,F,W],2);
const representedAction = (b:Builder,s:Scope,p?:Expr) => b.call(b.global(sym(p===undefined?'hom_int_precomp_tele_func':'hom_int_precomp_func')),
    [s.A,s.B,s.F,s.Y,s.X,...(p===undefined?[]:[p])].map((value,i)=>({value,plicity:i===2||i===5?'explicit':'implicit'})));
const representedParams:readonly Param[] = [['A','implicit',b=>b.global(sym('Cat'))],['B','implicit',b=>b.global(sym('Cat'))],
    ['F','explicit',(b,s)=>fn(b,s.B,s.A)],['Y','implicit',(b,s)=>obj(b,s.A)],['X','implicit',(b,s)=>obj(b,s.A)]];
const representedDomain = (b:Builder,s:Scope)=>hom(b,op(b,s.A),s.Y,s.X);
const representedCodomain = (b:Builder,s:Scope)=>hom(b,cc(b,s.B,cart(b)),represented(b,s.A,s.B,s.F,s.Y),represented(b,s.A,s.B,s.F,s.X));
const app = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr) => call(b, 'fapp0', [A, B, F, x], 2);
const action = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr, y: Expr, p?: Expr) => b.call(b.global(sym(p === undefined ? 'fapp1_func' : 'fapp1_fapp0')), [A, B, F, x, y, ...(p === undefined ? [] : [p])]
    .map((value, i) => ({ value, plicity: i === 2 || i === 5 ? 'explicit' : 'implicit' })));
const comp = (b: Builder, A: Expr, B: Expr, C: Expr, G: Expr, F: Expr) => call(b, 'comp_cat_fapp0', [A, B, C, G, F], 3);
const identity = (b: Builder, A: Expr, x: Expr) => call(b, 'id', [A, x]);
const point = (b: Builder, s: Scope, g: Expr) => precomp(b, 'hom_precomp_along_fapp0', s, [g]);
const precomp = (b: Builder, name: string, s: Scope, tail: readonly Expr[] = []) => b.call(b.global(sym(name)), [s.A, s.B, s.F, s.Z, s.W, s.X, s.h, ...tail]
    .map((value, i) => ({ value, plicity: i === 2 || i === 3 || i === 6 || i >= 7 ? 'explicit' : 'implicit' })));
const higher = (b: Builder, name: string, s: Scope, alpha?: Expr) => b.call(b.global(sym(name)), [s.A, s.B, s.F, s.Z, s.W, s.X, s.h, s.g, s.k, ...(alpha === undefined ? [] : [alpha])]
    .map((value, i) => ({ value, plicity: i === 2 || i === 3 || i === 6 || i === 9 ? 'explicit' : 'implicit' })));
const image = (b: Builder, s: Scope, x: Expr) => app(b, s.A, s.B, s.F, x);
// Precomposition along h: W→X maps Hom_B(F[X],Z) to Hom_B(F[W],Z).
const from = (b: Builder, s: Scope) => hom(b, s.B, image(b, s, s.X), s.Z);
const to = (b: Builder, s: Scope) => hom(b, s.B, image(b, s, s.W), s.Z);
const domain = (b: Builder, s: Scope) => hom(b, from(b, s), s.g, s.k);
const codomain = (b: Builder, s: Scope) => hom(b, to(b, s), point(b, s, s.g), point(b, s, s.k));
const parameters: readonly Param[] = [['A', 'implicit', cat], ['B', 'implicit', cat],
    ['F', 'explicit', (b, s) => fn(b, s.A, s.B)], ['Z', 'explicit', (b, s) => obj(b, s.B)],
    ['W', 'implicit', (b, s) => obj(b, s.A)], ['X', 'implicit', (b, s) => obj(b, s.A)],
    ['h', 'explicit', (b, s) => obj(b, hom(b, s.A, s.W, s.X))],
    ['g', 'implicit', (b, s) => obj(b, from(b, s))], ['k', 'implicit', (b, s) => obj(b, from(b, s))]];
const declaration = (name: string, params: readonly Param[], result: Body, order: number): CoreLfTransferDeclaration => {
    const b = new Builder();
    const build = (i: number, s: Scope): Expr => i === params.length ? result(b, s) :
        b.pi(params[i][0], params[i][2](b, s), v => build(i + 1, { ...s, [params[i][0]]: v }), params[i][1] === 'implicit' ? implicit : explicit);
    return { order, symbol: sym(name), type: b.term(build(0, {})), body: coreLfTransferAbsentBody(),
        modifiers: { visibility: 'public', rigidity: 'ordinary', sourceOpacity: 'opaque' }, provenance: source(`symbol ${name} [A B : Cat]`) };
};
const postcomp = (b:Builder,name:string,s:Scope,tail:readonly Expr[]=[]) => b.call(b.global(sym(name)),
    [s.A,s.B,s.F,s.W,s.X,s.Y,s.f,...tail].map((value,i)=>({value,plicity:[2,3,6].includes(i)||i>=7?'explicit':'implicit'})));
const postFrom = (b:Builder,s:Scope)=>hom(b,s.A,s.W,app(b,s.B,s.A,s.F,s.X));
const postTo = (b:Builder,s:Scope)=>hom(b,s.A,s.W,app(b,s.B,s.A,s.F,s.Y));
const postDomain=(b:Builder,s:Scope)=>hom(b,postFrom(b,s),s.g,s.h);
const postCodomain=(b:Builder,s:Scope)=>hom(b,postTo(b,s),postcomp(b,'hom_postcomp_fapp0',s,[s.g]),postcomp(b,'hom_postcomp_fapp0',s,[s.h]));
const postHigher=(b:Builder,s:Scope,alpha?:Expr)=>b.call(b.global(sym(alpha===undefined?'hom_postcomp_fapp1_func':'hom_postcomp_fapp1_fapp0')),
    [s.A,s.B,s.F,s.W,s.X,s.Y,s.f,s.g,s.h,...(alpha===undefined?[]:[alpha])].map((value,i)=>({value,plicity:[2,3,6,9].includes(i)?'explicit':'implicit'})));
const postParams:readonly Param[]=[['A','implicit',cat],['B','implicit',cat],['F','explicit',(b,s)=>fn(b,s.B,s.A)],
    ['W','explicit',(b,s)=>obj(b,s.A)],['X','implicit',(b,s)=>obj(b,s.B)],['Y','implicit',(b,s)=>obj(b,s.B)],
    ['f','explicit',(b,s)=>obj(b,hom(b,s.B,s.X,s.Y))],['g','implicit',(b,s)=>obj(b,postFrom(b,s))],['h','implicit',(b,s)=>obj(b,postFrom(b,s))]];
const declarations = [
    declaration('hom_precomp_along_fapp1_func', parameters, (b, s) => fn(b, domain(b, s), codomain(b, s)), 0),
    declaration('hom_precomp_along_fapp1_fapp0', [...parameters, ['alpha', 'explicit', (b, s) => obj(b, domain(b, s))]], (b, s) => obj(b, codomain(b, s)), 1),
    declaration('hom_int_precomp_tele_func',representedParams,(b,s)=>fn(b,representedDomain(b,s),representedCodomain(b,s)),2),
    declaration('hom_int_precomp_func',[...representedParams,['p','explicit',(b,s)=>obj(b,representedDomain(b,s))]],(b,s)=>obj(b,representedCodomain(b,s)),3),
    declaration('hom_postcomp_fapp1_func',postParams,(b,s)=>fn(b,postDomain(b,s),postCodomain(b,s)),4),
    declaration('hom_postcomp_fapp1_fapp0',[...postParams,['alpha','explicit',(b,s)=>obj(b,postDomain(b,s))]],(b,s)=>obj(b,postCodomain(b,s)),5)
];
const rule = (id: string, owner: string, params: readonly Param[], left: Body, right: Body, fragment: string): CoreLfTransferRuntimeRule => {
    const b = new Builder();
    let scope: Scope = {};
    const variables = params.map(([name, , type]) => { const t = b.template(type(b, scope)); scope = { ...scope, [name]: b.capture(name) }; return { name, type: t }; });
    return { order: 0, id, groupId: id, clauseOrder: 0, sourceOwner: sym(owner), variables,
        left: b.pattern(left(b, scope)), right: b.template(right(b, scope)), provenance: source(fragment) };
};
const component = (b: Builder, A: Expr, B: Expr, F: Expr, G: Expr, x: Expr, eta: Expr) => call(b, 'tapp0_fapp0', [A, B, F, G, x, eta], 4);
const pair = (b: Builder, A: Expr, B: Expr, x: Expr, y: Expr) => call(b, 'Product_pair', [A, B, x, y], 2);
// Ordinary Cat-valued observation retains a general, possibly lax eta.
const catParams: readonly Param[] = [['K', 'implicit', cat], ['E', 'explicit', (b, s) => fn(b, s.K, universe(b))],
    ['Z', 'explicit', cat], ['X', 'implicit', (b, s) => obj(b, s.K)], ['Y', 'implicit', (b, s) => obj(b, s.K)],
    ['F', 'explicit', (b, s) => obj(b, hom(b, s.K, s.X, s.Y))],
    ['G', 'implicit', (b, s) => fn(b, app(b, s.K, universe(b), s.E, s.Y), s.Z)],
    ['H', 'implicit', (b, s) => fn(b, app(b, s.K, universe(b), s.E, s.Y), s.Z)],
    ['eta', 'explicit', (b, s) => obj(b, hom(b, fc(b, app(b, s.K, universe(b), s.E, s.Y), s.Z), s.G, s.H))],
    ['i', 'explicit', (b, s) => obj(b, app(b, s.K, universe(b), s.E, s.X))]];
const catScope = (b: Builder, s: Scope): Scope => ({ A: s.K, B: universe(b), F: s.E, Z: s.Z, W: s.X, X: s.Y, h: s.F, g: s.G, k: s.H });
const rules = [
    rule('pathind.fixed-source.transfor-classifier-delta','Transf',[
        ['A','implicit',cat],['B','implicit',cat],['F','explicit',(b,s)=>fn(b,s.A,s.B)],['G','explicit',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>call(b,'Transf',[s.A,s.B,s.F,s.G],2),
        (b,s)=>call(b,'Obj',[call(b,'Transf_cat',[s.A,s.B,s.F,s.G],2)]),
        'injective symbol Transf [A B : Cat] (F G : τ (Functor A B)) : Grpd'),
    rule('categorical.precomp.post-hom','fapp1_func',postParams,
        (b,s)=>action(b,b.wildcard(postFrom(b,s)),b.wildcard(postTo(b,s)),postcomp(b,'hom_postcomp_func',s),s.g,s.h),
        (b,s)=>postHigher(b,s),'rule @fapp1_func _ _ (@hom_postcomp_func $A $B $F $W $X $Y $f) $g $h'),
    rule('categorical.precomp.post-arrow','fapp1_fapp0',[...postParams,['alpha','explicit',(b,s)=>obj(b,postDomain(b,s))]],
        (b,s)=>action(b,b.wildcard(postFrom(b,s)),b.wildcard(postTo(b,s)),postcomp(b,'hom_postcomp_func',s),s.g,s.h,s.alpha),
        (b,s)=>postHigher(b,s,s.alpha),'rule @fapp1_fapp0 _ _ (@hom_postcomp_func $A $B $F $W $X $Y $f) $g $h $alpha'),
    rule('categorical.precomp.post-object','fapp0',[...postParams,['alpha','explicit',(b,s)=>obj(b,postDomain(b,s))]],
        (b,s)=>app(b,b.wildcard(postDomain(b,s)),b.wildcard(postCodomain(b,s)),postHigher(b,s),s.alpha),
        (b,s)=>postHigher(b,s,s.alpha),'rule fapp0 (@hom_postcomp_fapp1_func $A $B $F $W $X $Y $f $g $h) $alpha'),
    rule('categorical.precomp.post-component','tapp0_fapp0',[
        ['K','implicit',cat],['A','implicit',cat],['B','implicit',cat],['H','explicit',(b,s)=>fn(b,s.A,s.B)],
        ['F','implicit',(b,s)=>fn(b,s.K,s.A)],['G','implicit',(b,s)=>fn(b,s.K,s.A)],
        ['eta','explicit',(b,s)=>obj(b,hom(b,fc(b,s.K,s.A),s.F,s.G))],['x','explicit',(b,s)=>obj(b,s.K)]],
        (b,s)=>{const P={A:universe(b),B:universe(b),F:call(b,'id_func',[universe(b)],1),W:s.K,X:s.A,Y:s.B,f:s.H,g:s.F,h:s.G};
            return component(b,b.wildcard(s.K),b.wildcard(s.B),b.wildcard(postcomp(b,'hom_postcomp_fapp0',P,[s.F])),
                b.wildcard(postcomp(b,'hom_postcomp_fapp0',P,[s.G])),s.x,postHigher(b,P,s.eta));},
        (b,s)=>action(b,s.A,s.B,s.H,app(b,s.K,s.A,s.F,s.x),app(b,s.K,s.A,s.G,s.x),component(b,s.K,s.A,s.F,s.G,s.x,s.eta)),
        'rule @tapp0_fapp0 _ _ _ _ $x (@hom_postcomp_fapp1_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $K $A $B $H $F $G $epsilon)'),
    rule('categorical.precomp.transfor-composite-component','tapp0_fapp0',[
        ['A','implicit',cat],['B','implicit',cat],['F','implicit',(b,s)=>fn(b,s.A,s.B)],['G','implicit',(b,s)=>fn(b,s.A,s.B)],
        ['H','implicit',(b,s)=>fn(b,s.A,s.B)],['V','explicit',(b,s)=>obj(b,hom(b,fc(b,s.A,s.B),s.G,s.H))],
        ['U','explicit',(b,s)=>obj(b,hom(b,fc(b,s.A,s.B),s.F,s.G))],['x','explicit',(b,s)=>obj(b,s.A)]],
        (b,s)=>component(b,b.wildcard(s.A),b.wildcard(s.B),b.wildcard(s.F),b.wildcard(s.H),s.x,
            call(b,'comp_fapp0',[fc(b,s.A,s.B),s.F,s.G,s.H,s.V,s.U],4)),
        (b,s)=>call(b,'comp_fapp0',[s.B,app(b,s.A,s.B,s.F,s.x),app(b,s.A,s.B,s.G,s.x),app(b,s.A,s.B,s.H,s.x),
            component(b,s.A,s.B,s.G,s.H,s.x,s.V),component(b,s.A,s.B,s.F,s.G,s.x,s.U)],4),
        'rule @tapp0_fapp0 _ _ _ _ $Y (@comp_fapp0 (Functor_cat $A $B) $F $G $H $η $ϵ)'),
    rule('categorical.precomp.represented-hom','fapp1_func',representedParams,
        (b,s)=>action(b,b.wildcard(op(b,s.A)),b.wildcard(cc(b,s.B,cart(b))),call(b,'hom_int',[s.A,s.B,s.F],2),s.Y,s.X),
        (b,s)=>representedAction(b,s),'rule @fapp1_func _ _ (@hom_int $A $B $F) $Y $X'),
    rule('categorical.precomp.represented-arrow','fapp1_fapp0',[...representedParams,['p','explicit',(b,s)=>obj(b,representedDomain(b,s))]],
        (b,s)=>action(b,b.wildcard(op(b,s.A)),b.wildcard(cc(b,s.B,cart(b))),call(b,'hom_int',[s.A,s.B,s.F],2),s.Y,s.X,s.p),
        (b,s)=>representedAction(b,s,s.p),'rule @fapp1_fapp0 _ _ (@hom_int $A $B $F) $Y $X $p'),
    rule('categorical.precomp.represented-object','fapp0',[...representedParams,['p','explicit',(b,s)=>obj(b,representedDomain(b,s))]],
        (b,s)=>app(b,b.wildcard(representedDomain(b,s)),b.wildcard(representedCodomain(b,s)),representedAction(b,s),s.p),
        (b,s)=>representedAction(b,s,s.p),'rule @fapp0 _ _ (@hom_int_precomp_tele_func $A $B $F $Y $X) $p'),
    rule('categorical.precomp.represented-component','tapp0_fapp0',[...representedParams,['p','explicit',(b,s)=>obj(b,representedDomain(b,s))],['b','explicit',(b,s)=>obj(b,s.B)]],
        (b,s)=>component(b,s.B,cart(b),b.wildcard(represented(b,s.A,s.B,s.F,s.Y)),b.wildcard(represented(b,s.A,s.B,s.F,s.X)),s.b,
            call(b,'strict_transfor',[b.wildcard(s.B),b.wildcard(cart(b)),b.wildcard(represented(b,s.A,s.B,s.F,s.Y)),b.wildcard(represented(b,s.A,s.B,s.F,s.X)),representedAction(b,s,s.p)],4)),
        (b,s)=>precomp(b,'hom_precomp_along_func',{A:s.A,B:s.A,F:call(b,'id_func',[s.A],1),Z:app(b,s.B,s.A,s.F,s.b),W:s.X,X:s.Y,h:s.p}),
        'rule @tapp0_fapp0 $B Cat_cart _ _ $b (@strict_transfor _ _ _ _ (@hom_int_precomp_func $A $B $F $Y $X $f))'),
    rule('categorical.precomp.hom', 'fapp1_func', parameters, (b, s) => action(b, b.wildcard(from(b, s)), b.wildcard(to(b, s)), precomp(b, 'hom_precomp_along_func', s), s.g, s.k), (b, s) => higher(b, 'hom_precomp_along_fapp1_func', s), 'rule @fapp1_func _ _ (@hom_precomp_along_func $A $B $F $Z $W $X $h) $g $k'),
    rule('categorical.precomp.hom-object', 'fapp0', [...parameters, ['alpha', 'explicit', (b, s) => obj(b, domain(b, s))]], (b, s) => app(b, b.wildcard(domain(b, s)), b.wildcard(codomain(b, s)), higher(b, 'hom_precomp_along_fapp1_func', s), s.alpha), (b, s) => higher(b, 'hom_precomp_along_fapp1_fapp0', s, s.alpha), 'rule fapp0 (@hom_precomp_along_fapp1_func $A $B $F $Z $W $X $h $g $k) $alpha'),
    rule('categorical.precomp.hom-capped', 'fapp1_fapp0', [...parameters, ['alpha', 'explicit', (b, s) => obj(b, domain(b, s))]], (b, s) => action(b, b.wildcard(from(b, s)), b.wildcard(to(b, s)), precomp(b, 'hom_precomp_along_func', s), s.g, s.k, s.alpha), (b, s) => higher(b, 'hom_precomp_along_fapp1_fapp0', s, s.alpha), 'rule @fapp1_fapp0 _ _ (@hom_precomp_along_func $A $B $F $Z $W $X $h) $g $k $alpha'),
    rule('categorical.precomp.cat-object', 'fapp0', catParams.filter(p => p[0] !== 'H' && p[0] !== 'eta'), (b, s) => { const a = catScope(b, s), X = image(b, a, a.W); return app(b, b.wildcard(X), b.wildcard(s.Z), point(b, a, s.G), s.i); }, (b, s) => { const X = app(b, s.K, universe(b), s.E, s.X), Y = app(b, s.K, universe(b), s.E, s.Y); return app(b, Y, s.Z, s.G, app(b, X, Y, action(b, s.K, universe(b), s.E, s.X, s.Y, s.F), s.i)); }, 'rule @fapp0 _ _ (@hom_precomp_along_fapp0 $K Cat_cat $E $Z $X $Y $F $G) $i'),
    rule('categorical.precomp.cat-component', 'tapp0_fapp0', catParams, (b, s) => {
        const a = catScope(b, s), X = image(b, a, a.W);
        return component(b, b.wildcard(X), b.wildcard(s.Z), b.wildcard(point(b, a, s.G)), b.wildcard(point(b, a, s.H)), s.i, higher(b, 'hom_precomp_along_fapp1_fapp0', a, s.eta));
    }, (b, s) => {
        const X = app(b, s.K, universe(b), s.E, s.X), Y = app(b, s.K, universe(b), s.E, s.Y);
        const F = action(b, s.K, universe(b), s.E, s.X, s.Y, s.F), XY = fc(b, X, Y), YZ = fc(b, Y, s.Z);
        const fg = pair(b, XY, YZ, F, s.G), fh = pair(b, XY, YZ, F, s.H);
        const theta = pair(b, hom(b, XY, F, F), hom(b, YZ, s.G, s.H), identity(b, XY, F), s.eta);
        const composite = b.call(b.global(sym('comp_prod_fapp1_fapp0')), [universe(b), X, Y, s.Z, fg, fh, theta]
            .map((value, i) => ({ value, plicity: i === 6 ? 'explicit' : 'implicit' })));
        return component(b, X, s.Z, comp(b, X, Y, s.Z, s.G, F), comp(b, X, Y, s.Z, s.H, F), s.i, composite);
    }, 'rule @tapp0_fapp0 _ _ _ _ $i (@hom_precomp_along_fapp1_fapp0 $K Cat_cat $E $Z $X $Y $F $G $H $eta)')
].map((r, order) => ({ ...r, order }));
/** Source-prior identity-family comparison already consumed by PathOut. */
export function nativePrecompositionIdentityFamilyProofRule(): CoreLfTransferProofRule {
    const b = new Builder(), A = b.capture('A'), Z = b.capture('Z'), W = b.capture('W'), X = b.capture('X'), h = b.capture('h'), g = b.capture('g');
    const s = { A, B: A, F: call(b, 'id_func', [A], 1), Z, W, X, h };
    const variable = (name: string, type: Expr) => ({ name, role: 'matched' as const, type: b.template(type) });
    return { order: 0, id: 'pathout.foundation.precomposition-identity-family', sourceOwner: sym('hom_precomp_along_fapp0'),
        variables: [variable('A', b.global(sym('Cat'))), variable('Z', obj(b, A)), variable('W', obj(b, A)), variable('X', obj(b, A)),
            variable('h', call(b, 'τ', [call(b, 'Hom', [A, W, X])])), variable('g', call(b, 'τ', [call(b, 'Hom', [A, X, Z])]))],
        problem: { left: b.pattern(point(b, s, g)), right: b.pattern(call(b, 'comp_fapp0', [A, W, X, Z, g, h], 4)) },
        generatedConstraints: [{ left: b.template(A), right: b.template(A) }],
        provenance: source('unif_rule @hom_precomp_along_fapp0 $A $A (@id Cat_cat $A) $Z $W $X $h $g ≡ @comp_fapp0 $A _ _ $Z $g $h ↪ [ tt ≡ tt ]') };
}
const names = ['Cat', 'τ', 'Obj', 'Functor', 'Hom', 'Hom_cat', 'Functor_cat', 'Cat_cat','Cat_cart','Functor_cart_cat','Op_cat','hom_','hom_int','strict_transfor', 'fapp0', 'fapp1_func', 'fapp1_fapp0',
    'Transf','Transf_cat','tapp0_fapp0', 'id', 'id_func', 'comp_fapp0', 'comp_cat_fapp0', 'hom_precomp_along_func', 'hom_precomp_along_fapp0',
    'Product_pair', 'comp_prod_fapp1_fapp0','hom_postcomp_func','hom_postcomp_fapp0'];
const providers = [...CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE.entries, ...CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries, ...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries];
const spec = (id: string, ds: readonly CoreLfTransferDeclaration[], rs: readonly CoreLfTransferRuntimeRule[] = [], ps: readonly CoreLfTransferProofRule[] = []): CoreLfModuleSpec => createCoreLfModuleSpec({ revision: `NATIVE-PRECOMP-ACTION-${id}-1`, moduleId, fragmentId: `native-precomp-${id}`,
    authorityPath: 'emdash2/emdash3_2.lp', sourceSha256: sha, dependencies: [],
    externalSymbols: [...names, ...(ds.length ? [] : declarations.map(d => d.symbol.name))].map(name => ({ symbol: sym(name), availability: 'earlier-fragment' as const })),
    declarations: ds, inductives: [], runtimeRules: rs, proofRules: ps });
export const CORE_NATIVE_PRECOMPOSITION_DECLARATIONS = spec('declarations', declarations);
export const CORE_NATIVE_PRECOMPOSITION_RUNTIME = spec('runtime', [], rules);
export const CORE_NATIVE_PRECOMPOSITION_PROOF = spec('proof', [], [], [nativePrecompositionIdentityFamilyProofRule()]);
const policy = (m: CoreLfModuleSpec) => createCoreLfTransferPolicyOverlay(m, { revision: m.revision + '-policy', moduleRevision: m.revision,
    entries: [...m.declarations.map(d => ({ order: d.order, target: { kind: 'declaration' as const, symbol: d.symbol }, policy: 'opaque-signature' as const, evidence: 'Existing native higher precomposition owner' })),
        ...m.runtimeRules.map(r => ({ order: r.order, target: { kind: 'runtime-rule' as const, id: r.id }, policy: 'runtime-rewrite' as const, evidence: r.provenance.sourceFragment })),
        ...m.proofRules.map(r => ({ order: r.order, target: { kind: 'proof-rule' as const, id: r.id }, policy: 'proof-unification' as const, evidence: r.provenance.sourceFragment }))] });
export const CORE_NATIVE_PRECOMPOSITION_LINKAGE = createCoreLfTransferDeclarationLinkage(CORE_NATIVE_PRECOMPOSITION_DECLARATIONS, {
    revision: 'NATIVE-PRECOMP-ACTION-LINKAGE-1', moduleRevision: CORE_NATIVE_PRECOMPOSITION_DECLARATIONS.revision,
    entries: [...names.map((name, order) => { const link = providers.find(l => l.symbol.moduleId === moduleId && l.symbol.name === name); if (!link)
            throw new Error('Missing native precomposition dependency ' + name); return { ...link, order }; }),
        ...declarations.map((d, i) => ({ order: names.length + i, symbol: d.symbol, kind: 'free-declaration' as const,
            coreName: ['hom_int_precomp_tele_func','hom_int_precomp_func'].includes(d.symbol.name)
                ? `emdash_v3_2_pathout_foundation_${d.symbol.name}` : `emdash_v3_2_native_precomp_${d.symbol.name}`, backendName: d.symbol.name }))]
});
export interface NativePrecompositionPrerequisite {
    readonly compiled: {
        readonly environment: CoreLfDeclarationEnvironment;
    };
    readonly declarationContext: CoreLfMixedDeclarationContext;
    readonly runtimeFragment: CoreLfCompiledRuntimeFragment;
}
export function compileCoreNativePrecompositionProof(prerequisite: NativePrecompositionPrerequisite) {
    return compileCoreLfProofProgram(CORE_NATIVE_PRECOMPOSITION_PROOF, policy(CORE_NATIVE_PRECOMPOSITION_PROOF),
        prerequisite.declarationContext, {runtimeProgram:prerequisite.runtimeFragment.runtime,comparisonStepLimit:2048});
}
export function compileCoreNativePrecompositionAction(prerequisite: NativePrecompositionPrerequisite) {
    const compiled = compileCoreLfDeclarations(CORE_NATIVE_PRECOMPOSITION_DECLARATIONS, policy(CORE_NATIVE_PRECOMPOSITION_DECLARATIONS), CORE_NATIVE_PRECOMPOSITION_LINKAGE, { initialEnvironment: prerequisite.compiled.environment, runtimeProgram: prerequisite.runtimeFragment.runtime, comparisonStepLimit: 512 });
    const declarationContext = new CoreLfMixedDeclarationContext(prerequisite.declarationContext, [compiled]);
    const runtimeFragment = compileCoreLfRuntimeFragment(CORE_NATIVE_PRECOMPOSITION_RUNTIME, policy(CORE_NATIVE_PRECOMPOSITION_RUNTIME), declarationContext, { dependencies: [{ relation: 'earlier-fragment', fragment: prerequisite.runtimeFragment }], comparisonStepLimit: 512 });
    const proofProgram = compileCoreNativePrecompositionProof({compiled,declarationContext,runtimeFragment});
    return { compiled, declarationContext, runtimeFragment, proofProgram, composedRuntime: runtimeFragment.runtime };
}
