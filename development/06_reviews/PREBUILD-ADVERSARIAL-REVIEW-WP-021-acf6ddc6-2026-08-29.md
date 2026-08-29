# PRE-BUILD ADVERSARIAL REVIEW — WP-021 DEVELOPMENT LIFECYCLE DESIGN

**Reviewer session:** `SESSION-0039`  
**Reviewed repository:** `batuhanozgun/soul`  
**Reviewed PR:** `#28` — draft, open, unaccepted, unmerged  
**Reviewed commit:** `acf6ddc621c644e5a0960e3382b25928d2518041`  
**Reviewed base:** `6fca29474ab97d22e363108b8be6438456316e01`  
**Result-control key:** `WP-022 / adversarial reviewer / acf6ddc621c644e5a0960e3382b25928d2518041 / attempt 1`  
**Authoritative specification:** `WP-000`, `WP-021`, `WP-022`, current foundation and governance  
**Date:** 2026-08-29

## Independence boundary and exact-target precheck

This section and the expected attack matrix below were recorded before reading
the target lifecycle, proposed ADR-0003, producer function/role analysis,
producer replay protocol or SESSION-0037 rationale.

Observed live PR metadata at the precheck:

- PR #28 was open and draft, base branch `phase0/development-os`, base commit
  `6fca29474ab97d22e363108b8be6438456316e01`, head branch
  `work/wp021-development-lifecycle-improvement`, and head commit
  `acf6ddc621c644e5a0960e3382b25928d2518041`;
- GitHub reported one commit, 1,200 additions, zero deletions and five changed
  files;
- direct Git diff confirmed that all five paths were additions and exactly
  matched the target list in WP-022;
- no current operational governance policy was in the exact target diff.

## Expected attack matrix frozen before producer rationale

| Attack class | Protected claim/property | Disproof probe fixed before target reading | Evidence needed to reject the attack |
|---|---|---|---|
| Planner necessity | A distinct Planner motivation is necessary and simpler deterministic or existing-role routing is insufficient. | Remove Planner as an actor; test whether explicit routing criteria plus Designer-owned technical selection preserve the same boundaries. Look for work-selection outputs that are mechanical enough to encode without a new role. | A concrete conflict-of-motivation analysis plus duties that cannot be safely absorbed or mechanised, with explicit cost/failure comparison. |
| Planner authority | Planner cannot become owner, architect, acceptance editor or backlog dictator. | Feed an ambiguous material finding, missing evidence and schedule pressure; trace who may alter objective, scope, criteria, priority and stop state. Test indefinite analysis/escalation. | Explicit non-authorities, bounded output contract, escalation destination and liveness/appeal path that preserve owner and technical decision boundaries. |
| Route correctness | Routes are deterministic enough to avoid oscillation, deadlock, universal escalation and preference-based de-escalation. | Construct borderline materiality, unavailable evidence, repeated low findings and one strong trigger mixed with routine work. Replay classification twice from identical facts. | Stable precedence, strong-trigger monotonicity, evidence-unavailable state, bounded recovery and auditable rationale. |
| Designer/Builder split | Separation changes completion motivation without merely moving the same conflict into Designer. | Let framing evidence change during design and let build expose an unstated material choice; test whether Designer can prematurely optimise for buildability and Builder can relabel redesign as local implementation. | Distinct success conditions, build-ready contract, enforceable materiality/reopen rules and no producer self-certification. |
| Pre-build independence | Challenge reduces anchoring rather than multiplying correlated agreement. | Use the same underlying model/role across pre- and post-build review; test shared assumptions, rationale leakage and Designer-controlled synthesis of findings. | Fresh-context ordering, explicit same-model limitation, immutable finding disposition, and independent control over whether material findings block implementation. |
| Integrator boundary | Integration is faithful mechanics, while substantive next-work selection remains elsewhere. | Issue FAIL, NOT VERIFIED and a review finding that supports several credible next actions; trace whether Integrator can manufacture or choose repair-shaped work. | Integrator output is result-preserving only and hands an explicit unresolved decision surface to an authorised selector without semantic routing. |
| Technical ADR ownership | A non-owner technical decision can be accepted without producer self-acceptance or Integrator authority leakage. | Make Designer the proposer/decision owner and ask who determines independent-review sufficiency, resolves findings and changes ADR status. | Separate acceptance conditions and actor, deterministic gate evidence, conflict path and no circular approval. |
| Context selection | Reduced context does not hide institutional truth or create a second authority hierarchy. | Misclassify decisive evidence as forensic or retrieve-on-trigger when the actor cannot know the trigger; test verifier/reviewer independence and cold-start recovery. | Authoritative metadata owner, fail-closed retrieval triggers, correction mechanism, minimum role context and source-of-truth precedence. |
| Replay validity | Historical replay can estimate pre-build value without leakage, resource bias or self-confirming evaluation. | Trace commit visibility, prompt/context contamination, evaluator access, baseline fidelity, token/agent imbalance, outcome-sensitive rubric changes and multiple-trial variance. | Frozen snapshots/inputs/rubric, credible blind boundary, comparable budgets, repeated trials, false-positive/cost measures and explicit limits on generalisation. |
| Preservation/rollback | Adoption preserves exact-target history, current result controls, fresh-session restart and owner boundaries; rollback remains executable after later history. | Simulate partial rollout, failed implementation and post-rollout canonical commits; attempt fallback without rewriting history or losing later evidence. | Forward restoration/migration plan, invariant checks, disable path and exact checkpoint semantics beyond a bare branch pointer. |
| Meta-work liveness | WP-021 cannot indefinitely displace unresolved WP-020/F-AR-008. | Let review/replay/synthesis stay inconclusive or repeatedly reopen; search for time/evidence/decision bounds and an explicit blocked outcome. | Bounded gate states and owner-visible stop/escalation criteria that neither falsely resolve F-AR-008 nor permit endless process redesign. |
| Complexity burden | Added roles, handoffs and artefacts earn their failure and coordination cost. | Compare against a smaller lifecycle using explicit gates and temporary responsibility separation; count new handoffs, state transitions and failure points. | Necessity-by-function, measurable effectiveness/cost thresholds and a simplification/reopen rule when benefit is absent. |
| Generality | The lifecycle is not overfit to result-control repair lineage. | Apply its contracts to a greenfield Phase-1 definition task and a materially different analytical/design task with no prior failure finding. | Domain-neutral protected properties, route examples beyond repair work and prospective evidence requirements. |
| Governance compatibility | Proposed lifecycle cannot silently supersede current authority before acceptance. | Look for normative present-tense claims that operational roles may execute before ADR/replay/synthesis/implementation gates, or duplicated semantics that conflict with current policies. | Explicit proposal status, precedence rules, implementation mapping and fresh assurance after operational change. |

## First-pass design attack

Pending exact-target design inspection.

## Producer evidence challenge

Pending; producer rationale remains unread at the time of this commit.

## Findings

Pending.

## Overall judgement

Pending completion of the required adversarial review. This draft is not a
result and grants no implementation or acceptance authority.
