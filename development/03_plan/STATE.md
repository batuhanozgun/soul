# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-015 — Phase 0 Moving-Candidate Convergence Verification
**Current branch:** `phase0/development-os`  
**Current material PR:** #19 — draft, unaccepted and unmerged
**Current exact material target:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Superseded rejected material PR:** #16 — closed unmerged at `adf067e4289e4c0b51cf40c1940193e8252b22e0`
**Current verification result:** WP-012 **PASS** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and activation `7c625107c09788d6066249c67d66cbf7c0c4b576`
**Verifier evidence integration:** PR #17 head `1caf39a3fcf62c18a8d017f71f26f9c834951e70`, merged evidence-only as `2d7329508fbecf7a05cf7f26cd16e2330985a076`
**Current adversarial re-review result:** WP-013 **Requires repair** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and activation `18b239e05452d1e78afffd6deaaeb2463d077720`; F-AR-005 medium/material, stands
**Reviewer evidence integration:** PR #18 head `2e78421f1c618995fe0cc0c8eb62104ecae63be1`, merged evidence-only as `fda9689107cf96ad2cc01e1b1bbe74b86055e771`
**Completed WP-013 result-control key:** `WP-013 / adversarial reviewer / adf067e4289e4c0b51cf40c1940193e8252b22e0 / attempt 1`
**Current result-control key:** `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Current provisional activation commit:** `5368abd0f0c9a846f89120be44c19b1f1b1825d9`
**State:** WP-014 producer repair is published on exact PR #19 target `2f5508c...`; fresh separate verification is active under WP-015; no WP-015 result, fresh adversarial re-review, ADR acceptance, material merge, Phase acceptance, or Phase 1 claim has occurred
**Authoritative product branch:** `main`

## Current objective

Freshly and independently verify the complete moving-candidate convergence repair under:

`development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md`.

The verifier must derive expectations before reading builder rationale, independently assess all current WP-000 criteria and F-AR-001 through F-AR-005, inspect the exact PR #19 nine-file target and test the exact WP-015 provisional activation bridge protecting this verification's own result interval.

The exact target is `2f5508c1d6941e951d494bb2a700ef861860431d` from base `dca520242585a80c2efaf22e18fe3d353147b93e`. WP-012 PASS and WP-013 **Requires repair** remain bound only to the superseded PR #16 target `adf067e...` and cannot certify this changed target. The verifier must not repair, resolve or contain candidates, advance attempts, integrate its own result, perform adversarial re-review, accept an ADR, merge PR #19/PR #1, accept Phase 0, or begin Phase 1.

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

Neither WP-009 verification, WP-010 adversarial review, nor this Integrator transition accepts ADR-0002. Repair/verification/re-review/Phase/owner decision gates remain.

## Completed adversarial re-review — WP-010

`development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md` is complete as a review activity.

The exact-target reviewer issued **Requires repair** and preserved three findings:

- F-AR-002 — no safe activation path for the repair's own verifier/reviewer result intervals — medium/material, stands;
- F-AR-003 — same-WP stale/ambiguous evidence can create persistent cold-start livelock — medium/material, stands;
- F-AR-004 — one-shot pending-result discovery has a check-then-act race — low/timing-dependent, stands.

Reviewer evidence PR #15 contained exactly the review artefact and SESSION-0017 handoff and was integrated evidence-only as merge commit `c8fc17bc50ca04893cc6a87e492408c078c79311`. The result remains bound only to `a45b463...`; evidence integration is not repair or acceptance.

## Builder-complete pending-result repair — WP-011

`development/04_work/WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md` is builder-complete as a producer responsibility only.

Draft PR #16 freezes exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` on branch `codex/wp011-pending-result-control-repair`, based on `8dcdc750600b336a2e97fde3433926b6a2217f26`, with exactly eight material files. Producer regression evidence reports 13 passing cases; it is not independent proof. PR #13 is closed unmerged as superseded, while all historical exact-target result bindings remain preserved.

The repair architecture adds a complete result-control key, initial and immediate pre-role live checks, exact-head canonical Integrator resolutions with moved-head reopening, current-valid-result suppression prevention, conflict-preserving attempt advancement, fail-closed recovery and a provisional WP-local activation bridge. It explicitly bounds the remaining publication-after-final-check edge instead of claiming an atomic lock. ADR-0002 remains proposed and PR #16 remains unaccepted/unmerged.

## Completed exact-target verification — WP-012

`development/04_work/WP-012-PHASE0-PENDING-RESULT-CONTROL-VERIFICATION.md` is complete as a verification activity and issued:

**PASS** for exact material target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and exact provisional activation `7c625107c09788d6066249c67d66cbf7c0c4b576`.

Result-control key: `WP-012 / verifier / adf067e4289e4c0b51cf40c1940193e8252b22e0 / attempt 1`.

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-adf067e4-2026-08-26.md`

Verifier handoff:

`development/07_sessions/SESSION-0020-PHASE0-PENDING-RESULT-CONTROL-VERIFIER.md`

Dedicated evidence PR #17 contained exactly those two files at immutable head `1caf39a3fcf62c18a8d017f71f26f9c834951e70` and was merged evidence-only by a separate Integrator as `2d7329508fbecf7a05cf7f26cd16e2330985a076`. PASS remains exact-target evidence, not target/ADR/Phase acceptance.

## Completed exact-target adversarial re-review — WP-013

`development/04_work/WP-013-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEW.md` is complete as an adversarial-review activity.

Result-control key: `WP-013 / adversarial reviewer / adf067e4289e4c0b51cf40c1940193e8252b22e0 / attempt 1`.

The reviewer issued **Requires repair** and preserved:

- **F-AR-005 — A mutable lower-authority candidate can repeatedly invalidate exact-head resolutions and deny progress indefinitely** — medium/material, stands.

Canonical review artefact:

`development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-adf067e4-2026-08-26.md`

Reviewer handoff:

`development/07_sessions/SESSION-0022-PHASE0-PENDING-RESULT-CONTROL-ADVERSARIAL-REREVIEWER.md`

Dedicated evidence PR #18 contained exactly those two files at immutable head `2e78421f1c618995fe0cc0c8eb62104ecae63be1` and was merged evidence-only by a separate Integrator as `fda9689107cf96ad2cc01e1b1bbe74b86055e771`.

The result remains bound only to target `adf067e...`, the exact four-field key and activation `18b239e...`. Evidence integration is not repair or acceptance and does not reinterpret WP-012 PASS.

## Builder-complete bounded repair — WP-014

`development/04_work/WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md` is complete as a producer responsibility only.

Draft PR #19 freezes exact target `2f5508c1d6941e951d494bb2a700ef861860431d` from canonical base `dca520242585a80c2efaf22e18fe3d353147b93e` with exactly nine material files. Producer regression reports 28/28 passing cases; that is producer evidence, not independent proof. ADR-0002 remains proposed and PR #19 remains unaccepted/unmerged.

PR #16 was not amended or merged. It is closed unmerged as superseded at immutable head `adf067e...`; WP-012 PASS, WP-013 **Requires repair** and F-AR-005 remain permanently bound only to that historical target.

## Active exact-target verification — WP-015

`development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md` is active for a fresh separate verifier.

Result-control key: `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`.

The WP-local activation bridge is a provisional material rollout control, not a transition-only relabel and not acceptance of PR #19 governance. Its exact activation commit is `5368abd0f0c9a846f89120be44c19b1f1b1825d9`. The verifier must execute both bridge checks and publish only the exact verification artefact plus verifier handoff for a separate Integrator.

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

**Fresh separate verifier under `development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md`.**

Verify exact PR #19 target `2f5508c...`, using WP-015 result-control attempt 1 and the exact provisional activation binding. Publish only the dedicated verifier artefact and handoff PR, then stop for a separate Integrator.

No current session may combine verifier, Integrator, repair, adversarial re-review, ADR acceptance, material merge, Phase acceptance, or Phase 1 responsibility.

## Remaining Phase 0 gates

Remaining gates include:

- WP-015 fresh exact-target verification of `2f5508c...`, followed by separate result integration;
- fresh separate adversarial re-review of the exact verified target, followed by separate result integration;
- repair/resolution or authorised acceptance of any later surviving material findings;
- ADR-0000, ADR-0001, and ADR-0002 reaching the status required by their declared decision paths;
- PR #19 may be integrated only after its required gates permit it; PR #16 and PR #13 remain closed unmerged and superseded;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain unchanged

No current WP-015 verifier session may:

- edit historical verifier/reviewer evidence or reinterpret WP-012 PASS, WP-013 **Requires repair**, or F-AR-001 through F-AR-005;
- weaken WP-000 acceptance criteria;
- repair the candidate, resolve or contain evidence candidates, advance the attempt, canonically integrate its own result, or perform adversarial re-review;
- accept ADR-0000, ADR-0001, or ADR-0002;
- merge PR #19, PR #16 or PR #1;
- accept Phase 0 or begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until a changed repair target resolving F-AR-005 has current independent verification and required adversarial re-review, all surviving material findings and decision gates are resolved through authorised paths, the authorised material repair is properly integrated, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
