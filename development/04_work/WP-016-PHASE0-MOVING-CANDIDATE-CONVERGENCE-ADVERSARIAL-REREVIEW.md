# WP-016 — Phase 0 Moving-Candidate Convergence Adversarial Re-review

**Status:** active — fresh separate adversarial reviewer required
**Owner role:** adversarial reviewer
**Decision authority:** independently attack exact WP-014 material target `2f5508c1d6941e951d494bb2a700ef861860431d`, its bounded moving-candidate lifecycle and this WP's exact provisional activation; issue evidence-backed findings and an overall suitability judgement; no repair, candidate resolution/containment, attempt advancement, canonical result integration, ADR acceptance, PR #19/#1 merge, Phase acceptance or Phase 1 authority
**Development branch:** `phase0/development-os`
**Material target PR:** #19 — `WP-014: bound moving-candidate convergence without result suppression`
**Exact material target:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Repair package:** `WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md`
**Verification activity:** WP-015 — **PASS** for this exact target, activation `5368abd0f0c9a846f89120be44c19b1f1b1825d9` and binding `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`
**Verifier evidence:** PR #20, head `a1a0c07c2f16faa4c963bec6da7dad85baeb5565`, integrated evidence-only as `df9c9c12129bb8c55e4948fa095a90ab25b90811`
**Result-control key:** `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Provisional activation commit:** pending exact binding; fail closed until the next canonical binding commit records this activation SHA

## Objective

Freshly and separately attack the complete WP-014 repair target after WP-015
PASS. Try to break the bounded moving-candidate containment lifecycle,
current-valid-result non-suppression, conflict preservation, fail-closed
recovery, authority boundaries, timing controls and provisional activation path
rather than repeating the verifier checklist or inheriting producer/verifier
confidence.

A clean review is legitimate if the evidence supports it. No finding quota
exists. The review remains permanently bound to the exact material target,
material base, result-control key and provisional activation named above.

## Exact target and freshness

At start, before result publication and immediately before close:

1. inspect live PR #19 and confirm open/draft, base
   `phase0/development-os`, exact head `2f5508c...`, material base `dca520...` and
   exactly the nine declared files;
2. confirm PR #16 remains closed unmerged at exact head `adf067e...` and all
   historical WP-012/WP-013 bindings remain immutable;
3. inspect WP-015 PASS, SESSION-0026 and evidence-only merge `df9c9c1...`
   without converting PASS into acceptance;
4. inspect the exact activation commit recorded above and classify every later
   canonical change as activation/routing/session evidence or material;
5. if PR #19, the active result-control key or activation binding moves, stop
   and classify freshness rather than silently retargeting;
6. bind both reviewer records to the complete key, target, base and activation.

## Provisional WP-local activation bridge

After Integrator activation, this bridge is active only because canonical
`STATE.md` names WP-016. It is a Step-3/Step-4 execution precondition, not a
replacement or reordering of COLD_START Steps 1–2 and not acceptance or merge
of PR #19 governance.

It is a **provisional material rollout control**, not a transition-only relabel
and not part of the exact material target certified by WP-015. The reviewer must
inspect the exact activation/binding commits independently as part of this
review.

### First bridge check — before review-specific Step 3 work

After COLD_START Steps 1–2:

1. re-read the still-canonical complete key from this WP;
2. inspect open and merged/closed evidence PRs targeting
   `phase0/development-os` that claim WP-016; PR metadata is locator only;
3. apply only canonical exact-head resolutions or moving-candidate containment
   records produced by a separate Integrator and bound to exact repository/PR
   identity plus the complete active key;
4. validate every inspectable observed head directly against review artefact +
   handoff key, completed judgement and evidence/session-only scope;
5. one current match routes to Integrator; multiple current matches remain a
   conflict; a current-valid head can never be suppressed;
6. a first invalid head routes exact-head resolution; one invalid moved head
   after resolution routes once to movement containment; later
   inspectable-invalid or candidate-specifically inaccessible heads covered by
   canonical containment are recorded as contained and do not reset recovery;
7. uncontained invalid/uninspectable candidates and repository-wide discovery
   failure remain fail-closed; continue as reviewer only when no current result,
   conflict or uncontained blocker remains.

### Final bridge check — immediately before Step 4 role commitment

Repeat the complete live check above against current canonical state/key and
candidate heads. No planning, branch creation or substantive review action may
occur between this check and declaring/beginning the adversarial-review
responsibility. Any changed or unavailable input uses the new fail-closed route.

The bridge narrows but does not claim to eliminate publication after the final
check. That residual host edge remains explicit and uses later conflict
handling.

### Activation close condition

After publishing the dedicated WP-016 evidence PR, do not change `STATE.md`. A
generic fresh session must still encounter the published exact-key result and
route to a separate Integrator before duplicate review.

## Scope

Attack surfaces include, without imposing a finding quota:

- all surviving historical F-AR-001 through F-AR-005 failure classes against
  the changed target;
- first fixed invalid-head resolution, first invalid moved-head containment and
  later invalid generation convergence beyond the prior five-step trace;
- containment identity across repository, PR and all four active-key fields,
  including wrong-repository/key, local, forged and candidate-authored controls;
- later-current-valid non-suppression and multiple-current-result conflict;
- closed, force-pushed, reopened, deleted/head-inaccessible, repeatedly moved
  and later-corrected candidate lifecycles;
- repository-wide discovery failure versus candidate-specific contained
  inaccessibility;
- initial/final live-check timing, including publication during bootstrap and
  the residual post-final-check edge;
- the real WP-015 post-result/pre-Integrator interval and PR #20 lifecycle;
- the WP-016 provisional activation bridge, exact activation binding and
  generic post-publication routing;
- canonical `STATE.md` + active-WP authority versus subordinate
  PR/evidence/control/index records;
- transition-only classification abuse, freshness laundering, false completion
  and role/authority leakage;
- current WP-000 criteria and any additional material failure path introduced
  or exposed by the nine-file repair.

## Non-scope

- repairing any finding;
- creating or applying a candidate resolution or containment record;
- advancing the result-control attempt;
- changing or weakening WP-000 acceptance criteria;
- reinterpreting WP-015 PASS, WP-013 Requires repair or historical F-AR-001
  through F-AR-005 evidence;
- accepting or rejecting ADR-0000, ADR-0001 or ADR-0002;
- canonically integrating the reviewer's own result;
- merging PR #19, PR #16 or PR #1;
- accepting Phase 0 or beginning Phase 1.

## Required reading and independence order

Enter through canonical `development/03_plan/COLD_START.md`, complete Steps 1–2,
then execute the first activation-bridge check above.

### A. Establish the attack model before producer/verifier conclusions

Read and persist attack hypotheses before reading PR #19's ADR rationale,
producer evidence/model, builder handoff or WP-015 verifier conclusions:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. all four foundation files;
3. canonical `SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`,
   `REASONING_POLICY.md`, `ROLE_MODEL.md`, `DECISION_POLICY.md` and
   `CHANGE_POLICY.md`;
4. canonical `VERIFICATION_POLICY.md`, `COLD_START.md`, `PR_GATE.md` and
   `PHASE_GATE.md`;
5. `development/06_reviews/ADVERSARIAL_REVIEW_TEMPLATE.md`;
6. immutable WP-007/WP-010/WP-013 adversarial review artefacts preserving
   F-AR-001 through F-AR-005;
7. SESSION-0011, SESSION-0012, SESSION-0017, SESSION-0018, SESSION-0022 and
   SESSION-0023 lifecycle evidence;
8. live PR #10/#12/#14/#15/#17/#18 metadata, heads and evidence-only scopes;
9. this WP and the exact canonical activation/binding chain.

Persist attack hypotheses before continuing.

### B. Inspect producer and verifier material

10. active WP-014 and exact PR #19 diff/all nine files at `2f5508c...`;
11. proposed ADR-0002, both producer evidence records, executable model and
    result-control template;
12. SESSION-0024 builder handoff;
13. WP-015, exact verifier artefact, SESSION-0026 and PR #20 merge record;
14. exact canonical commits after material base, classified individually;
15. `CHATGPT_PROJECT_ENTRY.md`, `NEXT_SESSION.md` and subordinate
    `WORKSPACE_INDEX.md`.

Then execute the final activation-bridge check immediately before Step 4 role
commitment.

## Acceptance criteria

The reviewer must produce exact evidence and an overall judgement for each
applicable item:

1. PR #19 target/base/nine-file scope remain exact and fresh at start and close;
2. attack hypotheses are persisted before relying on producer/verifier
   conclusions;
3. F-AR-001 through F-AR-005 are actively replayed and mutated rather than
   assumed closed;
4. fixed invalid-head resolution and first moved-head containment converge
   without turning either control into evidence validity;
5. later invalid generations cannot reset recovery indefinitely after valid
   containment;
6. containment identity is exact, canonical-before-use and Integrator-only;
7. every inspectable later head is validated and a current-valid result can
   never be suppressed by containment;
8. multiple current results remain a preserved conflict with Integrator-only
   attempt advancement;
9. wrong-key/repository, local, forged or candidate-authored controls cannot
   unblock or accept anything;
10. closed/force-pushed/reopened/deleted/inaccessible/later-corrected candidate
    states preserve exact validity and bounded recovery;
11. repository-wide discovery failure remains fail closed and cannot be
    contained away;
12. publication between initial and final checks is detected before role
    commitment;
13. the residual post-final-check edge is accurately bounded and later recovery
    cannot launder false completion;
14. the real PR #20 close interval routes a generic session to Integrator
    without duplicate verification;
15. the WP-016 provisional bridge is canonically active at the exact recorded
    commit and protects its own reviewer close interval without accepting PR
    #19 governance;
16. `STATE.md` + active WP remain canonical; evidence/control/PR/index records
    remain subordinate;
17. producer/verifier/reviewer/Integrator/owner authority remains separated and
    no transition-only label hides material change;
18. WP-015 PASS remains exact and does not accept ADR-0002, PR #19/#1 or Phase
    0; immutable historical findings/results remain preserved;
19. producer and verifier evidence are inputs, not substitutes for adversarial
    disproof attempts;
20. findings or an explicit no-surviving-finding statement are published with
    limitations, exact target/base/key/activation and an overall suitability
    judgement; reviewer performs no prohibited repair, control, transition,
    acceptance or merge.

## Methods

- exact Git commit/blob and live PR metadata/scope inspection;
- independent attack model fixed before producer/verifier conclusions;
- adversarial mutation of candidate, key, scope, head, resolution, containment,
  outage and timing states;
- multi-generation, later-valid and multiple-current lifecycle replay;
- historical PR lifecycle replay, including PR #20;
- canonical activation-commit and role-authority inspection;
- semantic attack where deterministic evidence is insufficient.

## Outputs and publication

- uniquely named exact-target adversarial re-review artefact under
  `development/06_reviews/`;
- fresh reviewer handoff under `development/07_sessions/`;
- dedicated evidence PR targeting `phase0/development-os` containing exactly
  those two files and exposing the complete WP-016 key;
- no repair/control record/state transition/ADR change/acceptance/merge.

## Result routing

After publication, a separate Integrator validates/integrates the evidence and
transitions canonical state without reinterpretation.

- any surviving material finding -> smallest bounded authorised repair or
  resolution path; changed material requires a new exact target and fresh
  verification/re-review;
- no surviving material finding and a suitable-to-proceed judgement -> only
  the remaining ADR/human-owner/PR/Phase gates; the review itself accepts none;
- cannot assess -> smallest bounded investigation/repair path, followed by
  fresh exact-target checks.

## Completion state

Active — fresh separate adversarial reviewer required after exact activation
binding. No WP-016 review result exists for `2f5508c...`.

## Handoff

Exact next responsibility after the immediate canonical binding commit: fresh
separate adversarial reviewer executes attempt 1, publishes only the review
artefact + reviewer handoff PR, and stops for another separate Integrator.
