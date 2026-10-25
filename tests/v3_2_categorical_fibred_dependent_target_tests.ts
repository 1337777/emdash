/**
 * End-user dependent-target and total-context eta evidence.
 */

import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import {
    describe,
    it
} from 'node:test';
import {
    CoreCategoricalFrontendError,
    CoreCategoricalProgram,
    CoreCategoricalProgramError,
    compileCoreCategoricalFibredDependentTargetTransfer,
    checkLambdapiProbe,
    serializeKernelExpression,
    kernelFree,
    provenance
} from '../src/v3_2';

describe('FIBRED-DEPENDENT-TARGET-1 TypeScript profile', () => {
    it('checks the whole Pi inclusion and emitted dependent target in Lambdapi', {
        skip: process.env.EMDASH_RUN_LAMBDAPI_CATEGORICAL_PI_PROBES !== '1'
    }, () => {
        const e = new CoreCategoricalProgram({ sourceFile: 'native-pi.ts', profile: 'fibred-dependent-target-1' });
        const K = e.category('K'), G = e.contravariantCategoryFamily('G', K);
        const motive = e.dependentSectionMotive(G), target = e.dependentSectionTarget(G);
        const k = e.object('k', K), M = e.object('M', e.fibre(motive, k));
        const actual = e.fibre(target, e.dependentPair(motive, k, M));
        const expected = e.dependentSectionCategoryAt(G, k, M);
        const actualObject = e.compile(e.object('w', actual));
        const expectedObject = e.compile(e.object('z', expected));
        const section = e.compile(e.section('s', target));
        const c = compileCoreCategoricalFibredDependentTargetTransfer();
        const weaken = c.prerequisite, transfd = weaken.prerequisite, binder = transfd.prerequisite;
        const structure = binder.prerequisite, product = structure.prerequisite;
        const comprehension = product.prerequisite, composition = comprehension.prerequisite;
        const dependent = composition.dependent, structural = dependent.structural;
        const modules = [structural.initialDeclarations, structural.compiled, dependent.compiled,
            composition.compiled, comprehension.compiled, product.compiled, structure.compiled,
            binder.compiled, transfd.compiled, weaken.compiled, c.compiled];
        const references = Object.assign({}, ...modules.flatMap(module => [
            module.externalFreeReferences, module.externalTransparentDefinitions
        ]));
        const serialize = (term: Parameters<typeof serializeKernelExpression>[0]) =>
            serializeKernelExpression(term, { externalFreeReferences: references });
        const site = provenance('derived', 'native whole Pi component');
        const componentAssertions = c.consumerRuntimeFragment.localProgram.rules
            .filter(rule => rule.id.endsWith('component')).map(rule => {
                const left = c.consumerRuntimeFragment.localProgram.instantiateRuleLeft(rule,
                    rule.variables.map(v => kernelFree(v.name === 'x' ? 'k' : v.name, site)), site);
                const result = c.consumerRuntimeFragment.localProgram.rewriteHead(left);
                assert.equal(result.status, 'rewritten');
                if (result.status !== 'rewritten') throw new Error('Missing Pi component projection');
                assert.equal(result.ruleId, rule.id);
                return `assert ⊢ ${serialize(left)} ≡ ${serialize(result.after)};`;
            });
        const source = [
            'require open emdash.emdash3_2;',
            'symbol K : Cat;', 'symbol G : τ (Functor K (Op_cat Cat_cart));',
            'symbol k : τ (Obj K);',
            'symbol M : τ (Functor (@fapp0 K (Op_cat Cat_cart) G k) Cat_cart);',
            `symbol w : ${serialize(actualObject.expectedType)};`,
            `assert ⊢ w : ${serialize(expectedObject.expectedType)};`,
            `assert ⊢ ${serialize(actualObject.expectedType)} ≡ ${serialize(expectedObject.expectedType)};`,
            `symbol s : ${serialize(section.expectedType)};`,
            `assert ⊢ ${serialize(section.explicitTerm)} : ${serialize(section.expectedType)};`,
            ...componentAssertions,
            'assertnot ⊢ Functor_cart_cat K Cat_cart ≡ Catd_cat K;'
        ].join('\n');
        assert.doesNotMatch(source, /dttlf_|emdash_v3_2_/);
        const result = checkLambdapiProbe({ source, sourceMap: [] }, {
            packageRoot: resolve(__dirname, '../emdash2'), timeoutMs: 60_000
        });
        assert.equal(result.accepted, true, result.diagnostics + '\n' + source);
        assert.equal(result.timedOut, false);
    });

    it(
        'computes B[k,M] to Pi(G[k],M) and checks total-context eta',
        () => {
            const emdash = new CoreCategoricalProgram({
                sourceFile:
                    'tests/fixtures/fibred-dependent-target.ts',
                profile: 'fibred-dependent-target-1'
            });
            const K = emdash.category('K', { line: 1 });
            const G = emdash.contravariantCategoryFamily(
                'G',
                K,
                { line: 2 }
            );
            const motive = emdash.dependentSectionMotive(
                G,
                { line: 3 }
            );
            const target = emdash.dependentSectionTarget(
                G,
                { line: 4 }
            );
            const k = emdash.object('k', K, { line: 5 });
            const M = emdash.object(
                'M',
                emdash.fibre(motive, k),
                { line: 6 }
            );
            const pair = emdash.dependentPair(
                motive,
                k,
                M,
                { line: 7 }
            );
            const actual = emdash.fibre(target, pair, { line: 8 });
            const expected = emdash.dependentSectionCategoryAt(
                G,
                k,
                M,
                { line: 9 }
            );
            const compatibility =
                emdash.dependentTargetCategoryCompatibility(
                    actual,
                    expected
                );

            assert.equal(compatibility.runtime.status, 'equal');
            assert.equal(compatibility.proofTime.status, 'solved');
            assert.equal(
                compatibility
                    .runtimeCategoryPresentationCollapseInstalled,
                false
            );
            assert.equal(
                compatibility.runtime.trace.some(entry =>
                    entry.reduction.kind === 'runtime' &&
                    entry.reduction.ruleId ===
                        'categorical.dependent-target.' +
                        'section-functor-object'
                ),
                true
            );
            assert.equal(
                compatibility.runtime.trace.some(entry =>
                    entry.reduction.kind === 'runtime' &&
                    entry.reduction.ruleId ===
                        'categorical.dependent-target.' +
                        'category-presentation'
                ),
                false
            );
            assert.match(
                emdash.serializeCategory(expected),
                /section-category/u
            );

            const section = emdash.section(
                'target_section',
                target,
                { line: 12 }
            );
            let callbackCount = 0;
            const eta = emdash.dependentLambda(
                'z',
                target,
                z => {
                    callbackCount += 1;
                    return emdash.apply(section, z, {
                        expectedShape: 'dependent-object',
                        source: { line: 16 }
                    });
                },
                {
                    variation: 'natural',
                    dependency: 'displayed',
                    source: { line: 14 }
                }
            );
            const compilation = emdash.compile(eta);
            assert.equal(callbackCount, 1);
            assert.equal(
                compilation.explicitCore,
                '(free "target_section")'
            );
            assert.equal(
                compilation.explicitInferredType,
                compilation.explicitExpectedType
            );
            assert.match(
                compilation.explicitExpectedType,
                /dttlf_Sigma_catd_functord_catd/u
            );
            assert.equal(
                compilation.productionLambdapiDependency,
                false
            );

            const wrongTarget = emdash.functor('wrong_G', K, K);
            assert.throws(
                () => emdash.dependentSectionMotive(wrongTarget),
                error =>
                    error instanceof CoreCategoricalProgramError &&
                    error.code === 'EXPECTED_FUNCTOR' &&
                    /Op\(Cat_cart\)/u.test(error.message)
            );
            assert.throws(
                () => emdash.dependentSectionCategoryAt(
                    G,
                    k,
                    emdash.object('wrong_M', K)
                ),
                error =>
                    error instanceof CoreCategoricalProgramError &&
                    error.code === 'EXPECTED_CATEGORY_OBJECT'
            );

            const total = emdash.totalCategory(motive);
            const otherTarget =
                emdash.displayedFamily('other_target', total);
            const otherSection =
                emdash.section('other_section', otherTarget);
            assert.throws(
                () => emdash.dependentLambda(
                    'z',
                    target,
                    z => emdash.apply(otherSection, z, {
                        expectedShape: 'dependent-object'
                    })
                ),
                error =>
                    error instanceof CoreCategoricalFrontendError &&
                    error.code === 'CLASSIFIER_ARGUMENT_MISMATCH'
            );
        }
    );

    it('keeps the dependent target out of earlier frozen profiles', () => {
        const emdash = new CoreCategoricalProgram();
        const K = emdash.category('K');
        assert.throws(
            () => emdash.contravariantCategoryFamily('G', K),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'UNAVAILABLE_DEPENDENT_TARGET'
        );
    });
});
