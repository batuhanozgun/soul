# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-007 — Phase 0 Adversarial Review  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-006 fresh independent verification completed with **PASS** for exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`; verifier evidence is integrated and the required separate adversarial review is now active  
**Authoritative product branch:** `main`

## Current objective

Execute a fresh, separate adversarial review of the Phase 0 material target under `development/04_work/WP-007-PHASE0-ADVERSARIAL-REVIEW.md` before any Phase/ADR acceptance or PR #1 merge.

The adversarial reviewer must actively seek material failure paths rather than repeat the WP-006 verifier checklist or producer rationale.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, and current next responsibility. The active WP named here supplies detailed responsibility, authority, required readings, acceptance criteria, and handoff.

`development/03_plan/NEXT_SESSION.md` and `development/03_plan/CHATGPT_PROJECT_ENTRY.md` are derived launch conveniences and intentionally store no copied current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed only by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Current exact-target verification

WP-006 completed and issued **PASS** against exact draft PR #1 material target:

`c690f858e7682f5bdf0511c0f10b0e932d868b0e`

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`

Verifier handoff:

`development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`

Verifier evidence PR #10 was inspected for authorised scope and merged evidence-only into the development line by a separate Integrator. The merge commit is `856c2cdf0a791501477d43dbe7419219f5dd62f0`.

The PASS remains permanently bound to `c690f858e7682f5bdf0511c0f10b0e932d868b0e`; it does not certify later commits. Under `VERIFICATION_POLICY.md`, evidence integration and mechanical routing/state/handoff commits do not make the result stale only while those changes remain explicitly transition-only. Any substantive repair, design, acceptance, authority, or verification-rule change after the target requires freshness re-evaluation and fresh independent verification where applicable.

## Material architecture status

### WP-004 — F2-R1 repair

- historical defect: stale `development/03_plan/BUILDER_STOP.md` next-responsibility pointer;
- repair: redundant routing artefact removed;
- WP-006 result: F2-R1 regression **PASS** at exact target `c690f858...`.

### WP-005 — Development Reasoning Policy

Implemented proposed architecture includes:

- canonical `development/01_governance/REASONING_POLICY.md`;
- source synthesis evidence under `development/05_evidence/`;
- proposed ADR-0001;
- policy loaded for every role through Step 2 of the single `COLD_START.md` sequence;
- strengthened WP-000 criterion 12;
- derived minimal `CHATGPT_PROJECT_ENTRY.md`.

WP-006 verified the current reasoning-policy acceptance properties at exact target `c690f858...`. This does **not** accept ADR-0001 or Phase 0.

## Process defect PD-002

PD-002 remains preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`.

WP-006 found the final current-work/activation discipline sufficient at the verified target and did not find evidence that one observed bootstrap incident alone justifies a new permanent mechanical gate. Recurrence remains subject to `CHANGE_POLICY.md` evidence and change analysis.

The defect record is not erased by that PASS.

## Required next responsibility

**Fresh adversarial reviewer under `development/04_work/WP-007-PHASE0-ADVERSARIAL-REVIEW.md`.**

The reviewer must:

- enter through `COLD_START.md`;
- operate separately from builder, verifier, and Integrator roles;
- bind the review to material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`;
- confirm that post-target changes are transition-only before relying on WP-006 freshness;
- establish attack hypotheses before relying on verifier conclusions;
- attack authority, state/bootstrap, verification/freshness, false-completion, change-safety, evidence/provenance, development/product separation, PD-002 recurrence, and the reasoning-policy risks specified by WP-005/ADR-0001;
- attempt to disprove candidate findings rather than preserve a quota;
- perform no repair, canonical transition, ADR acceptance, PR #1 merge, or Phase 1 work.

After reviewer close, a separate Integrator must integrate the review evidence and route surviving findings or remaining decision/owner gates.

## Remaining Phase 0 gates

WP-006 PASS is necessary but not sufficient for Phase 0 acceptance. Remaining gates include:

- WP-007 separate adversarial review;
- resolution or explicit acceptance of any material adversarial findings through existing governance;
- ADR-0000 and ADR-0001 reaching the status required by their declared owner/decision paths;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain unchanged

No current session has authority to:

- edit historical verifier evidence or reinterpret WP-006 PASS;
- weaken WP-000 acceptance criteria;
- treat transition-only integration as certification of a new material target;
- allow an adversarial reviewer to repair its own findings while reviewing;
- accept ADR-0000 or ADR-0001 outside their required paths;
- skip the required adversarial review;
- merge PR #1 into `main` before all gates are satisfied;
- begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until WP-000/Phase 0 has current exact-target verification, required adversarial review is resolved, relevant decisions have the correct status, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
