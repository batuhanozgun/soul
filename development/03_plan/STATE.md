# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-021 — Development OS Lifecycle and Work-Selection Improvement  
**Current branch:** `phase0/development-os`  
**Current work mode:** design-only; candidate governance implementation is gated behind fresh pre-build adversarial review and historical replay/evaluation  
**Fallback checkpoint:** `checkpoint/phase0-pre-lifecycle-v2-c4ebef9` at `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`  
**Blocked unresolved work:** WP-020 — F-AR-008 remains medium/material, stands, unresolved; no repair target exists  
**Current material PR:** #22 — draft, unaccepted and unmerged; remains the rejected WP-017 target and is not the WP-021 target  
**Current exact material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab` — historical/current rejected result-control target only; WP-021 has not yet frozen a lifecycle design target  
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033` — for PR #22 historical target  
**Superseded rejected material PR:** #19 — closed unmerged at `2f5508c1d6941e951d494bb2a700ef861860431d`
**Current verification result:** WP-012 **PASS** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and activation `7c625107c09788d6066249c67d66cbf7c0c4b576`
**Verifier evidence integration:** PR #17 head `1caf39a3fcf62c18a8d017f71f26f9c834951e70`, merged evidence-only as `2d7329508fbecf7a05cf7f26cd16e2330985a076`
**Current adversarial re-review result:** WP-013 **Requires repair** for exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0` and activation `18b239e05452d1e78afffd6deaaeb2463d077720`; F-AR-005 medium/material, stands
**Reviewer evidence integration:** PR #18 head `2e78421f1c618995fe0cc0c8eb62104ecae63be1`, merged evidence-only as `fda9689107cf96ad2cc01e1b1bbe74b86055e771`
**Completed WP-013 result-control key:** `WP-013 / adversarial reviewer / adf067e4289e4c0b51cf40c1940193e8252b22e0 / attempt 1`
**Completed WP-015 result-control key:** `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Current changed-target verification result:** WP-015 **PASS** for exact target `2f5508c1d6941e951d494bb2a700ef861860431d`, activation `5368abd0f0c9a846f89120be44c19b1f1b1825d9` and binding `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`
**Current verifier evidence integration:** PR #20 head `a1a0c07c2f16faa4c963bec6da7dad85baeb5565`, merged evidence-only as `df9c9c12129bb8c55e4948fa095a90ab25b90811`
**Completed WP-016 result-control key:** `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Completed WP-016 activation/binding:** `94bcc9bf9d0352bde67459635a6073c7e65171e2` / `91db45818f324a1c1aef4dd16d48e40591a3f4e1`
**Current changed-target adversarial re-review result:** WP-016 **Requires repair** for exact target `2f5508c1d6941e951d494bb2a700ef861860431d`; F-AR-006 medium/material and F-AR-007 low/evidence-model correctness stand
**Current reviewer evidence integration:** PR #21 head `c2c44604ea1694bd84e34bed950e38efe557ff71`, merged evidence-only as `276132a8ad3bcaa5263aba725f6f006019f79287`
**Completed WP-018 result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Current candidate-set verification result:** WP-018 **PASS** for exact target `5bd0db27fc3df368c9e112f01b7eed49a64402ab`, activation `fbe517bef10b5e820dc096a8a82e2c1a3047a38c` and binding `e62075228054f43f4dc8d318210ce9de0bf8b8ae`
**Current verifier evidence integration:** PR #24 head `1b1d5effa21e156d09b56db741fec0ae0966f2a7`, merged evidence-only as `b2e54a1f7398328a17ba6aaf3a6a91ddbe3c4595`
**Completed WP-019 result-control key:** `WP-019 / adversarial reviewer / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Completed WP-019 activation/binding:** `3b91acf02df2852c43404ec164725ac5748b9bad` / `fa6f208e6133f746a69a4a51faff3f2485798d24`
**Current candidate-set adversarial re-review result:** WP-019 **Requires repair** for exact target `5bd0db27fc3df368c9e112f01b7eed49a64402ab`; F-AR-008 medium/material, stands
**Current reviewer evidence integration:** PR #25 initial result commit `6b328cdeb127f56b163b999eaa8621fd6d5ead19`, final head `16b5aacb12d05157e183cb9257025f30636e0f71`, merged evidence-only as `8022ca6fb30fc32e6a95f22c5c1d58c5ab8c1745`
**State:** WP-019 result is fully integrated; WP-020 repair execution is blocked without resolving or weakening F-AR-008; WP-021 is active to design and evaluate a stronger Development OS work-selection/lifecycle before any further result-control build; no new lifecycle architecture, F-AR-008 repair, new exact repair target, ADR acceptance, material merge, Phase acceptance or Phase 1 claim has occurred
**Authoritative product branch:** `main`

## Current objective

Execute the **design-only stage** of:

`development/04_work/WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md`.

The current responsibility is to produce and freeze a proposed Development OS lifecycle/work-selection architecture, proposed ADR-0003, motivation/function map and historical replay protocol on a separate WP-021 candidate branch. The exact proposed design must then receive a fresh pre-build adversarial review and replay/evaluation evidence before any operational governance policy is modified to enact it.

WP-020 remains blocked, not completed or cancelled. F-AR-008 remains standing and unresolved exactly as issued by WP-019. PR #22 remains draft/unaccepted/unmerged at exact rejected target `5bd0db27fc3df368c9e112f01b7eed49a64402ab`; WP-018 PASS and WP-019 **Requires repair** remain permanently bound only to that target and their exact activation/result keys.

The owner-directed improvement may rewrite current Development OS mechanisms if justified, but it must preserve repository continuity, exact-target evidence history, independent assurance, canonical state authority, recoverability and the Human Owner boundary. The pre-change working checkpoint remains available at `checkpoint/phase0-pre-lifecycle-v2-c4ebef9`.

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

## Completed exact-target verification — WP-015

`development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md` is complete as a verification activity and issued:

**PASS** for exact material target `2f5508c1d6941e951d494bb2a700ef861860431d`, material base `dca520242585a80c2efaf22e18fe3d353147b93e`, provisional activation `5368abd0f0c9a846f89120be44c19b1f1b1825d9` and binding `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`.

Result-control key: `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`.

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-2f5508c1-2026-08-27.md`

Verifier handoff:

`development/07_sessions/SESSION-0026-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFIER.md`

Dedicated evidence PR #20 contained exactly those two files at immutable head `a1a0c07c2f16faa4c963bec6da7dad85baeb5565` and was merged evidence-only by a separate Integrator as `df9c9c12129bb8c55e4948fa095a90ab25b90811`. PASS remains exact-target evidence, not target/ADR/Phase acceptance.

## Completed exact-target adversarial re-review — WP-016

`development/04_work/WP-016-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEW.md` is complete as an adversarial-review activity.

Result-control key: `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`.

The reviewer issued **Requires repair** and preserved:

- **F-AR-006 — Rotating to fresh PR identities resets per-candidate containment and restores unbounded denial** — medium/material, stands;
- **F-AR-007 — The executable routing model lets an invalid candidate outrank a current-valid result** — low/evidence-model correctness, stands.

Dedicated evidence PR #21 contained exactly the canonical adversarial re-review artefact and SESSION-0028 at immutable head `c2c44604ea1694bd84e34bed950e38efe557ff71` and was merged evidence-only by a separate Integrator as `276132a8ad3bcaa5263aba725f6f006019f79287`.

The result remains bound only to exact target `2f5508c...`, base `dca520...`, the complete WP-016 key and activation/binding `94bcc9b...` / `91db458...`. Evidence integration is not repair or acceptance and does not reinterpret WP-015 PASS.

## Builder-complete candidate-set repair — WP-017

`development/04_work/WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md` is complete as a producer responsibility only.

Draft PR #22 freezes exact target `5bd0db27fc3df368c9e112f01b7eed49a64402ab` from canonical base `4524f21cced54c71fb2219b7f42119adbbb5b033` with exactly ten material files. Producer regression reports 67/67 passing cases and the deliberate invalid-first mutation fails red; that is producer evidence, not independent proof. ADR-0002 remains proposed and PR #22 remains unaccepted/unmerged.

PR #19 was not amended or merged. It is closed unmerged as superseded at immutable head `2f5508c...`; WP-015 PASS, WP-016 **Requires repair** and F-AR-006/F-AR-007 remain permanently bound only to that historical target.

## Completed exact-target verification — WP-018

`development/04_work/WP-018-PHASE0-CANDIDATE-SET-CONVERGENCE-VERIFICATION.md` is complete as a verification activity and issued:

**PASS** for exact material target `5bd0db27fc3df368c9e112f01b7eed49a64402ab`, material base `4524f21cced54c71fb2219b7f42119adbbb5b033`, provisional activation `fbe517bef10b5e820dc096a8a82e2c1a3047a38c` and binding `e62075228054f43f4dc8d318210ce9de0bf8b8ae`.

Result-control key: `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`.

Canonical verifier artefact:

`development/06_reviews/VERIFICATION-WP-000-5bd0db27-2026-08-28.md`

Verifier handoff:

`development/07_sessions/SESSION-0032-PHASE0-CANDIDATE-SET-CONVERGENCE-VERIFIER.md`

Dedicated evidence PR #24 contained exactly those two files at immutable head `1b1d5effa21e156d09b56db741fec0ae0966f2a7` and was merged evidence-only by a separate Integrator as `b2e54a1f7398328a17ba6aaf3a6a91ddbe3c4595`. PASS remains exact-target evidence, not target/ADR/Phase acceptance.

## Completed exact-target adversarial re-review — WP-019

`development/04_work/WP-019-PHASE0-CANDIDATE-SET-CONVERGENCE-ADVERSARIAL-REREVIEW.md` is complete as an adversarial-review activity.

Result-control key: `WP-019 / adversarial reviewer / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`.

The reviewer issued **Requires repair** and preserved:

- **F-AR-008 — A visible result suppresses an uncontained inspection blocker that may conceal a second current result** — medium/material, stands.

Canonical review artefact:

`development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-5bd0db27-2026-08-28.md`

Reviewer handoff:

`development/07_sessions/SESSION-0034-PHASE0-CANDIDATE-SET-CONVERGENCE-ADVERSARIAL-REREVIEWER.md`

Dedicated evidence PR #25 contained exactly those two files at initial
immutable result commit `6b328cdeb127f56b163b999eaa8621fd6d5ead19`
and final locator head `16b5aacb12d05157e183cb9257025f30636e0f71`.
It was merged evidence-only by a separate Integrator as
`8022ca6fb30fc32e6a95f22c5c1d58c5ab8c1745`.

The result remains bound only to target `5bd0db27...`, base `4524f21...`, the
complete WP-019 key and activation/binding `3b91acf...` / `fa6f208...`.
Evidence integration is not repair or acceptance and does not reinterpret
WP-018 PASS.

## Blocked bounded repair — WP-020

`development/04_work/WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`
is blocked from execution while WP-021 evaluates and strengthens the Development OS work-selection/lifecycle.

F-AR-008 remains unresolved and standing. No new exact repair target exists. The prior routing package is preserved so that, if a later accepted work-selection decision concludes the bounded repair is still the right next work, its finding-specific obligations remain available. WP-021 may instead establish that a broader successor work is justified; such a successor must carry F-AR-008 unchanged rather than erase it.

## Active Development OS improvement — WP-021

`development/04_work/WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md`
is active in a design-only stage.

The current task is to freeze a proposed lifecycle/work-selection architecture and ADR on a separate candidate branch, then subject that exact design to fresh pre-build adversarial review and historical replay/evaluation before operational governance implementation begins.

The improvement investigates whether recent repair progression reflects, in part, a structural bias caused by automatic repair-shaped result routing and the combined Designer/Builder motivation. The hypothesis is supported by evidence but is not treated as proven or as the sole cause. Added process complexity has a burden of proof.

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

WP-021 activation is intentionally recorded in canonical state **before** candidate lifecycle design work begins, so the Development OS improvement does not repeat PD-002's state-before-work ordering defect.

## Required next responsibility

Continue the **design-only** WP-021 responsibility on a separate candidate branch created from this canonical activation state.

Produce one frozen proposed Development OS lifecycle specification, proposed ADR-0003, function/motivation justification and replay protocol. Do not modify current operational governance policies to enact the proposed lifecycle yet. When the exact design target is frozen, stop implementation and route it to a fresh pre-build adversarial reviewer plus the historical replay/evaluation path required by WP-021.

No current session may combine design production with its independent pre-build adversarial review, later implementation, independent verification, post-build adversarial review, Integrator, ADR acceptance, material merge, Phase acceptance or Phase 1 responsibility.

## Remaining Phase 0 gates

Remaining gates now include:

- WP-021 design stage, fresh pre-build adversarial challenge and replay/evaluation before governance implementation;
- any resulting WP-021 lifecycle implementation, fresh exact-target verification, separate evidence integration and fresh post-build adversarial review;
- a separately controlled context/state-surface improvement if the accepted WP-021 design requires it;
- re-evaluation and completion/supersession of standing WP-020/F-AR-008 work under the accepted lifecycle;
- prospective evaluation of at least one material trajectory under the strengthened Development OS before final Phase-0 acceptance if the final WP-000 criteria require it;
- repair/resolution or authorised acceptance of any later surviving material findings;
- ADR-0000, ADR-0001, ADR-0002 and any later required architecture decisions reaching the status required by their declared decision paths;
- PR #22 may be integrated only if a later accepted path and all gates permit it; PR #19, PR #16 and PR #13 remain closed unmerged and superseded;
- human-owner/PR acceptance gates where required;
- PR #1 merge into `main` only after `PR_GATE.md` and `PHASE_GATE.md` are satisfied.

## Authority boundaries remain explicit

During the active WP-021 design-only stage no session may:

- execute or silently redesign WP-020/F-AR-008 repair work;
- edit historical verifier/reviewer evidence or reinterpret WP-018 PASS, WP-019 **Requires repair**, or F-AR-001 through F-AR-008;
- modify current operational governance policies to enact an unchallenged/unreplayed candidate lifecycle;
- treat predecessor research or external prior art as architecture truth without the decision process;
- self-review the produced lifecycle as the required fresh adversarial reviewer;
- self-verify a later implemented governance target;
- accept ADR-0000, ADR-0001, ADR-0002 or proposed ADR-0003;
- merge PR #22, PR #19, PR #16 or PR #1;
- accept Phase 0 or begin Phase 1.

## Phase 1 gate

Phase 1 does not begin until the Development OS lifecycle/work-selection improvement and any required context-surface migration have passed their own independent gates, standing F-AR-008/result-control work has been completed or explicitly resolved under the accepted lifecycle, all surviving material findings and decision gates are resolved through authorised paths, the final Phase-0 Development OS target has current independent verification and required adversarial review, human/PR acceptance gates are satisfied, and the Phase 0 PR is accepted into `main`.
