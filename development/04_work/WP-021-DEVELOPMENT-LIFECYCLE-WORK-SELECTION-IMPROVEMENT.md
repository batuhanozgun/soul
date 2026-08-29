# WP-021 — Development OS Lifecycle and Work-Selection Improvement

**Status:** active — design-only stage; governance implementation not yet authorised by this WP stage  
**Owner role:** designer/builder operating in a design-only responsibility under the current role model  
**Decision authority:** owner-directed Phase-0 Development OS strengthening; cross-cutting architecture changes require proposed ADR-0003 and independent review under `DECISION_POLICY.md`; no foundation change, policy implementation before the declared pre-build gates, independent self-verification, ADR acceptance, PR #22/#1 merge, Phase acceptance or Phase 1 authority  
**Development branch:** `phase0/development-os` for canonical work routing; candidate design/build must occur on a separate WP-021 branch  
**Fallback checkpoint:** `checkpoint/phase0-pre-lifecycle-v2-c4ebef9` at `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Blocked unresolved work:** `WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`; F-AR-008 remains standing and unresolved

## Objective

Strengthen the Phase-0 Development Operating System so that material evidence or failures do not automatically become repair-shaped implementation work before the system independently determines the correct next unit of work, required reasoning depth and technical design path.

The target improvement must preserve the working properties already achieved: repository-based continuity, exact-target evidence bindings, independent verification and adversarial review, canonical state authority, controlled decision/change history, recoverable fresh-session work, and the Human Owner boundary.

This WP must establish and evaluate the target lifecycle before implementing it into current governance. The current Development OS is not to be rewritten in place merely because the proposed model appears plausible.

## Problem

Recent Phase-0 history shows a repeated pattern in which a material independent finding is integrated and then routed directly into a bounded repair WP. The current `VERIFICATION_POLICY.md` explicitly encodes FAIL → repair and NOT VERIFIED → investigation/repair routing. The current `ROLE_MODEL.md` also combines technical design and implementation in one `Designer / Builder` responsibility.

The existing `REASONING_POLICY.md` already requires frame checks, necessity tests, alternatives, falsification and root-cause analysis. The observed weakness is therefore not simply missing reasoning advice. The deeper question is whether some of that reasoning occurs too late or under the wrong completion motivation, and whether project routing itself prematurely chooses `repair` before asking what kind of work is actually justified.

The F-AR-001 through F-AR-008 lineage is evidence for investigating this hypothesis, not proof that it is the sole cause. Hard state/concurrency problems can legitimately require iteration. The proposed process must therefore demonstrate value rather than adding ceremony by assumption.

## Owner direction

On 2026-08-29 the Human Owner directed a full Development OS improvement study, explicitly authorised the assistant to decide when planning was mature enough to enter execution, and required two simultaneous design perspectives:

1. determine what Development OS should do to improve the quality of work selection, problem framing, research, design and execution;
2. introduce any improvement without losing the working properties, history, continuity, evidence, safe restart or owner boundaries already achieved.

Changing, removing or rewriting current mechanisms is allowed when it is genuine improvement. `Do not break` means do not leave the Development OS unable to preserve those required properties; it does not mean preserve current file shapes or workflow merely because they exist.

The planning/research record is preserved outside SOUL authority in the scratch branch of `batuhanozgun/keel-research`. It is evidence/input only and is not architecture truth.

## Current stage — design before implementation

WP-021 begins under the **current** role/governance model. Proposed new responsibilities do not become authoritative merely because this WP discusses them.

The initial responsibility is an existing `designer/builder` role constrained to **design-only** work. It may create proposed architecture/specification/evidence artefacts on the WP-021 candidate branch, but it must not modify the existing governance policies to make the new lifecycle operational until the pre-build challenge and replay gates below are satisfied.

This avoids the bootstrap error of pretending unaccepted new roles already exist while still separating design from later implementation in practice.

## Scope

- derive one explicit canonical Development OS lifecycle model covering work-selection, reasoning-depth routing, problem/design/build boundaries, independent pre-build challenge, independent post-build assurance, result integration and return to next-work selection;
- test whether a distinct work/program planning motivation is necessary to select the correct next unit of work from accepted project/phase objectives and evidence rather than from implementation momentum;
- test and, if justified, specify separation of technical Designer and Builder motivations for material work;
- preserve Researcher, Verifier, Adversarial Reviewer, Integrator and Human Owner strengths unless evidence justifies a change;
- define risk/materiality-based routes so routine reversible work does not pay the cost of full architecture analysis;
- define evidence-based reframe-vs-repair conditions so `repair` becomes a conclusion rather than an automatic routing assumption;
- define the minimum pre-build information contract for material work: objective, problem, protected properties, assumptions/unknowns, evidence, alternatives where credible, challenge result where required, selected design, implementation boundary, verification plan and reopen conditions;
- clarify technical ADR decision ownership without converting the Human Owner into technical verifier or the Integrator into architecture decision-maker;
- define a minimal selective-context contract sufficient for the lifecycle while postponing major `STATE.md`/history compaction to a separate later WP;
- create historical blind-replay/development evaluation against selected pre-finding repository snapshots;
- define the prospective WP-020/F-AR-008 lineage as an effectiveness pilot after lifecycle adoption;
- preserve a rollback/fallback path to the pre-change Development OS checkpoint.

## Non-scope

- repairing F-AR-008 in this WP;
- changing, weakening, deleting or reinterpreting F-AR-001 through F-AR-008 or their historical PASS / Requires-repair exact-target bindings;
- modifying PR #22 or treating WP-018 PASS as certification of changed material;
- major `STATE.md` history compaction or a new retrieval/database/vector-store architecture;
- choosing SOUL product/runtime agent architecture, memory architecture, orchestration technology, model provider or implementation framework;
- treating multi-agent discussion or consensus as independent evidence;
- adding permanent roles merely because more functions can be named;
- changing foundation vision/definition/non-negotiables without a separate foundation decision path;
- accepting ADR-0000, ADR-0001, ADR-0002 or proposed ADR-0003;
- merging PR #22/PR #1, accepting Phase 0 or beginning Phase 1.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first.

For the initial design-only responsibility, Step 3 required-now reading is:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. this WP;
3. `development/03_plan/ROADMAP.md`;
4. `development/01_governance/ROLE_MODEL.md`;
5. `development/01_governance/VERIFICATION_POLICY.md`;
6. `development/01_governance/DECISION_POLICY.md`;
7. `development/01_governance/CHANGE_POLICY.md`;
8. `development/03_plan/PR_GATE.md` and `PHASE_GATE.md`;
9. `development/04_work/WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md`;
10. `development/04_work/WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md`;
11. `development/04_work/WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md`;
12. `development/04_work/WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`;
13. the exact adversarial findings that led to F-AR-005, F-AR-006/F-AR-007 and F-AR-008;
14. the owner-directed exploratory planning records in `batuhanozgun/keel-research` scratch only as non-authoritative evidence/input.

Conditional/retrieve-on-trigger sources include predecessor-repository evidence and external primary sources needed to resolve a concrete design question. Historical session records are forensic sources unless a specific trace is required.

## Inputs and dependencies

- canonical Phase-0 checkpoint `c4ebef9e58a4a94edce22ebbb94d94414dffd92c` and immutable fallback branch;
- standing WP-019 **Requires repair** judgement and F-AR-008;
- current WP-000 criteria and Phase-0 objective;
- existing `REASONING_POLICY.md` frame/necessity/alternative/falsification/root-cause requirements;
- owner-directed Development OS improvement investigation;
- comparative evidence from SOUL history, predecessor repositories and external prior art.

## Design-stage outputs

Before governance implementation may begin, the design stage must freeze:

- proposed `development/02_architecture/DEVELOPMENT_LIFECYCLE.md`;
- proposed `ADR-0003` covering work selection, design/build separation and risk-proportional pre-build lifecycle;
- function-to-role/motivation justification including negative justification for any new permanent role;
- Development Planner authority/non-authority and handoff boundaries if retained;
- three reasoning-depth routes and escalation/de-escalation conditions;
- reframe-vs-repair conditions;
- build-ready design information contract;
- technical ADR decision-owner rule;
- minimal selective-context contract;
- proposed WP-000 acceptance-criteria delta;
- exact historical replay protocol/holdout boundaries and evaluator criteria;
- rollback/fallback requirements;
- a design-only session handoff to fresh pre-build adversarial review.

## Pre-build gates before governance implementation

No modification of current operational governance policies to enact the candidate lifecycle may begin until all of the following exist:

1. a frozen proposed lifecycle/ADR design on an exact candidate commit;
2. a fresh separate adversarial review of that **design**, not of implementation;
3. historical replay/development evaluation using exact pre-finding snapshots with later findings hidden from work trajectories;
4. an explicit synthesis of surviving design findings and replay results;
5. a build-ready design updated for those results;
6. no unresolved material design finding that would make implementation premature.

Historical replay is development/regression evidence only because the candidate process was derived partly from known historical failures. It cannot by itself prove generalisation.

## Candidate lifecycle properties to test

The design must show, not merely claim, that:

- faithful result integration and substantive next-work selection are distinct responsibilities;
- a material independent finding does not automatically become a repair;
- the lightest safe reasoning route is used for routine work;
- high-risk/cross-cutting/repeated-failure work receives stronger pre-build framing and challenge;
- design and implementation completion motivations are separated when material;
- Builder can stop/reopen design when implementation falsifies a design premise rather than silently redesigning;
- research remains evidence and cannot silently become architecture truth;
- independent perspectives are generated before synthesis when diversity is needed rather than through consensus pressure;
- Human Owner is not turned into routine scheduler, technical verifier or architecture arbitrator;
- Integrator cannot reinterpret results or become hidden project planner;
- context selection reduces actor load without hiding institutional truth or breaking independence;
- the process has an explicit effectiveness evaluation and rollback path.

## Historical replay protocol — minimum

Use isolated repository snapshots before later findings were known, including at minimum the starts of WP-011, WP-014 and WP-017.

For each snapshot compare a baseline trajectory approximating the then-current combined Designer/Builder method with a candidate pre-build trajectory. Later findings are withheld from both trajectories and held only by the evaluator. Use multiple fresh trials where the execution environment permits it.

Primary question: did the candidate surface a later material failure class before implementation?

Secondary measures: validity/false alarms, unnecessary scope growth, context loaded, agent/tool/token/time cost, owner interventions, handoff/coordination failures and whether the candidate formed a more general protected-property model.

The evaluator criteria must be frozen before candidate results are inspected. More analysis or more artefacts is not a success metric.

## Required implementation after pre-build gates

If the design survives its pre-build gates, a **separate implementation-only responsibility** may update the operational governance artefacts required by the accepted candidate design. That producer must not silently redesign the lifecycle while implementing it. Material design invalidation returns to the design stage.

The implementation target then requires fresh exact-target verification, separate evidence integration and fresh post-build adversarial review before any architecture/Phase acceptance.

## Prospective effectiveness pilot

After the core lifecycle and later context-surface work are independently accepted, the standing WP-020/F-AR-008 lineage becomes the first prospective material use of the new discipline.

The new work-selection responsibility must decide from evidence whether the right next work is a bounded repair, broader result-control reframing/redesign, research into another control/state layer, or another authorised path. The answer is not predetermined by this WP.

A subsequent material reviewer finding is not automatically proof that the lifecycle failed. However, if the next escaped finding is another reasonably foreseeable widening of the same identity/state/frame boundary that the pre-build process claimed to cover, treat that as strong evidence that the intended countermeasure failed and reopen Development OS design before Phase-0 acceptance.

## Acceptance criteria

1. **Preservation:** activation and later design work preserve F-AR-008, PR #22, all historical exact-target results and the `c4ebef9...` fallback checkpoint without reinterpretation.
2. **Lifecycle visibility:** one proposed canonical lifecycle model makes the whole Development OS work loop visible without duplicating detailed role/verification semantics.
3. **Work-selection separation:** substantive next-work selection is distinct from result integration and implementation.
4. **Design/build motivation separation:** material technical design and implementation have distinct success objectives and a defined reopen path.
5. **Risk proportionality:** routine work can take a light route while explicit strong triggers require deeper pre-build work.
6. **Reframing discipline:** repeated/material findings can force frame/representation/layer/work-selection reconsideration; repair is not an automatic routing default.
7. **Research discipline:** research is conditional on evidence gaps and remains evidence rather than decision authority.
8. **Independent pre-build challenge:** high-risk designs can be attacked in fresh context before implementation without turning review into consensus debate.
9. **Integrator boundary:** independent results are preserved/integrated mechanically and substantive next-work choice is outside Integrator authority.
10. **Owner boundary:** technical work selection/design/verification do not become Human Owner orchestration duties.
11. **Technical decision ownership:** non-owner architecture decisions have an explicit technical decision owner and independent-review requirement.
12. **Context contract:** role-visible context is bounded and recoverable without creating a second truth hierarchy; major state compaction remains separately controlled.
13. **Effectiveness evidence:** historical replay protocol/results exist as development evidence and a prospective WP-020 lineage pilot is required before final Phase-0 acceptance.
14. **Complexity burden:** added role/handoff/process complexity has explicit necessity and failure-cost justification; absence of measured benefit requires simplification/reopening.
15. **Safe implementation gate:** operational governance is not modified to enact the new lifecycle before frozen design, fresh design challenge and replay synthesis are complete.
16. **Fresh assurance:** any implemented governance target receives fresh exact-target verification and fresh adversarial review; producer claims do not certify it.
17. **No false completion:** WP-021 does not accept an ADR, resolve F-AR-008, merge PR #22/#1, accept Phase 0 or begin Phase 1.

## Required verification and review

### Design stage

- fresh pre-build adversarial reviewer against the exact frozen lifecycle/ADR candidate;
- replay/evaluation evidence under the frozen protocol;
- design synthesis after findings/evidence, with material changes producing a new exact design target for challenge as required.

### Implementation stage

- fresh separate verifier against the exact implemented Development OS target, including every current and newly added WP-000 acceptance criterion;
- separate Integrator evidence/state transition;
- fresh separate post-build adversarial reviewer;
- fresh integration and repeat loop for any surviving material finding;
- ADR/owner/PR/Phase gates remain distinct.

## Evidence obligations

Persist enough evidence to distinguish:

- observed process failure from inferred cause;
- historical replay result from generalisation claim;
- design rationale from independent challenge;
- current-policy behaviour from proposed-policy behaviour;
- lower context load from lost information;
- fewer findings from weaker review;
- increased process cost from measured reliability benefit.

## Risks

- adding a Planner role that becomes an unbounded project dictator or hidden Human Owner;
- moving execution bias from Builder into Planner rather than eliminating it;
- every task escalating into a costly architecture process;
- pre-build reviewers and Designers anchoring on each other and creating consensus collapse;
- policy/file proliferation that records ceremony without changing behaviour;
- implementation silently redesigning the unaccepted lifecycle;
- context selection hiding evidence or breaking verifier independence;
- replay contamination being presented as proof of generalisation;
- transition complexity recreating owner orchestration;
- losing current cold-start/result/evidence guarantees while trying to improve reasoning quality.

## Completion state

Active — **design-only stage**. WP-020 is unresolved and blocked from execution while WP-021 determines and evaluates the correct Development OS lifecycle. No new lifecycle architecture is accepted and no operational governance implementation has begun.

## Handoff

Exact next responsibility after activation: continue the current design-only responsibility on a separate WP-021 candidate branch. Produce the frozen lifecycle specification, proposed ADR-0003, replay protocol and design handoff. Then stop implementation and route the exact design target to a fresh pre-build adversarial reviewer. Do not execute WP-020, modify PR #22, implement the proposed governance into current policies, self-verify, accept an ADR, accept Phase 0 or begin Phase 1.
