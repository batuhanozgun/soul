# DEVELOPMENT LIFECYCLE

**Status:** proposed — WP-021 design candidate; not operational governance until ADR-0003 and WP-021 gates permit implementation/acceptance  
**Scope:** SOUL Development Operating System only; not the eventual reusable SOUL runtime lifecycle  
**Decision path:** proposed ADR-0003  

## 1. Purpose

This specification defines the end-to-end lifecycle by which SOUL development turns new evidence, objectives and completed work into the next controlled unit of development.

The lifecycle exists to preserve two properties simultaneously:

1. development must continue without depending on one chat, one agent's memory or a human acting as hidden scheduler;
2. the system must not confuse **having a result** with **already knowing what substantive work should follow from that result**.

The current Development OS is already strong at exact-target verification, adversarial review, evidence integration and repository continuity. This proposed lifecycle adds an explicit work-selection and pre-build design boundary so that material findings, uncertainty or architecture work are not automatically converted into implementation-shaped work before the correct problem and required reasoning depth are established.

## 2. Protected properties

Any implementation of this lifecycle must preserve:

- repository state rather than chat memory as durable project truth;
- one authoritative current-work home;
- exact artefact/commit binding for verification and review results;
- producer ≠ sole independent verifier;
- independent adversarial review where required;
- research/evidence ≠ architecture decision;
- result integration ≠ result reinterpretation;
- technical decisions are not transferred to the Human Owner merely because they are difficult;
- Human Owner retains vision/value/scope authority and declared owner gates;
- historical decisions/findings/results are not rewritten to simplify the current narrative;
- interruption/restart must remain possible from repository state;
- process complexity must justify itself through identifiable reliability value.

The lifecycle may replace current mechanisms if these properties are preserved by stronger or simpler mechanisms.

## 3. Core separation

The proposed lifecycle separates four questions that may currently be compressed into one work package or one agent trajectory:

1. **What substantive work should happen next?**
2. **What is the correct technical design for that selected work?**
3. **How should the accepted design be realised?**
4. **Did the realised artefact actually satisfy the authoritative requirements and survive independent attack?**

These questions may use different roles because they have different success criteria. Separation is not justified merely by function count; it is justified where completion pressure, authority, evidence duties or success metrics conflict.

## 4. Entry signals

A lifecycle pass begins when canonical project state changes in a way that may require new substantive work. Entry signals include:

- a new owner-authorised objective or scope decision;
- a completed WP;
- an independently verified PASS / FAIL / NOT VERIFIED result;
- an adversarial-review judgement or surviving finding;
- a newly accepted/rejected/superseded architecture decision;
- new evidence that materially changes a current assumption;
- a blocked dependency becoming available or invalid;
- a material implementation observation that invalidates the accepted design.

Not every entry signal requires a new planning session. If an already accepted specification uniquely determines the next responsibility and no substantive choice exists, the transition may remain mechanical.

## 5. Result integration versus work selection

### 5.1 Integrator responsibility

The Integrator's motivation remains narrow: faithfully translate already-issued independent results and authorised decisions into canonical repository state without changing their meaning.

The Integrator may mechanically route to a next responsibility when the accepted specification already determines exactly what happens next and no substantive design/work-selection choice is being made. Examples can include:

- PASS → an already-required fresh adversarial review;
- completed pre-build challenge → return to the already-designated Designer for synthesis;
- accepted technical decision → record its status and activate the already-specified implementation responsibility.

The Integrator must not decide that a material failure necessarily implies repair, that a blocked result necessarily implies implementation, or that a new architecture problem should be scoped in a particular way merely to keep state moving.

### 5.2 Development Planner responsibility

When canonical state introduces a **substantive next-work choice**, responsibility moves to the Development Planner.

`Development Planner` is a SOUL Development OS role name, not a claim of a universal industry title.

**Single motivation:** maintain the best evidence-backed sequence of work toward the accepted project/phase objective.

The Planner determines the **kind and boundary of the next work**, not its technical solution.

It may:

- inspect accepted phase/project objectives, dependencies, current state and new evidence;
- determine whether the next work is direct implementation, technical design, full reframing/investigation, research, decision clarification, roadmap/dependency revision or a real owner-value decision;
- select the minimum required reasoning-depth route;
- define the bounded work objective/problem and required outputs without prescribing the substantive technical design;
- recognise that a previous WP should remain blocked, be superseded or resume under an accepted lifecycle;
- route architecture/value questions through `DECISION_POLICY.md`.

It may not:

- reinterpret verifier/reviewer findings;
- change acceptance criteria merely to restore progress;
- make the technical design it is supposed to route to a Designer;
- implement the work;
- verify or adversarially review the result;
- accept owner-value/foundation decisions on behalf of the Human Owner;
- become an unbounded backlog/product dictator outside accepted roadmap/phase authority.

## 6. Reasoning-depth routes

The lifecycle uses the lightest process that preserves reliability. There is no universal requirement to run all roles for every edit.

### Route 1 — direct implementation

Use only when **all** of the following are true:

- an accepted design, contract or specification already determines intended behaviour;
- the change is local and readily reversible;
- no new authority boundary, state semantics, context/memory semantics, evidence/provenance semantics, verification/evaluation semantics, security/permission boundary or cross-cutting architecture is introduced;
- no durable new role, process, control, service, data model or public interface is introduced;
- no material unresolved assumption or evidence gap determines the solution;
- no active same-mechanism repeated-material-failure/reframing trigger exists;
- expected correctness can be adequately checked with known verification methods.

Typical path:

Development Planner or existing accepted routing → Builder → Verifier → any already-required post-build review → Integrator.

For purely local reversible work already active under a clear WP, a separate Planner execution is not mandatory if no substantive next-work choice exists.

### Route 2 — separate design before implementation

Use when work is material and requires non-trivial design/trade-off, but the problem frame is sufficiently stable and no strong Route-3 trigger exists.

Typical path:

Development Planner → Designer → conditional Researcher and/or pre-build Adversarial Reviewer if required → Designer build-readiness → Builder → Verifier → required post-build Adversarial Reviewer → Integrator.

### Route 3 — full pre-build investigation

Use when any strong trigger is established, including:

- cross-cutting architecture involving authority, state, context, memory, evidence, verification/evaluation, orchestration, security/permissions or self-modification;
- a new durable governance/process/role/control whose failure would be systemic;
- a material finding that invalidates the claimed generality/boundedness of a prior repair;
- repeated material failure in the same mechanism family suggesting the abstraction, representation, layer or work-selection boundary may be wrong;
- material conflicting evidence or unknowns that determine the solution;
- significant irreversibility or high downstream cost;
- a problem likely to have material external prior art that has not been examined and could change the chosen layer/mechanism;
- inability to state meaningful acceptance/evaluation conditions under the current frame.

Typical path:

Development Planner → Designer problem definition → conditional Researcher → independent design perspectives when genuinely useful → fresh pre-build Adversarial Reviewer → Designer synthesis/build-readiness → Builder → Verifier → fresh post-build Adversarial Reviewer when required → Integrator → Development Planner if a new substantive work choice exists.

A strong trigger establishes a minimum route. New evidence may escalate a route. De-escalation requires explicit evidence that the triggering condition does not apply; it is not justified merely by schedule pressure.

## 7. Designer responsibility

**Single motivation:** produce the most defensible build-ready technical design for the selected problem.

The Designer owns problem framing and technical synthesis for the selected work because both optimise design quality rather than implementation completion. A separate permanent `Problem Framer` role is not justified unless future evidence shows this combination creates an independent motivational conflict.

The Designer must:

- describe the actual problem without assuming the current mechanism is the answer;
- identify protected properties and constraints;
- distinguish observed facts, inferences, assumptions and unknowns;
- decide whether additional internal/external evidence is needed;
- consider materially different credible solution layers/alternatives when they exist, including removal/simplification of existing mechanisms;
- incorporate independent challenge rather than merely collect agreement;
- define what the Builder may decide locally and what invalidates/reopens design;
- define verification/evaluation obligations and negative cases where applicable;
- document reopen conditions for architecture-level decisions.

The Designer may not implement material work in the same responsibility when Route 2/3 requires design/build separation.

## 8. Researcher responsibility

The Researcher retains one motivation: establish trustworthy external or empirical evidence needed by a decision.

Research is invoked by an actual evidence gap, not as mandatory browsing ritual.

The Researcher may investigate standards, literature, comparable systems, prior implementations, repository history or experiments. It must preserve source limitations/conflicts.

Research does not choose architecture and cannot silently promote popularity, precedent or retrieved text into SOUL truth.

## 9. Independent perspectives and pre-build challenge

Collective intelligence does not mean unrestricted group conversation or consensus.

When Route 3 needs diversity:

1. freeze the common problem/evidence input available to the independent perspectives;
2. generate materially independent solution analyses before those producers see each other's preferred answer where practical;
3. freeze their outputs;
4. subject the problem/design to a fresh Adversarial Reviewer;
5. let the Designer synthesize the evidence and challenge into one build-ready design.

Do not manufacture a fixed number of agents/options. Independence is useful only when the solution space is genuinely underdetermined or correlated blind spots are material.

### Pre-build Adversarial Reviewer

The existing Adversarial Reviewer motivation is reused rather than inventing a separate permanent critic role.

**Single motivation:** find material failure modes, hidden assumptions and invalid generality claims.

When reviewing a design it attacks the frozen problem/design artefact before implementation. When reviewing a realised artefact later it attacks the exact built target. These are separate fresh executions when both are required.

The pre-build reviewer does not repair the design, implement it or negotiate consensus with the Designer.

## 10. Build-ready design contract

For Route 2/3, implementation does not begin until the design artefact contains the information justified by the work, including:

1. authoritative objective served;
2. problem definition independent of the assumed current mechanism;
3. protected properties/constraints;
4. material assumptions and unknowns;
5. evidence relied on and its limitations;
6. credible alternatives/layers considered, when more than one exists;
7. required pre-build challenge findings and their disposition;
8. selected technical design and rationale;
9. implementation boundary: local Builder freedom versus design-reopen boundary;
10. verification/evaluation plan, including red-capable negative cases where applicable;
11. explicit design reopen conditions;
12. role-context specification: required-now, retrieve-on-trigger, forensic/history sources.

These are information obligations, not twelve mandatory files. Existing WP, ADR and evidence types should carry them where possible. File count is not evidence that reasoning occurred.

## 11. Builder responsibility

**Single motivation:** realise the accepted technical design correctly, completely and observably.

The Builder may make reversible local implementation choices inside the design boundary.

If implementation produces evidence that materially invalidates the design's assumptions, protected-property model or chosen architecture layer, successful Builder behaviour is to stop/reopen the design path. The Builder must not silently redesign the architecture merely to finish the WP.

The Builder may claim `ready for verification`; it may not self-certify material output.

## 12. Verification and post-build adversarial review

The existing exact-target verification model remains load-bearing.

The Verifier determines whether the exact realised artefact satisfies its authoritative specification and evidence obligations. Fresh-context requirements and deterministic checks remain governed by `VERIFICATION_POLICY.md`.

Post-build Adversarial Review remains distinct and attacks failure modes that ordinary specification verification may miss.

A lower number of reviewer findings is not automatically success. The objective is earlier detection and fewer **escaped material failure classes** without weakening the reviewer.

## 13. Reframe versus repair

A material finding does not automatically imply a repair WP.

A finding returns to Development Planner/Designer reframing when evidence establishes at least one of the following:

1. a new material failure reproduces the same protected-property problem by changing only an identity, level or boundary that the prior repair claimed to bound;
2. a fresh review shows the previous repair's claimed safety/generalisation was local to an incomplete represented state space;
3. the next proposed repair mainly adds another exception/state/control branch to preserve the existing abstraction rather than addressing a newly independent defect;
4. root-cause analysis identifies framing, representation, layer selection or work-selection/routing as the system cause;
5. the architecture can no longer state a coherent bounded safety/progress argument without accumulating special cases.

Reframing is not equivalent to rewrite. The reframed result may conclude that a bounded local repair remains the best answer. The requirement is that `repair` becomes an evidence-backed conclusion rather than the routing assumption.

## 14. Technical decision ownership

Every architecture ADR must identify a decision owner.

For a purely technical cross-cutting choice that does not change foundation/value authority, the responsible Designer may be the technical decision owner after required independent review and other declared gates are satisfied.

The Human Owner remains required for foundation changes, project value/scope choices and explicit owner-bound gates.

The Integrator may record an already-authorised decision/status transition but may not supply the technical judgement that accepts it.

This rule prevents technical uncertainty from being transferred to the Human Owner while avoiding an Integrator that becomes an architecture authority.

## 15. Context selection contract

Institutional truth and actor-visible working context are different objects.

Repository history and authoritative evidence remain complete. Each role should receive the smallest high-signal working set sufficient for its responsibility.

WP/context metadata may classify sources as:

- **required-now:** must be read before substantive work for this responsibility;
- **retrieve-on-trigger:** authoritative/evidentiary source that must be loaded when a stated question, conflict, assumption or failure condition arises;
- **forensic/history:** retained for traceability and deep historical analysis but not preloaded by default.

These classes are context-selection metadata only. They do not alter source authority and may not be used to hide a source that the task actually requires.

Role independence can require staged context. For example, a verifier may derive expected results from authoritative requirements before reading producer rationale.

Major `STATE.md`/history compaction is outside this core lifecycle change and requires separate controlled migration/evidence.

## 16. Human Owner boundary

The Human Owner is not the Development Planner, default technical decision-maker, technical verifier, fallback researcher or session scheduler.

The system may ask the Human Owner only when a real owner-dependent branch exists, such as vision, value, scope, irreversible/high-impact choice explicitly assigned by governance or final declared acceptance gate.

The existence of multiple technical options is not sufficient reason to ask the owner when the system can derive the technical answer.

## 17. Work-package implications

A material WP under this lifecycle should identify:

- selected route/depth;
- objective and problem;
- protected properties;
- implementation/design boundary when relevant;
- required-now / retrieve-on-trigger / forensic sources;
- required pre-build and post-build gates;
- reopen/reframe conditions where material.

Simple Route-1 work should not be forced to fill unused architecture-analysis sections.

A WP defines bounded work. It does not become a duplicate lifecycle authority.

## 18. Failure and route recovery

The lifecycle itself must fail closed on ambiguity that affects authority or material work selection, but it must not create an unbounded planning loop.

Examples:

- if route classification is genuinely ambiguous because a missing fact determines whether the work is architectural, open the smallest evidence/investigation step needed to resolve that fact;
- if Planner and accepted specification conflict, use normal source-of-truth/decision governance rather than silently selecting the convenient route;
- if pre-build challenge finds a material design defect, return to design/reframing; do not implement and hope post-build review catches it again;
- if no material concern survives pre-build challenge and replay evidence supports the candidate, proceed rather than researching indefinitely;
- if Builder falsifies a material design premise, reopen design rather than widening implementation authority.

## 19. Development OS effectiveness evaluation

The Development OS itself must be evaluated as a system, not trusted because its controls look disciplined.

Evidence should ask whether the lifecycle:

- surfaces material failure classes before implementation more often;
- reduces repeated same-family repair escapes;
- preserves existing regression guarantees;
- keeps false alarms and unnecessary scope growth bounded;
- keeps context, agent/handoff, time/tool/token and Human Owner burdens justified by reliability value;
- does not merely produce more process artefacts.

Historical blind replay is development/regression evidence only when the process design was derived from the same historical failures.

At least one prospective material trajectory should be evaluated before final Phase-0 acceptance so the next hidden failure class is not already known to the process designer.

## 20. Current WP-020 application

This proposed lifecycle does not decide the answer to F-AR-008.

After this lifecycle is accepted and any required context migration is complete, standing F-AR-008 plus the F-AR-001…008 lineage returns to Development Planner.

Because repeated material findings progressively widened result-control identity/state boundaries, Route 3 is a strong candidate. The Planner must still determine from evidence whether the correct next work is:

- the preserved bounded WP-020 repair;
- broader result-control reframing/redesign;
- targeted research into another control/state layer;
- another authorised path.

If bounded repair is selected after reframing, that is valid. If a broader successor is selected, F-AR-008 must remain an explicit unresolved acceptance obligation and its immutable review evidence must not be rewritten.

## 21. Acceptance and reopen conditions

This lifecycle may become operational only after the WP-021 design target has survived its pre-build challenge/replay gates, been implemented separately, and the implementation has fresh exact-target verification plus post-build adversarial review.

Reopen the lifecycle architecture if evidence shows, among other things:

- Development Planner becomes a hidden owner or unbounded project authority;
- normal low-risk work is forced into costly planning loops;
- route oscillation or handoff overhead creates greater failure burden than it removes;
- Designer/Builder separation does not measurably alter escaped material failures but materially increases cost;
- context selection causes missed required evidence/authority;
- technical ADR ownership creates self-acceptance or circular review;
- the prospective WP-020 lineage pilot escapes another reasonably foreseeable widening of the same frame that the pre-build process claimed to cover;
- a simpler mechanism demonstrates equivalent protection with lower coordination cost.

## 22. Non-goals

This specification does not:

- define SOUL runtime orchestration or Genesis role construction;
- claim that every task needs multiple agents;
- require group consensus/debate;
- make external research mandatory for every task;
- replace exact-target independent verification;
- make the Human Owner a technical arbiter;
- make context summaries authoritative;
- solve F-AR-008 directly;
- accept any ADR or Phase-0 target by itself.
