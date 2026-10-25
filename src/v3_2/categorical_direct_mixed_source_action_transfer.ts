/**
 * Direct mixed source action at its native Cartesian diagram profile.
 *
 * No declaration is introduced. Opposite-Hom computation is inherited from
 * the source-prior Homd duality fragment; this native rule projects the
 * contravariant source-family action of `Functor_catd_func` at a shared base
 * point and returns the whole ordinary composite `H o L[k]`.
 */

import {
    CoreCategoricalDirectMixedIntroductionCompilation,
    compileCoreCategoricalDirectMixedIntroductionTransfer
} from './categorical_direct_mixed_introduction_transfer';
import {
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_SYMBOLS
} from './categorical_displayed_nd_higher_foundation_transfer';
import {
    CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS
} from './categorical_mixed_action_transfer';
import {
    CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256
} from './categorical_mixed_mode_transfer';
import {
    CORE_CATEGORICAL_STRUCTURAL_SYMBOLS
} from './categorical_structural_transfer';
import {
    coreDirectedContinuationTransferSymbol
} from './directed_continuation_transfer';
import {
    CoreLfModuleSpec,
    CoreLfQualifiedSymbol,
    CoreLfTransferBuilderExpression,
    CoreLfTransferPolicyOverlay,
    CoreLfTransferRuntimeRule,
    CoreLfTransferScopedBuilder,
    coreLfQualifiedSymbol,
    createCoreLfModuleSpec,
    createCoreLfTransferPolicyOverlay
} from './lf_transfer';
import {
    CoreLfCompiledDeclarationModule,
    compileCoreLfDeclarations
} from './lf_transfer_compiler';
import {
    CoreLfMixedDeclarationContext
} from './lf_transfer_mixed';
import {
    CoreLfCompiledRuntimeFragment,
    CoreLfCompiledRuntimeProgram,
    CoreLfComposedRuntimeProgram,
    compileCoreLfRuntimeFragment
} from './lf_transfer_runtime';

const MODULE_ID = 'emdash.emdash3_2';

export const CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_TRANSFER_REVISION =
    'DIRECT-MIXED-SOURCE-ACTION-NATIVE-CART-2' as const;

const category =
    coreDirectedContinuationTransferSymbol('category-universe');
const decodeOwner = coreDirectedContinuationTransferSymbol('decode');
const objectClassifier =
    coreDirectedContinuationTransferSymbol('object-classifier');
const homCategory =
    coreDirectedContinuationTransferSymbol('hom-category');
const familyCoefficient =
    coreDirectedContinuationTransferSymbol('cartesian-category-coefficient');
const displayedCategoryCategory =
    coreDirectedContinuationTransferSymbol('displayed-category-category');
const functorObject =
    coreDirectedContinuationTransferSymbol('functor-object');
const functorHomCapped =
    coreDirectedContinuationTransferSymbol('functor-hom-capped');
const transforComponentCapped =
    coreDirectedContinuationTransferSymbol('transfor-component-capped');

const symbol = (name: string): CoreLfQualifiedSymbol =>
    coreLfQualifiedSymbol(MODULE_ID, name);

const displayedFamilyClassifier = symbol('Catd');
const displayedFunctorClassifier = symbol('Functord');
const oppositeCategory = symbol('Op_cat');
const functorCategory = symbol('Functor_cat');
const cartesianFunctorCategory = symbol('Functor_cart_cat');
const strictTransforView = symbol('strict_transfor');
const stableFunctorFamily = symbol('Functor_catd');

const {
    mixedFunctorFamily
} = CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_SYMBOLS;
const {
    mixedFunctorFamilyPartial
} = CORE_CATEGORICAL_MIXED_ACTION_SYMBOLS;
const {
    functorComposition
} = CORE_CATEGORICAL_STRUCTURAL_SYMBOLS;

interface BuilderArgument {
    readonly plicity: 'explicit' | 'implicit';
    readonly value: CoreLfTransferBuilderExpression;
}

const call = (
    builder: CoreLfTransferScopedBuilder,
    callee: CoreLfTransferBuilderExpression,
    arguments_: readonly BuilderArgument[]
): CoreLfTransferBuilderExpression => builder.call(callee, arguments_);

const globalCall = (
    builder: CoreLfTransferScopedBuilder,
    target: CoreLfQualifiedSymbol,
    arguments_: readonly BuilderArgument[]
): CoreLfTransferBuilderExpression =>
    call(builder, builder.global(target), arguments_);

const decode = (
    builder: CoreLfTransferScopedBuilder,
    classifier: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, decodeOwner, [{
        plicity: 'explicit',
        value: classifier
    }]);

const objectType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, objectClassifier, [{
        plicity: 'explicit',
        value: base
    }]));

const oppositeAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, oppositeCategory, [{
        plicity: 'explicit',
        value: base
    }]);

const displayedCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedCategoryCategory, [{
        plicity: 'explicit',
        value: base
    }]);

const displayedFamilyType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    objectType(builder, displayedCategoryAt(builder, base));

const functorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorCategory, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const cartesianFunctorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, cartesianFunctorCategory, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const homCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceObject: CoreLfTransferBuilderExpression,
    targetObject: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, homCategory, [
        { plicity: 'explicit', value: base },
        { plicity: 'explicit', value: sourceObject },
        { plicity: 'explicit', value: targetObject }
    ]);

const functorObjectAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression,
    object: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorObject, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: functor },
        { plicity: 'explicit', value: object }
    ]);

const fibreAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    functorObjectAt(
        builder,
        base,
        builder.global(familyCoefficient),
        family,
        point
    );

const stableFunctorFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceFamily: CoreLfTransferBuilderExpression,
    targetFamily: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, stableFunctorFamily, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: sourceFamily },
        { plicity: 'explicit', value: targetFamily }
    ]);

const mixedFunctorFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, mixedFunctorFamily, [{
        plicity: 'explicit',
        value: base
    }]);

const mixedFunctorFamilyPartialAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceFamily: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, mixedFunctorFamilyPartial, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: sourceFamily }
    ]);

const functorHomCappedAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression,
    sourceObject: CoreLfTransferBuilderExpression,
    targetObject: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorHomCapped, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: functor },
        { plicity: 'implicit', value: sourceObject },
        { plicity: 'implicit', value: targetObject },
        { plicity: 'explicit', value: arrow }
    ]);

const componentAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    targetCategory: CoreLfTransferBuilderExpression,
    sourceFunctor: CoreLfTransferBuilderExpression,
    targetFunctor: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression,
    transfor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, transforComponentCapped, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: targetCategory },
        { plicity: 'implicit', value: sourceFunctor },
        { plicity: 'implicit', value: targetFunctor },
        { plicity: 'explicit', value: point },
        { plicity: 'explicit', value: transfor }
    ]);

const composeFunctorsAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    middle: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    outer: CoreLfTransferBuilderExpression,
    inner: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorComposition, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: middle },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: outer },
        { plicity: 'explicit', value: inner }
    ]);

const source = (sourceFragment: string) => ({
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceFragment
});

/** Existing generic prerequisite: opposite reverses Hom endpoints. */
const directMixedSourceCompositionProjectionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const K = builder.capture('K');
    const APrime = builder.capture('APrime');
    const A = builder.capture('A');
    const B = builder.capture('B');
    const L = builder.capture('L');
    const k = builder.capture('k');
    const H = builder.capture('H');
    const oppositeK = oppositeAt(builder, K);
    const displayedK = displayedCategoryAt(builder, K);
    const displayedOppositeK = cartesianFunctorCategoryAt(builder, oppositeK, builder.global(familyCoefficient));
    const sourceConstructorCategory = oppositeAt(
        builder,
        displayedOppositeK
    );
    const targetConstructorCategory = functorCategoryAt(
        builder,
        displayedK,
        displayedK
    );
    const sourceFibre = fibreAt(builder, oppositeK, APrime, k);
    const middleFibre = fibreAt(builder, oppositeK, A, k);
    const targetFibre = fibreAt(builder, K, B, k);
    const sourceFunctorCategory = cartesianFunctorCategoryAt(
        builder,
        middleFibre,
        targetFibre
    );
    const targetFunctorCategory = cartesianFunctorCategoryAt(
        builder,
        sourceFibre,
        targetFibre
    );
    const constructorAction = functorHomCappedAt(
        builder,
        sourceConstructorCategory,
        targetConstructorCategory,
        mixedFunctorFamilyAt(builder, K),
        A,
        APrime,
        L
    );
    const sourceAction = componentAt(
        builder,
        displayedK,
        displayedK,
        mixedFunctorFamilyPartialAt(builder, K, A),
        mixedFunctorFamilyPartialAt(builder, K, APrime),
        B,
        constructorAction
    );
    const sourceComponent = componentAt(
        builder,
        K,
        builder.global(familyCoefficient),
        stableFunctorFamilyAt(builder, K, A, B),
        stableFunctorFamilyAt(builder, K, APrime, B),
        k,
        sourceAction
    );
    const LAtK = componentAt(
        builder,
        oppositeK,
        builder.global(familyCoefficient),
        APrime,
        A,
        k,
        globalCall(builder, strictTransforView, [
            { plicity: 'implicit', value: oppositeK },
            { plicity: 'implicit', value: builder.global(familyCoefficient) },
            { plicity: 'implicit', value: APrime },
            { plicity: 'implicit', value: A },
            { plicity: 'explicit', value: L }
        ])
    );
    return {
        order: 1,
        id:
            'categorical.direct-mixed-source-action.' +
            'source-composition-projection',
        groupId:
            'categorical.direct-mixed-source-action.' +
            'source-composition-projection',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'K',
                type: builder.template(builder.global(category))
            },
            {
                name: 'APrime',
                type: builder.template(displayedFamilyType(
                    builder,
                    oppositeK
                ))
            },
            {
                name: 'A',
                type: builder.template(displayedFamilyType(
                    builder,
                    oppositeK
                ))
            },
            {
                name: 'B',
                type: builder.template(displayedFamilyType(builder, K))
            },
            {
                name: 'L',
                type: builder.template(objectType(builder, homCategoryAt(
                    builder, displayedOppositeK, APrime, A
                )))
            },
            {
                name: 'k',
                type: builder.template(objectType(builder, K))
            },
            {
                name: 'H',
                type: builder.template(objectType(
                    builder,
                    sourceFunctorCategory
                ))
            }
        ],
        left: builder.pattern(functorObjectAt(
            builder,
            builder.wildcard(sourceFunctorCategory),
            builder.wildcard(targetFunctorCategory),
            sourceComponent,
            H
        )),
        right: builder.template(composeFunctorsAt(
            builder,
            sourceFibre,
            middleFibre,
            targetFibre,
            H,
            LAtK
        )),
        provenance: source(
            'rule @fapp0 _ _ (@tapp0_fapp0 $K Cat_cart _ _ $k ' +
                '(@tapp0_fapp0 (Catd_cat $K) (Catd_cat $K) ' +
                '(@Functor_catd_fapp0_func $K $A) ' +
                '(@Functor_catd_fapp0_func $K $A\') $B ' +
                '(@fapp1_fapp0 _ _ (@Functor_catd_func $K) ' +
                '$A $A\' $L))) $H'
        )
    };
};

const runtimeRules = Object.freeze([
    { ...directMixedSourceCompositionProjectionRule(), order: 0 }
]);

export const CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE:
CoreLfModuleSpec = createCoreLfModuleSpec({
    revision:
        CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_TRANSFER_REVISION,
    moduleId: MODULE_ID,
    fragmentId: 'direct-mixed-source-action-1e2-runtime',
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256: CORE_CATEGORICAL_MIXED_MODE_SOURCE_SHA256,
    dependencies: [],
    externalSymbols: [
        category,
        decodeOwner,
        objectClassifier,
        homCategory,
        familyCoefficient,
        displayedCategoryCategory,
        functorObject,
        functorHomCapped,
        transforComponentCapped,
        displayedFamilyClassifier,
        displayedFunctorClassifier,
        oppositeCategory,
        functorCategory,
        cartesianFunctorCategory,
        strictTransforView,
        stableFunctorFamily,
        mixedFunctorFamily,
        mixedFunctorFamilyPartial,
        functorComposition
    ].map(symbol_ => ({
        symbol: symbol_,
        availability: 'earlier-fragment' as const
    })),
    declarations: [],
    inductives: [],
    runtimeRules,
    proofRules: []
});

export const CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_POLICY:
CoreLfTransferPolicyOverlay = createCoreLfTransferPolicyOverlay(
    CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE,
    {
        revision: 'DIRECT-MIXED-SOURCE-ACTION-1E2-RUNTIME-POLICY-1',
        moduleRevision:
            CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE
                .revision,
        entries: runtimeRules.map((rule, index) => ({
            order: rule.order,
            target: {
                kind: 'runtime-rule' as const,
                id: rule.id
            },
            policy: 'runtime-rewrite' as const,
            evidence: index === 0
                ? 'Exact D-DTTLF-USABILITY-046 existing prerequisite'
                : 'Exact D-DTTLF-USABILITY-045 existing-owner projection'
        }))
    }
);

export const CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_BOUNDARY =
Object.freeze({
    decision: 'foundations-frontend-direct-mixed-2026-10-25',
    historicalDecision: 'D-DTTLF-USABILITY-046',
    parentDecision: 'D-DTTLF-USABILITY-045',
    declarationCount: 0,
    runtimeRuleIds: Object.freeze(runtimeRules.map(rule => rule.id)),
    runtimeRuleCount: runtimeRules.length,
    existingPrerequisiteRuntimeRuleIds: Object.freeze(runtimeRules.map(rule => rule.id)),
    existingPrerequisiteRuntimeRuleCount: 1,
    newMathematicalRuntimeRuleIds: Object.freeze([]),
    newMathematicalRuntimeRuleCount: 0,
    activeLambdapiOwnerDelta: 0,
    activeLambdapiRuleDelta: 0,
    intrinsicCoreOwnerDelta: 0,
    ownerSpecificCheckerOrEvaluatorDelta: 0,
    externalCoherenceEvidenceDelta: 0,
    contextualBinderDelta: 0,
    textOrBrowserDelta: 0,
    transfersContextualCurry: false,
    allEntriesUseGenericTransferEngines: true
});

export interface CoreCategoricalDirectMixedSourceActionCompilation {
    readonly prerequisite:
        CoreCategoricalDirectMixedIntroductionCompilation;
    readonly compiled: CoreLfCompiledDeclarationModule;
    readonly declarationContext: CoreLfMixedDeclarationContext;
    readonly runtimeFragment: CoreLfCompiledRuntimeFragment;
    readonly runtime: CoreLfCompiledRuntimeProgram;
    readonly composedRuntime: CoreLfComposedRuntimeProgram;
}

let cachedCompilation:
    CoreCategoricalDirectMixedSourceActionCompilation | undefined;

export function compileCoreCategoricalDirectMixedSourceActionTransfer():
CoreCategoricalDirectMixedSourceActionCompilation {
    if (cachedCompilation !== undefined) return cachedCompilation;
    const prerequisite =
        compileCoreCategoricalDirectMixedIntroductionTransfer();
    const runtimeFragment = compileCoreLfRuntimeFragment(
        CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_MODULE,
        CORE_CATEGORICAL_DIRECT_MIXED_SOURCE_ACTION_RUNTIME_POLICY,
        prerequisite.declarationContext,
        {
            dependencies: [{
                relation: 'earlier-fragment',
                fragment: prerequisite.runtimeFragment
            }],
            comparisonStepLimit: 512
        }
    );
    /*
     * The public program obtains its checker from the final compiled
     * declaration module. Recompile the unchanged mixed-action declarations
     * against the composed D-043/D-045/D-046 runtime so source-map terms are
     * checked with the same conversion boundary that subject-checked the
     * rule. This adds no declaration and mirrors the established finalization
     * pattern used by other categorical transfer continuations.
     */
    const mixedAction = prerequisite.prerequisite;
    const compiled = compileCoreLfDeclarations(
        mixedAction.compiled.module,
        mixedAction.compiled.policy,
        mixedAction.compiled.linkage,
        {
            initialEnvironment:
                mixedAction.initialCompiled.environment,
            runtimeProgram: runtimeFragment.runtime,
            comparisonStepLimit: 512
        }
    );
    const declarationContext = new CoreLfMixedDeclarationContext(
        new CoreLfMixedDeclarationContext(
            mixedAction.prerequisite.declarationContext,
            [mixedAction.initialCompiled]
        ),
        [compiled]
    );
    cachedCompilation = Object.freeze({
        prerequisite,
        compiled,
        declarationContext,
        runtimeFragment,
        runtime: runtimeFragment.localProgram,
        composedRuntime: runtimeFragment.runtime
    });
    return cachedCompilation;
}
