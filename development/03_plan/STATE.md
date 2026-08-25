# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-002 — Phase 0 Verification Repair  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-001 independent verification completed and integrated with overall FAIL; fresh builder repair is now required  
**Authoritative product branch:** `main`

## Current objective

Repair the exact Phase 0 defects established by independent verification without weakening WP-000 acceptance criteria or changing authority boundaries, then hand the changed exact PR #1 head to a fresh verifier.

## Verification result now part of canonical Phase 0 history

- WP-001 verification targeted exact draft PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71`.
- Overall result: **FAIL**.
- WP-000 criterion 1 — Cold-start sufficiency: **FAIL**.
- WP-000 criterion 2 — Single-source discipline: **FAIL**.
- WP-000 criteria 3–11: **PASS** at the verified target.
- Canonical verification artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`.
- Verifier handoff: `development/07_sessions/SESSION-0003-PHASE0-VERIFIER.md`.
- Verification records were integrated from PR #2 into `phase0/development-os` as merge commit `cbc1ab1fd8d675be9a7c4cd6f26feae75b957457`.
- WP-001 is complete as a verification activity. Its FAIL result does **not** verify or accept WP-000 or Phase 0.

## Active repair defects

WP-002 must address exactly these established defects:

1. **F1 — Cold-start order is internally contradictory.** See the canonical verification artefact.
2. **F2 — Current-work pointer has drifted outside canonical state.** See the canonical verification artefact. `development/03_plan/NEXT_SESSION.md` remains an intentionally unrepaired target for the fresh builder session; it must not be mistaken for newer canonical state.
3. **PD-001 — Missing verifier-result → canonical-state transition.** See `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md`.

F1 and F2 were not repaired by the verifier or by the integrator. PD-001 was recorded, not designed away, in this integration session.

## Required next responsibility

**Fresh designer/builder repair session.** Use the normal repository cold-start entry at `development/03_plan/COLD_START.md`; the active work package is `development/04_work/WP-002-PHASE0-VERIFICATION-REPAIR.md`.

The builder is authorised only to repair F1, F2, and PD-001 within WP-002. The builder must not:

- weaken or rewrite WP-000 acceptance criteria,
- edit the historical verification result to obtain a PASS,
- independently verify its own repair,
- accept ADR-0000,
- perform the required adversarial review,
- merge PR #1 into `main`,
- begin Phase 1.

After any material repair, the 2026-08-25 verification remains historical evidence for `1d2dd033ca3068484d841bcebf90e81ea84c7f71` and is stale for the changed target. A **new fresh verifier session** must verify the new exact PR #1 head.

## Proposed foundation on the Phase 0 branch

- SOUL is a general-purpose agentic architecture that creates the task-specific working system needed to pursue an intended outcome.
- Generality means generating domain/task-specific operating systems above a stable core, not forcing every problem through one fixed workflow.
- Persistent project truth must live outside chat/model memory.
- Missing capability creation is a first-class architectural requirement, governed by specification, isolation, testing, independent verification and admission.
- Completion is a system state, not an agent declaration.

These statements are not yet accepted into `main`; they remain proposed Phase 0 content pending successful repair, fresh independent verification, adversarial review, correct decision status, and human-owner acceptance where required.

## Phase 1 gate

Phase 1 does not begin until WP-000 is `verified-complete`, required adversarial review is resolved, relevant decisions have the correct status, and the Phase 0 PR is accepted into `main`.
