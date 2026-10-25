/** Native source-prior duality used by the corrected whole Homd target.
 * This is transfer data for existing owners, not a second duality theory.
 */
import { binderMode } from './kernel';
import {
    CoreLfTransferBuilderExpression as Expr, CoreLfTransferScopedBuilder as Builder,
    CoreLfQualifiedSymbol, CoreLfTransferRuntimeRule, coreLfQualifiedSymbol,
    coreLfTransferAbsentBody, createCoreLfModuleSpec, createCoreLfTransferPolicyOverlay
} from './lf_transfer';
import { createCoreLfTransferDeclarationLinkage, compileCoreLfDeclarations } from './lf_transfer_compiler';
import { CoreLfMixedDeclarationContext } from './lf_transfer_mixed';
import { CoreLfCompiledRuntimeFragment, compileCoreLfRuntimeFragment } from './lf_transfer_runtime';
import { CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE } from './directed_continuation_transfer';
import { CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE } from './categorical_fibred_dependent_target_transfer';
import { compileCoreCategoricalDisplayedChain2aClosureRuntime } from './categorical_displayed_chain_2a_closure_transfer';

const moduleId = 'emdash.emdash3_2';
const sym = (name: string) => coreLfQualifiedSymbol(moduleId, name);
const Cat = sym('Cat'), Obj = sym('Obj'), tau = sym('τ'), Functor = sym('Functor');
const Op = sym('Op_cat'), Hom = sym('Hom_cat'), fapp = sym('fapp0');
const C2 = sym('CoAt2_cat'), C2F = sym('CoAt2_func');
const implicit = binderMode('implicit', 'functorial'), explicit = binderMode('explicit', 'functorial');
const sourceSha256 = 'sha256:70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e';
const source = (sourceFragment: string) => ({ authorityPath: 'emdash2/emdash3_2.lp', sourceFragment });
const call = (b: Builder, s: CoreLfQualifiedSymbol, args: readonly Expr[], implicitCount = 0): Expr =>
    b.call(b.global(s), args.map((value,index) => ({ value, plicity: index < implicitCount ? 'implicit' : 'explicit' })));
const c2 = (b: Builder, A: Expr) => call(b,C2,[A]);
const op = (b: Builder, A: Expr) => call(b,Op,[A]);
const obj = (b: Builder, A: Expr) => call(b,tau,[call(b,Obj,[A])]);
const fn = (b: Builder, A: Expr, B: Expr) => call(b,tau,[call(b,Functor,[A,B])]);
const map = (b: Builder, A: Expr, B: Expr, F: Expr) => call(b,C2F,[A,B,F],2);
const app = (b: Builder, A: Expr, B: Expr, F: Expr, x: Expr) => call(b,fapp,[A,B,F,x],2);
const catType = () => {
    const b = new Builder(); return b.term(b.pi('A', b.global(Cat), () => b.global(Cat), explicit));
};
const mapType = () => {
    const b = new Builder();
    return b.term(b.pi('A',b.global(Cat), A => b.pi('B',b.global(Cat), B =>
        b.pi('F',fn(b,A,B), () => fn(b,c2(b,A),c2(b,B)),explicit),implicit),implicit));
};
const declarations = [
    { order:0, symbol:C2, type:catType(), body:coreLfTransferAbsentBody(),
        modifiers:{ visibility:'public' as const, rigidity:'injective' as const, sourceOpacity:'opaque' as const },
        provenance:source('injective symbol CoAt2_cat (A : Cat) : Cat;') },
    { order:1, symbol:C2F, type:mapType(), body:coreLfTransferAbsentBody(),
        modifiers:{ visibility:'public' as const, rigidity:'injective' as const, sourceOpacity:'opaque' as const },
        provenance:source('injective symbol CoAt2_func [A B : Cat] (F : τ (Functor A B))') }
];
const external = [Cat,Obj,tau,Functor,Op,Hom,fapp];
export const CORE_HOMD_DUALITY_MODULE = createCoreLfModuleSpec({
    revision:'HOMD-NATIVE-DUALITY-1', moduleId, fragmentId:'homd-native-duality',
    authorityPath:'emdash2/emdash3_2.lp', sourceSha256, dependencies:[],
    externalSymbols:external.map(symbol => ({symbol,availability:'earlier-fragment' as const})),
    declarations, inductives:[], runtimeRules:[], proofRules:[]
});
const policy = createCoreLfTransferPolicyOverlay(CORE_HOMD_DUALITY_MODULE, {
    revision:'HOMD-NATIVE-DUALITY-POLICY-1', moduleRevision:CORE_HOMD_DUALITY_MODULE.revision,
    entries:declarations.map(d => ({order:d.order,target:{kind:'declaration' as const,symbol:d.symbol},
        policy:'opaque-signature' as const,evidence:'Existing native strict-functor duality signature'}))
});
const priorLinks = [...CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE.entries,
    ...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries];
export const CORE_HOMD_DUALITY_LINKAGE = createCoreLfTransferDeclarationLinkage(CORE_HOMD_DUALITY_MODULE, {
    revision:'HOMD-NATIVE-DUALITY-LINKAGE-1',moduleRevision:CORE_HOMD_DUALITY_MODULE.revision,
    entries:[...external.map((symbol,order) => {
        const link=priorLinks.find(l=>l.symbol.moduleId===symbol.moduleId&&l.symbol.name===symbol.name);
        if(!link) throw new Error(`Missing native duality dependency ${symbol.name}`);
        return {...link,order};
    }),...declarations.map((d,index)=>({order:external.length+index,symbol:d.symbol,
        kind:'free-declaration' as const,coreName:`emdash_v3_2_homd_native_${d.symbol.name}`,backendName:d.symbol.name}))]
});
const categoryRule = (kind:'involution'|'objects'|'hom'|'commute', order:number): CoreLfTransferRuntimeRule => {
    const b=new Builder(), A=b.capture('A'), x=b.capture('x'), y=b.capture('y');
    const left=kind==='involution'?c2(b,c2(b,A)):kind==='objects'?call(b,Obj,[c2(b,A)]):
        kind==='hom'?call(b,Hom,[c2(b,A),x,y]):op(b,c2(b,A));
    const right=kind==='involution'?A:kind==='objects'?call(b,Obj,[A]):
        kind==='hom'?op(b,call(b,Hom,[A,x,y])):c2(b,op(b,A));
    return {order,id:`categorical.homd-duality.${kind}`,groupId:`categorical.homd-duality.${kind}`,clauseOrder:0,
        sourceOwner:kind==='involution'?C2:kind==='objects'?Obj:kind==='hom'?Hom:Op,
        variables:[{name:'A',type:b.template(b.global(Cat))},...(kind==='hom'?['x','y'].map(name=>({name,type:b.template(obj(b,A))})):[])],
        left:b.pattern(left),right:b.template(right),provenance:source(kind==='involution'?'rule CoAt2_cat (CoAt2_cat $A) ↪ $A;':
            kind==='objects'?'rule Obj (CoAt2_cat $A) ↪ Obj $A;':
            kind==='hom'?'rule Hom_cat (CoAt2_cat $A) $X $Y ↪ Op_cat (Hom_cat $A $X $Y);':
            'rule Op_cat (CoAt2_cat $A) ↪ CoAt2_cat (Op_cat $A);')};
};
const mapObjectRule = (): CoreLfTransferRuntimeRule => {
    const b=new Builder(), A=b.capture('A'), B=b.capture('B'), F=b.capture('F'), x=b.capture('x');
    return {order:4,id:'categorical.homd-duality.functor-object',groupId:'categorical.homd-duality.functor-object',clauseOrder:0,
        sourceOwner:fapp,variables:[...['A','B'].map(name=>({name,type:b.template(b.global(Cat))})),
            {name:'F',type:b.template(fn(b,A,B))},{name:'x',type:b.template(obj(b,A))}],
        left:b.pattern(app(b,b.wildcard(c2(b,A)),b.wildcard(c2(b,B)),map(b,A,B,F),x)),
        right:b.template(app(b,A,B,F,x)),provenance:source('rule @fapp0 _ _ (@CoAt2_func $A $B $F) $x ↪ @fapp0 $A $B $F $x;')};
};
const rules=[categoryRule('involution',0),categoryRule('objects',1),categoryRule('hom',2),categoryRule('commute',3),mapObjectRule()];
export const CORE_HOMD_DUALITY_RUNTIME_MODULE = createCoreLfModuleSpec({
    revision:'HOMD-NATIVE-DUALITY-RUNTIME-1',moduleId,fragmentId:'homd-native-duality-runtime',
    authorityPath:'emdash2/emdash3_2.lp',sourceSha256,dependencies:[],
    externalSymbols:[...external,C2,C2F].map(symbol=>({symbol,availability:'earlier-fragment' as const})),
    declarations:[],inductives:[],runtimeRules:rules,proofRules:[]
});
const runtimePolicy=createCoreLfTransferPolicyOverlay(CORE_HOMD_DUALITY_RUNTIME_MODULE,{
    revision:'HOMD-NATIVE-DUALITY-RUNTIME-POLICY-1',moduleRevision:CORE_HOMD_DUALITY_RUNTIME_MODULE.revision,
    entries:rules.map(rule=>({order:rule.order,target:{kind:'runtime-rule' as const,id:rule.id},
        policy:'runtime-rewrite' as const,evidence:'Literal native duality projection needed by the Homd target'}))
});
export function compileCoreHomdDualityTransfer() {
    const prerequisite=compileCoreCategoricalDisplayedChain2aClosureRuntime();
    const compiled=compileCoreLfDeclarations(CORE_HOMD_DUALITY_MODULE,policy,CORE_HOMD_DUALITY_LINKAGE,{
        initialEnvironment:prerequisite.compiled.environment,runtimeProgram:prerequisite.composedRuntime
    });
    const declarationContext=new CoreLfMixedDeclarationContext(prerequisite.declarationContext,[compiled]);
    const inherited=new CoreLfCompiledRuntimeFragment(prerequisite.runtime,[],prerequisite.composedRuntime);
    const runtimeFragment=compileCoreLfRuntimeFragment(CORE_HOMD_DUALITY_RUNTIME_MODULE,runtimePolicy,declarationContext,{
        dependencies:[{relation:'earlier-fragment',fragment:inherited}]
    });
    return {prerequisite,compiled,declarationContext,runtimeFragment,runtime:runtimeFragment.localProgram,
        composedRuntime:runtimeFragment.runtime};
}
