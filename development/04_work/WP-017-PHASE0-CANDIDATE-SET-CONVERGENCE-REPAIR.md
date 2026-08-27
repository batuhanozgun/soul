# WP-017 — Phase 0 Candidate-Set Convergence Repair

**Status:** builder repair published — fresh separate verifier activation pending
**Owner role:** designer/builder
**Decision authority:** bounded repair of F-AR-006 and F-AR-007 within existing foundation/governance and unchanged WP-000 acceptance criteria; architecture-level choices must follow `DECISION_POLICY.md`; no independent verification, adversarial-review self-approval, canonical independent-result integration, ADR acceptance, PR #19/#1 merge, Phase acceptance or Phase 1 authority
**Development branch:** `phase0/development-os`
**Rejected material target:** draft/unmerged PR #19 exact commit `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Repair branch:** `codex/wp017-candidate-set-convergence-repair`
**Repair PR:** #22 — `WP-017: bound candidate-set convergence and restore result precedence`
**Exact new material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Exact new material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Proposed verification routing:** WP-018 spec prepared on builder-close branch;
not canonically active until a fresh separate Integrator validates and activates it
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Prior repair package:** `WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md`
**Verification activity:** WP-015 — **PASS** for exact target `2f5508c1d6941e951d494bb2a700ef861860431d`, activation `5368abd0f0c9a846f89120be44c19b1f1b1825d9` and binding `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`
**Adversarial re-review activity:** WP-016 — **Requires repair**; F-AR-006 medium/material and F-AR-007 low/evidence-model correctness stand
**Reviewer evidence:** `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-2f5508c1-2026-08-27.md`
**Reviewer evidence PR:** #21, head `c2c44604ea1694bd84e34bed950e38efe557ff71`, integrated evidence-only as `276132a8ad3bcaa5263aba725f6f006019f79287`
**Completed review result-control key:** `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Completed review activation/binding:** `94bcc9bf9d0352bde67459635a6073c7e65171e2` / `91db45818f324a1c1aef4dd16d48e40591a3f4e1`

## Objective

Produce the smallest coherent material repair that gives the pending
independent-result control bounded progress across successive candidate PR
identities under one unchanged active result-control key, while preserving
direct validation and routing of every current-valid result. Reconcile the
executable producer model with the already normative current-valid-result
precedence rule and add negative regression coverage for the mixed states that
exposed F-AR-007.

The builder must derive the repair architecture. This routing WP does not
preselect repository/key-wide admission, batching, rate/budget control,
candidate-set containment, trust, freeze, a platform primitive or another
mechanism. It also does not decide whether PR #19 is amended, superseded or
otherwise related to the new target. The output must leave one explicit new
exact material target and a safe, reviewable activation and independent-result
path.

## Exact findings preserved

### F-AR-006 — Rotating to fresh PR identities resets per-candidate containment and restores unbounded denial

**Result:** stands.
**Severity:** medium — material.

The current repair converges only for one identity `(repository, PR number,
active key)`. A lower-authority source can publish the same invalid same-WP
claim through fresh PR identities, causing each identity to restart exact-head
resolution and movement containment. Repository-level independent work can
therefore be denied through an unbounded sequence of candidate identities even
though each individual PR converges.

### F-AR-007 — The executable routing model lets an invalid candidate outrank a current-valid result

**Result:** stands.
**Severity:** low — evidence/model correctness.

Canonical target prose says one current-valid result wins routing, but the
producer decision-table model checks uncontained invalid candidates first. In
mixed current-valid/uncontained-invalid states it returns resolution or
containment instead of `INTEGRATOR_RESULT`. The prose remains normative; the
executable evidence/model is inconsistent with it.

The full claims, evidence, failure paths, impacts, disproof attempts and
limitations remain authoritative in the immutable WP-016 review artefact. This
WP must not rewrite, soften or reinterpret them.

## Scope

- analyse both the immediate fresh-PR identity reset and the system cause that
  lets lower-authority candidate creation reset repository/key-level recovery;
- derive a bounded and auditable convergence rule across successive candidate
  PR identities under one complete unchanged active key;
- preserve direct inspection of every inspectable candidate head and the rule
  that one current-valid result routes to Integrator regardless of invalid or
  contained residue;
- preserve multiple-current-result conflict, exact repository/key/head
  freshness, canonical-before-use and Integrator-only control authority;
- preserve fail-closed repository-wide discovery and uncontained candidate
  inspection failure, while defining a bounded recovery condition that fresh PR
  identity creation cannot reset indefinitely;
- keep `STATE.md` + active WP canonical and all PR/evidence/control/index
  records subordinate;
- correct the exact executable producer routing precedence so one current-valid
  result is evaluated before uncontained invalid residue, without weakening
  conflict preservation or invalid-candidate recovery;
- add deterministic red-capable regression evidence for valid + first invalid,
  valid + moved invalid, valid + multiple fresh invalid, multiple-valid +
  invalid, and a long sequence of fresh invalid PR identities;
- preserve historical F-AR-001 through F-AR-007 records and exact-target
  bindings;
- record any architecture-level choice through the existing ADR path without
  accepting ADR-0002;
- identify one exact new material target, its base, complete scope, activation
  limitations and required fresh verification/re-review;
- explicitly record whether PR #19 is amended, superseded or otherwise related
  to the new target.

## Non-scope

- weakening, renaming, deleting or reinterpreting F-AR-001 through F-AR-007;
- changing WP-000 acceptance criteria to make the repair pass;
- treating WP-015 PASS as certification or acceptance of changed material;
- accepting or rejecting ADR-0000, ADR-0001 or ADR-0002;
- independently verifying or adversarially re-reviewing the builder's own
  repair;
- resolving/containing a live evidence candidate, advancing an independent-role
  attempt or canonically integrating an independent result;
- merging PR #19 or PR #1, accepting Phase 0 or beginning Phase 1;
- absorbing unrelated historical PR noise, generic abuse prevention, host
  administration or product-runtime architecture without a demonstrated direct
  dependency and explicit governance path.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first.
Within Step 3, read:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-2f5508c1-2026-08-27.md` — exact F-AR-006/F-AR-007 claims, evidence, failure paths and disproof attempts;
3. `development/07_sessions/SESSION-0028-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEWER.md`;
4. `development/04_work/WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md`;
5. `development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md`;
6. `development/04_work/WP-016-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEW.md`;
7. exact PR #19 metadata/diff and all nine files at `2f5508c1d6941e951d494bb2a700ef861860431d`;
8. exact PR #21 metadata, two-file evidence scope and evidence merge `276132a8ad3bcaa5263aba725f6f006019f79287`;
9. `development/07_sessions/SESSION-0027-PHASE0-WP015-INTEGRATOR.md` and the WP-016 result-Integrator handoff;
10. `development/01_governance/SOURCE_OF_TRUTH.md`;
11. `development/01_governance/WORKING_PROTOCOL.md`;
12. `development/01_governance/REASONING_POLICY.md`;
13. `development/01_governance/ROLE_MODEL.md`;
14. `development/01_governance/DECISION_POLICY.md`;
15. `development/01_governance/CHANGE_POLICY.md`;
16. `development/01_governance/VERIFICATION_POLICY.md`;
17. `development/03_plan/PR_GATE.md` and `development/03_plan/PHASE_GATE.md`;
18. proposed ADR-0002, both producer evidence records, the exact executable
    model and result-control template on PR #19.

## Inputs and dependencies

- immutable WP-016 judgement **Requires repair** for exact target `2f5508c...`;
- F-AR-006 medium/material and F-AR-007 low/evidence-model correctness, both
  standing;
- WP-015 historical **PASS** permanently bound only to exact target
  `2f5508c...` and its own activation/binding;
- PR #19 remaining draft, unaccepted and unmerged until the builder establishes
  its relation to one new exact target;
- unchanged WP-000 criteria and foundation/governance authority boundaries.

## Outputs

- a bounded material repair candidate on an explicit repair branch/PR;
- one exact new material target SHA and base with complete changed-file scope;
- any required proposed ADR update/supersession/new ADR under
  `DECISION_POLICY.md`;
- regression evidence covering F-AR-006/F-AR-007 and preservation of
  F-AR-001 through F-AR-005;
- a documented relation to PR #19 and the prior exact target;
- a fresh builder session handoff;
- routing to fresh separate verification and later fresh separate adversarial
  re-review, without performing either.

## Builder output

The fresh designer/builder responsibility is complete as a producer
responsibility only.

Draft PR #22 freezes exact material target
`5bd0db27fc3df368c9e112f01b7eed49a64402ab` from current canonical base
`4524f21cced54c71fb2219b7f42119adbbb5b033` and changes exactly ten files:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/F-AR-005-MOVING-CANDIDATE-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

The repair carries PR #19's exact-head and per-PR stream controls onto the
current canonical base and adds one final Integrator-only escalation. After an
earlier canonical invalid-candidate control and a later directly inspected
invalid claim at a distinct PR identity, candidate-set containment binds the
exact canonical repository + complete active key. Fresh PR identities cannot
reset it. Every inspectable head remains directly validated; exactly one
current-valid result routes before invalid residue, multiple current-valid
results remain conflict, and only invalid or candidate-specifically
inaccessible residue is contained non-valid. Repository-wide discovery and
uncontained inspection failures remain fail-closed.

Producer execution passed 67/67 declared cases. The deliberate invalid-first
mutation failed red/non-zero after 26 prior PASS observations at the first mixed
valid/invalid case. `git diff --check` passed. This is producer evidence, not
independent proof. ADR-0002 remains proposed.

PR #19 was not amended or merged. It was closed unmerged as superseded at
immutable head `2f5508c...`; WP-015 PASS, WP-016 **Requires repair** and
F-AR-006/F-AR-007 remain permanently bound only to that historical target. PR
#22 is the sole new WP-017 material target and remains draft/unaccepted/unmerged.

## Acceptance criteria — builder claim until independently verified

1. **Finding preservation:** F-AR-006 and F-AR-007 are addressed without weakening or erasing immutable F-AR-001 through F-AR-005 evidence or the WP-016 judgement.
2. **Candidate-set convergence:** successive invalid same-key PR identities cannot indefinitely reset canonical recovery or suppress the active independent responsibility.
3. **Valid-result precedence:** one current-valid exact-key result always routes to Integrator even when uncontained invalid candidates coexist.
4. **Conflict preservation:** multiple current-valid results remain an explicit conflict; no invalid candidate, control or ordering selects one.
5. **Exact freshness and authority:** repository/PR/head plus all four key fields remain exact; recovery controls are canonical-before-use and Integrator-only.
6. **Fail-closed with bounded recovery:** repository-wide discovery and uncontained inspection failures do not fail open, while the demonstrated fresh-identity denial class has a bounded recovery condition subordinate creation cannot reset forever.
7. **No arbitrary suppression:** invalid-candidate convergence cannot hide a later current-valid result, reinterpret containment as validity or let candidate authors create/reset canonical control.
8. **Model correctness:** the executable producer model matches normative current-valid precedence and fails red under a deliberate invalid-first mutation.
9. **Regression evidence:** deterministic/reproducible cases cover the mixed-valid states and fresh-identity sequence named in Scope, plus preserved same-PR/later-valid/conflict/outage cases.
10. **Canonical authority:** `STATE.md` + active WP remain the sole canonical current-work authority; PR, evidence, control and index records remain subordinate.
11. **Exact target:** one new exact material target and base are frozen; WP-015 PASS/WP-016 review are not reused as certification of changed material.
12. **Fresh gates:** changed material is routed to fresh separate verification and fresh separate adversarial re-review before any ADR/PR/Phase acceptance.
13. **No false completion:** the repair accepts no ADR, merges no PR #19/#1, accepts no Phase and begins no Phase 1 work.
14. **Scope discipline:** unrelated historical noise, generic host administration and product-runtime architecture are not silently absorbed.

The parent WP-000 acceptance criteria remain unchanged. These criteria narrow
the repair proof obligations; they do not replace or relax the parent criteria.

## Required verification and review

- fresh separate verifier against the exact new material target, including all
  current WP-000 criteria and explicit regression of F-AR-001 through F-AR-007;
- separate Integrator result transition after verifier close;
- fresh separate adversarial re-review of the exact verified repair target;
- fresh result integration after reviewer close;
- ADR/human-owner/PR/Phase gates remain separate and unchanged.

## Evidence obligations

Preserve a claim-to-trace chain for F-AR-006/F-AR-007 and every retained safety
property, including exact target/base/scope, negative cases that can fail red,
multi-PR identity traces, mixed valid/invalid traces, limitations, alternatives
considered and why the selected mechanism is necessary and smaller than
credible alternatives.

## Risks

- solving identity rotation with a broad repository/key ignore rule that can
  suppress a current-valid result;
- turning candidate admission, rate/budget state or batching into a second
  current-work authority;
- giving candidate authors or Integrators arbitrary evidence-suppression power;
- moving invalid-first precedence from the model into normative policy instead
  of correcting the evidence mismatch;
- treating a host-specific administrative policy as sufficient architecture
  without preserving repository-only continuation;
- laundering material repair as transition-only change;
- expanding the fix into a general orchestration platform before Phase 0
  acceptance.

## Completion state

**Builder repair published — fresh separate verifier activation pending.**

PR #22 exact target `5bd0db2...` is producer-complete only. No independent
verification or adversarial re-review exists for it. PR #19 remains closed
unmerged and immutable at `2f5508c...`; its historical results are not reused.

## Handoff

Exact next responsibility: **fresh separate Integrator for the WP-017
builder-close/routing package.** Validate live PR #22 target/base/ten-file scope,
PR #19 closure, the exact builder-close branch scope and proposed WP-018
attempt-1 key/bridge. Integrate only the authorised close records, then
canonically activate and bind WP-018 before dispatching a fresh separate
verifier. Do not verify/review the target, accept ADR-0002, merge PR #22/#1,
accept Phase 0 or begin Phase 1.
