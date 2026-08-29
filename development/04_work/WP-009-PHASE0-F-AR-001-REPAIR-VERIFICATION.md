# WP-009 — Phase 0 F-AR-001 Repair Verification

**Status:** complete — verification activity issued **PASS** for exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`; evidence integrated by separate Integrator  
**Owner role:** verifier  
**Decision authority:** independently issue PASS / FAIL / NOT VERIFIED for the exact WP-008 repair target; no repair, canonical result integration, adversarial re-review, ADR acceptance, PR #13 merge, PR #1 merge, Phase acceptance, or Phase 1 authority  
**Development branch:** `phase0/development-os`  
**Material target PR:** #13 — `WP-008: repair F-AR-001 pending independent-result discovery`  
**Exact material target:** `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Repair package:** `WP-008-PHASE0-F-AR-001-REPAIR.md`  
**Trigger:** WP-008 builder close; F-AR-001 repair is a producer claim only and requires fresh exact-target verification

## Objective

Freshly and independently verify the complete WP-008 material repair target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` against all current WP-000 acceptance criteria and the explicit F-AR-001 repair obligations, without relying on builder confidence or reusing the historical WP-006 PASS.

The verifier must establish whether the repaired development operating system actually prevents/detects duplicate independent verifier/reviewer execution during the post-result/pre-Integrator interval while preserving canonical-state authority, exact-target freshness, and role separation.

## Exact target and freshness rule

The verification target is exactly:

`a45b463b083604d3f59d75bdca5ba97d5bc170e6`

This is the frozen material head published in draft repair PR #13.

The historical WP-006 PASS remains permanently bound only to:

`c690f858e7682f5bdf0511c0f10b0e932d868b0e`

It is not current certification for the WP-008 repair.

At verification start and again before verifier close:

1. inspect PR #13 metadata and confirm its material head is still exactly `a45b463b083604d3f59d75bdca5ba97d5bc170e6`;
2. if PR #13 head has moved, classify the movement before proceeding;
3. any material change after the target makes this WP's fixed target stale and requires a new exact target rather than silently retargeting the verification;
4. do not treat canonical routing/handoff changes on `phase0/development-os` as part of the repair target unless they materially alter a property being verified.

## Scope

- all twelve current WP-000 acceptance criteria against the exact repaired target;
- exact F-AR-001 finding obligations from WP-007/WP-008;
- `COLD_START.md` pending independent-result guard placement and semantics;
- verifier/adversarial-review evidence-PR publication contract;
- preservation of `STATE.md` + active WP as canonical current-work authority;
- preservation of separate Integrator-owned canonical result transition;
- exact target/role/WP binding for pending-result discovery;
- fail-closed handling of same-WP stale, target-mismatched, conflicting, ambiguous, incomplete, or uninspectable evidence;
- rejection of unrelated historical evidence as a current result after mismatch is established;
- explicit replay of the observed WP-006 verifier / PR #10 lifecycle case;
- explicit replay of the WP-007 reviewer / PR #12 lifecycle case;
- no duplicate bootstrap/state authority through Project Instructions, indexes, PR metadata, or evidence PRs;
- ADR-0002 remains proposed and unaccepted;
- preservation of historical evidence and WP-007 `Requires repair` / F-AR-001 wording.

## Non-scope

- repairing any verifier finding;
- changing the WP-008 repair mechanism;
- changing WP-000 acceptance criteria;
- accepting/rejecting ADR-0000, ADR-0001, or ADR-0002;
- performing the required separate adversarial re-review;
- integrating the verifier's own result into canonical state;
- merging PR #13 or PR #1;
- accepting Phase 0 or beginning Phase 1.

## Required reading and independence order

Enter through `development/03_plan/COLD_START.md` and complete COLD_START Steps 1–2 using the canonical development line first. This WP is the active WP discovered in Step 1. The ordering below applies only within Step 3.

### A. Derive expectations before builder rationale/evidence

Read and derive the expected result/test plan before reading WP-008 builder rationale, ADR-0002 rationale, or builder regression conclusions:

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
14. `development/03_plan/PR_GATE.md`
15. `development/03_plan/PHASE_GATE.md`
16. `development/03_plan/CHATGPT_PROJECT_ENTRY.md`
17. `development/03_plan/NEXT_SESSION.md`
18. `development/03_plan/WORKSPACE_INDEX.md`
19. `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md` — read the exact F-AR-001 claim/evidence/failure-path/result, not the repair proposal
20. `development/07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md` — observed duplicate-verifier trace
21. `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md` — reviewer-close lifecycle reproduction

At this point persist the expected checks/result conditions before reading builder rationale or the repaired files as a preferred design.

### B. Then inspect the exact repair and builder evidence

22. `development/04_work/WP-008-PHASE0-F-AR-001-REPAIR.md`
23. draft PR #13 metadata, changed-file list, and exact diff at target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`
24. exact target versions of the six changed repair artefacts:
   - `development/03_plan/COLD_START.md`
   - `development/01_governance/WORKING_PROTOCOL.md`
   - `development/01_governance/VERIFICATION_POLICY.md`
   - `development/03_plan/PR_GATE.md`
   - `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`
   - `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md`
25. `development/07_sessions/SESSION-0014-PHASE0-F-AR-001-REPAIR-BUILDER.md` only after expectations are fixed
26. PR #10 metadata/changed-file scope and its exact verifier artefact/handoff
27. PR #12 metadata/changed-file scope and its exact review artefact/handoff
28. relevant historical WP-003 evidence PRs only as stale/unrelated-noise inputs for the negative regression

## Acceptance criteria

The verifier must issue PASS / FAIL / NOT VERIFIED for each item below with exact-target evidence.

1. **All current WP-000 criteria:** criteria 1–12 are independently re-checked against exact repair target `a45b463...`; no historical PASS is reused as current proof.
2. **Exact target freshness:** PR #13 and target SHA are captured independently at start and re-checked at close; any target movement is classified rather than silently absorbed.
3. **Single bootstrap authority:** `COLD_START.md` remains the one sequencing authority; the repair adds a guard inside it rather than creating a second bootstrap procedure in Project Instructions, PR metadata, an index, or a pending-state file.
4. **Guard timing:** when the active WP assigns an independent verifier/adversarial reviewer, pending-result discovery occurs after authoritative Step 1 state/WP/governance discovery but before duplicate independent role-specific execution/role declaration.
5. **Publication boundary:** a completed published independent result requires a dedicated evidence PR containing completed result artefact + handoff with active WP/role/exact-target binding; branch-only output is not silently treated as a completed published result.
6. **Canonical authority preserved:** evidence PRs remain lower-authority discovery triggers; `STATE.md` + active WP remain canonical until a separate Integrator validates and transitions the result.
7. **Role separation preserved:** verifier/reviewer cannot canonically integrate, repair, or accept their own result merely because publication is discoverable; Integrator authority remains separate and bounded.
8. **Verifier regression — SESSION-0011 / PR #10:** replaying the historical WP-006 canonical verifier-required state with PR #10 available routes the fresh session to Integrator before duplicate verifier execution. The observed duplicate verifier branch path is no longer a valid outcome under the repaired control flow.
9. **Reviewer regression — PR #12:** replaying the historical WP-007 reviewer-required state with completed PR #12 available routes the fresh session to Integrator before duplicate WP-007 reviewer execution.
10. **Unrelated historical evidence:** WP-003/old-target evidence does not become a current result or false conflict once its different WP/target is established.
11. **Stale/target-mismatched same-WP evidence:** it is not promoted as current and does not allow silent duplicate independent execution; routing fails closed to the bounded resolution path.
12. **Conflicting/ambiguous same-WP evidence:** multiple plausible or inconsistent candidates do not get arbitrarily selected and do not cause a further duplicate role; routing fails closed to bounded Integrator resolution.
13. **Discovery/inspection failure:** inability to enumerate/inspect required result evidence does not get interpreted as "no pending result"; the control records a blocker/fails closed.
14. **Evidence validation depth:** PR title/body/labels are discovery metadata only; exact artefact/handoff contents and changed-file scope must be inspected before a candidate is treated as a current pending result.
15. **No acceptance/historical weakening:** no WP-000 criterion, foundation rule, historical verifier/reviewer result, F-AR-001 wording, or WP-007 **Requires repair** judgement is edited/weakened by the repair.
16. **ADR-0002 status:** remains proposed; verifier result does not accept it or substitute for required adversarial/Phase/owner gates.
17. **No producer self-certification:** WP-008 builder regression table is treated as producer evidence only; verifier independently derives and executes the checks.
18. **Verifier scope discipline:** verifier performs no repair, result integration, adversarial re-review, ADR acceptance, PR merge, Phase acceptance, or Phase 1 work.

Overall PASS requires every mandatory current WP-000 criterion and all applicable F-AR-001 regression/control criteria above to PASS. `NOT VERIFIED` remains legitimate where the required evidence/capability is insufficient.

## Verification methods

Prefer, in order where applicable:

- exact commit/blob and PR metadata inspection;
- changed-file and diff scope checks;
- direct replay of historical `STATE.md` + active WP + PR #10/#12 inputs through the repaired decision table;
- negative tests for stale, conflicting, ambiguous, unrelated, and discovery-unavailable cases;
- direct authority/source-of-truth comparison;
- semantic model review only for properties that cannot be decided deterministically.

Do not treat builder prose, ADR rationale, PR body, or a green-looking table as proof.

## Outputs and publication

The verifier must produce:

- a uniquely named verification artefact under `development/06_reviews/`, bound to exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`;
- a fresh verifier handoff under `development/07_sessions/`;
- a dedicated verifier evidence PR targeting `phase0/development-os` that contains only those authorised verification/session outputs and satisfies the publication contract being verified;
- no material repair or canonical-state transition change.

## Result routing

After verifier publication/close, a **separate Integrator** validates and integrates the verifier evidence and performs the canonical result transition without reinterpretation.

- **PASS** → route to the required fresh separate adversarial re-review of the same exact WP-008 material target before repair acceptance/integration.
- **FAIL** → route the exact finding(s) to the smallest bounded separate builder repair; any changed target requires fresh verification.
- **NOT VERIFIED** → route the smallest bounded investigation/repair needed to resolve the blocker, then fresh verification.

The verifier must not perform this transition itself.

## Integration record

Verifier evidence PR #14 contained exactly two authorised files: `development/06_reviews/VERIFICATION-WP-000-a45b463b-2026-08-26.md` and `development/07_sessions/SESSION-0015-PHASE0-F-AR-001-REPAIR-VERIFIER.md`.

A separate Integrator inspected the exact PR scope and both files, confirmed the immutable result **PASS** was bound only to exact material target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`, confirmed PR #13 still had that exact head, and merged PR #14 evidence-only into `phase0/development-os` as merge commit `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`.

No repair, ADR acceptance, PR #13/PR #1 merge, Phase acceptance or Phase 1 work was performed by that evidence merge or by the canonical transition. The PASS is routed mechanically to fresh separate adversarial re-review under `WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md`.

## Completion state

**Complete as a verification activity — result: PASS for exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6`.**

This status does not accept the WP-008 repair, ADR-0000/0001/0002, PR #13, PR #1 or Phase 0. The required fresh separate adversarial re-review is active under WP-010. Any material change to the exact repair target reopens fresh verification for the changed target.
