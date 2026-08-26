# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-009 — Phase 0 F-AR-001 Repair Verification  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**Current material verification target:** WP-008 repair PR #13 exact commit `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**State:** WP-008 builder repair for F-AR-001 is published as an unverified material candidate in draft PR #13; fresh separate exact-target verification is now required under WP-009  
**Authoritative product branch:** `main`

## Current objective

Independently verify the exact WP-008 material repair target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

under `development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md`.

The verifier must re-check all current WP-000 acceptance criteria and explicitly regression-test F-AR-001 across both the observed verifier-result lifecycle and the equivalent reviewer-close lifecycle, including fail-closed stale/conflict/discovery-failure behaviour.

The verifier must not repair the target, integrate its own result, accept ADR-0002, merge PR #13/PR #1, accept Phase 0, or begin Phase 1.

## Canonical current-work rule

This file is the authoritative home for current phase, active WP, current material verification target, and current next responsibility. The active WP named here supplies detailed responsibility, authority, required readings, acceptance criteria, exact-target rules, and handoff.

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

The finding/judgement remains preserved exactly. WP-008 produced a repair candidate; independent verification has not yet established that F-AR-001 is closed.

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

The repair design preserves `STATE.md` + active WP as canonical state and keeps verifier/reviewer canonical result transition with a separate Integrator. Those statements are builder claims pending WP-009 verification.

No WP-000 acceptance criterion or historical verifier/reviewer artefact was changed by the material repair.

PR #13 is not merged/accepted by the builder close.

## Proposed ADR-0002

`development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md` exists on the exact repair target and remains **proposed**.

It records the architecture choice to preserve canonical state separation while adding:

- a discoverable evidence-PR publication boundary for completed verifier/reviewer results;
- a pre-role pending-result guard inside the single `COLD_START.md` sequence;
- exact WP/role/target/scope validation;
- fail-closed handling of same-WP stale/conflicting/ambiguous/uninspectable evidence.

WP-009 verification does not accept ADR-0002. Required independent/adversarial/Phase decision gates remain.

## Active verification routing — WP-009

`development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md` is active.

The fresh verifier must:

- enter through canonical `COLD_START.md`;
- bind verification to exact repair target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` and independently confirm PR #13 freshness at start/close;
- derive expectations before reading WP-008 builder rationale, ADR-0002 rationale, or builder regression conclusions;
- re-check all twelve current WP-000 acceptance criteria;
- replay the SESSION-0011 / PR #10 verifier duplicate-start case against the repaired control flow;
- replay the WP-007 / PR #12 reviewer-close case;
- test unrelated historical evidence noise and same-WP stale/target-mismatch/conflict/ambiguity/discovery-unavailable paths;
- verify that evidence PRs remain lower-authority triggers and that only a separate Integrator can canonically transition results;
- leave ADR-0002 proposed;
- publish a verifier artefact + handoff in a dedicated evidence PR targeting `phase0/development-os`;
- perform no repair or canonical result integration.

After verifier publication/close, a separate Integrator must validate/integrate the result and route it without reinterpretation.

A PASS still requires a fresh separate adversarial re-review of the repaired exact target before Phase 0 acceptance can proceed.

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

WP-006 verified those properties only at exact old target `c690f858...`. WP-009 must re-check current WP-000 criteria at the new repair target. ADR-0001 remains outside verifier acceptance authority.

## Process defect PD-002

PD-002 remains preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`.

WP-007 did not establish PD-002 recurrence as a separate material finding. WP-008 did not broaden its scope to repair PD-002.

## Required next responsibility

**Fresh separate verifier under `development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md`.**

Exact target:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

The current builder session is complete and must not continue into verifier work.

## Remaining Phase 0 gates

Remaining gates include:

- WP-009 fresh exact-target independent verification of PR #13 target `a45b463...`, including explicit F-AR-001 regressions;
- separate Integrator result transition after verifier close;
- appropriate fresh separate adversarial re-review after a verifier PASS;
- repair/resolution or authorised acceptance of any surviving material findings;
- ADR-0000, ADR-0001, and ADR-0002 reaching the status required by their declared decision paths;
- PR #13 material repair integration only after its required gates permit it;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain unchanged

No current verifier session may:

- edit historical verifier/reviewer evidence or reinterpret WP-006 PASS, F-AR-001, or the WP-007 **Requires repair** judgement;
- weaken WP-000 acceptance criteria;
- retarget historical PASS to `a45b463...`;
- repair the WP-008 target while verifying it;
- canonically integrate its own result;
- accept ADR-0000, ADR-0001, or ADR-0002;
- perform the fresh adversarial re-review in the same session;
- merge PR #13 or PR #1;
- accept Phase 0 or begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until the WP-008 repair target has current independent verification and required adversarial re-review, all surviving material findings and decision gates are resolved through authorised paths, PR #13 material repair is properly integrated, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
