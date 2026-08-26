# WP-006 — Phase 0 Fresh Verification after F2-R1 + Reasoning Policy

**Status:** complete — verification activity issued **PASS**  
**Owner role:** verifier  
**Decision authority:** verifier issues PASS / FAIL / NOT VERIFIED; no repair, canonical integration, ADR acceptance, adversarial-review acceptance, target merge, or Phase-acceptance authority  
**Verifier output branch:** `verification/wp006-phase0-reasoning-reverification`  
**Verified target:** draft PR #1 exact head `c690f858e7682f5bdf0511c0f10b0e932d868b0e`  
**Verifier evidence PR:** #10 — integrated evidence-only by separate Integrator

## Objective

Freshly and independently verify the complete materially changed Phase 0 Development Operating System after:

1. WP-004 removal of the F2-R1 stale `BUILDER_STOP.md` routing surface;
2. WP-005 addition of the canonical development `REASONING_POLICY.md`, single-COLD_START integration, proposed ADR-0001 and strengthened WP-000 criterion 12;
3. correction and explicit recording of PD-002 work-package activation-order defect.

The result must be bound to the new exact PR #1 head. No historical PASS fragment may be reused as current certification.

## Result

The verification activity completed on 2026-08-26 and issued **PASS** against exact target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`.

- all twelve current WP-000 acceptance criteria: **PASS**;
- F2-R1 regression: **PASS**;
- single-bootstrap authority: **PASS**;
- reasoning-policy scope/proportionality and private-chain-of-thought boundary: **PASS**;
- self-verification separation: **PASS**;
- source-synthesis evidence integrity: **PASS**;
- ADR-0001 proposed-status/acceptance path: **PASS**;
- PD-002 final activation/current-work discipline: **PASS**;
- historical freshness and verifier-scope controls: **PASS**.

Canonical verifier artefact: `development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`.  
Verifier handoff: `development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`.

The PASS remains permanently bound to `c690f858e7682f5bdf0511c0f10b0e932d868b0e`. Evidence integration and result-routing commits after that target are not certified target commits; they remain valid only while they are transition-only under `VERIFICATION_POLICY.md`.

## Scope

- all **twelve** current WP-000 acceptance criteria;
- regression check for F2-R1;
- single cold-start/Project-instruction authority check;
- reasoning-policy scope, proportionality and epistemic controls;
- chain-of-thought boundary;
- owner vs technical authority boundary;
- source-synthesis evidence integrity;
- ADR-0001 proposed-status/acceptance path;
- PD-002 final current-work/activation discipline;
- preservation of verifier/adversarial/owner/Phase gates;
- exact-target freshness.

## Non-scope

- repairing any finding;
- rewriting the reasoning policy;
- accepting/rejecting ADR-0001 or ADR-0000;
- integrating the verifier's own result into canonical state;
- performing the separate adversarial review;
- merging PR #1 into `main`;
- beginning Phase 1.

## Required reading and independence order

Enter through `development/03_plan/COLD_START.md` and complete COLD_START Steps 1–2 first. The sequence below applies **only within Step 3**.

### A. Derive expectations before builder rationale

1. `development/01_governance/VERIFICATION_POLICY.md`
2. `development/04_work/WP-000-DEVELOPMENT-OS.md`
3. `development/00_foundation/VISION.md`
4. `development/00_foundation/DEFINITION.md`
5. `development/00_foundation/SUCCESS_CRITERIA.md`
6. `development/00_foundation/NON_NEGOTIABLES.md`
7. `development/01_governance/SOURCE_OF_TRUTH.md`
8. `development/01_governance/WORKING_PROTOCOL.md`
9. `development/01_governance/REASONING_POLICY.md`
10. `development/01_governance/ROLE_MODEL.md`
11. `development/01_governance/DECISION_POLICY.md`
12. `development/01_governance/CHANGE_POLICY.md`
13. `development/03_plan/COLD_START.md`
14. `development/03_plan/NEXT_SESSION.md`
15. `development/03_plan/CHATGPT_PROJECT_ENTRY.md`
16. `development/03_plan/WORKSPACE_INDEX.md`
17. `development/03_plan/PR_GATE.md`
18. `development/03_plan/PHASE_GATE.md`

At this point derive and record the expected result/tests for all twelve WP-000 criteria, F2-R1, reasoning-policy integration and PD-002 before reading builder rationale/handoffs.

### B. Then inspect change rationale/evidence

19. `development/04_work/WP-004-PHASE0-F2R1-REPAIR.md`
20. `development/04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md`
21. `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
22. `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
23. `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`
24. `development/07_sessions/SESSION-0008-PHASE0-F2R1-REPAIR-BUILDER.md`
25. `development/07_sessions/SESSION-0009-PHASE0-REASONING-POLICY-BUILDER.md`
26. historical latest verifier artefact `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md` only as old-target evidence.

PR metadata may be inspected at start and close solely to capture/re-check exact target freshness.

## Acceptance criteria

1. Every current WP-000 criterion 1–12 receives PASS / FAIL / NOT VERIFIED with exact-target evidence.
2. Exact current draft PR #1 head SHA is captured independently at start and freshness-checked before verifier output closes.
3. **F2-R1 regression:** no current non-historical/non-derived planning or governance artefact materialises a stale competing current WP/next-responsibility pointer; `BUILDER_STOP.md` is absent and current routing remains single-source.
4. **Single bootstrap authority:** `COLD_START.md` remains the only sequencing authority; `REASONING_POLICY.md`, WP required-reading sections and `CHATGPT_PROJECT_ENTRY.md` do not create incompatible or duplicate ordering.
5. **Reasoning policy sufficiency:** current criterion 12 is satisfied at the exact target, including epistemic labels/proof limits, objective-method-state-evidence separation, triggered framing/necessity/alternatives/falsification/root-cause controls, analytical provenance, owner-vs-technical authority and proportional reasoning depth.
6. **No private chain-of-thought requirement:** policy requires only decision-relevant observable rationale/evidence and explicitly excludes private chain-of-thought disclosure/storage.
7. **No self-verification laundering:** reasoning-policy compliance does not become proof; producer/verifier separation and exact-target verification remain intact.
8. **Evidence integrity:** the synthesis evidence distinguishes source-observed principles from SOUL-specific design choices and does not count duplicated predecessor files as independent corroboration.
9. **ADR-0001 status:** remains proposed; verifier result does not silently accept it. Required review/owner/Phase gates remain explicit.
10. **PD-002:** the historical activation-order defect is accurately recorded, final canonical state is coherent, and current governance is sufficient to identify the required ordering; any claim that a new mechanical gate is required must be separately justified rather than assumed from one incident.
11. Historical verifier artefacts remain bound to their old exact targets and are not edited/reused as current proof.
12. Verifier performs no repair, result integration, ADR acceptance, adversarial review, target merge or Phase 1 work.

Overall PASS requires every mandatory current WP-000 criterion and the explicit regressions above to pass. NOT VERIFIED remains legitimate where evidence is insufficient.

## Verification methods

Prefer, where applicable:

- exact immutable file/commit inspection;
- repository-tree/reference checks;
- direct comparison of current routing surfaces;
- deterministic text/reference checks for duplicate bootstrap/current-state claims;
- source-to-synthesis spot checks using recorded source file/blob identities;
- semantic review only for properties that cannot be deterministically established.

Do not treat builder acceptance tables as proof.

## Outputs

- a new verification artefact under `development/06_reviews/` with a unique name, bound to the exact target SHA;
- a fresh verifier session handoff under `development/07_sessions/`;
- no target repair/integration changes.

## Completion state

This WP is **complete as a verification activity**. Its acceptance criteria were executed and it issued PASS for the exact target above.

This does **not** make WP-000/Phase 0 accepted, does not accept ADR-0000 or ADR-0001, does not satisfy the separate adversarial-review requirement, and does not certify any later material target change.

## Handoff

A separate Integrator inspected and merged verifier evidence PR #10 without reinterpretation and routed PASS to `WP-007-PHASE0-ADVERSARIAL-REVIEW.md`.

The next required responsibility is a fresh **adversarial reviewer** under WP-007. Any material change after the verified target requires freshness re-evaluation and, where applicable, fresh independent verification.
