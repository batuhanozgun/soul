# WP-022 — WP-021 Development Lifecycle Pre-Build Adversarial Review

**Status:** active — fresh separate adversarial reviewer required  
**Owner role:** adversarial reviewer  
**Decision authority:** independently attack the frozen WP-021 design candidate and issue findings/judgement; no design repair, governance implementation, ADR acceptance, replay-result synthesis, PR #28 merge, WP-020 execution, Phase acceptance or Phase 1 authority  
**Development branch:** `phase0/development-os` for canonical routing  
**Reviewed design PR:** #28 — draft, unaccepted, unmerged  
**Exact design target:** `acf6ddc621c644e5a0960e3382b25928d2518041`  
**Exact design base:** `6fca29474ab97d22e363108b8be6438456316e01`  
**Parent:** `WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md`  
**Result-control key:** `WP-022 / adversarial reviewer / acf6ddc621c644e5a0960e3382b25928d2518041 / attempt 1`

## Objective

Independently attack the **design before implementation** and determine whether the proposed Development OS lifecycle is suitable to proceed into historical replay/synthesis and later implementation, requires design revision, or cannot yet be assessed.

The purpose is not to find a quota of issues. The review must try to disprove the candidate's necessity, authority boundaries, proportionality, independence model and claimed preservation of current working guarantees.

## Reviewed target

The exact reviewed target is PR #28 commit:

`acf6ddc621c644e5a0960e3382b25928d2518041`

It adds exactly five design/evidence/session artefacts relative to canonical base `6fca294...` and intentionally does **not** modify operational governance policies.

Target artefacts:

- `development/02_architecture/DEVELOPMENT_LIFECYCLE.md`;
- `development/02_architecture/decisions/ADR-0003-DEVELOPMENT-WORK-SELECTION-AND-RISK-PROPORTIONAL-PREBUILD-LIFECYCLE.md`;
- `development/05_evidence/WP-021-FUNCTION-ROLE-MOTIVATION-ANALYSIS-2026-08-29.md`;
- `development/05_evidence/WP-021-HISTORICAL-BLIND-REPLAY-PROTOCOL-2026-08-29.md`;
- `development/07_sessions/SESSION-0037-PHASE0-WP021-LIFECYCLE-DESIGN.md`.

The reviewer must verify live PR/head/base/file scope before relying on these claims.

## Required reading and independence order

Enter through canonical `development/03_plan/COLD_START.md` and complete Steps 1–2 first.

Within Step 3, preserve the following order to reduce producer anchoring.

### A. Derive the attack model before producer rationale

Read first:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. `development/04_work/WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md`;
3. `development/03_plan/ROADMAP.md`;
4. current canonical `ROLE_MODEL.md`, `WORKING_PROTOCOL.md`, `REASONING_POLICY.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`, `VERIFICATION_POLICY.md`;
5. `SOURCE_OF_TRUTH.md`, `COLD_START.md`, `PR_GATE.md`, `PHASE_GATE.md`;
6. exact PR #28 metadata/diff/head/base/scope.

Before reading the producer's function/motivation analysis or SESSION-0037 rationale, record an expected attack matrix from the authoritative Phase-0 objective and WP-021 criteria.

### B. Inspect the design itself

Then read:

7. proposed `DEVELOPMENT_LIFECYCLE.md` at exact target;
8. proposed ADR-0003 at exact target.

Attempt to break the design from the frozen specification before reading the producer's supporting analysis.

### C. Read producer evidence/rationale last

Only after the initial attack model and first-pass design attack are frozen, read:

9. `WP-021-FUNCTION-ROLE-MOTIVATION-ANALYSIS-2026-08-29.md`;
10. `WP-021-HISTORICAL-BLIND-REPLAY-PROTOCOL-2026-08-29.md`;
11. `SESSION-0037-PHASE0-WP021-LIFECYCLE-DESIGN.md`;
12. predecessor/external sources only when needed to test a concrete claim; do not inherit the producer's synthesis as truth.

## Required attack surface

The reviewer must at least attempt to disprove the following claims/properties. This is not a fixed finding quota.

### 1. Development Planner necessity

- Can the work-selection function be absorbed more simply by deterministic routing, Designer, or another existing role without recreating execution bias?
- Does the proposed Planner have a genuinely distinct success motivation, or is the split architectural aesthetics?
- Is the `substantive next-work choice` boundary precise enough to prevent opportunistic authority movement?

### 2. Planner authority containment

- Can Planner become hidden Human Owner, backlog dictator, architecture decision-maker or acceptance-criteria editor?
- Can Planner suppress/delay valid work indefinitely by repeatedly escalating analysis?
- Can a lower-authority finding force project/roadmap scope change without the correct decision path?

### 3. Route correctness and liveness

- Can Route 1/2/3 classification oscillate, deadlock or always escalate?
- Are Route-3 strong triggers too broad for normal material work?
- Can schedule pressure or agent preference silently de-escalate a strong trigger?
- Is there a bounded recovery when evidence needed for route classification is unavailable?

### 4. Designer / Builder separation

- Is design/implementation motivation conflict real enough to justify a permanent split?
- Does combining problem framing + technical design inside Designer reproduce the same conflict one level earlier?
- Can Builder still silently redesign by calling a material choice `local implementation`?
- Are reopen conditions enforceable enough to matter?

### 5. Pre-build review independence

- Does using the same Adversarial Reviewer role before and after build create correlated assumptions or state contamination?
- Does the proposed independent-perspectives sequence reduce anchoring, or simply multiply same-model agreement?
- Can the Designer neutralise reviewer findings through synthesis without independent control?

### 6. Integrator boundary

- Does the lifecycle actually remove substantive work-selection from Integrator, or leave wording loopholes where `mechanical` routing still embeds a design decision?
- Can Integrator or Planner reinterpret PASS / FAIL / NOT VERIFIED / review findings?
- Can result integration still automatically manufacture a repair-shaped task through another artefact?

### 7. Technical ADR ownership

- Does `Designer may be technical decision owner after independent review` create producer self-acceptance or circular authority?
- Who decides that review conditions are satisfied?
- Can Integrator accidentally become the accepting authority?
- Is the current decision-policy ambiguity actually resolved by the candidate, or only renamed?

### 8. Context selection safety

- Can `required-now / retrieve-on-trigger / forensic` metadata hide evidence a role does not know it needs?
- Who is authorised to classify context and how is a wrong classification detected?
- Can selective context break verifier/reviewer independence or cold-start sufficiency?
- Does the design create a second source-of-truth hierarchy by accident?

### 9. Replay/effectiveness validity

- Is the historical replay too contaminated by lessons that generated the new process to justify implementation at all?
- Are baseline and candidate arms comparable enough to learn anything?
- Can the candidate win merely because it uses more agents/tokens?
- Are evaluator criteria capable of distinguishing generic risk language from genuinely surfacing a hidden failure class?
- Is prospective evidence sufficiently specified to keep Phase 0 from accepting a process on self-confirming evidence?

### 10. Preservation / rollback

- Can the candidate lifecycle be implemented without losing exact-target history, result discoverability, fresh-session restart and owner boundaries?
- Is fallback to `c4ebef9...` meaningful once later canonical history exists, or does rollback require a more explicit forward-restoration plan?
- Does blocking WP-020 while evaluating Development OS create an unbounded meta-work escape from resolving F-AR-008?

### 11. Complexity burden

- Does the design add more handoff/coordination failure modes than the failure class it aims to prevent?
- Are any proposed permanent functions better represented as mechanical gates instead of agents?
- Can the lifecycle be made materially simpler while protecting the same properties?

### 12. Generality

- Is the candidate overfitted to the F-AR-005/006/008 result-control lineage?
- Would the same lifecycle improve a materially different Phase-1/2 architecture task, or are its strongest mechanisms specific to repair-heavy control work?

## Disproof standard

A reviewer finding must include:

- exact claim/property challenged;
- evidence from the target/governance or a reproducible failure path;
- lost property/impact;
- severity with rationale;
- a real disproof attempt;
- result: stands | disproved | not-verifiable.

Generic preferences such as `too complex`, `more agents are risky`, or `Planner may be bad` are not material findings without a concrete failure path or evidence.

## Outputs

Produce exactly the independent design-review evidence required by the existing review discipline:

- one adversarial review artefact under `development/06_reviews/` bound to exact target `acf6ddc...`;
- one fresh reviewer session/handoff under `development/07_sessions/`;
- a dedicated evidence PR whose scope contains only those two authorised files.

The reviewer does not modify PR #28 or the candidate design.

## Judgement

Use one of:

- **Suitable to proceed to replay/synthesis** — no material design finding survives; this is not architecture acceptance or permission to implement before the replay/synthesis gate;
- **Requires design revision** — at least one material design finding survives;
- **Not assessable** — evidence/target/authority is insufficient to issue a defensible judgement.

Low findings may still require explicit disposition before implementation depending on their impact.

## Result publication and transition

Publish the review artefact + reviewer handoff in a dedicated evidence PR with exact target/key binding. Do not repair while publishing.

After publication, a separate Integrator validates scope/freshness and integrates the review result unchanged. A surviving material finding routes WP-021 back to design/synthesis rather than automatically authorising governance implementation.

The historical replay/evaluation remains separately required even if this review finds no material issue.

## Acceptance criteria for this review activity

1. exact PR #28 target/base/scope are independently revalidated;
2. attack model is derived before producer rationale is read;
3. every required attack-surface class receives a genuine disproof attempt or a documented reason it is not applicable;
4. findings cite concrete evidence/failure paths rather than stylistic preferences;
5. Planner necessity and simpler-mechanism alternatives are explicitly attacked;
6. authority/liveness/owner boundaries are explicitly attacked;
7. replay contamination/fairness and prospective-evidence claims are explicitly attacked;
8. reviewer does not repair, implement or accept ADR-0003;
9. judgement is bound only to exact target `acf6ddc...`;
10. output PR contains only the authorised review + session files;
11. no Phase/WP-020/PR #22/PR #28 acceptance or merge is performed.

## Handoff

Exact next responsibility: **fresh separate adversarial reviewer**. After review publication, stop for a separate Integrator. Do not combine review with design revision, replay synthesis, governance implementation or architecture acceptance.
