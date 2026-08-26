# WP-007 — Phase 0 Adversarial Review

**Status:** active  
**Owner role:** adversarial-reviewer  
**Decision authority:** adversarial reviewer may issue evidence-backed findings and an overall suitability judgement; no repair, canonical integration, ADR acceptance, target merge, Phase acceptance, or Phase 1 authority  
**Branch:** fresh adversarial-review branch/execution based on the current Phase 0 development line  
**Material review target:** draft PR #1 material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`  
**Trigger:** WP-006 exact-target verification PASS integrated through verifier evidence PR #10

## Objective

Independently attack the Phase 0 Development Operating System after WP-006 PASS and determine whether a material failure remains that normal verification did not expose.

The review must remain bound to material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`. Post-target commits may be treated as non-retargeting only if they are demonstrably transition-only under `VERIFICATION_POLICY.md`.

## Problem

WP-006 established specification conformance, but Phase 0 still requires a separate adversarial review before acceptance. The adversarial role must actively seek failure paths rather than repeat the verifier's checklist or producer rationale.

## Scope

Attack surfaces include, without imposing a finding quota:

- hidden assumptions and specification loopholes;
- authority leaks, owner-decision transfer, or role-confusion paths;
- duplicate bootstrap/current-state authority and stale-context failure paths;
- circular verification, self-approval, false completion, or freshness laundering;
- change-safety, self-modification, recovery and evidence/provenance gaps;
- development/product boundary failures;
- reasoning-policy risks explicitly identified by WP-005/ADR-0001: ritualised overthinking, duplicate authority, hidden transfer of technical decisions to the human owner, prompt-only false assurance, excessive cold-start burden, and private-chain-of-thought boundary erosion;
- PD-002 recurrence/activation-order ambiguity and whether current controls fail open;
- any other material attack surface discovered from the authoritative architecture.

## Non-scope

- repairing findings;
- rewriting acceptance criteria or governance to make review easier;
- accepting/rejecting ADR-0000 or ADR-0001;
- reinterpreting the WP-006 PASS;
- merging PR #1;
- beginning Phase 1.

## Required reading

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first. The sequence below applies only within COLD_START Step 3.

### A. Establish attack model before reading verifier conclusions

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`
2. `development/00_foundation/VISION.md`
3. `development/00_foundation/DEFINITION.md`
4. `development/00_foundation/SUCCESS_CRITERIA.md`
5. `development/00_foundation/NON_NEGOTIABLES.md`
6. `development/01_governance/SOURCE_OF_TRUTH.md`
7. `development/01_governance/WORKING_PROTOCOL.md`
8. `development/01_governance/REASONING_POLICY.md`
9. `development/01_governance/ROLE_MODEL.md`
10. `development/01_governance/DECISION_POLICY.md`
11. `development/01_governance/CHANGE_POLICY.md`
12. `development/01_governance/VERIFICATION_POLICY.md`
13. `development/03_plan/PR_GATE.md`
14. `development/03_plan/PHASE_GATE.md`
15. `development/06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`

At this point record the attack surfaces/hypotheses to test before relying on verifier or builder conclusions.

### B. Then inspect changed architecture and prior evidence

16. `development/04_work/WP-004-PHASE0-F2R1-REPAIR.md`
17. `development/04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md`
18. `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
19. `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
20. `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`
21. `development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`
22. `development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`

PR/repository metadata may be inspected to confirm that all commits after `c690f858e7682f5bdf0511c0f10b0e932d868b0e` are transition-only. If any material post-target change is found, stop: current verification/review freshness must be reconsidered before Phase 0 can proceed.

## Acceptance criteria

1. A fresh adversarial-review session operates separately from the builder, verifier, and Integrator roles.
2. Review target and post-target transition-only chain are identified exactly; no material change is silently covered by stale verification.
3. The reviewer records an attack model before reading verifier conclusions.
4. The review attempts to falsify Phase 0 across the scoped attack surfaces, including the specific reasoning-policy risks required by WP-005/ADR-0001.
5. Every surviving finding includes claim, exact evidence, failure path, impact, severity, disproof attempt, and result.
6. Findings are not quota-driven; if none survive disproof, the reviewer explicitly records a no-finding statement.
7. The reviewer performs no repair, canonical state transition, ADR acceptance, PR #1 merge, or Phase 1 work.
8. The review leaves an overall judgement on whether the material target is suitable to proceed to the remaining integration/decision gates.

## Verification / review method

Prefer deterministic repository/authority/path checks where possible, then direct artefact/source inspection, then semantic attack analysis for failure paths that cannot be mechanically decided. The reviewer must try to disprove candidate findings rather than preserve them for appearance.

## Outputs

- a new adversarial-review artefact under `development/06_reviews/`, uniquely named and bound to material target `c690f858...`;
- a fresh adversarial-review session handoff under `development/07_sessions/`;
- no repair or canonical transition changes.

## Completion state

Current: **active — fresh separate adversarial reviewer required**.

Completion of this review does not by itself accept Phase 0 or ADR-0000/ADR-0001. A separate Integrator must integrate the review evidence and route any surviving findings or remaining decision/owner gates without reinterpretation.

## Handoff

- surviving material finding(s) → separate Integrator records the review result and routes bounded repair/decision work under existing governance; any material repair requires fresh verification and appropriate re-review;
- no surviving material findings / suitable-to-proceed judgement → separate Integrator records the review completion and routes the remaining ADR/human-owner/PR acceptance gates; no Phase 1 work begins before Phase 0 is accepted into `main`.
