/**
 * Reviewed DIRECTED-FOUNDATION-1 runtime integration.
 *
 * These selected native coefficient and object-level reductions are executable only
 * through a directed catalog. They do not rewrite the stable category heads
 * themselves and are not imported by the default LF or browser paths.
 */

import {
    CORE_DIRECTED_1A_PRIMITIVE_NAMES
} from './directed_1a';
import {
    CORE_DIRECTED_FOUNDATION_PROPOSAL,
    CoreDirectedFoundationRuleId
} from './directed_foundation_proposal';
import {
    CORE_DIRECTED_FOUNDATION_REVIEW,
    validateCoreDirectedFoundationReview
} from './directed_foundation_review';
import {
    CoreRuntimeHeadRewriteResult,
    CoreRuntimeMatch
} from './evaluator';
import {
    CoreLfCatalogRuntime
} from './lf_conversion';
import {
    KernelExpression,
    Provenance,
    kernelApplication,
    kernelFree,
    provenance
} from './kernel';
import {
    CORE_OWNER_SCHEMAS,
    CoreOwnerId,
    Plicity
} from './schema';

export interface CoreDirectedFoundationRuntimeRule {
    readonly order: number;
    readonly id: CoreDirectedFoundationRuleId;
}

const frozenRules: readonly CoreDirectedFoundationRuntimeRule[] =
    Object.freeze(
        CORE_DIRECTED_FOUNDATION_PROPOSAL.runtimeRules.map(rule =>
            Object.freeze({
                order: rule.order,
                id: rule.id
            })
        )
    );

const matchOwnerApplication = (
    expression: KernelExpression,
    owner: CoreOwnerId
): readonly KernelExpression[] | undefined => {
    if (
        expression.tag !== 'application' ||
        expression.owner !== owner ||
        expression.arguments.length !==
            CORE_OWNER_SCHEMAS[owner].slots.length
    ) {
        return undefined;
    }
    for (let index = 0; index < expression.arguments.length; index++) {
        if (
            expression.arguments[index].plicity !==
            CORE_OWNER_SCHEMAS[owner].slots[index].plicity
        ) {
            return undefined;
        }
    }
    return expression.arguments.map(argument => argument.value);
};

const matchCandidateCall = (
    expression: KernelExpression,
    coreName: string,
    plicities: readonly Plicity[]
): readonly KernelExpression[] | undefined => {
    if (
        expression.tag !== 'call' ||
        expression.callee.tag !== 'reference' ||
        expression.callee.name !== coreName ||
        expression.arguments.length !== plicities.length
    ) {
        return undefined;
    }
    for (let index = 0; index < plicities.length; index++) {
        if (expression.arguments[index].plicity !== plicities[index]) {
            return undefined;
        }
    }
    return expression.arguments.map(argument => argument.value);
};

const decodedObjectCategory = (
    expression: KernelExpression
): KernelExpression | undefined => {
    const decode = matchOwnerApplication(expression, 'decode');
    if (!decode) return undefined;
    const object = matchOwnerApplication(
        decode[0],
        'object-classifier'
    );
    return object?.[0];
};

const emptyOwner = (
    expression: KernelExpression,
    owner: CoreOwnerId
): boolean => matchOwnerApplication(expression, owner)?.length === 0;

const rewrittenProvenance = (
    ruleId: CoreDirectedFoundationRuleId,
    redex: KernelExpression
): Provenance => provenance(
    'derived',
    `DIRECTED-FOUNDATION-1 runtime rewrite ${ruleId}`,
    redex.provenance.span
);

const owner = (
    ownerId: CoreOwnerId,
    arguments_: readonly KernelExpression[],
    nodeProvenance: Provenance
): KernelExpression => kernelApplication(
    ownerId,
    arguments_.map(value => ({ value })),
    nodeProvenance
);

const matchResult = (
    ruleId: CoreDirectedFoundationRuleId,
    bindings: readonly KernelExpression[]
): CoreRuntimeMatch => Object.freeze({
    ruleId,
    bindings: Object.freeze([...bindings])
});

const rewriteCategoryObject = (
    expression: KernelExpression
): CoreRuntimeHeadRewriteResult | undefined => {
    const category = decodedObjectCategory(expression);
    if (
        category === undefined ||
        !emptyOwner(category, 'category-of-categories')
    ) {
        return undefined;
    }
    const ruleId = 'directed.category-object.decode' as const;
    const nodeProvenance = rewrittenProvenance(ruleId, expression);
    return Object.freeze({
        status: 'rewritten',
        ruleId,
        ruleIndex: 0,
        before: expression,
        after: owner('category-universe', [], nodeProvenance),
        match: matchResult(ruleId, [])
    });
};

const cartesianCoefficient = (source: Provenance): KernelExpression =>
    kernelFree(
        CORE_DIRECTED_1A_PRIMITIVE_NAMES['cartesian-category-coefficient'],
        source
    );

const isCartesianCoefficient = (value: KernelExpression): boolean =>
    (value.tag === 'reference' && value.name ===
        CORE_DIRECTED_1A_PRIMITIVE_NAMES['cartesian-category-coefficient']) ||
    matchCandidateCall(value,
        CORE_DIRECTED_1A_PRIMITIVE_NAMES['cartesian-category-coefficient'],
        [])?.length === 0;

// Retained catalog mirror of the two native coefficient projections. The
// production transfer compiler still compiles their ordinary rule data.
const rewriteCartesianCoefficient = (
    expression: KernelExpression
): CoreRuntimeHeadRewriteResult | undefined => {
    const category = decodedObjectCategory(expression);
    const decoded = matchOwnerApplication(expression, 'decode');
    const hom = decoded === undefined ? undefined :
        matchOwnerApplication(decoded[0], 'hom-classifier');
    const isObject = category !== undefined && isCartesianCoefficient(category);
    if (!isObject && (hom === undefined || !isCartesianCoefficient(hom[0]))) {
        return undefined;
    }
    const ruleId = isObject
        ? 'directed.cartesian-category-object.decode' as const
        : 'directed.cartesian-category-hom.decode' as const;
    const source = rewrittenProvenance(ruleId, expression);
    const endpoints = isObject ? [] : [hom![1], hom![2]];
    return Object.freeze({
        status: 'rewritten', ruleId, ruleIndex: isObject ? 1 : 2,
        before: expression,
        after: owner('decode', [isObject
            ? owner('object-classifier', [
                owner('category-of-categories', [], source)
            ], source)
            : owner('functor-classifier', endpoints, source)
        ], source),
        match: matchResult(ruleId, endpoints)
    });
};

const rewriteDisplayedFamily = (
    expression: KernelExpression
): CoreRuntimeHeadRewriteResult | undefined => {
    const category = decodedObjectCategory(expression);
    if (category === undefined) return undefined;
    const displayed = matchOwnerApplication(
        category,
        'displayed-category-category'
    );
    if (!displayed) return undefined;

    const ruleId = 'directed.displayed-family.decode' as const;
    const nodeProvenance = rewrittenProvenance(ruleId, expression);
    const categoryOfCategories = cartesianCoefficient(nodeProvenance);
    return Object.freeze({
        status: 'rewritten',
        ruleId,
        ruleIndex: 3,
        before: expression,
        after: owner('decode', [
            owner('functor-classifier', [
                displayed[0],
                categoryOfCategories
            ], nodeProvenance)
        ], nodeProvenance),
        match: matchResult(ruleId, [displayed[0]])
    });
};

const rewriteDisplayedFunctor = (
    expression: KernelExpression
): CoreRuntimeHeadRewriteResult | undefined => {
    const category = decodedObjectCategory(expression);
    if (category === undefined) return undefined;
    const displayedFunctor = matchCandidateCall(
        category,
        CORE_DIRECTED_1A_PRIMITIVE_NAMES[
            'displayed-functor-category'
        ],
        ['implicit', 'explicit', 'explicit']
    );
    if (!displayedFunctor) return undefined;

    const [base, sourceFamily, targetFamily] = displayedFunctor;
    const ruleId = 'directed.displayed-functor.decode' as const;
    const nodeProvenance = rewrittenProvenance(ruleId, expression);
    const categoryOfCategories = cartesianCoefficient(nodeProvenance);
    return Object.freeze({
        status: 'rewritten',
        ruleId,
        ruleIndex: 4,
        before: expression,
        after: owner('decode', [
            owner('transfor-classifier', [
                base,
                categoryOfCategories,
                sourceFamily,
                targetFamily
            ], nodeProvenance)
        ], nodeProvenance),
        match: matchResult(
            ruleId,
            [base, sourceFamily, targetFamily]
        )
    });
};

/**
 * Closed exact runtime program for the selected native prerequisites.
 */
export class CoreDirectedFoundationRuntimeProgram
implements CoreLfCatalogRuntime {
    readonly revision = 'DIRECTED-FOUNDATION-1-REVIEWED';
    readonly rules = frozenRules;
    readonly ruleIds: readonly CoreDirectedFoundationRuleId[];

    private constructor() {
        this.ruleIds = Object.freeze(this.rules.map(rule => rule.id));
        Object.freeze(this);
    }

    static create(): CoreDirectedFoundationRuntimeProgram {
        validateCoreDirectedFoundationReview(
            CORE_DIRECTED_FOUNDATION_REVIEW
        );
        return new CoreDirectedFoundationRuntimeProgram();
    }

    rewriteHead(
        expression: KernelExpression
    ): CoreRuntimeHeadRewriteResult {
        const result =
            rewriteCategoryObject(expression) ??
            rewriteCartesianCoefficient(expression) ??
            rewriteDisplayedFamily(expression) ??
            rewriteDisplayedFunctor(expression);
        return result ?? Object.freeze({
            status: 'irreducible',
            expression
        });
    }
}
