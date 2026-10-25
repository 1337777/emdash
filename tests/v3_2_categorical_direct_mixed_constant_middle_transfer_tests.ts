/**
 * DIRECT-MIXED-CONSTANT-MIDDLE-COMPOSITION-1M generic transfer coverage.
 */

import assert from 'node:assert/strict';
import { coreCategoricalFamilyCoefficient } from '../src/v3_2/categorical_family_coefficient';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';
import { checkLambdapiProbe } from '../src/v3_2/probe';
import {
    createHash
} from 'node:crypto';
import {
    readFileSync
} from 'node:fs';
import {
    resolve
} from 'node:path';
import {
    describe,
    it
} from 'node:test';
import {
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY,
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_CORE_NAMES,
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_RUNTIME_MODULE,
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_RUNTIME_POLICY,
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_MODULE,
    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_POLICY,
    CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256,
    compileCoreCategoricalDirectMixedConstantMiddleTransfer,
    kernelApplication,
    kernelCall,
    kernelFree,
    provenance,
    serializeCoreExpression
} from '../src/v3_2';
import type {
    KernelExpression,
    Plicity
} from '../src/v3_2';

const activeKernelPath = resolve(
    __dirname,
    '..',
    'emdash2',
    'emdash3_2.lp'
);

const assertDeepFrozen = (value: unknown): void => {
    if (value === null || typeof value !== 'object') return;
    assert.equal(Object.isFrozen(value), true);
    Reflect.ownKeys(value).forEach(key =>
        assertDeepFrozen(
            (value as Record<PropertyKey, unknown>)[key]
        )
    );
};

describe('DIRECT-MIXED-CONSTANT-MIDDLE-1M transfer', () => {
    it('checks native distributor, weakening and constant-middle whole actions', {
        skip:process.env.EMDASH_RUN_LAMBDAPI_DIRECT_MIXED_STRUCTURES!=='1'
    },()=>{
        const c=compileCoreCategoricalDirectMixedConstantMiddleTransfer();
        const w=c.prerequisite, d=w.prerequisite;
        const selected=[d,w,c];
        const references:Record<string,string>={};
        for(const part of selected){
            for(const module of [part.compiled.module,part.runtime.module]){
                for(const entry of [...module.externalSymbols,...module.declarations]){
                    const decl=c.declarationContext.declaration(entry.symbol);
                    if(decl?.link.kind==='free-declaration')references[decl.link.coreName]=decl.link.backendName;
                }
            }
        }
        const serialize=(term:KernelExpression,names={})=>serializeKernelExpression(term,{externalFreeReferences:{...references,...names}});
        const commands=selected.flatMap(part=>part.compiled.declarations.flatMap(decl=>[
            `assert ⊢ @${decl.symbol.name} : ${serialize(decl.type)};`,
            ...(decl.body?[`assert ⊢ @${decl.symbol.name} ≡ ${serialize(decl.body)};`]:[])
        ]));
        const at=provenance('derived','direct mixed native structures');
        const equations=selected.flatMap((part,moduleIndex)=>part.runtime.rules.flatMap((rule,index)=>{
            const names=Object.fromEntries(rule.variables.map(v=>[v.name,`s${moduleIndex}_${index}_${v.name}`]));
            const types:Record<string,string>=rule.id.endsWith('ordinary-point')?{
                W:'Cat',X:'Cat',Z:'Cat',pg:'τ (Obj (Product_cat (Functor_cart_cat W X) (Functor_cart_cat X Z)))'
            }:{K:'Cat',X:'Cat',A:'τ (Catd (Op_cat K))',B:'τ (Catd K)',C:'τ (Catd K)',
                k:'τ (Obj K)',x:'τ (Obj K)',y:'τ (Obj K)',p:'τ (Hom K x y)'};
            const rename=(type:string)=>type.replace(/\b[A-Za-z]+\b/gu,n=>names[n]??n);
            const left=part.runtime.instantiateRuleLeft(rule,rule.variables.map(v=>kernelFree(v.name,at)),at);
            const result=part.runtime.rewriteHead(left);
            assert.equal(result.status,'rewritten');
            if(result.status!=='rewritten')throw new Error('Missing native structure projection');
            assert.equal(result.ruleId,rule.id);
            return [...rule.variables.map(v=>`symbol ${names[v.name]} : ${rename(types[v.name])};`),
                `assert ⊢ ${serialize(left,names)} ≡ ${serialize(result.after,names)};`];
        }));
        const source=['require open emdash.emdash3_2;',...commands,...equations].join('\n');
        assert.doesNotMatch(source,/dttlf_|emdash_v3_2_/u);
        const result=checkLambdapiProbe({source,sourceMap:[]},{packageRoot:resolve(__dirname,'../emdash2'),timeoutMs:60_000});
        assert.equal(result.accepted,true,result.diagnostics+'\n'+source);
        assert.equal(result.timedOut,false);
    });

    it('pins the exact three-declaration/four-rule generic boundary', () => {
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_MODULE
                .declarations.map(entry => entry.symbol.name),
            [
                'comp_prod_func',
                'Functor_comp_pair_func',
                'Functor_comp_pair_funcd'
            ]
        );
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_MODULE
                .declarations.map(entry => entry.body.kind),
            ['absent', 'explicit-term', 'absent']
        );
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_POLICY
                .entries.map(entry => entry.policy),
            [
                'opaque-signature',
                'checked-transparent-definition',
                'opaque-signature'
            ]
        );
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_RUNTIME_MODULE
                .runtimeRules.map(rule => rule.id),
            [
                'categorical.direct-mixed-constant-middle.ordinary-point',
                'categorical.direct-mixed-constant-middle.point',
                'categorical.direct-mixed-constant-middle.full-action',
                'categorical.direct-mixed-constant-middle.capped-action'
            ]
        );
        assert.deepEqual(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_RUNTIME_POLICY
                .entries.map(entry => entry.policy),
            Array.from({ length: 4 }, () => 'runtime-rewrite')
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY.decision,
            'foundations-frontend-direct-mixed-2026-10-25'
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .directNestedIntroductionRemainsFundamental,
            true
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .contextualCurryDependency,
            false
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .totalContextSectionDependency,
            false
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .ordinaryPointTransferScope,
            'Cat_cart-specialization'
        );
        assert.equal(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .ordinaryPointRightPresentation,
            'checked-transparent-comp_cat_fapp0'
        );
        assert.doesNotMatch(
            JSON.stringify({
                declarations:
                    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_TRANSFER_MODULE,
                runtime:
                    CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_RUNTIME_MODULE
            }),
            /mixed_curry|mix_uncurried_family|coerc|cast/u
        );
        assertDeepFrozen(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
        );
    });

    it('checks every declaration and runtime subject generically', () => {
        const compilation =
            compileCoreCategoricalDirectMixedConstantMiddleTransfer();

        assert.equal(compilation.compiled.declarations.length, 3);
        assert.equal(compilation.runtimeFragment.localProgram.rules.length, 4);
        assert.deepEqual(
            compilation.runtimeFragment.localProgram.rules.map(rule =>
                rule.subjectValidation.kind
            ),
            Array.from({ length: 4 }, () => 'typescript-checked')
        );
        assert.deepEqual(
            compilation.composedRuntime.ruleIds.slice(-4),
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_BOUNDARY
                .runtimeRuleIds
        );
        assertDeepFrozen(compilation.compiled.declarations);
        assertDeepFrozen(compilation.runtimeFragment.localProgram.rules);
    });

    it('computes ordinary object and inner-arrow action after point beta',
    () => {
        const compilation =
            compileCoreCategoricalDirectMixedConstantMiddleTransfer();
        const runtime = compilation.composedRuntime;
        const p = provenance('derived', 'constant-middle computation');
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
        const A = coreCategoricalFamilyCoefficient(p);
        const W = free('constant_middle_W');
        const X = free('constant_middle_X');
        const Z = free('constant_middle_Z');
        const pg = free('constant_middle_pair');
        const a = free('constant_middle_a');
        const aPrime = free('constant_middle_a_prime');
        const alpha = free('constant_middle_alpha');
        const compositionPair = call(
            CORE_CATEGORICAL_DIRECT_MIXED_CONSTANT_MIDDLE_CORE_NAMES
                .ordinaryCompositionPair,
            [
                { plicity: 'implicit', value: A },
                { plicity: 'implicit', value: W },
                { plicity: 'implicit', value: X },
                { plicity: 'implicit', value: Z }
            ]
        );
        const point = runtime.rewriteHead(kernelApplication(
            'functor-object',
            [
                { value: free('constant_middle_product_hom') },
                { value: free('constant_middle_target_hom') },
                { value: compositionPair },
                { value: pg }
            ],
            p
        ));

        assert.equal(point.status, 'rewritten');
        if (point.status !== 'rewritten') {
            assert.fail('Ordinary composition-pair point beta did not fire');
        }
        assert.equal(
            point.ruleId,
            'categorical.direct-mixed-constant-middle.ordinary-point'
        );
        assert.match(serializeCoreExpression(point.after), /comp_cat_fapp0/u);

        const objectAction = runtime.rewriteHead(kernelApplication(
            'functor-object',
            [
                { value: W },
                { value: Z },
                { value: point.after },
                { value: a }
            ],
            p
        ));
        const arrowAction = runtime.rewriteHead(kernelApplication(
            'functor-hom-capped',
            [
                { value: W },
                { value: Z },
                { value: point.after },
                { value: a },
                { value: aPrime },
                { value: alpha }
            ],
            p
        ));

        assert.equal(objectAction.status, 'rewritten');
        assert.equal(arrowAction.status, 'rewritten');
        if (
            objectAction.status === 'rewritten' &&
            arrowAction.status === 'rewritten'
        ) {
            assert.match(
                serializeCoreExpression(objectAction.after),
                /functor-object/u
            );
            assert.match(
                serializeCoreExpression(arrowAction.after),
                /functor-hom-capped/u
            );
        }
    });

    it('pins the current active kernel bytes and owner package', () => {
        const source = readFileSync(activeKernelPath, 'utf8');
        assert.equal(
            'sha256:' + createHash('sha256')
                .update(source)
                .digest('hex'),
            CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256
        );
        assert.match(
            source,
            /injective symbol Functor_comp_pair_funcd/u
        );
        assert.match(
            source,
            /rule @tapp1_fapp0[\s\S]*@Functor_comp_pair_funcd/u
        );
    });
});
