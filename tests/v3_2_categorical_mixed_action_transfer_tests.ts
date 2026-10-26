/**
 * MIXED-NEST-ACTION-0B existing-authority transfer and typed-consumer
 * evidence.
 */

import assert from 'node:assert/strict';
import {
    describe,
    it
} from 'node:test';
import {
    CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE,
    CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_POLICY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE,
    compileCoreCategoricalMixedActionTransfer
} from '../src/v3_2/categorical_mixed_action_transfer';
import { CoreCategoricalProgram, CoreCategoricalProgramError } from '../src/v3_2/categorical_program';
import { kernelApplication, kernelCall, kernelFree, provenance, KernelExpression } from '../src/v3_2/kernel';
import { coreLfDefinitionalCompare } from '../src/v3_2/lf_conversion';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';

const assertDeepFrozen = (value: unknown): void => {
    if (value === null || typeof value !== 'object') return;
    assert.equal(Object.isFrozen(value), true);
    Reflect.ownKeys(value).forEach(key =>
        assertDeepFrozen(
            (value as Record<PropertyKey, unknown>)[key]
        )
    );
};

describe('MIXED-NEST-ACTION-0B', () => {
    it('pins the measured existing-authority closure', () => {
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .declarationNames,
            ['Homd_index_cat', 'homd_index_presheaf', 'Functor_cart_component_func',
                'fib_cov_tapp0_func', 'homd_', 'Functor_catd_fapp0_func',
                'Homd_target_section_cat', 'homd_src_sec', 'homd_src_func', 'homd_tgt_func']
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .declarationCount,
            10
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .runtimeRuleCount,
            15
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .reusedProofRuleCount,
            0
        );
        assert.deepEqual(
            [
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .activeLambdapiOwnerDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .activeLambdapiRuleDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .intrinsicCoreOwnerDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .ownerSpecificCheckerOrEvaluatorDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .externalCoherenceEvidenceDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .nestedAbstractionLowererDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .textOrBrowserDelta
            ],
            [0, 0, 0, 0, 0, 0, 0]
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE
                .declarations.length,
            10
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE
                .runtimeRules.length,
            15
        );
        assertDeepFrozen(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
        );
    });

    it('subject-checks every declaration and rule generically', () => {
        const compilation =
            compileCoreCategoricalMixedActionTransfer();
        assert.equal(compilation.initialCompiled.declarations.length, 7);
        assert.equal(compilation.compiled.declarations.length, 3);
        assert.equal(compilation.runtime.rules.length, 15);
        assert.equal(
            compilation.runtime.rules.every(rule =>
                rule.subjectValidation.kind === 'typescript-checked'
            ),
            true
        );
        assert.deepEqual(
            compilation.composedRuntime.ruleIds.slice(-15),
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .runtimeRuleIds
        );
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_POLICY.entries.map(
                entry => entry.policy
            ),
            Array.from({length:10}, (_,i) => i === 5 ? 'opaque-signature' : 'checked-transparent-definition')
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY.entries.every(
                entry => entry.policy === 'runtime-rewrite'
            ),
            true
        );
    });

    it('computes native root/section projections and the independent endpoint leaf', () => {
        const c=compileCoreCategoricalMixedActionTransfer();
        const at=provenance('derived','native Homd ladder projections');
        const names=['K','D','E','FF','x','u','y','v','f'] as const;
        const [K,D,E,FF,x,u,y,v,f]=names.map(name=>kernelFree(name,at));
        const call=(name:string,args:readonly KernelExpression[]=[],implicitCount=0):KernelExpression=>{
            const link=CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE.entries.find(l=>l.symbol.name===name);
            assert.ok(link,`Missing ${name}`);
            return link.kind==='core-owner' ? kernelApplication(link.owner,args.map(value=>({value})),at)
                : args.length === 0 ? kernelFree(link.coreName,at)
                : kernelCall(kernelFree(link.coreName,at),args.map((value,index)=>({value,plicity:index<implicitCount?'implicit':'explicit'})),at);
        };
        const Cart=call('Cat_cart'),Q=call('Homd_coeff_cat');
        const op=(A:KernelExpression)=>call('Op_cat',[A]);
        const hom=(C:KernelExpression,a:KernelExpression,b:KernelExpression)=>call('Hom_cat',[C,a,b]);
        const app=(A:KernelExpression,B:KernelExpression,F:KernelExpression,z:KernelExpression)=>call('fapp0',[A,B,F,z],2);
        const fib=(A:KernelExpression,z:KernelExpression)=>app(K,Cart,A,z);
        const diagram=(A:KernelExpression)=>call('Homd_coeff_diagram',[K,A],1);
        const IX=call('hom_',[K,K,call('id_func',[K],1),x],2);
        const diagramCategory=call('Functor_cat',[K,Q]);
        const target=app(op(call('CoAt2_cat',[diagramCategory])),call('Functor_cart_cat',[K,Cart]),
            call('Homd_target_index_func',[K]),diagram(D));
        const root=call('homd_int',[K,D,E,FF],3);
        const source=call('homd_src_func',[K,D,E,FF,x],3);
        const section=call('homd_src_sec',[K,D,E,FF,x,u],3);
        const tgt=call('homd_tgt_func',[K,D,E,FF,x,u,y],3);
        const equal=(a:KernelExpression,b:KernelExpression)=>{
            const result=coreLfDefinitionalCompare(c.compiled.environment,a,b,1024,undefined,c.composedRuntime);
            const details = 'normalizedLeft' in result
                ? serializeKernelExpression(result.normalizedLeft)+'\nvs\n'+serializeKernelExpression(result.normalizedRight)
                : result.status;
            assert.equal(result.status,'equal',details);
        };
        equal(source,call('tapp0_fapp0',[K,Cart,E,target,x,root],4));
        equal(app(fib(E,x),op(call('Homd_target_section_cat',[K,D,x],1)),source,u),section);
        equal(tgt,call('tapp0_fapp0',[K,Q,diagram(D),diagram(IX),y,section],4));
        const endpoint=call('homd_',[K,D,E,FF,x,u,y,v],3);
        const component=call('tapp0_fapp0',[K,Cart,D,E,y,FF],4);
        const transport=kernelApplication('functor-hom-capped',[{value:K},{value:Cart},{value:E},
            {value:x},{value:y},{value:f}],at);
        equal(app(op(hom(K,x,y)),Cart,endpoint,f),hom(fib(E,y),app(fib(E,x),fib(E,y),transport,u),
            app(fib(D,y),fib(E,y),component,v)));
    });

    it('exposes typed internal-hom and endpoint-family consumers', () => {
        const emdash = new CoreCategoricalProgram({
            sourceFile: 'tests/fixtures/categorical-mixed-action.ts',
            profile: 'fibred-displayed-mixed-nest-1'
        });
        const K = emdash.category('mixed_action_program_K');
        const D = emdash.displayedFamily(
            'mixed_action_program_D',
            K
        );
        const E = emdash.displayedFamily(
            'mixed_action_program_E',
            K
        );
        const FF = emdash.displayedFunctor(
            'mixed_action_program_FF',
            D,
            E
        );
        const x = emdash.object('mixed_action_program_x', K);
        const y = emdash.object('mixed_action_program_y', K);
        const u = emdash.object(
            'mixed_action_program_u',
            emdash.fibre(E, x)
        );
        const v = emdash.object(
            'mixed_action_program_v',
            emdash.fibre(D, y)
        );
        const internalHom = emdash.displayedInternalHom(FF);
        const endpoint = emdash.displayedInternalHomEndpointFamily(
            FF,
            x,
            u,
            y,
            v
        );
        const compiled = emdash.compile(internalHom);
        const endpointTotal = emdash.serializeCategory(
            emdash.totalCategory(endpoint)
        );
        assert.equal(compiled.surfaceType.tag, 'displayed-functor');
        assert.match(compiled.explicitCore, /homd_int/u);
        assert.match(endpointTotal, /homd_/u);
        assert.equal(compiled.productionLambdapiDependency, false);
    });

    it('keeps the consumers behind the mixed root profile', () => {
        const emdash = new CoreCategoricalProgram({
            profile: 'fibred-displayed-nd-higher-1'
        });
        const K = emdash.category('mixed_action_gate_K');
        const D = emdash.displayedFamily('mixed_action_gate_D', K);
        const E = emdash.displayedFamily('mixed_action_gate_E', K);
        const FF = emdash.displayedFunctor(
            'mixed_action_gate_FF',
            D,
            E
        );
        assert.throws(
            () => emdash.displayedInternalHom(FF),
            (error: unknown) =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'UNAVAILABLE_MIXED_MODE'
        );
    });
});
