# WP-007 — Phase 0 Adversarial Review

**Status:** complete — review issued **Requires repair**; F-AR-001 stands  
**Owner role:** adversarial-reviewer  
**Decision authority:** adversarial reviewer may issue evidence-backed findings and an overall suitability judgement; no repair, canonical integration, ADR acceptance, target merge, Phase acceptance, or Phase 1 authority  
**Branch:** fresh adversarial-review branch/execution based on the current Phase 0 development line  
**Material review target:** draft PR #1 material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`  
**Trigger:** WP-006 exact-target verification PASS integrated through verifier evidence PR #10

## Objective

Independently attack the Phase 0 Development Operating System after WP-006 PASS and determine whether a material failure remains that normal verification did not expose.

The review remained bound to material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`. Post-target commits were treated as non-retargeting only after they were inspected as transition-only under `VERIFICATION_POLICY.md`.

## Problem

WP-006 established specification conformance, but Phase 0 still required a separate adversarial review before acceptance. The adversarial role had to actively seek failure paths rather than repeat the verifier's checklist or producer rationale.

## Scope

Attack surfaces included, without imposing a finding quota:

- hidden assumptions and specification loopholes;
- authority leaks, owner-decision transfer, or role-confusion paths;
- duplicate bootstrap/current-state authority and stale-context failure paths;
- verifier-result transition discoverability, including the observed pre-integration interval where canonical `STATE.md` can still say “verifier required” while completed verifier evidence exists only in a verification branch/PR, and whether a generic cold-start can incorrectly duplicate verifier work;
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

The reviewer entered through `development/03_plan/COLD_START.md` and completed Steps 1–2 first. The sequence below applied only within COLD_START Step 3.

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

The reviewer recorded the attack surfaces/hypotheses before relying on verifier, builder, or Integrator conclusions.

### B. Then inspect changed architecture and prior evidence

16. `development/04_work/WP-004-PHASE0-F2R1-REPAIR.md`
17. `development/04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md`
18. `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
19. `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
20. `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`
21. `development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`
22. `development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`
23. `development/07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md`

## Acceptance criteria result

The reviewer completed the required independent review activity, bound the review to the exact target, persisted its attack model before relying on prior conclusions, checked the post-target transition chain, attempted to disprove candidate findings, performed no repair/canonical transition/acceptance work, and issued an overall judgement.

One material finding survived disproof:

### F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated independent result

**Result:** stands.  
**Severity:** medium — material.  
**Overall judgement:** **Requires repair.**

Canonical review evidence:

`development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`

Reviewer handoff:

`development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`

## Integration record

Reviewer evidence PR #12 contained only the adversarial-review artefact and SESSION-0012 handoff. A separate Integrator inspected that evidence-only scope and merged PR #12 into `phase0/development-os` as merge commit `9de8a011aa2d14fb985181ba3f180f729342901d`.

The integration preserves F-AR-001 and the **Requires repair** judgement exactly. Evidence integration is not acceptance of the reviewed target and does not repair the finding.

The bounded repair responsibility is routed separately under `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md`.

## Completion state

**Complete as an adversarial-review activity — result: Requires repair.**

WP-000/Phase 0 is not accepted. The exact reviewed material target is not suitable to proceed directly to the remaining ADR/human-owner/PR acceptance gates until F-AR-001 is repaired or otherwise resolved through authorised governance.

## Handoff

- surviving material finding F-AR-001 → active `WP-008-PHASE0-F-AR-001-REPAIR.md` assigns a fresh separate designer/builder the bounded repair responsibility;
- the Integrator did not choose or implement the repair mechanism;
- any material repair requires fresh exact-target independent verification and appropriate fresh adversarial re-review;
- ADR-0000/ADR-0001, PR #1 merge, Phase acceptance, and Phase 1 remain outside this completed review activity.
