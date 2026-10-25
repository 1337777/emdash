/**
 * FIBRED-DEPENDENT-TARGET-1 existing-authority transfer closure.
 *
 * Eleven active declarations, eleven runtime clauses, and one
 * proof-time category-presentation rule are compiled through the generic
 * transfer engines. Nine runtime subjects check directly. Exactly the
 * package-component and pullback-component subjects use the proof rule.
 * The proof rule is never installed as a runtime rewrite.
 */

import {
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT,
    validateCoreCategoricalFibredDependentTargetContract
} from './categorical_fibred_dependent_target_contract';
import {
    CORE_CATEGORICAL_FIBRED_WEAKEN_REINDEX_TRANSFER_LINKAGE,
    CoreCategoricalFibredWeakenReindexCompilation,
    compileCoreCategoricalFibredWeakenReindexTransfer
} from './categorical_fibred_weaken_reindex_transfer';
import {
    CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE
} from './categorical_structural_transfer';
import {
    CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE
} from './directed_continuation_transfer';
import {
    CoreLfModuleSpec,
    CoreLfQualifiedSymbol,
    CoreLfTransferBuilderExpression,
    CoreLfTransferDeclaration,
    CoreLfTransferExpression,
    CoreLfTransferPolicyOverlay,
    CoreLfTransferRuntimeRule,
    CoreLfTransferScopedBuilder,
    coreLfQualifiedSymbol,
    coreLfTransferAbsentBody,
    coreLfTransferExplicitBody,
    createCoreLfModuleSpec,
    createCoreLfTransferPolicyOverlay
} from './lf_transfer';
import {
    CoreLfCompiledDeclarationModule,
    CoreLfTransferDeclarationLink,
    CoreLfTransferDeclarationLinkage,
    compileCoreLfDeclarations,
    createCoreLfTransferDeclarationLinkage
} from './lf_transfer_compiler';
import {
    CoreLfMixedDeclarationContext
} from './lf_transfer_mixed';
import {
    CoreLfCompiledProofProgram,
    compileCoreLfProofProgram
} from './lf_transfer_proof';
import {
    CoreLfCompiledRuntimeFragment,
    CoreLfComposedRuntimeProgram,
    compileCoreLfRuntimeFragment
} from './lf_transfer_runtime';
import {
    binderMode
} from './kernel';
import {
    CORE_LF_SCALE_STRESS_2B1_LINKAGE,
    CORE_LF_SCALE_STRESS_2B1_MODULE
} from './scale_stress_2b_representation';
import {
    validateCoreLfScaleEngineReview
} from './scale_engine_review';

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_REVISION =
    'FIBRED-DEPENDENT-TARGET-1-EXISTING-AUTHORITY-TRANSFER-D060-1' as const;

const MODULE_ID = 'emdash.emdash3_2';

// Qualified against the migrated whole Pi components and diagram inclusion.
const CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SOURCE_SHA256 =
    'sha256:70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e';
const symbol = (name: string): CoreLfQualifiedSymbol =>
    coreLfQualifiedSymbol(MODULE_ID, name);

const category = symbol('Cat');
const groupoid = symbol('Grpd');
const decodeOwner = symbol('τ');
const objectClassifier = symbol('Obj');
const homClassifier = symbol('Hom');
const homCategory = symbol('Hom_cat');
const functorClassifier = symbol('Functor');
const categoryOfCategories = symbol('Cat_cat');
const familyCoefficient = symbol('Cat_cart');
const cartesianFunctorCategory = symbol('Functor_cart_cat');
const cartesianInclusion = symbol('Functor_cart_include');
const contravariantHom = symbol('hom_con');
const identityFunctor = symbol('id_func');
const constantFamily = symbol('Const_catd');
const pullbackFamily = symbol('Pullback_catd');
const transforComponent = symbol('tapp0_fapp0');
const functorHomAction = symbol('fapp1_fapp0');
const pullbackFamilyFunctor = symbol('Pullback_catd_func');
const functorCategory = symbol('Functor_cat');
const displayedCategoryCategory = symbol('Catd_cat');
const displayedFunctorCategory = symbol('Functord_cat');
const sectionCategory = symbol('Pi_cat');
const functorObject = symbol('fapp0');
const functorComposition = symbol('comp_cat_fapp0');
const oppositeCategory = symbol('Op_cat');
const displayedFunctorClassifier = symbol('Functord');
const fixedEvaluation = symbol('fapp0_func');
const internalFunctorCategory = symbol('Functor_cat_func');
const partialFunctorCategory = symbol('Functor_cat_fapp0_func');
const displayedCategoryFunctor = symbol('Catd_cat_func');
const sectionCategoryFunctor = symbol('Pi_func');
const internalPi = symbol('Pi_int_funcd');
const pullbackPi = symbol('Pi_pullback_funcd');

export const CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SYMBOLS =
Object.freeze({
    homClassifier,
    oppositeCategory,
    displayedFunctorClassifier,
    fixedEvaluation,
    internalFunctorCategory,
    partialFunctorCategory,
    displayedCategoryFunctor,
    sectionCategoryFunctor,
    internalPi,
    pullbackPi
});

const implicitMode = binderMode('implicit', 'functorial');
const explicitMode = binderMode('explicit', 'functorial');

interface BuilderArgument {
    readonly plicity: 'explicit' | 'implicit';
    readonly value: CoreLfTransferBuilderExpression;
}

const call = (
    builder: CoreLfTransferScopedBuilder,
    callee: CoreLfTransferBuilderExpression,
    arguments_: readonly BuilderArgument[]
): CoreLfTransferBuilderExpression =>
    builder.call(callee, arguments_);

const globalCall = (
    builder: CoreLfTransferScopedBuilder,
    owner: CoreLfQualifiedSymbol,
    arguments_: readonly BuilderArgument[]
): CoreLfTransferBuilderExpression =>
    call(builder, builder.global(owner), arguments_);

const decode = (
    builder: CoreLfTransferScopedBuilder,
    classifier: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, decodeOwner, [{
        plicity: 'explicit',
        value: classifier
    }]);

const objectClassifierAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, objectClassifier, [{
        plicity: 'explicit',
        value: base
    }]);

const objectType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, objectClassifierAt(builder, base));

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

const functorClassifierAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorClassifier, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const functorType = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, functorClassifierAt(builder, source, target));

const functorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorCategory, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const opposite = (
    builder: CoreLfTransferScopedBuilder,
    value: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, oppositeCategory, [{
        plicity: 'explicit',
        value
    }]);

const fapp0 = (
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

const internalFunctorCategoryType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(functorType(
        builder,
        opposite(builder, builder.global(categoryOfCategories)),
        functorCategoryAt(
            builder,
            builder.global(categoryOfCategories),
            builder.global(categoryOfCategories)
        )
    ));
};

const partialFunctorCategoryType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'A',
        builder.global(category),
        _A => functorType(
            builder,
            builder.global(categoryOfCategories),
            builder.global(categoryOfCategories)
        ),
        explicitMode
    ));
};

const unary = (b: CoreLfTransferScopedBuilder, owner: CoreLfQualifiedSymbol,
    value: CoreLfTransferBuilderExpression) => globalCall(b, owner, [{ plicity: 'explicit', value }]);
const cartesianAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    B: CoreLfTransferBuilderExpression) => globalCall(b, cartesianFunctorCategory, [
        { plicity: 'explicit', value: A }, { plicity: 'explicit', value: B }
    ]);
const familyTypeAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression) =>
    objectType(b, unary(b, displayedCategoryCategory, K));
const constFamilyAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    C: CoreLfTransferBuilderExpression) => globalCall(b, constantFamily, [
        { plicity: 'explicit', value: K }, { plicity: 'explicit', value: C }
    ]);
const displayedMapTypeAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    E: CoreLfTransferBuilderExpression, D: CoreLfTransferBuilderExpression) =>
    decode(b, globalCall(b, displayedFunctorClassifier, [
        { plicity: 'implicit', value: K }, { plicity: 'explicit', value: E },
        { plicity: 'explicit', value: D }
    ]));
const pulledFamilyAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    L: CoreLfTransferBuilderExpression, E: CoreLfTransferBuilderExpression,
    G: CoreLfTransferBuilderExpression) => globalCall(b, pullbackFamily, [
        { plicity: 'implicit', value: K }, { plicity: 'implicit', value: L },
        { plicity: 'explicit', value: E }, { plicity: 'explicit', value: G }
    ]);
const homConAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    W: CoreLfTransferBuilderExpression, B: CoreLfTransferBuilderExpression,
    F: CoreLfTransferBuilderExpression) => globalCall(b, contravariantHom, [
        { plicity: 'implicit', value: A }, { plicity: 'explicit', value: W },
        { plicity: 'implicit', value: B }, { plicity: 'explicit', value: F }
    ]);
const contravariantHomType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder();
    return b.term(b.pi('A', b.global(category), A =>
        b.pi('W', objectType(b, A), _W =>
            b.pi('B', b.global(category), B =>
                b.pi('F', functorType(b, B, A), _F =>
                    functorType(b, opposite(b, B), b.global(familyCoefficient)), explicitMode),
                implicitMode), explicitMode), implicitMode));
};
const inclusionType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder();
    return b.term(b.pi('A', b.global(category), A =>
        b.pi('B', b.global(category), B =>
            functorType(b, cartesianAt(b, A, B), functorCategoryAt(b, A, B)),
            explicitMode), explicitMode));
};
const displayedCategoryFunctorType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    return b.term(functorType(b, opposite(b, cart), cart));
};
const displayedCategoryFunctorBody = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    return b.term(homConAt(b, cart, cart, cart,
        globalCall(b, identityFunctor, [{ plicity: 'implicit', value: cart }])));
};
const sectionFunctorType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder();
    return b.term(b.pi('K', b.global(category), K =>
        functorType(b, unary(b, displayedCategoryCategory, K), b.global(familyCoefficient)), explicitMode));
};
const internalPiType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    return b.term(displayedMapTypeAt(b, opposite(b, cart), b.global(displayedCategoryFunctor),
        constFamilyAt(b, opposite(b, cart), cart)));
};
const pullbackPiType = (): CoreLfTransferExpression => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    return b.term(b.pi('K', b.global(category), K =>
        b.pi('G', functorType(b, K, opposite(b, cart)), G =>
            displayedMapTypeAt(b, K,
                pulledFamilyAt(b, K, opposite(b, cart), b.global(displayedCategoryFunctor), G),
                constFamilyAt(b, K, cart)), explicitMode), implicitMode));
};

const homClassifierType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'A',
        builder.global(category),
        A => builder.pi(
            'X',
            objectType(builder, A),
            _X => builder.pi(
                'Y',
                objectType(builder, A),
                _Y => builder.global(groupoid),
                explicitMode
            ),
            explicitMode
        ),
        explicitMode
    ));
};

const homClassifierBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'A',
        builder.global(category),
        A => builder.lam(
            'X',
            objectType(builder, A),
            X => builder.lam(
                'Y',
                objectType(builder, A),
                Y => objectClassifierAt(
                    builder,
                    homCategoryAt(builder, A, X, Y)
                ),
                explicitMode
            ),
            explicitMode
        ),
        explicitMode
    ));
};

const source = (sourceFragment: string) => Object.freeze({
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceFragment
});

const modifiers = (
    rigidity: 'ordinary' | 'constant' | 'injective',
    sourceOpacity: 'transparent' | 'opaque'
) => Object.freeze({
    visibility: 'public' as const,
    rigidity,
    sourceOpacity
});

const originalDeclaration = (
    name: string
): CoreLfTransferDeclaration => {
    const declaration =
        CORE_LF_SCALE_STRESS_2B1_MODULE.declarations.find(
            candidate => candidate.symbol.name === name
        );
    if (declaration === undefined) {
        throw new Error(
            `FIBRED-DEPENDENT-TARGET-1 is missing active declaration ` +
                `'${name}'`
        );
    }
    return { ...declaration, provenance: source(`native declaration ${name}`) };
};

const declarations: readonly CoreLfTransferDeclaration[] =
Object.freeze([
    {
        order: 0,
        symbol: homClassifier,
        type: homClassifierType(),
        body: coreLfTransferExplicitBody(homClassifierBody()),
        modifiers: modifiers('injective', 'transparent'),
        provenance: source(
            'injective symbol Hom (A : Cat) (X Y : τ (Obj A)) : Grpd ' +
                '≔ Obj (Hom_cat A X Y)'
        )
    },
    originalDeclaration('Op_cat'),
    originalDeclaration('Functord'),
    {
        order: 0,
        symbol: internalFunctorCategory,
        type: internalFunctorCategoryType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('constant', 'opaque'),
        provenance: source(
            'constant symbol Functor_cat_func : ' +
                'τ (Functor (Op_cat Cat_cat) (Functor_cat Cat_cat Cat_cat))'
        )
    },
    {
        order: 0,
        symbol: partialFunctorCategory,
        type: partialFunctorCategoryType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol Functor_cat_fapp0_func (A : Cat) : ' +
                'τ (Functor Cat_cat Cat_cat)'
        )
    },
    {
        order: 0, symbol: contravariantHom, type: contravariantHomType(),
        body: coreLfTransferAbsentBody(), modifiers: modifiers('injective', 'opaque'),
        provenance: source('injective symbol hom_con [A : Cat] (W : τ (Obj A)) [B : Cat]')
    },
    {
        order: 0, symbol: cartesianInclusion, type: inclusionType(),
        body: coreLfTransferAbsentBody(), modifiers: modifiers('injective', 'opaque'),
        provenance: source('injective symbol Functor_cart_include (A B : Cat)')
    },
    {
        ...originalDeclaration('Catd_cat_func'),
        type: displayedCategoryFunctorType(),
        body: coreLfTransferExplicitBody(displayedCategoryFunctorBody()),
        provenance: source('symbol Catd_cat_func : τ (Functor (Op_cat Cat_cart) Cat_cart)')
    },
    { ...originalDeclaration('Pi_func'), type: sectionFunctorType(),
        provenance: source('injective symbol Pi_func (K : Cat) : τ (Functor (Catd_cat K) Cat_cart)') },
    { ...originalDeclaration('Pi_int_funcd'), type: internalPiType(),
        provenance: source('constant symbol Pi_int_funcd') },
    { ...originalDeclaration('Pi_pullback_funcd'), type: pullbackPiType(),
        provenance: source('injective symbol Pi_pullback_funcd [K : Cat]') }

].map((declaration, order) => Object.freeze({
    ...declaration,
    order
})));

const reusedDeclarationNames = new Set([
    'Pullback_catd',
    'Pullback_catd_func'
]);

const externalSymbols: readonly CoreLfQualifiedSymbol[] =
Object.freeze([
    ...CORE_LF_SCALE_STRESS_2B1_MODULE.externalSymbols.map(
        external => external.symbol
    ),
    homCategory,
    functorCategory,
    functorComposition,
    fixedEvaluation,
    familyCoefficient,
    cartesianFunctorCategory,
    identityFunctor,
    constantFamily,
    transforComponent,
    functorHomAction,
    pullbackFamilyFunctor,
    ...CORE_LF_SCALE_STRESS_2B1_MODULE.declarations
        .filter(declaration =>
            reusedDeclarationNames.has(declaration.symbol.name)
        )
        .map(declaration => declaration.symbol)
].filter((external, index, all) =>
    all.findIndex(other => other.moduleId === external.moduleId && other.name === external.name) === index &&
    !declarations.some(declaration =>
        declaration.symbol.moduleId === external.moduleId && declaration.symbol.name === external.name
    )
));

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE:
CoreLfModuleSpec = createCoreLfModuleSpec({
    revision:
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_REVISION,
    moduleId: MODULE_ID,
    fragmentId: 'fibred-dependent-target-1-signatures',
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256: CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SOURCE_SHA256,
    dependencies: [],
    externalSymbols: externalSymbols.map(external => ({
        symbol: external,
        availability: 'earlier-fragment' as const
    })),
    declarations,
    inductives: [],
    runtimeRules: [],
    proofRules: []
});

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_POLICY:
CoreLfTransferPolicyOverlay = createCoreLfTransferPolicyOverlay(
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE,
    {
        revision:
            'FIBRED-DEPENDENT-TARGET-1-SIGNATURE-POLICY-1',
        moduleRevision:
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE
                .revision,
        entries: declarations.map((declaration, order) => ({
            order,
            target: {
                kind: 'declaration' as const,
                symbol: declaration.symbol
            },
            policy: (
                declaration.symbol.name === 'Hom' ||
                declaration.symbol.name === 'Functord' ||
                declaration.symbol.name === 'Catd_cat_func'
            )
                ? 'checked-transparent-definition' as const
                : 'opaque-signature' as const,
            evidence:
                'Exact active v3.2 declaration required by the frozen ' +
                'dependent-target consumer'
        }))
    }
);

const earlierLinks = [
    ...CORE_CATEGORICAL_FIBRED_WEAKEN_REINDEX_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries,
    ...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries,
    ...CORE_LF_SCALE_STRESS_2B1_LINKAGE.entries
];

const symbolEquals = (
    left: CoreLfQualifiedSymbol,
    right: CoreLfQualifiedSymbol
): boolean =>
    left.moduleId === right.moduleId &&
    left.name === right.name;

const linkFor = (
    target: CoreLfQualifiedSymbol,
    order: number
): CoreLfTransferDeclarationLink => {
    const existing = earlierLinks.find(candidate =>
        symbolEquals(candidate.symbol, target)
    );
    if (existing !== undefined) {
        return Object.freeze({
            ...existing,
            order,
            symbol: Object.freeze({ ...existing.symbol })
        });
    }
    if (!declarations.some(declaration =>
        symbolEquals(declaration.symbol, target)
    )) {
        throw new Error(
            `FIBRED-DEPENDENT-TARGET-1 has no dependency link for ` +
                `${target.moduleId}.${target.name}`
        );
    }
    return Object.freeze({
        order,
        symbol: Object.freeze({ ...target }),
        kind: 'free-declaration' as const,
        coreName:
            `emdash_v3_2_fibred_dependent_target_1_${target.name}`,
        backendName: target.name
    });
};

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE:
CoreLfTransferDeclarationLinkage =
    createCoreLfTransferDeclarationLinkage(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE,
        {
            revision:
                'FIBRED-DEPENDENT-TARGET-1-SIGNATURE-LINKAGE-1',
            moduleRevision:
                CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE
                    .revision,
            entries: [
                ...externalSymbols.map(linkFor),
                ...declarations.map((declaration, index) =>
                    linkFor(
                        declaration.symbol,
                        externalSymbols.length + index
                    )
                )
            ]
        }
    );

const coreNameFor = (target: CoreLfQualifiedSymbol): string => {
    const link =
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE
            .entries.find(candidate =>
                symbolEquals(candidate.symbol, target)
            );
    if (link?.kind !== 'free-declaration') {
        throw new Error(
            `FIBRED-DEPENDENT-TARGET-1 symbol ` +
                `'${target.name}' is not a free Core declaration`
        );
    }
    return link.coreName;
};

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CORE_NAMES =
Object.freeze({
    oppositeCategory: coreNameFor(oppositeCategory),
    displayedFunctorClassifier:
        coreNameFor(displayedFunctorClassifier),
    fixedEvaluation: coreNameFor(fixedEvaluation),
    internalFunctorCategory:
        coreNameFor(internalFunctorCategory),
    partialFunctorCategory:
        coreNameFor(partialFunctorCategory),
    displayedCategoryFunctor:
        coreNameFor(displayedCategoryFunctor),
    sectionCategoryFunctor:
        coreNameFor(sectionCategoryFunctor),
    internalPi: coreNameFor(internalPi),
    pullbackPi: coreNameFor(pullbackPi)
});

const displayedFamilyType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    objectType(
        builder,
        globalCall(builder, displayedCategoryCategory, [{
            plicity: 'explicit',
            value: base
        }])
    );

const fixedEvaluationObjectRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const A = builder.capture('A');
    const B = builder.capture('B');
    const x = builder.capture('x');
    const F = builder.capture('F');
    return {
        order: 0,
        id: 'categorical.dependent-target.fixed-evaluation-object',
        groupId:
            'categorical.dependent-target.fixed-evaluation-object',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'A',
                type: builder.template(builder.global(category))
            },
            {
                name: 'B',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, A))
            },
            {
                name: 'F',
                type: builder.template(functorType(builder, A, B))
            }
        ],
        left: builder.pattern(fapp0(
            builder,
            functorCategoryAt(builder, A, B),
            B,
            globalCall(builder, fixedEvaluation, [
                { plicity: 'implicit', value: A },
                { plicity: 'implicit', value: B },
                { plicity: 'explicit', value: x }
            ]),
            F
        )),
        right: builder.template(fapp0(builder, A, B, F, x)),
        provenance: source(
            'rule fapp0 (fapp0_func $x) $F ↪ fapp0 $F $x'
        )
    };
};

const internalFunctorCategoryFirstRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const A = builder.capture('A');
    const cat = builder.global(categoryOfCategories);
    return {
        order: 0,
        id:
            'categorical.dependent-target.' +
            'functor-category-first-object',
        groupId:
            'categorical.dependent-target.' +
            'functor-category-first-object',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [{
            name: 'A',
            type: builder.template(builder.global(category))
        }],
        left: builder.pattern(fapp0(
            builder,
            opposite(builder, cat),
            functorCategoryAt(builder, cat, cat),
            builder.global(internalFunctorCategory),
            A
        )),
        right: builder.template(globalCall(
            builder,
            partialFunctorCategory,
            [{ plicity: 'explicit', value: A }]
        )),
        provenance: source(
            'rule @fapp0 _ _ Functor_cat_func $A ' +
                '↪ Functor_cat_fapp0_func $A'
        )
    };
};

const internalFunctorCategorySecondRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const A = builder.capture('A');
    const B = builder.capture('B');
    const cat = builder.global(categoryOfCategories);
    return {
        order: 0,
        id:
            'categorical.dependent-target.' +
            'functor-category-second-object',
        groupId:
            'categorical.dependent-target.' +
            'functor-category-second-object',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'A',
                type: builder.template(builder.global(category))
            },
            {
                name: 'B',
                type: builder.template(builder.global(category))
            }
        ],
        left: builder.pattern(fapp0(
            builder,
            cat,
            cat,
            globalCall(builder, partialFunctorCategory, [{
                plicity: 'explicit',
                value: A
            }]),
            B
        )),
        right: builder.template(functorCategoryAt(builder, A, B)),
        provenance: source(
            'rule @fapp0 Cat_cat Cat_cat ' +
                '(Functor_cat_fapp0_func $A) $B ' +
                '↪ Functor_cat $A $B'
        )
    };
};

const sectionFunctorObjectRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const K = builder.capture('K');
    const E = builder.capture('E');
    const displayedCategory = globalCall(
        builder,
        displayedCategoryCategory,
        [{ plicity: 'explicit', value: K }]
    );
    return {
        order: 0,
        id: 'categorical.dependent-target.section-functor-object',
        groupId:
            'categorical.dependent-target.section-functor-object',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'K',
                type: builder.template(builder.global(category))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(builder, K))
            }
        ],
        left: builder.pattern(fapp0(
            builder,
            builder.wildcard(displayedCategory),
            builder.global(familyCoefficient),
            globalCall(builder, sectionCategoryFunctor, [{
                plicity: 'explicit',
                value: K
            }]),
            E
        )),
        right: builder.template(globalCall(
            builder,
            sectionCategory,
            [
                { plicity: 'implicit', value: K },
                { plicity: 'explicit', value: E }
            ]
        )),
        provenance: source(
            'rule @fapp0 _ Cat_cart (@Pi_func $K) $E ' +
                '↪ @Pi_cat $K $E'
        )
    };
};

const originalRuntime = (
    id: string
): CoreLfTransferRuntimeRule => {
    const rule = CORE_LF_SCALE_STRESS_2B1_MODULE.runtimeRules.find(
        candidate => candidate.id === id
    );
    if (rule === undefined) {
        throw new Error(
            `FIBRED-DEPENDENT-TARGET-1 is missing active runtime ` +
                `rule '${id}'`
        );
    }
    const dependentTargetId = id.replace(
        'stress.internal-pi.',
        'categorical.dependent-target.'
    );
    return Object.freeze({
        ...rule,
        id: dependentTargetId,
        groupId: rule.groupId.replace(
            'stress.internal-pi.',
            'categorical.dependent-target.'
        )
    });
};

const contravariantHomObjectRule = (): CoreLfTransferRuntimeRule => {
    const b = new CoreLfTransferScopedBuilder();
    const A = b.capture('A'), W = b.capture('W'), B = b.capture('B'), F = b.capture('F'), x = b.capture('x');
    return {
        order: 0, id: 'categorical.dependent-target.hom-con-object',
        groupId: 'categorical.dependent-target.hom-con-object', clauseOrder: 0, sourceOwner: functorObject,
        variables: [
            { name: 'A', type: b.template(b.global(category)) },
            { name: 'W', type: b.template(objectType(b, A)) },
            { name: 'B', type: b.template(b.global(category)) },
            { name: 'F', type: b.template(functorType(b, B, A)) },
            { name: 'x', type: b.template(objectType(b, B)) }
        ],
        left: b.pattern(fapp0(b, b.wildcard(opposite(b, B)), b.global(familyCoefficient), homConAt(b, A, W, B, F), x)),
        right: b.template(homCategoryAt(b, A, fapp0(b, B, A, F, x), W)),
        provenance: source('rule @fapp0 _ Cat_cart (@hom_con $A $W $B $F) $x')
    };
};
const inclusionAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    B: CoreLfTransferBuilderExpression) => globalCall(b, cartesianInclusion, [
        { plicity: 'explicit', value: A }, { plicity: 'explicit', value: B }
    ]);
const inclusionObjectRule = (): CoreLfTransferRuntimeRule => {
    const b = new CoreLfTransferScopedBuilder();
    const A = b.capture('A'), B = b.capture('B'), F = b.capture('F');
    return {
        order: 0, id: 'categorical.dependent-target.cartesian-inclusion-object',
        groupId: 'categorical.dependent-target.cartesian-inclusion-object', clauseOrder: 0, sourceOwner: functorObject,
        variables: [
            ...['A', 'B'].map(name => ({ name, type: b.template(b.global(category)) })),
            { name: 'F', type: b.template(functorType(b, A, B)) }
        ],
        // Native inferred slots are wildcards. In particular the codomain
        // may be the proof-equal Catd presentation after Pi composition.
        left: b.pattern(fapp0(b, b.wildcard(cartesianAt(b, A, B)),
            b.wildcard(functorCategoryAt(b, A, B)), inclusionAt(b, A, B), F)),
        right: b.template(F), provenance: source('rule @fapp0 _ _ (Functor_cart_include _ _) $F ↪ $F')
    };
};
const constantPullbackRule = (): CoreLfTransferRuntimeRule => {
    const b = new CoreLfTransferScopedBuilder();
    const A = b.capture('A'), B = b.capture('B'), C = b.capture('C'), F = b.capture('F');
    return {
        order: 0, id: 'categorical.dependent-target.constant-pullback',
        groupId: 'categorical.dependent-target.constant-pullback', clauseOrder: 0, sourceOwner: pullbackFamily,
        variables: [
            ...['A', 'B', 'C'].map(name => ({ name, type: b.template(b.global(category)) })),
            { name: 'F', type: b.template(functorType(b, A, B)) }
        ],
        left: b.pattern(pulledFamilyAt(b, A, B, constFamilyAt(b, B, C), F)),
        right: b.template(constFamilyAt(b, A, C)),
        provenance: source('rule @Pullback_catd $A $B (@Const_catd $B $C) $F')
    };
};
const pullbackPiAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    G: CoreLfTransferBuilderExpression) => globalCall(b, pullbackPi, [
        { plicity: 'implicit', value: K }, { plicity: 'explicit', value: G }
    ]);
const componentAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    E: CoreLfTransferBuilderExpression, D: CoreLfTransferBuilderExpression,
    x: CoreLfTransferBuilderExpression, FF: CoreLfTransferBuilderExpression) =>
    globalCall(b, transforComponent, [
        { plicity: 'implicit', value: K }, { plicity: 'implicit', value: b.global(familyCoefficient) },
        { plicity: 'implicit', value: E }, { plicity: 'implicit', value: D },
        { plicity: 'explicit', value: x }, { plicity: 'explicit', value: FF }
    ]);
const includedPiAt = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression) => {
    const cart = b.global(familyCoefficient);
    return globalCall(b, functorComposition, [
        { plicity: 'implicit', value: cartesianAt(b, K, cart) },
        { plicity: 'implicit', value: unary(b, displayedCategoryCategory, K) },
        { plicity: 'implicit', value: cart },
        { plicity: 'explicit', value: unary(b, sectionCategoryFunctor, K) },
        { plicity: 'explicit', value: inclusionAt(b, K, cart) }
    ]);
};
const piComponentRule = (pulled: boolean): CoreLfTransferRuntimeRule => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    const K = b.capture('K'), G = b.capture('G'), x = b.capture('x');
    const base = pulled ? K : opposite(b, cart);
    const point = pulled ? x : K;
    const family = pulled ? pulledFamilyAt(b, K, opposite(b, cart), b.global(displayedCategoryFunctor), G)
        : b.global(displayedCategoryFunctor);
    const at = pulled ? fapp0(b, K, opposite(b, cart), G, x) : K;
    const id = 'categorical.dependent-target.' + (pulled ? 'pullback-component' : 'package-component');
    return {
        order: 0, id, groupId: id, clauseOrder: 0, sourceOwner: transforComponent,
        variables: [
            { name: 'K', type: b.template(b.global(category)) },
            ...(pulled ? [
                { name: 'G', type: b.template(functorType(b, K, opposite(b, cart))) },
                { name: 'x', type: b.template(objectType(b, K)) }
            ] : [])
        ],
        left: b.pattern(componentAt(b, base, family, constFamilyAt(b, base, cart), point,
            pulled ? pullbackPiAt(b, K, G) : b.global(internalPi))),
        right: b.template(includedPiAt(b, at)),
        provenance: source(pulled
            ? 'rule @tapp0_fapp0 $K Cat_cart _ _ $x (@Pi_pullback_funcd $K $G)'
            : 'rule @tapp0_fapp0 (Op_cat Cat_cart) Cat_cart _ _ $K Pi_int_funcd')
    };
};
const piPullbackFoldRule = (): CoreLfTransferRuntimeRule => {
    const b = new CoreLfTransferScopedBuilder(), cart = b.global(familyCoefficient);
    const K = b.capture('K'), G = b.capture('G'), base = opposite(b, cart);
    const sourceFamily = b.global(displayedCategoryFunctor), targetFamily = constFamilyAt(b, base, cart);
    const pull = globalCall(b, pullbackFamilyFunctor, [
        { plicity: 'implicit', value: K }, { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: G }
    ]);
    return {
        order: 0, id: 'categorical.dependent-target.pullback-fold',
        groupId: 'categorical.dependent-target.pullback-fold', clauseOrder: 0, sourceOwner: functorHomAction,
        variables: [
            { name: 'K', type: b.template(b.global(category)) },
            { name: 'G', type: b.template(functorType(b, K, base)) }
        ],
        left: b.pattern(globalCall(b, functorHomAction, [
            { plicity: 'implicit', value: unary(b, displayedCategoryCategory, base) },
            { plicity: 'implicit', value: unary(b, displayedCategoryCategory, K) },
            { plicity: 'explicit', value: pull },
            { plicity: 'implicit', value: sourceFamily }, { plicity: 'implicit', value: targetFamily },
            { plicity: 'explicit', value: b.global(internalPi) }
        ])),
        right: b.template(pullbackPiAt(b, K, G)),
        provenance: source('rule @fapp1_fapp0 (@Catd_cat (Op_cat Cat_cart)) _ (@Pullback_catd_func $K (Op_cat Cat_cart) $G) _ _ Pi_int_funcd')
    };
};

const runtimeRules: readonly CoreLfTransferRuntimeRule[] = Object.freeze([
    originalRuntime('stress.internal-pi.opposite-object'),
    fixedEvaluationObjectRule(),
    internalFunctorCategoryFirstRule(),
    internalFunctorCategorySecondRule(),
    constantPullbackRule(),
    sectionFunctorObjectRule(),
    contravariantHomObjectRule(),
    inclusionObjectRule(),
    piComponentRule(false),
    piPullbackFoldRule(),
    piComponentRule(true)
].map((rule, order) => Object.freeze({ ...rule, order })));

const runtimeModuleFor = (
    suffix: string,
    rules: readonly CoreLfTransferRuntimeRule[]
): CoreLfModuleSpec => createCoreLfModuleSpec({
    revision: `FIBRED-DEPENDENT-TARGET-1-${suffix}-D060-1`,
    moduleId: MODULE_ID,
    fragmentId:
        `fibred-dependent-target-1-${suffix.toLowerCase()}`,
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256: CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SOURCE_SHA256,
    dependencies: [],
    externalSymbols: [
        ...externalSymbols,
        ...declarations.map(declaration => declaration.symbol)
    ].map(external => ({
        symbol: external,
        availability: 'earlier-fragment' as const
    })),
    declarations: [],
    inductives: [],
    runtimeRules: rules.map((rule, order) => Object.freeze({
        ...rule,
        order
    })),
    proofRules: []
});

const runtimePolicyFor = (
    module: CoreLfModuleSpec
): CoreLfTransferPolicyOverlay =>
    createCoreLfTransferPolicyOverlay(module, {
        revision: `${module.revision}-POLICY-1`,
        moduleRevision: module.revision,
        entries: module.runtimeRules.map((rule, order) => ({
            order,
            target: {
                kind: 'runtime-rule' as const,
                id: rule.id
            },
            policy: 'runtime-rewrite' as const,
            evidence:
                'Exact active v3.2 runtime clause required by the ' +
                'frozen dependent-target consumer'
        }))
    });

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_MODULE =
    runtimeModuleFor(
        'PREREQUISITE-RUNTIME',
        runtimeRules.slice(0, 8)
    );

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_POLICY =
    runtimePolicyFor(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_MODULE
    );

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_MODULE =
    runtimeModuleFor(
        'CONSUMER-RUNTIME',
        runtimeRules.slice(8)
    );

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_POLICY =
    runtimePolicyFor(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_MODULE
    );

const categoryPresentationRule = () => {
    const builder = new CoreLfTransferScopedBuilder();
    const K = builder.capture('K');
    const K2 = builder.capture('K2');
    return {
        order: 0,
        id: 'categorical.dependent-target.category-presentation',
        sourceOwner: functorCategory,
        variables: [
            {
                name: 'K',
                role: 'matched' as const,
                type: builder.template(builder.global(category))
            },
            {
                name: 'K2',
                role: 'matched' as const,
                type: builder.template(builder.global(category))
            }
        ],
        problem: {
            left: builder.pattern(functorCategoryAt(
                builder,
                K,
                builder.global(familyCoefficient)
            )),
            right: builder.pattern(globalCall(
                builder,
                displayedCategoryCategory,
                [{ plicity: 'explicit', value: K2 }]
            ))
        },
        generatedConstraints: [{
            left: builder.template(K),
            right: builder.template(K2)
        }],
        provenance: source(
            'unif_rule Functor_cat $K Cat_cart ≡ @Catd_cat $K2 ' +
                '↪ [ $K ≡ $K2 ]'
        )
    };
};

const proofRule = categoryPresentationRule();

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE:
CoreLfModuleSpec = createCoreLfModuleSpec({
    revision: 'FIBRED-DEPENDENT-TARGET-1-PROOF-1',
    moduleId: MODULE_ID,
    fragmentId: 'fibred-dependent-target-1-proof',
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256: CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SOURCE_SHA256,
    dependencies: [],
    externalSymbols: [
        category,
        familyCoefficient,
        functorCategory,
        displayedCategoryCategory
    ].map(external => ({
        symbol: external,
        availability: 'earlier-fragment' as const
    })),
    declarations: [],
    inductives: [],
    runtimeRules: [],
    proofRules: [proofRule]
});

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY:
CoreLfTransferPolicyOverlay = createCoreLfTransferPolicyOverlay(
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,
    {
        revision:
            'FIBRED-DEPENDENT-TARGET-1-PROOF-POLICY-1',
        moduleRevision:
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE
                .revision,
        entries: [{
            order: 0,
            target: {
                kind: 'proof-rule' as const,
                id: proofRule.id
            },
            policy: 'proof-unification' as const,
            evidence:
                'Exact active category-presentation unification rule; ' +
                'the two category heads remain runtime-distinct'
        }]
    }
);

export const
CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_BOUNDARY =
Object.freeze({
    status:
        'root-only-existing-authority-dependent-target-closure',
    contractRevision:
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT.revision,
    declarationNames: Object.freeze(
        declarations.map(declaration => declaration.symbol.name)
    ),
    runtimeRuleIds: Object.freeze(
        runtimeRules.map(rule => rule.id)
    ),
    proofRuleIds: Object.freeze([proofRule.id]),
    declarationCount: declarations.length,
    runtimeRuleCount: runtimeRules.length,
    prerequisiteRuntimeRuleCount: 8,
    consumerRuntimeRuleCount: 3,
    inheritedRuntimeRuleIds: Object.freeze([
        'categorical.displayed-hom-category.reduce'
    ]),
    inheritedRuntimeRuleCount: 1,
    directlyCheckedRuntimeRuleCount: 9,
    proofCheckedRuntimeRuleCount: 2,
    proofCheckedRuntimeRuleIds: Object.freeze([
        'categorical.dependent-target.package-component',
        'categorical.dependent-target.pullback-component'
    ]),
    proofSubjectExternalOracleUsed: false,
    runtimeCategoryPresentationCollapseInstalled: false,
    newMathematicalOwnerCount: 0,
    newMathematicalRuntimeRuleCount: 0,
    newMathematicalProofRuleCount: 0,
    allEntriesUseGenericTransferEngines: true,
    doesNotProvide:
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONTRACT
            .doesNotProvide
});

export interface CoreCategoricalFibredDependentTargetCompilation {
    readonly prerequisite:
        CoreCategoricalFibredWeakenReindexCompilation;
    readonly compiled: CoreLfCompiledDeclarationModule;
    readonly declarationContext: CoreLfMixedDeclarationContext;
    readonly prerequisiteRuntimeFragment:
        CoreLfCompiledRuntimeFragment;
    readonly consumerRuntimeFragment:
        CoreLfCompiledRuntimeFragment;
    readonly composedRuntime: CoreLfComposedRuntimeProgram;
    readonly proofProgram: CoreLfCompiledProofProgram;
}

let cachedCompilation:
    CoreCategoricalFibredDependentTargetCompilation | undefined;

export function compileCoreCategoricalFibredDependentTargetTransfer():
CoreCategoricalFibredDependentTargetCompilation {
    if (cachedCompilation !== undefined) return cachedCompilation;
    validateCoreCategoricalFibredDependentTargetContract();
    validateCoreLfScaleEngineReview();
    const prerequisite =
        compileCoreCategoricalFibredWeakenReindexTransfer();
    const initialCompiled = compileCoreLfDeclarations(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_POLICY,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE,
        {
            initialEnvironment: prerequisite.compiled.environment,
            runtimeProgram: prerequisite.composedRuntime
        }
    );
    const initialContext = new CoreLfMixedDeclarationContext(
        prerequisite.declarationContext,
        [initialCompiled]
    );
    const inheritedRuntimeFragment = new CoreLfCompiledRuntimeFragment(
        prerequisite.runtime,
        [],
        prerequisite.composedRuntime
    );
    const prerequisiteRuntimeFragment =
        compileCoreLfRuntimeFragment(
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_MODULE,
            CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PREREQUISITE_RUNTIME_POLICY,
            initialContext,
            {
                dependencies: [{
                    relation: 'earlier-fragment',
                    fragment: inheritedRuntimeFragment
                }]
            }
        );
    const subjectProofProgram = compileCoreLfProofProgram(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY,
        initialContext,
        {
            runtimeProgram: prerequisiteRuntimeFragment.runtime
        }
    );
    const consumerRuntimeFragment = compileCoreLfRuntimeFragment(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_CONSUMER_RUNTIME_POLICY,
        initialContext,
        {
            dependencies: [{
                relation: 'earlier-fragment',
                fragment: prerequisiteRuntimeFragment
            }],
            subjectReductionProof: {
                program: subjectProofProgram,
                rules: [
                    {
                        runtimeRuleId:
                            'categorical.dependent-target.' +
                            'package-component',
                        proofRuleIds: [proofRule.id],
                        allowArgumentConversion: true
                    },
                    {
                        runtimeRuleId:
                            'categorical.dependent-target.' +
                            'pullback-component',
                        proofRuleIds: [proofRule.id],
                        allowArgumentConversion: true
                    }
                ]
            }
        }
    );
    const compiled = compileCoreLfDeclarations(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_POLICY,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE,
        {
            initialEnvironment: prerequisite.compiled.environment,
            runtimeProgram: consumerRuntimeFragment.runtime
        }
    );
    const declarationContext = new CoreLfMixedDeclarationContext(
        prerequisite.declarationContext,
        [compiled]
    );
    /*
     * The consumer rules were subject-checked with the source-time proof
     * program above. Recompile the same proof rule against the final
     * declaration objects and composed runtime returned to callers. This
     * preserves the proof compiler's exact-prefix invariant after the
     * required final declaration recheck; it does not weaken opaque-
     * extension validation or add a proof/runtime rule.
     */
    const proofProgram = compileCoreLfProofProgram(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY,
        declarationContext,
        {
            runtimeProgram: consumerRuntimeFragment.runtime
        }
    );
    cachedCompilation = Object.freeze({
        prerequisite,
        compiled,
        declarationContext,
        prerequisiteRuntimeFragment,
        consumerRuntimeFragment,
        composedRuntime: consumerRuntimeFragment.runtime,
        proofProgram
    });
    return cachedCompilation;
}
