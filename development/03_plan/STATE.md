# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-008 — Phase 0 F-AR-001 Repair  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** WP-006 fresh independent verification remains **PASS** only for exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`; WP-007 adversarial review completed with **Requires repair** and surviving material finding F-AR-001; reviewer evidence PR #12 is integrated evidence-only; bounded separate builder repair WP-008 is now active  
**Authoritative product branch:** `main`

## Current objective

Execute the bounded F-AR-001 repair under `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md` without reinterpreting the finding, weakening WP-000 acceptance criteria, or collapsing builder/verification/review/integration responsibilities.

The builder must derive the smallest repair that closes the observed generic cold-start completed-result discoverability failure while preserving canonical-state authority and separate Integrator-owned result transition.

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

Verifier evidence PR #10 was integrated evidence-only as merge commit `856c2cdf0a791501477d43dbe7419219f5dd62f0`.

The PASS remains permanently bound to `c690f858e7682f5bdf0511c0f10b0e932d868b0e`; it does not certify the later transition commits or any future F-AR-001 repair commit. The reviewer inspected the post-target chain through pre-review development head `572f25be68d438a800ebbce3a854b3bcd09bb0b1` and found it transition-only, so the PASS remained current for that exact material target at review time.

A material WP-008 repair will create a new target and will require fresh independent verification; the historical/current exact-target PASS must not be retargeted.

## Current adversarial-review result

WP-007 completed against the same exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e` and issued:

**Overall judgement:** **Requires repair**  
**Surviving finding:** **F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated independent result**  
**Severity:** **medium — material**  
**Finding result:** **stands**

Canonical review artefact:

`development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`

Reviewer handoff:

`development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`

Reviewer evidence PR #12 was inspected for evidence-only scope and merged by a separate Integrator into the development line as `9de8a011aa2d14fb985181ba3f180f729342901d`.

The evidence integration does not accept the target and does not repair F-AR-001. The result is preserved without reinterpretation.

## Active repair routing — WP-008

`development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md` is active.

Its bounded responsibility is to repair exactly the lifecycle failure identified by F-AR-001: during the legitimate post-independent-result/pre-Integrator interval, a generic cold-start must not begin duplicate verifier/reviewer execution before it deterministically discovers the completed repository-visible independent result.

The repair must preserve:

- `STATE.md` + active WP as canonical current-work authority;
- verifier/reviewer inability to canonically integrate their own results;
- separate Integrator-owned result transition;
- unchanged WP-000 acceptance criteria and historical evidence;
- fail-closed or explicitly bounded handling of ambiguous/conflicting/stale result evidence.

The Integrator that activated WP-008 did not choose or implement a repair mechanism.

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

WP-006 verified the reasoning-policy acceptance properties at exact target `c690f858...`. This does **not** accept ADR-0001 or Phase 0.

## Process defect PD-002

PD-002 remains preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`.

WP-007 did not establish PD-002 recurrence as a separate material finding. The surviving lifecycle-class issue is F-AR-001 and is routed through WP-008 rather than silently merged into PD-002.

## Required next responsibility

**Fresh separate designer/builder under `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md`.**

The builder must:

- enter through `COLD_START.md`;
- preserve F-AR-001 and the WP-007 **Requires repair** judgement as evidence, not reinterpret them;
- analyse the exact observed verifier duplicate-start trace in SESSION-0011 and the equivalent reviewer-close state represented by PR #12;
- derive and implement the smallest bounded repair under existing governance;
- follow `DECISION_POLICY.md` if the chosen mechanism materially changes architecture-level authority/state/evidence/verification semantics;
- add regression evidence for both verifier and reviewer lifecycle cases;
- avoid unrelated governance redesign, ADR acceptance, PR #1 merge, Phase acceptance, or Phase 1 work;
- leave the exact new material repair target and route fresh independent verification.

After material repair, a fresh independent verifier is required for the complete changed target, followed by appropriate fresh adversarial re-review before Phase 0 acceptance can proceed.

## Remaining Phase 0 gates

WP-006 PASS is historical/current only for exact target `c690f858...` and is no longer sufficient for a future repaired target. Remaining gates include:

- bounded repair of F-AR-001 under WP-008;
- fresh exact-target independent verification of the repaired Phase 0 target, including explicit F-AR-001 regression coverage;
- appropriate fresh separate adversarial re-review after the material repair;
- resolution/acceptance of any remaining material findings through authorised governance;
- ADR-0000 and ADR-0001 reaching the status required by their declared decision paths;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain unchanged

No current session may:

- edit historical verifier/reviewer evidence or reinterpret WP-006 PASS, F-AR-001, or the WP-007 **Requires repair** judgement;
- weaken WP-000 acceptance criteria;
- treat evidence integration or transition-only routing as acceptance/certification of a new material target;
- allow the repair builder to self-certify independent verification or adversarial re-review;
- accept ADR-0000 or ADR-0001 outside their required paths;
- merge PR #1 into `main` before all gates are satisfied;
- begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until the F-AR-001 repair has produced a new exact target, that target has current independent verification and required adversarial re-review, relevant decisions have the correct status, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
