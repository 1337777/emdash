/**
 * End-user FIBRED-WEAKEN-REINDEX-1 surface evidence.
 */

import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import {
    describe,
    it
} from 'node:test';
import {
    CoreCategoricalProgram,
    CoreCategoricalProgramError,
    compileCoreCategoricalFibredWeakenReindexTransfer,
    checkLambdapiProbe,
    serializeKernelExpression
} from '../src/v3_2';

const fixture = () => {
    const emdash = new CoreCategoricalProgram({
        sourceFile:
            'tests/fixtures/categorical-fibred-weaken-reindex.ts',
        profile: 'fibred-weaken-reindex-1'
    });
    const K = emdash.category('K', { line: 1 });
    const L = emdash.category('L', { line: 2 });
    const E = emdash.displayedFamily('E', K, { line: 3 });
    const D = emdash.displayedFamily('D', K, { line: 4 });
    const sigma = emdash.functor('sigma', L, K, { line: 5 });
    const FF = emdash.displayedFunctor('FF', E, D, { line: 6 });
    const s = emdash.section('s', D, { line: 7 });
    return {
        emdash,
        K,
        L,
        E,
        D,
        sigma,
        FF,
        s
    };
};

describe('FIBRED-WEAKEN-REINDEX-1 surface', () => {
    it('checks emitted weakening and reindexing against native owners', {
        skip: process.env.EMDASH_RUN_LAMBDAPI_CATEGORICAL_WEAKEN_PROBES !== '1'
    }, () => {
        const { emdash, K, L, E, D, sigma, FF, s } = fixture();
        const weakened = emdash.displayedFunctorLambda('a', E, D,
            a => emdash.apply(s, emdash.indexOf(a)));
        const k = emdash.object('k', K);
        const a = emdash.object('a0', emdash.fibre(E, k));
        const point = emdash.apply(emdash.apply(weakened, k), a);
        const pulled = emdash.pullbackDisplayedFunctor(FF, sigma);
        const x = emdash.object('x', L);
        const pulledComponent = emdash.apply(pulled, x);
        const terms = [weakened, point, pulled, pulledComponent].map(term => emdash.compile(term));
        const c = compileCoreCategoricalFibredWeakenReindexTransfer();
        const transfd = c.prerequisite, binder = transfd.prerequisite;
        const structure = binder.prerequisite, product = structure.prerequisite;
        const comprehension = product.prerequisite, composition = comprehension.prerequisite;
        const dependent = composition.dependent, structural = dependent.structural;
        const modules = [structural.initialDeclarations, structural.compiled,
            dependent.compiled, composition.compiled, comprehension.compiled,
            product.compiled, structure.compiled, binder.compiled, transfd.compiled, c.compiled];
        const references = Object.assign({}, ...modules.flatMap(module => [
            module.externalFreeReferences, module.externalTransparentDefinitions
        ]));
        const serialize = (term: Parameters<typeof serializeKernelExpression>[0]) =>
            serializeKernelExpression(term, { externalFreeReferences: references });
        const source = [
            'require open emdash.emdash3_2;',
            'symbol K : Cat;', 'symbol L : Cat;',
            'symbol E : τ (Catd K);', 'symbol D : τ (Catd K);',
            'symbol sigma : τ (Functor L K);', 'symbol FF : τ (Functord E D);',
            'symbol s : τ (Obj (Pi_cat D));', 'symbol k : τ (Obj K);',
            'symbol a0 : τ (Obj (Fibre_cat E k));', 'symbol x : τ (Obj L);',
            ...terms.map(term => `assert ⊢ ${serialize(term.explicitTerm)} : ${serialize(term.expectedType)};`),
            `assert ⊢ ${serialize(terms[0].explicitTerm)} ≡ @section_weaken_funcd K E D s;`,
            `assert ⊢ ${serialize(terms[1].explicitTerm)} ≡ @piapp0 K D s k;`,
            `assert ⊢ ${serialize(terms[3].explicitTerm)} ≡ @Fibre_func K E D FF (@fapp0 L K sigma x);`,
            'assertnot ⊢ @Pullback_catd (@Sigma_cat K E) K D (@Sigma_proj1_func K E) ≡ @Sigma_proj1_pullback_catd K E D;'
        ].join('\n');
        assert.doesNotMatch(source, /dttlf_|emdash_v3_2_/);
        const result = checkLambdapiProbe({ source, sourceMap: [] }, {
            packageRoot: resolve(__dirname, '../emdash2'), timeoutMs: 60_000
        });
        assert.equal(result.accepted, true, result.diagnostics + '\n' + source);
        assert.equal(result.timedOut, false);
    });

    it('lowers λ a :^fd E. s[indexOf(a)] and computes its point', () => {
        const {
            emdash,
            K,
            E,
            D,
            s
        } = fixture();
        const weakened = emdash.displayedFunctorLambda(
            'a',
            E,
            D,
            a => emdash.apply(s, emdash.indexOf(a)),
            { source: { line: 10 } }
        );
        const compiled = emdash.compile(weakened);
        assert.equal(
            compiled.abstractions.at(-1)?.rule,
            'categorical.displayed-functor-weakening'
        );
        assert.match(
            compiled.explicitCore,
            /emdash\.categorical\.section-weakening/u
        );
        assert.doesNotMatch(compiled.explicitCore, /sigma-first-projection|section-pullback/u);
        const compatibility =
            emdash.displayedFunctorClassifierCompatibility(E, D);
        assert.equal(compatibility.runtime.status, 'not-equal');
        assert.equal(compatibility.proofTime.status, 'solved');
        assert.equal(
            compatibility.proofTime.ruleApplications[0]?.ruleId,
            'stress.sigma-pi.uncurrying'
        );

        const k = emdash.object('k', K, { line: 11 });
        const Ek = emdash.fibre(E, k, { line: 12 });
        const a = emdash.object('a0', Ek, { line: 13 });
        const value = emdash.apply(
            emdash.apply(
                weakened,
                k,
                { expectedShape: 'fibre-functor' }
            ),
            a,
            { expectedShape: 'object-value' }
        );
        const direct = emdash.apply(
            s,
            k,
            { expectedShape: 'dependent-object' }
        );
        assert.equal(
            emdash.compile(value).explicitCore,
            emdash.compile(direct).explicitCore
        );
        assert.equal(emdash.compare(value, direct).status, 'equal');
    });

    it('reindexes a displayed functor and computes its base component', () => {
        const {
            emdash,
            L,
            E,
            D,
            sigma,
            FF
        } = fixture();
        const pulled = emdash.pullbackDisplayedFunctor(
            FF,
            sigma,
            { line: 20 }
        );
        const compiled = emdash.compile(pulled);
        assert.match(
            compiled.explicitCore,
            /emdash\.categorical\.displayed-pullback-functor/u
        );
        assert.match(compiled.explicitCore, /functor-hom-capped/u);

        const x = emdash.object('x', L, { line: 21 });
        const sigmaX = emdash.apply(sigma, x);
        const pulledAtX = emdash.apply(
            pulled,
            x,
            { expectedShape: 'fibre-functor' }
        );
        const originalAtSigmaX = emdash.apply(
            FF,
            sigmaX,
            { expectedShape: 'fibre-functor' }
        );
        const comparison = emdash.compare(
            pulledAtX,
            originalAtSigmaX,
            4_000
        );
        assert.equal(comparison.status, 'equal');
        assert.ok(
            comparison.trace.some(entry =>
                entry.reduction.kind === 'runtime' &&
                entry.reduction.ruleId ===
                    'categorical.weaken-reindex.' +
                    'pullback-hom-component'
            )
        );
    });

    it('commutes with the supported direct eta abstraction', () => {
        const {
            emdash,
            E,
            D,
            sigma,
            FF
        } = fixture();
        const before = emdash.pullbackDisplayedFunctor(
            emdash.displayedFunctorLambda(
                'a',
                E,
                D,
                a => emdash.apply(FF, a),
                { source: { line: 30 } }
            ),
            sigma,
            { line: 31 }
        );
        const pulledE = emdash.pullbackFamily(E, sigma, { line: 32 });
        const pulledD = emdash.pullbackFamily(D, sigma, { line: 33 });
        const pulledFF = emdash.pullbackDisplayedFunctor(
            FF,
            sigma,
            { line: 34 }
        );
        const after = emdash.displayedFunctorLambda(
            'a',
            pulledE,
            pulledD,
            a => emdash.apply(pulledFF, a),
            { source: { line: 35 } }
        );
        assert.equal(
            emdash.compile(before).explicitCore,
            emdash.compile(after).explicitCore
        );
    });

    it('fails closed outside the profile and on a wrong base', () => {
        const {
            emdash,
            L,
            E,
            D,
            FF
        } = fixture();
        const wrong = emdash.functor('wrong', L, L, { line: 40 });
        assert.throws(
            () => emdash.pullbackDisplayedFunctor(FF, wrong),
            (error: unknown) =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'DISPLAYED_BASE_MISMATCH'
        );

        const earlier = new CoreCategoricalProgram({
            profile: 'fibred-grouped-sequential-1'
        });
        const K0 = earlier.category('K0');
        const E0 = earlier.displayedFamily('E0', K0);
        const D0 = earlier.displayedFamily('D0', K0);
        const FF0 = earlier.displayedFunctor('FF0', E0, D0);
        const sigma0 = earlier.functor('sigma0', K0, K0);
        assert.throws(
            () => earlier.pullbackDisplayedFunctor(FF0, sigma0),
            (error: unknown) =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'UNAVAILABLE_WEAKEN_REINDEX'
        );
    });
});
