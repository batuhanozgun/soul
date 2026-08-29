# PRE-BUILD ADVERSARIAL REVIEW — WP-021 DEVELOPMENT LIFECYCLE DESIGN

**Reviewer session:** `SESSION-0039`  
**Reviewed repository:** `batuhanozgun/soul`  
**Reviewed PR:** `#28` — draft, open, unaccepted, unmerged  
**Reviewed commit:** `acf6ddc621c644e5a0960e3382b25928d2518041`  
**Reviewed base:** `6fca29474ab97d22e363108b8be6438456316e01`  
**Result-control key:** `WP-022 / adversarial reviewer / acf6ddc621c644e5a0960e3382b25928d2518041 / attempt 1`  
**Authoritative specification:** `WP-000`, `WP-021`, `WP-022`, current foundation and governance  
**Date:** 2026-08-29

## Independence boundary and exact-target precheck

This section and the expected attack matrix below were recorded before reading
the target lifecycle, proposed ADR-0003, producer function/role analysis,
producer replay protocol or SESSION-0037 rationale.

Observed live PR metadata at the precheck:

- PR #28 was open and draft, base branch `phase0/development-os`, base commit
  `6fca29474ab97d22e363108b8be6438456316e01`, head branch
  `work/wp021-development-lifecycle-improvement`, and head commit
  `acf6ddc621c644e5a0960e3382b25928d2518041`;
- GitHub reported one commit, 1,200 additions, zero deletions and five changed
  files;
- direct Git diff confirmed that all five paths were additions and exactly
  matched the target list in WP-022;
- no current operational governance policy was in the exact target diff.

## Expected attack matrix frozen before producer rationale

| Attack class | Protected claim/property | Disproof probe fixed before target reading | Evidence needed to reject the attack |
|---|---|---|---|
| Planner necessity | A distinct Planner motivation is necessary and simpler deterministic or existing-role routing is insufficient. | Remove Planner as an actor; test whether explicit routing criteria plus Designer-owned technical selection preserve the same boundaries. Look for work-selection outputs that are mechanical enough to encode without a new role. | A concrete conflict-of-motivation analysis plus duties that cannot be safely absorbed or mechanised, with explicit cost/failure comparison. |
| Planner authority | Planner cannot become owner, architect, acceptance editor or backlog dictator. | Feed an ambiguous material finding, missing evidence and schedule pressure; trace who may alter objective, scope, criteria, priority and stop state. Test indefinite analysis/escalation. | Explicit non-authorities, bounded output contract, escalation destination and liveness/appeal path that preserve owner and technical decision boundaries. |
| Route correctness | Routes are deterministic enough to avoid oscillation, deadlock, universal escalation and preference-based de-escalation. | Construct borderline materiality, unavailable evidence, repeated low findings and one strong trigger mixed with routine work. Replay classification twice from identical facts. | Stable precedence, strong-trigger monotonicity, evidence-unavailable state, bounded recovery and auditable rationale. |
| Designer/Builder split | Separation changes completion motivation without merely moving the same conflict into Designer. | Let framing evidence change during design and let build expose an unstated material choice; test whether Designer can prematurely optimise for buildability and Builder can relabel redesign as local implementation. | Distinct success conditions, build-ready contract, enforceable materiality/reopen rules and no producer self-certification. |
| Pre-build independence | Challenge reduces anchoring rather than multiplying correlated agreement. | Use the same underlying model/role across pre- and post-build review; test shared assumptions, rationale leakage and Designer-controlled synthesis of findings. | Fresh-context ordering, explicit same-model limitation, immutable finding disposition, and independent control over whether material findings block implementation. |
| Integrator boundary | Integration is faithful mechanics, while substantive next-work selection remains elsewhere. | Issue FAIL, NOT VERIFIED and a review finding that supports several credible next actions; trace whether Integrator can manufacture or choose repair-shaped work. | Integrator output is result-preserving only and hands an explicit unresolved decision surface to an authorised selector without semantic routing. |
| Technical ADR ownership | A non-owner technical decision can be accepted without producer self-acceptance or Integrator authority leakage. | Make Designer the proposer/decision owner and ask who determines independent-review sufficiency, resolves findings and changes ADR status. | Separate acceptance conditions and actor, deterministic gate evidence, conflict path and no circular approval. |
| Context selection | Reduced context does not hide institutional truth or create a second authority hierarchy. | Misclassify decisive evidence as forensic or retrieve-on-trigger when the actor cannot know the trigger; test verifier/reviewer independence and cold-start recovery. | Authoritative metadata owner, fail-closed retrieval triggers, correction mechanism, minimum role context and source-of-truth precedence. |
| Replay validity | Historical replay can estimate pre-build value without leakage, resource bias or self-confirming evaluation. | Trace commit visibility, prompt/context contamination, evaluator access, baseline fidelity, token/agent imbalance, outcome-sensitive rubric changes and multiple-trial variance. | Frozen snapshots/inputs/rubric, credible blind boundary, comparable budgets, repeated trials, false-positive/cost measures and explicit limits on generalisation. |
| Preservation/rollback | Adoption preserves exact-target history, current result controls, fresh-session restart and owner boundaries; rollback remains executable after later history. | Simulate partial rollout, failed implementation and post-rollout canonical commits; attempt fallback without rewriting history or losing later evidence. | Forward restoration/migration plan, invariant checks, disable path and exact checkpoint semantics beyond a bare branch pointer. |
| Meta-work liveness | WP-021 cannot indefinitely displace unresolved WP-020/F-AR-008. | Let review/replay/synthesis stay inconclusive or repeatedly reopen; search for time/evidence/decision bounds and an explicit blocked outcome. | Bounded gate states and owner-visible stop/escalation criteria that neither falsely resolve F-AR-008 nor permit endless process redesign. |
| Complexity burden | Added roles, handoffs and artefacts earn their failure and coordination cost. | Compare against a smaller lifecycle using explicit gates and temporary responsibility separation; count new handoffs, state transitions and failure points. | Necessity-by-function, measurable effectiveness/cost thresholds and a simplification/reopen rule when benefit is absent. |
| Generality | The lifecycle is not overfit to result-control repair lineage. | Apply its contracts to a greenfield Phase-1 definition task and a materially different analytical/design task with no prior failure finding. | Domain-neutral protected properties, route examples beyond repair work and prospective evidence requirements. |
| Governance compatibility | Proposed lifecycle cannot silently supersede current authority before acceptance. | Look for normative present-tense claims that operational roles may execute before ADR/replay/synthesis/implementation gates, or duplicated semantics that conflict with current policies. | Explicit proposal status, precedence rules, implementation mapping and fresh assurance after operational change. |

## First-pass design attack

The following candidate failure paths were frozen after reading only the exact
lifecycle specification and proposed ADR-0003, before producer evidence or
SESSION-0037. They are hypotheses to disprove, not final findings.

1. **Technical-decision acceptance is circular or unowned.** Lifecycle lines
   262–272 make the responsible Designer the technical decision owner after
   review, while forbidding the Integrator from supplying acceptance judgement.
   ADR-0003 line 6 explicitly defers final non-owner acceptance authority to the
   future accepted WP-021 decision-policy change. No actor or rule in the frozen
   design says who independently determines that review findings/gates are
   satisfied and authorises the ADR status transition. A Designer can therefore
   become producer and accepter, or the ADR can remain permanently proposed.
   Disproof sought from producer material: an already-frozen non-circular status
   transition and finding-disposition authority.
2. **Context classification can hide evidence with no detection path.**
   Lifecycle lines 274–290 define three context classes and prohibit hiding
   required sources, but do not assign authority for classification, require a
   manifest of omitted sources, or define how a fresh role discovers that an
   unknown trigger was omitted. A WP author can classify disconfirming evidence
   as forensic; a fresh reviewer following required-now material cannot know to
   retrieve it. Disproof sought: an explicit independent classification/checking
   mechanism that is part of the frozen candidate rather than future work.
3. **Rollback is asserted but not designed.** ADR-0003 line 216 names rollback
   as mitigation, while the lifecycle contains no rollback/disable procedure,
   migration invariant, or forward-restoration semantics. A checkpoint ref alone
   cannot safely undo operational governance after later canonical evidence and
   state commits exist. Disproof sought: an executable forward-restoration plan
   in the frozen design or an explicit pre-implementation output/gate that blocks
   build readiness until it exists.
4. **Planner can change canonical work scope through an undefined boundary.**
   Lifecycle lines 85–94 allow Planner to define the next objective/problem and
   recognise that a prior WP should remain blocked, be superseded or resume, but
   only prohibit authority outside accepted roadmap/phase boundaries. Superseding
   an owner-directed or active WP can itself alter accepted scope/priority. The
   design does not state which such transitions are technical routing, which need
   an ADR/WP change, and which return to Human Owner authority. Disproof sought:
   a concrete decision table or authority-preserving escalation rule.
5. **Route classification has no convergence criterion.** Strong Route-3
   triggers are intentionally broad; de-escalation needs evidence, ambiguity
   opens investigation, and the only liveness guard is the qualitative phrase
   `supports the candidate` / `proceed rather than researching indefinitely`
   (lifecycle lines 318–326). Repeated missing or mixed evidence can therefore
   produce unbounded Planner/investigation loops without a representable terminal
   not-assessable/owner-decision state. Disproof sought: bounded evaluation or a
   terminal routing state with authority and evidence criteria.
6. **The distinct permanent Planner may be more mechanism than the design has
   yet earned.** The design states a unique motivation but does not itself show
   why a bounded work-selection function plus deterministic route gate could not
   be assigned to an existing Designer execution with fresh-context separation.
   Disproof sought from producer analysis/replay: concrete conflict evidence and
   a lower-complexity comparison showing the permanent role changes outcomes.
7. **Pre-build independence can be consumed by Designer-controlled synthesis.**
   Lifecycle lines 185–207 freeze perspectives/review but return all synthesis to
   the Designer. It does not define an immutable finding-disposition gate or who
   prevents the Designer from labelling a material finding resolved in its own
   revised design. Disproof sought: exact-target re-review/finding acceptance
   rules outside the Designer's sole judgement.

## Producer evidence challenge

Producer material was read only after commits `38e5ee8` and `a5f7836` froze the
expected matrix and first-pass attack.

- The function/motivation analysis correctly treats Planner necessity as the
  main unresolved hypothesis and explicitly says replay must falsify it
  (`WP-021-FUNCTION-ROLE-MOTIVATION-ANALYSIS...`:222–226). It does not close the
  hypothesis. The replay protocol has no no-Planner/Designer-owned-selection
  ablation, so it cannot produce the evidence its own function analysis asks for.
- The replay protocol has useful safeguards: exact historical snapshots, future
  findings withheld, fresh executions, frozen outputs, per-trial evidence,
  comparable resource declarations, contamination checks, cost accounting and
  explicit non-generality. Those controls disprove a blanket claim that the
  replay is merely informal retrospective storytelling.
- The same protocol nevertheless changes Planner, design/build separation,
  pre-build review, optional Researcher/alternative generation and execution
  count in one candidate arm. It therefore tests the package, not the causal
  necessity of a permanent Planner.
- The producer explicitly lists circular technical ownership and context hiding
  as concerns requiring independent attack (SESSION-0037:77–91), but neither the
  lifecycle nor the supporting records add a closing control.
- No producer artefact supplies rollback semantics beyond ADR-0003's statement
  that rollback is a mitigation. The candidate's exact five-file search found no
  disable, restoration or rollback procedure.

## Required attack-surface disposition

| WP-022 attack class | Result | Evidence-backed disposition |
|---|---|---|
| 1. Planner necessity | **stands as F-AR-010** | A distinct work-selection function is plausible, but the proposed experiment cannot distinguish a permanent Planner from Designer-owned or mechanically gated alternatives. |
| 2. Planner authority containment | partially survives, no separate finding | The accepted phase/roadmap, explicit non-authorities and current change policy constrain Planner. The exact `supersede/resume` decision-class boundary remains underspecified, but the more immediate independent-gate leak is captured by F-AR-009. |
| 3. Route correctness/liveness | limitation, no separate material finding | Strong-trigger monotonicity and smallest-evidence-step recovery are explicit. No quantitative convergence rule exists; replay must record blocked/ambiguous events and implementation needs representable terminal outcomes. |
| 4. Designer/Builder separation | design claim survives first-pass attack | Distinct motivations, a build-ready contract and material reopen boundary are explicit. Effectiveness remains unverified pending replay; no concrete authority failure separate from F-AR-009 was established. |
| 5. Pre-build independence | **stands in part as F-AR-009** | Fresh executions and frozen outputs reduce anchoring, but Designer-controlled disposition/synthesis lacks a separate current-target closure gate after a material finding or revision. |
| 6. Integrator boundary | disproved | Integrator is limited to faithful, uniquely prescribed transitions and cannot choose repair/design where substantive choice exists. No contradictory target rule was found. |
| 7. Technical ADR ownership | **stands as F-AR-009** | The candidate acknowledges final acceptance authority is deferred to the very policy change that ADR-0003 would authorise; no non-circular actor/rule closes it. |
| 8. Context selection safety | **stands as F-AR-011** | Authority, manifest, completeness checking and unknown-trigger recovery are absent from the proposed minimum contract. |
| 9. Replay/effectiveness validity | **stands in part as F-AR-010** | Snapshot/blinding/cost controls are substantive, but bundled treatment prevents the declared role-necessity inference. Future-information leakage remains a per-trial check and is not yet verifiable because exact arm prompts do not yet exist. |
| 10. Preservation/rollback | **preservation disproved; rollback stands as F-AR-012** | Exact target adds only five proposed artefacts and leaves operational/historical state unchanged. The promised rollback mitigation itself has no frozen semantics. |
| 11. Complexity burden | **stands as F-AR-010** | Costs are measured, but no experiment isolates whether the new permanent role earns its own coordination burden. |
| 12. Generality | not verified, accurately bounded | The candidate explicitly limits historical replay and requires prospective evidence. The planned first prospective use remains in the same result-control lineage, so it cannot alone establish broad domain transfer; no current generality claim was promoted to verified truth. |
| Governance compatibility / false completion | disproved for the frozen target | PR #28 is proposal-only, modifies no operational governance, preserves F-AR-008/WP-020 and accepts/merges nothing. |

## Findings

### F-AR-009 — Technical design acceptance and material finding disposition are circular or unowned

- **Claim:** The frozen lifecycle has no non-circular authority that can determine
  a material pre-build finding is resolved and authorise a purely technical ADR
  status transition. The responsible Designer can become producer, synthesiser,
  finding disposer and decision owner, while the Integrator is correctly barred
  from supplying judgement and the Human Owner is correctly not the default
  technical arbiter.
- **Evidence:** `DEVELOPMENT_LIFECYCLE.md`:185–207 freezes independent challenge
  but returns synthesis to Designer; lines 209–226 require finding disposition
  inside the build-ready contract; lines 262–272 make the responsible Designer
  technical decision owner after review and bar Integrator judgement. ADR-0003
  line 6 says final non-owner acceptance authority must be made explicit by the
  future accepted WP-021 decision-policy change. ADR lines 222–228 require review
  and synthesis but no fresh exact-target reviewer after material revision and no
  actor that rules a finding satisfied. Current `DECISION_POLICY.md`:16–19
  requires independent review before architecture acceptance but likewise does
  not name an accepting technical authority.
- **Failure path:** The reviewer issues a material finding against exact target A.
  Designer produces target B, records its own disposition, declares build-ready
  and, as technical decision owner, treats review/gates as satisfied. Integrator
  can only record the already-authorised transition, so it cannot correct the
  self-acceptance. Alternatively every actor respects its prohibition and no one
  can authorise the ADR, producing a permanent governance deadlock.
- **Impact:** Producer/independent-assurance separation, explicit authority,
  exact-target freshness and no-false-completion are lost, or liveness is lost.
- **Severity:** **medium — material.** The current target is still proposal-only,
  so no live authority has yet escaped. But this is a build-blocking design gap in
  the exact acceptance path the candidate is meant to establish.
- **Disproof attempt:** Searched all five target artefacts for decision-owner,
  acceptance, status-transition, challenge, synthesis, material-change and
  re-review rules; compared them with current Decision/PR gates. The proposal
  recognises circularity as a reopen condition and producer concern, but provides
  no closing actor or mandatory fresh-target challenge rule.
- **Result:** **stands**.

### F-AR-010 — The replay bundles multiple changes and cannot establish that a permanent Planner is necessary

- **Claim:** The declared replay cannot falsify or justify the candidate's most
  consequential role hypothesis because its candidate arm changes several
  mechanisms simultaneously and has no ablation for work selection without a
  permanent Development Planner.
- **Evidence:** Function/motivation analysis lines 222–226 names Planner as the
  main unresolved hypothesis and requires review/replay to attack it. Replay
  protocol lines 53–76 compares one current combined Designer/Builder arm with a
  candidate arm that adds Planner-style selection, separate Designer framing,
  conditional Researcher work, independent alternatives, a fresh pre-build
  reviewer and Designer synthesis. Lines 100–110 permit the candidate more
  executions while only recording that added cost. Directional success at
  175–188 is defined for the whole bundle; it has no Option-C/no-Planner or
  mechanical-gate arm.
- **Failure path:** Candidate trials outperform baseline because a pre-build
  reviewer, extra execution budget or design/build separation catches a failure.
  Synthesis attributes sufficient value to Option D and operationalises a
  permanent Planner, although the same outcome was achievable with a smaller
  lifecycle. Later, Planner adds bottleneck/authority/handoff failures with no
  causal reliability benefit.
- **Impact:** The complexity-burden criterion and necessity discipline fail; a
  durable authority-bearing role can be admitted on evidence that does not test
  its necessity.
- **Severity:** **medium — material.** A permanent Planner changes authority,
  canonical routing and coordination across all later development work. Cost
  accounting does not repair causal non-identification.
- **Disproof attempt:** Looked for a factorial/ablation arm, an explicit
  Designer-owned work-selection comparison, a deterministic-gate comparison or
  a rule preventing Planner adoption from bundled improvement. Options A–E are
  discussed conceptually, and later evidence may remove Planner, but the frozen
  protocol runs only baseline versus the full Option-D package.
- **Result:** **stands**.

### F-AR-011 — Context-selection metadata can hide required evidence without detection

- **Claim:** The minimal context contract defines labels but not who may assign
  them, what complete candidate-source inventory is classified, or how a fresh
  role detects a needed source whose trigger is itself absent from working
  context.
- **Evidence:** `DEVELOPMENT_LIFECYCLE.md`:274–290 distinguishes institutional
  truth from actor context and defines `required-now`, `retrieve-on-trigger` and
  `forensic/history`. The only safety rule is that labels may not hide a source
  the task actually requires. Lines 300–314 require WPs to carry the labels but
  specify no classification authority, manifest, independent completeness check,
  correction path or fail-closed unknown-trigger behaviour. ADR-0003:121 and
  206–216 lists context metadata duplication/omission as a risk but no stronger
  control appears in the target.
- **Failure path:** A WP producer or Planner classifies disconfirming evidence as
  forensic, or uses a retrieve trigger whose premise is documented only in that
  omitted evidence. A fresh Designer/Verifier/Reviewer follows canonical
  cold-start plus required-now readings, never observes the trigger and proceeds
  with an incomplete frame. The repository remains complete, so the omission is
  invisible rather than an authority conflict that `SOURCE_OF_TRUTH.md` can
  resolve.
- **Impact:** Cold-start sufficiency, independent review, evidence completeness
  and context safety can fail while the session remains procedurally compliant.
- **Severity:** **medium — material.** Context selection is proposed as a
  cross-cutting role contract and WP-021 criterion 12 requires recoverability
  without a second truth hierarchy. A prose prohibition does not supply that
  property.
- **Disproof attempt:** Searched the lifecycle/ADR/evidence for classifier,
  manifest, correction, omission detection and role-minimum rules. Staged
  producer-rationale ordering is a valid independence example but does not solve
  unknown omitted evidence. Major compaction being deferred does not fill this
  minimum lifecycle gap.
- **Result:** **stands**.

### F-AR-012 — Rollback is claimed as mitigation but has no design contract

- **Claim:** The candidate claims rollback as part of its risk mitigation while
  freezing no rollback/disable/forward-restoration semantics for an operational
  governance migration.
- **Evidence:** WP-021 requires rollback/fallback requirements among design-stage
  outputs (`WP-021`:106–122) and preserves checkpoint `c4ebef9...`. ADR-0003:216
  says rollback is part of the decision's mitigation. Across the exact five
  target files, the only related statements are generic migration references,
  the checkpoint/base, and later reopen conditions; there is no invariant list,
  disable path, partial-rollout recovery, forward-restoration rule or treatment
  of canonical evidence/state created after adoption.
- **Failure path:** Operational governance is implemented and later creates
  canonical WPs, decisions and evidence under the new lifecycle. A failure then
  triggers `rollback`. Resetting to the checkpoint would discard later truth;
  leaving later commits while reverting only some policies can create mixed-role
  and mixed-state semantics. With no contract, the recovery agent must invent an
  architecture during the incident.
- **Impact:** Recoverability, historical preservation, one-authority semantics
  and safe interruption/restart are not demonstrated.
- **Severity:** **medium — material.** Nothing has been rolled out yet, but the
  omission violates a declared design-stage output and makes later implementation
  premature.
- **Disproof attempt:** Searched all five exact target artefacts for rollback,
  fallback, restore, disable and migration. ADR-0003's mitigation assertion was
  the only rollback claim; a branch checkpoint proves historical availability,
  not a safe forward recovery after subsequent canonical work.
- **Result:** **stands**.

## Disproved and bounded attacks

- **Exact target / preservation:** PR #28 remained draft/open at initial live
  inspection with exact head/base and five-file scope. The target adds proposal,
  evidence and session files only; it does not implement governance, modify
  historical findings or resolve WP-020/F-AR-008.
- **Integrator result reinterpretation:** no target rule lets Integrator soften a
  result or choose substantive repair when multiple next-work paths exist.
- **Universal heavy process:** Route 1 has restrictive all-of conditions and a
  separate Planner execution is optional when no substantive choice exists.
  Whether real routing remains proportionate is evaluation work, not a currently
  proven defect.
- **Consensus-as-independence:** the candidate explicitly rejects consensus
  councils, freezes independent outputs first and states same-model limitations.
- **Replay as proof of generalisation:** the protocol explicitly refuses this
  claim and requires prospective evidence. Exact future trial prompts and
  contamination outcomes remain not-verifiable until replay execution.
- **Owner as scheduler/technical arbiter:** the candidate repeatedly prohibits
  this transfer. F-AR-009 concerns the missing technical acceptance authority,
  not a recommendation to send it to the Human Owner by default.

## Limitations

- This is a design review, not execution of the 18-trial replay protocol and not
  verification of a later implementation.
- GitHub live metadata establishes current PR state/head/base/scope but not the
  semantic quality of the five target artefacts; those were inspected directly
  from the exact Git commit.
- Same-model fresh-context review reduces producer anchoring but is not true
  model-level independence.
- Route-frequency, false-alarm, token/cost and coordination claims remain
  empirical unknowns until a corrected protocol is executed.

## Overall judgement

**Requires design revision.** F-AR-009 through F-AR-012 stand at
medium/material severity against exact target
`acf6ddc621c644e5a0960e3382b25928d2518041`.

The candidate has real strengths: it preserves the current repository/evidence
boundary, separates substantive selection from result integration, makes process
depth proportional, adds pre-build challenge without consensus theatre and
defines a credible exact-snapshot replay skeleton. Those strengths do not close
the four design gaps above.

Operational governance implementation is therefore premature. The separate
Integrator must preserve this judgement unchanged and route WP-021 back to
design/synthesis. A changed lifecycle/ADR/protocol target is materially fresh and
requires the current independent finding-resolution path; this reviewer performs
no repair, replay synthesis, implementation, ADR acceptance, PR #28 merge,
WP-020 execution, Phase acceptance or Phase-1 work.
