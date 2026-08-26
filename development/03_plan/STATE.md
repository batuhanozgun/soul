# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-005 — Development Reasoning Policy  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-003 re-verification issued FAIL; verifier evidence was integrated; WP-004 F2-R1 repair is materially complete; owner-approved WP-005 reasoning-policy architecture change is active and requires fresh verification  
**Authoritative product branch:** `main`

## Current objective

Complete the owner-approved canonical development reasoning policy and its single-COLD_START integration, while keeping the F2-R1 repair separately traceable. Then cut one fresh verification target covering the complete changed Phase 0 system.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, and current next responsibility. The active WP named here supplies detailed responsibility, authority, required readings, acceptance criteria, and handoff.

`development/03_plan/NEXT_SESSION.md` and `development/03_plan/CHATGPT_PROJECT_ENTRY.md` are derived launch conveniences and intentionally store no copied current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed only by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Historical verification state

WP-003 independently verified exact draft PR #1 head `a02e36e5e71522995b74fb018a6b28235f1d7848` and issued **FAIL**.

- WP-000 criterion 2 — Single-source discipline: **FAIL**.
- F2 regression: **FAIL** because `BUILDER_STOP.md` contained a stale unqualified pointer to WP-001.
- WP-000 criteria 1 and 3–11: **PASS** at that exact target only.
- F1 regression: **PASS** at that exact target only.
- PD-001 regression: **PASS** at that exact target only.

Canonical verifier artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md`.

All of those results are stale for the current materially changed target.

## WP-004 repair state

WP-004 removed `development/03_plan/BUILDER_STOP.md` rather than preserving another routing surface. The builder marked the bounded F2-R1 repair materially complete and awaiting fresh independent verification.

Builder handoff: `development/07_sessions/SESSION-0008-PHASE0-F2R1-REPAIR-BUILDER.md`.

## WP-005 reasoning-policy state

The human owner approved the direction on 2026-08-26.

Current material outputs include:

- `development/01_governance/REASONING_POLICY.md`;
- `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`;
- proposed `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`;
- `COLD_START.md` integration that loads the policy as common governance;
- strengthened WP-000 acceptance criterion 12;
- derived `CHATGPT_PROJECT_ENTRY.md` for minimal Project Instructions.

These are builder outputs, not independently verified or accepted architecture.

## Process defect PD-002

During this bootstrap session, material WP-005 artefacts began before canonical `STATE.md` was first transitioned from completed WP-004 to WP-005. The owner-directed change had been queued and WP-005 existed, but the active-WP pointer lagged.

The defect is recorded at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`. The state is corrected here before further material WP-005 work. Fresh verification must inspect the final activation/current-work discipline; the defect is not erased by correction.

## Required next responsibility

**Designer/builder under `development/04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md`** until its material outputs and handoff are complete.

Then activate a **fresh verifier** against the exact changed PR #1 head. The fresh verifier must inspect all strengthened WP-000 criteria, F2-R1, reasoning-policy integration and PD-002 without relying on prior PASS fragments as current proof.

## Authority boundaries remain unchanged

No current session has authority to:

- edit historical verification results,
- weaken acceptance criteria to obtain a PASS,
- allow a builder to independently verify its own material output,
- accept ADR-0000 or ADR-0001 without their required paths,
- skip required adversarial review,
- merge PR #1 into `main` before gates are satisfied,
- begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until WP-000 is verified-complete on the current exact target, required adversarial review is resolved, relevant decisions have the correct status, and the Phase 0 PR is accepted into `main`.
