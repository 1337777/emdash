/**
 * Reference to the normal LF declaration used by admitted Catd families.
 * Its declaration/projections belong to the directed continuation profile;
 * this authoring helper grants no intrinsic owner or conversion rule.
 */
import { KernelExpression, Provenance, kernelFree } from './kernel';

export const CORE_CATEGORICAL_FAMILY_COEFFICIENT_CORE_NAME = 'dttlf_Cat_cart';

export const coreCategoricalFamilyCoefficient = (
    source: Provenance
): KernelExpression => kernelFree(
    CORE_CATEGORICAL_FAMILY_COEFFICIENT_CORE_NAME, source
);
