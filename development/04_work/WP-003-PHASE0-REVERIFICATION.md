# WP-003 — Phase 0 Fresh Re-verification

**Status:** active  
**Owner role:** verifier  
**Decision authority:** verifier issues PASS / FAIL / NOT VERIFIED; no repair, integration, adversarial-review, ADR-acceptance, or Phase-acceptance authority  
**Branch:** verifier must use a fresh verification branch/execution based on the exact current draft PR #1 head at verification start  
**Target:** draft PR #1 exact head commit captured at verification start

## Objective

Independently verify the materially repaired Phase 0 development operating system against the **unchanged WP-000 acceptance criteria**, including explicit regression checks for F1, F2, and PD-001, and bind the result to the new exact PR #1 target commit.

## Problem

WP-001 independently verified the earlier PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71` and issued overall FAIL. WP-002 subsequently made material governance/plan changes to repair F1, F2, and PD-001. The historical WP-001 result is therefore not current verification of the changed target.

A fresh verifier must re-derive the expected result from WP-000 and current governance before relying on the repair builder's rationale.

## Scope

- all eleven WP-000 acceptance criteria;
- regression verification of **F1 — cold-start order contradiction**;
- regression verification of **F2 — duplicated/stale current-work pointer**;
- explicit test of **PD-001 — verifier-result → canonical-state transition**;
- exact-target freshness and role-separation checks;
- confirmation that WP-000 acceptance criteria and owner/ADR/adversarial gates were not weakened by the repair.

## Non-scope

- repairing any finding;
- redesigning the repair;
- integrating the verifier's own result into canonical state;
- performing adversarial review;
- accepting ADR-0000;
- merging draft PR #1 into `main`;
- beginning Phase 1.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete COLD_START Steps 1–2 first. The order below applies **only within COLD_START Step 3** and does not replace the bootstrap sequence:

1. `development/01_governance/VERIFICATION_POLICY.md`
2. `development/04_work/WP-000-DEVELOPMENT-OS.md`
3. `development/00_foundation/VISION.md`
4. `development/00_foundation/DEFINITION.md`
5. `development/00_foundation/SUCCESS_CRITERIA.md`
6. `development/00_foundation/NON_NEGOTIABLES.md`
7. `development/01_governance/SOURCE_OF_TRUTH.md`
8. `development/01_governance/WORKING_PROTOCOL.md`
9. `development/03_plan/COLD_START.md`
10. `development/03_plan/NEXT_SESSION.md`
11. `development/03_plan/WORKSPACE_INDEX.md`
12. `development/01_governance/ROLE_MODEL.md`
13. `development/01_governance/DECISION_POLICY.md`
14. `development/01_governance/CHANGE_POLICY.md`
15. `development/03_plan/PR_GATE.md`
16. `development/03_plan/PHASE_GATE.md`
17. `development/04_work/WP_TEMPLATE.md`
18. `development/06_reviews/VERIFICATION_TEMPLATE.md`
19. only after deriving the expected result from WP-000/current governance: `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`
20. `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`
21. only after expectation derivation and inspection of the historical defect evidence: the WP-002 builder handoff named by current repository state/index.

PR metadata may be read before builder rationale only to capture and later freshness-check the exact target SHA. The historical verifier artefact is evidence of the previous target and findings, not proof that the repair succeeded.

## Inputs and dependencies

- WP-002 builder repair is materially complete and has handed off to this fresh verifier responsibility.
- WP-000 acceptance criteria remain textually and semantically unchanged.
- Historical WP-001 result remains FAIL for exact old target `1d2dd033ca3068484d841bcebf90e81ea84c7f71`.
- Current target must be captured independently from draft PR #1 metadata at verification start.

## Outputs

- a new dated verification artefact under `development/06_reviews/` bound to the new exact target SHA;
- a fresh verifier session handoff under `development/07_sessions/`;
- no repair/integration changes to Phase 0 artefacts.

## Acceptance criteria

1. All eleven WP-000 acceptance criteria receive PASS / FAIL / NOT VERIFIED with exact current evidence.
2. The verifier records the exact draft PR #1 target SHA at start and re-checks freshness before closing.
3. **F1 regression:** current mandatory bootstrap/read-order controls are mutually satisfiable under the explicit COLD_START sequencing mechanism; no current WP, protocol, launch view, or governance rule requires an incompatible bootstrap order.
4. **F2 regression:** `STATE.md` + active WP remain the authoritative current-work home; `NEXT_SESSION.md` does not materialise a competing current WP/role/target value; any index/view that repeats current state is explicitly subordinate and current.
5. **PD-001 regression:** `VERIFICATION_POLICY.md`, `ROLE_MODEL.md`, `WORKING_PROTOCOL.md`, and `PR_GATE.md` together define an unambiguous verifier-result → canonical-state transition with a separate Integrator, exact-target/result checks, evidence-only integration, PASS/FAIL/NOT VERIFIED routing, repair activation, freshness handling, and no-false-completion controls.
6. The repair has not changed or weakened any of WP-000's eleven acceptance criteria, verifier independence, owner gates, ADR status requirements, adversarial-review requirement, or Phase 1 gate.
7. The historical WP-001 FAIL artefact and SESSION-0003 verifier record remain accurate for their old target and are not reused as current proof.
8. The verifier performs no repair, canonical result integration, ADR acceptance, adversarial review, target merge, or Phase 1 work.
9. Overall PASS is issued only if all mandatory WP-000 criteria and the explicit F1/F2/PD-001 regression checks pass; NOT VERIFIED remains legitimate.

## Required verification

This WP is the fresh independent re-verification activity.

The verifier must:

- re-derive expected results from unchanged WP-000/current governance before reading the builder handoff;
- inspect the exact immutable PR #1 target commit rather than relying on an unpinned branch snapshot;
- test all eleven WP-000 criteria, not only the three repair defects;
- explicitly simulate or trace PASS, FAIL, and NOT VERIFIED through the new PD-001 transition controls without executing canonical integration itself;
- prefer direct/deterministic repository inspection over builder explanation;
- leave result integration to a later Integrator session.

## Evidence obligations

The verification artefact must cite the exact files/sections used for every WP-000 criterion and separately identify evidence for F1, F2, and PD-001. It must distinguish:

- the exact new target SHA,
- historical old-target verification evidence,
- builder claims,
- independently observed current repository facts.

## Risks

- treating the builder's repair rationale as proof;
- checking only F1/F2/PD-001 and failing to re-verify all WP-000 criteria;
- accepting an explicit precedence statement without checking competing current control surfaces;
- mistaking a subordinate index/view for a second authoritative state store;
- allowing Integrator transition authority to become repair or acceptance authority;
- reusing the historical FAIL or its PASS results for criteria 3–11 as current evidence after material repair;
- performing repairs inside the verifier session.

## Completion state

Current: **active — fresh verifier required**.

This WP becomes complete as a verification activity only after it has produced a current exact-target result and verifier handoff according to its own acceptance criteria. That activity status does not by itself accept WP-000, ADR-0000, Phase 0, or PR #1.

## Handoff

- **PASS** → separate **Integrator** session executes `VERIFICATION_POLICY.md` result-to-state transition and activates the required adversarial-review responsibility. PASS does not directly accept Phase 0.
- **FAIL** → separate Integrator records the result and activates a bounded fresh builder repair WP; any material repair requires another fresh verifier target.
- **NOT VERIFIED** → separate Integrator records the blocker and activates the smallest bounded investigation/repair responsibility needed before fresh verification.

The verifier must not perform its own result integration.
