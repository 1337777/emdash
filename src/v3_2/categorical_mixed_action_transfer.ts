/** Native direct Homd projection declarations and their source-prior rules.
 * The old Pi/edge section owner is retired. The section here is the actual
 * iterated Hom in Functor_cat(K,Q); no combined context or curry is introduced.
 * Identity covariance and mate projections are shared with PathInd. General-FF
 * target/diagram action remains a separate transfer requirement.
 */
import { binderMode } from './kernel';
import { compileCoreNativePrecompositionAction } from './categorical_precomposition_action_transfer';
import {
    CoreLfTransferBuilderExpression as Expr, CoreLfTransferScopedBuilder as Builder,
    CoreLfTransferDeclaration, CoreLfTransferRuntimeRule, coreLfQualifiedSymbol,
    coreLfTransferAbsentBody, coreLfTransferExplicitBody, createCoreLfModuleSpec,
    createCoreLfTransferPolicyOverlay
} from './lf_transfer';
import { compileCoreLfDeclarations, createCoreLfTransferDeclarationLinkage } from './lf_transfer_compiler';
import { CoreLfMixedDeclarationContext } from './lf_transfer_mixed';
import { compileCoreLfRuntimeFragment } from './lf_transfer_runtime';
import { CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE } from './directed_continuation_transfer';
import { CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE } from './categorical_fibred_dependent_target_transfer';
import { CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE } from './categorical_structural_transfer';
import { CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE } from './categorical_fibred_product_transfer';
import { CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE } from './categorical_fibred_transfd_transfer';
import { CORE_CATEGORICAL_FIBRED_WEAKEN_REINDEX_TRANSFER_LINKAGE } from './categorical_fibred_weaken_reindex_transfer';
import { CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE } from './categorical_displayed_nd_higher_foundation_transfer';
import {
    CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256,
    CORE_CATEGORICAL_MIXED_MODE_TRANSFER_LINKAGE,
    compileCoreCategoricalMixedModeTransfer
} from './categorical_mixed_mode_transfer';

const moduleId = 'emdash.emdash3_2';
const sym = (name: string) => coreLfQualifiedSymbol(moduleId, name);
export const CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_REVISION = 'MIXED-ACTION-NATIVE-HOMD-2' as const;
const site = (sourceFragment: string) => ({ authorityPath: 'emdash2/emdash3_2.lp', sourceFragment });
const implicit = binderMode('implicit', 'functorial');
const explicit = binderMode('explicit', 'functorial');
type Scope = Readonly<Record<string, Expr>>;
type Body = (b: Builder, s: Scope) => Expr;
type Parameter = readonly [string, 'implicit' | 'explicit', Body];
const call = (b: Builder, name: string, args: readonly Expr[], implicitCount = 0): Expr =>
    b.call(b.global(sym(name)), args.map((value, index) => ({ value,
        plicity: index < implicitCount ? 'implicit' : 'explicit' })));
const cat: Body = b => b.global(sym('Cat'));
const cart = (b: Builder) => b.global(sym('Cat_cart'));
const Q = (b: Builder) => b.global(sym('Homd_coeff_cat'));
const op = (b: Builder, A: Expr) => call(b, 'Op_cat', [A]);
const fc = (b: Builder, A: Expr, B: Expr) => call(b, 'Functor_cat', [A, B]);
const cc = (b: Builder, A: Expr, B: Expr) => call(b, 'Functor_cart_cat', [A, B]);
const obj = (b: Builder, A: Expr) => call(b, 'τ', [call(b, 'Obj', [A])]);
const fn = (b: Builder, A: Expr, B: Expr) => call(b, 'τ', [call(b, 'Functor', [A, B])]);
const hom = (b: Builder, A: Expr, x: Expr, y: Expr) => call(b, 'Hom_cat', [A, x, y]);
const app = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr) => call(b, 'fapp0', [A, B, F, x], 2);
const fibre = (b: Builder, K: Expr, E: Expr, x: Expr) => app(b, K, cart(b), E, x);
const comp = (b: Builder, A: Expr, B: Expr, C: Expr, G: Expr, F: Expr) =>
    call(b, 'comp_cat_fapp0', [A, B, C, G, F], 3);
const id = (b: Builder, A: Expr) => call(b, 'id_func', [A], 1);
const ix = (b: Builder, K: Expr, x: Expr) => call(b, 'hom_', [K, K, id(b, K), x], 2);
const diagram = (b: Builder, K: Expr, E: Expr) => call(b, 'Homd_coeff_diagram', [K, E], 1);
const target = (b: Builder, K: Expr, D: Expr) => app(b,
    op(b, call(b, 'CoAt2_cat', [fc(b, K, Q(b))])), cc(b, K, cart(b)),
    call(b, 'Homd_target_index_func', [K]), diagram(b, K, D));
const section = (b: Builder, K: Expr, E: Expr, x: Expr) => call(b, 'Homd_target_section_cat', [K, E, x], 1);
const index = (b: Builder, I: Expr) => call(b, 'Homd_index_cat', [I]);
const transf = (b: Builder, A: Expr, B: Expr, F: Expr, G: Expr) => call(b, 'Transf_cat', [A, B, F, G], 2);
const component = (b: Builder, A: Expr, B: Expr, F: Expr, G: Expr, x: Expr, U: Expr) =>
    call(b, 'tapp0_fapp0', [A, B, F, G, x, U], 4);
const action = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr, y: Expr) =>
    b.call(b.global(sym('fapp1_func')), [A,B,F,x,y].map((value,i)=>({value,plicity:i===2?'explicit':'implicit'})));
const capped = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr, y: Expr, p: Expr) =>
    b.call(b.global(sym('fapp1_fapp0')), [A,B,F,x,y,p].map((value,i)=>({value,plicity:i===2||i===5?'explicit':'implicit'})));
const familyParams: readonly Parameter[] = [['K','implicit',cat], ['D','implicit',(b,s)=>fn(b,s.K,cart(b))],
    ['E','implicit',(b,s)=>fn(b,s.K,cart(b))], ['FF','explicit',(b,s)=>obj(b,transf(b,s.K,cart(b),s.D,s.E))]];
const xParam: Parameter = ['x','explicit',(b,s)=>obj(b,s.K)];
const uParam: Parameter = ['u','explicit',(b,s)=>obj(b,fibre(b,s.K,s.E,s.x))];
const yParam: Parameter = ['y','explicit',(b,s)=>obj(b,s.K)];
const relative = (b: Builder, name: string, s: Scope, extra: readonly Expr[] = []) =>
    call(b,name,[s.K,s.D,s.E,s.FF,...extra],3);
const telescope = (parameters: readonly Parameter[], body: Body, lambda = false) => {
    const b = new Builder();
    const go = (position: number, scope: Scope): Expr => {
        if (position === parameters.length) return body(b, scope);
        const [name,plicity,type] = parameters[position];
        const next = (value: Expr) => go(position+1,{...scope,[name]:value});
        return lambda ? b.lam(name,type(b,scope),next,plicity==='implicit'?implicit:explicit)
            : b.pi(name,type(b,scope),next,plicity==='implicit'?implicit:explicit);
    };
    return b.term(go(0,{}));
};
const declaration = (name: string, parameters: readonly Parameter[], type: Body, body?: Body,
    injective = false): CoreLfTransferDeclaration => ({
    order: 0, symbol: sym(name), type: telescope(parameters,type),
    body: body ? coreLfTransferExplicitBody(telescope(parameters,body,true)) : coreLfTransferAbsentBody(),
    modifiers: { visibility:'public', rigidity:injective?'injective':'ordinary', sourceOpacity:body?'transparent':'opaque' },
    provenance: site(`${injective?'injective ':''}symbol ${name}`)
});
const categoryPair: readonly Parameter[] = [['A','implicit',cat],['B','implicit',cat]];
const covarianceParams: readonly Parameter[] = [['K','implicit',cat],['E','explicit',(b,s)=>fn(b,s.K,cart(b))],
    ['x','implicit',(b,s)=>obj(b,s.K)],['y','implicit',(b,s)=>obj(b,s.K)],uParam];
const initialDeclarations = [
    declaration('Homd_index_cat',[['I','explicit',cat]],cat,(b,s)=>op(b,fc(b,s.I,op(b,cart(b))))),
    declaration('homd_index_presheaf',[['I','implicit',cat],['H','explicit',(b,s)=>obj(b,index(b,s.I))]],
        (b,s)=>fn(b,op(b,s.I),cart(b)),(b,s)=>call(b,'Op_func',[s.I,op(b,cart(b)),s.H],2)),
    declaration('Functor_cart_component_func',[...categoryPair,['F','explicit',(b,s)=>fn(b,s.A,s.B)],
        ['G','explicit',(b,s)=>fn(b,s.A,s.B)],['a','explicit',(b,s)=>obj(b,s.A)]],
        (b,s)=>fn(b,hom(b,cc(b,s.A,s.B),s.F,s.G),hom(b,s.B,app(b,s.A,s.B,s.F,s.a),app(b,s.A,s.B,s.G,s.a))),
        (b,s)=>comp(b,hom(b,cc(b,s.A,s.B),s.F,s.G),transf(b,s.A,s.B,s.F,s.G),
            hom(b,s.B,app(b,s.A,s.B,s.F,s.a),app(b,s.A,s.B,s.G,s.a)),
            call(b,'tapp0_func',[s.A,s.B,s.F,s.G,s.a],4),
            action(b,cc(b,s.A,s.B),fc(b,s.A,s.B),call(b,'Functor_cart_include',[s.A,s.B]),s.F,s.G))),
    declaration('fib_cov_tapp0_func',covarianceParams,(b,s)=>fn(b,hom(b,s.K,s.x,s.y),fibre(b,s.K,s.E,s.y)),
        (b,s)=>{
            const A=fibre(b,s.K,s.E,s.x),B=fibre(b,s.K,s.E,s.y);
            return comp(b,hom(b,s.K,s.x,s.y),cc(b,A,B),B,
                comp(b,cc(b,A,B),fc(b,A,B),B,call(b,'fapp0_func',[A,B,s.u],2),call(b,'Functor_cart_include',[A,B])),
                action(b,s.K,cart(b),s.E,s.x,s.y));
        }),
    declaration('homd_',[...familyParams,xParam,uParam,yParam,['v','explicit',(b,s)=>obj(b,fibre(b,s.K,s.D,s.y))]],
        (b,s)=>fn(b,op(b,hom(b,s.K,s.x,s.y)),cart(b)),
        (b,s)=>b.call(b.global(sym('hom_con')),[
            {plicity:'implicit',value:fibre(b,s.K,s.E,s.y)},
            {plicity:'explicit',value:app(b,fibre(b,s.K,s.D,s.y),fibre(b,s.K,s.E,s.y),
                component(b,s.K,cart(b),s.D,s.E,s.y,s.FF),s.v)},
            {plicity:'implicit',value:hom(b,s.K,s.x,s.y)},
            {plicity:'explicit',value:b.call(b.global(sym('fib_cov_tapp0_func')),[
                {plicity:'implicit',value:s.K},{plicity:'explicit',value:s.E},{plicity:'implicit',value:s.x},
                {plicity:'implicit',value:s.y},{plicity:'explicit',value:s.u}])}]),true),
    declaration('Functor_catd_fapp0_func',[['K','implicit',cat],['A','explicit',(b,s)=>fn(b,op(b,s.K),cart(b))]],
        (b,s)=>fn(b,call(b,'Catd_cat',[s.K]),call(b,'Catd_cat',[s.K])),undefined,true),
    declaration('Homd_target_section_cat',[['K','implicit',cat],['E','explicit',(b,s)=>fn(b,s.K,cart(b))],xParam],cat,
        (b,s)=>hom(b,hom(b,b.global(sym('Cat_cat')),s.K,Q(b)),diagram(b,s.K,s.E),diagram(b,s.K,ix(b,s.K,s.x))))
].map((d,order)=>({...d,order}));
// Source-prior covariance is shared by Homd and the later PathInd consumer.
const identityParams: readonly Parameter[] = [
    ['K','implicit',cat], ['E','explicit',(b,s)=>fn(b,s.K,cart(b))]
];
const covarianceTarget = (b:Builder,K:Expr,E:Expr) => call(b,'FibCov_target_catd',[K,E],1);
const covariance = (b:Builder,K:Expr,E:Expr,x:Expr,u:Expr) => call(b,'fib_cov_transf',[K,E,x,u],1);
const mate = (b:Builder,K:Expr,E:Expr,D:Expr,U:Expr) => call(b,'Homd_coeff_mate',[K,E,D,U],3);
const componentFunctor = (b:Builder,K:Expr,E:Expr,D:Expr,y:Expr) => call(b,'Functor_cart_component_func',[K,cart(b),E,D,y],2);
const identityDeclarations = [
    declaration('FibCov_target_catd',identityParams,(b,s)=>fn(b,s.K,cart(b)),
        (b,s)=>b.call(b.global(sym('hom_con')),[cc(b,s.K,cart(b)),s.E,op(b,s.K),call(b,'hom_int',[s.K,s.K,id(b,s.K)],2)]
            .map((value,i)=>({value,plicity:i===0||i===2?'implicit':'explicit'})))),
    declaration('fib_cov_int',identityParams,
        (b,s)=>obj(b,transf(b,s.K,cart(b),s.E,covarianceTarget(b,s.K,s.E)))),
    declaration('fib_cov_src_func',[...identityParams,xParam],
        (b,s)=>fn(b,fibre(b,s.K,s.E,s.x),fibre(b,s.K,covarianceTarget(b,s.K,s.E),s.x))),
    declaration('fib_cov_transf',[...identityParams,xParam,uParam],
        (b,s)=>obj(b,fibre(b,s.K,covarianceTarget(b,s.K,s.E),s.x)),undefined,true),
    declaration('Homd_coeff_conjoint',[...categoryPair,['F','explicit',(b,s)=>fn(b,s.B,s.A)]],
        (b,s)=>obj(b,hom(b,Q(b),s.A,s.B)),undefined,true),
    declaration('Homd_coeff_rep_func',[['A','explicit',cat],['B','explicit',cat]],
        (b,s)=>fn(b,cc(b,s.A,s.B),hom(b,Q(b),s.A,s.B)),
        (b,s)=>b.call(b.global(sym('hom_postcomp_func')),[cart(b),cart(b),id(b,cart(b)),s.A,s.B,index(b,s.B),
            call(b,'Homd_coeff_conjoint',[s.B,s.B,id(b,s.B)],2)]
                .map((value,i)=>({value,plicity:[2,3,6].includes(i)?'explicit':'implicit'})))),
    declaration('Homd_coeff_rep',[...categoryPair,['F','explicit',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>obj(b,hom(b,Q(b),s.A,s.B)),undefined,true),
    declaration('Homd_coeff_mate',[
        ['K','implicit',cat],['E','implicit',(b,s)=>fn(b,s.K,cart(b))],['D','implicit',(b,s)=>fn(b,s.K,cart(b))],
        ['U','explicit',(b,s)=>obj(b,hom(b,cc(b,s.K,cart(b)),s.E,s.D))]],
        (b,s)=>obj(b,transf(b,s.K,Q(b),diagram(b,s.K,s.D),diagram(b,s.K,s.E)))),
    declaration('Homd_coeff_mate_func',[
        ['K','implicit',cat],['E','explicit',(b,s)=>fn(b,s.K,cart(b))],['D','explicit',(b,s)=>fn(b,s.K,cart(b))]],
        (b,s)=>fn(b,op(b,hom(b,cc(b,s.K,cart(b)),s.E,s.D)),
            transf(b,s.K,Q(b),diagram(b,s.K,s.D),diagram(b,s.K,s.E))),undefined,true),
    declaration('homd_id_src_sec',[...identityParams,xParam,uParam],
        (b,s)=>obj(b,section(b,s.K,s.E,s.x)),
        (b,s)=>mate(b,s.K,ix(b,s.K,s.x),s.E,covariance(b,s.K,s.E,s.x,s.u))),
    declaration('homd_id_src_func',[...identityParams,xParam],
        (b,s)=>fn(b,op(b,fibre(b,s.K,s.E,s.x)),section(b,s.K,s.E,s.x)),
        (b,s)=>{const H=hom(b,cc(b,s.K,cart(b)),ix(b,s.K,s.x),s.E);
            return comp(b,op(b,fibre(b,s.K,s.E,s.x)),op(b,H),section(b,s.K,s.E,s.x),
                call(b,'Homd_coeff_mate_func',[s.K,ix(b,s.K,s.x),s.E],1),
                call(b,'Op_func',[fibre(b,s.K,s.E,s.x),H,call(b,'fib_cov_src_func',[s.K,s.E,s.x],1)],2));}),
    declaration('homd_id_tgt_func',[...identityParams,xParam,uParam,yParam],
        (b,s)=>fn(b,fibre(b,s.K,s.E,s.y),index(b,hom(b,s.K,s.x,s.y))),
        (b,s)=>component(b,s.K,Q(b),diagram(b,s.K,s.E),diagram(b,s.K,ix(b,s.K,s.x)),s.y,
            call(b,'homd_id_src_sec',[s.K,s.E,s.x,s.u],1))),
    declaration('homd_id_',[...identityParams,xParam,uParam,yParam,['v','explicit',(b,s)=>obj(b,fibre(b,s.K,s.E,s.y))]],
        (b,s)=>fn(b,op(b,hom(b,s.K,s.x,s.y)),cart(b)),
        (b,s)=>call(b,'homd_index_presheaf',[hom(b,s.K,s.x,s.y),
            app(b,fibre(b,s.K,s.E,s.y),index(b,hom(b,s.K,s.x,s.y)),
                call(b,'homd_id_tgt_func',[s.K,s.E,s.x,s.u,s.y],1),s.v)],1))
].map((d,order)=>({...d,order,modifiers:d.symbol.name==='fib_cov_int'
    ? {...d.modifiers,rigidity:'constant' as const} : d.modifiers}));
const finalDeclarations = [
    declaration('homd_src_sec',[...familyParams,xParam,uParam],(b,s)=>obj(b,section(b,s.K,s.D,s.x)),
        (b,s)=>app(b,fibre(b,s.K,s.E,s.x),fibre(b,s.K,target(b,s.K,s.D),s.x),
            app(b,hom(b,cc(b,s.K,cart(b)),s.E,target(b,s.K,s.D)),
                hom(b,cart(b),fibre(b,s.K,s.E,s.x),fibre(b,s.K,target(b,s.K,s.D),s.x)),
                call(b,'Functor_cart_component_func',[s.K,cart(b),s.E,target(b,s.K,s.D),s.x],2),
                relative(b,'homd_rel_cart_int',s)),s.u)),
    declaration('homd_src_func',[...familyParams,xParam],(b,s)=>fn(b,fibre(b,s.K,s.E,s.x),op(b,section(b,s.K,s.D,s.x))),
        (b,s)=>component(b,s.K,cart(b),s.E,target(b,s.K,s.D),s.x,relative(b,'homd_int',s))),
    declaration('homd_tgt_func',[...familyParams,xParam,uParam,yParam],
        (b,s)=>fn(b,fibre(b,s.K,s.D,s.y),index(b,hom(b,s.K,s.x,s.y))),
        (b,s)=>component(b,s.K,Q(b),diagram(b,s.K,s.D),diagram(b,s.K,ix(b,s.K,s.x)),s.y,
            relative(b,'homd_src_sec',s,[s.x,s.u])))
].map((d,order)=>({...d,order}));
const declarations=[...initialDeclarations,...identityDeclarations,...finalDeclarations].map((d,order)=>({...d,order}));
const externalNames=['Cat','τ','Obj','Functor','Hom_cat','Cat_cat','Cat_cart','Functor_cat','Functor_cart_cat',
    'Catd_cat','Transf_cat','Op_cat','CoAt2_cat','fapp0','fapp1_func','fapp1_fapp0','fapp0_func','tapp0_func','tapp0_fapp0','strict_transfor',
    'hom_postcomp_func','hom_postcomp_fapp0','hom_precomp_along_func','hom_precomp_along_fapp0','comp_fapp0','comp_cat_fapp0','id_func','hom_con','hom_','Functor_cart_include','Homd_coeff_cat','Homd_coeff_include',
    'Homd_coeff_diagram','Homd_representable_func','Homd_target_index_func','Homd_target_catd',
    'homd_rel_cart_int','homd_id_int','homd_int','Op_func','Functor_catd','Functor_catd_func',
    // Preserve predecessor links used by downstream mixed profiles.
    'Catd','Functord','Const_catd','Pi_cat','Obj_func','Terminal_cat','id',
    'Op_catd','Op_catd_func','hom_int','HomPresheaf_catd_func'];
const allLinks=[...CORE_CATEGORICAL_MIXED_MODE_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_WEAKEN_REINDEX_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries,...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries];
const dependencyLink=(name:string,order:number)=>{
    const found=allLinks.find(l=>l.symbol.name===name&&l.symbol.moduleId===moduleId);
    if(!found) throw new Error(`Missing native Homd ladder dependency ${name}`);
    return {...found,order};
};
const relocatedCovarianceNames = new Set(['FibCov_target_catd','fib_cov_int','fib_cov_src_func','fib_cov_transf']);
const localCoreName=(name:string)=>relocatedCovarianceNames.has(name)
    ? `emdash_v3_2_pathind_fixed_source_${name}` : `emdash_v3_2_mixed_nest_action_0b_${name}`;
const makeModule=(fragmentId:string,ds:readonly CoreLfTransferDeclaration[],extra:readonly string[]=[],rules:readonly CoreLfTransferRuntimeRule[]=[])=>
    createCoreLfModuleSpec({revision:CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_REVISION,moduleId,fragmentId,
        authorityPath:'emdash2/emdash3_2.lp',sourceSha256:CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256,dependencies:[],
        externalSymbols:[...externalNames,...extra].map(name=>({symbol:sym(name),availability:'earlier-fragment' as const})),
        declarations:ds,inductives:[],runtimeRules:rules,proofRules:[]});
export const CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE=makeModule('native-homd-ladder',declarations);
const makePolicy=(module:ReturnType<typeof makeModule>)=>createCoreLfTransferPolicyOverlay(module,{
    revision:module.fragmentId+'-policy',moduleRevision:module.revision,entries:module.declarations.map(d=>({
        order:d.order,target:{kind:'declaration' as const,symbol:d.symbol},
        policy:d.body.kind==='explicit-term'?'checked-transparent-definition' as const:'opaque-signature' as const,
        evidence:'Current native direct Homd ladder owner'}))});
export const CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_POLICY=makePolicy(CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE);
const makeLinkage=(module:ReturnType<typeof makeModule>)=>createCoreLfTransferDeclarationLinkage(module,{
    revision:module.fragmentId+'-linkage',moduleRevision:module.revision,
    entries:[...module.externalSymbols.map((e,order)=>externalNames.includes(e.symbol.name)?dependencyLink(e.symbol.name,order):
        ({order,symbol:e.symbol,kind:'free-declaration' as const,coreName:localCoreName(e.symbol.name),backendName:e.symbol.name})),
        ...module.declarations.map((d,index)=>({order:module.externalSymbols.length+index,symbol:d.symbol,
            kind:'free-declaration' as const,coreName:localCoreName(d.symbol.name),backendName:d.symbol.name}))]});
export const CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE=makeLinkage(CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE);

type Variable = readonly [string,Body];
const rule=(name:string,owner:string,variables:readonly Variable[],left:Body,right:Body):CoreLfTransferRuntimeRule=>{
    const b=new Builder(),scope=Object.fromEntries(variables.map(([n])=>[n,b.capture(n)]));
    return {order:0,id:'categorical.mixed-action.'+name,groupId:'categorical.mixed-action.'+name,clauseOrder:0,
        sourceOwner:sym(owner),variables:variables.map(([name,type])=>({name,type:b.template(type(b,scope))})),
        left:b.pattern(left(b,scope)),right:b.template(right(b,scope)),provenance:site(`native ${name} projection`)};
};
const runtimeRules=[
    rule('functor-hom-object','fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],
        ['x',(b,s)=>obj(b,s.A)],['y',(b,s)=>obj(b,s.A)],['f',(b,s)=>obj(b,hom(b,s.A,s.x,s.y))]],
        (b,s)=>app(b,b.wildcard(hom(b,s.A,s.x,s.y)),
            b.wildcard(hom(b,s.B,app(b,s.A,s.B,s.F,s.x),app(b,s.A,s.B,s.F,s.y))),
            action(b,s.A,s.B,s.F,s.x,s.y),s.f),
        (b,s)=>b.call(b.global(sym('fapp1_fapp0')),[s.A,s.B,s.F,s.x,s.y,s.f]
            .map((value,i)=>({value,plicity:i===2||i===5?'explicit':'implicit'})))),
    rule('transfor-component-object','fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],
        ['G',(b,s)=>fn(b,s.A,s.B)],['x',(b,s)=>obj(b,s.A)],['U',(b,s)=>obj(b,transf(b,s.A,s.B,s.F,s.G))]],
        (b,s)=>app(b,b.wildcard(transf(b,s.A,s.B,s.F,s.G)),
            b.wildcard(hom(b,s.B,app(b,s.A,s.B,s.F,s.x),app(b,s.A,s.B,s.G,s.x))),
            call(b,'tapp0_func',[s.A,s.B,s.F,s.G,s.x],4),s.U),
        (b,s)=>component(b,s.A,s.B,s.F,s.G,s.x,s.U)),
    rule('coefficient-objects','Obj',[],b=>call(b,'Obj',[Q(b)]),b=>call(b,'Obj',[b.global(sym('Cat_cat'))])),
    rule('coefficient-hom','Hom_cat',[['A',cat],['B',cat]],(b,s)=>hom(b,Q(b),s.A,s.B),(b,s)=>cc(b,s.A,index(b,s.B))),
    rule('coefficient-include-object','fapp0',[['A',cat]],(b,s)=>app(b,cart(b),Q(b),b.global(sym('Homd_coeff_include')),s.A),(b,s)=>s.A),
    rule('represented-hom-object-projection','fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.B,s.A)],
        ['W',(b,s)=>obj(b,s.A)],['y',(b,s)=>obj(b,s.B)]],
        (b,s)=>app(b,s.B,cart(b),call(b,'hom_',[s.A,s.B,s.F,s.W],2),s.y),
        (b,s)=>hom(b,s.A,s.W,app(b,s.B,s.A,s.F,s.y))),
    rule('represented-package-object','fapp0',[['K',cat],['x',(b,s)=>obj(b,s.K)]],
        (b,s)=>app(b,b.wildcard(call(b,'CoAt2_cat',[s.K])),b.wildcard(fc(b,s.K,Q(b))),call(b,'Homd_representable_func',[s.K]),s.x),
        (b,s)=>diagram(b,s.K,ix(b,s.K,s.x))),
    rule('opposite-functor-object-projection','fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],['x',(b,s)=>obj(b,s.A)]],
        (b,s)=>app(b,b.wildcard(op(b,s.A)),b.wildcard(op(b,s.B)),call(b,'Op_func',[s.A,s.B,s.F],2),s.x),
        (b,s)=>app(b,s.A,s.B,s.F,s.x)),
    rule('displayed-opposite-functor-object-projection','fapp0',[['K',cat],['E',(b,s)=>fn(b,s.K,cart(b))]],
        (b,s)=>app(b,b.wildcard(call(b,'CoAt2_cat',[cc(b,s.K,cart(b))])),
            b.wildcard(cc(b,call(b,'CoAt2_cat',[s.K]),cart(b))),call(b,'Op_catd_func',[s.K]),s.E),
        (b,s)=>call(b,'Op_catd',[s.K,s.E],1)),
    rule('cartesian-include-arrow','fapp1_fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],
        ['G',(b,s)=>fn(b,s.A,s.B)],['U',(b,s)=>obj(b,hom(b,cc(b,s.A,s.B),s.F,s.G))]],
        (b,s)=>b.call(b.global(sym('fapp1_fapp0')), [
            b.wildcard(cc(b,s.A,s.B)), b.wildcard(fc(b,s.A,s.B)),
            call(b,'Functor_cart_include',[s.A,s.B]), s.F, s.G, s.U
        ].map((value,i)=>({value,plicity:i===2||i===5?'explicit':'implicit'}))),
        (b,s)=>call(b,'strict_transfor',[s.A,s.B,s.F,s.G,s.U],4)),
    // Native whole/capped opposite action and capped contravariant Hom action.
    // These retain the ordinary semantic owners used after family pullback.
    rule('opposite-functor-hom','fapp1_func',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],
        ['x',(b,s)=>obj(b,s.A)],['y',(b,s)=>obj(b,s.A)]],
        (b,s)=>action(b,b.wildcard(op(b,s.A)),b.wildcard(op(b,s.B)),call(b,'Op_func',[s.A,s.B,s.F],2),s.x,s.y),
        (b,s)=>action(b,s.A,s.B,s.F,s.y,s.x)),
    rule('opposite-functor-arrow','fapp1_fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)],
        ['x',(b,s)=>obj(b,s.A)],['y',(b,s)=>obj(b,s.A)],['p',(b,s)=>obj(b,hom(b,s.A,s.y,s.x))]],
        (b,s)=>capped(b,b.wildcard(op(b,s.A)),b.wildcard(op(b,s.B)),call(b,'Op_func',[s.A,s.B,s.F],2),s.x,s.y,s.p),
        (b,s)=>capped(b,s.A,s.B,s.F,s.y,s.x,s.p)),
    rule('contravariant-hom-arrow','fapp1_fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.B,s.A)],
        ['W',(b,s)=>obj(b,s.A)],['x',(b,s)=>obj(b,s.B)],['y',(b,s)=>obj(b,s.B)],
        ['p',(b,s)=>obj(b,hom(b,s.B,s.y,s.x))]],
        (b,s)=>capped(b,b.wildcard(op(b,s.B)),cart(b),
            b.call(b.global(sym('hom_con')),[s.A,s.W,s.B,s.F].map((value,i)=>({value,plicity:i===0||i===2?'implicit':'explicit'}))),s.x,s.y,s.p),
        (b,s)=>b.call(b.global(sym('hom_precomp_along_func')),
            [s.B,s.A,s.F,s.W,s.y,s.x,s.p].map((value,i)=>({value,plicity:i===2||i===3||i===6?'explicit':'implicit'})))),
    rule('mixed-functor-first-projection','fapp0',[['K',cat],['A',(b,s)=>fn(b,op(b,s.K),cart(b))]],
        (b,s)=>app(b,b.wildcard(op(b,cc(b,op(b,s.K),cart(b)))),
            b.wildcard(fc(b,call(b,'Catd_cat',[s.K]),call(b,'Catd_cat',[s.K]))),call(b,'Functor_catd_func',[s.K]),s.A),
        (b,s)=>call(b,'Functor_catd_fapp0_func',[s.K,s.A],1)),
    rule('mixed-functor-second-projection','fapp0',[['K',cat],['A',(b,s)=>fn(b,op(b,s.K),cart(b))],['B',(b,s)=>fn(b,s.K,cart(b))]],
        (b,s)=>app(b,call(b,'Catd_cat',[s.K]),call(b,'Catd_cat',[s.K]),call(b,'Functor_catd_fapp0_func',[s.K,s.A],1),s.B),
        (b,s)=>call(b,'Functor_catd',[s.K,s.A,s.B],1))
].map((r,order)=>({...r,order}));
const covarianceVariables: readonly Variable[] = [['K',cat],['E',(b,s)=>fn(b,s.K,cart(b))]];
const xVariable: Variable = ['x',(b,s)=>obj(b,s.K)];
const uVariable: Variable = ['u',(b,s)=>obj(b,fibre(b,s.K,s.E,s.x))];
const mateVariables: readonly Variable[] = [...covarianceVariables,['D',(b,s)=>fn(b,s.K,cart(b))],
    ['U',(b,s)=>obj(b,hom(b,cc(b,s.K,cart(b)),s.E,s.D))]];
const identityRuntimeRules = [
    rule('coefficient-include-hom','fapp1_func',[['A',cat],['B',cat]],
        (b,s)=>action(b,cart(b),Q(b),b.global(sym('Homd_coeff_include')),s.A,s.B),
        (b,s)=>call(b,'Homd_coeff_rep_func',[s.A,s.B])),
    rule('coefficient-include-arrow','fapp1_fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>capped(b,cart(b),Q(b),b.global(sym('Homd_coeff_include')),s.A,s.B,s.F),
        (b,s)=>call(b,'Homd_coeff_rep',[s.A,s.B,s.F],2)),
    rule('represented-coefficient-object','hom_postcomp_fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>b.call(b.global(sym('hom_postcomp_fapp0')),[cart(b),cart(b),id(b,cart(b)),s.A,s.B,index(b,s.B),
            call(b,'Homd_coeff_conjoint',[s.B,s.B,id(b,s.B)],2),s.F]
                .map((value,i)=>({value,plicity:[2,3,6,7].includes(i)?'explicit':'implicit'}))),
        (b,s)=>call(b,'Homd_coeff_rep',[s.A,s.B,s.F],2)),
    rule('coefficient-right-represented-composition','comp_fapp0',[
        ['A',cat],['B',cat],['C',cat],['P',(b,s)=>obj(b,hom(b,Q(b),s.B,s.C))],['F',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>call(b,'comp_fapp0',[Q(b),s.A,s.B,s.C,s.P,call(b,'Homd_coeff_rep',[s.A,s.B,s.F],2)],4),
        (b,s)=>comp(b,s.A,s.B,index(b,s.C),s.P,s.F)),
    rule('diagram-precomposition-mate','hom_precomp_along_fapp0',[
        ...mateVariables,['X',(b,s)=>fn(b,s.K,Q(b))],
        ['FF',(b,s)=>obj(b,transf(b,s.K,Q(b),s.X,diagram(b,s.K,s.D)))]],
        (b,s)=>b.call(b.global(sym('hom_precomp_along_fapp0')),
            [fc(b,s.K,Q(b)),fc(b,s.K,Q(b)),id(b,fc(b,s.K,Q(b))),b.wildcard(diagram(b,s.K,s.E)),s.X,b.wildcard(diagram(b,s.K,s.D)),
                s.FF,mate(b,s.K,s.E,s.D,s.U)].map((value,i)=>({value,plicity:[2,3,6,7].includes(i)?'explicit':'implicit'}))),
        (b,s)=>call(b,'comp_fapp0',[fc(b,s.K,Q(b)),s.X,diagram(b,s.K,s.D),diagram(b,s.K,s.E),
            mate(b,s.K,s.E,s.D,s.U),s.FF],4)),
    rule('cartesian-prewhiskering-component','tapp0_fapp0',[
        ['A',cat],['B',cat],['C',cat],['H',(b,s)=>fn(b,s.A,s.B)],
        ['F',(b,s)=>fn(b,s.B,s.C)],['G',(b,s)=>fn(b,s.B,s.C)],
        ['U',(b,s)=>obj(b,hom(b,cc(b,s.B,s.C),s.F,s.G))],['a',(b,s)=>obj(b,s.A)]],
        (b,s)=>component(b,b.wildcard(s.A),b.wildcard(s.C),
            b.wildcard(comp(b,s.A,s.B,s.C,s.F,s.H)),b.wildcard(comp(b,s.A,s.B,s.C,s.G,s.H)),s.a,
            call(b,'strict_transfor',[b.wildcard(s.A),b.wildcard(s.C),b.wildcard(comp(b,s.A,s.B,s.C,s.F,s.H)),
                b.wildcard(comp(b,s.A,s.B,s.C,s.G,s.H)),
                b.call(b.global(sym('hom_precomp_along_fapp1_fapp0')),
                    [cart(b),cart(b),id(b,cart(b)),s.C,s.A,s.B,s.H,s.F,s.G,s.U]
                        .map((value,i)=>({value,plicity:[2,3,6,9].includes(i)?'explicit':'implicit'})))],4)),
        (b,s)=>app(b,hom(b,cc(b,s.B,s.C),s.F,s.G),
            hom(b,s.C,app(b,s.B,s.C,s.F,app(b,s.A,s.B,s.H,s.a)),app(b,s.B,s.C,s.G,app(b,s.A,s.B,s.H,s.a))),
            call(b,'Functor_cart_component_func',[s.B,s.C,s.F,s.G,app(b,s.A,s.B,s.H,s.a)],2),s.U)),
    rule('dimension-two-precomposition','hom_precomp_along_func',[
        ['C',cat],['Z',(b,s)=>obj(b,s.C)],['X',(b,s)=>obj(b,s.C)],['Y',(b,s)=>obj(b,s.C)],
        ['p',(b,s)=>obj(b,hom(b,s.C,s.X,s.Y))]],
        (b,s)=>b.call(b.global(sym('hom_precomp_along_func')),
            [call(b,'CoAt2_cat',[s.C]),call(b,'CoAt2_cat',[s.C]),id(b,call(b,'CoAt2_cat',[s.C])),s.Z,s.X,s.Y,s.p]
                .map((value,i)=>({value,plicity:[2,3,6].includes(i)?'explicit':'implicit'}))),
        (b,s)=>call(b,'Op_func',[hom(b,s.C,s.Y,s.Z),hom(b,s.C,s.X,s.Z),
            b.call(b.global(sym('hom_precomp_along_func')),[s.C,s.C,id(b,s.C),s.Z,s.X,s.Y,s.p]
                .map((value,i)=>({value,plicity:[2,3,6].includes(i)?'explicit':'implicit'})))],2)),
    rule('covariance-root','tapp0_fapp0',[...covarianceVariables,xVariable],
        (b,s)=>component(b,s.K,cart(b),b.wildcard(s.E),b.wildcard(covarianceTarget(b,s.K,s.E)),s.x,
            call(b,'fib_cov_int',[s.K,s.E],1)),
        (b,s)=>call(b,'fib_cov_src_func',[s.K,s.E,s.x],1)),
    rule('covariance-object','fapp0',[...covarianceVariables,xVariable,uVariable],
        (b,s)=>app(b,b.wildcard(fibre(b,s.K,s.E,s.x)),b.wildcard(fibre(b,s.K,covarianceTarget(b,s.K,s.E),s.x)),
            call(b,'fib_cov_src_func',[s.K,s.E,s.x],1),s.u),
        (b,s)=>covariance(b,s.K,s.E,s.x,s.u)),
    rule('covariance-component','tapp0_fapp0',[...covarianceVariables,xVariable,uVariable,['y',(b,s)=>obj(b,s.K)]],
        (b,s)=>component(b,s.K,cart(b),b.wildcard(ix(b,s.K,s.x)),b.wildcard(s.E),s.y,
            call(b,'strict_transfor',[b.wildcard(s.K),b.wildcard(cart(b)),b.wildcard(ix(b,s.K,s.x)),b.wildcard(s.E),
                covariance(b,s.K,s.E,s.x,s.u)],4)),
        (b,s)=>b.call(b.global(sym('fib_cov_tapp0_func')),[s.K,s.E,s.x,s.y,s.u]
            .map((value,i)=>({value,plicity:i===0||i===2||i===3?'implicit':'explicit'})))),
    rule('opposite-functor-involution','Op_func',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.A,s.B)]],
        (b,s)=>call(b,'Op_func',[b.wildcard(op(b,s.A)),b.wildcard(op(b,s.B)),call(b,'Op_func',[s.A,s.B,s.F],2)],2),
        (b,s)=>s.F),
    rule('identity-homd-root','tapp0_fapp0',[...covarianceVariables,xVariable],
        (b,s)=>component(b,b.wildcard(s.K),b.wildcard(cart(b)),b.wildcard(s.E),b.wildcard(target(b,s.K,s.E)),s.x,
            call(b,'strict_transfor',[b.wildcard(s.K),b.wildcard(cart(b)),b.wildcard(s.E),b.wildcard(target(b,s.K,s.E)),
                call(b,'homd_id_int',[s.K,s.E],1)],4)),
        (b,s)=>call(b,'Op_func',[op(b,fibre(b,s.K,s.E,s.x)),section(b,s.K,s.E,s.x),call(b,'homd_id_src_func',[s.K,s.E,s.x],1)],2)),
    rule('mate-object','fapp0',mateVariables,
        (b,s)=>app(b,b.wildcard(op(b,hom(b,cc(b,s.K,cart(b)),s.E,s.D))),
            b.wildcard(transf(b,s.K,Q(b),diagram(b,s.K,s.D),diagram(b,s.K,s.E))),call(b,'Homd_coeff_mate_func',[s.K,s.E,s.D],1),s.U),
        (b,s)=>mate(b,s.K,s.E,s.D,s.U)),
    rule('mate-component','tapp0_fapp0',[...mateVariables,['y',(b,s)=>obj(b,s.K)]],
        (b,s)=>component(b,b.wildcard(s.K),b.wildcard(Q(b)),b.wildcard(diagram(b,s.K,s.D)),b.wildcard(diagram(b,s.K,s.E)),s.y,
            mate(b,s.K,s.E,s.D,s.U)),
        (b,s)=>call(b,'Homd_coeff_conjoint',[fibre(b,s.K,s.D,s.y),fibre(b,s.K,s.E,s.y),
            app(b,hom(b,cc(b,s.K,cart(b)),s.E,s.D),cc(b,fibre(b,s.K,s.E,s.y),fibre(b,s.K,s.D,s.y)),
                componentFunctor(b,s.K,s.E,s.D,s.y),s.U)],2)),
    rule('conjoint-object','fapp0',[['A',cat],['B',cat],['F',(b,s)=>fn(b,s.B,s.A)],['a',(b,s)=>obj(b,s.A)]],
        (b,s)=>app(b,b.wildcard(s.A),b.wildcard(index(b,s.B)),call(b,'Homd_coeff_conjoint',[s.A,s.B,s.F],2),s.a),
        (b,s)=>call(b,'Op_func',[op(b,s.B),cart(b),b.call(b.global(sym('hom_con')),[s.A,s.a,s.B,s.F]
            .map((value,i)=>({value,plicity:i===0||i===2?'implicit':'explicit'})))],2))
].map((r,order)=>({...r,order}));
export const CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE=makeModule('native-homd-ladder-projections',[],initialDeclarations.map(d=>d.symbol.name),runtimeRules);
export const CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY=createCoreLfTransferPolicyOverlay(CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE,{
    revision:'native-homd-ladder-runtime-policy',moduleRevision:CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE.revision,
    entries:runtimeRules.map(r=>({order:r.order,target:{kind:'runtime-rule' as const,id:r.id},policy:'runtime-rewrite' as const,
        evidence:'Existing native source-prior projection consumed by the direct Homd declarations'}))});
export const CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS=Object.freeze({
    contravariantRepresentable:sym('hom_con'),representedHomFamily:sym('hom_'),covariantFibreAction:sym('fib_cov_tapp0_func'),
    displayedHomEndpoint:sym('homd_'),mixedFunctorFamilyPartial:sym('Functor_catd_fapp0_func'),
    displayedHomTargetSection:sym('Homd_target_section_cat'),displayedHomSourceFunctor:sym('homd_src_func'),
    displayedHomSourceSection:sym('homd_src_sec'),displayedHomTargetFunctor:sym('homd_tgt_func')
});
export const CORE_CATEGORICAL_MIXED_ACTION_CORE_NAMES=Object.freeze(Object.fromEntries(Object.entries(CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS).map(([key,symbol])=>{
    const link=externalNames.includes(symbol.name)?dependencyLink(symbol.name,0):undefined;
    return [key,link?.kind==='free-declaration'?link.coreName:localCoreName(symbol.name)];
})) as Record<keyof typeof CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS,string>);
export type CoreCategoricalMixedActionSymbolId=keyof typeof CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS;
export const coreCategoricalMixedActionCoreName=(id:CoreCategoricalMixedActionSymbolId)=>CORE_CATEGORICAL_MIXED_ACTION_CORE_NAMES[id];
export const CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY=Object.freeze({
    revision:CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_REVISION,decision:'native-homd-ladder-migration-2026-10-25',
    declarationNames:Object.freeze(declarations.map(d=>d.symbol.name)),
    transparentDefinitionNames:Object.freeze(declarations.filter(d=>d.body.kind==='explicit-term').map(d=>d.symbol.name)),
    runtimeRuleIds:Object.freeze([...runtimeRules,...identityRuntimeRules].map(r=>r.id)),reusedProofRuleIds:Object.freeze([]),
    declarationCount:declarations.length,runtimeRuleCount:runtimeRules.length+identityRuntimeRules.length,proofRuleCount:0,reusedProofRuleCount:0,
    activeLambdapiOwnerDelta:0,activeLambdapiRuleDelta:0,intrinsicCoreOwnerDelta:0,ownerSpecificCheckerOrEvaluatorDelta:0,
    externalCoherenceEvidenceDelta:0,nestedAbstractionLowererDelta:0,textOrBrowserDelta:0,allEntriesUseGenericTransferEngines:true
});
const initialModule=makeModule('native-homd-ladder-initial',initialDeclarations);
export const CORE_NATIVE_HOMD_IDENTITY_MODULE=makeModule('native-homd-identity',identityDeclarations,initialDeclarations.map(d=>d.symbol.name));
const finalModule=makeModule('native-homd-ladder-final',finalDeclarations,[...initialDeclarations,...identityDeclarations].map(d=>d.symbol.name));
export const CORE_NATIVE_HOMD_IDENTITY_RUNTIME_MODULE=makeModule('native-homd-identity-projections',[],[...initialDeclarations,...identityDeclarations].map(d=>d.symbol.name).concat('hom_precomp_along_fapp1_fapp0'),identityRuntimeRules);
const identityRuntimePolicy=createCoreLfTransferPolicyOverlay(CORE_NATIVE_HOMD_IDENTITY_RUNTIME_MODULE,{
    revision:'native-homd-identity-projections-policy',moduleRevision:CORE_NATIVE_HOMD_IDENTITY_RUNTIME_MODULE.revision,
    entries:identityRuntimeRules.map(r=>({order:r.order,target:{kind:'runtime-rule' as const,id:r.id},policy:'runtime-rewrite' as const,
        evidence:'Existing native covariance/mate/identity projection'}))});
function compileNativeLadder() {
    const prerequisite=compileCoreCategoricalMixedModeTransfer();
    const initialCompiled=compileCoreLfDeclarations(initialModule,makePolicy(initialModule),makeLinkage(initialModule),{
        initialEnvironment:prerequisite.compiled.environment,runtimeProgram:prerequisite.composedRuntime,comparisonStepLimit:512});
    const initialContext=new CoreLfMixedDeclarationContext(prerequisite.declarationContext,[initialCompiled]);
    const initialRuntimeFragment=compileCoreLfRuntimeFragment(CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE,
        CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY,initialContext,{
            dependencies:[{relation:'earlier-fragment',fragment:prerequisite.runtimeFragment}],comparisonStepLimit:512});
    const precomposition=compileCoreNativePrecompositionAction({compiled:initialCompiled,
        declarationContext:initialContext,runtimeFragment:initialRuntimeFragment});
    const identityCompiled=compileCoreLfDeclarations(CORE_NATIVE_HOMD_IDENTITY_MODULE,makePolicy(CORE_NATIVE_HOMD_IDENTITY_MODULE),makeLinkage(CORE_NATIVE_HOMD_IDENTITY_MODULE),{
        initialEnvironment:precomposition.compiled.environment,runtimeProgram:precomposition.composedRuntime,comparisonStepLimit:2048});
    const identityContext=new CoreLfMixedDeclarationContext(precomposition.declarationContext,[identityCompiled]);
    const runtimeFragment=compileCoreLfRuntimeFragment(CORE_NATIVE_HOMD_IDENTITY_RUNTIME_MODULE,identityRuntimePolicy,identityContext,{
        dependencies:[{relation:'earlier-fragment',fragment:precomposition.runtimeFragment}],comparisonStepLimit:2048});
    const compiled=compileCoreLfDeclarations(finalModule,makePolicy(finalModule),makeLinkage(finalModule),{
        initialEnvironment:identityCompiled.environment,runtimeProgram:runtimeFragment.runtime,comparisonStepLimit:512});
    const declarationContext=new CoreLfMixedDeclarationContext(identityContext,[compiled]);
    return {prerequisite,initialCompiled,identityCompiled,precomposition,initialRuntimeFragment,compiled,declarationContext,runtimeFragment,
        runtime:runtimeFragment.localProgram,composedRuntime:runtimeFragment.runtime};
}
export type CoreCategoricalMixedActionCompilation=ReturnType<typeof compileNativeLadder>;
let cached:CoreCategoricalMixedActionCompilation|undefined;
export function compileCoreCategoricalMixedActionTransfer():CoreCategoricalMixedActionCompilation {
    return cached??(cached=compileNativeLadder());
}
