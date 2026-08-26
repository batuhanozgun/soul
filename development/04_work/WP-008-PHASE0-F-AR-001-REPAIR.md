# WP-008 — Phase 0 F-AR-001 Repair

**Status:** builder repair published — fresh independent verification required  
**Owner role:** designer/builder  
**Decision authority:** bounded repair of F-AR-001 within existing foundation/governance and unchanged WP-000 acceptance criteria; substantive architecture choices must follow `DECISION_POLICY.md`; no independent verification, adversarial-review self-approval, ADR acceptance, PR #13 merge, PR #1 merge, Phase acceptance, or Phase 1 authority  
**Builder branch:** `repair/wp008-f-ar-001-cold-start-result-discovery`  
**Repair PR:** #13 — draft  
**Exact material repair target:** `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Trigger:** WP-007 adversarial review judgement **Requires repair**, surviving finding F-AR-001  
**Review evidence:** `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`  
**Reviewer handoff:** `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`  
**Evidence PR:** #12, integrated evidence-only as merge commit `9de8a011aa2d14fb985181ba3f180f729342901d`

## Objective

Repair exactly F-AR-001 so a generic fresh-session cold-start can reliably detect a completed but not-yet-canonically-integrated independent verifier/reviewer result before it commits to duplicating the just-completed independent role, while preserving the existing separation between evidence production and Integrator-owned canonical state transition.

This WP routed the finding without prescribing the mechanism. The builder derived the bounded mechanism recorded below; its sufficiency is a producer claim until WP-009 independent verification completes.

## Exact finding

**F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated independent result.**

The WP-007 reviewer found that the architecture intentionally leaves canonical `STATE.md` unchanged during the post-result/pre-Integrator interval, while `COLD_START.md` does not deterministically surface a completed independent verifier/reviewer result before role selection. SESSION-0011 contains an observed duplicate-verifier execution trace, and reviewer close reproduced the same lifecycle state with completed reviewer evidence PR #12 while canonical state still assigned WP-007 reviewer work.

**Reviewer result:** stands.  
**Severity:** medium — material.  
**Overall WP-007 judgement:** **Requires repair.**

The canonical claim/evidence/failure-path/impact/disproof record remains the WP-007 adversarial-review artefact and was not rewritten by this repair WP.

## Scope

- analyse the exact F-AR-001 lifecycle failure path and its immediate/system cause under existing governance;
- implement the smallest repair that prevents or deterministically detects duplicate role selection during the supported post-independent-result/pre-Integrator interval;
- preserve `STATE.md` + active WP as canonical current-work authority rather than creating a competing state home;
- preserve verifier/reviewer inability to perform their own canonical result transition;
- define deterministic ambiguity/failure behaviour when completed independent-result evidence is absent, conflicting, stale, or cannot be unambiguously bound to the active target;
- add or update regression evidence/tests/observable checks sufficient to exercise both the SESSION-0011 verifier case and the equivalent reviewer-close case identified by WP-007;
- update only directly affected governance/planning surfaces and required subordinate views/handoffs;
- leave a builder handoff with the exact changed target and fresh verification/re-review requirements.

## Non-scope

- reinterpreting, weakening, renaming, or deleting F-AR-001;
- changing the WP-007 **Requires repair** judgement;
- weakening WP-000 acceptance criteria;
- treating reviewer evidence integration as target acceptance;
- redesigning unrelated bootstrap, role, verification, reasoning, ADR, or Phase-gate architecture;
- repairing PD-002 or other historical findings unless a direct contradiction is mechanically inseparable from the F-AR-001 repair and is explicitly recorded;
- accepting/rejecting ADR-0000, ADR-0001, or ADR-0002;
- independent verification or adversarial re-review of the builder's own material repair;
- merging PR #13 or PR #1 into their target branches before required gates;
- beginning Phase 1.

## Required reading

The builder entered through `development/03_plan/COLD_START.md`, then read the material needed to preserve the exact finding and existing authority boundaries:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`
2. `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md` — exact F-AR-001 record
3. `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`
4. `development/07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md` — observed duplicate-verifier trace
5. `development/01_governance/SOURCE_OF_TRUTH.md`
6. `development/01_governance/WORKING_PROTOCOL.md`
7. `development/01_governance/REASONING_POLICY.md`
8. `development/01_governance/ROLE_MODEL.md`
9. `development/01_governance/DECISION_POLICY.md`
10. `development/01_governance/CHANGE_POLICY.md`
11. `development/01_governance/VERIFICATION_POLICY.md`
12. `development/03_plan/PR_GATE.md`

Because the chosen repair changes cross-cutting cold-start/evidence/verification semantics, the builder followed `DECISION_POLICY.md` and recorded proposed architecture decision ADR-0002 rather than burying the choice in implementation prose.

## Builder repair output

The frozen material repair target is:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

Draft repair PR: **#13 — `WP-008: repair F-AR-001 pending independent-result discovery`**.

The exact material diff from builder base `bf1f89cbc2e407034c3f9a7a7d4ec7001a6a43c5` contains six files:

1. `development/03_plan/COLD_START.md`
   - adds a pending independent-result guard after authoritative Step 1 state/WP discovery and before independent role-specific execution;
   - resolves expected target, discovers/inspects same-WP evidence PRs, routes one current match to Integrator, and fails closed on stale/conflicting/ambiguous/uninspectable same-WP evidence;
   - preserves canonical `STATE.md` until the Integrator performs the authorised transition.
2. `development/01_governance/WORKING_PROTOCOL.md`
   - defines the independent-result publication contract: a completed published verifier/reviewer result requires a dedicated evidence PR containing the result artefact + handoff;
   - branch-only output is incomplete publication rather than an undiscoverable completed result.
3. `development/01_governance/VERIFICATION_POLICY.md`
   - binds verifier close/publication to the evidence-PR contract and makes the evidence PR an Integrator transition precondition;
   - preserves PASS / FAIL / NOT VERIFIED semantics and separate Integrator authority.
4. `development/03_plan/PR_GATE.md`
   - defines evidence-PR discovery/validation rules and explicit stale/conflict fail-closed behaviour;
   - keeps PR metadata as discovery metadata, not proof or canonical state.
5. `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`
   - proposed Class B architecture decision recording the chosen publication + pre-role guard mechanism and rejected alternatives.
6. `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md`
   - producer regression matrix covering the observed WP-006 / PR #10 verifier case, the WP-007 / PR #12 reviewer-close case, unrelated old-WP evidence, same-WP stale target, conflicting candidates, and discovery-unavailable behaviour.

No WP-000 acceptance criterion or historical verifier/reviewer artefact is changed in PR #13.

## Acceptance criteria — builder claim only

1. A generic cold-start has a deterministic repository-visible path to detect a completed but unintegrated independent verifier/reviewer result before beginning duplicate execution of the active independent role.
2. The repair preserves `STATE.md` + active WP as canonical current-work authority and does not promote evidence PRs/branches into a competing state authority.
3. The repair preserves role separation: verifier/reviewer evidence remains non-canonical until a separate Integrator performs the authorised transition.
4. The SESSION-0011 duplicate-verifier failure path is no longer reproducible under the repaired cold-start/control flow.
5. The equivalent reviewer-close state demonstrated by PR #12 is no longer able to route a generic fresh session into duplicate WP-007 reviewer execution before completed-result discovery.
6. Ambiguous, conflicting, stale, or target-mismatched result evidence fails closed or routes to an explicit bounded resolution path rather than silently choosing one result or role.
7. No WP-000 acceptance criterion, foundation rule, ADR/human gate, exact historical verification result, or WP-007 finding/judgement is weakened or reinterpreted.
8. The builder records the material repair target exactly and does not claim independent verification or adversarial re-review.

**Builder assessment:** all eight are claimed satisfied at target `a45b463...`, with the decision-relevant evidence recorded in ADR-0002 and the F-AR-001 regression evidence artefact. These remain producer claims only.

## Required verification and re-review

F-AR-001 is material and its repair changes the Phase 0 material target.

`development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md` is now the active fresh-verifier package for exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`.

The fresh verifier must:

- verify the complete changed target against all current WP-000 acceptance criteria;
- explicitly regression-test F-AR-001 using both the verifier and reviewer lifecycle cases;
- test stale/conflicting/ambiguous/unavailable discovery paths and unrelated historical evidence noise;
- treat the builder regression record as producer evidence rather than proof;
- publish its result through the dedicated evidence-PR contract;
- perform no repair or canonical result integration.

The prior WP-006 PASS remains historical/current only for exact target `c690f858e7682f5bdf0511c0f10b0e932d868b0e` and is not retargeted to the repair.

After fresh verification, an appropriate fresh separate adversarial re-review is required because F-AR-001 caused a material repair to the reviewed architecture. Result integration remains a separate Integrator responsibility.

## Completion state

Current: **builder responsibility complete — exact material repair published at PR #13 / `a45b463...`; fresh independent verification active under WP-009.**

This status means the builder has produced a verification candidate. It does **not** mean F-AR-001 is independently closed, ADR-0002 is accepted, WP-000/Phase 0 is accepted, or PR #13/PR #1 may merge.

WP-000/Phase 0 remains unaccepted. PR #13 and PR #1 remain draft/unmerged. Phase 1 remains blocked.

## Handoff

Builder close is recorded in `development/07_sessions/SESSION-0014-PHASE0-F-AR-001-REPAIR-BUILDER.md`.

Exact next responsibility: **fresh separate verifier under WP-009 against exact material target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`.** The builder must not perform that verification or the subsequent adversarial re-review in this session.
