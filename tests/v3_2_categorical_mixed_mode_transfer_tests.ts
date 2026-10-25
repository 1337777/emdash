/**
 * MIXED-NEST-0A existing-authority generic transfer evidence.
 */

import assert from 'node:assert/strict';
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
    CORE_CATEGORICAL_MIXED_MODE_CORE_NAMES,
    CORE_CATEGORICAL_MIXED_MODE_RUNTIME_MODULE,
    CORE_CATEGORICAL_MIXED_MODE_RUNTIME_POLICY,
    CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256,
    CORE_CATEGORICAL_MIXED_MODE_SYMBOLS,
    CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY,
    CORE_CATEGORICAL_MIXED_MODE_TRANSFER_LINKAGE,
    CORE_CATEGORICAL_MIXED_MODE_TRANSFER_MODULE,
    CORE_CATEGORICAL_MIXED_MODE_TRANSFER_POLICY,
    CoreCategoricalMixedModeSymbolId,
    compileCoreCategoricalMixedModeTransfer,
    coreCategoricalMixedModeCoreName
} from '../src/v3_2/categorical_mixed_mode_transfer';
import { kernelFree, provenance } from '../src/v3_2/kernel';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';
import { checkLambdapiProbe } from '../src/v3_2/probe';
import { compileCoreCategoricalMixedActionTransfer } from '../src/v3_2/categorical_mixed_action_transfer';
import { CoreCategoricalProgram } from '../src/v3_2/categorical_program';

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

describe('MIXED-NEST-0A generic transfer', () => {
    it('pins mixed families and their native total-duality prerequisites', () => {
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY.declarationNames,
            ['CoAbove2_cat', 'TotalOp_cat', 'TotalOp_catd', 'Hom_catd', 'Transf_catd']
        );
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY.runtimeRuleIds,
            [
                'categorical.mixed-mode.higher-dual-objects',
                'categorical.mixed-mode.higher-dual-hom',
                'categorical.mixed-mode.higher-dual-involution',
                'categorical.mixed-mode.higher-dual-commute',
                'categorical.mixed-mode.total-family-fibre',
                'categorical.mixed-mode.total-family-involution',
                'categorical.mixed-mode.displayed-opposite-fibre',
                'categorical.mixed-mode.hom-family-fibre',
                'categorical.mixed-mode.transfor-family-fibre',
                'categorical.mixed-mode.functor-hom-fold'
            ]
        );
        assert.deepEqual(
            [
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .activeLambdapiOwnerDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .activeLambdapiRuleDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .intrinsicCoreOwnerDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .ownerSpecificCheckerOrEvaluatorDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .externalCoherenceEvidenceDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .nestedAbstractionLowererDelta,
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
                    .textOrBrowserDelta
            ],
            [0, 0, 0, 0, 0, 0, 0]
        );
        assertDeepFrozen(
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY
        );
    });

    it('uses one immutable Core-name contract for transfer linkage', () => {
        for (const id of Object.keys(
            CORE_CATEGORICAL_MIXED_MODE_CORE_NAMES
        ) as CoreCategoricalMixedModeSymbolId[]) {
            const symbol = CORE_CATEGORICAL_MIXED_MODE_SYMBOLS[id];
            const link =
                CORE_CATEGORICAL_MIXED_MODE_TRANSFER_LINKAGE.entries
                    .find(candidate =>
                        candidate.symbol.moduleId === symbol.moduleId &&
                        candidate.symbol.name === symbol.name
                    );
            assert.equal(
                link?.kind === 'free-declaration'
                    ? link.coreName
                    : undefined,
                CORE_CATEGORICAL_MIXED_MODE_CORE_NAMES[id]
            );
            assert.equal(
                coreCategoricalMixedModeCoreName(id),
                CORE_CATEGORICAL_MIXED_MODE_CORE_NAMES[id]
            );
        }
        assertDeepFrozen(CORE_CATEGORICAL_MIXED_MODE_CORE_NAMES);
    });

    it('pins active source bytes and owner/rule positions', () => {
        const source = readFileSync(activeKernelPath, 'utf8');
        assert.equal(
            'sha256:' + createHash('sha256')
                .update(source)
                .digest('hex'),
            CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256
        );
        assert.match(
            source,
            /injective symbol Hom_catd \[K : Cat\]/u
        );
        assert.match(
            source,
            /injective symbol Transf_catd \[K : Cat\]/u
        );
        assert.match(
            source,
            /rule @Hom_catd \$K \(@Functor_catd \$K \$A \$B\) \$FF \$GG/u
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_MODULE
                .declarations.length,
            5
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_MODE_RUNTIME_MODULE
                .runtimeRules.length,
            10
        );
    });

    it('subject-checks every signature and runtime rule generically', () => {
        const compilation =
            compileCoreCategoricalMixedModeTransfer();
        assert.deepEqual(
            compilation.compiled.declarations.map(declaration => ({
                name: declaration.symbol.name,
                status: declaration.status,
                hasBody: declaration.body !== undefined
            })),
            [
                { name: 'CoAbove2_cat', status: 'installed-opaque', hasBody: false },
                { name: 'TotalOp_cat', status: 'installed-transparent', hasBody: true },
                { name: 'TotalOp_catd', status: 'installed-opaque', hasBody: false },
                {
                    name: 'Hom_catd',
                    status: 'installed-opaque',
                    hasBody: false
                },
                {
                    name: 'Transf_catd',
                    status: 'installed-opaque',
                    hasBody: false
                }
            ]
        );
        assert.deepEqual(
            compilation.runtime.rules.map(rule =>
                rule.subjectValidation.kind
            ),
            Array(10).fill('typescript-checked')
        );
        assert.deepEqual(
            compilation.composedRuntime.ruleIds.slice(-10),
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_BOUNDARY.runtimeRuleIds
        );
        assert.doesNotThrow(
            () => compilation.compiled.createChecker()
                .validateEnvironment()
        );
    });

    it('checks the native derived total dual and opaque family owners', () => {
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_MODE_TRANSFER_POLICY.entries.map(
                entry => entry.policy
            ),
            ['opaque-signature', 'checked-transparent-definition',
                'opaque-signature', 'opaque-signature', 'opaque-signature']
        );
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_MODE_RUNTIME_POLICY.entries.map(
                entry => entry.policy
            ),
            Array(10).fill('runtime-rewrite')
        );
        assertDeepFrozen(CORE_CATEGORICAL_MIXED_MODE_TRANSFER_MODULE);
        assertDeepFrozen(CORE_CATEGORICAL_MIXED_MODE_RUNTIME_MODULE);
    });

    it('checks emitted mixed signatures and every fibre/duality projection natively', {
        skip: process.env.EMDASH_RUN_LAMBDAPI_MIXED_DUALITY_PROBES !== '1'
    }, () => {
        const ladder = compileCoreCategoricalMixedActionTransfer();
        const c = ladder.prerequisite;
        const foundation = c.prerequisite.prerequisite;
        const duality = foundation.prerequisite, chain2 = duality.prerequisite;
        const chain = chain2.prerequisite, evaluation = chain.prerequisite;
        const pi = evaluation.prerequisite, weaken = pi.prerequisite;
        const transfd = weaken.prerequisite, binder = transfd.prerequisite;
        const structure = binder.prerequisite, product = structure.prerequisite;
        const comprehension = product.prerequisite, composition = comprehension.prerequisite;
        const dependent = composition.dependent, structural = dependent.structural;
        const modules = [structural.initialDeclarations, structural.compiled, dependent.compiled,
            composition.compiled, comprehension.compiled, product.compiled, structure.compiled,
            binder.compiled, transfd.compiled, weaken.compiled, pi.compiled,
            evaluation.prerequisiteCompiled, evaluation.compiled, chain.prerequisiteCompiled,
            chain.compiled, chain2.compiled, duality.compiled, foundation.signatureCompiled,
            foundation.compiled, c.prerequisite.compiled, c.compiled, ladder.initialCompiled, ladder.compiled];
        const references = Object.assign({}, ...modules.flatMap(m => [m.externalFreeReferences,
            m.externalTransparentDefinitions, Object.fromEntries(m.linkage.entries.flatMap(link =>
                link.kind === 'free-declaration' && link.backendName
                    ? [[link.coreName, link.backendName]] : []))]));
        const serialize = (term: Parameters<typeof serializeKernelExpression>[0], names = {}) =>
            serializeKernelExpression(term, { externalFreeReferences: { ...references, ...names } });
        const site = provenance('derived', 'native mixed total-duality conformance');
        const declarations = [...c.compiled.declarations, ...ladder.initialCompiled.declarations,
            ...ladder.compiled.declarations].flatMap(d => [
            `assert ⊢ @${d.symbol.name} : ${serialize(d.type)};`,
            ...(d.body ? [`assert ⊢ @${d.symbol.name} ≡ ${serialize(d.body)};`] : [])
        ]);
        const equations = [...c.runtime.rules, ...ladder.runtime.rules].flatMap((rule, index) => {
            const family = rule.id.endsWith('transfor-family-fibre') || rule.id.endsWith('functor-hom-fold');
            const mixedConstructor = rule.id.includes('mixed-functor-');
            const types: Record<string, string> = family ? {
                K: 'Cat', A: 'τ (Catd (Op_cat K))', B: 'τ (Catd K)',
                FF: 'τ (Obj (Pi_cat (TotalOp_catd (@Functor_catd K A B))))',
                GG: 'τ (Obj (Pi_cat (@Functor_catd K A B)))', k: 'τ (Obj K)'
            } : mixedConstructor ? {
                K: 'Cat', A: 'τ (Catd (Op_cat K))', B: 'τ (Catd K)'
            } : {
                A: 'Cat', x: 'τ (Obj A)', y: 'τ (Obj A)', K: 'Cat', E: 'τ (Catd K)',
                X: 'τ (Obj (Pi_cat (TotalOp_catd E)))', Y: 'τ (Obj (Pi_cat E))', k: 'τ (Obj K)',
                B: 'Cat', F: 'τ (Functor A B)', G: 'τ (Functor A B)',
                W: 'τ (Obj A)', f: 'τ (Hom A x y)', U: 'τ (@Transf A B F G)'
            };
            if (rule.id.endsWith('represented-hom-object-projection')) {
                types.F = 'τ (Functor B A)'; types.y = 'τ (Obj B)';
            }
            if (rule.id.endsWith('represented-package-object')) types.x = 'τ (Obj K)';
            if (rule.id.endsWith('cartesian-include-arrow')) types.U = 'τ (Hom (Functor_cart_cat A B) F G)';
            const names = Object.fromEntries(rule.variables.map(v => [v.name, `r${index}_${v.name}`]));
            const rename = (type: string) => type.replace(/\b[A-Za-z]+\b/gu, name => names[name] ?? name);
            const runtime = index < c.runtime.rules.length ? c.runtime : ladder.runtime;
            const left = runtime.instantiateRuleLeft(rule, rule.variables.map(v => kernelFree(v.name, site)), site);
            const result = runtime.rewriteHead(left);
            assert.equal(result.status, 'rewritten');
            if (result.status !== 'rewritten') throw new Error('Missing native mixed projection');
            assert.equal(result.ruleId, rule.id);
            return [
                ...rule.variables.map(v => `symbol ${names[v.name]} : ${rename(types[v.name])};`),
                `assert ⊢ ${serialize(left, names)} ≡ ${serialize(result.after, names)};`
            ];
        });
        const e = new CoreCategoricalProgram({profile:'fibred-displayed-mixed-nest-1'});
        const base=e.category('K'), D=e.displayedFamily('D',base), E=e.displayedFamily('E',base);
        const FF=e.displayedFunctor('FF',D,E), x=e.object('x',base), y=e.object('y',base);
        const u=e.object('u',e.fibre(E,x)), v=e.object('v',e.fibre(D,y));
        const root=e.compile(e.displayedInternalHom(FF));
        const endpoint=e.displayedInternalHomEndpointFamily(FF,x,u,y,v);
        // Its total is an actual downstream consumer of the endpoint family.
        const endpointText=e.serializeCategory(e.totalCategory(endpoint));
        assert.match(endpointText,/homd_/u);
        const source = ['require open emdash.emdash3_2;', ...declarations, ...equations,
            'symbol K : Cat;', 'symbol E : τ (Catd K);',
            'symbol X : τ (Obj (Pi_cat (TotalOp_catd E)));', 'symbol Y : τ (Obj (Pi_cat E));',
            'symbol XT : τ (Obj (Pi_cat (Op_catd E)));',
            'assert ⊢ @Hom_catd K E X Y : τ (Catd K);',
            'assertnot ⊢ @Hom_catd K E XT Y : τ (Catd K);',
            'assertnot ⊢ @TotalOp_catd K E : τ (Catd K);',
            'assertnot ⊢ CoAbove2_cat K ≡ K;',
            'assertnot ⊢ TotalOp_cat K ≡ Op_cat K;',
            'symbol D : τ (Catd K);', 'symbol FF : τ (Functord D E);',
            'symbol x : τ (Obj K);', 'symbol y : τ (Obj K);',
            'symbol u : τ (Obj (Fibre_cat E x));', 'symbol v : τ (Obj (Fibre_cat D y));',
            'symbol f : τ (Hom K x y);',
            `assert ⊢ ${serialize(root.explicitTerm)} : ${serialize(root.expectedType)};`,
            'assert ⊢ tapp0_fapp0 x (@homd_int K D E FF) ≡ @homd_src_func K D E FF x;',
            'assert ⊢ fapp0 (@homd_src_func K D E FF x) u ≡ @homd_src_sec K D E FF x u;',
            'assert ⊢ tapp0_fapp0 y (@homd_src_sec K D E FF x u) ≡ @homd_tgt_func K D E FF x u y;',
            'assert ⊢ homd_index_presheaf (fapp0 (@homd_tgt_func K D E FF x u y) v) ≡ @homd_ K D E FF x u y v;',
            'assert ⊢ fapp0 (@homd_ K D E FF x u y v) f ≡ Hom_cat (Fibre_cat E y) (fapp0 (fapp1_fapp0 E f) u) (fapp0 (Fibre_func FF y) v);'
        ].join('\n');
        assert.doesNotMatch(source, /dttlf_|emdash_v3_2_/u);
        const result = checkLambdapiProbe({ source, sourceMap: [] }, {
            packageRoot: resolve(__dirname, '../emdash2'), timeoutMs: 60_000
        });
        assert.equal(result.accepted, true, result.diagnostics + '\n' + source);
        assert.equal(result.timedOut, false);
    });
});
