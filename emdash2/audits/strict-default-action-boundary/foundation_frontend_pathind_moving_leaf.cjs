// Non-library required-computation diagnostic; currently expected to exit 1.
// See foundation_frontend_pathind_internalized_review.md.
const fs=require('node:fs');
const k=require('../../../src/v3_2/kernel');
const {coreLfDefinitionalCompare}=require('../../../src/v3_2/lf_conversion');
const {compileCoreLfProofProgram,createCoreLfProofCheckingChecker}=require('../../../src/v3_2/lf_transfer_proof');
const pi=require('../../../src/v3_2/categorical_fibred_dependent_target_transfer');
const {serializeKernelExpression:s}=require('../../../src/v3_2/lambdapi');
const p=require('../../../src/v3_2/pathind_internalized_transfer');
const fixed=require('../../../src/v3_2/pathind_fixed_source_transfer');
const out=require('../../../src/v3_2/pathout_foundation_transfer');
const c=p.compileCorePathindInternalized1dTransfer(), at=k.provenance('derived','required whole moving PathInd component');
const app=(owner,args)=>k.kernelApplication(owner,args.map(value=>({value})),at);
const obj=A=>app('decode',[app('object-classifier',[A])]);
let env=c.compiled.environment;
const add=(name,type)=>{env=env.extend({name,type,mode:k.binderMode('explicit','functorial'),provenance:at,transparency:'opaque'});return k.kernelFree(name,at);};
const Z=add('moving_leaf_Z',app('category-universe',[]));
const x=add('moving_leaf_x',obj(Z));
const pathout=c.predecessor.predecessor.libraryCompiled.application(out.CORE_PATHOUT_FOUNDATION_1B_SYMBOLS.pathoutCategory,[Z,x],at);
const E=add('moving_leaf_E',obj(app('displayed-category-category',[pathout])));
const program=c.baseRuntimeFragment.localProgram,rule=program.rule('pathind.internalized.path-ind-transfd-component');
const whole=program.instantiateRuleLeft(rule,[Z,x],at),next=program.rewriteHead(whole);
if(next.status!=='rewritten'||next.after.tag!=='application')throw new Error('Whole component projection missing');
const target=next.after.arguments[1].value;
const [A,B,F,G]=target.arguments.map(a=>a.value);
const observed=app('transfor-component-capped',[A,B,F,G,E,whole]);
const expected=c.predecessor.trustedCompiled.application(fixed.CORE_PATHIND_FIXED_SOURCE_1C_SYMBOLS.pathInductionComponentFunctor,[Z,x,E],at);
const proof=compileCoreLfProofProgram(pi.CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_MODULE,pi.CORE_CATEGORICAL_FIBRED_DEPENDENT_TARGET_PROOF_POLICY,c.declarationContext,{runtimeProgram:c.composedRuntime,comparisonStepLimit:2048});
const checker=createCoreLfProofCheckingChecker(env,c.composedRuntime,proof);
let typing;
try{checker.infer(checker.rootContext,observed);typing='passed';}catch(error){typing=String(error);}
const comparison=coreLfDefinitionalCompare(env,observed,expected,2048,undefined,c.composedRuntime);
const result={typing,requiredRuntimeEquality:comparison.status==='equal',status:comparison.status,steps:comparison.steps,
 observed:s(observed),expected:s(expected),...(comparison.status==='not-equal'?{normalizedLeft:s(comparison.normalizedLeft),normalizedRight:s(comparison.normalizedRight)}:{})};
fs.mkdirSync('emdash2/tmp/probes/kernel_boundary_continuation',{recursive:true});
fs.writeFileSync('emdash2/tmp/probes/kernel_boundary_continuation/internalized_moving_leaf.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({typing,status:comparison.status,steps:comparison.steps,requiredRuntimeEquality:result.requiredRuntimeEquality}));

if (!result.requiredRuntimeEquality) process.exitCode = 1;
