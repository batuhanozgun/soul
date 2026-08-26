# WP-010 — Phase 0 F-AR-001 Repair Adversarial Re-review

**Status:** active  
**Owner role:** adversarial-reviewer  
**Decision authority:** independently attack the exact WP-008 repair target and issue evidence-backed findings / an overall suitability judgement; no repair, canonical result integration, ADR acceptance, PR #13 merge, PR #1 merge, Phase acceptance, or Phase 1 authority  
**Development branch:** `phase0/development-os`  
**Material target PR:** #13 — `WP-008: repair F-AR-001 pending independent-result discovery`  
**Exact material target:** `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Repair package:** `WP-008-PHASE0-F-AR-001-REPAIR.md`  
**Verification activity:** `WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md` — completed **PASS** for this exact target  
**Trigger:** WP-009 verifier PASS integrated evidence-only from PR #14 as merge commit `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`

## Objective

Freshly and separately adversarially re-review exact repaired material target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` after WP-009 PASS, with particular emphasis on bypasses, spoofing, ambiguity, authority leakage and discovery/tooling failure paths that ordinary verification may not expose.

This activity must try to disprove the repaired control architecture rather than repeat the verifier checklist or accept the builder/verifier rationale. A clean review is legitimate if the evidence supports it; no finding quota exists.

## Exact target and freshness rule

The review target is exactly:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

The WP-009 PASS remains permanently bound only to that same SHA. At review start and immediately before close, inspect PR #13 and confirm its head is still exactly this SHA. Any material target movement requires classification and a new exact-target verification/re-review path rather than silent retargeting.

Post-target repository commits may be treated as non-retargeting only after they are inspected and classified as evidence integration or transition-only routing under `VERIFICATION_POLICY.md`.

## Scope

Attack surfaces include, without imposing a finding quota:

- the repaired F-AR-001 lifecycle: completed but unintegrated verifier/reviewer evidence during the post-result/pre-Integrator interval;
- bypass or spoof paths around the pending-result discovery guard;
- PR metadata, artefact/handoff binding and changed-file-scope validation failures;
- same-WP stale, target-mismatched, conflicting, ambiguous, incomplete or maliciously-shaped result evidence;
- repository/PR discovery or inspection unavailability and fail-closed behaviour;
- unrelated historical evidence being mistaken for current evidence, or current evidence being incorrectly ignored;
- role confusion, authority leakage, verifier/reviewer self-transition, or evidence becoming a second canonical state authority;
- circular verification, freshness laundering, false completion or transition-only classification abuse;
- the historical WP-006 / PR #10 duplicate-verifier lifecycle and WP-007 / PR #12 reviewer-close lifecycle under the repaired control flow;
- interaction of the repair with current WP-000 acceptance criteria, especially cold-start sufficiency, single-source discipline, role separation, verification discipline, session continuity and no-false-completion controls;
- the transition chain after exact target `a45b463...`, including PR #14 evidence integration and the WP-009 → WP-010 canonical routing, to confirm those changes do not materially alter the reviewed target;
- any additional material failure path discovered from the repaired architecture.

## Non-scope

- repairing any finding;
- changing the WP-008 repair mechanism;
- changing or weakening WP-000 acceptance criteria;
- reinterpreting the WP-009 PASS or historical WP-007 **Requires repair** judgement;
- accepting/rejecting ADR-0000, ADR-0001 or ADR-0002;
- canonically integrating the reviewer's own result;
- merging PR #13 or PR #1;
- accepting Phase 0 or beginning Phase 1.

## Required reading and independence order

Enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 on the canonical development line first. The ordering below applies within Step 3.

### A. Establish attack model before relying on producer/verifier conclusions

Read:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`
2. `development/00_foundation/VISION.md`
3. `development/00_foundation/DEFINITION.md`
4. `development/00_foundation/SUCCESS_CRITERIA.md`
5. `development/00_foundation/NON_NEGOTIABLES.md`
6. `development/01_governance/SOURCE_OF_TRUTH.md`
7. `development/01_governance/WORKING_PROTOCOL.md`
8. `development/01_governance/REASONING_POLICY.md`
9. `development/01_governance/ROLE_MODEL.md`
10. `development/01_governance/DECISION_POLICY.md`
11. `development/01_governance/CHANGE_POLICY.md`
12. `development/01_governance/VERIFICATION_POLICY.md`
13. `development/03_plan/COLD_START.md`
14. `development/03_plan/PR_GATE.md`
15. `development/03_plan/PHASE_GATE.md`
16. `development/06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`
17. `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md` — exact historical F-AR-001 claim/evidence/failure path/result
18. `development/07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md` — observed duplicate-verifier lifecycle
19. `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md` — reviewer-close lifecycle

Persist the adversarial attack surfaces/hypotheses before relying on WP-008 builder rationale, builder regression conclusions, WP-009 verifier conclusions, or the current Integrator's routing conclusion.

### B. Then inspect the repair target and prior evidence

20. `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md`
21. PR #13 metadata, changed-file list and exact diff at `a45b463b083604d3f59d75bdca5ba97d5bc170e6`
22. exact target versions of the six repair files:
   - `development/03_plan/COLD_START.md`
   - `development/01_governance/WORKING_PROTOCOL.md`
   - `development/01_governance/VERIFICATION_POLICY.md`
   - `development/03_plan/PR_GATE.md`
   - `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`
   - `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md`
23. `development/07_sessions/SESSION-0014-PHASE0-F-AR-001-REPAIR-BUILDER.md`
24. `development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md`
25. `development/06_reviews/VERIFICATION-WP-000-a45b463b-2026-08-26.md`
26. `development/07_sessions/SESSION-0015-PHASE0-F-AR-001-REPAIR-VERIFIER.md`
27. PR #14 metadata/changed-file scope and evidence-only merge record
28. the current transition-only WP-009 → WP-010 state/handoff changes

## Acceptance criteria

The reviewer must produce evidence for each applicable item and issue an overall judgement.

1. **Exact-target freshness:** PR #13 remains bound to exact `a45b463...` at start/close, or any movement is explicitly classified and handled without silent retargeting.
2. **Adversarial independence:** attack hypotheses are persisted before relying on builder/verifier conclusions.
3. **F-AR-001 bypass resistance:** actively attempt to reproduce or mutate the post-result/pre-Integrator duplicate-role failure against the repaired mechanism, including both verifier and reviewer lifecycles.
4. **Spoof/conflict/stale resistance:** attempt to make stale, target-mismatched, conflicting, ambiguous, incomplete or misleading evidence produce an unsafe route.
5. **Discovery-failure containment:** inspect whether repository/PR discovery or evidence-inspection failure can fail open or silently duplicate independent work.
6. **Authority containment:** attempt to make evidence PRs, verifier/reviewer roles, PR metadata or subordinate views become a competing canonical state/transition authority.
7. **Freshness/transition integrity:** inspect post-target PR #14 evidence integration and WP-009 → WP-010 routing and classify them as transition-only or material; any material change reopens verification/re-review.
8. **No false completion:** confirm a verifier PASS does not by itself accept ADR-0002, merge PR #13/#1, accept Phase 0 or begin Phase 1.
9. **Historical preservation:** F-AR-001 and the WP-007 **Requires repair** record remain historical evidence and are not rewritten to manufacture closure.
10. **Broader material attack:** attempt to identify any other material WP-000 failure introduced or exposed by the six-file repair.
11. **Reviewer scope discipline:** perform no repair, ADR acceptance, canonical result integration, target merge, Phase acceptance or Phase 1 work.
12. **Evidence-backed close:** publish findings (or no surviving finding) with disproof attempts, limitations, exact target and an overall suitability judgement.

## Outputs and publication

The reviewer must produce:

- a uniquely named adversarial-review artefact under `development/06_reviews/`, bound to exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`;
- a fresh reviewer handoff under `development/07_sessions/`;
- a dedicated reviewer evidence PR targeting `phase0/development-os` containing only authorised review/session outputs;
- no repair, ADR status change, canonical-state transition, target merge or Phase acceptance change.

## Result routing

After reviewer publication/close, a **separate Integrator** must validate/integrate the review evidence and perform the next canonical transition without reinterpretation.

A surviving material finding routes to the smallest bounded authorised repair/resolution path. A review that leaves no surviving material finding permits routing only to the remaining declared ADR/human-owner/PR/Phase gates; it does not itself accept an ADR, Phase 0, PR #13 or PR #1.

## Completion state

Current: **active — fresh separate adversarial re-review required for exact WP-008 repair target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`.**

WP-009 verification activity has issued **PASS** for this exact target and is complete as a verification activity once its canonical transition is recorded. PR #13 and PR #1 remain unmerged/draft. ADR-0000, ADR-0001 and ADR-0002 remain unaccepted/proposed according to their declared paths. Phase 0 remains unaccepted and Phase 1 remains blocked.
