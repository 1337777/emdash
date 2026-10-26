/** Proof-only declaration typing closes LF parameters without changing bodies. */
import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { binderMode, kernelExpressionEquals, kernelFree, provenance, kernelLambda, kernelBinder, kernelBound, kernelCall } from '../src/v3_2/kernel';
import { coreLfDefinitionalCompare } from '../src/v3_2/lf_conversion';
import { CoreLfTransferScopedBuilder as Builder, coreLfQualifiedSymbol as qualified,
    coreLfTransferAbsentBody, coreLfTransferExplicitBody, createCoreLfModuleSpec,
    createCoreLfTransferPolicyOverlay } from '../src/v3_2/lf_transfer';
import { compileCoreLfDeclarations, createCoreLfTransferDeclarationLinkage } from '../src/v3_2/lf_transfer_compiler';
import { compileCoreLfRuntimeProgram } from '../src/v3_2/lf_transfer_runtime';
import { CoreLfCompiledProofProgram, compileCoreLfProofProgram } from '../src/v3_2/lf_transfer_proof';

const fixture = () => {
    const moduleId='fixture.definition_proof', sym=(name:string)=>qualified(moduleId,name);
    const Index=sym('Index'), P=sym('P'), Q=sym('Q'), input=sym('input'), occupied=sym('occupied');
    const b=new Builder(), explicit=binderMode('explicit','functorial');
    const app=(name:typeof P,x:ReturnType<Builder['global']>)=>b.call(b.global(name),[{plicity:'explicit',value:x}]);
    const params={moduleId,authorityPath:'tests/fixtures/definition_proof.lp',sourceSha256:'sha256:'+'a'.repeat(64),dependencies:[],inductives:[]};
    const source={authorityPath:params.authorityPath,sourceFragment:'generic declaration proof fixture'};
    const modifiers={visibility:'public' as const,rigidity:'ordinary' as const,sourceOpacity:'opaque' as const};
    const decls=[
        {symbol:Index,type:b.term(b.type())},
        {symbol:P,type:b.term(b.pi('x',b.global(Index),()=>b.type(),explicit))},
        {symbol:Q,type:b.term(b.pi('x',b.global(Index),()=>b.type(),explicit))},
        {symbol:input,type:b.term(b.pi('x',b.global(Index),x=>app(P,x),explicit))},
        {symbol:occupied,type:b.term(b.global(Index))}
    ].map((d,order)=>({...d,order,body:coreLfTransferAbsentBody(),modifiers,provenance:source}));
    const base=createCoreLfModuleSpec({...params,revision:'definition-proof-base-1',fragmentId:'base',externalSymbols:[],declarations:decls,runtimeRules:[],proofRules:[]});
    const basePolicy=createCoreLfTransferPolicyOverlay(base,{revision:'base-policy',moduleRevision:base.revision,
        entries:decls.map(d=>({order:d.order,target:{kind:'declaration' as const,symbol:d.symbol},policy:'opaque-signature' as const,evidence:'fixture'}))});
    const baseLinks=createCoreLfTransferDeclarationLinkage(base,{revision:'base-links',moduleRevision:base.revision,
        entries:decls.map(d=>({order:d.order,symbol:d.symbol,kind:'free-declaration' as const,
            coreName:d.symbol===occupied?'lf_definition_parameter_0':'defproof_'+d.symbol.name,backendName:d.symbol.name}))});
    const declarations=compileCoreLfDeclarations(base,basePolicy,baseLinks);
    const runtimeModule=createCoreLfModuleSpec({...base,fragmentId:'empty-runtime',declarations:[],
        externalSymbols:decls.map(d=>({symbol:d.symbol,availability:'earlier-fragment' as const}))});
    const runtime=compileCoreLfRuntimeProgram(runtimeModule,createCoreLfTransferPolicyOverlay(runtimeModule,
        {revision:'empty-runtime-policy',moduleRevision:runtimeModule.revision,entries:[]}),declarations);
    const x=b.capture('x'),y=b.capture('y');
    const proofModule=createCoreLfModuleSpec({...params,revision:'definition-proof-rule-1',fragmentId:'proof',
        externalSymbols:[Index,P,Q].map(symbol=>({symbol,availability:'earlier-fragment' as const})),declarations:[],runtimeRules:[],
        proofRules:[{order:0,id:'fixture.definition.types',sourceOwner:P,
            variables:['x','y'].map(name=>({name,role:'matched' as const,type:b.template(b.global(Index))})),
            problem:{left:b.pattern(app(P,x)),right:b.pattern(app(Q,y))},
            generatedConstraints:[{left:b.template(x),right:b.template(y)}],provenance:source}]});
    const proofPolicy=createCoreLfTransferPolicyOverlay(proofModule,{revision:'proof-policy',moduleRevision:proofModule.revision,
        entries:[{order:0,target:{kind:'proof-rule',id:'fixture.definition.types'},policy:'proof-unification',evidence:'fixture'}]});
    const program=compileCoreLfProofProgram(proofModule,proofPolicy,declarations,{runtimeProgram:runtime});
    const definition=(options:{wrong?:boolean;unnecessary?:boolean;implicit?:boolean;badDomain?:boolean;dependent?:boolean}={})=>{
        const {wrong=false,unnecessary=false,implicit=false,badDomain=false,dependent=false}=options;
        const name=sym('lift');
        const module=createCoreLfModuleSpec({...params,revision:'definition-proof-consumer-1',fragmentId:'consumer',
            externalSymbols:decls.map(d=>({symbol:d.symbol,availability:'earlier-fragment' as const})),runtimeRules:[],proofRules:[],
            declarations:[{order:0,symbol:name,type:b.term(b.pi('x',b.global(Index),v=>dependent ? b.pi('u',app(P,v),()=>app(Q,v),explicit) : app(unnecessary?P:Q,v),explicit)),
                body:coreLfTransferExplicitBody(b.term(b.lam('x',badDomain?app(P,b.global(occupied)):b.global(Index),v=>dependent ? b.lam('u',app(P,v),u=>u,explicit) : app(input,wrong?b.global(occupied):v),implicit?binderMode('implicit','functorial'):explicit))),
                modifiers:{...modifiers,sourceOpacity:'transparent'},provenance:source}]});
        const policy=createCoreLfTransferPolicyOverlay(module,{revision:'consumer-policy',moduleRevision:module.revision,
            entries:[{order:0,target:{kind:'declaration',symbol:name},policy:'checked-transparent-definition',evidence:'fixture'}]});
        const links=createCoreLfTransferDeclarationLinkage(module,{revision:'consumer-links',moduleRevision:module.revision,
            entries:[...baseLinks.entries,{order:baseLinks.entries.length,symbol:name,kind:'free-declaration',coreName:'defproof_lift',backendName:'lift'}]});
        const compile=(proof=program,ids:readonly string[]=['fixture.definition.types'])=>compileCoreLfDeclarations(module,policy,links,{
            initialEnvironment:declarations.environment,runtimeProgram:runtime,
            definitionTypeProof:{program:proof,declarations:[{symbol:name,proofRuleIds:ids}]}});
        return {module,policy,links,compile};
    };
    return {declarations,runtime,program,definition};
};

describe('LF declaration proof checking',()=>{
    it('requires an explicit proof profile and preserves the definition body',()=>{
        const f=fixture(),d=f.definition();
        assert.throws(()=>compileCoreLfDeclarations(d.module,d.policy,d.links,{initialEnvironment:f.declarations.environment,runtimeProgram:f.runtime}));
        const c=d.compile(),result=c.declarations[0];
        assert.equal(result.status,'installed-transparent');
        assert.deepEqual(result.definitionProofRuleIds,['fixture.definition.types']);
        assert.ok(result.body);
        assert.equal(result.body.tag,'lambda');
        const originalAt=provenance('derived','unchanged definition body');
        const original=kernelLambda(kernelBinder('x',kernelFree('defproof_Index',originalAt),binderMode('explicit','functorial'),originalAt),
            kernelCall(kernelFree('defproof_input',originalAt),[{plicity:'explicit',value:kernelBound(0,originalAt)}],originalAt),originalAt);
        assert.equal(kernelExpressionEquals(result.body,original),true);
        assert.equal(c.environment.lookup('lf_definition_parameter_1'),undefined);
        assert.equal(kernelExpressionEquals(result.body,c.environment.lookup('defproof_lift')!.body!),true);
        const at=provenance('derived','proof noncollapse'),value=kernelFree('lf_definition_parameter_0',at);
        const p={tag:'call' as const,callee:kernelFree('defproof_P',at),arguments:[{plicity:'explicit' as const,value,provenance:at}],provenance:at};
        const q={...p,callee:kernelFree('defproof_Q',at)};
        assert.equal(coreLfDefinitionalCompare(c.environment,p,q,64,undefined,f.runtime).status,'not-equal');
        assert.throws(()=>c.environment.extend({name:'later',type:result.type,body:result.body,transparency:'transparent',
            mode:binderMode('explicit','functorial'),provenance:at}));
    });
    it('preserves parameter identity and binder modes',()=>{
        const f=fixture();
        assert.throws(()=>f.definition({wrong:true}).compile());
        assert.throws(()=>f.definition({implicit:true}).compile());
        assert.throws(()=>f.definition({badDomain:true}).compile());
    });
    it('closes a dependent parameter telescope without losing earlier variables',()=>{
        const f=fixture(),c=f.definition({dependent:true}).compile();
        assert.deepEqual(c.declarations[0].definitionProofRuleIds,['fixture.definition.types']);
        assert.equal(c.declarations[0].body?.tag,'lambda');
        assert.equal(c.environment.declarations.length,f.declarations.environment.declarations.length+1);
    });
    it('rejects wrong, unnecessary and foreign proof allowances',()=>{
        const f=fixture(),d=f.definition();
        assert.throws(()=>d.compile(f.program,['missing.rule']));
        assert.throws(()=>f.definition({unnecessary:true}).compile());
        assert.throws(()=>d.compile(fixture().program));
    });
    it('propagates the selected proof budget',()=>{
        const f=fixture(),d=f.definition();
        const bounded=new CoreLfCompiledProofProgram(f.program.module,f.program.policy,f.program.declarations,
            f.program.rules,0,f.runtime);
        assert.throws(()=>d.compile(bounded),/step|budget|conversion/iu);
    });
});
