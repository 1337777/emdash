/**
 * DISPLAYED-CHAIN-2A three-level mixed contextual consumer evidence.
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
    CoreCategoricalSlotToken,
    CoreCategoricalTerm,
    CoreLfComparisonResult,
    serializeCoreCategoricalExpression,
    serializeKernelExpression,
    compileCoreCategoricalDisplayedChain2aClosureRuntime,
    checkLambdapiProbe
} from '../src/v3_2';

const runtimeRuleIds = (
    result: CoreLfComparisonResult
): readonly string[] => result.trace.flatMap(entry =>
    entry.reduction.kind === 'runtime'
        ? [entry.reduction.ruleId]
        : []
);

const fixture = () => {
    const emdash = new CoreCategoricalProgram({
        sourceFile:
            'tests/fixtures/categorical-displayed-chain-2a.ts',
        profile: 'fibred-displayed-chain-2a'
    });
    const K = emdash.category('K', { line: 1 });
    const A = emdash.displayedFamily('A', K, { line: 2 });
    const sigmaA = emdash.totalCategory(A, { line: 3 });
    const B = emdash.displayedFamily('B', sigmaA, { line: 4 });
    const C = emdash.displayedFamily('C', sigmaA, { line: 5 });
    const P = emdash.displayedProduct(B, C, { line: 6 });
    const sigmaP = emdash.totalCategory(P, { line: 7 });
    const D = emdash.displayedFamily('D', sigmaP, { line: 8 });
    const projectionA = emdash.sigmaProjection(A, { line: 9 });
    const liftedA1 = emdash.pullbackFamily(
        A,
        projectionA,
        { line: 10 }
    );
    const projectionP = emdash.sigmaProjection(P, { line: 11 });
    const liftedA2 = emdash.pullbackFamily(
        liftedA1,
        projectionP,
        { line: 12 }
    );
    const liftedB = emdash.pullbackFamily(
        B,
        projectionP,
        { line: 13 }
    );
    const liftedC = emdash.pullbackFamily(
        C,
        projectionP,
        { line: 14 }
    );
    const liftedProduct = emdash.displayedProduct(
        liftedB,
        liftedC,
        { line: 15 }
    );
    const bindings = [
        { name: 'a', family: A },
        { name: 'b', family: B },
        { name: 'c', family: C },
        { name: 'd', family: D }
    ] as const;
    const grouped = emdash.groupedSequentialContext(
        'ka',
        sigmaA,
        [
            { name: 'b', family: B },
            { name: 'c', family: C }
        ],
        { line: 16 }
    );
    return {
        emdash,
        K,
        A,
        sigmaA,
        B,
        C,
        P,
        sigmaP,
        D,
        liftedA2,
        liftedB,
        liftedC,
        liftedProduct,
        bindings,
        grouped
    };
};

const abstractions = (
    value: ReturnType<typeof fixture>,
    countCallbacks = false
) => {
    const {
        emdash,
        bindings,
        liftedA2,
        liftedB,
        liftedC,
        liftedProduct,
        D
    } = value;
    let callbackCount = 0;
    const body = (
        build: (
            tokens: readonly CoreCategoricalSlotToken[]
        ) => ReturnType<typeof emdash.fibrePair> | CoreCategoricalSlotToken
    ) => (tokens: readonly CoreCategoricalSlotToken[]) => {
        if (countCallbacks) callbackCount += 1;
        return build(tokens);
    };
    const a = emdash.displayedDependentContextLambda(
        bindings,
        liftedA2,
        body(([a]) => a)
    );
    const b = emdash.displayedDependentContextLambda(
        bindings,
        liftedB,
        body(([, b]) => b)
    );
    const c = emdash.displayedDependentContextLambda(
        bindings,
        liftedC,
        body(([, , c]) => c)
    );
    const d = emdash.displayedDependentContextLambda(
        bindings,
        D,
        body(([, , , d]) => d)
    );
    const pair = emdash.displayedDependentContextLambda(
        bindings,
        liftedProduct,
        body(([, b, c]) => emdash.fibrePair(b, c))
    );
    return {
        a,
        b,
        c,
        d,
        pair,
        callbackCount
    };
};

const makePoint = (
    value: ReturnType<typeof fixture>,
    suffix: string
) => {
    const {
        emdash,
        K,
        A,
        B,
        C,
        D,
        grouped
    } = value;
    const k = emdash.object(`k${suffix}`, K);
    const a = emdash.object(
        `a${suffix}`,
        emdash.fibre(A, k)
    );
    const ka = emdash.dependentPair(A, k, a);
    const b = emdash.object(
        `b${suffix}`,
        emdash.fibre(B, ka)
    );
    const c = emdash.object(
        `c${suffix}`,
        emdash.fibre(C, ka)
    );
    const product = emdash.groupedSequentialObject(
        grouped,
        ka,
        [b, c]
    );
    const d = emdash.object(
        `d${suffix}`,
        emdash.fibre(D, product.groupedObject)
    );
    return {
        k,
        a,
        ka,
        b,
        c,
        product,
        d
    };
};

const applyAt = (
    value: ReturnType<typeof fixture>,
    abstraction: CoreCategoricalTerm,
    point: ReturnType<typeof makePoint>
) => value.emdash.apply(
    value.emdash.apply(
        abstraction,
        point.product.groupedObject,
        { expectedShape: 'fibre-functor' }
    ),
    point.d
);

describe('DISPLAYED-CHAIN-2A mixed contextual consumer', () => {
    it('checks emitted three-level maps and paired internal action in Lambdapi', {
        skip: process.env.EMDASH_RUN_LAMBDAPI_CATEGORICAL_CHAIN2_PROBES !== '1'
    }, () => {
        const value = fixture(), e = value.emdash, maps = abstractions(value);
        const p0 = makePoint(value, '0'), p1 = makePoint(value, '1');
        const p = e.hom('p', value.K, p0.k, p1.k);
        const alpha = e.hom('alpha', e.fibre(value.A, p1.k),
            e.apply(e.familyTransport(value.A, p), p0.a), p1.a);
        const qA = e.sigmaArrow(value.A, p0.a, p1.a, p, alpha);
        const rho = e.hom('rho', e.fibre(value.P, p1.ka),
            e.apply(e.familyTransport(value.P, qA), p0.product.groupedFibreObject), p1.product.groupedFibreObject);
        const qP = e.sigmaArrow(value.P, p0.product.groupedFibreObject, p1.product.groupedFibreObject, qA, rho);
        const e0 = e.object('e0', e.fibre(value.D, p0.product.groupedObject));
        const terms = [maps.a, maps.pair, maps.d, applyAt(value, maps.pair, p0), p0.product.groupedFibreObject,
            e.displayedFunctorInternalCell(maps.pair, qP, p0.d),
            e.displayedFunctorInternalCell(maps.pair, qP, e0)].map(term => e.compile(term));
        const c = compileCoreCategoricalDisplayedChain2aClosureRuntime(), chain = c.prerequisite;
        const evaluation = chain.prerequisite, pi = evaluation.prerequisite, weaken = pi.prerequisite;
        const transfd = weaken.prerequisite, binder = transfd.prerequisite, structure = binder.prerequisite;
        const product = structure.prerequisite, comprehension = product.prerequisite;
        const composition = comprehension.prerequisite, dependent = composition.dependent, structural = dependent.structural;
        const modules = [structural.initialDeclarations, structural.compiled, dependent.compiled, composition.compiled,
            comprehension.compiled, product.compiled, structure.compiled, binder.compiled, transfd.compiled,
            weaken.compiled, pi.compiled, evaluation.prerequisiteCompiled, evaluation.compiled,
            chain.prerequisiteCompiled, chain.compiled, c.compiled];
        const references = Object.assign({}, ...modules.flatMap(module => [
            module.externalFreeReferences, module.externalTransparentDefinitions
        ]));
        const serialize = (term: Parameters<typeof serializeKernelExpression>[0]) =>
            serializeKernelExpression(term, { externalFreeReferences: references });
        const assumptions = [p0.k,p1.k,p0.a,p1.a,p0.b,p1.b,p0.c,p1.c,p0.d,p1.d,p,alpha,rho,e0].map(term => {
            const compiled = e.compile(term);
            assert.equal(compiled.explicitTerm.tag, 'reference');
            return `symbol ${serialize(compiled.explicitTerm)} : ${serialize(compiled.expectedType)};`;
        });
        const source = [
            'require open emdash.emdash3_2;',
            'symbol K : Cat;', 'symbol A : τ (Catd K);',
            'symbol B : τ (Catd (@Sigma_cat K A));', 'symbol C : τ (Catd (@Sigma_cat K A));',
            'symbol P : τ (Catd (@Sigma_cat K A)) ≔ @comp_cat_fapp0 (@Sigma_cat K A) (Product_cat Cat_cart Cat_cart) Cat_cart (@uncurry_func Cat_cart Cat_cart Cat_cart Product_cat_coeff_func) (Struct_sigma B C);',
            'symbol D : τ (Catd (@Sigma_cat (@Sigma_cat K A) P));',
            ...assumptions,
            ...terms.map(term => `assert ⊢ ${serialize(term.explicitTerm)} : ${serialize(term.expectedType)};`),
            `assert ⊢ ${serialize(terms[3].explicitTerm)} ≡ ${serialize(terms[4].explicitTerm)};`,
            `assert ⊢ ${serialize(terms[5].explicitTerm)} ≡ ${serialize(terms[6].explicitTerm)};`,
            `assertnot ⊢ ${serialize(terms[5].explicitTerm)} ≡ rho;`
        ].join('\n');
        assert.doesNotMatch(source, /dttlf_|emdash_v3_2_/);
        const result = checkLambdapiProbe({ source, sourceMap: [] }, {
            packageRoot: resolve(__dirname, '../emdash2'), timeoutMs: 60_000
        });
        assert.equal(result.accepted, true, result.diagnostics + '\n' + source);
        assert.equal(result.timedOut, false);
    });

    it('compiles the exact mixed telescope once with frozen evidence', () => {
        const value = fixture();
        const compiledAbstractions = abstractions(value, true);
        assert.equal(compiledAbstractions.callbackCount, 5);
        const compilation = value.emdash.compile(
            compiledAbstractions.pair
        );
        const evidence = compilation.abstractions.at(-1);
        assert.equal(
            evidence?.rule,
            'categorical.displayed-mixed-dependent-context-bracket'
        );
        if (
            evidence?.rule !==
                'categorical.displayed-mixed-dependent-context-bracket'
        ) {
            assert.fail('Missing mixed contextual evidence');
        }
        assert.deepEqual(
            evidence.bindingNames,
            ['a', 'b', 'c', 'd']
        );
        assert.deepEqual(evidence.siblingGroup, ['b', 'c']);
        assert.equal(evidence.contextSize, 4);
        assert.equal(
            evidence.contextRelation,
            'two-dependency-transitions-with-middle-siblings'
        );
        assert.equal(evidence.body.tag, 'typed-pair');
        assert.equal(Object.isFrozen(evidence), true);
        assert.equal(Object.isFrozen(evidence.body), true);
        assert.match(
            compilation.explicitCore,
            /emdash\.categorical\.displayed-product-pair/u
        );
        assert.equal(compilation.productionLambdapiDependency, false);
    });

    it('computes a, b, c, d, and the recursive sibling pair', () => {
        const value = fixture();
        const compiledAbstractions = abstractions(value);
        const point = makePoint(value, '0');
        const cases = [
            [compiledAbstractions.a, point.a],
            [compiledAbstractions.b, point.b],
            [compiledAbstractions.c, point.c],
            [compiledAbstractions.d, point.d],
            [
                compiledAbstractions.pair,
                point.product.groupedFibreObject
            ]
        ] as const;
        for (const [abstraction, expected] of cases) {
            assert.equal(
                value.emdash.compare(
                    applyAt(value, abstraction, point),
                    expected,
                    60_000
                ).status,
                'equal'
            );
        }
    });

    it('recurses beneath a closed displayed-functor application', () => {
        const value = fixture();
        const {
            emdash,
            bindings,
            liftedProduct
        } = value;
        const HH = emdash.displayedFunctor(
            'HH',
            liftedProduct,
            liftedProduct
        );
        const mapped = emdash.displayedDependentContextLambda(
            bindings,
            liftedProduct,
            ([, b, c]) => emdash.apply(
                HH,
                emdash.fibrePair(b, c)
            )
        );
        const point = makePoint(value, 'recursive');
        const actual = applyAt(value, mapped, point);
        const pairedInput = applyAt(
            value,
            abstractions(value).pair,
            point
        );
        const expected = emdash.apply(
            emdash.apply(
                HH,
                point.product.groupedObject,
                { expectedShape: 'fibre-functor' }
            ),
            pairedInput
        );
        const comparison = emdash.compare(
            actual,
            expected,
            60_000
        );
        assert.equal(comparison.status, 'equal');
        assert.match(
            emdash.compile(mapped).explicitCore,
            /generic-category-composition/u
        );
    });

    it('computes internalized actions and retains the paired cell', () => {
        const value = fixture();
        const {
            emdash,
            K,
            A,
            P,
            D
        } = value;
        const compiledAbstractions = abstractions(value);
        const p0 = makePoint(value, '0');
        const p1 = makePoint(value, '1');
        const p = emdash.hom('p', K, p0.k, p1.k);
        const alpha = emdash.hom(
            'alpha',
            emdash.fibre(A, p1.k),
            emdash.apply(emdash.familyTransport(A, p), p0.a),
            p1.a
        );
        const qA = emdash.sigmaArrow(
            A,
            p0.a,
            p1.a,
            p,
            alpha
        );
        const rho = emdash.hom(
            'rho',
            emdash.fibre(P, p1.ka),
            emdash.apply(
                emdash.familyTransport(P, qA),
                p0.product.groupedFibreObject
            ),
            p1.product.groupedFibreObject
        );
        const qP = emdash.sigmaArrow(
            P,
            p0.product.groupedFibreObject,
            p1.product.groupedFibreObject,
            qA,
            rho
        );
        const e0 = emdash.object(
            'e0',
            emdash.fibre(D, p0.product.groupedObject)
        );
        const named = [
            ['a', compiledAbstractions.a],
            ['b', compiledAbstractions.b],
            ['c', compiledAbstractions.c],
            ['d', compiledAbstractions.d],
            ['pair', compiledAbstractions.pair]
        ] as const;
        const cells = new Map<string, ReturnType<
            typeof emdash.displayedFunctorInternalCell
        >>();
        const independence =
            new Map<string, CoreLfComparisonResult>();
        for (const [name, abstraction] of named) {
            const left = emdash.displayedFunctorInternalCell(
                abstraction,
                qP,
                p0.d
            );
            const right = emdash.displayedFunctorInternalCell(
                abstraction,
                qP,
                name === 'd' ? p0.d : e0
            );
            const comparison = emdash.compare(left, right, 60_000);
            assert.equal(comparison.status, 'equal');
            cells.set(name, left);
            independence.set(name, comparison);
        }
        const forcedResults =
            new Map<string, CoreLfComparisonResult>();
        for (const name of ['b', 'c', 'pair']) {
            const forced = emdash.compare(
                cells.get(name) as CoreCategoricalTerm,
                rho,
                60_000
            );
            assert.equal(forced.status, 'not-equal');
            forcedResults.set(name, forced);
        }
        const pairedIndependence =
            independence.get('pair') as CoreLfComparisonResult;
        assert.equal(
            runtimeRuleIds(pairedIndependence).includes(
                'categorical.displayed-chain-2a.' +
                    'displayed-product-pair-internal-cell'
            ),
            true
        );
        const noncollapse =
            forcedResults.get('pair') as CoreLfComparisonResult;
        if (noncollapse.status !== 'not-equal') {
            assert.fail('Paired internalized cell unexpectedly collapsed');
        }
        assert.match(
            serializeCoreCategoricalExpression(
                noncollapse.normalizedLeft
            ),
            /product-pair/u
        );
    });

    it('preserves ordinary reindexing and point computation', () => {
        const value = fixture();
        const {
            emdash,
            sigmaP,
            D
        } = value;
        const paired = abstractions(value).pair;
        const L = emdash.category('L');
        const u = emdash.functor('u', L, sigmaP);
        const reindexed = emdash.pullbackDisplayedFunctor(paired, u);
        const compilation = emdash.compile(reindexed);
        assert.equal(compilation.surfaceType.tag, 'displayed-functor');
        assert.match(
            compilation.explicitCore,
            /emdash\.categorical\.displayed-pullback-functor/u
        );
        const x = emdash.object('x', L);
        const ux = emdash.apply(u, x);
        const pulledD = emdash.pullbackFamily(D, u);
        const dx = emdash.object(
            'dx',
            emdash.fibre(pulledD, x)
        );
        const beforeFibre = emdash.apply(
            paired,
            ux,
            { expectedShape: 'fibre-functor' }
        );
        const afterFibre = emdash.apply(
            reindexed,
            x,
            { expectedShape: 'fibre-functor' }
        );
        assert.equal(
            emdash.compare(
                afterFibre,
                beforeFibre,
                60_000
            ).status,
            'equal'
        );
        const after = emdash.apply(afterFibre, dx);
        assert.equal(
            emdash.compile(after).surfaceType.tag,
            'object'
        );
    });

    it('fails closed on predecessor, bases, names, arity, and modes', () => {
        const value = fixture();
        const {
            emdash,
            K,
            A,
            B,
            C,
            D,
            bindings
        } = value;
        const predecessor = new CoreCategoricalProgram({
            profile: 'fibred-displayed-chain-1'
        });
        const PK = predecessor.category('PK');
        const PA = predecessor.displayedFamily('PA', PK);
        const PsigmaA = predecessor.totalCategory(PA);
        const PB = predecessor.displayedFamily('PB', PsigmaA);
        const PC = predecessor.displayedFamily('PC', PsigmaA);
        const PP = predecessor.displayedProduct(PB, PC);
        const PD = predecessor.displayedFamily(
            'PD',
            predecessor.totalCategory(PP)
        );
        assert.throws(
            () => predecessor.displayedDependentContextLambda(
                [
                    { name: 'a', family: PA },
                    { name: 'b', family: PB },
                    { name: 'c', family: PC },
                    { name: 'd', family: PD }
                ],
                PD,
                ([, , , d]) => d
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'UNAVAILABLE_DISPLAYED_CHAIN'
        );
        const wrongMiddle = emdash.displayedFamily('wrongMiddle', K);
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                [
                    { name: 'a', family: A },
                    { name: 'b', family: wrongMiddle },
                    { name: 'c', family: C },
                    { name: 'd', family: D }
                ],
                D,
                ([, , , d]) => d
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'DISPLAYED_BASE_MISMATCH'
        );
        const wrongDeep = emdash.displayedFamily('wrongDeep', K);
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                [
                    { name: 'a', family: A },
                    { name: 'b', family: B },
                    { name: 'c', family: C },
                    { name: 'd', family: wrongDeep }
                ],
                wrongDeep,
                ([, , , d]) => d
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'DISPLAYED_BASE_MISMATCH'
        );
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                bindings,
                B,
                ([, b]) => b
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'DISPLAYED_BASE_MISMATCH'
        );
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                [
                    { name: 'a', family: A },
                    { name: 'b', family: B },
                    { name: 'b', family: C },
                    { name: 'd', family: D }
                ],
                D,
                ([, , , d]) => d
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'INVALID_DISPLAYED_CONTEXT'
        );
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                [
                    { name: 'a', family: A },
                    { name: 'c', family: C },
                    { name: 'b', family: B },
                    { name: 'd', family: D }
                ],
                D,
                ([, , , d]) => d
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'DISPLAYED_BASE_MISMATCH'
        );
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                [
                    { name: 'a', family: A },
                    { name: 'b', family: B },
                    { name: 'c', family: C }
                ],
                D,
                ([, , c]) => c
            ),
            error =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'INVALID_DISPLAYED_CONTEXT'
        );
        for (const options of [
            { variation: 'natural' as const },
            { polarity: 'contravariant' as const },
            { cellLevel: 'arrow' as const },
            { dependency: 'ordinary' as const }
        ]) {
            assert.throws(
                () => emdash.displayedDependentContextLambda(
                    bindings,
                    D,
                    ([, , , d]) => d,
                    options
                ),
                error =>
                    error instanceof CoreCategoricalFrontendError ||
                    error instanceof CoreCategoricalProgramError
            );
        }
    });

    it('fails closed on escaped, foreign, and unsupported bodies', () => {
        const value = fixture();
        const {
            emdash,
            bindings,
            D
        } = value;
        let escaped: CoreCategoricalSlotToken | undefined;
        emdash.displayedDependentContextLambda(
            bindings,
            D,
            ([a, , , d]) => {
                escaped = a;
                return d;
            }
        );
        assert.throws(
            () => emdash.fibrePair(
                escaped as CoreCategoricalSlotToken,
                escaped as CoreCategoricalSlotToken
            ),
            error =>
                error instanceof CoreCategoricalFrontendError &&
                error.code === 'ESCAPED_SLOT'
        );

        const foreign = fixture();
        const foreignTerm =
            foreign.emdash.displayedDependentContextLambda(
                foreign.bindings,
                foreign.D,
                ([, , , d]) => d
            );
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                bindings,
                D,
                () => foreignTerm
            ),
            error =>
                error instanceof CoreCategoricalFrontendError &&
                error.code === 'FOREIGN_TERM'
        );
        const closed = emdash.displayedFunctor('closed', D, D);
        assert.throws(
            () => emdash.displayedDependentContextLambda(
                bindings,
                D,
                () => closed
            ),
            error =>
                error instanceof CoreCategoricalFrontendError &&
                error.code === 'CLASSIFIER_ARGUMENT_MISMATCH'
        );
    });
});
