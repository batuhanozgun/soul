# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-010 — Phase 0 F-AR-001 Repair Adversarial Re-review  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**Current material review target:** WP-008 repair PR #13 exact commit `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**State:** WP-009 fresh independent verification issued **PASS** for exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`; verifier evidence PR #14 is integrated evidence-only; fresh separate adversarial re-review is now required under WP-010  
**Authoritative product branch:** `main`

## Current objective

Freshly and separately adversarially re-review exact WP-008 material repair target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

under `development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md`.

The reviewer must actively attack the repaired F-AR-001 result-discovery/control path, including bypass/spoof, stale/conflict/ambiguity, discovery/inspection failure, authority leakage, false-completion and transition-only abuse paths, rather than repeat the WP-009 verifier checklist.

The reviewer must not repair the target, canonically integrate its own result, accept ADR-0000/0001/0002, merge PR #13/PR #1, accept Phase 0, or begin Phase 1.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, current material target, and current next responsibility. The active WP named here supplies detailed responsibility, authority, required readings, acceptance criteria, exact-target rules, and handoff.

`development/03_plan/NEXT_SESSION.md` and `development/03_plan/CHATGPT_PROJECT_ENTRY.md` are derived launch conveniences and intentionally store no copied mutable current WP/role/target values. `development/03_plan/WORKSPACE_INDEX.md` is navigational and subordinate to this state.

Fresh-session sequencing is governed only by `development/03_plan/COLD_START.md`; semantic authority/conflict resolution remains governed by `development/01_governance/SOURCE_OF_TRUTH.md`.

## Historical exact-target verification

WP-006 issued **PASS** against exact historical material target:

`c690f858e7682f5bdf0511c0f10b0e932d868b0e`

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`

Verifier handoff:

`development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`

Verifier evidence PR #10 was integrated evidence-only as merge commit `856c2cdf0a791501477d43dbe7419219f5dd62f0`.

That PASS remains permanently bound only to `c690f858...`. It does **not** certify the later WP-008 material repair target `a45b463...`.

## Adversarial-review result that triggered repair

WP-007 reviewed exact target `c690f858e7682f5bdf0511c0f10b0e932d868b0e` and issued:

**Overall judgement:** **Requires repair**  
**Surviving finding:** **F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated independent result**  
**Severity:** **medium — material**  
**Finding result:** **stands**

Canonical review artefact:

`development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`

Reviewer handoff:

`development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`

Reviewer evidence PR #12 was integrated evidence-only as merge commit `9de8a011aa2d14fb985181ba3f180f729342901d`.

This historical finding/judgement remains preserved exactly. WP-008 produced a repair candidate; WP-009 has now verified that exact candidate as PASS, but the required fresh adversarial re-review remains outstanding.

## WP-008 material repair candidate

WP-008 builder responsibility is complete as a **producer** responsibility only.

Draft repair PR:

**#13 — `WP-008: repair F-AR-001 pending independent-result discovery`**

Exact frozen material repair target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

Builder base:

`bf1f89cbc2e407034c3f9a7a7d4ec7001a6a43c5`

The material repair changes exactly six files relative to that base:

- `development/03_plan/COLD_START.md` — pending independent-result guard before duplicate independent role execution;
- `development/01_governance/WORKING_PROTOCOL.md` — independent result evidence-PR publication contract;
- `development/01_governance/VERIFICATION_POLICY.md` — verifier publication/transition binding;
- `development/03_plan/PR_GATE.md` — discoverability, exact-scope validation, and fail-closed ambiguity handling;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md` — proposed architecture decision;
- `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md` — producer regression evidence.

No WP-000 acceptance criterion or historical verifier/reviewer artefact was changed by the material repair.

PR #13 remains unmerged/unaccepted and its current head remains the exact reviewed target unless later freshness inspection proves otherwise.

## Current exact-target verification — WP-009

WP-009 is complete as a verification activity and issued:

**PASS** for exact material target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-a45b463b-2026-08-26.md`

Verifier handoff:

`development/07_sessions/SESSION-0015-PHASE0-F-AR-001-REPAIR-VERIFIER.md`

Dedicated verifier evidence PR #14 contained only those two authorised evidence/session files and was integrated evidence-only into `phase0/development-os` as merge commit:

`37f4bceb8f7ad4e0552f52af3ce878db03eb694f`

The PASS remains permanently bound only to exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`. It does not accept ADR-0000, ADR-0001 or ADR-0002; it does not accept Phase 0; it does not merge PR #13 or PR #1; and it does not substitute for the required fresh adversarial re-review.

## Proposed ADR-0002

`development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md` exists on the exact WP-008 repair target and remains **proposed**.

It records the repair architecture choice to preserve canonical state separation while adding a discoverable evidence-PR publication boundary, a pre-role pending-result guard, exact WP/role/target/scope validation, and fail-closed stale/conflict/ambiguity/uninspectable handling.

Neither WP-009 verification nor this Integrator transition accepts ADR-0002. Required adversarial/Phase/owner decision gates remain.

## Active adversarial re-review routing — WP-010

`development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md` is active.

The fresh separate reviewer must:

- enter through canonical `COLD_START.md`;
- bind review to exact repair target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` and independently confirm PR #13 freshness at start/close;
- persist an adversarial attack model before relying on WP-008 builder rationale or WP-009 verifier conclusions;
- attack the repaired post-result/pre-Integrator lifecycle for both verifier and reviewer cases;
- attempt bypass/spoof, stale/target-mismatch, conflict/ambiguity/incomplete-evidence and discovery/inspection-unavailable failures;
- test evidence/canonical-state separation, role authority containment, freshness and false-completion controls;
- inspect PR #14 evidence integration and WP-009 → WP-010 routing as post-target transition-only changes rather than silently assuming they are non-material;
- leave ADR-0002 proposed;
- publish a review artefact + reviewer handoff in a dedicated evidence PR targeting `phase0/development-os`;
- perform no repair or canonical result integration.

After reviewer publication/close, a separate Integrator must validate/integrate that review result and route it without reinterpretation.

## Material architecture status

### WP-004 — F2-R1 repair

- historical defect: stale `development/03_plan/BUILDER_STOP.md` next-responsibility pointer;
- repair: redundant routing artefact removed;
- WP-006 result: F2-R1 regression **PASS** at exact old target `c690f858...`.

### WP-005 — Development Reasoning Policy

Implemented proposed architecture includes:

- canonical `development/01_governance/REASONING_POLICY.md`;
- source synthesis evidence under `development/05_evidence/`;
- proposed ADR-0001;
- strengthened WP-000 criterion 12;
- derived minimal `CHATGPT_PROJECT_ENTRY.md`.

WP-009 re-checked all current WP-000 criteria at exact repair target `a45b463...` and issued PASS. ADR-0001 remains outside verifier/integrator acceptance authority.

## Process defect PD-002

PD-002 remains preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`.

WP-007 did not establish PD-002 recurrence as a separate material finding. WP-008 did not broaden its scope to repair PD-002. WP-009 PASS did not accept or close PD-002 through a new decision path.

## Required next responsibility

**Fresh separate adversarial reviewer under `development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md`.**

Exact target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

This Integrator session must stop after the canonical routing/handoff and must not continue into the adversarial re-review.

## Remaining Phase 0 gates

Remaining gates include:

- WP-010 fresh separate adversarial re-review of exact PR #13 target `a45b463...`;
- separate Integrator result transition after reviewer close;
- repair/resolution or authorised acceptance of any surviving material findings;
- ADR-0000, ADR-0001, and ADR-0002 reaching the status required by their declared decision paths;
- PR #13 material repair integration only after its required gates permit it;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain unchanged

No current adversarial-review session may:

- edit historical verifier/reviewer evidence or reinterpret WP-009 PASS, F-AR-001, or the historical WP-007 **Requires repair** judgement;
- weaken WP-000 acceptance criteria;
- repair the WP-008 target while reviewing it;
- canonically integrate its own result;
- accept ADR-0000, ADR-0001, or ADR-0002;
- merge PR #13 or PR #1;
- accept Phase 0 or begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until the WP-008 repair target has current independent verification and required adversarial re-review, all surviving material findings and decision gates are resolved through authorised paths, PR #13 material repair is properly integrated, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
