/**
 * Non-authorizing PATHOUT-TRUSTED-LIBRARY-GRADUATE-0G proposal.
 *
 * This record classifies the historical root-only profile at85b560e. It is
 * not current migration or release qualification. It installs no
 * declaration, rule, parser, export, package entry, or release effect.
 */

import {
    CORE_PATHOUT_PRESENTATION_1F_MANIFEST
} from './pathout_presentation';
import {
    CORE_PATHOUT_PRESENTATION_1F_CLI_PROFILE
} from './pathout_presentation_cli';
import {
    CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT,
    validateCorePathoutTrustBoundary0aAudit
} from './pathout_trust_boundary_audit';

export const CORE_PATHOUT_LIBRARY_GRADUATION_0G_PROPOSAL_REVISION =
    'PATHOUT-TRUSTED-LIBRARY-GRADUATE-0G-PROPOSAL-1' as const;

const deepFreeze = <T>(value: T): T => {
    if (value !== null && typeof value === 'object') {
        Reflect.ownKeys(value as object).forEach(key =>
            deepFreeze((value as Record<PropertyKey, unknown>)[key])
        );
        if (!Object.isFrozen(value)) Object.freeze(value);
    }
    return value;
};

const mathematicalOpaqueOwners = Object.freeze(
    CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.selectedOwners
        .filter(entry => entry.sourceOpacity === 'opaque')
        .map(entry => entry.name)
);

// These are the exact historical values approved at85b560e. The proposal
// source at that checkpoint and the unchanged main baseline has SHA-256
// fc35b53dd151694069974b4df6ad3c04ee55cd5d8bacad34f9f21c47c8cee572.
// Current migration qualification belongs to the living foundations plan;
// live transfer changes must not silently rewrite this old approval record.
const sealedSupportingOwners = Object.freeze([
    "hom_int_precomp_tele_func",
    "hom_int_precomp_func",
    "Sigma_func",
    "hom_postcomp_func",
    "hom_precomp_along_func",
    "fib_cov_int",
    "fib_cov_src_func",
    "fib_cov_transf",
    "Sigma_transfd_funcd"
]);

const transparentDefinitions = Object.freeze([
    "Rep_catd_func",
    "Rep_catd",
    "Rep_transport_func",
    "PathOut_cat",
    "PathOut_cat_func",
    "PathOut_transport_func",
    "pathout_obj",
    "pathout_refl_obj",
    "pathout_refl_arrow",
    "FibCov_target_catd",
    "pathout_refl_eval_func",
    "pathout_refl_eval_base_func",
    "pathout_refl_arrow_sec",
    "PathInd_src_catd",
    "PathInd_tgt_catd",
    "PathOutMotives_catd",
    "PathOutPi_funcd",
    "PathIndTgt_catd",
    "pathout_motive_transport_obj",
    "pathout_motive_transport_arrow",
    "PathIndSrc_catd",
    "PathIndSrc_transport_func",
    "PathInd_funcd",
    "pathout_pi_transport_func",
    "PathIndTgt_transport_func",
    "CompTarget_catd",
    "CompTarget_fapp1_func",
    "CompMotive_catd",
    "path_comp_sec",
    "path_comp_func"
]);

const runtimeRuleIds = Object.freeze([
    "pathout.foundation.represented-hom-capped-action",
    "pathout.foundation.postcomposition-object-action",
    "pathout.foundation.represented-hom-object-action-fusion",
    "pathout.foundation.postcomposition-identity-source-unit",
    "pathout.foundation.precomposition-object-action",
    "pathout.foundation.precomposition-identity-incoming",
    "pathout.foundation.hom-int-precomp-component",
    "pathout.foundation.hom-int-precomp-component-object-fusion",
    "pathout.foundation.hom-int-precomp-full-action",
    "pathout.foundation.hom-int-precomp-capped-action",
    "pathout.foundation.hom-int-precomp-tele-application",
    "pathout.foundation.sigma-func-object",
    "pathout.foundation.sigma-func-capped-action",
    "pathind.fixed-source.contravariant-representable-object",
    "pathind.fixed-source.displayed-functor-object",
    "pathind.fixed-source.displayed-hom-object-fusion",
    "pathind.fixed-source.transfor-classifier-delta",
    "pathind.fixed-source.fib-cov-target-section-fusion",
    "pathind.fixed-source.fixed-evaluation-post-delta-presentation-fusion",
    "pathind.fixed-source.fib-cov-package-component",
    "pathind.fixed-source.fib-cov-component-object",
    "pathind.fixed-source.fib-cov-section-point",
    "pathind.fixed-source.path-ind-section-object-action",
    "pathind.fixed-source.path-ind-point-computation",
    "pathind.fixed-source.path-ind-sigma-pullback-computation",
    "pathind.internalized.sigma-transfd-object-component",
    "pathind.internalized.pathout-refl-eval-component",
    "pathind.internalized.path-ind-functor-component-post-prefix-subject-fusion",
    "pathind.internalized.path-ind-functor-component",
    "pathind.internalized.path-ind-transfd-component-subject-fusion",
    "pathind.internalized.pi-pullback-component",
    "pathind.internalized.path-ind-transfd-component",
    "pathind.internalized.motive-transport-functor-category-presentation-fusion",
    "pathind.internalized.motive-transport-action-category-presentation-fusion",
    "pathind.internalized.path-ind-source-fibre-at-sigma-pair-presentation-fusion",
    "pathind.internalized.transported-motive-reflexive-fibre-presentation-fusion",
    "pathind.internalized.pathout-pi-transport-post-delta-presentation-fusion",
    "pathind.internalized.path-ind-target-fibre-at-sigma-pair-presentation-fusion",
    "pathout.transitivity.fixed-source-selected-component-consumer-parent-fusion"
]);

const proofRuleIds = Object.freeze([
    "pathout.foundation.precomposition-identity-family",
    "pathout.foundation.hom-int-precomp-projection-order"
]);

const rawProposal = {
    revision: CORE_PATHOUT_LIBRARY_GRADUATION_0G_PROPOSAL_REVISION,
    row: 'PATHOUT-TRUSTED-LIBRARY-GRADUATE-0G',
    status: 'ready-for-separate-review',
    recommendation:
        'graduate-qualified-root-only-trusted-and-derived-profile',
    parent: {
        trustAuditRevision: CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.revision,
        trustAuditCheckpoint: 'a05493b',
        activeSourceSha256:
            CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.authority.source.sha256,
        activeChecksSha256:
            CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.authority.checks.sha256,
        foundationSemanticCheckpoint: '550316a',
        foundationLedgerCheckpoint: '349b6d4',
        fixedSourceSemanticCheckpoint: 'a361dc3',
        fixedSourceLedgerCheckpoint: '033dbb8',
        genericClosureCheckpoint: 'e560551',
        internalizedSemanticCheckpoint: 'b6005b3',
        internalizedLedgerCheckpoint: '6225075',
        transitivitySemanticCheckpoint: '3b113ad',
        transitivityLedgerCheckpoint: '10432ba',
        presentationProposalCheckpoint: '6ad0812',
        presentationReviewCheckpoint: 'f03ef01',
        presentationSemanticCheckpoint: '8d226cc',
        presentationLedgerCheckpoint: 'be487c9'
    },
    productProfile: {
        id: 'emdash-v3.2-pathout-pathind-root-1',
        qualification: 'root-only-source-qualified',
        mathematicalAuthority: 'active-emdash-v3.2-lambdapi-source',
        productionBackend: 'typescript-emdash',
        lambdapiRole: 'bounded-conformance-oracle',
        genericKernel:
            'existing-backend-neutral-explicit-core-checker-and-rule-engines',
        intrinsicCoreOwnerDelta: 0,
        checkerBranchDelta: 0,
        evaluatorBranchDelta: 0,
        activeLambdapiOwnerDelta: 0,
        activeLambdapiRuleDelta: 0
    },
    sealedTrustedProfile: {
        policy:
            'provenance-pinned-opaque-owners-and-exact-rules-only',
        mathematicalOpaqueOwners,
        sealedSupportingOwners,
        mathematicalOpaqueOwnerCount: mathematicalOpaqueOwners.length,
        sealedSupportingOwnerCount: sealedSupportingOwners.length,
        totalLocalSealedDeclarationCount:
            mathematicalOpaqueOwners.length + sealedSupportingOwners.length,
        runtimeRuleIds,
        proofRuleIds,
        runtimeRuleCount: runtimeRuleIds.length,
        proofRuleCount: proofRuleIds.length,
        ordinaryUsersMayAddOpaqueOwners: false,
        ordinaryUsersMayAddRuntimeRules: false,
        ordinaryUsersMayAddProofRules: false
    },
    transparentDerivedLibrary: {
        policy: 'checked-transparent-definitions-and-proof-terms',
        definitionNames: transparentDefinitions,
        definitionCount: transparentDefinitions.length,
        ordinaryUsersMayAddCheckedTransparentDefinitions: true,
        includes: [
            'represented fixed-source outgoing-arrow category',
            'canonical arrow from the reflexive outgoing arrow',
            'fixed-source arrow-induction section',
            'functorial motive and source-varying induction packaging',
            'composition recovered from arrow induction'
        ]
    },
    localSliceBoundaries: [
        {
            id: 'PATHOUT-LIBRARY-FOUNDATION-1B',
            exact: '5/13/2/9',
            sealedDeclarations: 5,
            runtimeRules: 13,
            proofRules: 2,
            transparentDefinitions: 9
        },
        {
            id: 'PATHIND-TRUSTED-PROFILE-1C',
            exact: '5/12/0/6',
            sealedDeclarations: 5,
            runtimeRules: 12,
            proofRules: 0,
            transparentDefinitions: 6
        },
        {
            id: 'PATHOUT-LIBRARY-INTERNALIZED-1D',
            exact: '4/13/0/10',
            sealedDeclarations: 4,
            runtimeRules: 13,
            proofRules: 0,
            transparentDefinitions: 10
        },
        {
            id: 'PATHOUT-LIBRARY-TRANSITIVITY-1E',
            exact: '0/1/0/5',
            sealedDeclarations: 0,
            runtimeRules: 1,
            proofRules: 0,
            transparentDefinitions: 5
        }
    ],
    computationEnvelope: {
        fixedSourcePointAndArrowComputation: true,
        internallyVaryingSourceAction: true,
        selectedHigherAction: true,
        compositionNormalForm: true,
        compositionNormalFormTarget: 'stable-representable-precomposition',
        pathCategoryComparisonLibraryIncluded: false,
        pathCategoryReflexiveJoinRuleIncluded: false,
        arbitraryExternalNaturalityIncluded: false,
        wholeTheoryNormalizationClaimed: false,
        confluenceClaimed: false,
        canonicityClaimed: false,
        consistencyClaimed: false
    },
    presentation: {
        manifestRevision: CORE_PATHOUT_PRESENTATION_1F_MANIFEST.revision,
        cliRevision: CORE_PATHOUT_PRESENTATION_1F_CLI_PROFILE.revision,
        formIds: CORE_PATHOUT_PRESENTATION_1F_MANIFEST.forms.map(
            form => form.id
        ),
        formCount: CORE_PATHOUT_PRESENTATION_1F_MANIFEST.forms.length,
        browserEvidence:
            'qualified-at-pinned-checkpoint-not-rerun-in-browser',
        nodeEvidence: 'explicit-fresh-TypeScript-semantic-check',
        browserLoadsSemanticTransfer: false,
        declarationOrBinderParserIncluded: false
    },
    distribution: {
        contributorSourceQualified: true,
        contributorBarrelExported: false,
        npmBarrelExported: false,
        npmVersionChanged: false,
        releaseOrRegistryEffect: false,
        browserUsesDirectLazyRootSource: true,
        publicExportNeedsConcreteConsumerAndSeparateReleaseDecision: true
    },
    decision: {
        proposalIsSelfAuthorizing: false,
        separateImmutableReviewRequired: true,
        implementationChangeRequiredForGraduation: false,
        recommendedAfterApproval:
            'complete-STDLIB-8B-and-audit-next-concrete-consumer'
    },
    doesNotAuthorize: [
        'new Core node or checker/evaluator branch',
        'new declaration, runtime rule, proof rule, or equation',
        'ordinary-user opaque declarations or rule installation',
        'general inductive, HIT, or categorical-HIT declarations',
        'general declaration or binder text parsing',
        'whole-library transfer graduation',
        'path-category comparison bridge',
        'metatheoretic normalization, confluence, canonicity, or consistency',
        'public or npm barrel export',
        'package version, publication, release, push, merge, or deployment',
        'active Lambdapi source edit',
        'sibling-repository mutation or worktree cleanup'
    ]
} as const;

export type CorePathoutLibraryGraduation0gProposal = typeof rawProposal;

export type CorePathoutLibraryGraduation0gProposalErrorCode =
    | 'PATHOUT_GRADUATION_PREREQUISITE_DRIFT'
    | 'PATHOUT_GRADUATION_CLASSIFICATION_DRIFT'
    | 'PATHOUT_GRADUATION_PROPOSAL_DRIFT';

export class CorePathoutLibraryGraduation0gProposalError extends Error {
    constructor(
        public readonly code:
            CorePathoutLibraryGraduation0gProposalErrorCode,
        message: string
    ) {
        super(message);
        this.name = 'CorePathoutLibraryGraduation0gProposalError';
    }
}

export const CORE_PATHOUT_LIBRARY_GRADUATION_0G_PROPOSAL =
    deepFreeze(rawProposal);

export function cloneCorePathoutLibraryGraduation0gProposal():
CorePathoutLibraryGraduation0gProposal {
    return JSON.parse(JSON.stringify(rawProposal)) as
        CorePathoutLibraryGraduation0gProposal;
}

const sameData = (left: unknown, right: unknown): boolean =>
    JSON.stringify(left) === JSON.stringify(right);

export function validateCorePathoutLibraryGraduation0gProposal(
    proposal: CorePathoutLibraryGraduation0gProposal =
        CORE_PATHOUT_LIBRARY_GRADUATION_0G_PROPOSAL
): CorePathoutLibraryGraduation0gProposal {
    validateCorePathoutTrustBoundary0aAudit();
    const boundaries = proposal.localSliceBoundaries;
    if (
        proposal.parent.presentationSemanticCheckpoint !== '8d226cc' ||
        proposal.parent.presentationLedgerCheckpoint !== 'be487c9' ||
        proposal.parent.activeSourceSha256 !==
            CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.authority.source.sha256 ||
        proposal.parent.activeChecksSha256 !==
            CORE_PATHOUT_TRUST_BOUNDARY_0A_AUDIT.authority.checks.sha256 ||
        boundaries.length !== 4 ||
        !sameData(boundaries.map(boundary => boundary.exact), [
            '5/13/2/9',
            '5/12/0/6',
            '4/13/0/10',
            '0/1/0/5'
        ]) ||
        proposal.presentation.manifestRevision !==
            CORE_PATHOUT_PRESENTATION_1F_MANIFEST.revision ||
        proposal.presentation.cliRevision !==
            CORE_PATHOUT_PRESENTATION_1F_CLI_PROFILE.revision
    ) {
        throw new CorePathoutLibraryGraduation0gProposalError(
            'PATHOUT_GRADUATION_PREREQUISITE_DRIFT',
            'PathOut graduation prerequisites drifted'
        );
    }
    if (
        proposal.sealedTrustedProfile.mathematicalOpaqueOwnerCount !== 5 ||
        proposal.sealedTrustedProfile.sealedSupportingOwnerCount !== 9 ||
        proposal.sealedTrustedProfile.totalLocalSealedDeclarationCount !==
            14 ||
        proposal.sealedTrustedProfile.runtimeRuleCount !== 39 ||
        proposal.sealedTrustedProfile.proofRuleCount !== 2 ||
        proposal.transparentDerivedLibrary.definitionCount !== 30 ||
        new Set(proposal.sealedTrustedProfile.runtimeRuleIds).size !== 39 ||
        new Set(proposal.transparentDerivedLibrary.definitionNames).size !==
            30 ||
        proposal.distribution.contributorBarrelExported ||
        proposal.distribution.npmBarrelExported
    ) {
        throw new CorePathoutLibraryGraduation0gProposalError(
            'PATHOUT_GRADUATION_CLASSIFICATION_DRIFT',
            'PathOut graduation trust/library classification drifted'
        );
    }
    if (!sameData(proposal, rawProposal)) {
        throw new CorePathoutLibraryGraduation0gProposalError(
            'PATHOUT_GRADUATION_PROPOSAL_DRIFT',
            'PathOut graduation proposal drifted'
        );
    }
    return deepFreeze(proposal);
}
