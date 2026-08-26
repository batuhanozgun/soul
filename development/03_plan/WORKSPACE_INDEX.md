# SOUL DEVELOPMENT INDEX

## Foundation
- `../00_foundation/VISION.md`
- `../00_foundation/DEFINITION.md`
- `../00_foundation/SUCCESS_CRITERIA.md`
- `../00_foundation/NON_NEGOTIABLES.md`

## Governance
- `../01_governance/SOURCE_OF_TRUTH.md`
- `../01_governance/WORKING_PROTOCOL.md`
- `../01_governance/REASONING_POLICY.md`
- `../01_governance/ROLE_MODEL.md`
- `../01_governance/DECISION_POLICY.md`
- `../01_governance/VERIFICATION_POLICY.md`
- `../01_governance/CHANGE_POLICY.md`

## Planning
- `ROADMAP.md`
- `STATE.md`
- `COLD_START.md` — single fresh-session sequencing authority
- `PHASE_GATE.md`
- `PR_GATE.md`
- `NEXT_SESSION.md` — derived launch view; no authoritative current-state values
- `CHATGPT_PROJECT_ENTRY.md` — derived minimal Project Instructions convenience; no governance copy

## Current work
- Active: `../04_work/WP-007-PHASE0-ADVERSARIAL-REVIEW.md` — fresh separate adversarial-review responsibility
- Completed verification activity: `../04_work/WP-006-PHASE0-REASONING-REVERIFICATION.md` — **PASS** against exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`
- Material reasoning-policy architecture: `../04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md` — verified for current WP-000 properties at `c690f858...`; ADR-0001 still proposed/not Phase-accepted
- Completed bounded repair: `../04_work/WP-004-PHASE0-F2R1-REPAIR.md` — F2-R1 regression PASS at `c690f858...`
- Parent package: `../04_work/WP-000-DEVELOPMENT-OS.md` — exact material target has current WP-006 PASS; still awaiting adversarial review and remaining decision/acceptance gates
- Historical completed verification activity: `../04_work/WP-003-PHASE0-REVERIFICATION.md` — exact old target `a02e36e5...`, result FAIL
- Historical completed verification activity: `../04_work/WP-001-PHASE0-VERIFICATION.md` — old target result FAIL
- Historical repair package: `../04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md`

## Verification, reviews, defects and evidence
- `../06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md` — current issued verification: **PASS** against exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`; verifier evidence PR #10 integrated evidence-only
- `../06_reviews/VERIFICATION-WP-000-2026-08-26.md` — historical FAIL against exact target `a02e36e5e71522995b74fb018a6b28235f1d7848`; stale for current material target
- `../06_reviews/VERIFICATION-WP-000-2026-08-25.md` — historical FAIL against exact old target `1d2dd033ca3068484d841bcebf90e81ea84c7f71`
- `../06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`
- `../06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md` — defect preserved; final current-work discipline passed WP-006 verification at `c690f858...`
- `../05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md` — source-to-SOUL synthesis evidence for WP-005
- Adversarial review for WP-007: **not yet produced**

## Decisions
- `../02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md` — proposed; still requires its declared owner path
- `../02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md` — proposed; owner direction approved, independent verification passed, adversarial/Phase acceptance path still pending

## Templates
- ADR: `../01_governance/ADR_TEMPLATE.md`
- Work package: `../04_work/WP_TEMPLATE.md`
- Evidence: `../05_evidence/EVIDENCE_TEMPLATE.md`
- Verification: `../06_reviews/VERIFICATION_TEMPLATE.md`
- Adversarial review: `../06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`
- Session handoff: `../07_sessions/SESSION_TEMPLATE.md`

## Handoffs and historical launch records
- `../07_sessions/SESSION-0001-PHASE0-BUILDER.md`
- `../07_sessions/SESSION-0002-NEXT-VERIFIER-BRIEF.md` — historical, not a current cold-start authority
- `../07_sessions/SESSION-0003-PHASE0-VERIFIER.md`
- `../07_sessions/SESSION-0004-PHASE0-INTEGRATOR.md`
- `../07_sessions/SESSION-0005-PHASE0-REPAIR-BUILDER.md`
- `../07_sessions/SESSION-0006-PHASE0-REVERIFIER.md`
- `../07_sessions/SESSION-0007-PHASE0-REVERIFICATION-INTEGRATOR.md`
- `../07_sessions/SESSION-0008-PHASE0-F2R1-REPAIR-BUILDER.md`
- `../07_sessions/SESSION-0009-PHASE0-REASONING-POLICY-BUILDER.md`
- `../07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md` — current exact-target PASS handoff; verifier evidence PR #10

This index is **navigational and derived only**. It does not override the authority hierarchy defined in `SOURCE_OF_TRUTH.md`, the bootstrap sequence in `COLD_START.md`, or current project truth in `STATE.md`. If any current-work value here ever disagrees with `STATE.md`, `STATE.md` wins and this index is stale until updated.
