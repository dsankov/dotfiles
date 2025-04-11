exports.id=928,exports.ids=[928],exports.modules={1687:(e,t,i)=>{i.d(t,{HomeWebviewProvider:()=>HomeWebviewProvider});var r=i(1398),s=i(5425),o=i(6525),n=i(1518),a=i(457),h=i(8191),l=i(1192),u=i(7222),c=i(3949),p=i(1403),d=i(6066),g=i(3467),m=i(778),v=i(3447),w=i(1081),b=i(311),f=i(3711),y=i(9317),C=i(8554),R=i(3310),P=i(6599),S=i(6461),_=i(9426),k=i(1078),D=i(3378);async function O(e){let t=await e.launchpad.getCategorizedItems();if(null!=t.error)return{error:t.error};let i=k.H.get("launchpad.indicator.groups")??[];return(0,D.a)(t.items,i)}var I=i(5725),B=i(4301),W=i(655),$=i(6612),F=i(4342),q=i(6851),L=i(7747),H=i(5576);let SubscriptionManager=class SubscriptionManager{constructor(e,t){this.source=e,this.subscribe=t}_status="stopped";get status(){return this._status}_subscription;dispose(){this.stop()}start(){(null==this._subscription||"started"!==this._status)&&(this._subscription=this.subscribe(this.source),this._status="started")}pause(){this.stop("paused")}resume(){this.start()}stop(e){this._subscription?.dispose(),this._subscription=void 0,this._status=e??"stopped"}};var T=i(9881),M=i(5510);let E="home",U=new M.Oz(E,"launchpad/summary"),A=new M.Oz(E,"overview/active"),z=new M.Oz(E,"overview/inactive"),x=new M.Oz(E,"overviewFilter"),N=new M.Q2(E,"overview/repository/change"),G=new M.C1(E,"overview/repository/didChange"),Z=new M.Q2(E,"previewEnabled/toggle"),Q=new M.Q2(E,"section/collapse"),j=new M.Q2(E,"walkthrough/dismiss"),V=new M.Q2(E,"overview/filter/set"),Y=new M.Q2(E,"openInGraph"),J=new M.C1(E,"repositories/didCompleteDiscovering"),K=new M.C1(E,"previewEnabled/didChange"),X=new M.C1(E,"repository/wip/didChange"),ee=new M.C1(E,"repositories/didChange"),et=new M.C1(E,"walkthroughProgress/didChange"),ei=new M.C1(E,"integrations/didChange"),er=new M.C1(E,"launchpad/didChange"),es=new M.C1(E,"subscription/didChange"),eo=new M.C1(E,"org/settings/didChange"),en=new M.C1(E,"home/ownerFilter/didChange"),ea=new M.C1(E,"account/didFocus");var eh=Object.defineProperty,el=Object.getOwnPropertyDescriptor,eu=(e,t,i,r)=>{for(var s,o=r>1?void 0:r?el(t,i):t,n=e.length-1;n>=0;n--)(s=e[n])&&(o=(r?s(t,i,o):s(o))||o);return r&&o&&eh(t,i,o),o};let ec=Object.freeze({dispose:()=>{}}),ep={OneDay:864e5,OneWeek:6048e5,OneMonth:2592e6,OneYear:31536e6};let HomeWebviewProvider=class HomeWebviewProvider{constructor(e,t){this.container=e,this.host=t,this._disposable=r.Disposable.from(this.container.git.onDidChangeRepositories(this.onRepositoriesChanged,this),r.workspace.isTrusted?ec:r.workspace.onDidGrantWorkspaceTrust(()=>this.notifyDidChangeRepositories(),this),this.container.subscription.onDidChange(this.onSubscriptionChanged,this),(0,W.wt)(this.onContextChanged,this),this.container.integrations.onDidChangeConfiguredIntegrations(this.onIntegrationsChanged,this),this.container.walkthrough.onProgressChanged(this.onWalkthroughChanged,this),k.H.onDidChange(this.onDidChangeConfig,this),this.container.launchpad.onDidChange(this.onDidLaunchpadChange,this),this.container.ai.onDidChangeModel(this.onAIModelChanged,this))}_disposable;_discovering;_etag;_etagFileSystem;_etagRepository;_etagSubscription;_pendingFocusAccount=!1;dispose(){this._disposable.dispose()}getTelemetryContext(){return{...this.host.getTelemetryContext(),"context.preview":this.getPreviewEnabled()?"v16":void 0}}_overviewBranchFilter={recent:{threshold:"OneWeek"},stale:{threshold:"OneYear",show:!1,limit:9}};onShowing(e,t,...i){this._etag=this.container.git.etag,this.ensureRepoDiscovery();let[r]=i;if(r?.focusAccount===!0){if(!e&&this.host.ready&&this.host.visible)return queueMicrotask(()=>void this.host.notify(ea,void 0)),[!0,void 0];this._pendingFocusAccount=!0}return[!0,void 0]}async ensureRepoDiscovery(){this.container.git.isDiscoveringRepositories&&(this._discovering=this.container.git.isDiscoveringRepositories,this._discovering.finally(()=>this._discovering=void 0),this._etag=await this._discovering,this.notifyDidCompleteDiscoveringRepositories())}onAIModelChanged(e){this.notifyDidChangeIntegrations()}onIntegrationsChanged(e){this.notifyDidChangeIntegrations()}async onChooseRepository(){let e=this.getSelectedRepository(),t=this.container.git.openRepositories.sort((t,i)=>(t===e?1:-1)-(i===e?1:-1)||(t.starred?-1:1)-(i.starred?-1:1)||t.index-i.index),i=await (0,I.oe)(`Switch Repository ${n.EO.Dot} ${e?.name}`,"Choose a repository to switch to",t);if(null!=i&&i!==e)return this.selectRepository(i.path)}onRepositoriesChanged(){null==this._discovering&&this._etag!==this.container.git.etag&&this.notifyDidChangeRepositories()}onWalkthroughChanged(){this.notifyDidChangeProgress()}onDidChangeConfig(e){k.H.changed(e,"home.preview.enabled")&&this.notifyDidChangeConfig()}onDidLaunchpadChange(){this.notifyDidChangeLaunchpad()}async push(e=!1){let t=this.getSelectedRepository();return t?(0,h.b)({command:"push",state:{repos:[t],flags:e?["--force"]:void 0}}):Promise.resolve()}async publishBranch(e){let{repo:t,branch:i}=await this.getRepoInfoFromRef(e);if(null!=i)return u.VC(t,void 0,(0,v.iw)(i))}async pull(){let e=this.getSelectedRepository();return e?(0,h.b)({command:"pull",state:{repos:[e]}}):Promise.resolve()}registerCommands(){return[(0,B.Lb)(`${this.host.id}.pull`,this.pull,this),(0,B.Lb)(`${this.host.id}.push`,e=>{this.push(e.force)},this),(0,B.Lb)(`${this.host.id}.publishBranch`,this.publishBranch,this),(0,B.Lb)(`${this.host.id}.refresh`,()=>this.host.refresh(!0),this),(0,B.Lb)(`${this.host.id}.disablePreview`,()=>this.onTogglePreviewEnabled(!1),this),(0,B.Lb)(`${this.host.id}.enablePreview`,()=>this.onTogglePreviewEnabled(!0),this),(0,B.Lb)(`${this.host.id}.previewFeedback`,()=>(0,$.CZ)("https://github.com/gitkraken/vscode-gitlens/discussions/3721"),this),(0,B.Lb)(`${this.host.id}.whatsNew`,()=>(0,$.CZ)(n.DS.releaseNotes),this),(0,B.Lb)(`${this.host.id}.help`,()=>(0,$.CZ)(n.DS.helpCenter),this),(0,B.Lb)(`${this.host.id}.issues`,()=>(0,$.CZ)(n.DS.githubIssues),this),(0,B.Lb)(`${this.host.id}.info`,()=>(0,$.CZ)(n.DS.helpCenterHome),this),(0,B.Lb)(`${this.host.id}.discussions`,()=>(0,$.CZ)(n.DS.githubDiscussions),this),(0,B.Lb)(`${this.host.id}.account.resync`,e=>this.container.subscription.validate({force:!0},e),this),(0,B.Lb)("gitlens.home.deleteBranchOrWorktree",this.deleteBranchOrWorktree,this),(0,B.Lb)("gitlens.home.pushBranch",this.pushBranch,this),(0,B.Lb)("gitlens.home.openMergeTargetComparison",this.mergeTargetCompare,this),(0,B.Lb)("gitlens.home.openPullRequestChanges",this.pullRequestChanges,this),(0,B.Lb)("gitlens.home.openPullRequestComparison",this.pullRequestCompare,this),(0,B.Lb)("gitlens.home.openPullRequestOnRemote",this.pullRequestViewOnRemote,this),(0,B.Lb)("gitlens.home.openPullRequestDetails",this.pullRequestDetails,this),(0,B.Lb)("gitlens.home.createPullRequest",this.pullRequestCreate,this),(0,B.Lb)("gitlens.home.openWorktree",this.worktreeOpen,this),(0,B.Lb)("gitlens.home.switchToBranch",this.switchToBranch,this),(0,B.Lb)("gitlens.home.fetch",this.fetch,this),(0,B.Lb)("gitlens.home.openInGraph",this.openInGraph,this),(0,B.Lb)("gitlens.home.createBranch",this.createBranch,this),(0,B.Lb)("gitlens.home.mergeIntoCurrent",this.mergeIntoCurrent,this),(0,B.Lb)("gitlens.home.rebaseCurrentOnto",this.rebaseCurrentOnto,this),(0,B.Lb)("gitlens.home.startWork",this.startWork,this),(0,B.Lb)("gitlens.home.createCloudPatch",this.createCloudPatch,this),(0,B.Lb)("gitlens.home.skipPausedOperation",this.skipPausedOperation,this),(0,B.Lb)("gitlens.home.continuePausedOperation",this.continuePausedOperation,this),(0,B.Lb)("gitlens.home.abortPausedOperation",this.abortPausedOperation,this),(0,B.Lb)("gitlens.home.openRebaseEditor",this.openRebaseEditor,this)]}setOverviewFilter(e){this._overviewBranchFilter=e,this.host.notify(en,{filter:this._overviewBranchFilter})}async onMessageReceived(e){switch(!0){case Q.is(e):this.onCollapseSection(e.params);break;case j.is(e):this.dismissWalkthrough();break;case V.is(e):this.setOverviewFilter(e.params);break;case U.is(e):this.host.respond(U,e,await O(this.container));break;case x.is(e):this.host.respond(x,e,this._overviewBranchFilter);break;case N.is(e):if(await this.onChooseRepository()==null)return;this.host.notify(G,void 0);break;case Z.is(e):this.onTogglePreviewEnabled();break;case Y.is(e):this.openInGraph(e.params);break;case A.is(e):this.host.respond(A,e,await this.getActiveBranchOverview());break;case z.is(e):this.host.respond(z,e,await this.getInactiveBranchOverview())}}includeBootstrap(){return this.getState()}onRefresh(){this.resetBranchOverview(),this.notifyDidChangeRepositories()}onReloaded(){this.onRefresh(),this.notifyDidChangeProgress()}onReady(){!0===this._pendingFocusAccount&&(this._pendingFocusAccount=!1,this.host.notify(ea,void 0))}hasRepositoryChanged(){if(this._repositorySubscription?.source!=null){if(this._repositorySubscription.source.etag!==this._etagRepository||this._repositorySubscription.source.etagFileSystem!==this._etagFileSystem)return!0}else if(this._etag!==this.container.git.etag)return!0;return!1}onVisibilityChanged(e){if(!e){this._repositorySubscription?.pause();return}this._repositorySubscription?.resume(),null==this._discovering&&(this.container.subscription.etag!==this._etagSubscription||this.hasRepositoryChanged())&&this.notifyDidChangeRepositories(!0)}openInGraph(e){let t=null!=e?this._repositoryBranches.get(e.repoPath):void 0;if(null==t){(0,B.RS)("gitlens.showGraph",this.getSelectedRepository());return}if("branch"===e.type){let i=t.branches.find(t=>t.id===e.branchId);if(null!=i){(0,B.RS)("gitlens.showInCommitGraph",{ref:(0,v.iw)(i)});return}}(0,B.RS)("gitlens.showGraph",t.repo)}createBranch(){this.container.telemetry.sendEvent("home/createBranch"),(0,B.RS)("gitlens.gitCommands",{command:"branch",state:{subcommand:"create",repo:this.getSelectedRepository(),suggestNameOnly:!0,suggestRepoOnly:!0,confirmOptions:["--switch","--worktree"]}})}async mergeIntoCurrent(e){let{repo:t,branch:i}=await this.getRepoInfoFromRef(e);null!=i&&u.h1(t,(0,v.iw)(i))}async rebaseCurrentOnto(e){let{repo:t,branch:i}=await this.getRepoInfoFromRef(e);null!=i&&u.RU(t,(0,v.iw)(i))}startWork(){this.container.telemetry.sendEvent("home/startWork"),(0,B.RS)("gitlens.startWork",{command:"startWork",source:"home"})}async abortPausedOperation(e){let t=this.container.git.status(e.repoPath).abortPausedOperation;if(null!=t)try{await t()}catch(e){r.window.showErrorMessage(e.message)}}async continuePausedOperation(e){if("revert"===e.type)return;let t=this.container.git.status(e.repoPath).continuePausedOperation;if(null!=t)try{await t()}catch(e){r.window.showErrorMessage(e.message)}}async skipPausedOperation(e){let t=this.container.git.status(e.repoPath).continuePausedOperation;if(null!=t)try{await t({skip:!0})}catch(e){r.window.showErrorMessage(e.message)}}async openRebaseEditor(e){if("rebase"!==e.type)return;let t=await this.container.git.config(e.repoPath).getGitDir?.();if(null==t)return;let i=r.Uri.joinPath(t.uri,"rebase-merge","git-rebase-todo");(0,B.S4)("vscode.openWith",i,"gitlens.rebase",{preview:!1})}async createCloudPatch(e){let{repo:t}=await this.getRepoInfoFromRef(e);if(null==t)return;let i=await t.git.status().getStatus();if(null==i){r.window.showErrorMessage("Unable to create cloud patch");return}let s=[];for(let e of i.files){let t={repoPath:e.repoPath,path:e.path,status:e.status,originalPath:e.originalPath,staged:e.staged};s.push(t),e.staged&&e.wip&&s.push({...t,staged:!1})}let o={type:"wip",repository:{name:t.name,path:t.path,uri:t.uri.toString()},files:s,revision:{to:d.SU,from:"HEAD"}};(0,R.X)({mode:"create",create:{changes:[o]}})}onTogglePreviewEnabled(e){void 0===e&&(e=!this.getPreviewEnabled()),this.getPreviewCollapsed()||this.onCollapseSection({section:"newHomePreview",collapsed:!0}),this.container.telemetry.sendEvent("home/preview/toggled",{enabled:e,version:"v16"}),k.H.updateEffective("home.preview.enabled",e)}onCollapseSection(e){let t=this.container.storage.get("home:sections:collapsed");if(null==t){!0===e.collapsed&&this.container.storage.store("home:sections:collapsed",[e.section]).catch();return}let i=t.indexOf(e.section);if(!0===e.collapsed){-1===i&&this.container.storage.store("home:sections:collapsed",[...t,e.section]).catch();return}-1!==i&&(t.splice(i,1),this.container.storage.store("home:sections:collapsed",t).catch())}dismissWalkthrough(){this.container.storage.get("home:walkthrough:dismissed")||(this.container.storage.store("home:walkthrough:dismissed",!0).catch(),this.container.usage.track("home:walkthrough:dismissed").catch())}getWalkthroughDismissed(){return this.container.storage.get("home:walkthrough:dismissed")??!1}getPreviewCollapsed(){return this.container.storage.get("home:sections:collapsed")?.includes("newHomePreview")??!1}getAmaBannerCollapsed(){return Date.now()>=new Date("2025-02-13T13:00:00-05:00").getTime()||(this.container.storage.get("home:sections:collapsed")?.includes("feb2025AmaBanner")??!1)}getIntegrationBannerCollapsed(){return this.container.storage.get("home:sections:collapsed")?.includes("integrationBanner")??!1}getOrgSettings(){return{drafts:(0,W.SD)("gitlens:gk:organization:drafts:enabled",!1),ai:(0,W.SD)("gitlens:gk:organization:ai:enabled",!0)}}onContextChanged(e){"gitlens:gk:organization:drafts:enabled"===e&&this.notifyDidChangeOrgSettings()}async onSubscriptionChanged(e){e.etag!==this._etagSubscription&&(await this.notifyDidChangeSubscription(e.current),(0,P.k0)(e.current.state)!==(0,P.k0)(e.previous.state)&&this.onOverviewRepoChanged())}async getState(e){let[t,i,r]=await Promise.allSettled([this.getSubscriptionState(e),this.getIntegrationStates(!0),this.container.ai.getModel({silent:!0},{source:"home"})]);if("rejected"===t.status)throw t.reason;let s=(0,H.Ro)(i)??[],o=s.some(e=>e.connected),n={model:(0,H.Ro)(r)};return{...this.host.baseWebviewState,discovering:null!=this._discovering,repositories:this.getRepositoriesState(),webroot:this.host.getWebRoot(),subscription:t.value.subscription,avatar:t.value.avatar,organizationsCount:t.value.organizationsCount,orgSettings:this.getOrgSettings(),previewCollapsed:this.getPreviewCollapsed(),integrationBannerCollapsed:this.getIntegrationBannerCollapsed(),integrations:s,ai:n,hasAnyIntegrationConnected:o,walkthroughProgress:this.getWalkthroughDismissed()?void 0:{allCount:this.container.walkthrough.walkthroughSize,doneCount:this.container.walkthrough.doneCount,progress:this.container.walkthrough.progress},previewEnabled:this.getPreviewEnabled(),newInstall:(0,W.SD)("gitlens:install:new",!1),amaBannerCollapsed:this.getAmaBannerCollapsed()}}getPreviewEnabled(){return k.H.get("home.preview.enabled")}getRepositoriesState(){return{count:this.container.git.repositoryCount,openCount:this.container.git.openRepositoryCount,hasUnsafe:this.container.git.hasUnsafeRepositories(),trusted:r.workspace.isTrusted}}async getActiveBranchOverview(){null!=this._discovering&&await this._discovering;let e=this.getSelectedRepository();if(null==e)return;let t="repo"===this._invalidateOverview,i="wip"===this._invalidateOverview,[r,s,o]=await Promise.allSettled([this.getBranchesData(e,t),this.isSubscriptionPro(),this.formatRepository(e)]),{branches:n,worktreesByBranch:a}=(0,H.Ro)(r),h=n.find(e=>"active"===this.getBranchOverviewType(e,a)),l=(0,H.Ro)(s),[u]=ed(this.container,[h],a,l,{isActive:!0,forceStatus:!!t||!!i||void 0});return i&&(this._invalidateOverview=void 0),this._etagFileSystem=e.etagFileSystem,{repository:(0,H.Ro)(o),active:u}}async getInactiveBranchOverview(){let e;null!=this._discovering&&await this._discovering;let t=this.getSelectedRepository();if(null==t)return;let i="repo"===this._invalidateOverview,[r,s,o]=await Promise.allSettled([this.getBranchesData(t,i),this.isSubscriptionPro(),this.formatRepository(t)]),{branches:n,worktreesByBranch:a}=(0,H.Ro)(r),h=n.filter(e=>"recent"===this.getBranchOverviewType(e,a)),l=(0,H.Ro)(s);if(this._overviewBranchFilter.stale.show)for(let t of((0,w.Xn)(n,{missingUpstream:!0,orderBy:"date:asc"}),n)){if(null!=e&&e.length>this._overviewBranchFilter.stale.limit)break;h.some(e=>e.id===t.id)||"stale"===this.getBranchOverviewType(t,a)&&(e??=[]).push(t)}let u=ed(this.container,h,a,l),c=null==e?void 0:ed(this.container,e,a,l);return i||(this._invalidateOverview=void 0),{repository:(0,H.Ro)(o),recent:u,stale:c}}async formatRepository(e){let t=await e.git.remotes().getBestRemotesWithProviders(),i=t.find(e=>e.hasIntegration())??t[0];return{name:e.commonRepositoryName??e.name,path:e.path,provider:i?.provider?{name:i.provider.name,supportedFeatures:i.provider.supportedFeatures,icon:"remote"===i.provider.icon?"cloud":i.provider.icon,url:await i.provider.url({type:c.J.Repo})}:void 0}}_repositorySubscription;selectRepository(e){let t;return null!=e?t=this.container.git.getRepository(e):null==(t=this.container.git.highlander)&&(t=this.container.git.getBestRepositoryOrFirst()),this._repositorySubscription?.dispose(),this._repositorySubscription=void 0,null!=t&&(this._repositorySubscription=new SubscriptionManager(t,e=>this.subscribeToRepository(e)),this.host.visible&&this._repositorySubscription.start()),t}resetBranchOverview(){if(this._repositoryBranches.clear(),!this.host.visible){this._repositorySubscription?.pause();return}this._repositorySubscription?.resume()}subscribeToRepository(e){return r.Disposable.from(e.watchFileSystem(1e3),e.onDidChangeFileSystem(t=>this.onOverviewWipChanged(t,e)),e.onDidChange(t=>{t.changed(p.Z_.Config,p.Z_.Head,p.Z_.Heads,p.Z_.Remotes,p.Z_.PausedOperationStatus,p.Z_.Unknown,p.Ti.Any)&&this.onOverviewRepoChanged(e)}))}onOverviewWipChanged(e,t){e.repository.id===t.id&&this._etagFileSystem!==t.etagFileSystem&&("repo"!==this._invalidateOverview&&(this._invalidateOverview="wip"),this.host.visible&&this.host.notify(X,void 0))}onOverviewRepoChanged(e){if(null!=e){if(this._etagRepository===e.etag)return}else if(this._etag===this.container.git.etag)return;this._invalidateOverview="repo",this.host.visible&&this.notifyDidChangeRepositories()}getSelectedRepository(){return null==this._repositorySubscription&&this.selectRepository(),this._repositorySubscription?.source}_invalidateOverview;_repositoryBranches=new Map;async getBranchesData(e,t=!1){if(t||!this._repositoryBranches.has(e.path)||e.etag!==this._etagRepository){let t=await e.git.worktrees()?.getWorktrees()??[],i=(0,b.PU)(t,{includeDefault:!0}),[r]=await Promise.allSettled([e.git.branches().getBranches({filter:e=>!e.remote,sort:{current:!0,openedWorktreesByBranch:(0,b.vJ)(i)}})]),s=(0,H.Ro)(r)?.values??[];this._etagRepository=e.etag,this._repositoryBranches.set(e.path,{repo:e,branches:s,worktreesByBranch:i})}return this._repositoryBranches.get(e.path)}_integrationStates;_defaultSupportedCloudIntegrations;async getIntegrationStates(e=!1){if(e||null==this._integrationStates){let e=(0,L.x1)(await this.container.integrations.getConfigured(),e=>{if(!(0,a.LT)(e.integrationId))return;let t=a.U4.find(t=>t.id===e.integrationId);return{id:e.integrationId,name:S.Mt[e.integrationId].name,icon:`gl-provider-${S.Mt[e.integrationId].iconKey}`,connected:!0,supports:t?.supports!=null?t.supports:"hosting"===S.Mt[e.integrationId].type?["prs","issues"]:"issues"===S.Mt[e.integrationId].type?["issues"]:[],requiresPro:t?.requiresPro??!1}}),t=await Promise.allSettled(e),i=[...(0,L.x1)(t,e=>(0,H.Ro)(e))];this._defaultSupportedCloudIntegrations??=a.U4.map(e=>({...e,connected:!1})),this._defaultSupportedCloudIntegrations.forEach(e=>{let t=i.find(t=>t.id===e.id);null==t?i.push(e):t.icon!==e.icon&&(t.icon=e.icon)}),i.sort((e,t)=>a.rK.indexOf(e.id)-a.rK.indexOf(t.id)),this._integrationStates=i}return this._integrationStates}_subscription;async getSubscription(e){return null!=e?this._subscription=e:null!=this._subscription?e=this._subscription:this._subscription=e=await this.container.subscription.getSubscription(!0),this._subscription}async isSubscriptionPro(){let e=await this.getSubscription();return null!=e&&(0,P.k0)(e.state)}async getSubscriptionState(e){let t;return e=await this.getSubscription(e),this._etagSubscription=this.container.subscription.etag,t=e.account?.email?(0,o.ML)(e.account.email,34).toString():`${this.host.getWebRoot()??""}/media/gitlens-logo.webp`,{subscription:e,avatar:t,organizationsCount:null!=e?(await this.container.organizations.getOrganizations()??[]).length:0}}notifyDidCompleteDiscoveringRepositories(){this.host.notify(J,{discovering:null!=this._discovering,repositories:this.getRepositoriesState()})}notifyDidChangeRepositoriesCore(){this.host.notify(ee,this.getRepositoriesState())}_notifyDidChangeRepositoriesDebounced=void 0;notifyDidChangeRepositories(e=!1){if(null==this._discovering){if(e){this.notifyDidChangeRepositoriesCore();return}null==this._notifyDidChangeRepositoriesDebounced&&(this._notifyDidChangeRepositoriesDebounced=(0,q.s)(this.notifyDidChangeRepositoriesCore.bind(this),500)),this._notifyDidChangeRepositoriesDebounced()}}notifyDidChangeProgress(){this.host.notify(et,{allCount:this.container.walkthrough.walkthroughSize,doneCount:this.container.walkthrough.doneCount,progress:this.container.walkthrough.progress})}notifyDidChangeConfig(){this.host.notify(K,{previewEnabled:this.getPreviewEnabled(),previewCollapsed:this.getPreviewCollapsed()})}notifyDidChangeLaunchpad(){this.host.notify(er,void 0)}async notifyDidChangeIntegrations(){let[e,t]=await Promise.allSettled([this.getIntegrationStates(!0),this.container.ai.getModel({silent:!0},{source:"home"})]),i=(0,H.Ro)(e)??[],r=i.some(e=>e.connected),s={model:(0,H.Ro)(t)};r&&this.onCollapseSection({section:"integrationBanner",collapsed:!0}),this.host.notify(ei,{hasAnyIntegrationConnected:r,integrations:i,ai:s})}async notifyDidChangeSubscription(e){let t=await this.getSubscriptionState(e);this.host.notify(es,{subscription:t.subscription,avatar:t.avatar,organizationsCount:t.organizationsCount})}notifyDidChangeOrgSettings(){this.host.notify(eo,{orgSettings:this.getOrgSettings()})}async deleteBranchOrWorktree(e,t){let{repo:i,branch:s}=await this.getRepoInfoFromRef(e);if(null!=s){if(s.current&&null!=t&&(!s.worktree||s.worktree.isDefault)){let i=(0,f.km)(t.branchName),o=await r.window.showWarningMessage(`Before deleting the current branch '${s.name}', you will be switched to '${i}'.`,{modal:!0},{title:"Continue"});if(null==o||"Continue"!==o.title)return;await this.container.git.checkout(e.repoPath,i),(0,h.b)({command:"branch",state:{subcommand:"delete",repo:e.repoPath,references:s}})}else if(null!=i&&s?.worktree!=null&&!s.worktree.isDefault){let e=await i.getCommonRepository(),t=await i.git.worktrees?.()?.getWorktree(e=>e.isDefault);if(null==t||null==e)return;let o=await r.window.showWarningMessage(`Before deleting the worktree for '${s.name}', you will be switched to the default worktree.`,{modal:!0},{title:"Continue"});if(null==o||"Continue"!==o.title)return;let n=k.H.get("deepLinks.schemeOverride"),a="string"==typeof n?n:r.env.uriScheme,l={url:`${a}://${this.container.context.extension.id}/link/${T.vk.Repository}/-/${T.vk.Branch}/${encodeURIComponent(s.name)}?path=${encodeURIComponent(e.path)}&action=delete-branch`,repoPath:e.path,useProgress:!1,state:T.rq.GoToTarget};(0,h.b)({command:"worktree",state:{subcommand:"open",repo:t.repoPath,worktree:t,onWorkspaceChanging:async e=>this.container.storage.store("deepLinks:pending",l),worktreeDefaultOpen:"current"}})}}}pushBranch(e){this.container.git.push(e.repoPath,{reference:{name:e.branchName,ref:e.branchId,refType:"branch",remote:!1,repoPath:e.repoPath,upstream:e.branchUpstreamName?{name:e.branchUpstreamName,missing:!1}:void 0}})}mergeTargetCompare(e){return this.container.views.searchAndCompare.compare(e.repoPath,e.branchName,e.mergeTargetName)}async pullRequestCompare(e){let t=await this.getPullRequestFromRef(e);if(t?.refs?.base==null||null==t.refs.head){r.window.showErrorMessage("Unable to find pull request to compare");return}let i=(0,y.tI)(e.repoPath,t.refs);return this.container.views.searchAndCompare.compare(i.repoPath,i.head,i.base)}async pullRequestChanges(e){let t=await this.getPullRequestFromRef(e);if(t?.refs?.base==null||null==t.refs.head){r.window.showErrorMessage("Unable to find pull request to open changes");return}let i=(0,y.tI)(e.repoPath,t.refs);return(0,l.$5)(this.container,{repoPath:i.repoPath,lhs:i.base.ref,rhs:i.head.ref},{title:`Changes in Pull Request #${t.id}`})}async pullRequestViewOnRemote(e,t){let i=await this.getPullRequestFromRef(e);if(null==i){r.window.showErrorMessage("Unable to find pull request to open on remote");return}(0,B.RS)("gitlens.openPullRequestOnRemote",{pr:{url:i.url},clipboard:t})}async pullRequestDetails(e){let t=await this.getPullRequestFromRef(e);if(null==t){r.window.showErrorMessage("Unable to find pull request to open details");return}this.container.views.pullRequest.showPullRequest(t,e.repoPath)}async pullRequestCreate({ref:e,describeWithAI:t,source:i}){let{branch:r}=await this.getRepoInfoFromRef(e);if(null==r)return;let o=await r.getRemote(),n=t?this.container.actionRunners.get("createPullRequest")?.find(e=>e.type===s.do.BuiltIn)?.id:void 0;(0,B.ph)("createPullRequest",{repoPath:e.repoPath,remote:null!=o?{name:o.name,provider:null!=o.provider?{id:o.provider.id,name:o.provider.name,domain:o.provider.domain}:void 0,url:o.url}:void 0,branch:{name:r.name,upstream:r.upstream?.name,isRemote:r.remote},describeWithAI:t,source:i},n)}async worktreeOpen(e){let{branch:t}=await this.getRepoInfoFromRef(e),i=await t?.getWorktree();null!=i&&(0,$.OH)(i.uri)}async switchToBranch(e){let{repo:t,branch:i}=await this.getRepoInfoFromRef(e);null!=i&&u.S_(t,(0,v.iw)(i))}async fetch(e){if(null==e){let e=this.getSelectedRepository();u.hd(e);return}let{repo:t,branch:i}=await this.getRepoInfoFromRef(e);null!=i&&u.hd(t,(0,v.iw)(i))}getBranchOverviewType(e,t){if(e.current||t.get(e.id)?.opened)return"active";let i=e.date?.getTime();if(null!=i){let e=Date.now();if(i>e-ep[this._overviewBranchFilter.recent.threshold])return"recent";if(i<e-ep[this._overviewBranchFilter.stale.threshold])return"stale"}if(e.upstream?.missing)return"stale"}async getPullRequestFromRef(e){let{branch:t}=await this.getRepoInfoFromRef(e);return t?.getAssociatedPullRequest()}async getRepoInfoFromRef(e){let t=this.container.git.getRepository(e.repoPath);if(null==t)return{repo:void 0,branch:void 0};let i=await t.git.branches().getBranch(e.branchName);return{repo:t,branch:i}}};function ed(e,t,i,r,s){let o,n;if(0===t.length)return[];let a=s?.isActive??!1,h=s?.forceStatus?{force:!0}:void 0,l=new Map,u=new Map,p=new Map,d=new Map,m=new Map,w=new Map,b=new Map,f=[];for(let s of t){s.upstream?.missing===!1&&l.set(s.id,s.getRemote());let t=i.get(s.id),c=s.date?.getTime();!0===r&&(u.set(s.id,eb(e,s,o)),p.set(s.id,s.getEnrichedAutolinks()),d.set(s.id,(0,g.GI)(e,s).then(e=>e.value)),w.set(s.id,e.git.branches(s.repoPath).getBranchContributionsOverview(s.ref)),s.current&&b.set(s.id,ev(e,s))),null!=t?m.set(s.id,t.getStatus(h)):!0===a&&(void 0===n&&(n=e.git.status(s.repoPath).getStatus()),m.set(s.id,n)),f.push({reference:(0,v.iw)(s),repoPath:s.repoPath,id:s.id,name:s.name,opened:a,timestamp:c,status:s.status,upstream:s.upstream,worktree:t?{name:t.name,uri:t.uri.toString(),isDefault:t.isDefault}:void 0})}return f.length>0&&function(e,t,i,r,s,o,n,a,h,l){for(let u of t){u.remote=r.get(u.id)?.then(async e=>{if(null!=e)return{name:e.name,provider:e.provider?{name:e.provider.name,icon:"remote"===e.provider.icon?"cloud":e.provider.icon,url:await e.provider.url({type:c.J.Repo}),supportedFeatures:e.provider.supportedFeatures}:void 0}}),u.pr=s.get(u.id);let t=o.get(u.id);u.autolinks=t?.then(e=>eg(e));let p=n.get(u.id);u.issues=p?.then(e=>e?.map(e=>({id:e.id,title:e.title,state:e.state,url:e.url}))??[]),u.wip=ef(e,u,a.get(u.id),i);let d=h.get(u.id);u.contributors=em(e,d),u.mergeTarget=l.get(u.id)}}(e,f,a,l,u,p,d,m,w,b),f}async function eg(e){return null==e?[]:(await Promise.allSettled((0,L.x1)([...e.values()],async e=>{let t=e?.[0];if(null==t)return;let i=await t;if(null!=i)return{id:i.id,title:i.title,url:i.url,state:i.state}}))).map(e=>"fulfilled"===e.status?e.value:void 0).filter(e=>null!=e)}async function em(e,t){if(null==t)return[];let i=await t;return i?.contributors==null?[]:(await Promise.allSettled(i.contributors.map(async e=>({name:e.name??"",email:e.email??"",current:e.current,timestamp:e.latestCommitDate?.getTime(),count:e.commits,stats:e.stats,avatarUrl:(await e.getAvatarUri())?.toString()})))).map(e=>"fulfilled"===e.status?e.value:void 0).filter(e=>null!=e)}async function ev(e,t){let i,r=await (0,m.y1)(e,t,{associatedPullRequest:t.getAssociatedPullRequest()});!r.targetBranch.paused&&r.targetBranch.value&&(i=r.targetBranch.value);let s=i??r.baseBranch??r.defaultBranch;if(null==s)return;let o=e.git.branches(t.repoPath),n=await o.getBranch(s);if(null==n)return;let[a,h,l]=await Promise.allSettled([e.git.commits(t.repoPath).getLeftRightCommitCount((0,C.Xn)(n.name,t.ref,"..."),{excludeMerges:!0}),o.getPotentialMergeOrRebaseConflict?.(t.name,n.name),o.getBranchMergedStatus?.(t,n)]),u=(0,H.Ro)(a),c=null!=u?{ahead:u.right,behind:u.left}:void 0,p=(0,H.Ro)(l);return{repoPath:t.repoPath,id:n.id,name:n.name,status:c,mergedStatus:p,potentialConflicts:(0,H.Ro)(h),targetBranch:n.name,baseBranch:r.baseBranch,defaultBranch:r.defaultBranch}}async function ew(e,t,i){i??=e.launchpad.getCategorizedItems();let r=await i;if(null!=r.error)return;let s=r.items.find(e=>e.url===t.url);if(null==s){if(null!=(r=await e.launchpad.getCategorizedItems({search:[t]})).error)return;s=r.items.find(e=>e.url===t.url)}if(null!=s)return{uuid:s.uuid,category:s.actionableCategory,groups:(0,_._v)(s),suggestedActions:s.suggestedActions,failingCI:s.failingCI,hasConflicts:s.hasConflicts,review:{decision:s.reviewDecision,reviews:s.reviews??[],counts:{approval:s.approvalReviewCount,changeRequest:s.changeRequestReviewCount,comment:s.commentReviewCount,codeSuggest:s.codeSuggestionsCount}},author:s.author,createdDate:s.createdDate,viewer:{...s.viewer,enrichedItems:void 0}}}async function eb(e,t,i){let r=await t.getAssociatedPullRequest({avatarSize:64});if(null!=r)return{id:r.id,url:r.url,state:r.state,title:r.title,draft:r.isDraft,launchpad:ew(e,r,i)}}async function ef(e,t,i,r){if(null==i)return;let[s,o]=await Promise.allSettled([i,r?e.git.status(t.repoPath).getPausedOperationStatus?.():void 0]),n=(0,H.Ro)(s),a=(0,H.Ro)(o);return{workingTreeState:n?.getDiffStatus(),hasConflicts:n?.hasConflicts,conflictsCount:n?.conflicts.length,pausedOpStatus:a}}eu([(0,F.Rm)({args:{0:e=>`${e?.type}, repoPath=${e?.repoPath}, branchId=${e?.branchId}`}})],HomeWebviewProvider.prototype,"openInGraph",1),eu([(0,F.Rm)()],HomeWebviewProvider.prototype,"createBranch",1),eu([(0,F.Rm)({args:{0:e=>e.branchId}})],HomeWebviewProvider.prototype,"mergeIntoCurrent",1),eu([(0,F.Rm)({args:{0:e=>e.branchId}})],HomeWebviewProvider.prototype,"rebaseCurrentOnto",1),eu([(0,F.Rm)()],HomeWebviewProvider.prototype,"startWork",1),eu([(0,F.Rm)({args:{0:e=>e.type}})],HomeWebviewProvider.prototype,"abortPausedOperation",1),eu([(0,F.Rm)({args:{0:e=>e.type}})],HomeWebviewProvider.prototype,"continuePausedOperation",1),eu([(0,F.Rm)({args:{0:e=>e.type}})],HomeWebviewProvider.prototype,"skipPausedOperation",1),eu([(0,F.Rm)({args:{0:e=>e.type}})],HomeWebviewProvider.prototype,"openRebaseEditor",1),eu([(0,F.Rm)({args:{0:e=>e.branchId}})],HomeWebviewProvider.prototype,"createCloudPatch",1),eu([(0,F.Rm)()],HomeWebviewProvider.prototype,"dismissWalkthrough",1),eu([(0,F.Yz)({args:!1})],HomeWebviewProvider.prototype,"onSubscriptionChanged",1),eu([(0,F.Yz)({args:{0:!1}})],HomeWebviewProvider.prototype,"onOverviewWipChanged",1),eu([(0,F.Yz)()],HomeWebviewProvider.prototype,"onOverviewRepoChanged",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`,1:e=>e?.branchId}})],HomeWebviewProvider.prototype,"deleteBranchOrWorktree",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pushBranch",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}, mergeTargetId: ${e.mergeTargetId}`}})],HomeWebviewProvider.prototype,"mergeTargetCompare",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pullRequestCompare",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pullRequestChanges",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pullRequestViewOnRemote",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, upstream: ${e.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pullRequestDetails",1),eu([(0,F.Rm)({args:{0:e=>`${e.ref.branchId}, upstream: ${e.ref.branchUpstreamName}`}})],HomeWebviewProvider.prototype,"pullRequestCreate",1),eu([(0,F.Rm)({args:{0:e=>`${e.branchId}, worktree: ${e.worktree?.name}`}})],HomeWebviewProvider.prototype,"worktreeOpen",1),eu([(0,F.Rm)({args:{0:e=>e.branchId}})],HomeWebviewProvider.prototype,"switchToBranch",1),eu([(0,F.Rm)({args:{0:e=>e?.branchId}})],HomeWebviewProvider.prototype,"fetch",1)}};