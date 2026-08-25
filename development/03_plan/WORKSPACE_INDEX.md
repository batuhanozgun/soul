# SOUL DEVELOPMENT INDEX

## Foundation
- `../00_foundation/VISION.md`
- `../00_foundation/DEFINITION.md`
- `../00_foundation/SUCCESS_CRITERIA.md`
- `../00_foundation/NON_NEGOTIABLES.md`

## Governance
- `../01_governance/SOURCE_OF_TRUTH.md`
- `../01_governance/WORKING_PROTOCOL.md`
- `../01_governance/ROLE_MODEL.md`
- `../01_governance/DECISION_POLICY.md`
- `../01_governance/VERIFICATION_POLICY.md`
- `../01_governance/CHANGE_POLICY.md`

## Planning
- `ROADMAP.md`
- `STATE.md`
- `COLD_START.md`
- `PHASE_GATE.md`
- `PR_GATE.md`
- `NEXT_SESSION.md` — derived launch view; no authoritative current-state values
- `BUILDER_STOP.md`

## Current work
- Active: `../04_work/WP-003-PHASE0-REVERIFICATION.md` — fresh verifier responsibility
- Repair package awaiting verification: `../04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md`
- Parent package under re-verification: `../04_work/WP-000-DEVELOPMENT-OS.md`
- Historical completed verification activity: `../04_work/WP-001-PHASE0-VERIFICATION.md` — old target result FAIL

## Verification and repair evidence
- `../06_reviews/VERIFICATION-WP-000-2026-08-25.md` — historical FAIL against exact PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71`; stale for repaired target
- `../06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md` — repair implemented; pending independent verification

## Decisions
- `../02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md` — proposed; includes repaired governance proposal and still requires its declared owner path

## Templates
- ADR: `../01_governance/ADR_TEMPLATE.md`
- Work package: `../04_work/WP_TEMPLATE.md`
- Evidence: `../05_evidence/EVIDENCE_TEMPLATE.md`
- Verification: `../06_reviews/VERIFICATION_TEMPLATE.md`
- Adversarial review: `../06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`
- Session handoff: `../07_sessions/SESSION_TEMPLATE.md`

## Handoffs and historical launch records
- Completed builder record: `../07_sessions/SESSION-0001-PHASE0-BUILDER.md`
- Historical WP-001 verifier launch brief: `../07_sessions/SESSION-0002-NEXT-VERIFIER-BRIEF.md` — not a current cold-start authority
- Completed historical verifier record: `../07_sessions/SESSION-0003-PHASE0-VERIFIER.md`
- Completed verification-result integrator record: `../07_sessions/SESSION-0004-PHASE0-INTEGRATOR.md`
- Current repair-builder handoff: `../07_sessions/SESSION-0005-PHASE0-REPAIR-BUILDER.md`

This index is **navigational and derived only**. It does not override the authority hierarchy defined in `SOURCE_OF_TRUTH.md`, the bootstrap sequence in `COLD_START.md`, or current project truth in `STATE.md`. If any current-work value here ever disagrees with `STATE.md`, `STATE.md` wins and this index is stale until mechanically updated.
