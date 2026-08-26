# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-006 — Phase 0 Fresh Verification after F2-R1 + Reasoning Policy  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-004 bounded F2-R1 repair and WP-005 reasoning-policy material architecture work are complete; fresh independent verification of the complete changed target is now required  
**Authoritative product branch:** `main`

## Current objective

Freshly verify the exact current Phase 0 PR target against all **twelve** current WP-000 acceptance criteria, including F2-R1 regression, the single-COLD_START reasoning-policy integration, source-synthesis evidence integrity and PD-002 current-work discipline.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, and current next responsibility. The active WP named here supplies detailed responsibility, authority, required readings, acceptance criteria, and handoff.

`development/03_plan/NEXT_SESSION.md` and `development/03_plan/CHATGPT_PROJECT_ENTRY.md` are derived launch conveniences and intentionally store no copied current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed only by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Material changes awaiting verification

### WP-004 — F2-R1 repair

- historical verifier finding: stale `BUILDER_STOP.md` next-responsibility pointer;
- builder repair: `development/03_plan/BUILDER_STOP.md` removed rather than preserved as a second routing surface;
- status: materially complete, **not independently verified**.

### WP-005 — Development Reasoning Policy

Owner-approved direction implemented as proposed architecture:

- canonical `development/01_governance/REASONING_POLICY.md`;
- source synthesis evidence under `development/05_evidence/`;
- proposed ADR-0001;
- policy loaded for every role through Step 2 of the single `COLD_START.md` sequence;
- `WORKING_PROTOCOL.md` integration;
- strengthened WP-000 criterion 12;
- derived minimal `CHATGPT_PROJECT_ENTRY.md` that points to repository cold-start instead of copying governance.

Status: materially complete, **not independently verified or accepted**.

## Process defect PD-002

The bootstrap builder began early WP-005 material writes before first moving this active-WP pointer from completed WP-004 to WP-005. The defect is preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`; canonical state was corrected before further material work.

Fresh verification must inspect the final activation/current-work discipline. One observed incident does not by itself justify inventing a new mechanical gate; any stronger mechanism must follow `CHANGE_POLICY.md` evidence and change analysis.

## Historical verification is stale

Latest historical independent result before these changes:

- WP-003 target: `a02e36e5e71522995b74fb018a6b28235f1d7848`;
- result: **FAIL** due F2-R1;
- F1 and PD-001 passed at that exact target;
- WP-000 criteria 1 and 3–11 passed at that exact target only.

Canonical historical artefact: `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md`.

No historical PASS fragment certifies the current changed target.

## Required next responsibility

**Fresh verifier under `development/04_work/WP-006-PHASE0-REASONING-REVERIFICATION.md`.**

The verifier must:

- enter through `COLD_START.md`;
- capture the exact current PR #1 head from PR metadata;
- derive expected results from strengthened WP-000/current governance before reading builder rationale;
- verify all twelve criteria;
- regression-test F2-R1;
- verify reasoning-policy scope, proportionality, no-private-chain-of-thought boundary and no duplicate bootstrap authority;
- inspect PD-002;
- perform no repair or canonical result integration.

After verifier close, a separate Integrator executes the result-dependent transition under `VERIFICATION_POLICY.md`.

## Authority boundaries remain unchanged

No current session has authority to:

- edit historical verification results,
- weaken acceptance criteria to obtain a PASS,
- allow a builder to independently verify its own material output,
- accept ADR-0000 or ADR-0001 outside their required paths,
- skip required adversarial review,
- merge PR #1 into `main` before gates are satisfied,
- begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until WP-000 is verified-complete on the current exact target, required adversarial review is resolved, relevant decisions have the correct status, and the Phase 0 PR is accepted into `main`.
