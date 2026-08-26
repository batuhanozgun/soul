# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-004 — Phase 0 F2-R1 Repair  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-003 fresh re-verification completed with exact-target **FAIL**; verifier evidence is integrated; bounded F2-R1 builder repair is now active  
**Authoritative product branch:** `main`

## Current objective

Repair the single remaining verifier finding F2-R1 without weakening WP-000 acceptance criteria or widening the verifier-triggered repair scope. The stale next-responsibility pointer in `development/03_plan/BUILDER_STOP.md` must stop competing with this canonical state.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, and current next responsibility. The active WP named here supplies the detailed responsibility, authority, required readings, acceptance criteria, and handoff.

`development/03_plan/NEXT_SESSION.md` is a derived launch convenience and intentionally stores no copied current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Current verification result

WP-003 independently verified exact draft PR #1 head `a02e36e5e71522995b74fb018a6b28235f1d7848` and issued **FAIL**.

- WP-000 criterion 2 — Single-source discipline: **FAIL**.
- F2 regression: **FAIL** because `BUILDER_STOP.md` contained a stale unqualified pointer to WP-001.
- WP-000 criteria 1 and 3–11: **PASS** at that exact target only.
- F1 regression: **PASS** at that exact target only.
- PD-001 regression: **PASS** at that exact target only.

Canonical verifier artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md`.
Verifier handoff: `development/07_sessions/SESSION-0006-PHASE0-REVERIFIER.md`.

The verifier evidence PR #9 was integrated transition-only into `phase0/development-os`. Evidence integration is not acceptance of the target.

## Required next responsibility

**Designer/builder session under `development/04_work/WP-004-PHASE0-F2R1-REPAIR.md`.**

The builder must repair only the exact F2-R1 stale-pointer class and leave the result awaiting fresh verification. It must not hide unrelated governance redesign inside the verifier-triggered repair.

## Owner-directed reasoning-policy change queued after bounded repair

On 2026-08-26 the human owner explicitly approved adding a canonical SOUL development reasoning policy synthesized from prior KEEL/OS-Architect/KEEL-Research lessons, and integrating it through the single `COLD_START.md` authority rather than creating a second bootstrap order.

This is a **separate material governance change**, not part of F2-R1 repair. After WP-004 is materially complete, it must be represented by its own work package before the next fresh verification target is cut. The next verifier should therefore verify the exact target containing both the completed F2-R1 repair and the separately governed reasoning-policy change, avoiding two redundant verification cycles while preserving scope transparency.

## Authority boundaries remain unchanged

No current session has authority to:

- weaken WP-000 acceptance criteria to obtain a PASS,
- edit historical verification results,
- allow a builder to self-verify material repair or governance changes,
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
