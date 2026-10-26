/**
 * MIXED-NEST-ACTION-0B existing-authority transfer and typed-consumer
 * evidence.
 */

import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { binderMode } from '../src/v3_2/kernel';
import { createCoreLfChecker } from '../src/v3_2/lf_checker';
import { checkLambdapiProbe } from '../src/v3_2/probe';
import {
    describe,
    it
} from 'node:test';
import {
    CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE,
    CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_POLICY,
    CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE,
    compileCoreCategoricalMixedActionTransfer
} from '../src/v3_2/categorical_mixed_action_transfer';
import { CoreCategoricalProgram, CoreCategoricalProgramError } from '../src/v3_2/categorical_program';
import { kernelApplication, kernelCall, kernelFree, provenance, KernelExpression } from '../src/v3_2/kernel';
import { coreLfDefinitionalCompare } from '../src/v3_2/lf_conversion';
import { serializeKernelExpression } from '../src/v3_2/lambdapi';

const assertDeepFrozen = (value: unknown): void => {
    if (value === null || typeof value !== 'object') return;
    assert.equal(Object.isFrozen(value), true);
    Reflect.ownKeys(value).forEach(key =>
        assertDeepFrozen(
            (value as Record<PropertyKey, unknown>)[key]
        )
    );
};

describe('MIXED-NEST-ACTION-0B', () => {
    it('pins the measured existing-authority closure', () => {
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .declarationNames,
            ['Homd_index_cat', 'homd_index_presheaf', 'Functor_cart_component_func',
                'fib_cov_tapp0_func', 'homd_', 'Functor_catd_fapp0_func',
                'Homd_target_section_cat', 'FibCov_target_catd', 'fib_cov_int', 'fib_cov_src_func', 'fib_cov_transf',
                'Homd_coeff_conjoint', 'Homd_coeff_rep_func', 'Homd_coeff_rep', 'Homd_coeff_mate', 'Homd_coeff_mate_func', 'homd_id_src_sec', 'homd_id_src_func',
                'homd_id_tgt_func', 'homd_id_', 'homd_src_sec', 'homd_src_func', 'homd_tgt_func']
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .declarationCount,
            23
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .runtimeRuleCount,
            30
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .reusedProofRuleCount,
            0
        );
        assert.deepEqual(
            [
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .activeLambdapiOwnerDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .activeLambdapiRuleDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .intrinsicCoreOwnerDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .ownerSpecificCheckerOrEvaluatorDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .externalCoherenceEvidenceDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .nestedAbstractionLowererDelta,
                CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                    .textOrBrowserDelta
            ],
            [0, 0, 0, 0, 0, 0, 0]
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_MODULE
                .declarations.length,
            23
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_MODULE
                .runtimeRules.length,
            15
        );
        assertDeepFrozen(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
        );
    });

    it('subject-checks every declaration and rule generically', () => {
        const compilation =
            compileCoreCategoricalMixedActionTransfer();
        assert.equal(compilation.initialCompiled.declarations.length, 7);
        assert.equal(compilation.compiled.declarations.length, 3);
        assert.equal(compilation.identityCompiled.declarations.length, 13);
        assert.equal(compilation.runtime.rules.length, 15);
        assert.equal(
            compilation.runtime.rules.every(rule =>
                rule.subjectValidation.kind === 'typescript-checked'
            ),
            true
        );
        assert.deepEqual(
            compilation.composedRuntime.ruleIds.filter(id=>CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY.runtimeRuleIds.includes(id)),
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_BOUNDARY
                .runtimeRuleIds
        );
        assert.deepEqual(
            CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_POLICY.entries.map(
                entry => entry.policy
            ),
            Array.from({length:23}, (_,i) => [5,8,9,10,11,13,14,15].includes(i) ? 'opaque-signature' : 'checked-transparent-definition')
        );
        assert.equal(
            CORE_CATEGORICAL_MIXED_ACTION_RUNTIME_POLICY.entries.every(
                entry => entry.policy === 'runtime-rewrite'
            ),
            true
        );
    });

    it('computes native root/section projections and the independent endpoint leaf', () => {
        const c=compileCoreCategoricalMixedActionTransfer();
        const at=provenance('derived','native Homd ladder projections');
        const names=['K','D','E','FF','x','u','y','v','f'] as const;
        const [K,D,E,FF,x,u,y,v,f]=names.map(name=>kernelFree(name,at));
        const call=(name:string,args:readonly KernelExpression[]=[],implicitCount=0):KernelExpression=>{
            const link=CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE.entries.find(l=>l.symbol.name===name);
            assert.ok(link,`Missing ${name}`);
            return link.kind==='core-owner' ? kernelApplication(link.owner,args.map(value=>({value})),at)
                : args.length === 0 ? kernelFree(link.coreName,at)
                : kernelCall(kernelFree(link.coreName,at),args.map((value,index)=>({value,plicity:index<implicitCount?'implicit':'explicit'})),at);
        };
        const Cart=call('Cat_cart'),Q=call('Homd_coeff_cat');
        const op=(A:KernelExpression)=>call('Op_cat',[A]);
        const hom=(C:KernelExpression,a:KernelExpression,b:KernelExpression)=>call('Hom_cat',[C,a,b]);
        const app=(A:KernelExpression,B:KernelExpression,F:KernelExpression,z:KernelExpression)=>call('fapp0',[A,B,F,z],2);
        const fib=(A:KernelExpression,z:KernelExpression)=>app(K,Cart,A,z);
        const diagram=(A:KernelExpression)=>call('Homd_coeff_diagram',[K,A],1);
        const IX=call('hom_',[K,K,call('id_func',[K],1),x],2);
        const diagramCategory=call('Functor_cat',[K,Q]);
        const target=app(op(call('CoAt2_cat',[diagramCategory])),call('Functor_cart_cat',[K,Cart]),
            call('Homd_target_index_func',[K]),diagram(D));
        const root=call('homd_int',[K,D,E,FF],3);
        const source=call('homd_src_func',[K,D,E,FF,x],3);
        const section=call('homd_src_sec',[K,D,E,FF,x,u],3);
        const tgt=call('homd_tgt_func',[K,D,E,FF,x,u,y],3);
        const equal=(a:KernelExpression,b:KernelExpression)=>{
            const result=coreLfDefinitionalCompare(c.compiled.environment,a,b,4096,undefined,c.composedRuntime);
            const details = 'normalizedLeft' in result
                ? serializeKernelExpression(result.normalizedLeft)+'\nvs\n'+serializeKernelExpression(result.normalizedRight)
                : result.status;
            assert.equal(result.status,'equal',details);
        };
        equal(source,call('tapp0_fapp0',[K,Cart,E,target,x,root],4));
        equal(app(fib(E,x),op(call('Homd_target_section_cat',[K,D,x],1)),source,u),section);
        equal(tgt,call('tapp0_fapp0',[K,Q,diagram(D),diagram(IX),y,section],4));
        const endpoint=call('homd_',[K,D,E,FF,x,u,y,v],3);
        const component=call('tapp0_fapp0',[K,Cart,D,E,y,FF],4);
        const transport=kernelApplication('functor-hom-capped',[{value:K},{value:Cart},{value:E},
            {value:x},{value:y},{value:f}],at);
        equal(app(op(hom(K,x,y)),Cart,endpoint,f),hom(fib(E,y),app(fib(E,x),fib(E,y),transport,u),
            app(fib(D,y),fib(E,y),component,v)));
    });

    it('computes typed identity and general-FF roots through the whole y-section', () => {
        const c=compileCoreCategoricalMixedActionTransfer();
        const at=provenance('derived','constructed identity Homd ladder');
        const invoke=(name:string,args:readonly KernelExpression[]=[],implicitCount=0):KernelExpression=>{
            const link=CORE_CATEGORICAL_MIXED_ACTION_TRANSFER_LINKAGE.entries.find(l=>l.symbol.name===name);
            assert.ok(link,`Missing identity Homd dependency ${name}`);
            return link.kind==='core-owner'?kernelApplication(link.owner,args.map(value=>({value})),at):args.length
                ?kernelCall(kernelFree(link.coreName,at),args.map((value,i)=>({value,plicity:i<implicitCount?'implicit':'explicit'})),at)
                :kernelFree(link.coreName,at);
        };
        let environment=c.compiled.environment;
        const add=(name:string,type:KernelExpression)=>{
            environment=environment.extend({name,type,mode:binderMode('explicit','functorial'),provenance:at,transparency:'opaque'});
            return kernelFree(name,at);
        };
        const obj=(A:KernelExpression)=>invoke('τ',[invoke('Obj',[A])]);
        const fn=(A:KernelExpression,B:KernelExpression)=>invoke('τ',[invoke('Functor',[A,B])]);
        const hom=(A:KernelExpression,a:KernelExpression,b:KernelExpression)=>invoke('Hom_cat',[A,a,b]);
        const app=(A:KernelExpression,B:KernelExpression,F:KernelExpression,a:KernelExpression)=>invoke('fapp0',[A,B,F,a],2);
        const Cart=invoke('Cat_cart'),Q=invoke('Homd_coeff_cat');
        const K=add('identity_homd_K',invoke('Cat'));
        const E=add('identity_homd_E',fn(K,Cart)),D=add('identity_homd_D',fn(K,Cart));
        const x=add('identity_homd_x',obj(K)),y=add('identity_homd_y',obj(K));
        const fibre=(A:KernelExpression,z:KernelExpression)=>app(K,Cart,A,z);
        const u=add('identity_homd_u',obj(fibre(E,x))),v=add('identity_homd_v',obj(fibre(E,y)));
        const foreign=add('identity_homd_foreign',obj(fibre(D,y)));
        const I=hom(K,x,y),f=add('identity_homd_f',obj(I));
        const target=invoke('Homd_target_catd',[K,E],1),section=invoke('Homd_target_section_cat',[K,E,x],1);
        const root=invoke('homd_id_int',[K,E],1);
        const view=invoke('strict_transfor',[K,Cart,E,target,root],4);
        const source=invoke('tapp0_fapp0',[K,Cart,E,target,x,view],4);
        const S=app(fibre(E,x),invoke('Op_cat',[section]),source,u);
        const ix=invoke('hom_',[K,K,invoke('id_func',[K],1),x],2);
        const diagram=(A:KernelExpression)=>invoke('Homd_coeff_diagram',[K,A],1);
        const local=invoke('tapp0_fapp0',[K,Q,diagram(E),diagram(ix),y,S],4);
        const observed=invoke('homd_index_presheaf',[I,app(fibre(E,y),invoke('Homd_index_cat',[I]),local,v)],1);
        const endpoint=invoke('homd_id_',[K,E,x,u,y,v],1);
        const fAction=kernelApplication('functor-hom-capped',[K,Cart,E,x,y,f].map(value=>({value})),at);
        const expected=hom(fibre(E,y),app(fibre(E,x),fibre(E,y),fAction,u),v);
        const leaf=app(invoke('Op_cat',[I]),Cart,observed,f);
        const checker=createCoreLfChecker(environment,4096,c.composedRuntime);
        for(const term of [root,source,S,local,observed,endpoint,leaf]) {
            assert.doesNotThrow(()=>checker.infer(checker.rootContext,term));
        }
        const equal=(left:KernelExpression,right:KernelExpression)=>{
            const r=coreLfDefinitionalCompare(environment,left,right,4096,undefined,c.composedRuntime);
            assert.equal(r.status,'equal',r.status==='not-equal'
                ?serializeKernelExpression(r.normalizedLeft)+'\nvs\n'+serializeKernelExpression(r.normalizedRight):r.status);
        };
        equal(S,invoke('homd_id_src_sec',[K,E,x,u],1));
        equal(local,invoke('homd_id_tgt_func',[K,E,x,u,y],1));
        equal(observed,endpoint);
        equal(leaf,expected);
        assert.throws(()=>checker.infer(checker.rootContext,
            app(fibre(E,y),invoke('Homd_index_cat',[I]),local,foreign)));

        const FF=add('relative_homd_FF',obj(invoke('Transf_cat',[K,Cart,D,E],2)));
        const diagramCategory=invoke('Functor_cat',[K,Q]);
        const relativeTarget=app(invoke('Op_cat',[invoke('CoAt2_cat',[diagramCategory])]),
            invoke('Functor_cart_cat',[K,Cart]),invoke('Homd_target_index_func',[K]),diagram(D));
        const relativeRoot=invoke('homd_int',[K,D,E,FF],3);
        const relativeSource=invoke('tapp0_fapp0',[K,Cart,E,relativeTarget,x,relativeRoot],4);
        const relativeSection=app(fibre(E,x),invoke('Op_cat',[invoke('Homd_target_section_cat',[K,D,x],1)]),relativeSource,u);
        const relativeLocal=invoke('tapp0_fapp0',[K,Q,diagram(D),diagram(ix),y,relativeSection],4);
        const relativeObserved=invoke('homd_index_presheaf',[I,
            app(fibre(D,y),invoke('Homd_index_cat',[I]),relativeLocal,foreign)],1);
        const relativeEndpoint=invoke('homd_',[K,D,E,FF,x,u,y,foreign],3);
        const ffPoint=invoke('tapp0_fapp0',[K,Cart,D,E,y,FF],4);
        const relativeLeaf=app(invoke('Op_cat',[I]),Cart,relativeObserved,f);
        const relativeExpected=hom(fibre(E,y),app(fibre(E,x),fibre(E,y),fAction,u),
            app(fibre(D,y),fibre(E,y),ffPoint,foreign));
        const relativeChecker=createCoreLfChecker(environment,8192,c.composedRuntime);
        for(const term of [relativeRoot,relativeSource,relativeSection,relativeLocal,relativeObserved,relativeEndpoint,relativeLeaf]) {
            assert.doesNotThrow(()=>relativeChecker.infer(relativeChecker.rootContext,term));
        }
        equal(relativeSection,invoke('homd_src_sec',[K,D,E,FF,x,u],3));
        equal(relativeLocal,invoke('homd_tgt_func',[K,D,E,FF,x,u,y],3));
        equal(relativeObserved,relativeEndpoint);
        equal(relativeLeaf,relativeExpected);
        assert.throws(()=>relativeChecker.infer(relativeChecker.rootContext,
            invoke('strict_transfor',[K,Cart,D,E,FF],4)));
    });

    it('matches native identity and relative declarations and whole ladders', {
        skip:process.env.EMDASH_RUN_LAMBDAPI_HOMD_IDENTITY_PROBES!=='1'
    },()=>{
        const c=compileCoreCategoricalMixedActionTransfer();
        const modules=[c.precomposition.compiled,c.identityCompiled];
        const references=Object.assign({},...modules.flatMap(m=>[m.externalFreeReferences,m.externalTransparentDefinitions,
            Object.fromEntries(m.linkage.entries.flatMap(l=>l.kind==='free-declaration'?[[l.coreName,l.backendName]]:[]))]));
        const serialize=(term:KernelExpression)=>serializeKernelExpression(term,{externalFreeReferences:references});
        const source=['require open emdash.emdash3_2;',
            ...modules.flatMap(m=>m.declarations.flatMap(d=>[`assert ⊢ @${d.symbol.name} : ${serialize(d.type)};`,
                // Expected typing disambiguates the whole represented-inclusion body;
                // its full function equality is still checked, not only its points.
                ...(d.body ? d.symbol.name==='Homd_coeff_rep_func' ? [
                    `symbol relative_rep_mirror : ${serialize(d.type)} ≔ ${serialize(d.body)};`,
                    'assert ⊢ @Homd_coeff_rep_func ≡ relative_rep_mirror;'
                ] : [`assert ⊢ @${d.symbol.name} ≡ ${serialize(d.body)};`] : [])])),
            'symbol K : Cat; symbol E : τ (Catd K);',
            'symbol x : τ (Obj K); symbol y : τ (Obj K);',
            'symbol u : τ (Obj (fapp0 E x)); symbol v : τ (Obj (fapp0 E y));',
            'symbol f : τ (Hom K x y);',
            'symbol S : τ (Obj (@Homd_target_section_cat K E x)) ≔',
            '  @fapp0 (@fapp0 K Cat_cart E x) (Op_cat (@Homd_target_section_cat K E x))',
            '    (@tapp0_fapp0 K Cat_cart E (@Homd_target_catd K E) x',
            '      (@strict_transfor K Cat_cart E (@Homd_target_catd K E) (@homd_id_int K E))) u;',
            'assert ⊢ S ≡ @homd_id_src_sec K E x u;',
            'symbol T : τ (Functor (fapp0 E y) (Homd_index_cat (Hom_cat K x y))) ≔',
            '  @tapp0_fapp0 K Homd_coeff_cat (@Homd_coeff_diagram K E)',
            '    (@Homd_coeff_diagram K (@hom_ K K (@id_func K) x)) y S;',
            'assert ⊢ T ≡ @homd_id_tgt_func K E x u y;',
            'assert ⊢ @homd_index_presheaf (Hom_cat K x y) (fapp0 T v) ≡ @homd_id_ K E x u y v;',
            'assert ⊢ fapp0 (@homd_index_presheaf (Hom_cat K x y) (fapp0 T v)) f',
            '  ≡ Hom_cat (fapp0 E y) (fapp0 (@fapp1_fapp0 K Cat_cart E x y f) u) v;',
            'symbol D : τ (Catd K); symbol w : τ (Obj (fapp0 D y));',
            'assertnot ⊢ @fapp0 (fapp0 E y) (Homd_index_cat (Hom_cat K x y)) T w',
            '  : τ (Obj (Homd_index_cat (Hom_cat K x y)));',
            'symbol FF : τ (@Transf K Cat_cart D E);',
            'symbol SR : τ (Obj (@Homd_target_section_cat K D x)) ≔',
            '  @fapp0 (fapp0 E x) (Op_cat (@Homd_target_section_cat K D x))',
            '    (@tapp0_fapp0 K Cat_cart E (fapp0 (Homd_target_index_func K) (@Homd_coeff_diagram K D)) x',
            '      (@homd_int K D E FF)) u;',
            'assert ⊢ SR ≡ @homd_src_sec K D E FF x u;',
            'symbol TR : τ (Functor (fapp0 D y) (Homd_index_cat (Hom_cat K x y))) ≔',
            '  @tapp0_fapp0 K Homd_coeff_cat (@Homd_coeff_diagram K D)',
            '    (@Homd_coeff_diagram K (@hom_ K K (@id_func K) x)) y SR;',
            'assert ⊢ TR ≡ @homd_tgt_func K D E FF x u y;',
            'assert ⊢ @homd_index_presheaf (Hom_cat K x y) (fapp0 TR w) ≡ @homd_ K D E FF x u y w;',
            'assert ⊢ fapp0 (@homd_index_presheaf (Hom_cat K x y) (fapp0 TR w)) f',
            '  ≡ Hom_cat (fapp0 E y) (fapp0 (@fapp1_fapp0 K Cat_cart E x y f) u)',
            '      (fapp0 (@tapp0_fapp0 K Cat_cart D E y FF) w);',
            'assertnot ⊢ FF : τ (@StrictTransfor K Cat_cart D E);'
        ].join('\n');
        assert.doesNotMatch(source,/dttlf_|emdash_v3_2_/u);
        const result=checkLambdapiProbe({source:source+'\n',sourceMap:[]},{
            packageRoot:resolve(__dirname,'../emdash2'),timeoutMs:60000,warningsEnabled:true});
        assert.equal(result.accepted,true,result.diagnostics);
        assert.equal(result.timedOut,false);
    });

    it('exposes typed internal-hom and endpoint-family consumers', () => {
        const emdash = new CoreCategoricalProgram({
            sourceFile: 'tests/fixtures/categorical-mixed-action.ts',
            profile: 'fibred-displayed-mixed-nest-1'
        });
        const K = emdash.category('mixed_action_program_K');
        const D = emdash.displayedFamily(
            'mixed_action_program_D',
            K
        );
        const E = emdash.displayedFamily(
            'mixed_action_program_E',
            K
        );
        const FF = emdash.displayedFunctor(
            'mixed_action_program_FF',
            D,
            E
        );
        const x = emdash.object('mixed_action_program_x', K);
        const y = emdash.object('mixed_action_program_y', K);
        const u = emdash.object(
            'mixed_action_program_u',
            emdash.fibre(E, x)
        );
        const v = emdash.object(
            'mixed_action_program_v',
            emdash.fibre(D, y)
        );
        const internalHom = emdash.displayedInternalHom(FF);
        const endpoint = emdash.displayedInternalHomEndpointFamily(
            FF,
            x,
            u,
            y,
            v
        );
        const compiled = emdash.compile(internalHom);
        const endpointTotal = emdash.serializeCategory(
            emdash.totalCategory(endpoint)
        );
        assert.equal(compiled.surfaceType.tag, 'displayed-functor');
        assert.match(compiled.explicitCore, /homd_int/u);
        assert.match(endpointTotal, /homd_/u);
        assert.equal(compiled.productionLambdapiDependency, false);
    });

    it('keeps the consumers behind the mixed root profile', () => {
        const emdash = new CoreCategoricalProgram({
            profile: 'fibred-displayed-nd-higher-1'
        });
        const K = emdash.category('mixed_action_gate_K');
        const D = emdash.displayedFamily('mixed_action_gate_D', K);
        const E = emdash.displayedFamily('mixed_action_gate_E', K);
        const FF = emdash.displayedFunctor(
            'mixed_action_gate_FF',
            D,
            E
        );
        assert.throws(
            () => emdash.displayedInternalHom(FF),
            (error: unknown) =>
                error instanceof CoreCategoricalProgramError &&
                error.code === 'UNAVAILABLE_MIXED_MODE'
        );
    });
});
