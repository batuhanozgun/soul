# WP-014 — Phase 0 Moving-Candidate Convergence Repair

**Status:** active — fresh separate designer/builder required
**Owner role:** designer/builder
**Decision authority:** bounded repair of F-AR-005 within existing foundation/governance and unchanged WP-000 acceptance criteria; architecture-level choices must follow `DECISION_POLICY.md`; no independent verification, adversarial-review self-approval, canonical independent-result integration, ADR acceptance, PR #16/#1 merge, Phase acceptance, or Phase 1 authority
**Development branch:** `phase0/development-os`
**Rejected material target:** draft PR #16 exact commit `adf067e4289e4c0b51cf40c1940193e8252b22e0`
**Material base:** `8dcdc750600b336a2e97fde3433926b6a2217f26`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Prior repair package:** `WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md`
**Verification activity:** WP-012 — **PASS** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and activation `7c625107c09788d6066249c67d66cbf7c0c4b576`
**Adversarial re-review activity:** WP-013 — **Requires repair**; F-AR-005 medium/material, stands
**Reviewer evidence:** `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-adf067e4-2026-08-26.md`
**Reviewer evidence PR:** #18, head `2e78421f1c618995fe0cc0c8eb62104ecae63be1`, integrated evidence-only as `fda9689107cf96ad2cc01e1b1bbe74b86055e771`

## Objective

Produce the smallest coherent material repair that gives the pending independent-result control a bounded convergence path when the same lower-authority invalid candidate repeatedly moves its head, without weakening exact-head freshness, current-valid-result non-suppression, conflict preservation, fail-closed inspection, canonical-state authority or role separation.

The builder must derive the repair architecture. This routing WP does not preselect trust, publication freeze, quarantine, repeated-movement escalation or another mechanism, and it does not decide whether PR #16 is amended, superseded or otherwise related to the new target. The output must leave one explicit new exact target and a safe, reviewable activation and independent-result path.

## Exact finding preserved

### F-AR-005 — A mutable lower-authority candidate can repeatedly invalidate exact-head resolutions and deny progress indefinitely

**Result:** stands.
**Severity:** medium — material.

Exact-head resolution converges for a fixed invalid candidate, but every moved head intentionally reopens inspection and every unresolved invalid same-WP candidate blocks. Because discovery includes closed PRs, closing alone is not resolution, attempt advancement leaves a same-WP mismatch, and the target has no trust/freeze/quarantine/repeated-movement convergence rule, a mutable subordinate locator can repeatedly force Integrator routing and indefinitely deny the canonical responsibility.

The full claim, evidence, five-generation failure path, impact, disproof attempts and limitations remain authoritative in the immutable WP-013 review artefact. This WP must not rewrite or soften them.

## Scope

- analyse both the immediate moving-head failure and the system cause that lets lower-authority mutable locator state repeatedly suppress canonical work;
- derive a bounded, auditable convergence rule for repeated movement of the same invalid/stale/malformed same-WP candidate;
- preserve the rule that a resolution for one immutable head does not silently suppress a later current valid result;
- preserve exact four-field key validation, exact repository/PR/head binding, multiple-current-result conflict handling and Integrator-only resolution/attempt authority;
- preserve fail-closed discovery/inspection while defining an explicit recovery condition that cannot be reset forever by lower-authority mutation;
- define how closed, force-pushed, deleted, inaccessible or repeatedly updated candidates participate in the lifecycle without becoming a permanent denial primitive;
- keep `STATE.md` + active WP canonical and PR/evidence/resolution metadata subordinate;
- record any architecture-level choice through the existing ADR path without accepting ADR-0002;
- add deterministic or reproducible negative evidence for fixed-head recovery, a later valid head, and repeated invalid-head generations beyond the reviewer’s five-step trace;
- identify one exact new material target, its base, complete scope, activation limitations and required fresh verification/re-review;
- explicitly record whether PR #16 is amended, superseded or otherwise related to the new target.

## Non-scope

- weakening, renaming, deleting or reinterpreting F-AR-001 through F-AR-005;
- changing WP-000 acceptance criteria to make the repair pass;
- treating WP-012 PASS as certification of changed material or as acceptance of PR #16;
- accepting or rejecting ADR-0000, ADR-0001 or ADR-0002;
- independently verifying or adversarially re-reviewing the builder’s own repair;
- resolving a live result candidate or advancing an independent-role attempt as part of repair implementation unless a separate currently authorised Integrator responsibility requires it;
- merging PR #16 or PR #1, accepting Phase 0 or beginning Phase 1;
- absorbing unrelated historical PR noise or process defects without a direct demonstrated dependency and explicit routing.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first. Within Step 3, read:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-adf067e4-2026-08-26.md` — exact F-AR-005 claim/evidence/failure path/disproof;
3. `development/07_sessions/SESSION-0022-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEWER.md`;
4. `development/04_work/WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md`;
5. `development/04_work/WP-012-PHASE0-PENDING-RESULT-CONTROL-VERIFICATION.md`;
6. `development/04_work/WP-013-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEW.md`;
7. exact PR #16 metadata/diff and all eight files at `adf067e4289e4c0b51cf40c1940193e8252b22e0`;
8. exact PR #18 metadata, two-file evidence scope and evidence merge `fda9689107cf96ad2cc01e1b1bbe74b86055e771`;
9. `development/07_sessions/SESSION-0021-PHASE0-WP012-INTEGRATOR.md` and `development/07_sessions/SESSION-0023-PHASE0-WP013-INTEGRATOR.md`;
10. `development/01_governance/SOURCE_OF_TRUTH.md`;
11. `development/01_governance/WORKING_PROTOCOL.md`;
12. `development/01_governance/REASONING_POLICY.md`;
13. `development/01_governance/ROLE_MODEL.md`;
14. `development/01_governance/DECISION_POLICY.md`;
15. `development/01_governance/CHANGE_POLICY.md`;
16. `development/01_governance/VERIFICATION_POLICY.md`;
17. `development/03_plan/PR_GATE.md` and `development/03_plan/PHASE_GATE.md`;
18. proposed ADR-0002, current pending-result resolution template and both producer/reviewer executable-model evidence records.

## Inputs and dependencies

- immutable WP-013 judgement **Requires repair** for exact target `adf067e...`;
- F-AR-005 as a medium/material denial-of-progress and bounded-authority failure;
- WP-012 historical **PASS** permanently bound only to exact target `adf067e...` and activation `7c625107...`;
- current canonical development head after evidence-only result integration and transition routing;
- PR #16 remaining draft, unaccepted and unmerged until the authorised builder establishes its relation to one new exact target;
- unchanged WP-000 criteria and foundation/governance authority boundaries.

## Outputs

- a bounded material repair candidate on an explicit repair branch/PR;
- one exact new material target SHA and base with complete changed-file scope;
- any required proposed ADR update/supersession/new ADR under `DECISION_POLICY.md`;
- regression evidence covering F-AR-005 and preservation of F-AR-001 through F-AR-004;
- a documented relation to PR #16 and the prior exact target;
- a fresh builder session handoff;
- routing to fresh separate verification and later fresh separate adversarial re-review, without performing either.

## Acceptance criteria — builder claim until independently verified

1. **Finding preservation:** F-AR-005 is addressed without weakening or erasing immutable F-AR-001 through F-AR-004 evidence or the WP-013 judgement.
2. **Bounded convergence:** repeated invalid-head movement by the same lower-authority candidate cannot indefinitely reset canonical recovery or suppress the active responsibility.
3. **Valid-result protection:** a later current valid exact-key result cannot be hidden by an earlier resolution, quarantine or convergence mechanism.
4. **Exact freshness:** repository/PR/head and four-field key bindings remain exact enough to prevent stale or mismatched evidence from becoming current.
5. **Conflict and authority:** multiple current results remain an explicit conflict; resolution, exclusion and attempt advancement remain separately authorised and auditable.
6. **Fail-closed recovery:** discovery/inspection failures do not fail open, while every blocked class has a bounded recovery condition that subordinate mutation cannot reset forever.
7. **Canonical authority:** `STATE.md` + active WP remain the sole canonical current-work authority; PR, evidence and resolution records remain subordinate.
8. **Regression evidence:** deterministic/reproducible cases cover one fixed invalid head, successive invalid heads, a later corrected/current-valid head, closed/moved/deleted or inaccessible candidates as applicable, conflict and inspection outage.
9. **Exact target:** one new exact material target and base are frozen; WP-012 PASS/WP-013 review are not reused as certification of changed material.
10. **Fresh gates:** the changed target is routed to fresh separate verification and fresh separate adversarial re-review before any ADR/PR/Phase acceptance.
11. **No false completion:** the repair accepts no ADR, merges no PR #16/#1, accepts no Phase and begins no Phase 1 work.
12. **Scope discipline:** unrelated historical noise and process defects are not silently absorbed.

## Required verification and review

- fresh separate verifier against the exact new material target, including all current WP-000 criteria and explicit regression of F-AR-001 through F-AR-005;
- separate Integrator result transition after verifier close;
- fresh separate adversarial re-review of the exact verified target;
- fresh result integration after reviewer close;
- ADR/human-owner/PR/Phase gates remain separate and unchanged.

## Evidence obligations

Preserve a claim-to-trace chain for F-AR-005 and every preserved safety property, including exact target/base/scope, negative cases that can fail red, repeated-movement traces, limitations, alternatives considered and why the selected mechanism is necessary and smaller than credible alternatives.

## Risks

- solving denial-of-progress with a broad ignore/quarantine rule that can suppress a later valid result;
- giving candidate authors or Integrators unbounded evidence-suppression authority;
- creating a retry counter whose reset, scope, storage or authority reproduces the same failure;
- relying on mutable PR metadata as canonical state;
- adding prompt-only escalation without deterministic convergence evidence;
- laundering material repair as transition-only change;
- expanding the fix into a general orchestration platform before Phase 0 acceptance.

## Completion state

Active — fresh separate designer/builder required. No repaired exact target exists yet.

## Handoff

Exact next responsibility: fresh separate designer/builder under this WP. Preserve the immutable reviewer judgement and finding, derive and publish the smallest coherent repair with one exact target and regression evidence, route that target to fresh separate verification, and stop without self-verification, self-review, result integration, ADR acceptance, target merge, Phase acceptance or Phase 1 work.
