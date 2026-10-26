/**
 * Existing-authority transfer evidence for FIBRED-DEPENDENT-TARGET-1.
 */

import assert from 'node:assert/strict';
import { KernelExpression, kernelFree, kernelExpressionEquals, provenance } from '../src/v3_2/kernel';
import {
    describe,
    it
} from 'node:test';
import {
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_MODULE,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_MODULE,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE,
    CoreLfTransferExpression,
    compileCoreCategoricalFibredDependentTargetTransfer,
    validateCoreCategoricalFibredDependentTargetContract
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

const wildcardWitnesses = (
    expression: CoreLfTransferExpression
): readonly CoreLfTransferExpression[] => {
    switch (expression.tag) {
        case 'wildcard':
            return expression.checking === undefined
                ? []
                : [expression.checking];
        case 'call':
            return [
                ...wildcardWitnesses(expression.callee),
                ...expression.arguments.flatMap(argument =>
                    wildcardWitnesses(argument.value)
                )
            ];
        case 'pi':
        case 'lambda':
            return [
                ...wildcardWitnesses(expression.binder.type),
                ...wildcardWitnesses(expression.body)
            ];
        case 'type':
        case 'bound':
        case 'global':
        case 'capture':
            return [];
        default: {
            const exhaustive: never = expression;
            return exhaustive;
        }
    }
};

describe(
    'FIBRED-DEPENDENT-TARGET-1 existing-authority transfer',
    () => {
        it('freezes the exact eleven/eleven/one no-new-mathematics contract', () => {
            validateCoreCategoricalFibredDependentTargetContract();
            assertDeepFrozen(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT
            );
            assert.deepEqual(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE
                    .declarations.map(entry => entry.symbol.name),
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT
                    .transfer.declarations
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .declarationCount,
                11
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .runtimeRuleCount,
                11
            );
            assert.deepEqual(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .inheritedRuntimeRuleIds,
                ['categorical.displayed-hom-category.reduce']
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .proofRuleIds.length,
                1
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .newMathematicalOwnerCount,
                0
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY
                    .proofSubjectExternalOracleUsed,
                false
            );
        });

        it('retains the exact active wildcard with a typed checking witness', () => {
            const rule =
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_MODULE
                    .runtimeRules.find(candidate =>
                        candidate.id ===
                            'categorical.dependent-target.' +
                            'section-functor-object'
                    );
            assert.ok(rule);
            assert.equal(
                wildcardWitnesses(rule.left).length,
                1
            );
            assertDeepFrozen(rule);
        });

        it('checks nine local runtime subjects directly and two by proof', () => {
            const compilation =
                compileCoreCategoricalFibredDependentTargetTransfer();
            assert.deepEqual(
                compilation.compiled.declarations.map(declaration => ({
                    name: declaration.symbol.name,
                    status: declaration.status,
                    hasBody: declaration.body !== undefined
                })),
                [
                    {
                        name: 'Hom',
                        status: 'intrinsic-transparent',
                        hasBody: true
                    },
                    {
                        name: 'Op_cat',
                        status: 'installed-opaque',
                        hasBody: false
                    },
                    {
                        name: 'Functord',
                        status: 'installed-transparent',
                        hasBody: true
                    },
                    {
                        name: 'Functor_cat_func',
                        status: 'installed-opaque',
                        hasBody: false
                    },
                    {
                        name: 'Functor_cat_fapp0_func',
                        status: 'installed-opaque',
                        hasBody: false
                    },
                    { name: 'hom_con', status: 'installed-opaque', hasBody: false },
                    { name: 'Functor_cart_include', status: 'installed-opaque', hasBody: false },
                    {
                        name: 'Catd_cat_func',
                        status: 'installed-transparent',
                        hasBody: true
                    },
                    {
                        name: 'Pi_func',
                        status: 'installed-opaque',
                        hasBody: false
                    },
                    {
                        name: 'Pi_int_funcd',
                        status: 'installed-opaque',
                        hasBody: false
                    },
                    {
                        name: 'Pi_pullback_funcd',
                        status: 'installed-opaque',
                        hasBody: false
                    }
                ]
            );
            const prerequisite =
                compilation.prerequisiteRuntimeFragment.localProgram.rules;
            const consumer =
                compilation.consumerRuntimeFragment.localProgram.rules;
            assert.deepEqual(
                prerequisite.map(rule => rule.subjectValidation.kind),
                Array.from({ length: 8 }, () => 'typescript-checked')
            );
            assert.deepEqual(
                consumer.map(rule => rule.subjectValidation.kind),
                [
                    'typescript-proof-checked',
                    'typescript-checked',
                    'typescript-proof-checked'
                ]
            );
            assert.deepEqual(
                consumer.flatMap(rule =>
                    rule.subjectValidation.kind ===
                        'typescript-proof-checked'
                        ? [{
                            runtimeRuleId: rule.id,
                            proofRuleIds:
                                rule.subjectValidation.proofRuleIds
                        }]
                        : []
                ),
                [
                    {
                        runtimeRuleId:
                            'categorical.dependent-target.' +
                            'package-component',
                        proofRuleIds: [
                            'categorical.dependent-target.' +
                            'category-presentation'
                        ]
                    },
                    {
                        runtimeRuleId:
                            'categorical.dependent-target.' +
                            'pullback-component',
                        proofRuleIds: [
                            'categorical.dependent-target.' +
                            'category-presentation'
                        ]
                    }
                ]
            );
            assert.deepEqual(
                compilation.proofProgram.ruleIds,
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE
                    .proofRules.map(rule => rule.id)
            );
            assert.equal(
                compilation.proofProgram.declarations.environment,
                compilation.compiled.environment
            );
            assert.equal(
                compilation.composedRuntime.ruleIds.includes(
                    'categorical.dependent-target.' +
                        'category-presentation'
                ),
                false
            );
            assert.equal(
                compilation.composedRuntime.ruleIds.filter(id =>
                    id === 'categorical.displayed-hom-category.reduce'
                ).length,
                1
            );
            assert.equal(
                [
                    ...prerequisite,
                    ...consumer
                ].some(rule =>
                    rule.id ===
                        'categorical.displayed-hom-category.reduce'
                ),
                false
            );
            assert.equal(
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_MODULE
                    .runtimeRules.length,
                3
            );
        });
    }
);

it('projects pulled Pi after its inferred family alias has unfolded', () => {
    const c = compileCoreCategoricalFibredDependentTargetTransfer();
    const program = c.consumerRuntimeFragment.localProgram;
    const rule = program.rule('categorical.dependent-target.pullback-component');
    assert.ok(rule);
    const alias = c.compiled.declarations.find(d => d.symbol.name === 'Catd_cat_func');
    const link = c.compiled.linkage.entries.find(d => d.symbol.name === 'Catd_cat_func');
    assert.ok(alias?.body);
    assert.ok(link?.kind === 'free-declaration');
    const at = provenance('derived', 'unfolded inferred Pi family regression');
    const bindings = ['K', 'G', 'x'].map(name => kernelFree('pi_unfold_' + name, at));
    const redex = program.instantiateRuleLeft(rule, bindings, at);
    const expand = (term: KernelExpression): KernelExpression => {
        if (term.tag === 'reference' && term.name === link.coreName) return alias.body;
        if (term.tag === 'application') return { ...term,
            arguments: term.arguments.map(arg => ({ ...arg, value: expand(arg.value) })) };
        if (term.tag === 'call') return { ...term, callee: expand(term.callee),
            arguments: term.arguments.map(arg => ({ ...arg, value: expand(arg.value) })) };
        return term;
    };
    assert.equal(redex.tag, 'application');
    if (redex.tag !== 'application') return;
    const expanded = { ...redex, arguments: redex.arguments.map((arg, index) =>
        index === 2 ? { ...arg, value: expand(arg.value) } : arg) };
    assert.equal(kernelExpressionEquals(redex, expanded), false);
    const original = program.rewriteHead(redex), projected = program.rewriteHead(expanded);
    assert.equal(original.status, 'rewritten');
    assert.equal(projected.status, 'rewritten');
    if (original.status === 'rewritten' && projected.status === 'rewritten') {
        assert.equal(kernelExpressionEquals(original.after, projected.after), true);
    }
    const wrongCoefficient = { ...expanded, arguments: expanded.arguments.map((arg, index) =>
        index === 1 ? { ...arg, value: kernelFree('pi_unfold_wrong_coefficient', at) } : arg) };
    assert.equal(program.matchRule(wrongCoefficient, rule), undefined);
});
