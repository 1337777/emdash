/**
 * PATHOUT-LIBRARY-INTERNALIZED-1D root-only existing-authority transfer.
 *
 * Current local boundary: four opaque declarations, four native runtime
 * projections plus five retained presentation rules, two proof-time comparisons,
 * and ten transparent definitions; two existing whiskering signatures are reused. The module deliberately retains
 * PathInd_transfd as the primary internally natural theorem and PathInd_funcd
 * as its derived Sigma-total presentation. It stops before transitivity and
 * every public/browser/package presentation.
 */

import { compileCoreLfProofProgram } from './lf_transfer_proof';
import { CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE, CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY } from './categorical_fibred_dependent_target_transfer';
import { compileCoreCategoricalCompositionalNaturalAt, CORE_CATEGORICAL_COMPOSITIONAL_NATURAL_TRANSFER_LINKAGE } from './categorical_compositional_natural_transfer';
import {
    CORE_CATEGORICAL_DISPLAYED_CHAIN_TRANSFER_LINKAGE
} from './categorical_displayed_chain_transfer';
import {
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SYMBOLS,
    CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE
} from './categorical_fibred_dependent_target_transfer';
import {
    CORE_CATEGORICAL_FIBRED_TRANSFD_SYMBOLS,
    CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE
} from './categorical_fibred_transfd_transfer';
import {
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE
} from './categorical_mixed_action_transfer';
import {
    CORE_CATEGORICAL_STRUCTURAL_SYMBOLS,
    CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE
} from './categorical_structural_transfer';
import {
    CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE,
    coreDirectedContinuationTransferSymbol
} from './directed_continuation_transfer';
import {
    CoreLfModuleSpec,
    CoreLfQualifiedSymbol,
    CoreLfTransferBuilderExpression,
    CoreLfTransferDeclaration,
    CoreLfTransferExpression,
    CoreLfTransferPolicyOverlay,
    CoreLfTransferRuntimeRule,
    CoreLfTransferProofRule,
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
import { binderMode } from './kernel';
import {
    CORE_PATHIND_FIXED_SOURCE_1C_FIBRE_TARGET_LINKAGE,
    CORE_PATHIND_FIXED_SOURCE_1C_LIBRARY_LINKAGE,
    CORE_PATHIND_FIXED_SOURCE_1C_REVISION,
    CORE_PATHIND_FIXED_SOURCE_1C_SYMBOLS,
    CORE_PATHIND_FIXED_SOURCE_1C_TRUSTED_LINKAGE,
    CorePathindFixedSource1cCompilation,
    compileCorePathindFixedSource1cTransfer
} from './pathind_fixed_source_transfer';
import {
    validateCorePathindInternalized1dReviewV14
} from './pathind_internalized_review_v14';
import {
    CORE_PATHOUT_FOUNDATION_1B_LIBRARY_LINKAGE,
    CORE_PATHOUT_FOUNDATION_1B_PREREQUISITE_LINKAGE,
    CORE_PATHOUT_FOUNDATION_1B_SYMBOLS,
    CORE_PATHOUT_FOUNDATION_SOURCE_SHA256
} from './pathout_foundation_transfer';

const MODULE_ID = 'emdash.emdash3_2';

export const CORE_PATHIND_INTERNALIZED_1D_REVISION =
    'PATHIND-INTERNALIZED-NATIVE-CART-15' as const;

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
const familyCoefficient =
    coreDirectedContinuationTransferSymbol('cartesian-category-coefficient');
const displayedCategoryCategory =
    coreDirectedContinuationTransferSymbol('displayed-category-category');
const displayedFunctorCategory =
    coreDirectedContinuationTransferSymbol('displayed-functor-category');
const functorObject =
    coreDirectedContinuationTransferSymbol('functor-object');
const functorHomCapped =
    coreDirectedContinuationTransferSymbol('functor-hom-capped');
const transforComponentCapped =
    coreDirectedContinuationTransferSymbol('transfor-component-capped');
const transforCategory =
    coreDirectedContinuationTransferSymbol('transfor-category');
const sigmaCategory =
    coreDirectedContinuationTransferSymbol('sigma-category');
const sigmaTelescopeFamily =
    coreDirectedContinuationTransferSymbol('sigma-telescope-family');
const dependentPair =
    coreDirectedContinuationTransferSymbol('dependent-pair');
const constantDisplayedFamily =
    coreDirectedContinuationTransferSymbol('constant-displayed-family');
const sigmaTransportArrow =
    coreDirectedContinuationTransferSymbol('sigma-transport-arrow');

const {
    functorCategory
} = CORE_CATEGORICAL_STRUCTURAL_SYMBOLS;

const {
    sectionCategoryFunctor,
    pullbackPi
} = CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_SYMBOLS;

const symbol = (name: string): CoreLfQualifiedSymbol =>
    coreLfQualifiedSymbol(MODULE_ID, name);

const cartesianFunctorCategory = symbol('Functor_cart_cat');
const cartesianInclusion = symbol('Functor_cart_include');
const strictTransforView = symbol('strict_transfor');
const functorComposition = symbol('comp_cat_fapp0');
const genericComposition = symbol('comp_fapp0');
const ordinaryCategories = symbol('Cat_cat');
const prewhiskeringAction = symbol('comp_cat_con_fapp1_func');
const displayedFamilyClassifier = symbol('Catd');
const displayedFunctorClassifier = symbol('Functord');
const oppositeCategory = symbol('Op_cat');
const oppositeFunctor = symbol('Op_func');
const pullbackDisplayedFamily = symbol('Pullback_catd');
const pullbackDisplayedFamilyFunctor = symbol('Pullback_catd_func');
const displayedCategoryFunctor = symbol('Catd_cat_func');
const piInternalDisplayedFunctor = symbol('Pi_int_funcd');
const fibreFunctor = symbol('Fibre_func');
const sectionCategory = symbol('Pi_cat');
const terminalCategory = symbol('Terminal_cat');
const sectionPullbackFunctor = symbol('section_pullback_func');
const displayedInternalCell = symbol('fdapp1_int_cell');

const {
    displayedTransformationClassifier,
    displayedComponent
} = CORE_CATEGORICAL_FIBRED_TRANSFD_SYMBOLS;

const {
    pathoutCategory,
    pathoutCategoryFunctor,
    pathoutTransport,
    pathoutObject,
    pathoutReflexiveObject
} = CORE_PATHOUT_FOUNDATION_1B_SYMBOLS;

const {
    pathoutReflexiveEvaluation,
    pathoutReflexiveBaseTransport,
    pathInductionSection,
    pathInductionSourceFamily,
    pathInductionTargetFamily,
    pathInductionComponentFunctor
} = CORE_PATHIND_FIXED_SOURCE_1C_SYMBOLS;

export const CORE_PATHIND_INTERNALIZED_1D_SYMBOLS = Object.freeze({
    sigmaDisplayedTransformation: symbol('Sigma_transfd_funcd'),
    pathoutMotives: symbol('PathOutMotives_catd'),
    pathoutPi: symbol('PathOutPi_funcd'),
    pathInductionTotalTarget: symbol('PathIndTgt_catd'),
    pathoutReflexiveEvaluationDisplayed:
        symbol('PathOutReflEval_funcd'),
    pathoutMotiveTransportObject:
        symbol('pathout_motive_transport_obj'),
    pathoutMotiveTransportArrow:
        symbol('pathout_motive_transport_arrow'),
    pathInductionFunctor: symbol('PathInd_func'),
    pathInductionTransformation: symbol('PathInd_transfd'),
    pathInductionTotalSource: symbol('PathIndSrc_catd'),
    pathInductionSourceTransport:
        symbol('PathIndSrc_transport_func'),
    pathInductionTotalFunctor: symbol('PathInd_funcd'),
    pathoutPiTransport: symbol('pathout_pi_transport_func'),
    pathInductionTargetTransport:
        symbol('PathIndTgt_transport_func')
});

const {
    sigmaDisplayedTransformation,
    pathoutMotives,
    pathoutPi,
    pathInductionTotalTarget,
    pathoutReflexiveEvaluationDisplayed,
    pathoutMotiveTransportObject,
    pathoutMotiveTransportArrow,
    pathInductionFunctor,
    pathInductionTransformation,
    pathInductionTotalSource,
    pathInductionSourceTransport,
    pathInductionTotalFunctor,
    pathoutPiTransport,
    pathInductionTargetTransport
} = CORE_PATHIND_INTERNALIZED_1D_SYMBOLS;

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

const homType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, homClassifier, [
        { plicity: 'explicit', value: base },
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]));

const functorType = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, functorClassifier, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]));

const functorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorCategory, [
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const transforCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    left: CoreLfTransferBuilderExpression,
    right: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, transforCategory, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: left },
        { plicity: 'explicit', value: right }
    ]);

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

const displayedFunctorCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedFunctorCategory, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target }
    ]);

const displayedTransformationType = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceFamily: CoreLfTransferBuilderExpression,
    targetFamily: CoreLfTransferBuilderExpression,
    sourceFunctor: CoreLfTransferBuilderExpression,
    targetFunctor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    decode(builder, globalCall(builder, displayedTransformationClassifier, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: sourceFamily },
        { plicity: 'implicit', value: targetFamily },
        { plicity: 'explicit', value: sourceFunctor },
        { plicity: 'explicit', value: targetFunctor }
    ]));

const oppositeAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, oppositeCategory, [{
        plicity: 'explicit',
        value: base
    }]);

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

const constantFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    value: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, constantDisplayedFamily, [
        { plicity: 'explicit', value: base },
        { plicity: 'explicit', value }
    ]);

const fibreAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, functorObject, [
        { plicity: 'implicit', value: base },
        {
            plicity: 'implicit',
            value: builder.global(familyCoefficient)
        },
        { plicity: 'explicit', value: family },
        { plicity: 'explicit', value: point }
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
    sourceFamily: CoreLfTransferBuilderExpression,
    targetFamily: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression,
    displayedFunctor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, transforComponentCapped, [
        { plicity: 'implicit', value: base },
        {
            plicity: 'implicit',
            value: builder.global(familyCoefficient)
        },
        { plicity: 'implicit', value: sourceFamily },
        { plicity: 'implicit', value: targetFamily },
        { plicity: 'explicit', value: point },
        { plicity: 'explicit', value: displayedFunctor }
    ]);

const displayedComponentAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceFamily: CoreLfTransferBuilderExpression,
    targetFamily: CoreLfTransferBuilderExpression,
    sourceFunctor: CoreLfTransferBuilderExpression,
    targetFunctor: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression,
    transformation: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, displayedComponent, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: sourceFamily },
        { plicity: 'implicit', value: targetFamily },
        { plicity: 'implicit', value: sourceFunctor },
        { plicity: 'implicit', value: targetFunctor },
        { plicity: 'explicit', value: point },
        { plicity: 'explicit', value: transformation }
    ]);

const sigmaCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, sigmaCategory, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: family }
    ]);

const sigmaTelescopeFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    displayedFunctor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, sigmaTelescopeFamily, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: family },
        { plicity: 'explicit', value: displayedFunctor }
    ]);

const sigmaPairAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    first: CoreLfTransferBuilderExpression,
    second: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression => {
    const familyClassifier = builder.lam(
        'pairPoint',
        objectType(builder, base),
        pairPoint => objectClassifierAt(
            builder,
            fibreAt(builder, base, family, pairPoint)
        ),
        explicitMode
    );
    return globalCall(builder, dependentPair, [
        {
            plicity: 'implicit',
            value: objectClassifierAt(builder, base)
        },
        { plicity: 'implicit', value: familyClassifier },
        { plicity: 'explicit', value: first },
        { plicity: 'explicit', value: second }
    ]);
};

const pullbackFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pullbackDisplayedFamily, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: family },
        { plicity: 'explicit', value: functor }
    ]);

const pullbackFamilyFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    functor: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pullbackDisplayedFamilyFunctor, [
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: functor }
    ]);

const sectionCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, sectionCategory, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: family }
    ]);

const fibreFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    sourceFamily: CoreLfTransferBuilderExpression,
    targetFamily: CoreLfTransferBuilderExpression,
    displayedFunctor: CoreLfTransferBuilderExpression,
    point: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, fibreFunctor, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: sourceFamily },
        { plicity: 'implicit', value: targetFamily },
        { plicity: 'explicit', value: displayedFunctor },
        { plicity: 'explicit', value: point }
    ]);

const sigmaDisplayedTransformationAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    family: CoreLfTransferBuilderExpression,
    sourceFunctor: CoreLfTransferBuilderExpression,
    targetFunctor: CoreLfTransferBuilderExpression,
    transformation: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, sigmaDisplayedTransformation, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: family },
        { plicity: 'implicit', value: sourceFunctor },
        { plicity: 'implicit', value: targetFunctor },
        { plicity: 'explicit', value: transformation }
    ]);

const pathoutCategoryAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutCategory, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathoutCategoryFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutCategoryFunctor, [{
        plicity: 'implicit',
        value: base
    }]);

const pathoutTransportAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutTransport, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: arrow }
    ]);

const pathoutObjectAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutObject, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: target },
        { plicity: 'explicit', value: arrow }
    ]);

const pathoutReflexiveObjectAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutReflexiveObject, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathoutReflexiveEvaluationAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutReflexiveEvaluation, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathoutReflexiveBaseTransportAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression,
    motive: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutReflexiveBaseTransport, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: arrow },
        { plicity: 'explicit', value: motive }
    ]);

const pathInductionComponentFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    motive: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionComponentFunctor, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source },
        { plicity: 'explicit', value: motive }
    ]);

const pathInductionSourceFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionSourceFamily, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathInductionTargetFamilyAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionTargetFamily, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathoutMotivesAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutMotives, [{
        plicity: 'implicit',
        value: base
    }]);

const pathoutPiAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutPi, [{
        plicity: 'implicit',
        value: base
    }]);

const pathInductionTotalTargetAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionTotalTarget, [{
        plicity: 'implicit',
        value: base
    }]);

const pathoutReflexiveEvaluationDisplayedAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutReflexiveEvaluationDisplayed, [{
        plicity: 'implicit',
        value: base
    }]);

const pathoutMotiveTransportObjectAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression,
    motive: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutMotiveTransportObject, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: arrow },
        { plicity: 'explicit', value: motive }
    ]);

const pathInductionFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionFunctor, [
        { plicity: 'implicit', value: base },
        { plicity: 'explicit', value: source }
    ]);

const pathInductionTransformationAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionTransformation, [{
        plicity: 'implicit',
        value: base
    }]);

const pathInductionTotalSourceAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionTotalSource, [{
        plicity: 'implicit',
        value: base
    }]);

const pathInductionTotalFunctorAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathInductionTotalFunctor, [{
        plicity: 'implicit',
        value: base
    }]);

const pathoutPiTransportAt = (
    builder: CoreLfTransferScopedBuilder,
    base: CoreLfTransferBuilderExpression,
    source: CoreLfTransferBuilderExpression,
    target: CoreLfTransferBuilderExpression,
    arrow: CoreLfTransferBuilderExpression,
    motive: CoreLfTransferBuilderExpression
): CoreLfTransferBuilderExpression =>
    globalCall(builder, pathoutPiTransport, [
        { plicity: 'implicit', value: base },
        { plicity: 'implicit', value: source },
        { plicity: 'implicit', value: target },
        { plicity: 'explicit', value: arrow },
        { plicity: 'explicit', value: motive }
    ]);

const source = (sourceFragment: string) => ({
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceFragment
});

const modifiers = (
    rigidity: 'ordinary' | 'constant' | 'injective',
    sourceOpacity: 'transparent' | 'opaque'
) => ({
    visibility: 'public' as const,
    rigidity,
    sourceOpacity
});

const cartesianFamiliesAt = (b: CoreLfTransferScopedBuilder,
    K: CoreLfTransferBuilderExpression): CoreLfTransferBuilderExpression =>
    globalCall(b, cartesianFunctorCategory, [
        { plicity: 'explicit', value: K },
        { plicity: 'explicit', value: b.global(familyCoefficient) }
    ]);
const inclusionAt = (b: CoreLfTransferScopedBuilder,
    K: CoreLfTransferBuilderExpression): CoreLfTransferBuilderExpression =>
    globalCall(b, cartesianInclusion, [
        { plicity: 'explicit', value: K },
        { plicity: 'explicit', value: b.global(familyCoefficient) }
    ]);
const composeAt = (b: CoreLfTransferScopedBuilder,
    A: CoreLfTransferBuilderExpression, B: CoreLfTransferBuilderExpression,
    C: CoreLfTransferBuilderExpression, G: CoreLfTransferBuilderExpression,
    F: CoreLfTransferBuilderExpression): CoreLfTransferBuilderExpression =>
    globalCall(b, functorComposition, [
        { plicity: 'implicit', value: A }, { plicity: 'implicit', value: B },
        { plicity: 'implicit', value: C }, { plicity: 'explicit', value: G },
        { plicity: 'explicit', value: F }
    ]);
const ordinaryComponentAt = (b: CoreLfTransferScopedBuilder,
    K: CoreLfTransferBuilderExpression, R: CoreLfTransferBuilderExpression,
    S: CoreLfTransferBuilderExpression, T: CoreLfTransferBuilderExpression,
    k: CoreLfTransferBuilderExpression, eta: CoreLfTransferBuilderExpression, pattern = false
): CoreLfTransferBuilderExpression => {
    const constant = constantFamilyAt(b, K, b.global(familyCoefficient));
    const inferred = (value: CoreLfTransferBuilderExpression) => pattern ? b.wildcard(value) : value;
    return globalCall(b, strictTransforView, [
        { plicity: 'implicit', value: inferred(fibreAt(b, K, R, k)) },
        { plicity: 'implicit', value: inferred(b.global(familyCoefficient)) },
        { plicity: 'implicit', value: inferred(fibreFunctorAt(b, K, R, constant, S, k)) },
        { plicity: 'implicit', value: inferred(fibreFunctorAt(b, K, R, constant, T, k)) },
        { plicity: 'explicit', value: displayedComponentAt(b, K, inferred(R), inferred(constant), inferred(S), inferred(T), k, eta) }
    ]);
};

const sigmaDisplayedTransformationType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'K',
        builder.global(category),
        K => builder.pi(
            'R',
            displayedFamilyType(builder, K),
            R => {
                const constantCategories = constantFamilyAt(
                    builder,
                    K,
                    builder.global(familyCoefficient)
                );
                return builder.pi(
                    'S',
                    displayedFunctorType(
                        builder,
                        K,
                        R,
                        constantCategories
                    ),
                    S => builder.pi(
                        'T',
                        displayedFunctorType(
                            builder,
                            K,
                            R,
                            constantCategories
                        ),
                        T => builder.pi(
                            'eta',
                            displayedTransformationType(
                                builder,
                                K,
                                R,
                                constantCategories,
                                S,
                                T
                            ),
                            _eta => displayedFunctorType(
                                builder,
                                sigmaCategoryAt(builder, K, R),
                                sigmaTelescopeFamilyAt(
                                    builder,
                                    K,
                                    R,
                                    S
                                ),
                                sigmaTelescopeFamilyAt(
                                    builder,
                                    K,
                                    R,
                                    T
                                )
                            ),
                            explicitMode
                        ),
                        implicitMode
                    ),
                    implicitMode
                );
            },
            implicitMode
        ),
        implicitMode
    ));
};

const pathoutMotivesType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFamilyType(builder, Z),
        implicitMode
    ));
};

const pathoutMotivesBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => pullbackFamilyAt(
            builder,
            Z,
            oppositeAt(builder, builder.global(familyCoefficient)),
            builder.global(displayedCategoryFunctor),
            oppositeFunctorAt(
                builder,
                oppositeAt(builder, Z),
                builder.global(familyCoefficient),
                pathoutCategoryFunctorAt(builder, Z)
            )
        ),
        implicitMode
    ));
};

const pathoutPiType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFunctorType(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            constantFamilyAt(
                builder,
                Z,
                builder.global(familyCoefficient)
            )
        ),
        implicitMode
    ));
};

const pathoutPiBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => {
            const opCat = oppositeAt(
                builder,
                builder.global(familyCoefficient)
            );
            const opPathout = oppositeFunctorAt(
                builder,
                oppositeAt(builder, Z),
                builder.global(familyCoefficient),
                pathoutCategoryFunctorAt(builder, Z)
            );
            return functorHomCappedAt(
                builder,
                displayedCategoryAt(builder, opCat),
                displayedCategoryAt(builder, Z),
                pullbackFamilyFunctorAt(builder, Z, opCat, opPathout),
                builder.global(displayedCategoryFunctor),
                constantFamilyAt(
                    builder,
                    opCat,
                    builder.global(familyCoefficient)
                ),
                builder.global(piInternalDisplayedFunctor)
            );
        },
        implicitMode
    ));
};

const pathInductionTotalTargetType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFamilyType(
            builder,
            sigmaCategoryAt(builder, Z, pathoutMotivesAt(builder, Z))
        ),
        implicitMode
    ));
};

const pathInductionTotalTargetBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => sigmaTelescopeFamilyAt(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            pathoutPiAt(builder, Z)
        ),
        implicitMode
    ));
};

const pathoutReflexiveEvaluationDisplayedType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFunctorType(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            constantFamilyAt(
                builder,
                Z,
                builder.global(familyCoefficient)
            )
        ),
        implicitMode
    ));
};

const pathoutMotiveTransportObjectType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => builder.pi(
                'y',
                objectType(builder, Z),
                y => builder.pi(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.pi(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        _E => displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, y)
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
    ));
};

const pathoutMotiveTransportObjectBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => builder.lam(
            'x',
            objectType(builder, Z),
            x => builder.lam(
                'y',
                objectType(builder, Z),
                y => builder.lam(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.lam(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => pullbackFamilyAt(builder,
                            pathoutCategoryAt(builder, Z, y),
                            pathoutCategoryAt(builder, Z, x),
                            E, pathoutTransportAt(builder, Z, x, y, p)),
                        explicitMode
                    ),
                    explicitMode
                ),
                implicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const pathoutMotiveTransportArrowType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => builder.pi(
                'y',
                objectType(builder, Z),
                y => builder.pi(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.pi(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => homType(
                            builder,
                            sigmaCategoryAt(
                                builder,
                                Z,
                                pathoutMotivesAt(builder, Z)
                            ),
                            sigmaPairAt(
                                builder,
                                Z,
                                pathoutMotivesAt(builder, Z),
                                x,
                                E
                            ),
                            sigmaPairAt(
                                builder,
                                Z,
                                pathoutMotivesAt(builder, Z),
                                y,
                                pathoutMotiveTransportObjectAt(
                                    builder,
                                    Z,
                                    x,
                                    y,
                                    p,
                                    E
                                )
                            )
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
    ));
};

const pathoutMotiveTransportArrowBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => builder.lam(
            'x',
            objectType(builder, Z),
            x => builder.lam(
                'y',
                objectType(builder, Z),
                y => builder.lam(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.lam(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => globalCall(builder, sigmaTransportArrow, [
                            { plicity: 'implicit', value: Z },
                            {
                                plicity: 'explicit',
                                value: pathoutMotivesAt(builder, Z)
                            },
                            { plicity: 'implicit', value: x },
                            { plicity: 'implicit', value: y },
                            { plicity: 'explicit', value: p },
                            { plicity: 'explicit', value: E }
                        ]),
                        explicitMode
                    ),
                    explicitMode
                ),
                implicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const pathInductionFunctorType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => displayedFunctorType(
                builder,
                displayedCategoryAt(
                    builder,
                    pathoutCategoryAt(builder, Z, x)
                ),
                pathInductionSourceFamilyAt(builder, Z, x),
                pathInductionTargetFamilyAt(builder, Z, x)
            ),
            explicitMode
        ),
        implicitMode
    ));
};

const pathInductionTransformationType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedTransformationType(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            constantFamilyAt(
                builder,
                Z,
                builder.global(familyCoefficient)
            ),
            pathoutReflexiveEvaluationDisplayedAt(builder, Z),
            pathoutPiAt(builder, Z)
        ),
        implicitMode
    ));
};

const pathInductionTotalSourceType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFamilyType(
            builder,
            sigmaCategoryAt(builder, Z, pathoutMotivesAt(builder, Z))
        ),
        implicitMode
    ));
};

const pathInductionTotalSourceBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => sigmaTelescopeFamilyAt(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            pathoutReflexiveEvaluationDisplayedAt(builder, Z)
        ),
        implicitMode
    ));
};

const pathInductionSourceTransportType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => builder.pi(
                'y',
                objectType(builder, Z),
                y => builder.pi(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.pi(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => functorType(
                            builder,
                            fibreAt(
                                builder,
                                sigmaCategoryAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z)
                                ),
                                pathInductionTotalSourceAt(builder, Z),
                                sigmaPairAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z),
                                    x,
                                    E
                                )
                            ),
                            fibreAt(
                                builder,
                                sigmaCategoryAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z)
                                ),
                                pathInductionTotalSourceAt(builder, Z),
                                sigmaPairAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z),
                                    y,
                                    pathoutMotiveTransportObjectAt(
                                        builder,
                                        Z,
                                        x,
                                        y,
                                        p,
                                        E
                                    )
                                )
                            )
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
    ));
};

const pathInductionSourceTransportBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => builder.lam(
            'x',
            objectType(builder, Z),
            x => builder.lam(
                'y',
                objectType(builder, Z),
                y => builder.lam(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.lam(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => pathoutReflexiveBaseTransportAt(
                            builder,
                            Z,
                            x,
                            y,
                            p,
                            E
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
    ));
};

const pathInductionTotalFunctorType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => displayedFunctorType(
            builder,
            sigmaCategoryAt(builder, Z, pathoutMotivesAt(builder, Z)),
            pathInductionTotalSourceAt(builder, Z),
            pathInductionTotalTargetAt(builder, Z)
        ),
        implicitMode
    ));
};

const pathInductionTotalFunctorBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => sigmaDisplayedTransformationAt(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            pathoutReflexiveEvaluationDisplayedAt(builder, Z),
            pathoutPiAt(builder, Z),
            pathInductionTransformationAt(builder, Z)
        ),
        implicitMode
    ));
};

const pathoutPiTransportType = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => builder.pi(
                'y',
                objectType(builder, Z),
                y => builder.pi(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.pi(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => functorType(
                            builder,
                            sectionCategoryAt(
                                builder,
                                pathoutCategoryAt(builder, Z, x),
                                E
                            ),
                            sectionCategoryAt(
                                builder,
                                pathoutCategoryAt(builder, Z, y),
                                pathoutMotiveTransportObjectAt(
                                    builder,
                                    Z,
                                    x,
                                    y,
                                    p,
                                    E
                                )
                            )
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
    ));
};

const pathoutPiTransportBody = (): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => builder.lam(
            'x',
            objectType(builder, Z),
            x => builder.lam(
                'y',
                objectType(builder, Z),
                y => builder.lam(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.lam(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => globalCall(builder, sectionPullbackFunctor, [
                            {
                                plicity: 'implicit',
                                value: pathoutCategoryAt(builder, Z, y)
                            },
                            {
                                plicity: 'implicit',
                                value: pathoutCategoryAt(builder, Z, x)
                            },
                            {
                                plicity: 'explicit',
                                value: pathoutTransportAt(
                                    builder,
                                    Z,
                                    x,
                                    y,
                                    p
                                )
                            },
                            { plicity: 'explicit', value: E }
                        ]),
                        explicitMode
                    ),
                    explicitMode
                ),
                implicitMode
            ),
            implicitMode
        ),
        implicitMode
    ));
};

const pathInductionTargetTransportType =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.pi(
        'Z',
        builder.global(category),
        Z => builder.pi(
            'x',
            objectType(builder, Z),
            x => builder.pi(
                'y',
                objectType(builder, Z),
                y => builder.pi(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.pi(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => functorType(
                            builder,
                            fibreAt(
                                builder,
                                sigmaCategoryAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z)
                                ),
                                pathInductionTotalTargetAt(builder, Z),
                                sigmaPairAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z),
                                    x,
                                    E
                                )
                            ),
                            fibreAt(
                                builder,
                                sigmaCategoryAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z)
                                ),
                                pathInductionTotalTargetAt(builder, Z),
                                sigmaPairAt(
                                    builder,
                                    Z,
                                    pathoutMotivesAt(builder, Z),
                                    y,
                                    pathoutMotiveTransportObjectAt(
                                        builder,
                                        Z,
                                        x,
                                        y,
                                        p,
                                        E
                                    )
                                )
                            )
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
    ));
};

const pathInductionTargetTransportBody =
(): CoreLfTransferExpression => {
    const builder = new CoreLfTransferScopedBuilder();
    return builder.term(builder.lam(
        'Z',
        builder.global(category),
        Z => builder.lam(
            'x',
            objectType(builder, Z),
            x => builder.lam(
                'y',
                objectType(builder, Z),
                y => builder.lam(
                    'p',
                    homType(builder, Z, x, y),
                    p => builder.lam(
                        'E',
                        displayedFamilyType(
                            builder,
                            pathoutCategoryAt(builder, Z, x)
                        ),
                        E => pathoutPiTransportAt(
                            builder,
                            Z,
                            x,
                            y,
                            p,
                            E
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
    ));
};

const sigmaTrustedDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze([
    Object.freeze({
        order: 0,
        symbol: sigmaDisplayedTransformation,
        type: sigmaDisplayedTransformationType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('constant', 'opaque'),
        provenance: source('constant symbol Sigma_transfd_funcd [K : Cat]')
    })
]);

const preludeDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze([
    Object.freeze({
        order: 0,
        symbol: pathoutMotives,
        type: pathoutMotivesType(),
        body: coreLfTransferExplicitBody(pathoutMotivesBody()),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source('symbol PathOutMotives_catd [Z : Cat]')
    }),
    Object.freeze({
        order: 1,
        symbol: pathoutPi,
        type: pathoutPiType(),
        body: coreLfTransferExplicitBody(pathoutPiBody()),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source('symbol PathOutPi_funcd [Z : Cat]')
    }),
    Object.freeze({
        order: 2,
        symbol: pathInductionTotalTarget,
        type: pathInductionTotalTargetType(),
        body: coreLfTransferExplicitBody(
            pathInductionTotalTargetBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source('symbol PathIndTgt_catd [Z : Cat]')
    })
]);

const theoremTrustedDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze([
    Object.freeze({
        order: 0,
        symbol: pathoutReflexiveEvaluationDisplayed,
        type: pathoutReflexiveEvaluationDisplayedType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('constant', 'opaque'),
        provenance: source(
            'constant symbol PathOutReflEval_funcd [Z : Cat]'
        )
    }),
    Object.freeze({
        order: 1,
        symbol: pathInductionFunctor,
        type: pathInductionFunctorType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('constant', 'opaque'),
        provenance: source('constant symbol PathInd_func [Z : Cat]')
    }),
    Object.freeze({
        order: 2,
        symbol: pathInductionTransformation,
        type: pathInductionTransformationType(),
        body: coreLfTransferAbsentBody(),
        modifiers: modifiers('constant', 'opaque'),
        provenance: source('constant symbol PathInd_transfd [Z : Cat]')
    })
]);

const derivedLibraryDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze([
    Object.freeze({
        order: 0,
        symbol: pathoutMotiveTransportObject,
        type: pathoutMotiveTransportObjectType(),
        body: coreLfTransferExplicitBody(
            pathoutMotiveTransportObjectBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol pathout_motive_transport_obj [Z : Cat]'
        )
    }),
    Object.freeze({
        order: 1,
        symbol: pathoutMotiveTransportArrow,
        type: pathoutMotiveTransportArrowType(),
        body: coreLfTransferExplicitBody(
            pathoutMotiveTransportArrowBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol pathout_motive_transport_arrow [Z : Cat]'
        )
    }),
    Object.freeze({
        order: 2,
        symbol: pathInductionTotalSource,
        type: pathInductionTotalSourceType(),
        body: coreLfTransferExplicitBody(
            pathInductionTotalSourceBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source('symbol PathIndSrc_catd [Z : Cat]')
    }),
    Object.freeze({
        order: 3,
        symbol: pathInductionSourceTransport,
        type: pathInductionSourceTransportType(),
        body: coreLfTransferExplicitBody(
            pathInductionSourceTransportBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol PathIndSrc_transport_func [Z : Cat]'
        )
    }),
    Object.freeze({
        order: 4,
        symbol: pathInductionTotalFunctor,
        type: pathInductionTotalFunctorType(),
        body: coreLfTransferExplicitBody(
            pathInductionTotalFunctorBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source('symbol PathInd_funcd [Z : Cat]')
    }),
    Object.freeze({
        order: 5,
        symbol: pathoutPiTransport,
        type: pathoutPiTransportType(),
        body: coreLfTransferExplicitBody(pathoutPiTransportBody()),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol pathout_pi_transport_func [Z : Cat]'
        )
    }),
    Object.freeze({
        order: 6,
        symbol: pathInductionTargetTransport,
        type: pathInductionTargetTransportType(),
        body: coreLfTransferExplicitBody(
            pathInductionTargetTransportBody()
        ),
        modifiers: modifiers('ordinary', 'transparent'),
        provenance: source(
            'symbol PathIndTgt_transport_func [Z : Cat]'
        )
    })
]);

const derivedLibraryPrefixDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze(
    derivedLibraryDeclarations.slice(0, 3)
);

const derivedLibrarySuffixDeclarations:
readonly CoreLfTransferDeclaration[] = Object.freeze(
    derivedLibraryDeclarations.slice(3)
);

const sigmaObjectComponentRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const K = builder.capture('K');
    const R = builder.capture('R');
    const S = builder.capture('S');
    const T = builder.capture('T');
    const eta = builder.capture('eta');
    const k = builder.capture('k');
    const r = builder.capture('r');
    const constantCategories = constantFamilyAt(
        builder,
        K,
        builder.global(familyCoefficient)
    );
    return {
        order: 0,
        id: 'pathind.internalized.sigma-transfd-object-component',
        groupId: 'pathind.internalized.runtime-projections',
        clauseOrder: 0,
        sourceOwner: transforComponentCapped,
        variables: [
            {
                name: 'K',
                type: builder.template(builder.global(category))
            },
            {
                name: 'R',
                type: builder.template(displayedFamilyType(builder, K))
            },
            {
                name: 'S',
                type: builder.template(displayedFunctorType(
                    builder,
                    K,
                    R,
                    constantCategories
                ))
            },
            {
                name: 'T',
                type: builder.template(displayedFunctorType(
                    builder,
                    K,
                    R,
                    constantCategories
                ))
            },
            {
                name: 'eta',
                type: builder.template(displayedTransformationType(
                    builder,
                    K,
                    R,
                    constantCategories,
                    S,
                    T
                ))
            },
            {
                name: 'k',
                type: builder.template(objectType(builder, K))
            },
            {
                name: 'r',
                type: builder.template(objectType(
                    builder,
                    fibreAt(builder, K, R, k)
                ))
            }
        ],
        left: builder.pattern(componentAt(
            builder,
            sigmaCategoryAt(builder, K, R),
            sigmaTelescopeFamilyAt(builder, K, R, S),
            sigmaTelescopeFamilyAt(builder, K, R, T),
            sigmaPairAt(builder, K, R, k, r),
            sigmaDisplayedTransformationAt(
                builder,
                K,
                R,
                S,
                T,
                eta
            )
        )),
        right: builder.template(componentAt(
            builder,
            fibreAt(builder, K, R, k),
            fibreFunctorAt(
                builder,
                K,
                R,
                constantCategories,
                S,
                k
            ),
            fibreFunctorAt(
                builder,
                K,
                R,
                constantCategories,
                T,
                k
            ),
            r,
            ordinaryComponentAt(builder, K, R, S, T, k, eta)
        )),
        provenance: source(
            'rule @tapp0_fapp0 _ Cat_cart _ _ (Struct_sigma $k $r) ' +
            '(@Sigma_transfd_funcd $K $R $S $T $eta)'
        )
    };
};

const pathoutReflexiveEvaluationComponentRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const constantCategories = constantFamilyAt(
        builder,
        Z,
        builder.global(familyCoefficient)
    );
    return {
        order: 1,
        id: 'pathind.internalized.pathout-refl-eval-component',
        groupId: 'pathind.internalized.runtime-projections',
        clauseOrder: 1,
        sourceOwner: transforComponentCapped,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            }
        ],
        left: builder.pattern(componentAt(
            builder,
            Z,
            pathoutMotivesAt(builder, Z),
            constantCategories,
            x,
            pathoutReflexiveEvaluationDisplayedAt(builder, Z)
        )),
        right: builder.template(composeAt(builder,
            cartesianFamiliesAt(builder, pathoutCategoryAt(builder, Z, x)),
            displayedCategoryAt(builder, pathoutCategoryAt(builder, Z, x)),
            builder.global(familyCoefficient),
            pathoutReflexiveEvaluationAt(builder, Z, x),
            inclusionAt(builder, pathoutCategoryAt(builder, Z, x)))),
        provenance: source(
            'rule @tapp0_fapp0 _ Cat_cart _ _ $x ' +
            '(@PathOutReflEval_funcd $Z)'
        )
    };
};

const pathInductionFunctorComponentRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const E = builder.capture('E');
    const pathout = pathoutCategoryAt(builder, Z, x);
    return {
        order: 3,
        id: 'pathind.internalized.path-ind-functor-component',
        groupId: 'pathind.internalized.runtime-projections',
        clauseOrder: 3,
        sourceOwner: transforComponentCapped,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(builder, pathout))
            }
        ],
        left: builder.pattern(componentAt(
            builder,
            builder.wildcard(displayedCategoryAt(builder, pathout)),
            builder.wildcard(pathInductionSourceFamilyAt(builder, Z, x)),
            builder.wildcard(pathInductionTargetFamilyAt(builder, Z, x)),
            E,
            pathInductionFunctorAt(builder, Z, x)
        )),
        right: builder.template(pathInductionComponentFunctorAt(
            builder,
            Z,
            x,
            E
        )),
        provenance: source(
            'rule @tapp0_fapp0 _ Cat_cart _ _ $E ' +
            '(@PathInd_func $Z $x)'
        )
    };
};

const pathInductionFunctorComponentPostPrefixSubjectFusionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const E = builder.capture('E');
    const pathout = pathoutCategoryAt(builder, Z, x);
    const motives = displayedCategoryAt(builder, pathout);
    return {
        order: 2,
        id:
            'pathind.internalized.' +
            'path-ind-functor-component-post-prefix-subject-fusion',
        groupId: 'pathind.internalized.runtime-projections',
        clauseOrder: 2,
        sourceOwner: decodeOwner,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(builder, pathout))
            }
        ],
        left: builder.pattern(objectType(
            builder,
            functorCategoryAt(
                builder,
                fibreAt(
                    builder,
                    motives,
                    pathInductionSourceFamilyAt(builder, Z, x),
                    E
                ),
                fibreAt(
                    builder,
                    motives,
                    pathInductionTargetFamilyAt(builder, Z, x),
                    E
                )
            )
        )),
        right: builder.template(objectType(
            builder,
            functorCategoryAt(
                builder,
                fibreAt(
                    builder,
                    pathout,
                    E,
                    pathoutReflexiveObjectAt(builder, Z, x)
                ),
                sectionCategoryAt(builder, pathout, E)
            )
        )),
        provenance: source(
            'derived stable post-prefix PathInd_func component subject ' +
            'fusion from active Hom/Functor, Catd/Functor comparison, ' +
            'fixed evaluation, Pi object, PathInd_src, and PathInd_tgt ' +
            'equations'
        )
    };
};

const pathInductionTransformationComponentRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const constantCategories = constantFamilyAt(
        builder,
        Z,
        builder.global(familyCoefficient)
    );
    return {
        order: 6,
        id: 'pathind.internalized.path-ind-transfd-component',
        groupId: 'pathind.internalized.runtime-projections',
        clauseOrder: 6,
        sourceOwner: strictTransforView,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            }
        ],
        left: builder.pattern(ordinaryComponentAt(builder, Z,
            pathoutMotivesAt(builder, Z), pathoutReflexiveEvaluationDisplayedAt(builder, Z),
            pathoutPiAt(builder, Z), x, pathInductionTransformationAt(builder, Z), true)),
        right: builder.template((() => {
            const base = pathoutCategoryAt(builder, Z, x), cart = cartesianFamiliesAt(builder, base);
            const ambient = displayedCategoryAt(builder, base), coefficient = builder.global(familyCoefficient);
            const source = pathInductionSourceFamilyAt(builder, Z, x);
            const target = pathInductionTargetFamilyAt(builder, Z, x);
            const inclusion = inclusionAt(builder, base);
            const reindex = globalCall(builder, prewhiskeringAction, [
                { plicity: 'implicit', value: cart }, { plicity: 'implicit', value: ambient },
                { plicity: 'implicit', value: coefficient }, { plicity: 'explicit', value: inclusion },
                { plicity: 'implicit', value: source }, { plicity: 'implicit', value: target }
            ]);
            return functorObjectAt(builder,
                transforCategoryAt(builder, ambient, coefficient, source, target),
                transforCategoryAt(builder, cart, coefficient,
                    composeAt(builder, cart, ambient, coefficient, source, inclusion),
                    composeAt(builder, cart, ambient, coefficient, target, inclusion)),
                reindex, pathInductionFunctorAt(builder, Z, x));
        })()),
        provenance: source(
            'rule @tdapp0_fapp0 $Z _ _ _ _ $x ' +
            '(@PathInd_transfd $Z)'
        )
    };
};

const pathInductionSourceFibreStagedParentFusionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const E = builder.capture('E');
    const motives = pathoutMotivesAt(builder, Z);
    return {
        order: 9,
        id:
            'pathind.internalized.' +
            'path-ind-source-fibre-at-sigma-pair-presentation-fusion',
        groupId: 'pathind.internalized.runtime-source-fibre-extension',
        clauseOrder: 0,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(
                    builder,
                    pathoutCategoryAt(builder, Z, x)
                ))
            }
        ],
        left: builder.pattern(fibreAt(
            builder,
            sigmaCategoryAt(builder, Z, motives),
            pathInductionTotalSourceAt(builder, Z),
            sigmaPairAt(
                builder,
                Z,
                motives,
                x,
                E
            )
        )),
        right: builder.template(fibreAt(
            builder,
            pathoutCategoryAt(builder, Z, x),
            E,
            pathoutReflexiveObjectAt(builder, Z, x)
        )),
        provenance: source(
            'derived staged complete-parent source-fibre fusion ' +
            'from active lines 13297-13314, 19080-19091, and 19296-19317'
        )
    };
};

const transportedMotiveReflexiveFibreFusionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const y = builder.capture('y');
    const p = builder.capture('p');
    const E = builder.capture('E');
    return {
        order: 10,
        id:
            'pathind.internalized.' +
            'transported-motive-reflexive-fibre-presentation-fusion',
        groupId: 'pathind.internalized.runtime-source-fibre-extension',
        clauseOrder: 1,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'y',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'p',
                type: builder.template(homType(builder, Z, x, y))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(
                    builder,
                    pathoutCategoryAt(builder, Z, x)
                ))
            }
        ],
        left: builder.pattern(fibreAt(
            builder,
            pathoutCategoryAt(builder, Z, y),
            pathoutMotiveTransportObjectAt(builder, Z, x, y, p, E),
            pathoutReflexiveObjectAt(builder, Z, y)
        )),
        right: builder.template(fibreAt(
            builder,
            pathoutCategoryAt(builder, Z, x),
            E,
            pathoutObjectAt(builder, Z, x, y, p)
        )),
        provenance: source(
            'derived complete-parent pullback-fibre and PathOut ' +
            'reflexive-action fusion from active lines 12034-12035, ' +
            '18981-18992, 19046-19058, 19132-19154, and 19309-19318'
        )
    };
};

const pathoutPiTransportPostDeltaPresentationFusionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const y = builder.capture('y');
    const p = builder.capture('p');
    const E = builder.capture('E');
    const sourcePathout = pathoutCategoryAt(builder, Z, x);
    const targetPathout = pathoutCategoryAt(builder, Z, y);
    const transportedMotive = pullbackFamilyAt(
        builder,
        targetPathout,
        sourcePathout,
        E,
        pathoutTransportAt(builder, Z, x, y, p)
    );
    return {
        order: 11,
        id:
            'pathind.internalized.' +
            'pathout-pi-transport-post-delta-presentation-fusion',
        groupId: 'pathind.internalized.runtime-source-fibre-extension',
        clauseOrder: 2,
        sourceOwner: decodeOwner,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'y',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'p',
                type: builder.template(homType(builder, Z, x, y))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(
                    builder,
                    sourcePathout
                ))
            }
        ],
        left: builder.pattern(objectType(
            builder,
            functorCategoryAt(
                builder,
                displayedFunctorCategoryAt(
                    builder,
                    sourcePathout,
                    constantFamilyAt(
                        builder,
                        sourcePathout,
                        builder.global(terminalCategory)
                    ),
                    E
                ),
                displayedFunctorCategoryAt(
                    builder,
                    targetPathout,
                    constantFamilyAt(
                        builder,
                        targetPathout,
                        builder.global(terminalCategory)
                    ),
                    transportedMotive
                )
            )
        )),
        right: builder.template(objectType(
            builder,
            functorCategoryAt(
                builder,
                sectionCategoryAt(builder, sourcePathout, E),
                sectionCategoryAt(
                    builder,
                    targetPathout,
                    pathoutMotiveTransportObjectAt(
                        builder,
                        Z,
                        x,
                        y,
                        p,
                        E
                    )
                )
            )
        )),
        provenance: source(
            'derived stable post-Functor-delta complete-parent ' +
            'section-pullback presentation fusion from active lines ' +
            '3316-3317, 12554-12561, 16502-16506, 19139-19153, ' +
            'and 19734-19744'
        )
    };
};

const pathInductionTargetFibreStagedParentFusionRule =
(): CoreLfTransferRuntimeRule => {
    const builder = new CoreLfTransferScopedBuilder();
    const Z = builder.capture('Z');
    const x = builder.capture('x');
    const E = builder.capture('E');
    const motives = pathoutMotivesAt(builder, Z);
    return {
        order: 12,
        id:
            'pathind.internalized.' +
            'path-ind-target-fibre-at-sigma-pair-presentation-fusion',
        groupId: 'pathind.internalized.runtime-source-fibre-extension',
        clauseOrder: 3,
        sourceOwner: functorObject,
        variables: [
            {
                name: 'Z',
                type: builder.template(builder.global(category))
            },
            {
                name: 'x',
                type: builder.template(objectType(builder, Z))
            },
            {
                name: 'E',
                type: builder.template(displayedFamilyType(
                    builder,
                    pathoutCategoryAt(builder, Z, x)
                ))
            }
        ],
        left: builder.pattern(fibreAt(
            builder,
            sigmaCategoryAt(builder, Z, motives),
            pathInductionTotalTargetAt(builder, Z),
            sigmaPairAt(builder, Z, motives, x, E)
        )),
        right: builder.template(sectionCategoryAt(
            builder,
            pathoutCategoryAt(builder, Z, x),
            E
        )),
        provenance: source(
            'derived staged complete-parent target-fibre fusion ' +
            'from active lines 12554-12561, 13297-13314, ' +
            '19018-19041, and 19751-19759'
        )
    };
};

// Existing native whole family composition/pullback comparison. The explicit
// Core uses the native comp_fapp0(Cat_cat,...) head after unfolding its facade.
const familyCompositionPullbackRule = (): CoreLfTransferProofRule => {
    const b = new CoreLfTransferScopedBuilder();
    const A=b.capture('A'), B=b.capture('B'), E=b.capture('E'), F=b.capture('F');
    const variable=(name:string,type:CoreLfTransferBuilderExpression)=>({name,role:'matched' as const,type:b.template(type)});
    return {
        order:1,id:'categorical.reindex.composition-presentation',sourceOwner:genericComposition,
        variables:[variable('A',b.global(category)),variable('B',b.global(category)),
            variable('E',displayedFamilyType(b,B)),variable('F',functorType(b,A,B))],
        problem:{left:b.pattern(globalCall(b,genericComposition,[b.global(ordinaryCategories),A,B,b.global(familyCoefficient),E,F].map((value,i)=>({value,plicity:i<4?'implicit':'explicit'})))),
            right:b.pattern(pullbackFamilyAt(b,A,B,E,F))},
        generatedConstraints:[{left:b.template(A),right:b.template(A)}],
        provenance:source('unif_rule @comp_fapp0 Cat_cat $A $B Cat_cart $E $F ≡ @Pullback_catd $A $B $E $F ↪ [ tt ≡ tt ];')
    };
};

const baseRuntimeRules: readonly CoreLfTransferRuntimeRule[] = Object.freeze([
    sigmaObjectComponentRule(),
    pathoutReflexiveEvaluationComponentRule(),
    pathInductionFunctorComponentPostPrefixSubjectFusionRule(),
    pathInductionFunctorComponentRule(),
    pathInductionTransformationComponentRule()
].map((rule, order) => ({ ...rule, order, clauseOrder: order })));

const sourceFibreExtensionRules:
readonly CoreLfTransferRuntimeRule[] = Object.freeze([
    pathInductionSourceFibreStagedParentFusionRule(),
    transportedMotiveReflexiveFibreFusionRule(),
    pathoutPiTransportPostDeltaPresentationFusionRule(),
    pathInductionTargetFibreStagedParentFusionRule()
].map((rule, index) => ({ ...rule, order: baseRuntimeRules.length + index })));

const runtimeRules: readonly CoreLfTransferRuntimeRule[] = Object.freeze([
    ...baseRuntimeRules,
    ...sourceFibreExtensionRules
]);

const commonExternalSymbols = Object.freeze([
    cartesianFunctorCategory, cartesianInclusion, strictTransforView, functorComposition, genericComposition, ordinaryCategories, prewhiskeringAction,
    category,
    decodeOwner,
    objectClassifier,
    homClassifier,
    functorClassifier,
    functorCategory,
    familyCoefficient,
    displayedCategoryCategory,
    displayedFunctorCategory,
    displayedFamilyClassifier,
    displayedFunctorClassifier,
    displayedTransformationClassifier,
    displayedComponent,
    functorObject,
    functorHomCapped,
    transforComponentCapped,
    transforCategory,
    sigmaCategory,
    sigmaTelescopeFamily,
    dependentPair,
    constantDisplayedFamily,
    sigmaTransportArrow,
    oppositeCategory,
    oppositeFunctor,
    pullbackDisplayedFamily,
    pullbackDisplayedFamilyFunctor,
    displayedCategoryFunctor,
    piInternalDisplayedFunctor,
    pullbackPi,
    fibreFunctor,
    sectionCategory,
    terminalCategory,
    sectionCategoryFunctor,
    sectionPullbackFunctor,
    displayedInternalCell,
    pathoutCategory,
    pathoutCategoryFunctor,
    pathoutTransport,
    pathoutObject,
    pathoutReflexiveObject,
    pathoutReflexiveEvaluation,
    pathoutReflexiveBaseTransport,
    pathInductionSection,
    pathInductionSourceFamily,
    pathInductionTargetFamily,
    pathInductionComponentFunctor
]);

const uniqueSymbols = (
    values: readonly CoreLfQualifiedSymbol[]
): readonly CoreLfQualifiedSymbol[] => {
    const seen = new Set<string>();
    return values.filter(value => {
        const key = `${value.moduleId}.${value.name}`;
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
    });
};

const moduleSpec = (
    fragmentId: string,
    declarations: readonly CoreLfTransferDeclaration[],
    externalSymbols: readonly CoreLfQualifiedSymbol[],
    rules: readonly CoreLfTransferRuntimeRule[] = []
): CoreLfModuleSpec => createCoreLfModuleSpec({
    revision: `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-${fragmentId}`,
    moduleId: MODULE_ID,
    fragmentId,
    authorityPath: 'emdash2/emdash3_2.lp',
    sourceSha256: CORE_PATHOUT_FOUNDATION_SOURCE_SHA256,
    dependencies: [],
    externalSymbols: uniqueSymbols(externalSymbols).map(target => ({
        symbol: target,
        availability: 'earlier-fragment' as const
    })),
    declarations,
    inductives: [],
    runtimeRules: rules,
    proofRules: []
});

export const CORE_PATHIND_INTERNALIZED_1D_SIGMA_MODULE = moduleSpec(
    'pathind-internalized-1d-sigma-trusted',
    sigmaTrustedDeclarations,
    commonExternalSymbols
);

export const CORE_PATHIND_INTERNALIZED_1D_PRELUDE_MODULE = moduleSpec(
    'pathind-internalized-1d-prelude',
    preludeDeclarations,
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol)
    ]
);

export const CORE_PATHIND_INTERNALIZED_1D_TRUSTED_MODULE = moduleSpec(
    'pathind-internalized-1d-theorem-trusted',
    theoremTrustedDeclarations,
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol)
    ]
);

export const CORE_PATHIND_INTERNALIZED_1D_BASE_RUNTIME_MODULE = moduleSpec(
    'pathind-internalized-1d-runtime-base',
    [],
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol),
        ...theoremTrustedDeclarations.map(entry => entry.symbol)
    ],
    baseRuntimeRules
);

export const CORE_PATHIND_INTERNALIZED_1D_MOTIVE_MODULE = moduleSpec(
    'pathind-internalized-1d-motive',
    derivedLibraryPrefixDeclarations.slice(0, 1),
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol),
        ...theoremTrustedDeclarations.map(entry => entry.symbol)
    ]
);

export const CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_MODULE = moduleSpec(
    'pathind-internalized-1d-library-prefix',
    derivedLibraryPrefixDeclarations.slice(1),
    [
        pathoutMotiveTransportObject,
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol),
        ...theoremTrustedDeclarations.map(entry => entry.symbol)
    ]
);

export const CORE_PATHIND_INTERNALIZED_1D_SOURCE_FIBRE_RUNTIME_MODULE =
moduleSpec(
    'pathind-internalized-1d-runtime-source-fibre-extension',
    [],
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol),
        ...theoremTrustedDeclarations.map(entry => entry.symbol),
        ...derivedLibraryPrefixDeclarations.map(entry => entry.symbol)
    ],
    sourceFibreExtensionRules
);

export const CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_MODULE = moduleSpec(
    'pathind-internalized-1d-library-suffix',
    derivedLibrarySuffixDeclarations,
    [
        ...commonExternalSymbols,
        ...sigmaTrustedDeclarations.map(entry => entry.symbol),
        ...preludeDeclarations.map(entry => entry.symbol),
        ...theoremTrustedDeclarations.map(entry => entry.symbol),
        ...derivedLibraryPrefixDeclarations.map(entry => entry.symbol)
    ]
);

const policyForDeclarations = (
    module: CoreLfModuleSpec,
    revision: string,
    declarations: readonly CoreLfTransferDeclaration[],
    policy: 'opaque-signature' | 'checked-transparent-definition'
): CoreLfTransferPolicyOverlay => createCoreLfTransferPolicyOverlay(
    module,
    {
        revision,
        moduleRevision: module.revision,
        entries: declarations.map(declaration => ({
            order: declaration.order,
            target: {
                kind: 'declaration' as const,
                symbol: declaration.symbol
            },
            policy,
            evidence:
                `Exact active v3.2 ${policy} selected by reviewed ` +
                'PATHOUT-LIBRARY-INTERNALIZED-1D proposal v14'
        }))
    }
);

export const CORE_PATHIND_INTERNALIZED_1D_SIGMA_POLICY =
    policyForDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_SIGMA_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-SIGMA-POLICY-1`,
        sigmaTrustedDeclarations,
        'opaque-signature'
    );

export const CORE_PATHIND_INTERNALIZED_1D_PRELUDE_POLICY =
    policyForDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_PRELUDE_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-PRELUDE-POLICY-1`,
        preludeDeclarations,
        'checked-transparent-definition'
    );

export const CORE_PATHIND_INTERNALIZED_1D_TRUSTED_POLICY =
    policyForDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_TRUSTED_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-TRUSTED-POLICY-1`,
        theoremTrustedDeclarations,
        'opaque-signature'
    );

const derivedSupportRuleIds = new Set([
    'pathind.internalized.' +
        'path-ind-functor-component-post-prefix-subject-fusion',
    'pathind.internalized.' +
        'path-ind-transfd-component-subject-fusion',
    'pathind.internalized.' +
        'motive-transport-functor-category-presentation-fusion',
    'pathind.internalized.' +
        'motive-transport-action-category-presentation-fusion',
    'pathind.internalized.' +
        'path-ind-source-fibre-at-sigma-pair-presentation-fusion',
    'pathind.internalized.' +
        'transported-motive-reflexive-fibre-presentation-fusion',
    'pathind.internalized.' +
        'pathout-pi-transport-post-delta-presentation-fusion',
    'pathind.internalized.' +
        'path-ind-target-fibre-at-sigma-pair-presentation-fusion'
]);

const policyForRuntimeRules = (
    module: CoreLfModuleSpec,
    revision: string,
    rules: readonly CoreLfTransferRuntimeRule[]
): CoreLfTransferPolicyOverlay => createCoreLfTransferPolicyOverlay(
    module,
    {
        revision,
        moduleRevision: module.revision,
        entries: rules.map(rule => ({
            order: rule.order,
            target: {
                kind: 'runtime-rule' as const,
                id: rule.id
            },
            policy: 'runtime-rewrite' as const,
            evidence:
                derivedSupportRuleIds.has(rule.id)
                    ? 'Derived type-presentation support ' +
                        'selected by reviewed ' +
                        'PATHOUT-LIBRARY-INTERNALIZED-1D proposal v14'
                    : 'Exact active v3.2 projection selected by reviewed ' +
                        'PATHOUT-LIBRARY-INTERNALIZED-1D proposal v14'
        }))
    }
);

export const CORE_PATHIND_INTERNALIZED_1D_BASE_RUNTIME_POLICY =
    policyForRuntimeRules(
        CORE_PATHIND_INTERNALIZED_1D_BASE_RUNTIME_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-BASE-RUNTIME-POLICY-1`,
        baseRuntimeRules
    );

export const CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE = createCoreLfModuleSpec({
    ...moduleSpec('pathind-internalized-1d-motive-proof', [], [
        ...commonExternalSymbols, ...sigmaTrustedDeclarations.map(d=>d.symbol),
        ...preludeDeclarations.map(d=>d.symbol), ...theoremTrustedDeclarations.map(d=>d.symbol),
        pathoutMotiveTransportObject
    ]),
    proofRules: [...CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE.proofRules,
        familyCompositionPullbackRule()]
});
export const CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_POLICY = createCoreLfTransferPolicyOverlay(
    CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE, {
        revision: `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-MOTIVE-PROOF-POLICY`,
        moduleRevision: CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE.revision,
        entries: CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE.proofRules.map((rule,order)=>({
            order,target:{kind:'proof-rule' as const,id:rule.id},policy:'proof-unification' as const,
            evidence:'Existing native proof-time comparison; operational terms unchanged'
        }))
    });

export const CORE_PATHIND_INTERNALIZED_1D_MOTIVE_POLICY = policyForDeclarations(
    CORE_PATHIND_INTERNALIZED_1D_MOTIVE_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-MOTIVE-POLICY`,
    derivedLibraryPrefixDeclarations.slice(0, 1), 'checked-transparent-definition');

export const CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_POLICY =
    policyForDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-PREFIX-LIBRARY-POLICY-1`,
        derivedLibraryPrefixDeclarations.slice(1),
        'checked-transparent-definition'
    );

export const CORE_PATHIND_INTERNALIZED_1D_SOURCE_FIBRE_RUNTIME_POLICY =
    policyForRuntimeRules(
        CORE_PATHIND_INTERNALIZED_1D_SOURCE_FIBRE_RUNTIME_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-` +
            'SOURCE-FIBRE-RUNTIME-POLICY-1',
        sourceFibreExtensionRules
    );

export const CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_POLICY =
    policyForDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_MODULE,
        `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-SUFFIX-LIBRARY-POLICY-1`,
        derivedLibrarySuffixDeclarations,
        'checked-transparent-definition'
    );

const providerLinks = [
    ...CORE_CATEGORICAL_COMPOSITIONAL_NATURAL_TRANSFER_LINKAGE.entries,
    ...CORE_PATHIND_FIXED_SOURCE_1C_FIBRE_TARGET_LINKAGE.entries,
    ...CORE_PATHIND_FIXED_SOURCE_1C_TRUSTED_LINKAGE.entries,
    ...CORE_PATHIND_FIXED_SOURCE_1C_LIBRARY_LINKAGE.entries,
    ...CORE_PATHOUT_FOUNDATION_1B_PREREQUISITE_LINKAGE.entries,
    ...CORE_PATHOUT_FOUNDATION_1B_LIBRARY_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_TRANSFD_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_DISPLAYED_CHAIN_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE.entries,
    ...CORE_CATEGORICAL_STRUCTURAL_TRANSFER_LINKAGE.entries,
    ...CORE_DIRECTED_CONTINUATION_TRANSFER_LINKAGE.entries
];

const symbolEquals = (
    left: CoreLfQualifiedSymbol,
    right: CoreLfQualifiedSymbol
): boolean =>
    left.moduleId === right.moduleId && left.name === right.name;

const dependencyLink = (
    candidates: readonly CoreLfTransferDeclarationLink[],
    target: CoreLfQualifiedSymbol,
    order: number,
    owner: string
): CoreLfTransferDeclarationLink => {
    const inherited = candidates.find(candidate =>
        symbolEquals(candidate.symbol, target)
    );
    if (inherited === undefined) {
        throw new Error(
            `${owner} has no dependency link for ` +
            `${target.moduleId}.${target.name}`
        );
    }
    return Object.freeze({
        ...inherited,
        order,
        symbol: Object.freeze({ ...target })
    });
};

const localLink = (
    declaration: CoreLfTransferDeclaration,
    order: number
): CoreLfTransferDeclarationLink => Object.freeze({
    order,
    symbol: declaration.symbol,
    kind: 'free-declaration' as const,
    coreName:
        `emdash_v3_2_pathind_internalized_${declaration.symbol.name}`,
    backendName: declaration.symbol.name
});

const createLinkage = (
    module: CoreLfModuleSpec,
    revision: string,
    externalCandidates: readonly CoreLfTransferDeclarationLink[],
    declarations: readonly CoreLfTransferDeclaration[]
): CoreLfTransferDeclarationLinkage => {
    const externalSymbols = module.externalSymbols.map(entry => entry.symbol);
    return createCoreLfTransferDeclarationLinkage(module, {
        revision,
        moduleRevision: module.revision,
        entries: [
            ...externalSymbols.map((target, order) => dependencyLink(
                externalCandidates,
                target,
                order,
                module.fragmentId
            )),
            ...declarations.map((declaration, index) => localLink(
                declaration,
                externalSymbols.length + index
            ))
        ]
    });
};

export const CORE_PATHIND_INTERNALIZED_1D_SIGMA_LINKAGE = createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_SIGMA_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-SIGMA-LINKAGE-1`,
    providerLinks,
    sigmaTrustedDeclarations
);

const sigmaLinks = [
    ...CORE_PATHIND_INTERNALIZED_1D_SIGMA_LINKAGE.entries,
    ...providerLinks
];

export const CORE_PATHIND_INTERNALIZED_1D_PRELUDE_LINKAGE = createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_PRELUDE_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-PRELUDE-LINKAGE-1`,
    sigmaLinks,
    preludeDeclarations
);

const preludeLinks = [
    ...CORE_PATHIND_INTERNALIZED_1D_PRELUDE_LINKAGE.entries,
    ...sigmaLinks
];

export const CORE_PATHIND_INTERNALIZED_1D_TRUSTED_LINKAGE = createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_TRUSTED_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-TRUSTED-LINKAGE-1`,
    preludeLinks,
    theoremTrustedDeclarations
);

const trustedLinks = [
    ...CORE_PATHIND_INTERNALIZED_1D_TRUSTED_LINKAGE.entries,
    ...preludeLinks
];

export const CORE_PATHIND_INTERNALIZED_1D_MOTIVE_LINKAGE =
createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_MOTIVE_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-MOTIVE-LINKAGE-1`,
    trustedLinks,
    derivedLibraryPrefixDeclarations.slice(0, 1)
);

export const CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_LINKAGE =
createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-PREFIX-LIBRARY-LINKAGE-1`,
    [...CORE_PATHIND_INTERNALIZED_1D_MOTIVE_LINKAGE.entries, ...trustedLinks],
    derivedLibraryPrefixDeclarations.slice(1)
);

const prefixLibraryLinks = [
    ...CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_LINKAGE.entries,
    ...trustedLinks
];

export const CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_LINKAGE =
createLinkage(
    CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_MODULE,
    `${CORE_PATHIND_INTERNALIZED_1D_REVISION}-SUFFIX-LIBRARY-LINKAGE-1`,
    prefixLibraryLinks,
    derivedLibrarySuffixDeclarations
);

export const CORE_PATHIND_INTERNALIZED_1D_CORE_NAMES = Object.freeze(
    Object.fromEntries([
        ...sigmaTrustedDeclarations,
        ...preludeDeclarations,
        ...theoremTrustedDeclarations,
        ...derivedLibraryDeclarations
    ].map(declaration => [
        declaration.symbol.name,
        `emdash_v3_2_pathind_internalized_${declaration.symbol.name}`
    ])) as Readonly<Record<string, string>>
);

export type CorePathindInternalizedOrdinaryLibraryCapability =
    | 'checked-transparent-definition'
    | 'opaque-signature'
    | 'runtime-rewrite'
    | 'proof-unification';

export class CorePathindInternalizedOrdinaryLibraryCapabilityError
    extends Error {
    constructor(
        public readonly capability:
            CorePathindInternalizedOrdinaryLibraryCapability
    ) {
        super(
            `Ordinary internalized PathInd library code cannot request ` +
            `'${capability}'`
        );
        this.name =
            'CorePathindInternalizedOrdinaryLibraryCapabilityError';
    }
}

export function assertCorePathindInternalizedOrdinaryLibraryCapability(
    capability: CorePathindInternalizedOrdinaryLibraryCapability
): 'checked-transparent-definition' {
    if (capability !== 'checked-transparent-definition') {
        throw new CorePathindInternalizedOrdinaryLibraryCapabilityError(
            capability
        );
    }
    return capability;
}

export const CORE_PATHIND_INTERNALIZED_1D_TRANSFER_BOUNDARY = Object.freeze({
    revision: CORE_PATHIND_INTERNALIZED_1D_REVISION,
    reviewedAuthorization: 'STRICT-FUNCTOR-DUALITY-FOUNDATIONS-V3.2',
    historicalReviewedAuthorization: 'PATHOUT-LIBRARY-INTERNALIZED-1D-REVIEWED-14',
    selectedPredecessor: CORE_PATHIND_FIXED_SOURCE_1C_REVISION,
    trustedDeclarationNames: Object.freeze([
        ...sigmaTrustedDeclarations,
        ...theoremTrustedDeclarations
    ].map(declaration => declaration.symbol.name)),
    runtimeRuleIds: Object.freeze(runtimeRules.map(rule => rule.id)),
    proofRuleIds: Object.freeze(CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE.proofRules.map(r=>r.id)),
    reusedWhiskeringSignatureCount: 2,
    transparentDefinitionNames: Object.freeze([
        ...preludeDeclarations,
        ...derivedLibraryDeclarations
    ].map(declaration => declaration.symbol.name)),
    trustedDeclarationCount:
        sigmaTrustedDeclarations.length + theoremTrustedDeclarations.length,
    runtimeRuleCount: runtimeRules.length,
    mathematicalRuntimeProjectionCount: 4,
    derivedRuntimeSupportRuleCount: 5,
    v2PrePrefixSubjectFusionRetained: false,
    postPrefixSubjectFusionSelected: true,
    transfdComponentSubjectFusionSelected: false,
    currentSupportFusionsFollowNativeComputation: true,
    nativeMovingComponentProjectionIncluded: true,
    activePiPullbackComponentProjectionSelected: true,
    piPullbackComponentInherited: true,
    piPullbackInferredFamilySlotsAreTypedWildcards: true,
    motiveTransportCategoryPresentationFusionSelected: false,
    motiveTransportUsesNativePullbackBody: true,
    motiveTransportActionCategoryPresentationFusionSelected: false,
    motiveTransportArrowUsesProofOnlyCompositionView: true,
    baseRuntimeRuleCount: baseRuntimeRules.length,
    prefixTransparentDefinitionCount:
        derivedLibraryPrefixDeclarations.length,
    sourceFibreExtensionRuntimeRuleCount:
        sourceFibreExtensionRules.length,
    suffixTransparentDefinitionCount:
        derivedLibrarySuffixDeclarations.length,
    pathInductionSourceFibreStagedParentFusionSelected: true,
    transportedMotiveReflexiveFibreFusionSelected: true,
    targetFibreFusionUsesActivePullbackAndPathoutAction: true,
    pathoutPiTransportPostDeltaPresentationFusionSelected: true,
    pathoutPiTransportFusionClosesCompleteFunctorParent: true,
    pathoutPiTransportFusionUsesStablePostDeltaType: true,
    v12PreDeltaFusionRetained: false,
    underlyingSectionCategoryRuntimeEqualityIncluded: false,
    pathInductionTargetFibreStagedParentFusionSelected: true,
    targetFibreFusionCoversBothAliasEndpoints: true,
    genericSigmaFibreRuntimeRuleIncluded: false,
    sourceFibreFusionCompiledAfterPrefix: true,
    sourceFibreFusionUsesOnlyEarlierDeclaredSymbolsAtItsStage: true,
    v8PrePrefixPathIndSrcGlobalRuleRejected: true,
    v9PostSigmaProjectionRuleRejectedByTrace: true,
    declarationOrderPreservedAcrossStages: true,
    historicalSemanticCountDeltaFromV13: 1,
    genericComparisonNormalFormClosureRequired: true,
    genericCategoryCollapseIncluded: false,
    proofRuleCount: 2,
    transparentDefinitionCount:
        preludeDeclarations.length + derivedLibraryDeclarations.length,
    typedLibraryConsumerCount: 2,
    negativeConsumerCount: 10,
    selectedRuntimeObservationCount: 10,
    boundedOracleAssertionCount: 38,
    allEntriesUseGenericTransferEngines: true,
    ordinarySafeLibraryCanAddTransparentDefinitions: true,
    ordinarySafeLibraryCanAddOpaqueOwners: false,
    ordinarySafeLibraryCanAddRuntimeRules: false,
    ordinarySafeLibraryCanAddProofRules: false,
    rootOnlyQualification: true,
    browserOrPublicPackageExported: false,
    primaryTheorem: 'PathInd_transfd',
    sigmaTotalPresentation: 'PathInd_funcd',
    sourceArrowRemainsInternallyOwned: true,
    higherActionRemainsInternallyOwned: true,
    wholeScaleStress2b3Imported: false,
    arbitraryNonCartesianSigmaNaturalityIncluded: false,
    transitivityDefinitionsIncluded: false,
    pathCategoryProofBridgeIncluded: false,
    intrinsicCoreOwnerDelta: 0,
    checkerBranchDelta: 0,
    evaluatorBranchDelta: 0,
    activeLambdapiOwnerDelta: 0,
    activeLambdapiRuleDelta: 0
});

export interface CorePathindInternalized1dCompilation {
    readonly predecessor: CorePathindFixedSource1cCompilation;
    readonly whiskering: ReturnType<typeof compileCoreCategoricalCompositionalNaturalAt<CorePathindFixedSource1cCompilation>>;
    readonly whiskeringCompiled: CoreLfCompiledDeclarationModule;
    readonly sigmaCompiled: CoreLfCompiledDeclarationModule;
    readonly preludeCompiled: CoreLfCompiledDeclarationModule;
    readonly trustedCompiled: CoreLfCompiledDeclarationModule;
    readonly baseRuntimeFragment: CoreLfCompiledRuntimeFragment;
    readonly motiveCompiled: CoreLfCompiledDeclarationModule;
    readonly motiveProof: ReturnType<typeof compileCoreLfProofProgram>;
    readonly prefixLibraryCompiled: CoreLfCompiledDeclarationModule;
    readonly sourceFibreRuntimeFragment: CoreLfCompiledRuntimeFragment;
    readonly suffixLibraryCompiled: CoreLfCompiledDeclarationModule;
    readonly libraryCompiled: CoreLfCompiledDeclarationModule;
    readonly compiled: CoreLfCompiledDeclarationModule;
    readonly declarationContext: CoreLfMixedDeclarationContext;
    readonly runtimeFragment: CoreLfCompiledRuntimeFragment;
    readonly runtime: CoreLfCompiledRuntimeProgram;
    readonly composedRuntime: CoreLfComposedRuntimeProgram;
}

let cachedCompilation: CorePathindInternalized1dCompilation | undefined;

export function compileCorePathindInternalized1dTransfer():
CorePathindInternalized1dCompilation {
    if (cachedCompilation !== undefined) return cachedCompilation;
    validateCorePathindInternalized1dReviewV14();
    const predecessor = compileCorePathindFixedSource1cTransfer();
    const whiskering = compileCoreCategoricalCompositionalNaturalAt(predecessor);
    const whiskeringCompiled = whiskering.compiled;
    const sigmaCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_SIGMA_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_SIGMA_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_SIGMA_LINKAGE,
        {
            initialEnvironment: whiskeringCompiled.environment,
            runtimeProgram: whiskering.composedRuntime,
            comparisonStepLimit: 512
        }
    );
    const preludeCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_PRELUDE_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_PRELUDE_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_PRELUDE_LINKAGE,
        {
            initialEnvironment: sigmaCompiled.environment,
            runtimeProgram: whiskering.composedRuntime,
            comparisonStepLimit: 512
        }
    );
    const trustedCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_TRUSTED_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_TRUSTED_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_TRUSTED_LINKAGE,
        {
            initialEnvironment: preludeCompiled.environment,
            runtimeProgram: whiskering.composedRuntime,
            comparisonStepLimit: 512
        }
    );
    const trustedContext = new CoreLfMixedDeclarationContext(
        whiskering.declarationContext,
        [sigmaCompiled, preludeCompiled, trustedCompiled]
    );
    const subjectProof = compileCoreLfProofProgram(
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,
        CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY,
        trustedContext,
        // The whole component expands both restricted endpoint functors.
        // Its recorded 512-step trace ends in ordinary beta reduction.
        { runtimeProgram: whiskering.composedRuntime, comparisonStepLimit: 2048 }
    );
    const baseRuntimeFragment = compileCoreLfRuntimeFragment(
        CORE_PATHIND_INTERNALIZED_1D_BASE_RUNTIME_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_BASE_RUNTIME_POLICY,
        trustedContext,
        {
            dependencies: [{
                relation: 'earlier-fragment',
                fragment: whiskering.runtimeFragment
            }],
            comparisonStepLimit: 512,
            subjectReductionProof: {
                program: subjectProof,
                rules: [{
                    runtimeRuleId: 'pathind.internalized.pathout-refl-eval-component',
                    proofRuleIds: ['categorical.dependent-target.category-presentation'],
                    allowArgumentConversion: true
                }, {
                    runtimeRuleId: 'pathind.internalized.path-ind-transfd-component',
                    proofRuleIds: ['categorical.dependent-target.category-presentation'],
                    allowArgumentConversion: true
                }]
            }
        }
    );
    const motiveCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_MOTIVE_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_MOTIVE_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_MOTIVE_LINKAGE,
        { initialEnvironment: trustedCompiled.environment,
          runtimeProgram: baseRuntimeFragment.runtime, comparisonStepLimit: 512 }
    );
    const motiveContext = new CoreLfMixedDeclarationContext(trustedContext, [motiveCompiled]);
    const motiveProof = compileCoreLfProofProgram(
        CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_MOTIVE_PROOF_POLICY,
        motiveContext,
        { runtimeProgram: baseRuntimeFragment.runtime, comparisonStepLimit: 2048 }
    );
    const prefixLibraryCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_PREFIX_LIBRARY_LINKAGE,
        {
            initialEnvironment: motiveCompiled.environment,
            runtimeProgram: baseRuntimeFragment.runtime,
            comparisonStepLimit: 512,
            definitionTypeProof: { program: motiveProof, declarations: [{
                symbol: pathoutMotiveTransportArrow,
                proofRuleIds: ['categorical.reindex.composition-presentation']
            }] }
        }
    );
    const prefixContext = new CoreLfMixedDeclarationContext(
        whiskering.declarationContext,
        [
            sigmaCompiled,
            preludeCompiled,
            trustedCompiled,
            motiveCompiled,
            prefixLibraryCompiled
        ]
    );
    const sourceFibreRuntimeFragment = compileCoreLfRuntimeFragment(
        CORE_PATHIND_INTERNALIZED_1D_SOURCE_FIBRE_RUNTIME_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_SOURCE_FIBRE_RUNTIME_POLICY,
        prefixContext,
        {
            dependencies: [{
                relation: 'earlier-fragment',
                fragment: baseRuntimeFragment
            }],
            comparisonStepLimit: 512
        }
    );
    const suffixLibraryCompiled = compileCoreLfDeclarations(
        CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_MODULE,
        CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_POLICY,
        CORE_PATHIND_INTERNALIZED_1D_SUFFIX_LIBRARY_LINKAGE,
        {
            initialEnvironment: prefixLibraryCompiled.environment,
            runtimeProgram: sourceFibreRuntimeFragment.runtime,
            comparisonStepLimit: 512
        }
    );
    const declarationContext = new CoreLfMixedDeclarationContext(
        whiskering.declarationContext,
        [
            sigmaCompiled,
            preludeCompiled,
            trustedCompiled,
            motiveCompiled,
            prefixLibraryCompiled,
            suffixLibraryCompiled
        ]
    );
    cachedCompilation = Object.freeze({
        predecessor,
        whiskering,
        whiskeringCompiled,
        sigmaCompiled,
        preludeCompiled,
        trustedCompiled,
        baseRuntimeFragment,
        motiveCompiled,
        motiveProof,
        prefixLibraryCompiled,
        sourceFibreRuntimeFragment,
        suffixLibraryCompiled,
        libraryCompiled: suffixLibraryCompiled,
        compiled: suffixLibraryCompiled,
        declarationContext,
        runtimeFragment: sourceFibreRuntimeFragment,
        runtime: sourceFibreRuntimeFragment.localProgram,
        composedRuntime: sourceFibreRuntimeFragment.runtime
    });
    return cachedCompilation;
}
