# ADR-0003 — Development Work Selection and Risk-Proportional Pre-Build Lifecycle

**Status:** proposed — WP-021 design candidate; not accepted  
**Decision class:** Architecture decision  
**Date:** 2026-08-29  
**Decision owner:** provisional WP-021 technical design responsibility; final non-owner technical ADR acceptance authority must be made explicit by the accepted WP-021 decision-policy change before this ADR can become `accepted`  
**Supersedes:** none  
**Superseded by:** none

## Problem

The Phase-0 Development Operating System is strong at repository continuity, exact-target verification, adversarial review, evidence integration and owner/producer separation, but two current architectural choices may create avoidable execution/closure bias for material work:

1. `VERIFICATION_POLICY.md` currently turns FAIL into a bounded Builder repair WP and NOT VERIFIED into investigation/repair routing as part of mechanical result integration;
2. `ROLE_MODEL.md` combines technical design and implementation in one `Designer / Builder` responsibility.

`REASONING_POLICY.md` already tells material sessions to test framing, necessity, alternatives, falsifying evidence and root causes. The issue is therefore not simply missing instructions. Those checks may occur under a responsibility whose success is still shaped by finishing an already repair-shaped job, and the workflow may select `repair` before an independent responsibility asks what kind of work is actually justified.

The recent F-AR-001…F-AR-008 lineage is evidence for investigating this problem because repair scope repeatedly widened from one locator/head boundary to broader identity/state boundaries after later adversarial review. It is not proof that workflow bias is the sole cause; difficult state/concurrency controls can legitimately require iterative discovery.

The architecture decision is therefore whether Phase-0 should retain the current combined/routing model, strengthen it only with more reasoning instructions, or introduce explicit work-selection plus risk-proportional pre-build design separation while preserving existing post-build assurance.

## Scope

This decision governs the **Development Operating System used to build SOUL**.

It affects:

- substantive next-work selection after new evidence/results;
- role/motivation placement for planning, design and implementation;
- risk-proportional pre-build lifecycle;
- result-integration versus next-work boundary;
- reframe-versus-repair routing;
- minimum context-selection contract needed by the lifecycle;
- effectiveness evaluation expectations for the Development OS.

It does not decide:

- SOUL runtime/Genesis orchestration or role architecture;
- the substantive repair for F-AR-008;
- a major `STATE.md` history-compaction design;
- databases, vector stores, retrieval engines, model providers or agent frameworks;
- foundation vision/definition/non-negotiables;
- whether any existing ADR is accepted.

## Constraints

- repository state must remain sufficient for fresh-session continuation;
- `COLD_START.md` remains the single bootstrap sequencing authority unless separately and validly superseded;
- historical verifier/reviewer evidence and exact-target bindings must remain immutable in meaning;
- producer work cannot self-certify material output;
- research is evidence, not architecture authority;
- owner value/scope authority must remain distinct from technical derivation/verification;
- new process complexity has a burden of proof;
- routine reversible work must not be forced through full architecture ceremony;
- design independence must not be implemented as unrestricted multi-agent consensus/debate;
- implementation of this decision cannot precede the WP-021 pre-build challenge/replay gates.

## Options considered

### Option A — Keep the current Development OS lifecycle unchanged

Continue using the combined `Designer / Builder`, current reasoning policy and independent post-build verification/review. Material FAIL/NOT VERIFIED results continue to route directly into bounded repair/investigation work.

**Benefits**
- no migration/coordination cost;
- current system is restartable and already catches failures through independent review;
- avoids adding another planning role/handoff.

**Costs / risks**
- preserves the questioned repair-shaped routing assumption;
- keeps frame selection, design and implementation under one completion trajectory;
- relies on post-build reviewers to discover abstraction/frame misses that may have been detectable before implementation;
- does not create an explicit system-level owner for `what work should happen next?` when the answer is not already mechanically predetermined.

### Option B — Keep current roles/routing but strengthen `REASONING_POLICY.md`

Add more mandatory prompts/checklists requiring Designer/Builder and Integrator to ask whether a finding should be reframed before repair.

**Benefits**
- smallest apparent change;
- little additional coordination;
- builds on an existing canonical reasoning policy.

**Costs / risks**
- current policy already contains frame/necessity/root-cause/repeated-repair checks, so more prose may duplicate rather than change behaviour;
- keeps the same completion motivation and result-routing authority;
- conflicts with the existing principle that recurring mechanically representable failures should migrate away from prompt reminders;
- risks more cold-start/context load and ritualised overthinking without a changed responsibility boundary.

### Option C — Split Designer from Builder but retain current result routing

Material design is produced in a separate responsibility before implementation, while FAIL/NOT VERIFIED integration continues to create bounded repair-shaped work.

**Benefits**
- directly attacks design/implementation completion-pressure conflict;
- smaller than introducing work-selection responsibility;
- preserves current result integration model.

**Costs / risks**
- work can still be framed as `repair` before Designer sees it;
- Integrator remains partly a hidden project planner because result integration selects the substantive next-work type;
- addresses only one of the two identified bias locations.

### Option D — Explicit work-selection plus design/build separation and risk-proportional pre-build lifecycle

Introduce a Development Planner responsibility for substantive next-work selection; preserve mechanical Integrator transitions only when the accepted specification already uniquely determines the next step; split material technical design from implementation; use three reasoning-depth routes; use existing Adversarial Reviewer motivation for fresh pre-build challenge where risk justifies it; retain exact-target post-build assurance.

**Benefits**
- attacks both routing-level and implementation-level closure bias;
- makes `repair` a conclusion rather than automatic default;
- preserves a light path for routine work;
- turns existing reasoning-policy principles into lifecycle placement rather than adding prompt text;
- gives the whole Development OS lifecycle one visible architecture model;
- keeps the Human Owner out of routine technical sequencing.

**Costs / risks**
- introduces a new Planner responsibility and more potential handoffs;
- may create route oscillation, over-planning or a hidden project dictator;
- pre-build review can add latency and correlated-agent failure if independence is poorly implemented;
- lifecycle/context metadata can become duplicate authority if not bounded;
- requires migration and effectiveness evidence.

**Decision candidate:** chosen, subject to WP-021 pre-build adversarial challenge and replay/evaluation.

### Option E — Multi-agent consensus council before every material build

Have several agents discuss the problem/design until they converge on a common plan.

**Benefits**
- superficially increases perspective count;
- may expose some disagreements early.

**Costs / risks**
- consensus does not establish correctness or independence;
- homogeneous agents can correlate, anchor and converge on shared errors;
- high coordination/context cost;
- conflicts with the principle that functions/roles need necessity evidence, not more-agent aesthetics.

**Rejected.** Independent generation/challenge is preferred when diversity is actually needed.

## Evidence

### Internal observed evidence

- `development/01_governance/REASONING_POLICY.md` already requires frame inspection, necessity testing, credible alternatives, falsifying evidence and immediate+system root-cause analysis for material work. Therefore the candidate change is not justified as merely adding missing reasoning questions.
- `development/01_governance/VERIFICATION_POLICY.md` currently routes FAIL to bounded repair and NOT VERIFIED to bounded investigation/repair as part of result transition.
- `development/01_governance/ROLE_MODEL.md` currently combines Designer and Builder.
- F-AR-005, F-AR-006/F-AR-007 and F-AR-008 show successive material discoveries after prior exact-target PASS/review loops, widening the result-control problem boundary. This supports examining pre-build framing/work-selection but does not prove causality.
- `os-architect` records earlier observed `çerçeve körlüğü` / work-completion bias: repairs can inherit the existing mechanism's frame, missing questions can remain invisible inside the frame, and completion incentives can suppress stepping back.
- `keel-research` explicitly separates function necessity from role motivation and treats single-motivation role placement as falsifiable rather than automatic.

### External primary/authoritative prior art

- NASA Systems Engineering Handbook, Decision Analysis: decision need/criteria are established before evaluating alternatives; alternative generation can use prior systems/literature; analysis method intensity should fit the mission/system/decision complexity; uncertainty that can change ranking should be considered. Source: NASA Systems Engineering Handbook §6.8 / NASA public handbook pages.
- NASA NPR 7123.1C Decision Analysis Process: technical decision processes identify criteria, alternatives, analyse alternatives and select among them using relevant data/uncertainty across the system lifecycle.
- CMU SEI QAW/ATAM guidance: architecture/quality risks and trade-offs can be analysed before full development; ATAM iterates candidate architecture → analysis/risk mitigation → refined architecture.
- Anthropic, `Effective context engineering for AI agents` (2025): context is a finite attention resource with diminishing returns; effective agent context aims for the smallest high-signal sufficient set.
- Anthropic, `Demystifying evals for AI agents` (2026): without rigorous evals, teams can fall into reactive loops where one fix creates another; capability/regression evals make behaviour changes visible.
- OpenAI, `How evals drive the next chapter in AI for businesses` (2025): evaluation discipline is framed as Specify → Measure → Improve; fuzzy goals should become explicit measurable expectations before claiming improvement.

These sources are analogous design evidence, not proof that the exact SOUL lifecycle is correct.

## Decision

Subject to WP-021 pre-build gates, adopt the architecture specified by proposed `development/02_architecture/DEVELOPMENT_LIFECYCLE.md`:

1. distinguish faithful result integration from substantive next-work selection;
2. introduce a bounded Development Planner motivation for selecting/sequencing the next unit and minimum reasoning depth when a substantive choice exists;
3. retain mechanical routing where an accepted specification already uniquely determines the next responsibility;
4. split material technical Designer from Builder so design quality and implementation completion are not the same success objective;
5. retain Researcher, Verifier, Adversarial Reviewer, Integrator and Human Owner with their current motivations unless evidence justifies later change;
6. use Route 1 / Route 2 / Route 3 reasoning depths with explicit strong escalation triggers rather than one heavy process for all work;
7. use fresh pre-build adversarial challenge for high-risk design rather than relying exclusively on post-build discovery;
8. treat `repair` as a possible outcome of work selection/reframing, not the automatic consequence of a negative independent result;
9. require a bounded build-ready design contract and explicit Builder reopen boundary for material work;
10. make non-owner architecture ADR technical decision ownership explicit; Integrator records authorised decisions but does not supply technical judgement;
11. treat institutional truth and actor-visible context separately, using required-now / retrieve-on-trigger / forensic-history selection metadata without altering source authority;
12. require historical replay as development/regression evidence and a prospective material trajectory before final Phase-0 acceptance to evaluate whether added process is actually load-bearing.

This decision does not become operational merely because this ADR is written. WP-021 explicitly gates governance implementation behind fresh design challenge and replay/evaluation.

## Rationale

Option D is the only considered option that addresses both observed locations of possible execution bias without replacing strong existing assurance:

- Option B changes instructions but not responsibility/route placement despite existing instructions already containing the relevant questions.
- Option C separates design/build but still lets result integration select `repair` before the design responsibility begins.
- Option A accepts the current repair progression without testing a plausible process cause.
- Option E adds coordination without preserving useful independence.

The proposed model is intentionally risk-proportional. NASA and SEI prior art support analysing alternatives/architecture risk before realisation while tailoring decision-analysis depth to decision complexity rather than applying maximal process universally. The design also retains post-build verification because earlier reasoning does not prove realised correctness.

## Consequences and new risks

### Positive

- negative findings no longer automatically define their own repair-shaped next work;
- material design can be challenged before implementation consumes another build/review loop;
- Builder success is faithful realisation or correct design-reopen, not silent redesign to finish;
- whole lifecycle becomes visible as one architecture model;
- existing reasoning policy becomes more structurally placed rather than expanded with more reminders;
- routine work retains a direct route;
- Human Owner remains outside routine technical orchestration.

### Costs / new risks

- Development Planner may become a bottleneck or hidden owner;
- route classification can oscillate or over-escalate;
- additional handoffs can create coordination failures;
- pre-build challenge may correlate with Designer reasoning if context/model separation is weak;
- design artefacts may become duplicate sources of truth;
- context selection can omit necessary evidence;
- added process may not reduce escaped material failures enough to justify its cost.

Mitigation is part of the decision: bounded Planner authority, mechanical transitions where deterministic, explicit route triggers, exact source-of-truth separation, independent challenge, effectiveness evaluation and rollback.

## Rejected alternatives

Options A, B, C and E are rejected as the target architecture for the reasons above, but their lower-complexity properties remain useful comparison baselines. If replay/prospective evidence shows Option D adds cost without meaningful reliability benefit, this ADR must be reopened and a simpler option reconsidered.

## Verification required

Before implementation:

1. fresh pre-build adversarial review of the exact lifecycle/ADR design target;
2. historical replay/development evaluation under a frozen protocol with later findings hidden from work trajectories;
3. design synthesis resolving any surviving material challenge before governance implementation.

After implementation:

1. fresh exact-target verification of every then-current WP-000 acceptance criterion;
2. deterministic lifecycle/route fixtures where semantics permit;
3. regression of historical cold-start, exact-target result and independent integration properties;
4. fresh post-build adversarial review focused on Planner authority, route over-escalation/oscillation, design/build leakage, Integrator planning leakage, context omission, owner orchestration and coordination burden;
5. prospective material use/effectiveness evaluation before final Phase-0 acceptance.

## Reopen conditions

Reopen this ADR if:

- pre-build review/replay provides no material evidence that the added separation changes failure detection or design quality;
- Development Planner becomes a hidden owner, architecture dictator or mandatory bottleneck;
- routine work cannot reliably stay on the light route;
- design/build separation materially increases cost without reducing escaped same-family material failures;
- context-selection contracts cause required evidence/authority to disappear from actor view;
- technical decision ownership becomes circular/self-accepting;
- a simpler mechanism demonstrates equivalent protected properties;
- the first prospective material trajectory escapes another reasonably foreseeable widening of the same frame the pre-build process claimed to cover;
- later SOUL architecture provides a stronger general lifecycle mechanism that should supersede this development-only scaffold.
