# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-003 — Phase 0 Fresh Re-verification  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-002 builder repair is materially complete; F1/F2/PD-001 repairs are pending fresh independent verification against the changed exact PR #1 head  
**Authoritative product branch:** `main`

## Current objective

Freshly and independently re-verify the repaired Phase 0 development operating system against the **unchanged WP-000 acceptance criteria**, including explicit regression tests for F1, F2, and PD-001. The verifier must bind the new result to the exact draft PR #1 head captured at verification start.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, and current next responsibility. The active WP named here supplies the detailed responsibility, authority, required readings, acceptance criteria, and handoff.

`development/03_plan/NEXT_SESSION.md` is a derived launch convenience and intentionally stores no copied current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Historical verification now stale for the repaired target

- WP-001 verification targeted exact draft PR #1 head `1d2dd033ca3068484d841bcebf90e81ea84c7f71`.
- Overall historical result: **FAIL**.
- WP-000 criterion 1 — Cold-start sufficiency: **FAIL**.
- WP-000 criterion 2 — Single-source discipline: **FAIL**.
- WP-000 criteria 3–11: **PASS** at that historical target only.
- Canonical historical verification artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-25.md`.
- Historical verifier handoff: `development/07_sessions/SESSION-0003-PHASE0-VERIFIER.md`.
- WP-001 is complete as a verification activity. Its FAIL result does **not** verify or accept WP-000 or Phase 0 and is stale for the materially changed WP-002 target.

## WP-002 repair state

WP-002 builder responsibility is complete and the package is in `verification`, not `verified-complete`.

Repair claims awaiting independent verification:

1. **F1 — Cold-start order contradiction:** repaired by assigning fresh-session sequencing to `COLD_START.md`, separating semantic authority from sequencing in `SOURCE_OF_TRUTH.md`, delegating `WORKING_PROTOCOL.md` to COLD_START, and constraining WP-required reading order to COLD_START Step 3.
2. **F2 — Current-work pointer drift:** repaired by removing current phase/WP/role/target materialisation from `NEXT_SESSION.md` and keeping current-work truth here plus the active WP.
3. **PD-001 — Missing verifier-result → canonical-state transition:** repaired by an Integrator-owned transition in `VERIFICATION_POLICY.md`, with supporting role/working/PR-gate controls. The defect record is `development/06_reviews/PROCESS-DEFECT-PD-001-VERIFIER-STATE-TRANSITION.md` and remains pending independent verification.

Builder handoff: `development/07_sessions/SESSION-0005-PHASE0-REPAIR-BUILDER.md`.

These statements describe the builder's claimed repair state; they are not independent evidence that the repairs pass.

## Required next responsibility

**Fresh verifier session under `development/04_work/WP-003-PHASE0-REVERIFICATION.md`.**

The verifier must:

- start through `development/03_plan/COLD_START.md`;
- independently capture the exact current draft PR #1 head SHA from PR metadata;
- derive expected results from unchanged WP-000/current governance before reading the WP-002 builder handoff;
- re-verify all eleven WP-000 acceptance criteria;
- explicitly test F1, F2, and PD-001 regressions;
- re-check target freshness before closing;
- perform no repair, canonical result integration, ADR acceptance, adversarial review, target merge, or Phase 1 work.

After the verifier closes, a **separate Integrator session** must execute the verifier-result → canonical-state transition in `VERIFICATION_POLICY.md`. The verifier does not perform that transition itself.

## Authority boundaries remain unchanged

No current session or repair has authority to:

- weaken or rewrite WP-000 acceptance criteria,
- edit the historical verification result to obtain a PASS,
- allow a builder to self-verify material repair,
- accept ADR-0000 without its declared human-owner gate,
- skip required adversarial review,
- merge PR #1 into `main` before gates are satisfied,
- begin Phase 1.

## Proposed foundation on the Phase 0 branch

- SOUL is a general-purpose agentic architecture that creates the task-specific working system needed to pursue an intended outcome.
- Generality means generating domain/task-specific operating systems above a stable core, not forcing every problem through one fixed workflow.
- Persistent project truth must live outside chat/model memory.
- Missing capability creation is a first-class architectural requirement, governed by specification, isolation, testing, independent verification and admission.
- Completion is a system state, not an agent declaration.

These statements are not yet accepted into `main`; they remain proposed Phase 0 content pending successful fresh independent verification, adversarial review, correct decision status, and human-owner acceptance where required.

## Phase 1 gate

Phase 1 does not begin until WP-000 is `verified-complete`, required adversarial review is resolved, relevant decisions have the correct status, and the Phase 0 PR is accepted into `main`.
