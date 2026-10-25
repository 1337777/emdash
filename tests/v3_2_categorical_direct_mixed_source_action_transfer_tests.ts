/**
 * DIRECT-MIXED-SOURCE-ACTION-1E2 and D-046 prerequisite coverage.
 */

import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { coreCategoricalFamilyCoefficient } from '../src/v3_2/categorical_family_coefficient';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';
import { checkLambdapiProbe } from '../src/v3_2/probe';
import { CoreCategoricalProgram } from '../src/v3_2/categorical_program';
import { CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE } from '../src/v3_2/directed_continuation_transfer';
import {
    describe,
    it
} from 'node:test';
import {
    CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY,
    CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE,
    CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_POLICY,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CORE_NAMES,
    CORE_CATEGORICAL_STRUCTURAL_SYMBOLS,
    compileCoreCategoricalDirectMixedSourceActionTransfer,
    coreCategoricalDisplayedEvaluationCoreName,
    coreCategoricalDisplayedNdHigherFoundationCoreName,
    coreCategoricalMixedActionCoreName,
    coreCategoricalStructuralSymbolCoreName,
    coreCategoricalFibredProductCoreName,
    kernelApplication,
    kernelCall,
    kernelExpressionEquals,
    kernelFree,
    provenance
} from '../src/v3_2';
import type {
    KernelExpression,
    Plicity
} from '../src/v3_2';

const assertDeepFrozen = (value: unknown): void => {
    if (value === null || typeof value !== 'object') return;
    assert.equal(Object.isFrozen(value), true);
    Reflect.ownKeys(value).forEach(key =>
        assertDeepFrozen(
            (value as Record<PropertyKey, unknown>)[key]
        )
    );
};

describe('DIRECT-MIXED-SOURCE-ACTION-1E2 runtime transfer', () => {
    it('uses a Cartesian diagram-map carrier with the ordinary displayed view', () => {
        const e = new CoreCategoricalProgram({profile:'fibred-displayed-mixed-nest-1'});
        const K=e.category('strict_K'), A=e.displayedFamily('strict_A',K), B=e.displayedFamily('strict_B',K);
        const L=e.cartesianDisplayedFunctor('strict_L',A,B), G=e.displayedFunctor('lax_G',A,B);
        const strict=e.compile(L), lax=e.compile(G);
        assert.equal(strict.surfaceType.tag,'displayed-functor');
        assert.equal(lax.surfaceType.tag,'displayed-functor');
        assert.match(strict.explicitCore,/strict_transfor/u);
        assert.doesNotMatch(lax.explicitCore,/strict_transfor/u);
        const k=e.object('strict_k',K), a=e.object('strict_a',e.fibre(A,k));
        assert.doesNotThrow(()=>e.compile(e.apply(e.apply(L,k,{expectedShape:'fibre-functor'}),a)));
    });

    it('checks emitted native actions and rejects a lax negative-family map', {
        skip:process.env.EMDASH_RUN_LAMBDAPI_DIRECT_MIXED_PROBES!=='1'
    },()=>{
        const c=compileCoreCategoricalDirectMixedSourceActionTransfer();
        const intro=c.prerequisite;
        const references: Record<string,string>={};
        for (const link of CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries) {
            if (link.kind==='free-declaration') references[link.coreName]=link.backendName;
        }
        for (const module of [CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE,intro.runtime.module]) {
            for (const external of module.externalSymbols) {
                const d=c.declarationContext.declaration(external.symbol);
                if (d?.link.kind==='free-declaration') references[d.link.coreName]=d.link.backendName;
            }
        }
        const at=provenance('derived','native direct mixed profiles');
        const action=c.prerequisite.prerequisite;
        for (const module of [action.initialCompiled,action.compiled]) {
            Object.assign(references,module.externalFreeReferences,module.externalTransparentDefinitions);
        }
        for (const name of ['comp_catd_fapp0','comp_fapp0']) {
            const d=c.declarationContext.declaration({moduleId:'emdash.emdash3_2',name});
            if(d?.link.kind==='free-declaration')references[d.link.coreName]=d.link.backendName;
        }
        const equations=[...intro.runtime.rules,...c.runtime.rules].flatMap((rule,index)=>{
            const names=Object.fromEntries(rule.variables.map(v=>[v.name,`r${index}_${v.name}`]));
            const runtime=index<intro.runtime.rules.length?intro.runtime:c.runtime;
            const types:Record<string,string>=rule.id.endsWith('cartesian-postcomposition')?{
                A:'Cat',B:'Cat',C:'Cat',F:'τ (Functor A B)',G:'τ (Functor B C)'
            }:rule.id.endsWith('opposite-hom-endpoints')?{
                A:'Cat',X:'τ (Obj A)',Y:'τ (Obj A)'
            }:{
                K:'Cat',A:'τ (Catd (Op_cat K))',APrime:'τ (Catd (Op_cat K))',B:'τ (Catd K)',D:'τ (Catd K)',
                L:'τ (Hom (Functor_cart_cat (Op_cat K) Cat_cart) APrime A)',G:'τ (Functord B D)',k:'τ (Obj K)',
                H:'τ (Functor (Fibre_cat A k) (Fibre_cat B k))'
            };
            const rename=(s:string)=>s.replace(/\b[A-Za-z]+\b/gu,n=>names[n]??n);
            const left=runtime.instantiateRuleLeft(rule,rule.variables.map(v=>kernelFree(v.name,at)),at);
            const result=runtime.rewriteHead(left);
            assert.equal(result.status,'rewritten');
            if(result.status!=='rewritten')throw new Error('Missing direct action projection');
            assert.equal(result.ruleId,rule.id);
            const serialize=(term:KernelExpression)=>serializeKernelExpression(term,{externalFreeReferences:{...references,...names}});
            return [...rule.variables.map(v=>`symbol ${names[v.name]} : ${rename(types[v.name])};`),
                `assert ⊢ ${serialize(left)} ≡ ${serialize(result.after)};`];
        });
        const e=new CoreCategoricalProgram({profile:'fibred-direct-mixed-introduction-1'});
        const base=e.category('K'), negative=e.oppositeCategory(base);
        const A=e.displayedFamily('A',negative), AP=e.displayedFamily('AP',negative);
        const C=e.displayedFamily('C',base), B=e.displayedFamily('B',base), D=e.displayedFamily('D',base);
        const L=e.cartesianDisplayedFunctor('L',AP,A), G=e.displayedFunctor('G',B,D);
        const F=e.displayedFunctor('F',C,e.mixedDisplayedFunctorFamily(A,B));
        const resultTerm=e.mixedDisplayedFunctorLambda({name:'c',family:C},{name:'a',family:AP},D,
            (c,a)=>e.apply(G,e.apply(e.apply(F,c),e.apply(L,a))));
        const checked=e.compile(resultTerm);
        const lax=e.displayedFunctor('LL',AP,A);
        assert.throws(()=>e.mixedDisplayedFunctorLambda({name:'badc',family:C},{name:'bada',family:AP},B,
            (c,a)=>e.apply(e.apply(F,c),e.apply(lax,a))),/Cartesian displayed map/u);
        const source=['require open emdash.emdash3_2;',...equations,
            'symbol K : Cat;', 'symbol A : τ (Catd (Op_cat K));', 'symbol AP : τ (Catd (Op_cat K));',
            'symbol C : τ (Catd K);', 'symbol B : τ (Catd K);', 'symbol D : τ (Catd K);',
            'symbol F : τ (Functord C (Functor_catd A B));', 'symbol G : τ (Functord B D);',
            'symbol L : τ (Hom (Functor_cart_cat (Op_cat K) Cat_cart) AP A);',
            'symbol LL : τ (Functord AP A);',
            'assert ⊢ @strict_transfor (Op_cat K) Cat_cart AP A L : τ (Functord AP A);',
            'assert ⊢ @fapp1_fapp0 (Op_cat (Functor_cart_cat (Op_cat K) Cat_cart)) (Functor_cat (Catd_cat K) (Catd_cat K)) (Functor_catd_func K) A AP L : τ (Hom (Functor_cat (Catd_cat K) (Catd_cat K)) (@Functor_catd_fapp0_func K A) (@Functor_catd_fapp0_func K AP));',
            'assertnot ⊢ @fapp1_fapp0 (Op_cat (Functor_cart_cat (Op_cat K) Cat_cart)) (Functor_cat (Catd_cat K) (Catd_cat K)) (Functor_catd_func K) A AP LL : τ (Hom (Functor_cat (Catd_cat K) (Catd_cat K)) (@Functor_catd_fapp0_func K A) (@Functor_catd_fapp0_func K AP));',
            `assert ⊢ ${serializeKernelExpression(checked.explicitTerm,{externalFreeReferences:references})} : ${serializeKernelExpression(checked.expectedType,{externalFreeReferences:references})};`
        ].join('\n');
        assert.doesNotMatch(source,/dttlf_|emdash_v3_2_/u);
        const result=checkLambdapiProbe({source,sourceMap:[]},{packageRoot:resolve(__dirname,'../emdash2'),timeoutMs:60_000});
        assert.equal(result.accepted,true,result.diagnostics+'\n'+source);
        assert.equal(result.timedOut,false);
    });

    it('pins the two native source-action rules',
    () => {
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE
                .declarations.length,
            0
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE
                .runtimeRules.length,
            2
        );
        assert.deepEqual(
            [
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .parentDecision,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .decision
            ],
            [
                'D-DTTLF-USABILITY-045',
                'foundations-frontend-direct-mixed-2026-10-25'
            ]
        );
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_POLICY
                .entries.map(entry => entry.policy),
            ['runtime-rewrite', 'runtime-rewrite']
        );
        assert.deepEqual(
            [
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .existingPrerequisiteRuntimeRuleCount,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .newMathematicalRuntimeRuleCount,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .activeLambdapiOwnerDelta,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .activeLambdapiRuleDelta,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .intrinsicCoreOwnerDelta,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .ownerSpecificCheckerOrEvaluatorDelta,
                CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                    .externalCoherenceEvidenceDelta
            ],
            [2, 0, 0, 0, 0, 0, 0]
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
                .transfersContextualCurry,
            false
        );
        assertDeepFrozen(
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY
        );
    });

    it('subject-checks both rules without an external oracle', () => {
        const compilation =
            compileCoreCategoricalDirectMixedSourceActionTransfer();
        assert.deepEqual(
            compilation.runtime.rules.map(rule =>
                rule.subjectValidation.kind
            ),
            ['typescript-checked', 'typescript-checked']
        );
        assert.deepEqual(
            compilation.composedRuntime.ruleIds.slice(-2),
            [
                'categorical.direct-mixed-source-action.' +
                    'opposite-hom-endpoints',
                'categorical.direct-mixed-source-action.' +
                    'source-composition-projection'
            ]
        );
    });

    it('reverses opposite Hom endpoints without collapsing categories',
    () => {
        const compilation =
            compileCoreCategoricalDirectMixedSourceActionTransfer();
        const p = provenance('derived', 'opposite Hom transfer witness');
        const A = kernelFree('source_action_category', p);
        const X = kernelFree('source_action_X', p);
        const Y = kernelFree('source_action_Y', p);
        const opA = kernelCall(
            kernelFree(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CORE_NAMES
                    .oppositeCategory,
                p
            ),
            [{ plicity: 'explicit', value: A }],
            p
        );
        const before = kernelApplication(
            'hom-category',
            [{ value: opA }, { value: X }, { value: Y }],
            p
        );
        const expected = kernelApplication(
            'hom-category',
            [{ value: A }, { value: Y }, { value: X }],
            p
        );
        const reduced = compilation.composedRuntime.rewriteHead(before);

        assert.equal(reduced.status, 'rewritten');
        if (reduced.status !== 'rewritten') {
            assert.fail('Opposite Hom endpoint rule did not fire');
        }
        assert.equal(
            reduced.ruleId,
            'categorical.direct-mixed-source-action.' +
                'opposite-hom-endpoints'
        );
        assert.equal(kernelExpressionEquals(reduced.after, expected), true);
        assert.equal(kernelExpressionEquals(opA, A), false);
    });

    it('projects the contravariant source action to an iterable composite',
    () => {
        const compilation =
            compileCoreCategoricalDirectMixedSourceActionTransfer();
        const p = provenance('derived', 'direct source action witness');
        const free = (name: string): KernelExpression => kernelFree(name, p);
        const call = (
            name: string,
            arguments_: readonly {
                readonly plicity: Plicity;
                readonly value: KernelExpression;
            }[]
        ): KernelExpression => kernelCall(
            kernelFree(name, p),
            arguments_,
            p
        );
        const K = free('source_action_K');
        const APrime = free('source_action_A_prime');
        const A = free('source_action_A');
        const B = free('source_action_B');
        const L = free('source_action_L');
        const k = free('source_action_k');
        const H = free('source_action_H');
        const a = free('source_action_a');
        const aPrime = free('source_action_a_prime');
        const ell = free('source_action_ell');
        const cat = coreCategoricalFamilyCoefficient(p);
        const opK = call(
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CORE_NAMES
                .oppositeCategory,
            [{ plicity: 'explicit', value: K }]
        );
        const catdK = kernelApplication(
            'displayed-category-category',
            [{ value: K }],
            p
        );
        const catdOpK = call(coreCategoricalStructuralSymbolCoreName(
            CORE_CATEGORICAL_STRUCTURAL_SYMBOLS.cartesianFunctorCategory), [
            { plicity: 'explicit', value: opK }, { plicity: 'explicit', value: cat }
        ]);
        const opCatdOpK = call(
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CORE_NAMES
                .oppositeCategory,
            [{ plicity: 'explicit', value: catdOpK }]
        );
        const functorCategory = (
            source: KernelExpression,
            target: KernelExpression
        ): KernelExpression => call(
            coreCategoricalStructuralSymbolCoreName(
                CORE_CATEGORICAL_STRUCTURAL_SYMBOLS.functorCategory
            ),
            [
                { plicity: 'explicit', value: source },
                { plicity: 'explicit', value: target }
            ]
        );
        const fibre = (
            base: KernelExpression,
            family: KernelExpression
        ): KernelExpression => kernelApplication(
            'functor-object',
            [
                { value: base },
                { value: cat },
                { value: family },
                { value: k }
            ],
            p
        );
        const stable = (
            source: KernelExpression,
            target: KernelExpression
        ): KernelExpression => call(
            coreCategoricalDisplayedEvaluationCoreName(
                'stableFunctorFamily'
            ),
            [
                { plicity: 'implicit', value: K },
                { plicity: 'explicit', value: source },
                { plicity: 'explicit', value: target }
            ]
        );
        const partial = (source: KernelExpression): KernelExpression =>
            call(
                coreCategoricalMixedActionCoreName(
                    'mixedFunctorFamilyPartial'
                ),
                [
                    { plicity: 'implicit', value: K },
                    { plicity: 'explicit', value: source }
                ]
            );
        const mixed = call(
            coreCategoricalDisplayedNdHigherFoundationCoreName(
                'mixedFunctorFamily'
            ),
            [{ plicity: 'explicit', value: K }]
        );
        const constructorAction = kernelApplication(
            'functor-hom-capped',
            [
                { value: opCatdOpK },
                { value: functorCategory(catdK, catdK) },
                { value: mixed },
                { value: A },
                { value: APrime },
                { value: L }
            ],
            p
        );
        const familyAction = kernelApplication(
            'transfor-component-capped',
            [
                { value: catdK },
                { value: catdK },
                { value: partial(A) },
                { value: partial(APrime) },
                { value: B },
                { value: constructorAction }
            ],
            p
        );
        const fibreAction = kernelApplication(
            'transfor-component-capped',
            [
                { value: K },
                { value: cat },
                { value: stable(A, B) },
                { value: stable(APrime, B) },
                { value: k },
                { value: familyAction }
            ],
            p
        );
        const sourceFibre = fibre(opK, APrime);
        const middleFibre = fibre(opK, A);
        const targetFibre = fibre(K, B);
        const cartesianFunctorCategory = (source: KernelExpression, target: KernelExpression) => call(
            coreCategoricalStructuralSymbolCoreName(CORE_CATEGORICAL_STRUCTURAL_SYMBOLS.cartesianFunctorCategory),
            [{ plicity: 'explicit', value: source }, { plicity: 'explicit', value: target }]);
        const before = kernelApplication(
            'functor-object',
            [
                { value: cartesianFunctorCategory(middleFibre, targetFibre) },
                { value: cartesianFunctorCategory(sourceFibre, targetFibre) },
                { value: fibreAction },
                { value: H }
            ],
            p
        );
        const LAtK = kernelApplication(
            'transfor-component-capped',
            [
                { value: opK },
                { value: cat },
                { value: APrime },
                { value: A },
                { value: k },
                { value: call(coreCategoricalFibredProductCoreName('strict-transfor-view'), [
                    { plicity: 'implicit', value: opK }, { plicity: 'implicit', value: cat },
                    { plicity: 'implicit', value: APrime }, { plicity: 'implicit', value: A },
                    { plicity: 'explicit', value: L }
                ]) }
            ],
            p
        );
        const expected = call(
            coreCategoricalStructuralSymbolCoreName(
                CORE_CATEGORICAL_STRUCTURAL_SYMBOLS.functorComposition
            ),
            [
                { plicity: 'implicit', value: sourceFibre },
                { plicity: 'implicit', value: middleFibre },
                { plicity: 'implicit', value: targetFibre },
                { plicity: 'explicit', value: H },
                { plicity: 'explicit', value: LAtK }
            ]
        );
        const projected = compilation.composedRuntime.rewriteHead(before);

        assert.equal(projected.status, 'rewritten');
        if (projected.status !== 'rewritten') {
            assert.fail('Direct mixed source projection did not fire');
        }
        assert.equal(
            projected.ruleId,
            'categorical.direct-mixed-source-action.' +
                'source-composition-projection'
        );
        assert.equal(
            kernelExpressionEquals(projected.after, expected),
            true
        );

        const objectAction = compilation.composedRuntime.rewriteHead(
            kernelApplication(
                'functor-object',
                [
                    { value: sourceFibre },
                    { value: targetFibre },
                    { value: projected.after },
                    { value: a }
                ],
                p
            )
        );
        const arrowAction = compilation.composedRuntime.rewriteHead(
            kernelApplication(
                'functor-hom-capped',
                [
                    { value: sourceFibre },
                    { value: targetFibre },
                    { value: projected.after },
                    { value: a },
                    { value: aPrime },
                    { value: ell }
                ],
                p
            )
        );
        assert.equal(objectAction.status, 'rewritten');
        assert.equal(arrowAction.status, 'rewritten');
        if (
            objectAction.status === 'rewritten' &&
            arrowAction.status === 'rewritten'
        ) {
            assert.equal(
                kernelExpressionEquals(
                    objectAction.after,
                    arrowAction.after
                ),
                false
            );
        }
    });
});
