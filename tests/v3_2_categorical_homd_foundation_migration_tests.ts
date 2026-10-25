/** Current native Homd target/root, separate from historical acquisition. */
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { describe,it } from 'node:test';
import { compileCoreCategoricalDisplayedNdHigherFoundationTransfer } from '../src/v3_2/categorical_displayed_nd_higher_foundation_transfer';
import { compileCoreCategoricalDisplayedNdHigherTargetTransfer } from '../src/v3_2/categorical_displayed_nd_higher_target_transfer';
import { CoreCategoricalProgram } from '../src/v3_2/categorical_program';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';
import { checkLambdapiProbe } from '../src/v3_2/probe';

const migrated = () => {
    const target=compileCoreCategoricalDisplayedNdHigherTargetTransfer(),foundation=target.prerequisite;
    const duality=foundation.prerequisite,chain2=duality.prerequisite,chain=chain2.prerequisite;
    const evaluation=chain.prerequisite,pi=evaluation.prerequisite,weaken=pi.prerequisite;
    const transfd=weaken.prerequisite,binder=transfd.prerequisite,structure=binder.prerequisite;
    const product=structure.prerequisite,comprehension=product.prerequisite,composition=comprehension.prerequisite;
    const dependent=composition.dependent,structural=dependent.structural;
    const modules=[structural.initialDeclarations,structural.compiled,dependent.compiled,composition.compiled,
        comprehension.compiled,product.compiled,structure.compiled,binder.compiled,transfd.compiled,
        weaken.compiled,pi.compiled,evaluation.prerequisiteCompiled,evaluation.compiled,
        chain.prerequisiteCompiled,chain.compiled,chain2.compiled,duality.compiled,
        foundation.signatureCompiled,foundation.compiled,target.compiled];
    const references=Object.assign({},...modules.flatMap(m=>[m.externalFreeReferences,m.externalTransparentDefinitions,
        Object.fromEntries(m.linkage.entries.flatMap(link=>link.kind==='free-declaration' && link.backendName
            ? [[link.coreName,link.backendName]] : []))]));
    return {target,foundation,serialize:(term:Parameters<typeof serializeKernelExpression>[0])=>
        serializeKernelExpression(term,{externalFreeReferences:references})};
};

describe('native Homd foundation migration',()=>{
    it('checks the defined target and relative root through native precomposition owners',()=>{
        const c=compileCoreCategoricalDisplayedNdHigherFoundationTransfer();
        assert.deepEqual(c.compiled.declarations.map(d=>[d.symbol.name,d.status]),[
            ['Homd_target_con_func','installed-transparent'],['Homd_target_map','installed-transparent'],
            ['homd_id_int','installed-opaque'],['homd_rel_cart_int','installed-transparent'],['homd_int','installed-transparent']]);
        assert.equal(c.signatureCompiled.declarations.find(d=>d.symbol.name==='Homd_target_catd')?.status,'installed-transparent');
        assert.deepEqual(c.runtime.ruleIds,[
            'categorical.homd-native.hom-int-object','categorical.homd-native.precomp-object',
            'categorical.homd-native.cart-precomp-composition',
            'categorical.homd-native.postcomp-object','categorical.homd-native.diagram-object']);
        assert.ok(c.runtime.rules.every(r=>r.subjectValidation.kind==='typescript-checked'));
    });
    it('checks exact native types, defined bodies and the emitted whole higher action',{
        skip:process.env.EMDASH_RUN_LAMBDAPI_NATIVE_HOMD_PROBES!=='1'
    },()=>{
        const {foundation,target,serialize}=migrated();
        const e=new CoreCategoricalProgram({sourceFile:'native-homd.ts',profile:'fibred-displayed-nd-higher-1'});
        const K=e.category('K'),E=e.displayedFamily('E',K),D=e.displayedFamily('D',K);
        const FF=e.displayedFunctor('FF',E,D),GG=e.displayedFunctor('GG',E,D);
        const epsilon=e.displayedTransfor('epsilon',FF,GG),epsilonPrime=e.displayedTransfor('epsilonPrime',FF,GG);
        const category=e.displayedTransforCategory(FF,GG),m=e.hom('m',category,epsilon,epsilonPrime);
        const action=e.displayedTransforInternalHomAction(FF,GG);
        const object=e.apply(action,epsilon);
        const hom=e.apply(action,e.homBoundary(category,epsilon,epsilonPrime),{expectedShape:'whole-hom-action'});
        const cell=e.apply(hom,m);
        const terms=[action,object,hom,cell].map(t=>e.compile(t));
        const declarations=[...foundation.signatureCompiled.declarations,...foundation.compiled.declarations,...target.compiled.declarations];
        const source=['require open emdash.emdash3_2;',
            ...declarations.flatMap(d=>[
                `assert ⊢ @${d.symbol.name} : ${serialize(d.type)};`,
                ...(d.body?[`assert ⊢ @${d.symbol.name} ≡ ${serialize(d.body)};`]:[])
            ]),
            'symbol K : Cat;','symbol E : τ (Catd K);','symbol D : τ (Catd K);',
            'symbol FF : τ (Functord E D);','symbol GG : τ (Functord E D);',
            'symbol epsilon : τ (Transfd FF GG);','symbol epsilonPrime : τ (Transfd FF GG);',
            'symbol m : τ (Hom (Transfd_cat FF GG) epsilon epsilonPrime);',
            ...terms.map(t=>`assert ⊢ ${serialize(t.explicitTerm)} : ${serialize(t.expectedType)};`),
            `assert ⊢ ${serialize(terms[1].explicitTerm)} ≡ @tdapp1_int_fapp0_transfd K E D FF GG epsilon;`,
            'assertnot ⊢ @Op_funcd K E D FF : τ (Hom (Functor_cart_cat (CoAt2_cat K) Cat_cart) (@Op_catd K E) (@Op_catd K D));'
        ].join('\n');
        assert.doesNotMatch(source,/dttlf_|emdash_v3_2_/);
        const result=checkLambdapiProbe({source,sourceMap:[]},{packageRoot:resolve(__dirname,'../emdash2'),timeoutMs:60_000});
        assert.equal(result.accepted,true,result.diagnostics+'\n'+source);
        assert.equal(result.timedOut,false);
    });
});
