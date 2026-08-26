# WP-008 — Phase 0 F-AR-001 Repair

**Status:** active  
**Owner role:** designer/builder  
**Decision authority:** bounded repair of F-AR-001 within existing foundation/governance and unchanged WP-000 acceptance criteria; substantive architecture choices must follow `DECISION_POLICY.md`; no independent verification, adversarial-review self-approval, ADR acceptance, PR #1 merge, Phase acceptance, or Phase 1 authority  
**Branch:** fresh builder-repair branch/execution based on `phase0/development-os`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Trigger:** WP-007 adversarial review judgement **Requires repair**, surviving finding F-AR-001  
**Review evidence:** `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`  
**Reviewer handoff:** `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`  
**Evidence PR:** #12, integrated evidence-only as merge commit `9de8a011aa2d14fb985181ba3f180f729342901d`

## Objective

Repair exactly F-AR-001 so a generic fresh-session cold-start can reliably detect a completed but not-yet-canonically-integrated independent verifier/reviewer result before it commits to duplicating the just-completed independent role, while preserving the existing separation between evidence production and Integrator-owned canonical state transition.

This WP routes the finding; it does not prescribe the repair mechanism. The builder must derive the smallest mechanism that satisfies the finding and existing governance.

## Exact finding

**F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated independent result.**

The WP-007 reviewer found that the architecture intentionally leaves canonical `STATE.md` unchanged during the post-result/pre-Integrator interval, while `COLD_START.md` does not deterministically surface a completed independent verifier/reviewer result before role selection. SESSION-0011 contains an observed duplicate-verifier execution trace, and reviewer close reproduced the same lifecycle state with completed reviewer evidence PR #12 while canonical state still assigned WP-007 reviewer work.

**Reviewer result:** stands.  
**Severity:** medium — material.  
**Overall WP-007 judgement:** **Requires repair.**

The canonical claim/evidence/failure-path/impact/disproof record remains the WP-007 adversarial-review artefact and must not be rewritten by this repair WP.

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
- accepting/rejecting ADR-0000 or ADR-0001;
- independent verification or adversarial re-review of the builder's own material repair;
- merging PR #1 into `main` or beginning Phase 1.

## Required reading

Enter through `development/03_plan/COLD_START.md`, then read the material needed to preserve the exact finding and existing authority boundaries:

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

If the chosen repair changes cross-cutting authority, state semantics, evidence/verification semantics, or another architecture-level contract, follow `DECISION_POLICY.md` rather than burying that decision inside implementation prose. This routing WP does not pre-decide the repair architecture.

## Acceptance criteria — builder claim only

1. A generic cold-start has a deterministic repository-visible path to detect a completed but unintegrated independent verifier/reviewer result before beginning duplicate execution of the active independent role.
2. The repair preserves `STATE.md` + active WP as canonical current-work authority and does not promote evidence PRs/branches into a competing state authority.
3. The repair preserves role separation: verifier/reviewer evidence remains non-canonical until a separate Integrator performs the authorised transition.
4. The SESSION-0011 duplicate-verifier failure path is no longer reproducible under the repaired cold-start/control flow.
5. The equivalent reviewer-close state demonstrated by PR #12 is no longer able to route a generic fresh session into duplicate WP-007 reviewer execution before completed-result discovery.
6. Ambiguous, conflicting, stale, or target-mismatched result evidence fails closed or routes to an explicit bounded resolution path rather than silently choosing one result or role.
7. No WP-000 acceptance criterion, foundation rule, ADR/human gate, exact historical verification result, or WP-007 finding/judgement is weakened or reinterpreted.
8. The builder records the material repair target exactly and does not claim independent verification or adversarial re-review.

These are producer claims only. They do not satisfy the required independent gates.

## Required verification and re-review

F-AR-001 is material and its repair changes the Phase 0 material target. After the builder closes:

- a fresh independent verifier must verify the complete changed Phase 0 target against the current WP-000 acceptance criteria and explicitly regression-test F-AR-001, including both the verifier and reviewer lifecycle cases;
- the prior WP-006 PASS remains historical/current only for exact target `c690f858e7682f5bdf0511c0f10b0e932d868b0e` and must not be retargeted to the repair commit;
- after fresh verification, an appropriate fresh separate adversarial re-review is required because the surviving WP-007 finding caused a material repair to the reviewed architecture;
- result integration remains a separate Integrator responsibility.

## Completion state

Current: **active — fresh separate builder repair required.**

WP-000/Phase 0 remains unaccepted. PR #1 remains draft. Phase 1 remains blocked.

## Handoff

Builder close must leave the exact repair commit/target, changed artefacts, decision/ADR consequences if any, regression evidence, unresolved items, and the exact fresh-verifier next responsibility. The builder must not perform the independent verifier or adversarial-review roles in the same repair session.
