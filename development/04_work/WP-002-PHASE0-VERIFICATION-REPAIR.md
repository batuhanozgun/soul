# WP-002 — Phase 0 Verification Repair

**Status:** verification  
**Owner role:** designer/builder  
**Decision authority:** builder may repair the verified Phase 0 defects within this WP; WP-000 acceptance criteria, foundation authority, owner gates, and verifier independence may not be weakened or redefined  
**Branch:** `phase0/development-os`  
**PR:** #1 — draft

## Objective

Repair the exact defects exposed by the completed WP-001 verification so that the Phase 0 development operating system can be re-verified against the unchanged WP-000 acceptance criteria.

## Problem

Independent verification of draft PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71` produced an overall **FAIL**. WP-000 criteria 1 and 2 failed because the repository contained incompatible mandatory cold-start/read-order procedures and a stale duplicated current-work pointer. The subsequent integrator review also identified a separate process defect: the operating system lacked an explicit verifier-result → canonical-state transition mechanism.

These defects blocked Phase 0 acceptance. WP-002 has now produced a builder repair and must receive fresh independent verification against the changed exact PR #1 head.

## Scope

- repair verifier finding **F1 — Cold-start order is internally contradictory**;
- repair verifier finding **F2 — Current-work pointer has drifted outside canonical state**;
- repair **PD-001 — Missing verifier-result → canonical-state transition**;
- make only the governance/plan/work-package/session-launch changes needed to satisfy those defects and restore WP-000 criteria 1 and 2;
- preserve verification freshness, role separation, source-of-truth discipline, and no-false-completion controls;
- prepare a fresh independent verification responsibility after material repair.

## Non-scope

- weakening, rewriting, deleting, or replacing any WP-000 acceptance criterion;
- declaring WP-000, ADR-0000, Phase 0, or PR #1 accepted;
- performing the independent re-verification in the builder session;
- performing adversarial review;
- beginning Phase 1;
- broad governance cleanup unrelated to F1, F2, or PD-001;
- modifying the historical verifier artefact or verifier session record to make the FAIL disappear.

## Required reading

The builder must use repository state, not prior-chat memory. Start from `development/03_plan/STATE.md` and this active WP as directed by the repository cold-start surface, then inspect all of the following repair evidence and controls before editing:

- `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`
- `development/07_sessions/SESSION-0003-PHASE0-VERIFIER.md`
- `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`
- `development/04_work/WP-000-DEVELOPMENT-OS.md`
- `development/04_work/WP-001-PHASE0-VERIFICATION.md`
- `development/03_plan/COLD_START.md`
- `development/01_governance/WORKING_PROTOCOL.md`
- `development/01_governance/SOURCE_OF_TRUTH.md`
- `development/03_plan/NEXT_SESSION.md`
- `development/03_plan/WORKSPACE_INDEX.md`
- `development/01_governance/ROLE_MODEL.md`
- `development/01_governance/CHANGE_POLICY.md`
- `development/01_governance/VERIFICATION_POLICY.md`
- `development/03_plan/PR_GATE.md`

**F1 cold-start note:** the pre-repair repository contained contradictory order instructions; that contradiction was the repair target. The builder did not treat the old orders as simultaneously satisfiable. The repair design assigns fresh-session sequencing to one explicit authority and makes WP reading order subordinate to that sequence.

## Inputs and dependencies

- PR #2 verifier records are integrated into `phase0/development-os`.
- Canonical verification artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`.
- Verified failed target: draft PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71`.
- Overall verification result: **FAIL**.
- Exact verifier findings: F1 and F2 in the canonical verification artefact.
- Separate integrator process defect: PD-001.
- WP-000 acceptance criteria remain authoritative and unchanged.

## Unknowns and assumptions

- The historical verification remains exact evidence for the old target only.
- Historical session/verifier records remain evidence and were not rewritten to erase the original failure.
- The new verifier must decide whether the implemented precedence and transition mechanisms actually satisfy WP-000; builder rationale is not proof.
- A branch commit cannot safely embed its own final commit SHA inside a tracked handoff file without changing that SHA. Therefore the exact final PR #1 head is authoritative in GitHub PR metadata and is independently captured by the verifier at start; the builder close additionally records the observed final SHA in a PR comment after repository-changing close commits, so recording the SHA does not itself move the target.

## Outputs

### F1 — cold-start/read-order repair

- `development/03_plan/COLD_START.md` — single authoritative bootstrap sequencing procedure; WP/local reading orders are constrained to Step 3.
- `development/01_governance/WORKING_PROTOCOL.md` — delegates bootstrap sequence to COLD_START instead of defining a competing ordered procedure.
- `development/01_governance/SOURCE_OF_TRUTH.md` — separates semantic authority from bootstrap sequencing and makes current-state home explicit.
- `development/04_work/WP_TEMPLATE.md` — prevents future WPs from redefining COLD_START Steps 1–2.

### F2 — single current-work home

- `development/03_plan/NEXT_SESSION.md` — converted to a derived launch view that stores no current phase/WP/role/target/next-responsibility value.
- `development/01_governance/SOURCE_OF_TRUTH.md` — states that current phase/active WP/next responsibility live in `STATE.md` + active WP and that derived views are subordinate.
- `development/03_plan/WORKSPACE_INDEX.md` — updated as a subordinate navigational view at builder close.

### PD-001 — verifier-result → canonical-state transition

- `development/01_governance/VERIFICATION_POLICY.md` — explicit Integrator-owned trigger, sequence, PASS/FAIL/NOT VERIFIED routing, transition-only/material freshness distinction, and no-false-completion controls.
- `development/01_governance/ROLE_MODEL.md` — explicit Integrator transition authority and prohibitions; verifier remains unable to integrate/repair its own result.
- `development/01_governance/WORKING_PROTOCOL.md` — verifier close hands canonical transition to a separate Integrator.
- `development/03_plan/PR_GATE.md` — distinguishes verification/review evidence PR integration from target acceptance.
- `development/02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md` — records the proposed governance change without accepting the ADR or bypassing its owner gate.
- `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md` — records implemented repair as pending independent verification.

### Fresh verification preparation

- `development/04_work/WP-003-PHASE0-REVERIFICATION.md` — fresh verifier responsibility for the changed exact PR #1 head, with all eleven WP-000 criteria plus F1/F2/PD-001 regression checks.
- builder close state/index/handoff updates under `development/03_plan/` and `development/07_sessions/`.

## Acceptance criteria

1. **F1 resolved:** all mandatory cold-start/read-order control surfaces are mutually satisfiable, or one explicit authoritative ordering/precedence mechanism makes their relationship unambiguous without relying on chat memory.
2. **F2 resolved:** the current-work fact has one authoritative home; operational/derived views cannot present a conflicting stale active-WP value, and any derived status pointer is explicitly subordinate to canonical state.
3. **PD-001 resolved:** the repository explicitly defines the authorised verifier-result → canonical-state transition, including integration of verifier evidence, result-dependent routing, state/WP updates, repair activation, and verification-staleness handling.
4. **WP-000 criteria preserved:** the text and meaning of all eleven WP-000 acceptance criteria are not weakened or changed to obtain a PASS.
5. **Verification history preserved:** `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md` and `development/07_sessions/SESSION-0003-PHASE0-VERIFIER.md` remain an accurate historical record of the FAIL against `1d2dd033ca3068484d841bcebf90e81ea84c7f71`.
6. **Cold-start continuity restored:** a repository-only fresh-session simulation can identify current phase, active WP, authority hierarchy, mandatory readings, role, and exact next responsibility without unstated precedence or prior-chat replay.
7. **No authority expansion:** the repair does not accept ADR-0000, bypass human-owner gates, perform adversarial review, begin Phase 1, or allow a builder to self-certify the repair.
8. **Fresh verification prepared:** after material repair, canonical state points to a fresh verifier responsibility that must verify the new exact PR #1 head rather than reusing WP-001's result.

## Required verification

- a **fresh verifier session** under `development/04_work/WP-003-PHASE0-REVERIFICATION.md`;
- re-derive expected results from unchanged WP-000 before relying on builder rationale;
- verify all eleven WP-000 acceptance criteria, not only F1/F2/PD-001;
- bind the new result to the exact changed draft PR #1 head commit;
- explicitly test F1, F2, and the new PD-001 transition mechanism;
- treat the prior 2026-08-25 verification as stale for the changed target;
- no builder self-verification;
- after a future all-PASS verification, separate adversarial review is still required before Phase 0 acceptance.

## Evidence obligations

The builder handoff must identify:

- each changed artefact and which of F1, F2, or PD-001 it addresses;
- why the repair does not weaken WP-000 acceptance criteria or authority controls;
- the exact resulting PR #1 head commit to be independently verified, recorded without moving the target;
- any unresolved issue that prevents a clean verifier handoff.

## Risks

- repairing F1 by creating another competing read-order instruction;
- repairing F2 by moving the duplicate rather than eliminating/subordinating it;
- repairing PD-001 with another status document that itself becomes a duplicate source of truth;
- editing historical verifier evidence instead of repairing current controls;
- broadening the repair into Phase 1 design;
- treating the previous FAIL as current evidence after the target changes;
- allowing transition-only integration to hide substantive repair/design changes.

## Completion state

Builder responsibility: **complete; independent verification pending**.

WP-002 is now in `verification`, not `verified-complete`. The builder has implemented the scoped repairs and prepared a fresh verifier package, but none of F1, F2, PD-001, WP-000, ADR-0000, Phase 0, or PR #1 is accepted merely because these edits exist.

## Handoff

Current next responsibility: **fresh verifier session under WP-003 — Phase 0 Fresh Re-verification**.

The verifier must independently capture the exact current PR #1 head, follow `COLD_START.md`, verify all eleven unchanged WP-000 criteria plus F1/F2/PD-001 regressions, write only verification evidence/handoff, and stop. Canonical result integration belongs to a later separate Integrator session under `VERIFICATION_POLICY.md`.
