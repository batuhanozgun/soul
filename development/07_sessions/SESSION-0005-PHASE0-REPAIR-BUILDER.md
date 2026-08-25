# SESSION-0005 — Phase 0 verification repair builder

**Date:** 2026-08-25  
**Work package:** WP-002 — Phase 0 Verification Repair  
**Role:** designer/builder  
**Branch / PR:** `phase0/development-os`, draft PR #1

## Responsibility for this session

Repair only the exact Phase 0 defects established by WP-001/SESSION-0003 verification and SESSION-0004 integration: F1, F2, and PD-001. Preserve unchanged WP-000 acceptance criteria and authority gates, then hand the materially changed PR #1 target to a fresh verifier without self-verifying the repair.

## Inputs read

Cold-start and active work:

- `development/03_plan/STATE.md`
- `development/03_plan/COLD_START.md`
- `development/04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md`

Role/governance/foundation:

- `development/01_governance/SOURCE_OF_TRUTH.md`
- `development/01_governance/WORKING_PROTOCOL.md`
- `development/01_governance/ROLE_MODEL.md`
- `development/01_governance/DECISION_POLICY.md`
- `development/01_governance/CHANGE_POLICY.md`
- `development/01_governance/VERIFICATION_POLICY.md`
- `development/00_foundation/VISION.md`
- `development/00_foundation/DEFINITION.md`
- `development/00_foundation/NON_NEGOTIABLES.md`
- `development/00_foundation/SUCCESS_CRITERIA.md`

Repair evidence and controls:

- `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`
- `development/07_sessions/SESSION-0003-PHASE0-VERIFIER.md`
- `development/07_sessions/SESSION-0004-PHASE0-INTEGRATOR.md`
- `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`
- `development/04_work/WP-000-DEVELOPMENT-OS.md`
- `development/04_work/WP-001-PHASE0-VERIFICATION.md`
- `development/03_plan/NEXT_SESSION.md`
- `development/03_plan/WORKSPACE_INDEX.md`
- `development/03_plan/PR_GATE.md`
- `development/04_work/WP_TEMPLATE.md`
- `development/07_sessions/SESSION-0002-NEXT-VERIFIER-BRIEF.md`
- proposed `development/02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md`
- draft PR #1 metadata, including the current branch/head during work.

## Repair design

### F1 — cold-start order contradiction

The repair does not try to pretend the old orders were compatible. It assigns one explicit sequencing authority:

- `development/03_plan/COLD_START.md` owns fresh-session bootstrap order;
- `SOURCE_OF_TRUTH.md` owns semantic authority and explicitly distinguishes it from bootstrap sequencing;
- `WORKING_PROTOCOL.md` delegates to COLD_START instead of restating a competing sequence;
- active WPs may order only their COLD_START Step 3 required-reading material;
- `WP_TEMPLATE.md` encodes that constraint for future work packages;
- historical launch briefs/handoffs remain evidence/continuity artefacts and cannot override current COLD_START sequencing.

### F2 — stale duplicated current-work pointer

The repair removes current-state materialisation from `NEXT_SESSION.md` rather than merely updating its stale value:

- `STATE.md` + the active WP remain the authoritative current phase/WP/next-responsibility home;
- `NEXT_SESSION.md` is now a derived launch convenience that stores none of those current values;
- `SOURCE_OF_TRUTH.md` explicitly requires any derived current-state view to be subordinate;
- `WORKSPACE_INDEX.md` remains navigational only and is updated at close.

### PD-001 — missing verifier-result → canonical-state transition

The repair uses existing governance surfaces rather than introducing another state store:

- `VERIFICATION_POLICY.md` defines a separate Integrator-owned result transition with exact-target/result provenance checks, evidence-only integration, verification-activity closure, `STATE.md` routing, PASS/FAIL/NOT VERIFIED branches, transition-only/material freshness handling, and no-false-completion prohibitions;
- `ROLE_MODEL.md` makes Integrator transition authority explicit while prohibiting result reinterpretation, hidden repair, or gate bypass;
- `WORKING_PROTOCOL.md` makes verifier close stop before canonical integration;
- `PR_GATE.md` distinguishes a verifier/reviewer evidence PR from the material target PR and states that merging FAIL/NOT VERIFIED evidence is not target acceptance;
- ADR-0000 records the proposed cross-cutting governance change but remains **proposed** and retains its human-owner decision gate;
- the PD-001 defect record is marked repair-implemented/pending independent verification, not resolved by builder declaration.

## Outputs produced

F1:

- updated `development/03_plan/COLD_START.md`
- updated `development/01_governance/WORKING_PROTOCOL.md`
- updated `development/01_governance/SOURCE_OF_TRUTH.md`
- updated `development/04_work/WP_TEMPLATE.md`

F2:

- updated `development/03_plan/NEXT_SESSION.md`
- updated `development/01_governance/SOURCE_OF_TRUTH.md`
- close-time update to `development/03_plan/WORKSPACE_INDEX.md`

PD-001:

- updated `development/01_governance/VERIFICATION_POLICY.md`
- updated `development/01_governance/ROLE_MODEL.md`
- updated `development/01_governance/WORKING_PROTOCOL.md`
- updated `development/03_plan/PR_GATE.md`
- updated proposed `development/02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md`
- updated `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`

Fresh verification preparation:

- created `development/04_work/WP-003-PHASE0-REVERIFICATION.md`
- updated `development/04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md` to builder-complete / verification-pending
- close-time update to `development/03_plan/STATE.md`
- this builder handoff.

## Decisions taken or proposed

- **Work-package repair design:** one bootstrap sequencing authority (`COLD_START.md`) plus semantic authority (`SOURCE_OF_TRUTH.md`), instead of attempting to keep multiple mandatory read orders synchronized.
- **Work-package repair design:** remove current-work values from `NEXT_SESSION.md` so it cannot become a second state store.
- **Architecture/governance proposal recorded, not accepted:** verifier result integration is a separate Integrator transition under `VERIFICATION_POLICY.md`. ADR-0000 was updated to record this proposal but its status remains `proposed`; no human-owner decision was taken.

No WP-000 acceptance criterion was changed. No foundation document was changed. No verifier result was edited. ADR-0000 was not accepted. No adversarial review or Phase 1 work was performed.

## Why WP-000 and authority controls were not weakened

- all eleven WP-000 acceptance-criterion texts remain unchanged;
- verifier independence is strengthened by preventing the verifier from integrating/repairing its own result;
- F1 is fixed by removing competing sequencing authority, not by relaxing cold-start sufficiency;
- F2 is fixed by removing duplicated current state, not by declaring stale duplication acceptable;
- PD-001 routes FAIL/NOT VERIFIED into bounded repair/investigation and PASS into adversarial review when required; it does not make PASS equal acceptance;
- material repair still makes prior verification stale for the changed target;
- owner/ADR gates and `main` acceptance remain outside builder/integrator authority.

## Verification status

**Builder repair only — NOT independently verified.**

Historical WP-001 result remains **FAIL** for exact old target `1d2dd033ca3068484d841bcebf90e81ea84c7f71`. It is evidence of the original defects, not current verification of the changed PR #1 target.

The fresh verification responsibility is `development/04_work/WP-003-PHASE0-REVERIFICATION.md` and must verify all eleven unchanged WP-000 criteria plus explicit F1/F2/PD-001 regressions.

## Exact target recording

The verifier must independently capture the exact draft PR #1 head SHA at verification start and re-check it before closing.

A tracked handoff file cannot contain the SHA of the final commit that contains that same handoff without changing the SHA again. To avoid creating a self-referential/stale duplicate, the authoritative live head remains GitHub PR #1 metadata. After all repository-changing close commits are complete, this builder session records the observed final PR #1 head SHA in a **non-head-changing PR comment**. That PR comment is a handoff evidence pointer; the verifier still independently captures PR metadata rather than trusting the builder's copy.

## Unresolved items

- F1, F2, and PD-001 are **repair claims pending independent verification**.
- WP-000 / Phase 0 remain unverified-complete and unaccepted.
- ADR-0000 remains proposed and still requires its declared human-owner path after required verification/review.
- Separate adversarial review remains required after a future all-PASS re-verification.
- No issue prevents a clean verifier handoff; the verifier may still find new defects or reject this repair.

## Next required responsibility

**Open a new fresh verifier session for WP-003. Do not continue verification in this builder chat.**

The verifier starts through `development/03_plan/COLD_START.md`, derives expected results from unchanged WP-000/current governance before reading this builder handoff, captures the exact current draft PR #1 head, verifies every WP-000 criterion plus F1/F2/PD-001 regressions, writes only verifier evidence/handoff, and stops for a later separate Integrator result transition.
