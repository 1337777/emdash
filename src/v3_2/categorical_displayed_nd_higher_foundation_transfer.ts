/** Current native Q-valued Homd foundation transfer.
 * The historical D-019/D-020 records remain separate. Source-prior duality,
 * native target definitions and precomposition projections precede the two
 * checked relative-root definitions. No native kernel rule is added.
 * Homd_target_con_func now has its native composition body. The complete
 * lower P-index endpoint computation still needs its represented-action closure.
 */

import {
    CORE_CATEGORICAL_DISPLAYED_CHAIN_2A_CLOSURE_TRANSFER_LINKAGE
} from './categorical_displayed_chain_2a_closure_transfer';
import {
    CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE
} from './categorical_fibred_transfd_transfer';
import {
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT
} from './categorical_displayed_nd_higher_audit';
import {
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_CORE_NAMES,
    CoreCategoricalDisplayedNdHigherFoundationSymbolId,
    coreCategoricalDisplayedNdHigherFoundationCoreName
} from './categorical_displayed_nd_higher_foundation_contract';
import {
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_REVIEW,
    validateCoreCategoricalDisplayedNdHigherReview
} from './categorical_displayed_nd_higher_review';
import {
    coreDirectedContinuationTransferSymbol,
    CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE
} from './directed_continuation_transfer';
import {
    CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE
} from './categorical_structural_transfer';
import { CORE_HOMD_DUALITY_LINKAGE, compileCoreHomdDualityTransfer } from './categorical_homd_duality_transfer';
import { CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE } from './categorical_fibred_product_transfer';
import { CORE_CATEGORICAL_FIBRED_STRUCTURE_TRANSFER_LINKAGE } from './categorical_fibred_structure_transfer';
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
    CoreLfCompiledRuntimeFragment,
    CoreLfCompiledRuntimeProgram,
    CoreLfComposedRuntimeProgram,
    compileCoreLfRuntimeFragment
} from './lf_transfer_runtime';
import {
    binderMode, KernelExpression, Provenance, kernelApplication, kernelCall, kernelFree
} from './kernel';
import {
    CoreOwnerId
} from './schema';
import {
    CORE_LF_SCALE_STRESS_3A2A_MODULE
} from './scale_stress_3a2a_representation';

export {
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_CORE_NAMES,
    coreCategoricalDisplayedNdHigherFoundationCoreName
};
export type {
    CoreCategoricalDisplayedNdHigherFoundationSymbolId
};

const MODULE_ID = 'emdash.emdash3_2';

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_REVISION =
    'DISPLAYED-ND-HIGHER-FOUNDATION-1A-GENERIC-TRANSFER-D057-1' as const;

const category =
    coreDirectedContinuationTransferSymbol('category-universe');
const decodeOwner =
    coreDirectedContinuationTransferSymbol('decode');
const objectClassifier =
    coreDirectedContinuationTransferSymbol('object-classifier');
const homClassifier =
    coreDirectedContinuationTransferSymbol('hom-classifier');
const functorClassifier =
    coreDirectedContinuationTransferSymbol('functor-classifier');
const categoryOfCategories =
    coreDirectedContinuationTransferSymbol('category-of-categories');
const familyCoefficient = coreDirectedContinuationTransferSymbol('cartesian-category-coefficient');
const displayedCategoryCategory =
    coreDirectedContinuationTransferSymbol(
        'displayed-category-category'
    );
const functorObject =
    coreDirectedContinuationTransferSymbol('functor-object');
const constantDisplayedFamily =
    coreDirectedContinuationTransferSymbol(
        'constant-displayed-family'
    );

const symbol = (name: string): CoreLfQualifiedSymbol =>
    coreLfQualifiedSymbol(MODULE_ID, name);
const coAt2Category = symbol('CoAt2_cat');
const coAt2Functor = symbol('CoAt2_func');
const cartesianFunctorCategory = symbol('Functor_cart_cat');
const identityFunctor = symbol('id_func');
const representedHom = symbol('hom_');
const homdCoefficient = symbol('Homd_coeff_cat');
const homdInclude = symbol('Homd_coeff_include');
const homdDiagram = symbol('Homd_coeff_diagram');
const homdRepresentable = symbol('Homd_representable_func');
const precompAlong = symbol('hom_precomp_along_func');
const precompPoint = symbol('hom_precomp_along_fapp0');
const postcompFunctor = symbol('hom_postcomp_func');
const postcompPoint = symbol('hom_postcomp_fapp0');
const functorHomFull = coreDirectedContinuationTransferSymbol('functor-hom-full');
const homdTargetIndex = symbol('Homd_target_index_func');
const homdTargetCon = symbol('Homd_target_con_func');
const homdTargetMap = symbol('Homd_target_map');
const homdIdentity = symbol('homd_id_int');
const homdRelative = symbol('homd_rel_cart_int');
const strictTransforView = symbol('strict_transfor');
const transforCategory = symbol('Transf_cat');

const displayedFamilyClassifier = symbol('Catd');
const displayedFunctorClassifier = symbol('Functord');
const ordinaryComposition = symbol('comp_fapp0');
const oppositeCategory = symbol('Op_cat');
const functorCategory = symbol('Functor_cat');
const functorEvaluation = symbol('fapp0_func');
const functorComposition = symbol('comp_cat_fapp0');
const sectionCategoryFunctor = symbol('Pi_func');

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_SYMBOLS =
Object.freeze({
    identityArrow: symbol('id'),
    displayedComposition: symbol('comp_catd_fapp0'),
    oppositeFunctor: symbol('Op_func'),
    displayedOppositeFunctor: symbol('Op_catd_func'),
    internalHom: symbol('hom_int'),
    displayedOpposite: symbol('Op_catd'),
    displayedOppositeAction: symbol('Op_funcd'),
    mixedFunctorFamily: symbol('Functor_catd_func'),
    edgeFamily: symbol('Edge_catd_func'),
    presheafFamily: symbol('Presheaf_catd_func'),
    homPresheafFamily: symbol('HomPresheaf_catd_func'),
    displayedHomTarget: symbol('Homd_target_catd'),
    displayedInternalHom: symbol('homd_int')
});

const {
    identityArrow,
    displayedComposition,
    oppositeFunctor,
    displayedOppositeFunctor,
    internalHom,
    displayedOpposite,
    displayedOppositeAction,
    mixedFunctorFamily,
    edgeFamily,
    presheafFamily,
    homPresheafFamily,
    displayedHomTarget,
    displayedInternalHom
} = CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_SYMBOLS;

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

const functorType = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, functorClassifier, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]));

const displayedFamilyType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, displayedFamilyClassifier, [{
        plicity: 'explicit',
        value: base
    }]));

const displayedFunctorType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, displayedFunctorClassifier, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]));

const opposite = (
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

const functorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorCategory, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const constantFamily = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    fibre: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, constantDisplayedFamily, [
        { plicity: 'explicit', value: base },
        { plicity: 'explicit', value: fibre }
    ]);

const identityAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    object: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, identityArrow, [
        { plicity: 'explicit', value: base },
        { plicity: 'explicit', value: object }
    ]);

const ordinaryComposeAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    middle: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    outer: CoreLfTransferBuilderExpression,
    inner: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, ordinaryComposition, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: middle },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: outer },
        { plicity: 'explicit', value: inner }
    ]);

const functorComposeAt = (
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

const displayedComposeAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    middle: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    outer: CoreLfTransferBuilderExpression,
    inner: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedComposition, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: middle },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: outer },
        { plicity: 'explicit', value: inner }
    ]);

const oppositeFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, oppositeFunctor, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: functor }
    ]);

const displayedOppositeAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedOpposite, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: family }
    ]);

const internalHomAt = (
    builder: CoreLfTransferScopedBuilder,
    target: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, internalHom, [
        { plicity: 'implicit', value: target },
        { plicity: 'implicit', value: source },
        { plicity: 'explicit', value: functor }
    ]);

const displayedOppositeFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedOppositeFunctor, [{
        plicity: 'explicit',
        value: base
    }]);

const mixedFunctorFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, mixedFunctorFamily, [{
        plicity: 'explicit',
        value: base
    }]);

const edgeFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, edgeFamily, [{
        plicity: 'implicit',
        value: base
    }]);

const presheafFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, presheafFamily, [{
        plicity: 'explicit',
        value: base
    }]);

const homPresheafFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, homPresheafFamily, [{
        plicity: 'implicit',
        value: base
    }]);

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

const functorEvaluationAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    object: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorEvaluation, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: object }
    ]);

const sectionCategoryFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, sectionCategoryFunctor, [{
        plicity: 'explicit',
        value: base
    }]);

const source = (
    sourceFragment: string,
    canonicalCommandOrdinal?: number
) => ({
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceFragment,
    canonicalCommandOrdinal
});

const modifiers = (
    rigidity: 'ordinary' | 'injective',
    sourceOpacity: 'transparent' | 'opaque'
) => ({
    visibility: 'public' as const,
    rigidity,
    sourceOpacity
});

const priorIdentityDeclaration =
    CORE_LF_SCALE_STRESS_3A2A_MODULE.declarations.find(declaration =>
        declaration.symbol.moduleId === identityArrow.moduleId &&
        declaration.symbol.name === identityArrow.name
    );

if (priorIdentityDeclaration === undefined) {
    throw new Error(
        'SCALE-STRESS-3A2A no longer exposes the exact id declaration'
    );
}

const displayedCompositionType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'K',
        builder.global(category),
        K => builder.pi(
            'E',
            displayedFamilyType(builder, K),
            E => builder.pi(
                'D',
                displayedFamilyType(builder, K),
                D => builder.pi(
                    'C',
                    displayedFamilyType(builder, K),
                    C => builder.pi(
                        'FF',
                        displayedFunctorType(builder, K, D, C),
                        FF => builder.pi(
                            'GG',
                            displayedFunctorType(builder, K, E, D),
                            _GG => displayedFunctorType(
                                builder,
                                K,
                                E,
                                C
                            ),
                            explicitMode
                        ),
                        explicitMode
                    ),
                    implicitMode
                ),
                implicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const displayedCompositionBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'K',
        builder.global(category),
        K => builder.lam(
            'E',
            displayedFamilyType(builder, K),
            E => builder.lam(
                'D',
                displayedFamilyType(builder, K),
                D => builder.lam(
                    'C',
                    displayedFamilyType(builder, K),
                    C => builder.lam(
                        'FF',
                        displayedFunctorType(builder, K, D, C),
                        FF => builder.lam(
                            'GG',
                            displayedFunctorType(builder, K, E, D),
                            GG => ordinaryComposeAt(
                                builder,
                                displayedCategoryAt(builder, K),
                                E,
                                D,
                                C,
                                FF,
                                GG
                            ),
                            explicitMode
                        ),
                        explicitMode
                    ),
                    implicitMode
                ),
                implicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const oppositeFunctorType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'A',
        builder.global(category),
        A => builder.pi(
            'B',
            builder.global(category),
            B => builder.pi(
                'F',
                functorType(builder, A, B),
                _F => functorType(
                    builder,
                    opposite(builder, A),
                    opposite(builder, B)
                ),
                explicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const coAt2At = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression) =>
    globalCall(b, coAt2Category, [{ plicity: 'explicit', value:A }]);
const cartAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression, B: CoreLfTransferBuilderExpression) =>
    globalCall(b, cartesianFunctorCategory, [{ plicity:'explicit',value:A },{ plicity:'explicit',value:B }]);
const homAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    X: CoreLfTransferBuilderExpression, Y: CoreLfTransferBuilderExpression) =>
    globalCall(b,symbol('Hom_cat'),[{plicity:'explicit',value:A},{plicity:'explicit',value:X},{plicity:'explicit',value:Y}]);
const cartMapType = (b: CoreLfTransferScopedBuilder, K: CoreLfTransferBuilderExpression,
    E: CoreLfTransferBuilderExpression, D: CoreLfTransferBuilderExpression) =>
    decode(b,globalCall(b,homClassifier,[
        {plicity:'explicit',value:cartAt(b,K,b.global(familyCoefficient))},
        {plicity:'explicit',value:E},{plicity:'explicit',value:D}]));
const coAt2Map = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    B: CoreLfTransferBuilderExpression, F: CoreLfTransferBuilderExpression) =>
    globalCall(b,coAt2Functor,[{plicity:'implicit',value:A},{plicity:'implicit',value:B},{plicity:'explicit',value:F}]);

const displayedOppositeFunctorType = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    return b.term(b.pi('Z',b.global(category),Z=>functorType(b,
        coAt2At(b,cartAt(b,Z,cart)),cartAt(b,coAt2At(b,Z),cart)),explicitMode));
};

const internalHomType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'A',
        builder.global(category),
        A => builder.pi(
            'B',
            builder.global(category),
            B => builder.pi(
                'F',
                functorType(builder, B, A),
                _F => functorType(
                    builder,
                    opposite(builder, A),
                    cartAt(builder, B, builder.global(familyCoefficient))
                ),
                explicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const displayedOppositeType = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder();
    return b.term(b.pi('K',b.global(category),K=>b.pi('E',displayedFamilyType(b,K),
        ()=>displayedFamilyType(b,coAt2At(b,K)),explicitMode),implicitMode));
};
const displayedOppositeActionType = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder();
    return b.term(b.pi('K',b.global(category),K=>b.pi('E',displayedFamilyType(b,K),E=>
        b.pi('D',displayedFamilyType(b,K),D=>b.pi('U',cartMapType(b,K,E,D),()=>
            cartMapType(b,coAt2At(b,K),displayedOppositeAt(b,K,E),displayedOppositeAt(b,K,D)),explicitMode),
            implicitMode),implicitMode),implicitMode));
};

const mixedFunctorFamilyType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'K',
        builder.global(category),
        K => functorType(
            builder,
            opposite(
                builder,
                cartAt(builder, opposite(builder, K), builder.global(familyCoefficient))
            ),
            functorCategoryAt(
                builder,
                displayedCategoryAt(builder, K),
                displayedCategoryAt(builder, K)
            )
        ),
        explicitMode
    ));
};

const edgeFamilyType = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    return b.term(b.pi('Z',b.global(category),Z=>functorType(b,
        coAt2At(b,opposite(b,Z)),cartAt(b,coAt2At(b,Z),cart)),implicitMode));
};
const edgeFamilyBody = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    return b.term(b.lam('Z',b.global(category),Z=>functorComposeAt(b,
        coAt2At(b,opposite(b,Z)),coAt2At(b,cartAt(b,Z,cart)),cartAt(b,coAt2At(b,Z),cart),
        displayedOppositeFunctorAt(b,Z),coAt2Map(b,opposite(b,Z),cartAt(b,Z,cart),
            internalHomAt(b,Z,Z,identityAt(b,b.global(categoryOfCategories),Z)))),implicitMode));
};

const presheafFamilyType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'K',
        builder.global(category),
        K => functorType(
            builder,
            opposite(
                builder,
                cartAt(builder, opposite(builder, K), builder.global(familyCoefficient))
            ),
            displayedCategoryAt(builder, K)
        ),
        explicitMode
    ));
};

const presheafFamilyBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'K',
        builder.global(category),
        K => {
            const source = opposite(
                builder,
                cartAt(builder, opposite(builder, K), builder.global(familyCoefficient))
            );
            const middle = functorCategoryAt(
                builder,
                displayedCategoryAt(builder, K),
                displayedCategoryAt(builder, K)
            );
            const target = displayedCategoryAt(builder, K);
            return functorComposeAt(
                builder,
                source,
                middle,
                target,
                functorEvaluationAt(
                    builder,
                    displayedCategoryAt(builder, K),
                    displayedCategoryAt(builder, K),
                    constantFamily(
                        builder,
                        K,
                        builder.global(familyCoefficient)
                    )
                ),
                mixedFunctorFamilyAt(builder, K)
            );
        },
        explicitMode
    ));
};

const homPresheafFamilyType = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder();
    return b.term(b.pi('Z',b.global(category),Z=>functorType(b,coAt2At(b,Z),
        displayedCategoryAt(b,opposite(b,coAt2At(b,Z)))),implicitMode));
};
const homPresheafFamilyBody = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    return b.term(b.lam('Z',b.global(category),Z=>{
        const c2Z=coAt2At(b,Z), inner=cartAt(b,c2Z,cart);
        return functorComposeAt(b,c2Z,opposite(b,inner),displayedCategoryAt(b,opposite(b,c2Z)),
            globalCall(b,presheafFamily,[{plicity:'explicit',value:opposite(b,c2Z)}]),
            oppositeFunctorAt(b,coAt2At(b,opposite(b,Z)),inner,
                globalCall(b,edgeFamily,[{plicity:'implicit',value:Z}])));
    },implicitMode));
};

const displayedHomTargetType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'E',
            displayedFamilyType(builder, Z),
            _E => displayedFamilyType(builder, Z),
            explicitMode
        ),
        implicitMode
    ));
};

const idFunctorAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression) =>
    globalCall(b,identityFunctor,[{plicity:'implicit',value:A}]);
const representedAt = (b: CoreLfTransferScopedBuilder, A: CoreLfTransferBuilderExpression,
    B: CoreLfTransferBuilderExpression,F: CoreLfTransferBuilderExpression,W: CoreLfTransferBuilderExpression) =>
    globalCall(b,representedHom,[{plicity:'implicit',value:A},{plicity:'implicit',value:B},
        {plicity:'explicit',value:F},{plicity:'explicit',value:W}]);
const diagramAt = (b: CoreLfTransferScopedBuilder,K: CoreLfTransferBuilderExpression,E: CoreLfTransferBuilderExpression) =>
    globalCall(b,homdDiagram,[{plicity:'implicit',value:K},{plicity:'explicit',value:E}]);
const homdRepresentableAt = (b: CoreLfTransferScopedBuilder,K: CoreLfTransferBuilderExpression) =>
    globalCall(b,homdRepresentable,[{plicity:'explicit',value:K}]);
const homdBaseMap = (b: CoreLfTransferScopedBuilder,K: CoreLfTransferBuilderExpression) =>
    coAt2Map(b,coAt2At(b,K),functorCategoryAt(b,K,b.global(homdCoefficient)),homdRepresentableAt(b,K));
const displayedHomTargetBody = (): CoreLfTransferExpression => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    return b.term(b.lam('K',b.global(category),K=>b.lam('E',displayedFamilyType(b,K),E=>{
        const A=coAt2At(b,functorCategoryAt(b,K,b.global(homdCoefficient)));
        return functorComposeAt(b,K,A,cart,representedAt(b,A,A,idFunctorAt(b,A),diagramAt(b,K,E)),homdBaseMap(b,K));
    },explicitMode),implicitMode));
};

const objectTypeAt = (b:CoreLfTransferScopedBuilder,A:CoreLfTransferBuilderExpression)=>
    decode(b,globalCall(b,objectClassifier,[{plicity:'explicit',value:A}]));
const targetAt = (b:CoreLfTransferScopedBuilder,K:CoreLfTransferBuilderExpression,E:CoreLfTransferBuilderExpression)=>
    globalCall(b,displayedHomTarget,[{plicity:'implicit',value:K},{plicity:'explicit',value:E}]);
const indexAt = (b:CoreLfTransferScopedBuilder,K:CoreLfTransferBuilderExpression)=>
    globalCall(b,homdTargetIndex,[{plicity:'explicit',value:K}]);
const indexFamilyAt = (b:CoreLfTransferScopedBuilder,K:CoreLfTransferBuilderExpression,E:CoreLfTransferBuilderExpression)=>
    functorObjectAt(b,opposite(b,coAt2At(b,functorCategoryAt(b,K,b.global(homdCoefficient)))),
        cartAt(b,K,b.global(familyCoefficient)),indexAt(b,K),diagramAt(b,K,E));
const familyMapTelescope = (body:boolean, result:(b:CoreLfTransferScopedBuilder,K:CoreLfTransferBuilderExpression,
    D:CoreLfTransferBuilderExpression,E:CoreLfTransferBuilderExpression,FF:CoreLfTransferBuilderExpression)=>CoreLfTransferBuilderExpression) => {
    const b=new CoreLfTransferScopedBuilder();
    const bind=body?b.lam.bind(b):b.pi.bind(b);
    return b.term(bind('K',b.global(category),K=>bind('D',displayedFamilyType(b,K),D=>
        bind('E',displayedFamilyType(b,K),E=>bind('FF',displayedFunctorType(b,K,D,E),FF=>
            result(b,K,D,E,FF),explicitMode),implicitMode),implicitMode),implicitMode));
};
const rootCall = (b:CoreLfTransferScopedBuilder,owner:CoreLfQualifiedSymbol,K:CoreLfTransferBuilderExpression,
    D:CoreLfTransferBuilderExpression,E:CoreLfTransferBuilderExpression,FF:CoreLfTransferBuilderExpression)=>
    globalCall(b,owner,[{plicity:'implicit',value:K},{plicity:'implicit',value:D},
        {plicity:'implicit',value:E},{plicity:'explicit',value:FF}]);
const identityRootAt = (b:CoreLfTransferScopedBuilder,K:CoreLfTransferBuilderExpression,E:CoreLfTransferBuilderExpression)=>
    globalCall(b,homdIdentity,[{plicity:'implicit',value:K},{plicity:'explicit',value:E}]);
const displayedInternalHomType = () => familyMapTelescope(false,(b,K,D,E)=>
    displayedFunctorType(b,K,E,indexFamilyAt(b,K,D)));
const displayedInternalHomBody = () => familyMapTelescope(true,(b,K,D,E,FF)=>
    globalCall(b,strictTransforView,[{plicity:'implicit',value:K},{plicity:'implicit',value:b.global(familyCoefficient)},
        {plicity:'implicit',value:E},{plicity:'implicit',value:indexFamilyAt(b,K,D)},
        {plicity:'explicit',value:rootCall(b,homdRelative,K,D,E,FF)}]));

const nativeTargetPrerequisites: readonly CoreLfTransferDeclaration[] = (() => {
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient), Q=b.global(homdCoefficient);
    const opaque=(name:CoreLfQualifiedSymbol,type:CoreLfTransferExpression,rigidity:'injective'|'ordinary'='injective') => ({
        order:0,symbol:name,type,body:coreLfTransferAbsentBody(),modifiers:modifiers(rigidity,'opaque'),
        provenance:source(`native signature ${name.name}`)
    });
    return [
        opaque(representedHom,b.term(b.pi('A',b.global(category),A=>b.pi('B',b.global(category),B=>
            b.pi('F',functorType(b,B,A),()=>b.pi('W',decode(b,globalCall(b,objectClassifier,[{plicity:'explicit',value:A}])),
                ()=>functorType(b,B,cart),explicitMode),explicitMode),implicitMode),implicitMode))),
        opaque(homdCoefficient,b.term(b.global(category))),
        opaque(homdInclude,b.term(functorType(b,cart,Q))),
        {order:0,symbol:homdDiagram,
            type:b.term(b.pi('K',b.global(category),K=>b.pi('E',functorType(b,K,cart),()=>functorType(b,K,Q),explicitMode),implicitMode)),
            body:coreLfTransferExplicitBody(b.term(b.lam('K',b.global(category),K=>b.lam('E',functorType(b,K,cart),E=>
                functorComposeAt(b,K,cart,Q,b.global(homdInclude),E),explicitMode),implicitMode))),
            modifiers:modifiers('ordinary','transparent'),provenance:source('symbol Homd_coeff_diagram [K : Cat]')},
        opaque(homdRepresentable,b.term(b.pi('K',b.global(category),K=>
            functorType(b,coAt2At(b,K),functorCategoryAt(b,K,Q)),explicitMode)))
    ];
})();

const nativeRootPrerequisites: readonly CoreLfTransferDeclaration[] = (()=>{
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient), Q=b.global(homdCoefficient);
    const make=(owner:CoreLfQualifiedSymbol,type:CoreLfTransferExpression,body?:CoreLfTransferExpression,rigidity:'ordinary'|'injective'='ordinary')=>({
        order:0,symbol:owner,type,body:body===undefined?coreLfTransferAbsentBody():coreLfTransferExplicitBody(body),
        modifiers:modifiers(rigidity,body===undefined?'opaque':'transparent'),provenance:source(`native declaration ${owner.name}`)
    });
    const precompType=b.term(b.pi('A',b.global(category),A=>b.pi('B',b.global(category),B=>
        b.pi('F',functorType(b,A,B),F=>b.pi('Z',objectTypeAt(b,B),Z=>
            b.pi('W',objectTypeAt(b,A),W=>b.pi('X',objectTypeAt(b,A),X=>
                b.pi('h',objectTypeAt(b,homAt(b,A,W,X)),()=>functorType(b,
                    homAt(b,B,functorObjectAt(b,A,B,F,X),Z),homAt(b,B,functorObjectAt(b,A,B,F,W),Z)),explicitMode),
            implicitMode),implicitMode),explicitMode),explicitMode),implicitMode),implicitMode));
    const postcompType=b.term(b.pi('A',b.global(category),A=>b.pi('B',b.global(category),B=>
        b.pi('F',functorType(b,B,A),F=>b.pi('W',objectTypeAt(b,A),W=>
            b.pi('X',objectTypeAt(b,B),X=>b.pi('Y',objectTypeAt(b,B),Y=>
                b.pi('f',objectTypeAt(b,homAt(b,B,X,Y)),()=>functorType(b,
                    homAt(b,A,W,functorObjectAt(b,B,A,F,X)),homAt(b,A,W,functorObjectAt(b,B,A,F,Y))),explicitMode),
            implicitMode),implicitMode),explicitMode),explicitMode),implicitMode),implicitMode));
    const idxType=b.term(b.pi('K',b.global(category),K=>functorType(b,
        opposite(b,coAt2At(b,functorCategoryAt(b,K,Q))),cartAt(b,K,cart)),explicitMode));
    const idxBody=b.term(b.lam('K',b.global(category),K=>{
        const A=coAt2At(b,functorCategoryAt(b,K,Q));
        const pre=globalCall(b,precompAlong,[{plicity:'implicit',value:cart},{plicity:'implicit',value:cart},
            {plicity:'explicit',value:idFunctorAt(b,cart)},{plicity:'explicit',value:cart},
            {plicity:'implicit',value:K},{plicity:'implicit',value:A},{plicity:'explicit',value:homdBaseMap(b,K)}]);
        return functorComposeAt(b,opposite(b,A),cartAt(b,A,cart),cartAt(b,K,cart),pre,
            internalHomAt(b,A,A,idFunctorAt(b,A)));
    },explicitMode));
    const conType=b.term(b.pi('K',b.global(category),K=>b.pi('D',displayedFamilyType(b,K),D=>
        b.pi('E',displayedFamilyType(b,K),E=>functorType(b,
            opposite(b,globalCall(b,transforCategory,[{plicity:'implicit',value:K},{plicity:'implicit',value:cart},
                {plicity:'explicit',value:D},{plicity:'explicit',value:E}])),
            homAt(b,cartAt(b,K,cart),targetAt(b,K,E),targetAt(b,K,D))),explicitMode),explicitMode),implicitMode));
    const conBody=b.term(b.lam('K',b.global(category),K=>b.lam('D',displayedFamilyType(b,K),D=>
        b.lam('E',displayedFamilyType(b,K),E=>{
            const diagramD=diagramAt(b,K,D),diagramE=diagramAt(b,K,E);
            const transfs=(coefficient:CoreLfTransferBuilderExpression,F:CoreLfTransferBuilderExpression,G:CoreLfTransferBuilderExpression)=>
                globalCall(b,transforCategory,[{plicity:'implicit',value:K},{plicity:'implicit',value:coefficient},
                    {plicity:'explicit',value:F},{plicity:'explicit',value:G}]);
            const action=(A:CoreLfTransferBuilderExpression,B:CoreLfTransferBuilderExpression,F:CoreLfTransferBuilderExpression,
                X:CoreLfTransferBuilderExpression,Y:CoreLfTransferBuilderExpression)=>globalCall(b,functorHomFull,[
                    {plicity:'implicit',value:A},{plicity:'implicit',value:B},{plicity:'explicit',value:F},
                    {plicity:'implicit',value:X},{plicity:'implicit',value:Y}]);
            const source=transfs(cart,D,E), middle=transfs(Q,diagramD,diagramE);
            const include=globalCall(b,postcompFunctor,[{plicity:'implicit',value:b.global(categoryOfCategories)},
                {plicity:'implicit',value:b.global(categoryOfCategories)},
                {plicity:'explicit',value:idFunctorAt(b,b.global(categoryOfCategories))},
                {plicity:'explicit',value:K},{plicity:'implicit',value:cart},{plicity:'implicit',value:Q},
                {plicity:'explicit',value:b.global(homdInclude)}]);
            return functorComposeAt(b,opposite(b,source),opposite(b,middle),
                homAt(b,cartAt(b,K,cart),targetAt(b,K,E),targetAt(b,K,D)),
                action(opposite(b,coAt2At(b,functorCategoryAt(b,K,Q))),cartAt(b,K,cart),
                    globalCall(b,homdTargetIndex,[{plicity:'explicit',value:K}]),diagramE,diagramD),
                oppositeFunctorAt(b,source,middle,action(functorCategoryAt(b,K,cart),functorCategoryAt(b,K,Q),include,D,E)));
        },explicitMode),explicitMode),implicitMode));
    const mapBody=familyMapTelescope(true,(b,K,D,E,FF)=>{
        const transfs=globalCall(b,transforCategory,[{plicity:'implicit',value:K},{plicity:'implicit',value:b.global(familyCoefficient)},
            {plicity:'explicit',value:D},{plicity:'explicit',value:E}]);
        return functorObjectAt(b,opposite(b,transfs),homAt(b,cartAt(b,K,b.global(familyCoefficient)),targetAt(b,K,E),targetAt(b,K,D)),
            globalCall(b,homdTargetCon,[{plicity:'implicit',value:K},{plicity:'explicit',value:D},{plicity:'explicit',value:E}]),FF);
    });
    const idType=b.term(b.pi('K',b.global(category),K=>b.pi('E',displayedFamilyType(b,K),E=>
        cartMapType(b,K,E,targetAt(b,K,E)),explicitMode),implicitMode));
    return [
        make(precompAlong,precompType),make(postcompFunctor,postcompType),make(homdTargetIndex,idxType,idxBody),
        make(homdTargetCon,conType,conBody),
        make(homdTargetMap,familyMapTelescope(false,(b,K,D,E)=>cartMapType(b,K,targetAt(b,K,E),targetAt(b,K,D))),mapBody),
        make(homdIdentity,idType),
        make(homdRelative,familyMapTelescope(false,(b,K,D,E)=>cartMapType(b,K,E,targetAt(b,K,D))),
            familyMapTelescope(true,(b,K,D,E,FF)=>ordinaryComposeAt(b,cartAt(b,K,b.global(familyCoefficient)),E,
                indexFamilyAt(b,K,E),indexFamilyAt(b,K,D),rootCall(b,homdTargetMap,K,D,E,FF),identityRootAt(b,K,E))))
    ];
})();

const reviewedFoundationDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze([
    Object.freeze({
        ...priorIdentityDeclaration,
        order: 0
    }),
    Object.freeze({
        order: 1,
        symbol: displayedComposition,
        type: displayedCompositionType(),
        body: coreLfTransferExplicitBody(
            displayedCompositionBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol comp_catd_fapp0 [K : Cat] [E D : τ (Catd K)]',
            403
        )
    }),
    Object.freeze({
        order: 2,
        symbol: oppositeFunctor,
        type: oppositeFunctorType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source('injective symbol Op_func', 509)
    }),
    Object.freeze({
        order: 3,
        symbol: displayedOppositeFunctor,
        type: displayedOppositeFunctorType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol Op_catd_func (Z : Cat)',
            544
        )
    }),
    Object.freeze({
        order: 4,
        symbol: internalHom,
        type: internalHomType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol hom_int [A B : Cat]',
            646
        )
    }),
    Object.freeze({
        order: 5,
        symbol: displayedOpposite,
        type: displayedOppositeType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol Op_catd [K : Cat]',
            967
        )
    }),
    Object.freeze({
        order: 6,
        symbol: displayedOppositeAction,
        type: displayedOppositeActionType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol Op_funcd [K : Cat]',
            978
        )
    }),
    Object.freeze({
        order: 7,
        symbol: mixedFunctorFamily,
        type: mixedFunctorFamilyType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('injective', 'opaque'),
        provenance: source(
            'injective symbol Functor_catd_func (K : Cat)',
            1091
        )
    }),
    Object.freeze({
        order: 8,
        symbol: edgeFamily,
        type: edgeFamilyType(),
        body: coreLfTransferExplicitBody(edgeFamilyBody()),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol Edge_catd_func [Z : Cat]',
            1114
        )
    }),
    Object.freeze({
        order: 9,
        symbol: presheafFamily,
        type: presheafFamilyType(),
        body: coreLfTransferExplicitBody(
            presheafFamilyBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol Presheaf_catd_func (K : Cat)',
            1115
        )
    }),
    Object.freeze({
        order: 10,
        symbol: homPresheafFamily,
        type: homPresheafFamilyType(),
        body: coreLfTransferExplicitBody(
            homPresheafFamilyBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol HomPresheaf_catd_func [Z : Cat]',
            1116
        )
    }),
    ...nativeTargetPrerequisites,
    Object.freeze({
        order: 11,
        symbol: displayedHomTarget,
        type: displayedHomTargetType(),
        body: coreLfTransferExplicitBody(
            displayedHomTargetBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol Homd_target_catd [K : Cat]',
            1118
        )
    }),
    ...nativeRootPrerequisites,
    Object.freeze({
        order: 12,
        symbol: displayedInternalHom,
        type: displayedInternalHomType(),
        body: coreLfTransferExplicitBody(displayedInternalHomBody()),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol homd_int [K : Cat] [D E : τ (Catd K)]',
            1119
        )
    })
]);

const nativeOrdinals: Readonly<Record<string,number>> = Object.freeze({
    "comp_catd_fapp0": 438,
    "Op_func": 547,
    "Op_catd_func": 618,
    "hom_": 619,
    "hom_precomp_along_func": 684,
    "hom_int": 735,
    "Op_catd": 1212,
    "Op_funcd": 1223,
    "Functor_catd_func": 1386,
    "Edge_catd_func": 1409,
    "Presheaf_catd_func": 1410,
    "HomPresheaf_catd_func": 1411,
    "Homd_coeff_cat": 1447,
    "Homd_coeff_include": 1468,
    "Homd_coeff_diagram": 1472,
    "Homd_representable_func": 1520,
    "Homd_target_catd": 1524,
    "homd_id_int": 1528,
    "Homd_target_index_func": 1541,
    "Homd_target_con_func": 1542,
    "Homd_target_map": 1543,
    "homd_rel_cart_int": 1544,
    "homd_int": 1546,
    "tdapp1_int_func_transfd": 1552,
    "tdapp1_int_fapp0_transfd": 1553,
    "tdapp1_int_fapp1_func_transfd": 1555
});

const declarations: readonly CoreLfTransferDeclaration[] =
Object.freeze(
    reviewedFoundationDeclarations
        .filter(declaration =>
            declaration.symbol.moduleId !== identityArrow.moduleId ||
            declaration.symbol.name !== identityArrow.name
        )
        .map((declaration, order) => Object.freeze({
            ...declaration,
            order,
            provenance: {...declaration.provenance,canonicalCommandOrdinal:nativeOrdinals[declaration.symbol.name]}
        }))
);

const foundationExternalSymbols = Object.freeze([
    category,
    decodeOwner,
    objectClassifier,
    homClassifier,
    functorClassifier,
    categoryOfCategories,
    familyCoefficient,
    cartesianFunctorCategory,
    coAt2Category,
    coAt2Functor,
    symbol('Hom_cat'),
    identityFunctor,
    precompPoint,
    postcompPoint,
    strictTransforView,
    transforCategory,
    displayedCategoryCategory,
    functorObject,
    functorHomFull,
    constantDisplayedFamily,
    displayedFamilyClassifier,
    displayedFunctorClassifier,
    ordinaryComposition,
    oppositeCategory,
    functorCategory,
    functorEvaluation,
    functorComposition,
    sectionCategoryFunctor,
    identityArrow
]);

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_DEPENDENCY_CORRECTION =
Object.freeze({
    revision:
        'DISPLAYED-ND-HIGHER-FOUNDATION-1A-DEPENDENCY-CORRECTION-1',
    triggeredBy:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT
            .recommendedContinuation.mandatoryStop,
    auditCheckpoint:
        '4db1ce8a80725c0030ac8908f416d412591620bd',
    reviewCheckpoint:
        'f674be92ae04eff5642428724053fb4e75274e50',
    decision:
        'D-DTTLF-USABILITY-020-directly-approved-2026-07-29',
    missingExistingCoreOwnerLinks: Object.freeze([
        Object.freeze({
            symbol: 'Obj',
            owner: 'object-classifier' as CoreOwnerId
        }),
        Object.freeze({
            symbol: 'Hom',
            owner: 'hom-classifier' as CoreOwnerId
        })
    ]),
    missingExistingRuntimeRule: Object.freeze({
        id: 'categorical.opposite.involution',
        canonicalCommandOrdinal: 237,
        canonicalCommandText:
            'rule Op_cat (Op_cat $A) ↪ $A;',
        canonicalCommandTextSha256:
            'c9ff2c9e112c82facf9f1a01573c5cbf7aa9fa6cfa5458d1c46e77c94feb24ec',
        activeLambdapiRuleDelta: 0,
        typescriptRuntimeRuleDelta: 1
    }),
    reason:
        'the-reused-id-signature-references-Obj-and-Hom-and-the-' +
        'HomPresheaf-catd-func-transparent-body-needs-opposite-involution;' +
        'all-three-are-existing-authority-omitted-from-the-audit-boundary',
    semanticScopeChanged: false,
    declarationCountChanged: false,
    policyChanged: false,
    typescriptRuntimeRuleDelta: 1,
    activeLambdapiRuntimeRuleDelta: 0,
    proofRuleDelta: 0,
    intrinsicCoreOwnerDelta: 0,
    checkerBranchDelta: 0,
    surfaceMethodDelta: 0,
    disposition:
        'apply-the-directly-approved-D-020-dependency-correction-and-' +
        'continue-the-exact-reviewed-thirteen-declaration-scope'
});

const oppositeInvolutionRule = (): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const A = builder.capture('A');
    return {
        order: 0,
        id:
            CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_DEPENDENCY_CORRECTION
                .missingExistingRuntimeRule.id,
        groupId: 'categorical.opposite',
        clauseOrder: 0,
        sourceOwner: oppositeCategory,
        variables: [{
            name: 'A',
            type: builder.template(builder.global(category))
        }],
        left: builder.pattern(opposite(builder, opposite(builder, A))),
        right: builder.template(A),
        provenance: source(
            'rule Op_cat (Op_cat $A) ↪ $A;',
            239
        )
    };
};

const foundationRuntimeRules:
readonly CoreLfTransferRuntimeRule[] = Object.freeze([
    oppositeInvolutionRule()
]);

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_MODULE:
CoreLfModuleSpec = createCoreLfModuleSpec({
    revision:
        'DISPLAYED-ND-HIGHER-FOUNDATION-1A-RUNTIME-D020-1',
    moduleId: MODULE_ID,
    fragmentId: 'displayed-nd-higher-foundation-1a-runtime',
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256:
        'sha256:70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e',
    dependencies: [],
    externalSymbols: [category, oppositeCategory].map(symbol_ => ({
        symbol: symbol_,
        availability: 'earlier-fragment' as const
    })),
    declarations: [],
    inductives: [],
    runtimeRules: foundationRuntimeRules,
    proofRules: []
});

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_POLICY:
CoreLfTransferPolicyOverlay = createCoreLfTransferPolicyOverlay(
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_MODULE,
    {
        revision:
            'DISPLAYED-ND-HIGHER-FOUNDATION-1A-RUNTIME-D020-POLICY-1',
        moduleRevision:
            CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_MODULE
                .revision,
        entries: foundationRuntimeRules.map(rule => ({
            order: rule.order,
            target: {
                kind: 'runtime-rule' as const,
                id: rule.id
            },
            policy: 'runtime-rewrite' as const,
            evidence:
                'Exact opposite-involution computation directly approved ' +
                'by D-DTTLF-USABILITY-020'
        }))
    }
);

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE:
CoreLfModuleSpec = createCoreLfModuleSpec({
    revision:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_REVISION,
    moduleId: MODULE_ID,
    fragmentId: 'displayed-nd-higher-foundation-1a',
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256:
        'sha256:70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e',
    dependencies: [],
    externalSymbols: foundationExternalSymbols.map(symbol_ => ({
        symbol: symbol_,
        availability: 'earlier-fragment' as const
    })),
    declarations,
    inductives: [],
    runtimeRules: [],
    proofRules: []
});

const reviewedPolicies =
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_REVIEW
        .authorization.exactPolicies;

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_POLICY:
CoreLfTransferPolicyOverlay = createCoreLfTransferPolicyOverlay(
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE,
    {
        revision:
            'DISPLAYED-ND-HIGHER-FOUNDATION-1A-POLICY-D057-1',
        moduleRevision:
            CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE
                .revision,
        entries: declarations.map(declaration => {
            if (declaration.symbol.name==='homd_int') {
                return {order:declaration.order,target:{kind:'declaration' as const,symbol:declaration.symbol},
                    policy:'checked-transparent-definition' as const,evidence:'Native defined relative Homd root under current foundations migration'};
            }
            const reviewed = reviewedPolicies.find(entry =>
                entry.name === declaration.symbol.name
            );
            if ([...nativeTargetPrerequisites,...nativeRootPrerequisites].some(d=>d.symbol.name===declaration.symbol.name)) {
                return { order:declaration.order,target:{kind:'declaration' as const,symbol:declaration.symbol},
                    policy:declaration.body.kind==='explicit-term'
                        ? 'checked-transparent-definition' as const : 'opaque-signature' as const,
                    evidence:'Current foundations migration: selected native Q target dependency' };
            }
            if (reviewed === undefined) {
                throw new Error(
                    `No D-019 policy for ${declaration.symbol.name}`
                );
            }
            return {
                order: declaration.order,
                target: {
                    kind: 'declaration' as const,
                    symbol: declaration.symbol
                },
                policy: reviewed.policy,
                evidence:
                    'Current foundations migration: checked native signature/body; historical D-019 approval retained separately'
            };
        })
    }
);

const auditedCoreOwnerLinks = [
    ...CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT
        .dependencyBoundary.alreadyAvailableCoreOwnerLinks,
    ...CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_DEPENDENCY_CORRECTION
        .missingExistingCoreOwnerLinks
];

const auditedFreeDeclarationLinks =
    CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT
        .dependencyBoundary.alreadyAvailableFreeDeclarationLinks;

const externalLink = (
    target: CoreLfQualifiedSymbol,
    order: number
): CoreLfTransferDeclarationLink => {
    const migrated = [...CORE_HOMD_DUALITY_LINKAGE.entries,
        ...CORE_CATEGORICAL_FIBRED_PRODUCT_TRANSFER_LINKAGE.entries,
        ...CORE_CATEGORICAL_FIBRED_STRUCTURE_TRANSFER_LINKAGE.entries,
        ...CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries,
        ...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries].find(entry =>
            entry.symbol.moduleId===target.moduleId && entry.symbol.name===target.name);
    if (migrated && ['CoAt2_cat','CoAt2_func','Functor_cart_cat','Cat_cart','Hom_cat','id_func','strict_transfor','Transf_cat','hom_precomp_along_fapp0','hom_postcomp_fapp0','fapp1_func'].includes(target.name)) {
        return Object.freeze({...migrated,order});
    }
    if (target.name === 'fapp0_func') {
        const inherited = CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries.find(
            entry => entry.symbol.moduleId === target.moduleId && entry.symbol.name === target.name);
        if (inherited === undefined) throw new Error('Missing structural fixed-evaluation owner');
        return Object.freeze({ ...inherited, order });
    }
    if (
        target.moduleId === identityArrow.moduleId &&
        target.name === identityArrow.name
    ) {
        const identityLink =
            CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE.entries.find(
                entry =>
                    entry.symbol.moduleId === target.moduleId &&
                    entry.symbol.name === target.name
            );
        if (
            identityLink === undefined ||
            identityLink.kind !== 'free-declaration' ||
            identityLink.coreName !==
                'emdash_v3_2_scale_stress_3a2a_id'
        ) {
            throw new Error(
                'D-057 identity relocation is absent from fibred-transfd'
            );
        }
        return Object.freeze({
            ...identityLink,
            order,
            symbol: target
        });
    }
    const core = auditedCoreOwnerLinks.find(entry =>
        entry.symbol === target.name
    );
    if (core !== undefined) {
        return Object.freeze({
            order,
            symbol: target,
            kind: 'core-owner' as const,
            owner: core.owner
        });
    }
    const free = auditedFreeDeclarationLinks.find(entry =>
        entry.symbol === target.name
    );
    if (free !== undefined) {
        return Object.freeze({
            order,
            symbol: target,
            kind: 'free-declaration' as const,
            coreName: free.coreName,
            backendName: free.symbol
        });
    }
    throw new Error(
        `No reviewed foundation dependency link for ${target.name}`
    );
};

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE:
CoreLfTransferDeclarationLinkage =
    createCoreLfTransferDeclarationLinkage(
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE,
        {
            revision:
                'DISPLAYED-ND-HIGHER-FOUNDATION-1A-LINKAGE-D057-1',
            moduleRevision:
                CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE
                    .revision,
            entries: [
                ...foundationExternalSymbols.map(externalLink),
                ...declarations.map((declaration, index) => ({
                    order: foundationExternalSymbols.length + index,
                    symbol: declaration.symbol,
                    kind: 'free-declaration' as const,
                    coreName: (() => {
                        const entry = Object.entries(
                            CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_SYMBOLS
                        ).find(([, symbol_]) =>
                            symbol_.moduleId ===
                                declaration.symbol.moduleId &&
                            symbol_.name === declaration.symbol.name
                        );
                        if (entry === undefined && [...nativeTargetPrerequisites,...nativeRootPrerequisites].some(d=>d.symbol.name===declaration.symbol.name)) {
                            return `emdash_v3_2_homd_native_${declaration.symbol.name}`;
                        }
                        if (entry === undefined) {
                            throw new Error(
                                'Displayed higher foundation declaration ' +
                                `'${declaration.symbol.name}' has no Core ` +
                                'name contract entry'
                            );
                        }
                        return coreCategoricalDisplayedNdHigherFoundationCoreName(
                            entry[0] as
                                CoreCategoricalDisplayedNdHigherFoundationSymbolId
                        );
                    })(),
                    backendName: declaration.symbol.name
                }))
            ]
        }
    );

export function coreNativeHomdCoreName(name:string):string {
    const link=CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE.entries.find(l=>l.symbol.name===name);
    if(!link||link.kind!=='free-declaration') throw new Error(`No native Homd free owner ${name}`);
    return link.coreName;
}
/** Exact target-index presentation retained by the native relative root. */
export function coreNativeHomdTargetFamily(K:KernelExpression,E:KernelExpression,p:Provenance):KernelExpression {
    const ref=(name:string)=>kernelFree(coreNativeHomdCoreName(name),p);
    const call=(name:string,args:KernelExpression[],implicitCount=0)=>kernelCall(ref(name),
        args.map((value,index)=>({value,plicity:index<implicitCount?'implicit':'explicit'})),p);
    const Q=ref('Homd_coeff_cat'),cart=ref('Cat_cart');
    const source=call('Op_cat',[call('CoAt2_cat',[call('Functor_cat',[K,Q])])]);
    const target=call('Functor_cart_cat',[K,cart]);
    return kernelApplication('functor-object',[{value:source},{value:target},
        {value:call('Homd_target_index_func',[K])},{value:call('Homd_coeff_diagram',[K,E],1)}],p);
}

export const
CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_BOUNDARY =
Object.freeze({
    revision:
        'DISPLAYED-ND-HIGHER-FOUNDATION-1A-BOUNDARY-1',
    declarationNames: Object.freeze(
        declarations.map(declaration => declaration.symbol.name)
    ),
    declarationCount: declarations.length,
    reviewedDeclarationCount:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT.measuredClosure.foundationDeclarations.length,
    relocatedEarlierDeclarationNames: Object.freeze(['id']),
    relocatedEarlierDeclarationCount: 1,
    checkedTransparentDefinitionCount:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_POLICY
            .entries.filter(entry =>
            entry.policy === 'checked-transparent-definition'
        ).length,
    opaqueSignatureCount:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_POLICY
            .entries.filter(entry =>
            entry.policy === 'opaque-signature'
        ).length,
    reviewedCheckedTransparentDefinitionCount:
        reviewedPolicies.filter(entry =>
            entry.policy === 'checked-transparent-definition'
        ).length,
    reviewedOpaqueSignatureCount:
        reviewedPolicies.filter(entry =>
            entry.policy === 'opaque-signature'
        ).length,
    existingRuntimeRuleIds: Object.freeze([
        ...foundationRuntimeRules.map(rule => rule.id),
        'categorical.homd-native.hom-int-object',
        'categorical.homd-native.precomp-object',
        'categorical.homd-native.cart-precomp-composition'
    ]),
    runtimeRuleCount: foundationRuntimeRules.length + 3,
    proofRuleCount: 0,
    reusedIdentityCoreName:
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_AUDIT
            .dependencyBoundary.reusablePriorRepresentation.coreName,
    activeLambdapiOwnerDelta: 0,
    activeLambdapiRuleDelta: 0,
    typescriptRuntimeRuleDelta: 4,
    intrinsicCoreOwnerDelta: 0,
    ownerSpecificCheckerOrEvaluatorDelta: 0,
    surfaceMethodDelta: 0,
    browserPromotionDelta: 0,
    targetOwnersIncluded: false,
    targetProjectionRulesIncluded: false,
    allEntriesUseGenericTransferEngines: true
});

export interface CoreCategoricalDisplayedNdHigherFoundationCompilation {
    readonly prerequisite: ReturnType<typeof compileCoreHomdDualityTransfer>;
    readonly compiled: CoreLfCompiledDeclarationModule;
    readonly signatureCompiled: CoreLfCompiledDeclarationModule;
    readonly declarationContext: CoreLfMixedDeclarationContext;
    readonly runtimeFragment: CoreLfCompiledRuntimeFragment;
    readonly runtime: CoreLfCompiledRuntimeProgram;
    readonly composedRuntime: CoreLfComposedRuntimeProgram;
}

const rootNames = new Set(['Homd_target_con_func','Homd_target_map','homd_id_int','homd_rel_cart_int','homd_int']);
const signatureDeclarations = declarations.filter(d=>!rootNames.has(d.symbol.name));
const relativeDeclarations = declarations.filter(d=>rootNames.has(d.symbol.name));
const declarationPhase = (id:string, entries:readonly CoreLfTransferDeclaration[], additional:readonly CoreLfQualifiedSymbol[]) => {
    const external=[...foundationExternalSymbols,...additional];
    const module=createCoreLfModuleSpec({
        revision:`HOMD-${id}-DECLARATIONS-1`,moduleId:MODULE_ID,fragmentId:`homd-${id.toLowerCase()}`,
        authorityPath:'emdash2/emdash3_2.lp',sourceSha256:CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE.sourceSha256,
        dependencies:[],externalSymbols:external.map(symbol=>({symbol,availability:'earlier-fragment' as const})),
        declarations:entries.map((d,order)=>({...d,order})),inductives:[],runtimeRules:[],proofRules:[]
    });
    const policy=createCoreLfTransferPolicyOverlay(module,{
        revision:`HOMD-${id}-POLICY-1`,moduleRevision:module.revision,
        entries:module.declarations.map(d=>{
            const inherited=CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_POLICY.entries.find(entry=>
                entry.target.kind==='declaration'&&entry.target.symbol.name===d.symbol.name);
            if(!inherited) throw new Error(`Missing Homd policy ${d.symbol.name}`);
            return {...inherited,order:d.order};
        })
    });
    const links=CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_LINKAGE.entries;
    const linkage=createCoreLfTransferDeclarationLinkage(module,{
        revision:`HOMD-${id}-LINKAGE-1`,moduleRevision:module.revision,
        entries:[...external,...module.declarations.map(d=>d.symbol)].map((symbol,order)=>{
            const inherited=links.find(l=>l.symbol.moduleId===symbol.moduleId&&l.symbol.name===symbol.name);
            if(!inherited) throw new Error(`Missing Homd phase link ${symbol.name}`);
            return {...inherited,order};
        })
    });
    return {module,policy,linkage};
};
const signaturePhase=declarationPhase('SIGNATURE',signatureDeclarations,[]);
const relativePhase=declarationPhase('RELATIVE',relativeDeclarations,signatureDeclarations.map(d=>d.symbol));

const representedObjectRule = ():CoreLfTransferRuntimeRule=>{
    const b=new CoreLfTransferScopedBuilder(), A=b.capture('A'),B=b.capture('B'),F=b.capture('F'),W=b.capture('W');
    return {order:0,id:'categorical.homd-native.hom-int-object',groupId:'categorical.homd-native.hom-int-object',clauseOrder:0,
        sourceOwner:functorObject,variables:[...['A','B'].map(name=>({name,type:b.template(b.global(category))})),
            {name:'F',type:b.template(functorType(b,B,A))},{name:'W',type:b.template(objectTypeAt(b,A))}],
        left:b.pattern(functorObjectAt(b,b.wildcard(opposite(b,A)),b.wildcard(cartAt(b,B,b.global(familyCoefficient))),internalHomAt(b,A,B,F),W)),
        right:b.template(representedAt(b,A,B,F,W)),provenance:source('rule @fapp0 _ _ (@hom_int $A $B $F) $W ↪ @hom_ $A $B $F $W;')};
};
const precompAt = (b:CoreLfTransferScopedBuilder,owner:CoreLfQualifiedSymbol,A:CoreLfTransferBuilderExpression,
    B:CoreLfTransferBuilderExpression,F:CoreLfTransferBuilderExpression,Z:CoreLfTransferBuilderExpression,
    W:CoreLfTransferBuilderExpression,X:CoreLfTransferBuilderExpression,h:CoreLfTransferBuilderExpression,g?:CoreLfTransferBuilderExpression)=>
    globalCall(b,owner,[{plicity:'implicit',value:A},{plicity:'implicit',value:B},{plicity:'explicit',value:F},
        {plicity:'explicit',value:Z},{plicity:'implicit',value:W},{plicity:'implicit',value:X},{plicity:'explicit',value:h},
        ...(g===undefined?[]:[{plicity:'explicit' as const,value:g}])]);
const precompObjectRule = ():CoreLfTransferRuntimeRule=>{
    const b=new CoreLfTransferScopedBuilder(), A=b.capture('A'),B=b.capture('B'),F=b.capture('F'),Z=b.capture('Z');
    const W=b.capture('W'),X=b.capture('X'),h=b.capture('h'),g=b.capture('g');
    const sourceCategory=homAt(b,B,functorObjectAt(b,A,B,F,X),Z), target=homAt(b,B,functorObjectAt(b,A,B,F,W),Z);
    return {order:1,id:'categorical.homd-native.precomp-object',groupId:'categorical.homd-native.precomp-object',clauseOrder:0,
        sourceOwner:functorObject,variables:[...['A','B'].map(name=>({name,type:b.template(b.global(category))})),
            {name:'F',type:b.template(functorType(b,A,B))},{name:'Z',type:b.template(objectTypeAt(b,B))},
            ...['W','X'].map(name=>({name,type:b.template(objectTypeAt(b,A))})),
            {name:'h',type:b.template(objectTypeAt(b,homAt(b,A,W,X)))},{name:'g',type:b.template(objectTypeAt(b,sourceCategory))}],
        left:b.pattern(functorObjectAt(b,b.wildcard(sourceCategory),b.wildcard(target),precompAt(b,precompAlong,A,B,F,Z,W,X,h),g)),
        right:b.template(precompAt(b,precompPoint,A,B,F,Z,W,X,h,g)),
        provenance:source('rule fapp0 (@hom_precomp_along_func $A $B $F $Z $W $X $h) $g ↪ @hom_precomp_along_fapp0 $A $B $F $Z $W $X $h $g;')};
};
const cartPrecompRule = ():CoreLfTransferRuntimeRule=>{
    const b=new CoreLfTransferScopedBuilder(), cart=b.global(familyCoefficient);
    const A=b.capture('A'),B=b.capture('B'),Z=b.capture('Z'),F=b.capture('F'),G=b.capture('G');
    return {order:2,id:'categorical.homd-native.cart-precomp-composition',groupId:'categorical.homd-native.cart-precomp-composition',clauseOrder:0,
        sourceOwner:precompPoint,variables:[...['A','B','Z'].map(name=>({name,type:b.template(b.global(category))})),
            {name:'F',type:b.template(functorType(b,A,B))},{name:'G',type:b.template(functorType(b,B,Z))}],
        left:b.pattern(precompAt(b,precompPoint,cart,cart,idFunctorAt(b,cart),Z,A,B,F,G)),
        right:b.template(functorComposeAt(b,A,B,Z,G,F)),
        provenance:source('native Cartesian identity-family precomposition fold, with the transparent id_func spelling: rule @hom_precomp_along_fapp0 Cat_cart Cat_cart (@id Cat_cat Cat_cart) $Z $A $B $F $G ↪ @comp_cat_fapp0 $A $B $Z $G $F;')};
};
const postcompObjectRule = ():CoreLfTransferRuntimeRule=>{
    const b=new CoreLfTransferScopedBuilder(),A=b.capture('A'),B=b.capture('B'),F=b.capture('F'),W=b.capture('W');
    const X=b.capture('X'),Y=b.capture('Y'),f=b.capture('f'),g=b.capture('g');
    const image=(x:CoreLfTransferBuilderExpression)=>functorObjectAt(b,B,A,F,x);
    const from=homAt(b,A,W,image(X)),to=homAt(b,A,W,image(Y));
    const args=[{plicity:'implicit' as const,value:A},{plicity:'implicit' as const,value:B},
        {plicity:'explicit' as const,value:F},{plicity:'explicit' as const,value:W},
        {plicity:'implicit' as const,value:X},{plicity:'implicit' as const,value:Y},{plicity:'explicit' as const,value:f}];
    return {order:0,id:'categorical.homd-native.postcomp-object',groupId:'categorical.homd-native.postcomp-object',clauseOrder:0,
        sourceOwner:functorObject,variables:[...['A','B'].map(name=>({name,type:b.template(b.global(category))})),
            {name:'F',type:b.template(functorType(b,B,A))},{name:'W',type:b.template(objectTypeAt(b,A))},
            ...['X','Y'].map(name=>({name,type:b.template(objectTypeAt(b,B))})),
            {name:'f',type:b.template(objectTypeAt(b,homAt(b,B,X,Y)))},{name:'g',type:b.template(objectTypeAt(b,from))}],
        left:b.pattern(functorObjectAt(b,b.wildcard(from),b.wildcard(to),globalCall(b,postcompFunctor,args),g)),
        right:b.template(globalCall(b,postcompPoint,[...args,{plicity:'explicit',value:g}])),
        provenance:source('rule fapp0 (@hom_postcomp_func $A $B $F $W $X $Y $f) $g ↪ @hom_postcomp_fapp0 $A $B $F $W $X $Y $f $g;')};
};
const diagramObjectRule = ():CoreLfTransferRuntimeRule=>{
    const b=new CoreLfTransferScopedBuilder(),K=b.capture('K'),E=b.capture('E'),cat=b.global(categoryOfCategories);
    return {order:0,id:'categorical.homd-native.diagram-object',groupId:'categorical.homd-native.diagram-object',clauseOrder:0,
        sourceOwner:postcompPoint,variables:[{name:'K',type:b.template(b.global(category))},
            {name:'E',type:b.template(functorType(b,K,b.global(familyCoefficient)))}],
        left:b.pattern(globalCall(b,postcompPoint,[{plicity:'implicit',value:cat},{plicity:'implicit',value:cat},
            {plicity:'explicit',value:idFunctorAt(b,cat)},{plicity:'explicit',value:K},
            {plicity:'implicit',value:b.global(familyCoefficient)},{plicity:'implicit',value:b.global(homdCoefficient)},
            {plicity:'explicit',value:b.global(homdInclude)},{plicity:'explicit',value:E}])),
        right:b.template(diagramAt(b,K,E)),
        provenance:source('rule @hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $K Cat_cart Homd_coeff_cat Homd_coeff_include $E ↪ @Homd_coeff_diagram $K $E;')};
};
const rootRuntimeRules=[representedObjectRule(),precompObjectRule(),cartPrecompRule(),postcompObjectRule(),diagramObjectRule()]
    .map((rule,order)=>({...rule,order}));
export const CORE_HOMD_NATIVE_ROOT_RUNTIME_MODULE=createCoreLfModuleSpec({
    revision:'HOMD-NATIVE-ROOT-RUNTIME-1',moduleId:MODULE_ID,fragmentId:'homd-native-root-runtime',authorityPath:'emdash2/emdash3_2.lp',
    sourceSha256:CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_TRANSFER_MODULE.sourceSha256,dependencies:[],
    externalSymbols:[...foundationExternalSymbols,...signatureDeclarations.map(d=>d.symbol)].map(symbol=>({symbol,availability:'earlier-fragment' as const})),
    declarations:[],inductives:[],runtimeRules:rootRuntimeRules,proofRules:[]
});
const rootRuntimePolicy=createCoreLfTransferPolicyOverlay(CORE_HOMD_NATIVE_ROOT_RUNTIME_MODULE,{
    revision:'HOMD-NATIVE-ROOT-RUNTIME-POLICY-1',moduleRevision:CORE_HOMD_NATIVE_ROOT_RUNTIME_MODULE.revision,
    entries:rootRuntimeRules.map(rule=>({order:rule.order,target:{kind:'runtime-rule' as const,id:rule.id},policy:'runtime-rewrite' as const,
        evidence:'Existing native represented/precomposition projection required before the relative root definition'}))
});

let cachedCompilation:
    CoreCategoricalDisplayedNdHigherFoundationCompilation | undefined;

export function compileCoreCategoricalDisplayedNdHigherFoundationTransfer():
CoreCategoricalDisplayedNdHigherFoundationCompilation {
    if (cachedCompilation !== undefined) return cachedCompilation;
    validateCoreCategoricalDisplayedNdHigherReview();
    const prerequisite = compileCoreHomdDualityTransfer();
    const runtimeFragment = compileCoreLfRuntimeFragment(
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_MODULE,
        CORE_CATEGORICAL_DISPLAYED_ND_HIGHER_FOUNDATION_RUNTIME_POLICY,
        prerequisite.declarationContext,
        {
            dependencies: [{
                relation: 'earlier-fragment',
                fragment: prerequisite.runtimeFragment
            }],
            comparisonStepLimit: 512
        }
    );
    const signatureCompiled = compileCoreLfDeclarations(signaturePhase.module,signaturePhase.policy,signaturePhase.linkage,{
        initialEnvironment:prerequisite.compiled.environment,runtimeProgram:runtimeFragment.runtime,comparisonStepLimit:512
    });
    const signatureContext = new CoreLfMixedDeclarationContext(prerequisite.declarationContext,[signatureCompiled]);
    const rootRuntimeFragment = compileCoreLfRuntimeFragment(CORE_HOMD_NATIVE_ROOT_RUNTIME_MODULE,rootRuntimePolicy,signatureContext,{
        dependencies:[{relation:'earlier-fragment',fragment:runtimeFragment}],comparisonStepLimit:512
    });
    const compiled = compileCoreLfDeclarations(relativePhase.module,relativePhase.policy,relativePhase.linkage,{
        initialEnvironment:signatureCompiled.environment,runtimeProgram:rootRuntimeFragment.runtime,comparisonStepLimit:512
    });
    const declarationContext = new CoreLfMixedDeclarationContext(signatureContext,[compiled]);
    cachedCompilation = Object.freeze({
        prerequisite,
        compiled, signatureCompiled,
        declarationContext,
        runtimeFragment: rootRuntimeFragment,
        runtime: rootRuntimeFragment.localProgram,
        composedRuntime: rootRuntimeFragment.runtime
    });
    return cachedCompilation;
}
