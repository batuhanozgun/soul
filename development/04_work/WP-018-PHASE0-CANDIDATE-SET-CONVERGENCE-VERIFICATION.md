# WP-018 — Phase 0 Candidate-Set Convergence Verification

**Status:** active — fresh separate verifier required
**Owner role:** verifier
**Decision authority:** independently issue PASS / FAIL / NOT VERIFIED for the
complete WP-017 material target and its exact provisional activation; no repair,
candidate resolution/containment, attempt advancement, canonical result
integration, adversarial re-review, ADR acceptance, PR #22/#1 merge, Phase
acceptance or Phase 1 authority
**Development branch:** `phase0/development-os`
**Material target PR:** #22 — `WP-017: bound candidate-set convergence and restore result precedence`
**Exact material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Repair package:** `WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md`
**Historical rejected target:** closed-unmerged PR #19 at
`2f5508c1d6941e951d494bb2a700ef861860431d`
**Result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Provisional activation commit:**
`fbe517bef10b5e820dc096a8a82e2c1a3047a38c`

## Objective

Freshly and independently verify the complete WP-017 material target against
all current WP-000 acceptance criteria and F-AR-001 through F-AR-007. Explicitly
verify bounded convergence across fresh PR identities, normative
current-valid-result precedence in every mixed state, exact candidate-set
control identity/authority and the WP-local activation bridge protecting this
verification's own result interval.

The verifier must derive expectations before reading builder rationale,
producer evidence/model or builder handoff. WP-015 **PASS** and WP-016
**Requires repair** remain permanently bound only to `2f5508c...` and cannot
certify the changed target.

## Exact target and freshness

At start, before result publication and immediately before close:

1. inspect live PR #22 and confirm open/draft, base
   `phase0/development-os`, exact head `5bd0db2...`, material base `4524f21...`
   and exactly the ten declared files;
2. confirm PR #19 is closed unmerged at exact head `2f5508c...` and recorded as
   superseded without mutation of its historical target/result bindings;
3. inspect WP-016 evidence PR #21 exact two-file scope and evidence merge
   `276132a8...` without converting evidence integration into acceptance;
4. inspect the canonical activation commit recorded above and classify every
   later canonical change as activation/routing/session evidence or material;
5. if PR #22, the active key or activation binding moves, stop and classify
   freshness rather than silently retargeting;
6. bind both verifier records to the complete key, target, base and activation.

## Provisional WP-local activation bridge

After Integrator activation, this bridge is active only because canonical
`STATE.md` names WP-018. It is a Step-3/Step-4 execution precondition, not a
replacement/reordering of COLD_START Steps 1–2 and not acceptance/merge of PR
#22 governance.

### First bridge check — before verification-specific Step 3 work

After COLD_START Steps 1–2:

1. re-read the still-canonical complete key from this WP;
2. inspect open and merged/closed evidence PRs targeting
   `phase0/development-os` that claim WP-018; PR metadata is locator only;
3. apply only canonical exact-head resolution, moving-candidate containment or
   candidate-set containment records produced by a separate Integrator and
   bound to the required repository/PR/head plus complete active key identities;
4. validate every inspectable observed head directly against result artefact +
   handoff key, completed result and evidence/session-only scope before routing
   any invalid residue;
5. exactly one current match routes to Integrator regardless of invalid residue;
   multiple current matches remain conflict and no control suppresses either;
6. with no current match, a first invalid head routes exact-head resolution; a
   later invalid moved head on the same PR routes once to stream containment; a
   directly inspected invalid candidate at a fresh PR identity after an earlier
   canonical invalid-candidate control routes once to candidate-set containment;
7. later inspectable-invalid or candidate-specifically inaccessible candidates
   covered by the exact applicable containment are recorded as contained
   non-valid and cannot reset recovery;
8. uncontained invalid/uninspectable candidates and repository-wide discovery
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

After publishing the dedicated WP-018 evidence PR, do not change `STATE.md`. A
generic fresh session must still encounter the published exact-key result and
route to a separate Integrator before duplicate verification.

## Scope

- all twelve current WP-000 criteria;
- exact PR #22 target/base/ten-file scope and PR #19 supersession relation;
- immutable WP-015 PASS, WP-016 Requires repair and F-AR-001 through F-AR-007;
- exact-head, PR-stream and repository/key candidate-set control
  trigger/identity/effect;
- long fresh-PR identity rotation after candidate-set containment;
- valid + first invalid, valid + moved invalid, valid + multiple fresh invalid,
  valid + inaccessible invalid and multiple-valid + invalid precedence;
- later-current-valid non-suppression and multiple-result conflict preservation;
- wrong repository/key, local, forged, candidate-authored and unproven controls,
  changed attempt and canonical-before-use;
- fixed, moved, force-pushed, closed, inaccessible/deleted and later-corrected
  candidate lifecycles across same and fresh PR identities;
- global discovery failure versus candidate-specific contained inaccessibility;
- initial/final timing checks and provisional activation;
- proposed ADR-0002 status, role separation and all remaining gates.

## Non-scope

- repairing the target or changing acceptance criteria;
- creating/applying any live resolution or containment record;
- advancing the result-control attempt;
- integrating the verifier's own result or performing adversarial re-review;
- accepting/rejecting ADR-0000/0001/0002;
- merging PR #22, PR #19 or PR #1;
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
6. active WP-017 and this WP;
7. immutable WP-007/WP-010/WP-013/WP-016 adversarial review artefacts
   preserving F-AR-001 through F-AR-007;
8. WP-015 verifier artefact, SESSION-0026, WP-016 review, SESSION-0028 and
   SESSION-0029 Integrator handoff;
9. live PR #19/#21/#22 metadata, exact heads, states and scopes;
10. derived launch/index files only as subordinate views.

Persist the expected criterion/result matrix before continuing.

### B. Inspect producer material afterward

11. exact PR #22 diff and all ten files at `5bd0db2...`;
12. target ADR-0002, all three producer evidence records, executable model and
    result-control template;
13. SESSION-0030 builder handoff only after expectations are fixed;
14. exact canonical provisional activation and binding commits;
15. independently authored mutations and repository checks; do not import the
    producer model as the verifier decision function.

Then execute the final bridge check immediately before Step 4 role commitment.

## Acceptance criteria

Issue PASS / FAIL / NOT VERIFIED for each item with exact evidence:

1. all current WP-000 criteria pass at the exact changed target;
2. PR #22 head/base/ten-file scope remain exact and fresh;
3. PR #19 is superseded closed-unmerged without mutating historical bindings;
4. immutable WP-015/WP-016 results and F-AR-001 through F-AR-007 are preserved;
5. a first fixed invalid head requires exact-head resolution and then unblocks;
6. same-PR invalid movement converges after one stream-containment escalation;
7. a second invalid PR identity after an earlier canonical control requires one
   candidate-set containment escalation;
8. a long later sequence of fresh invalid PR identities requires no further
   canonical controls after valid candidate-set containment;
9. candidate-set identity binds exact canonical repository + all four active-key
   fields and is canonical-before-use/Integrator-only;
10. every inspectable head remains directly validated under containment;
11. exactly one current-valid result always routes before first/moved/multiple/
    inaccessible invalid residue;
12. multiple current-valid results remain explicit conflict despite invalid
    residue or containment;
13. wrong-key/repository, local, forged, candidate-authored or unproven controls
    cannot unblock, suppress or accept anything;
14. a canonical key change ends prior candidate-set containment scope;
15. closed/force-pushed/deleted/inaccessible/reopened states follow the
    documented lifecycle without becoming validity claims or reset primitives;
16. repository-wide discovery and uncontained candidate inspection failure
    remain fail-closed;
17. F-AR-001 through F-AR-005 discovery, fixed recovery, activation, timing and
    same-PR movement properties remain intact;
18. the producer model matches normative precedence, can fail red under the
    deliberate invalid-first mutation and is not reused as independent proof;
19. `STATE.md` + active WP remain canonical; PR/evidence/control records remain
    subordinate;
20. verifier/reviewer/Integrator/owner authority remains separate;
21. provisional activation is exact and protects WP-018 close without accepting
    general governance;
22. ADR-0002 remains proposed and every ADR/PR/human/Phase gate stays separate;
23. verifier performs no repair, resolution/containment, attempt advancement,
    result integration, re-review, acceptance or merge.

Overall PASS requires every current WP-000 criterion and every applicable item
above to PASS.

## Methods

- exact Git commit/blob and live PR metadata/scope inspection;
- independently derived decision model/mutations, including red cases;
- multi-generation, multi-PR and later-valid lifecycle replay;
- canonical activation, repository identity and authority comparison;
- semantic review where deterministic evidence is insufficient.

## Outputs and publication

- uniquely named exact-target verification artefact under `development/06_reviews/`;
- fresh verifier handoff under `development/07_sessions/`;
- dedicated evidence PR targeting `phase0/development-os` containing exactly
  those two files and exposing the complete WP-018 key;
- no repair/control record/state transition/acceptance/merge.

## Result routing

After publication, a separate Integrator validates/integrates the evidence and
transitions canonical state without reinterpretation.

- PASS -> fresh separate adversarial re-review of the same exact target;
- FAIL -> smallest bounded separate repair and a new exact target;
- NOT VERIFIED -> smallest bounded investigation/repair, then fresh verification.

## Completion state

Active — fresh separate verifier required after exact activation binding. No
verification result exists for `5bd0db2...`.

## Handoff

Exact next responsibility after the immediate canonical binding commit: fresh
separate verifier executes attempt 1, publishes only verification artefact +
handoff PR, and stops for another separate Integrator.
