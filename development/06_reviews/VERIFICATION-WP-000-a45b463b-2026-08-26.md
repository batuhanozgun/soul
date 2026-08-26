# VERIFICATION — WP-000 / WP-009 F-AR-001 REPAIR

**Verifier session:** SESSION-0015  
**Verification activity:** WP-009 — Phase 0 F-AR-001 Repair Verification  
**Verified commit/artefact:** `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Material target PR:** #13 — `WP-008: repair F-AR-001 pending independent-result discovery`  
**Specification:** `development/04_work/WP-009-PHASE0-F-AR-001-REPAIR-VERIFICATION.md`; parent `development/04_work/WP-000-DEVELOPMENT-OS.md`  
**Date:** 2026-08-26  
**Status:** verification in progress — pre-rationale expectations fixed before builder rationale/evidence

## Independence note

This verifier entered through canonical `development/03_plan/COLD_START.md` on `phase0/development-os`, completed Steps 1–2, then followed WP-009 Step 3A. The expected checks and result conditions below were derived before reading WP-008 builder rationale, ADR-0002 rationale, the repaired target files as a preferred design, builder regression conclusions, or SESSION-0014.

At verification start, direct PR #13 metadata inspection showed the PR remained open/draft and its material head was exactly `a45b463b083604d3f59d75bdca5ba97d5bc170e6`, matching WP-009's frozen target. This start freshness observation is not a close-time freshness check.

## Expected result derived from specification

Overall PASS is permitted only if all twelve current WP-000 acceptance criteria pass against exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` and every applicable WP-009 F-AR-001 control/regression criterion passes. Historical WP-006 PASS is evidence about the old target only and cannot certify this repair.

The repair is expected to preserve one canonical bootstrap/state authority while making the legitimate post-independent-result/pre-Integrator interval reliably discoverable before duplicate independent role execution. A completed verifier/reviewer evidence PR may trigger routing but must remain lower authority than `STATE.md` + active WP and must not itself canonically transition project state.

A correct repair must therefore satisfy all of the following independently testable conditions:

1. A fresh session still discovers phase, active WP, authority hierarchy, mandatory readings, role, and next responsibility from repository controls without old-chat replay.
2. `COLD_START.md` remains the single sequencing authority; the repair must not create a second bootstrap/current-state authority in Project Instructions, indexes, PR metadata, evidence PRs, or a new pending-state store.
3. Pending independent-result discovery, when the active WP assigns verifier/adversarial-reviewer work, must occur only after authoritative Step 1 state/WP/governance discovery and before duplicate independent role-specific execution or role declaration.
4. A completed published independent result must have an inspectable dedicated evidence PR containing the completed result artefact plus handoff and binding to active WP, role, and exact target. Branch-only producer output is insufficient to be silently treated as a completed published result.
5. Evidence PR title/body/labels are discovery metadata only. Candidate validity requires inspection of exact artefact/handoff contents and changed-file scope.
6. Evidence PRs remain lower-authority discovery triggers. `STATE.md` + active WP remain canonical until a separate Integrator validates the result and executes the authorised canonical transition.
7. Verifier/reviewer role separation remains intact: discoverability must not grant those roles repair, canonical integration, ADR acceptance, PR merge, Phase acceptance, or self-certification authority.
8. Historical verifier lifecycle replay: with the WP-006 verifier-required canonical state and completed PR #10 available, a fresh generic cold-start must route to the bounded Integrator path before duplicate verifier execution. The SESSION-0011 duplicate branch path must no longer be a valid outcome.
9. Historical reviewer lifecycle replay: with the WP-007 reviewer-required canonical state and completed PR #12 available, a fresh generic cold-start must route to the bounded Integrator path before duplicate reviewer execution.
10. Unrelated historical evidence, including WP-003/old-target evidence, must not be promoted to a current result or false conflict once WP/role/target mismatch is established.
11. Same-WP stale or target-mismatched evidence must not be promoted to current and must not permit silent duplicate independent execution; routing must fail closed to bounded resolution.
12. Multiple plausible, conflicting, ambiguous, incomplete, or mutually inconsistent same-WP candidates must not be arbitrarily selected and must not cause another independent execution; routing must fail closed to bounded Integrator resolution.
13. Failure to enumerate or inspect the required evidence surface must not be interpreted as "no pending result"; the control must expose a blocker/fail closed.
14. The repaired mechanism must not weaken any WP-000 acceptance criterion, foundation constraint, historical verifier/reviewer result, F-AR-001 wording, or WP-007 **Requires repair** judgement.
15. ADR-0002 must remain proposed; verifier PASS, if earned, cannot itself accept it or substitute for adversarial, Phase, owner, or PR gates.
16. WP-008 producer regression evidence may inform test inputs after expectations are fixed but cannot count as independent proof.
17. Post-target routing/evidence commits may preserve exact-target freshness only when they are demonstrably transition/evidence-only; any material semantics change requires fresh verification.
18. The verifier itself must perform no repair, canonical result integration, adversarial re-review, ADR acceptance, PR merge, Phase acceptance, or Phase 1 work.

## Planned verification methods

- exact PR/commit/blob inspection and changed-file scope checks;
- direct comparison of repaired files against authoritative governance and WP-000 criteria;
- deterministic replay of the PR #10 verifier and PR #12 reviewer lifecycle cases against the repaired decision path;
- negative decision-table tests for unrelated, stale, target-mismatched, conflicting, ambiguous, incomplete, and discovery-unavailable evidence;
- direct inspection of evidence-PR publication and Integrator authority boundaries;
- close-time PR #13 freshness re-check against the frozen SHA;
- semantic review only where deterministic inspection cannot decide a criterion.

## Checks

The criterion-by-criterion results are intentionally not populated until after the exact repair and producer material are inspected under WP-009 Step 3B.

## Findings

Pending verification execution.

## Overall result

Pending — PASS / FAIL / NOT VERIFIED will be issued only after the complete WP-009 verification and close-time freshness check.
