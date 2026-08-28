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
- Active: `../04_work/WP-018-PHASE0-CANDIDATE-SET-CONVERGENCE-VERIFICATION.md` — fresh separate verifier for PR #22 exact target `5bd0db2...`, result-control attempt 1, including the provisional WP-local activation bridge
- Builder-complete repair: `../04_work/WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md` — PR #22 exact target `5bd0db2...` from canonical base `4524f21...`; producer-only, fresh independent verification/re-review outstanding
- Completed adversarial re-review: `../04_work/WP-016-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEW.md` — **Requires repair** for PR #19 exact target `2f5508c...`; F-AR-006/F-AR-007 stand; evidence PR #21 integrated evidence-only as `276132a8...`
- Completed verification activity: `../04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md` — **PASS** for PR #19 exact target `2f5508c...`, activation `5368abd...` and binding `3d49561...`; evidence PR #20 integrated evidence-only as `df9c9c12...`
- Builder-complete repair: `../04_work/WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md` — PR #19 exact target `2f5508c...` from canonical base `dca520...`; WP-015 PASS, WP-016 **Requires repair**, F-AR-006/F-AR-007 routed to WP-017
- Completed adversarial re-review: `../04_work/WP-013-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEW.md` — **Requires repair** for PR #16 exact target `adf067e...`; F-AR-005 medium/material stands; evidence PR #18 integrated evidence-only as `fda96891...`
- Completed verification activity: `../04_work/WP-012-PHASE0-PENDING-RESULT-CONTROL-VERIFICATION.md` — **PASS** for PR #16 exact target `adf067e...` and activation `7c625107...`; evidence PR #17 integrated evidence-only as `2d732950...`
- Builder-complete repair: `../04_work/WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md` — PR #16 exact target `adf067e...` from base `8dcdc750...`; WP-012 PASS, WP-013 **Requires repair**, F-AR-005 routed to WP-014
- Completed adversarial re-review: `../04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md` — **Requires repair** for exact target `a45b463...`; reviewer evidence PR #15 integrated evidence-only as `c8fc17bc...`
- Completed verification activity: `../04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md` — **PASS** for exact target `a45b463...`; verifier evidence PR #14 integrated evidence-only as `37f4bceb...`
- Builder-complete prior repair: `../04_work/WP-008-PHASE0-F-AR-001-REPAIR.md` — exact target `a45b463...`; WP-009 verified PASS, but WP-010 adversarial re-review issued **Requires repair**
- Completed adversarial review: `../04_work/WP-007-PHASE0-ADVERSARIAL-REVIEW.md` — historical **Requires repair**; F-AR-001 stands against exact old material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`
- Completed verification activity: `../04_work/WP-006-PHASE0-REASONING-REVERIFICATION.md` — historical **PASS** against exact old material target `c690f858...`; not certification of `a45b463...`
- Material reasoning-policy architecture: `../04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md` — ADR-0001 remains proposed/not Phase-accepted
- Completed bounded repair: `../04_work/WP-004-PHASE0-F2R1-REPAIR.md` — F2-R1 regression PASS at old target `c690f858...`
- Parent package: `../04_work/WP-000-DEVELOPMENT-OS.md` — Phase 0 remains unaccepted pending WP-018 verification, fresh adversarial re-review and decision/owner/PR gates
- Historical completed verification activity: `../04_work/WP-003-PHASE0-REVERIFICATION.md` — exact old target `a02e36e5...`, result FAIL
- Historical completed verification activity: `../04_work/WP-001-PHASE0-VERIFICATION.md` — old target result FAIL
- Historical repair package: `../04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md`

## Verification, reviews, defects and evidence
- `../06_reviews/ADVERSARIAL-REREVIEW-WP-000-2f5508c1-2026-08-27.md` — WP-016 result: **Requires repair** for exact PR #19 target `2f5508c...`; F-AR-006 medium/material and F-AR-007 low/evidence-model correctness stand; PR #21 integrated evidence-only as `276132a8...`
- `../06_reviews/VERIFICATION-WP-000-2f5508c1-2026-08-27.md` — WP-015 issued **PASS** for exact PR #19 target `2f5508c...`, activation `5368abd...` and binding `3d49561...`; PR #20 integrated evidence-only as `df9c9c12...`
- `../05_evidence/F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md` — WP-017 producer regression record on PR #22 target; 67/67 declared cases plus deliberate red mutation, not independent proof
- `../06_reviews/ADVERSARIAL-REREVIEW-WP-000-adf067e4-2026-08-26.md` — WP-013 result: **Requires repair** for exact target `adf067e...`; F-AR-005 medium/material stands; PR #18 integrated evidence-only as `fda96891...`
- `../06_reviews/VERIFICATION-WP-000-adf067e4-2026-08-26.md` — WP-012 issued **PASS** for exact PR #16 target `adf067e...` and activation `7c625107...`; PR #17 integrated evidence-only as `2d732950...`
- `../05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md` — WP-011 producer regression record on PR #16 target; 13 declared cases, not independent proof
- `../05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md` — proposed exact-bound canonical Integrator resolution/containment template on PR #22 target
- `../05_evidence/pending_result_control_regression.py` — executable producer decision-table regression model on PR #22 target
- `../06_reviews/ADVERSARIAL-REREVIEW-WP-000-a45b463b-2026-08-26.md` — WP-010 result: **Requires repair**; F-AR-002/F-AR-003 medium/material and F-AR-004 low/timing-dependent stand; PR #15 integrated evidence-only
- `../06_reviews/VERIFICATION-WP-000-a45b463b-2026-08-26.md` — WP-009 issued **PASS** against exact repair target `a45b463...`; verifier evidence PR #14 integrated evidence-only
- `../05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md` — WP-008 producer regression evidence on PR #13 target; covers WP-006/PR #10 verifier case, WP-007/PR #12 reviewer case, stale/conflict/unavailable cases; not independent proof
- `../06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md` — WP-007 result: **Requires repair**; surviving **F-AR-001**, medium/material; exact old target `c690f858...`
- `../06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md` — historical issued verification: **PASS** against exact old target `c690f858...`; verifier evidence PR #10 integrated evidence-only
- `../06_reviews/VERIFICATION-WP-000-2026-08-26.md` — historical FAIL against exact target `a02e36e5e71522995b74fb018a6b28235f1d7848`; stale for current material target
- `../06_reviews/VERIFICATION-WP-000-2026-08-25.md` — historical FAIL against exact old target `1d2dd033ca3068484d841bcebf90e81ea84c7f71`
- `../06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`
- `../06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md` — preserved; WP-008 did not broaden scope to repair it
- `../05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md` — source-to-SOUL synthesis evidence for WP-005

## Decisions
- `../02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md` — proposed; still requires its declared owner path
- `../02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md` — proposed; owner direction approved, acceptance path still pending
- `../02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md` — revised/proposed on exact WP-017 repair target `5bd0db2...`; fresh WP-018 verification and later re-review remain outstanding

## Templates
- ADR: `../01_governance/ADR_TEMPLATE.md`
- Work package: `../04_work/WP_TEMPLATE.md`
- Evidence: `../05_evidence/EVIDENCE_TEMPLATE.md`
- Verification: `../06_reviews/VERIFICATION_TEMPLATE.md`
- Adversarial review: `../06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`
- Pending-result resolution: `../05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md` — proposed on exact PR #16 target
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
- `../07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md` — exact-target historical PASS handoff; verifier evidence PR #10
- `../07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md` — PASS integration and observed duplicate-verifier transition-discoverability trace
- `../07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md` — WP-007 review handoff; **Requires repair**, F-AR-001 stands; reviewer evidence PR #12
- `../07_sessions/SESSION-0013-PHASE0-WP007-INTEGRATOR.md` — reviewer evidence integration and routing to WP-008; no repair
- `../07_sessions/SESSION-0014-PHASE0-F-AR-001-REPAIR-BUILDER.md` — WP-008 builder close; exact repair target PR #13 / `a45b463...`; fresh verifier WP-009 next
- `../07_sessions/SESSION-0015-PHASE0-F-AR-001-REPAIR-VERIFIER.md` — WP-009 **PASS** handoff for exact target `a45b463...`; verifier evidence PR #14
- `../07_sessions/SESSION-0016-PHASE0-WP009-INTEGRATOR.md` — PR #14 evidence integration and canonical PASS routing to WP-010; no repair/acceptance
- `../07_sessions/SESSION-0017-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEWER.md` — WP-010 **Requires repair** handoff; F-AR-002/F-AR-003/F-AR-004 stand; reviewer evidence PR #15
- `../07_sessions/SESSION-0018-PHASE0-WP010-INTEGRATOR.md` — PR #15 evidence integration and canonical **Requires repair** routing to WP-011; no repair/acceptance
- `../07_sessions/SESSION-0019-PHASE0-PENDING-RESULT-CONTROL-BUILDER.md` — WP-011 builder close; PR #16 exact target `adf067e...`; provisional activation `7c625107...`; WP-012 verifier next
- `../07_sessions/SESSION-0020-PHASE0-PENDING-RESULT-CONTROL-VERIFIER.md` — WP-012 **PASS** for exact target `adf067e...`; verifier evidence PR #17 integrated evidence-only as `2d732950...`
- `../07_sessions/SESSION-0021-PHASE0-WP012-INTEGRATOR.md` — PR #17 evidence integration, WP-012 PASS binding and canonical WP-013 adversarial re-review activation; no review/repair/acceptance
- `../07_sessions/SESSION-0022-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEWER.md` — WP-013 **Requires repair** for exact target `adf067e...`; F-AR-005 medium/material; evidence PR #18
- `../07_sessions/SESSION-0023-PHASE0-WP013-INTEGRATOR.md` — PR #18 evidence integration, WP-013 **Requires repair** binding and canonical WP-014 bounded repair activation; no repair/acceptance
- `../07_sessions/SESSION-0024-PHASE0-MOVING-CANDIDATE-CONVERGENCE-BUILDER.md` — WP-014 builder close; PR #19 exact target `2f5508c...`; WP-015 verifier routing prepared for separate Integrator activation
- `../07_sessions/SESSION-0025-PHASE0-WP015-ACTIVATION-INTEGRATOR.md` — exact builder-close integration and WP-015 activation/binding; no verification/review/repair/acceptance
- `../07_sessions/SESSION-0026-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFIER.md` — WP-015 **PASS** for exact target `2f5508c...`; verifier evidence PR #20 integrated evidence-only as `df9c9c12...`
- `../07_sessions/SESSION-0027-PHASE0-WP015-INTEGRATOR.md` — PR #20 evidence integration, WP-015 PASS binding and canonical WP-016 adversarial re-review activation; no review/repair/acceptance
- `../07_sessions/SESSION-0028-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEWER.md` — WP-016 **Requires repair** for exact target `2f5508c...`; F-AR-006/F-AR-007 stand; reviewer evidence PR #21
- `../07_sessions/SESSION-0029-PHASE0-WP016-RESULT-INTEGRATOR.md` — PR #21 evidence integration, WP-016 **Requires repair** binding and canonical WP-017 bounded repair activation; no repair/acceptance
- `../07_sessions/SESSION-0030-PHASE0-CANDIDATE-SET-CONVERGENCE-BUILDER.md` — WP-017 builder close; PR #22 exact target `5bd0db2...`; WP-018 verifier routing prepared for separate Integrator activation
- `../07_sessions/SESSION-0031-PHASE0-WP018-ACTIVATION-INTEGRATOR.md` — exact builder-close integration and WP-018 activation/binding; no verification/review/repair/acceptance

This index is **navigational and derived only**. It does not override the authority hierarchy defined in `SOURCE_OF_TRUTH.md`, the bootstrap sequence in `COLD_START.md`, or current project truth in `STATE.md`. If any current-work value here ever disagrees with `STATE.md`, `STATE.md` wins and this index is stale until updated.
