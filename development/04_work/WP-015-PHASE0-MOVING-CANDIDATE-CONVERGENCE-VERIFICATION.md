# WP-015 — Phase 0 Moving-Candidate Convergence Verification

**Status:** proposed — awaiting fresh separate Integrator activation
**Owner role:** verifier
**Decision authority:** independently issue PASS / FAIL / NOT VERIFIED for the
complete WP-014 material target and its exact provisional activation; no repair,
candidate resolution/containment, attempt advancement, canonical result
integration, adversarial re-review, ADR acceptance, PR #19/#1 merge, Phase
acceptance or Phase 1 authority
**Development branch:** `phase0/development-os`
**Material target PR:** #19 — `WP-014: bound moving-candidate convergence without result suppression`
**Exact material target:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Repair package:** `WP-014-PHASE0-MOVING-CANDIDATE-CONVERGENCE-REPAIR.md`
**Historical rejected target:** closed-unmerged PR #16 at
`adf067e4289e4c0b51cf40c1940193e8252b22e0`
**Result-control key:** `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Provisional activation commit:** not yet assigned; a fresh separate Integrator
must activate and bind this WP canonically before verifier execution

## Objective

Freshly and independently verify the complete WP-014 material target against all
current WP-000 acceptance criteria and F-AR-001 through F-AR-005, including the
bounded moving-candidate containment lifecycle and the WP-local activation bridge
protecting this verification's own result interval.

The verifier must derive expectations before reading the builder rationale,
producer evidence/model or builder handoff. WP-012 **PASS** and WP-013
**Requires repair** remain permanently bound only to `adf067e...` and cannot
certify the changed target.

## Exact target and freshness

At start, before result publication and immediately before close:

1. inspect live PR #19 and confirm open/draft, base
   `phase0/development-os`, exact head `2f5508c...`, material base `dca520...` and
   exactly the nine declared files;
2. confirm PR #16 is closed unmerged at exact head `adf067e...` and recorded as
   superseded without mutation of its historical target/result bindings;
3. inspect the canonical activation commit recorded above and classify every
   later canonical change as activation/routing/session evidence or material;
4. if PR #19, the active key or activation binding moves, stop and classify
   freshness rather than silently retargeting;
5. bind both verifier records to the complete key, target, base and activation.

## Provisional WP-local activation bridge

After Integrator activation, this bridge is active only because canonical
`STATE.md` names WP-015. It is a
Step-3/Step-4 execution precondition, not a replacement/reordering of COLD_START
Steps 1–2 and not acceptance/merge of PR #19 governance.

### First bridge check — before verification-specific Step 3 work

After COLD_START Steps 1–2:

1. re-read the still-canonical complete key from this WP;
2. inspect open and merged/closed evidence PRs targeting
   `phase0/development-os` that claim WP-015; PR metadata is locator only;
3. apply only canonical exact-head resolutions or moving-candidate containment
   records produced by a separate Integrator and bound to exact repository/PR
   identity plus the complete active key;
4. validate every inspectable observed head directly against result artefact +
   handoff key, completed result and evidence/session-only scope;
5. one current match routes to Integrator; multiple current matches remain a
   conflict; a current-valid head can never be suppressed;
6. a first invalid head routes exact-head resolution; one invalid moved head
   after resolution routes once to movement containment; later
   inspectable-invalid or candidate-specifically inaccessible heads covered by
   canonical containment are recorded as contained and do not reset recovery;
7. uncontained invalid/uninspectable candidates and repository-wide discovery
   failure remain fail-closed; continue as verifier only when no current result,
   conflict or uncontained blocker remains.

### Final bridge check — immediately before Step 4 role commitment

Repeat the complete live check above against current canonical state/key and
candidate heads. No planning, branch creation or substantive verification action
may occur between this check and declaring/beginning the verifier responsibility.
Any changed or unavailable input uses the new fail-closed route.

The bridge narrows but does not claim to eliminate publication after the final
check. That residual host edge remains explicit and uses later conflict handling.

### Activation close condition

After publishing the dedicated WP-015 evidence PR, do not change `STATE.md`. A
generic fresh session must still encounter the published exact-key result and
route to a separate Integrator before duplicate verification.

## Scope

- all twelve current WP-000 criteria;
- exact PR #19 target/base/nine-file scope and PR #16 supersession relation;
- immutable WP-012 PASS, WP-013 Requires repair and F-AR-001 through F-AR-005;
- exact-head resolution plus bounded stream-containment trigger/identity/effect;
- later-current-valid non-suppression and multiple-result conflict preservation;
- wrong repository/key controls, changed attempt and canonical-before-use;
- fixed, moved, force-pushed, closed, inaccessible/deleted and later-corrected
  candidate lifecycles;
- global discovery failure versus candidate-specific contained inaccessibility;
- initial/final timing checks and provisional activation;
- proposed ADR-0002 status, role separation and all remaining gates.

## Non-scope

- repairing the target or changing acceptance criteria;
- creating/applying a resolution or containment record;
- advancing the result-control attempt;
- integrating the verifier's own result or performing adversarial re-review;
- accepting/rejecting ADR-0000/0001/0002;
- merging PR #19, PR #16 or PR #1;
- accepting Phase 0 or beginning Phase 1.

## Required reading and independence order

Enter through canonical `development/03_plan/COLD_START.md`, complete Steps 1–2,
then execute the first activation-bridge check above.

### A. Derive and persist expected checks first

1. canonical `development/01_governance/VERIFICATION_POLICY.md`;
2. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
3. all four foundation files;
4. canonical `SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, `REASONING_POLICY.md`,
   `ROLE_MODEL.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`;
5. canonical `COLD_START.md`, `PR_GATE.md` and `PHASE_GATE.md`;
6. active WP-014 and this WP;
7. immutable WP-007/WP-010/WP-013 adversarial review artefacts preserving
   F-AR-001 through F-AR-005;
8. WP-012 verifier artefact, SESSION-0020, WP-013 review, SESSION-0022 and
   SESSION-0023 Integrator handoff;
9. live PR #16/#18/#19 metadata, exact heads and scopes;
10. derived launch/index files only as subordinate views.

Persist the expected criterion/result matrix before continuing.

### B. Inspect producer material afterward

11. exact PR #19 diff and all nine files at `2f5508c...`;
12. target ADR-0002, both producer evidence records, executable model and
    result-control template;
13. WP-014 builder handoff only after expectations are fixed;
14. exact canonical provisional activation and binding commits;
15. independently authored mutations and repository checks; do not import the
    producer model as the verifier decision function.

Then execute the final bridge check immediately before Step 4 role commitment.

## Acceptance criteria

Issue PASS / FAIL / NOT VERIFIED for each item with exact evidence:

1. all current WP-000 criteria pass at the exact changed target;
2. PR #19 head/base/nine-file scope remain exact and fresh;
3. PR #16 is superseded closed-unmerged without mutating historical bindings;
4. immutable WP-012/WP-013 results and F-AR-001 through F-AR-005 are preserved;
5. a first fixed invalid head requires exact-head resolution and then unblocks;
6. the first invalid moved generation requires one containment escalation;
7. invalid generations beyond the reviewer five-step trace do not require more
   canonical resolutions after valid containment;
8. containment identity binds repository + PR + all four active-key fields and
   is canonical-before-use/Integrator-only;
9. a later current-valid head on the same contained PR always routes to
   Integrator and cannot be suppressed;
10. multiple current-valid results remain an explicit conflict;
11. wrong-key/repository, local, forged or candidate-authored controls cannot
    unblock or accept anything;
12. closed/force-pushed/deleted/inaccessible/reopened candidate states follow the
    documented lifecycle without becoming validity claims or reset primitives;
13. repository-wide discovery failure remains fail-closed;
14. F-AR-001 through F-AR-004 result discovery, fixed recovery, activation and
    final-check timing properties remain intact;
15. the producer model can fail red and is not reused as independent proof;
16. `STATE.md` + active WP remain canonical; PR/evidence/control records remain
    subordinate;
17. verifier/reviewer/Integrator/owner authority remains separate;
18. provisional activation is exact and protects WP-015 close without accepting
    general governance;
19. ADR-0002 remains proposed and every ADR/PR/human/Phase gate stays separate;
20. verifier performs no repair, resolution/containment, attempt advancement,
    result integration, re-review, acceptance or merge.

Overall PASS requires every current WP-000 criterion and every applicable item
above to PASS.

## Methods

- exact Git commit/blob and live PR metadata/scope inspection;
- independent decision model/mutations, including red cases;
- multi-generation and later-valid lifecycle replay;
- canonical activation and authority comparison;
- semantic review where deterministic evidence is insufficient.

## Outputs and publication

- uniquely named exact-target verification artefact under `development/06_reviews/`;
- fresh verifier handoff under `development/07_sessions/`;
- dedicated evidence PR targeting `phase0/development-os` containing exactly
  those two files and exposing the complete WP-015 key;
- no repair/control record/state transition/acceptance/merge.

## Result routing

After publication, a separate Integrator validates/integrates the evidence and
transitions canonical state without reinterpretation.

- PASS -> fresh separate adversarial re-review of the same exact target;
- FAIL -> smallest bounded separate repair and a new exact target;
- NOT VERIFIED -> smallest bounded investigation/repair, then fresh verification.

## Completion state

Proposed — awaiting separate Integrator validation, canonical activation and
exact activation binding. No verification result exists for `2f5508c...`.

## Handoff

Exact next responsibility before verification: fresh separate Integrator to
validate/integrate the builder-close routing records and canonically activate
this WP with an exact binding. Only then does a fresh separate verifier execute
attempt 1, publish only verification artefact + handoff PR, and stop for another
separate Integrator.
