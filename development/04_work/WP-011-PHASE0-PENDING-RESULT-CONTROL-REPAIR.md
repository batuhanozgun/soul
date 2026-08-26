# WP-011 — Phase 0 Pending Independent-Result Control Repair

**Status:** builder repair published — fresh separate verification required
**Owner role:** designer/builder  
**Decision authority:** bounded repair of F-AR-002, F-AR-003 and F-AR-004 within existing foundation/governance and unchanged WP-000 acceptance criteria; architecture-level choices must follow `DECISION_POLICY.md`; no independent verification, adversarial-review self-approval, canonical result integration, ADR acceptance, PR #13 merge, PR #1 merge, Phase acceptance, or Phase 1 authority  
**Development branch:** `phase0/development-os`  
**Superseded rejected material target:** closed-unmerged PR #13 exact commit `a45b463b083604d3f59d75bdca5ba97d5bc170e6`
**Repair branch:** `codex/wp011-pending-result-control-repair`
**Repair PR:** #16 — `WP-011: repair pending independent-result control lifecycle`
**Exact new material target:** `adf067e4289e4c0b51cf40c1940193e8252b22e0`
**Material base:** `8dcdc750600b336a2e97fde3433926b6a2217f26`
**Provisional activation commit:** `7c625107c09788d6066249c67d66cbf7c0c4b576`
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Prior repair package:** `WP-008-PHASE0-F-AR-001-REPAIR.md`  
**Verification activity:** WP-009 — **PASS** for exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Adversarial re-review activity:** WP-010 — **Requires repair**; F-AR-002, F-AR-003 and F-AR-004 stand  
**Reviewer evidence:** `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-a45b463b-2026-08-26.md`  
**Reviewer evidence PR:** #15, integrated evidence-only as merge commit `c8fc17bc50ca04893cc6a87e492408c078c79311`

## Objective

Produce the smallest bounded material repair that resolves the three surviving WP-010 findings against the pending independent-result control architecture, without weakening the original F-AR-001 obligation, canonical-state authority, role separation, exact-target freshness, fail-closed behaviour, or WP-000 acceptance criteria.

The builder must derive the repair architecture. This routing WP does not pre-decide whether the existing PR #13 is amended, superseded, split, or paired with a separately governed activation mechanism. Whatever path is chosen must leave one explicit new exact material target and a safe, reviewable activation/transition story.

## Exact findings preserved

### F-AR-002 — The repair has no safe activation path for its own verifier/reviewer result intervals

**Result:** stands.  
**Severity:** medium — material.

The repaired pending-result guard exists only on unmerged PR #13. Canonical `phase0/development-os` therefore remained on the pre-repair cold-start during WP-009 verifier close and WP-010 reviewer close, reproducing the original post-result/pre-Integrator duplicate-role exposure.

### F-AR-003 — Same-WP stale/ambiguous evidence can create a persistent cold-start livelock

**Result:** stands.  
**Severity:** medium — material.

The repaired guard searches open and merged/closed same-WP evidence candidates and fails closed on stale, mismatched, conflicting, ambiguous, incomplete or uninspectable candidates, but defines no durable resolution/exclusion state. A resolved historical candidate can therefore keep routing every later cold-start back to Integrator and suppress legitimate independent execution.

### F-AR-004 — One-shot pending-result discovery has a check-then-act race

**Result:** stands.  
**Severity:** low — timing-dependent.

The repaired guard runs once after Step 1. A completed evidence PR published during later bootstrap work can be missed before role declaration/substantive execution because no mandatory re-check, lease, lock or equivalent bounded concurrency control exists.

The full claim/evidence/failure-path/impact/disproof records remain authoritative in the immutable WP-010 review artefact. This WP must not rewrite or soften them.

## Scope

- analyse the immediate and system causes of F-AR-002, F-AR-003 and F-AR-004 together rather than applying three disconnected prompt patches;
- define and implement a safe activation/rollout path that protects the repair's own required verifier/reviewer post-result intervals without treating an unaccepted material target as accepted governance or depending on a human-selected scheduler;
- define a durable, authoritative and auditable resolution lifecycle for stale, target-mismatched, malformed, conflicting, ambiguous or otherwise invalid same-WP evidence candidates so resolved historical residue cannot create permanent re-routing, while preventing arbitrary evidence suppression;
- close or explicitly bound the check-then-act race immediately before independent role commitment/substantive execution through the smallest justified control;
- preserve `STATE.md` + active WP as the canonical current-work authority and keep evidence/PR metadata subordinate;
- preserve separate verifier/reviewer and Integrator authority, including the prohibition on self-transition and self-acceptance;
- preserve fail-closed discovery/inspection behaviour while adding a bounded recovery/progress path;
- decide and record, through the proper change/ADR path, whether PR #13 is amended, superseded, or otherwise related to the new exact material target;
- add deterministic or reproducible regression evidence for the observed PR #14 and PR #15 result intervals, resolved stale-candidate recovery, conflicting/malformed candidates, discovery failure, and concurrent publication timing;
- leave a builder handoff that identifies the exact new target, branch/PR, changed-file scope, unresolved limitations, and required fresh verification/re-review.

## Non-scope

- weakening, renaming, deleting or reinterpreting F-AR-001 through F-AR-004;
- changing WP-000 acceptance criteria to make the repair pass;
- treating the historical WP-009 PASS as certification of a changed target;
- accepting or rejecting ADR-0000, ADR-0001, ADR-0002, or any new/updated architecture decision;
- independently verifying or adversarially re-reviewing the builder's own repair;
- canonically integrating a verifier/reviewer result;
- merging PR #13 or PR #1, accepting Phase 0, or beginning Phase 1;
- repairing unrelated historical PR noise or PD-002 unless a direct mechanical dependency is demonstrated and explicitly routed.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first. Within Step 3, read:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`
2. `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-a45b463b-2026-08-26.md` — exact findings and disproof attempts
3. `development/07_sessions/SESSION-0017-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEWER.md`
4. `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md`
5. `development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md`
6. `development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md`
7. exact PR #13 metadata/diff at `a45b463b083604d3f59d75bdca5ba97d5bc170e6`
8. PR #14 and PR #15 metadata, exact evidence-only scope and merge records
9. `development/07_sessions/SESSION-0016-PHASE0-WP009-INTEGRATOR.md`
10. `development/07_sessions/SESSION-0018-PHASE0-WP010-INTEGRATOR.md`
11. `development/01_governance/SOURCE_OF_TRUTH.md`
12. `development/01_governance/WORKING_PROTOCOL.md`
13. `development/01_governance/REASONING_POLICY.md`
14. `development/01_governance/ROLE_MODEL.md`
15. `development/01_governance/DECISION_POLICY.md`
16. `development/01_governance/CHANGE_POLICY.md`
17. `development/01_governance/VERIFICATION_POLICY.md`
18. `development/03_plan/PR_GATE.md`
19. exact target versions of the six WP-008 repair files and proposed ADR-0002

## Inputs and dependencies

- immutable WP-010 reviewer result **Requires repair** for exact target `a45b463...`;
- F-AR-002 and F-AR-003 as medium/material findings and F-AR-004 as a real low/timing-dependent finding;
- current canonical development head after evidence integration and transition routing;
- PR #13 remaining open/draft and frozen at the rejected target until an authorised builder changes or supersedes it;
- unchanged WP-000 criteria and existing foundation/governance authority boundaries.

## Outputs

- a bounded material repair candidate on an explicit repair branch/PR;
- one exact new material target SHA and base, with complete changed-file scope;
- any required proposed ADR update/supersession/new ADR under `DECISION_POLICY.md`;
- regression evidence covering all three findings and their interaction;
- updated repair-package status/routing records required to identify the new target;
- a fresh builder session handoff;
- routing to a fresh separate verifier without performing that verification.

## Builder output

The fresh designer/builder responsibility is complete as a producer responsibility only.

PR #16 freezes exact material target `adf067e4289e4c0b51cf40c1940193e8252b22e0` from base `8dcdc750600b336a2e97fde3433926b6a2217f26` and changes exactly:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

The candidate introduces a complete result-control key (`WP / independent role / exact target / positive attempt`), a mandatory initial and immediate pre-role live re-check, exact-head canonical Integrator resolution records, moved-head reopening, protection against suppressing a current valid result, conflict-preserving fresh-attempt routing, fail-closed discovery recovery, and a provisional WP-local activation bridge for the repair's own verification/re-review intervals. It explicitly records the residual publication-after-final-check edge rather than claiming an atomic platform lock.

Producer regression execution passed all 13 declared cases, including the real PR #14 and PR #15 intervals. This is producer evidence, not independent verification.

PR #13 was closed unmerged as superseded; its exact historical target and WP-009/WP-010 bindings remain immutable. ADR-0002 remains proposed. PR #16 remains draft/unaccepted/unmerged.

## Acceptance criteria — builder claim until independently verified

1. **Finding preservation:** F-AR-002, F-AR-003 and F-AR-004 are addressed without weakening or erasing F-AR-001 or the immutable WP-010 result.
2. **Safe activation:** a generic fresh session is protected during the repair's own required verifier/reviewer post-result intervals without silently accepting unreviewed governance or relying on human awareness/scheduling.
3. **Bounded stale-candidate recovery:** an invalid or historical same-WP evidence candidate can be durably classified/resolved so it does not cause permanent Integrator re-routing, and the resolution mechanism cannot arbitrarily suppress a current valid result.
4. **Race containment:** the publication-between-check-and-role-commit path is prevented, deterministically detected, or reduced to an explicitly justified residual boundary with a mandatory final freshness control.
5. **Canonical authority:** `STATE.md` + active WP remain the sole canonical home of current work; evidence, PR metadata, resolution records and derived views remain subordinate inputs to bounded transition logic.
6. **Role separation:** verifier/reviewer roles cannot integrate, suppress, accept or repair their own result; Integrator routing remains separate and mechanical.
7. **Fail-closed with recovery:** discovery/inspection/conflict failures do not fail open into duplicate work, while every blocked class has a documented bounded recovery condition.
8. **Regression evidence:** the repair exercises the real PR #14 and PR #15 close intervals, stale closed same-WP evidence, malformed/conflicting candidates, unavailable inspection, and concurrent publication timing with observable expected/actual results.
9. **Exact target/freshness:** the builder freezes one exact new material target and does not reuse WP-009 PASS or WP-010 review as certification of changed material.
10. **No false completion:** the repair does not accept an ADR, merge PR #13/#1, accept Phase 0, begin Phase 1, or claim independent verification/re-review.
11. **Scope discipline:** unrelated historical noise, PD-002 and broader product architecture are not silently absorbed.

## Required verification and review

- fresh separate verifier against the exact new material target, including every current WP-000 criterion and explicit regressions for F-AR-001 through F-AR-004;
- separate Integrator result transition after verifier close;
- fresh separate adversarial re-review of the exact verified repair target;
- fresh result integration after reviewer close;
- ADR/human-owner/PR/Phase gates remain separate and unchanged.

## Evidence obligations

The builder must preserve a claim-to-trace chain for each finding, including the real repository lifecycle evidence, negative cases that can fail/red, exact target/base/file scope, limitations, and the reason the chosen mechanism is necessary and smaller than credible alternatives.

## Risks

- solving activation by silently making proposed governance canonical before its gates;
- solving livelock with an overly broad ignore mechanism that hides current evidence;
- adding more prompt-only rules without a durable resolution state or deterministic check;
- creating a lock/lease mechanism whose own authority, stale-state or recovery semantics are undefined;
- expanding the repair into a general orchestration platform before Phase 0 acceptance;
- laundering material repair as transition-only change.

## Completion state

Current: **builder repair published — fresh separate verification required.**

The prior target `a45b463...` remains historically verified PASS under WP-009 but unsuitable because WP-010 issued **Requires repair**. The changed target `adf067e...` has no independent verification or adversarial re-review result.

## Handoff

Exact next responsibility: **fresh separate verifier under WP-012** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0`, result-control attempt 1. The builder stops without self-verification, self-review, result integration, acceptance, or merge.
