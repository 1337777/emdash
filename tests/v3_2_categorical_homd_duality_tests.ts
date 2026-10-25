/** Native duality prerequisites of the migrated whole Homd target. */
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { resolve } from 'node:path';
import { describe, it } from 'node:test';
import { compileCoreHomdDualityTransfer, CORE_HOMD_DUALITY_MODULE } from '../src/v3_2/categorical_homd_duality_transfer';
import { checkLambdapiProbe } from '../src/v3_2/probe';
import { kernelFree, provenance } from '../src/v3_2/kernel';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';

describe('native Homd dimension-two duality transfer', () => {
    it('checks the native signatures and projections against the exact source', () => {
        const c=compileCoreHomdDualityTransfer();
        assert.equal(c.compiled.declarations.length,2);
        assert.equal(c.runtime.rules.length,5);
        assert.ok(c.runtime.rules.every(r=>r.subjectValidation.kind==='typescript-checked'));
        assert.equal(CORE_HOMD_DUALITY_MODULE.sourceSha256,
            'sha256:'+createHash('sha256').update(readFileSync(resolve(__dirname,'../emdash2/emdash3_2.lp'))).digest('hex'));
    });
    it('checks the whole dual functor and retained variance in Lambdapi', {
        skip:process.env.EMDASH_RUN_LAMBDAPI_HOMD_DUALITY_PROBES!=='1'
    },()=>{
        const c=compileCoreHomdDualityTransfer(), chain=c.prerequisite.prerequisite;
        const evaluation=chain.prerequisite, pi=evaluation.prerequisite, weaken=pi.prerequisite;
        const transfd=weaken.prerequisite,binder=transfd.prerequisite,structure=binder.prerequisite;
        const product=structure.prerequisite,comprehension=product.prerequisite,composition=comprehension.prerequisite;
        const dependent=composition.dependent,structural=dependent.structural;
        const modules=[structural.initialDeclarations,structural.compiled,dependent.compiled,composition.compiled,
            comprehension.compiled,product.compiled,structure.compiled,binder.compiled,transfd.compiled,
            weaken.compiled,pi.compiled,evaluation.prerequisiteCompiled,evaluation.compiled,
            chain.prerequisiteCompiled,chain.compiled,c.prerequisite.compiled,c.compiled];
        const references=Object.assign({},...modules.flatMap(m=>[m.externalFreeReferences,m.externalTransparentDefinitions]));
        const serialize=(t:Parameters<typeof serializeKernelExpression>[0])=>serializeKernelExpression(t,{externalFreeReferences:references});
        const site=provenance('derived','native Homd duality conformance');
        const equations=c.runtime.rules.map(rule=>{
            const left=c.runtime.instantiateRuleLeft(rule,rule.variables.map(v=>kernelFree(v.name,site)),site);
            const result=c.runtime.rewriteHead(left);
            assert.equal(result.status,'rewritten');
            if(result.status!=='rewritten') throw new Error('Missing duality projection');
            assert.equal(result.ruleId,rule.id);
            return `assert ⊢ ${serialize(left)} ≡ ${serialize(result.after)};`;
        });
        const source=['require open emdash.emdash3_2;','symbol A : Cat;','symbol B : Cat;',
            'symbol F : τ (Functor A B);','symbol x : τ (Obj A);','symbol y : τ (Obj A);',...equations,
            'symbol G : τ (Functor (CoAt2_cat A) B);',
            'assert ⊢ @CoAt2_func (CoAt2_cat A) B G : τ (Functor A (CoAt2_cat B));',
            'assertnot ⊢ CoAt2_cat A ≡ A;',
            'assertnot ⊢ Hom_cat (CoAt2_cat A) x y ≡ Hom_cat A y x;'].join('\n');
        const result=checkLambdapiProbe({source,sourceMap:[]},{packageRoot:resolve(__dirname,'../emdash2'),timeoutMs:60_000});
        assert.equal(result.accepted,true,result.diagnostics+'\n'+source);
        assert.equal(result.timedOut,false);
    });
});
