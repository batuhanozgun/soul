# WP-021 — Phase 0 Uncontained Inspection Fail-Closed Verification

**Status:** proposed — awaiting fresh separate Integrator activation
**Owner role:** verifier
**Decision authority:** independently issue PASS / FAIL / NOT VERIFIED for the
complete WP-020 material target and its exact provisional activation; no repair,
candidate resolution/containment, attempt advancement, canonical result
integration, adversarial re-review, ADR acceptance, PR #26/#1 merge, Phase
acceptance or Phase 1 authority
**Development branch:** `phase0/development-os`
**Material target PR:** #26 — `WP-020: fail closed on uncontained inspection unknowns`
**Exact material target:** `a42101cfc7fef58ac169150458ff3f889f10527b`
**Material base:** `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Repair package:** `WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`
**Historical rejected target:** closed-unmerged PR #22 at
`5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Result-control key:** `WP-021 / verifier / a42101cfc7fef58ac169150458ff3f889f10527b / attempt 1`
**Provisional activation commit:** not yet assigned; a fresh separate Integrator
must activate and bind this WP canonically before verifier execution

## Objective

Freshly and independently verify the complete WP-020 material target against
all current WP-000 acceptance criteria and F-AR-001 through F-AR-008. Explicitly
verify that uncontained uninspectable same-scope candidates remain epistemically
unknown and fail closed in every mixed state, without weakening current-valid
precedence over directly proven invalid or validly resolved/contained non-valid
residue.

The verifier must derive expectations before reading builder rationale,
producer evidence/model or builder handoff. WP-018 **PASS** and WP-019
**Requires repair** remain permanently bound only to `5bd0db27...` and cannot
certify the changed target.

## Exact target and freshness

At start, before result publication and immediately before close:

1. inspect live PR #26 and confirm open/draft, base
   `phase0/development-os`, exact head `a42101c...`, material base `c4ebef9...`
   and exactly the eleven declared files;
2. confirm PR #22 is closed unmerged at exact head `5bd0db27...`, base
   `4524f21...`, with ten files and immutable WP-018/WP-019 bindings;
3. inspect WP-019 evidence PR #25 exact two-file scope and evidence merge
   `8022ca6f...` without converting evidence integration into acceptance;
4. inspect the canonical activation and binding commits recorded above and
   classify every later canonical change as activation/routing/session evidence
   or material;
5. if PR #26, the active key or activation binding moves, stop and classify
   freshness rather than silently retargeting;
6. bind both verifier records to the complete key, target, base and activation.

## Provisional WP-local activation bridge

After Integrator activation, this bridge is active only because canonical
`STATE.md` names WP-021. It is a Step-3/Step-4 execution precondition, not a
replacement/reordering of COLD_START Steps 1–2 and not acceptance/merge of PR
#26 governance.

It is a **provisional material rollout control**, not a transition-only relabel
and not part of the exact material target. The verifier must inspect the exact
activation/binding commits independently.

### First bridge check — before verification-specific Step 3 work

After COLD_START Steps 1–2:

1. re-read the still-canonical complete key from this WP;
2. inspect open and merged/closed evidence PRs targeting
   `phase0/development-os` that claim WP-021; PR metadata is locator only;
3. apply only canonical exact-head resolution, moving-candidate containment or
   candidate-set containment records produced by a separate Integrator and
   bound to the exact repository/PR/head plus complete active-key identities;
4. validate every inspectable observed head directly against result artefact +
   handoff key, completed result and evidence/session-only scope, then classify
   current-valid, directly inspected invalid, exactly resolved/contained
   non-valid and uncontained uninspectable candidates separately;
5. repository-wide discovery failure or any uncontained uninspectable
   same-scope candidate blocks before result/conflict routing, even when one or
   more current-valid results are visible;
6. if no unknown remains, multiple current-valid candidates remain conflict and
   exactly one current-valid candidate routes to Integrator before directly
   proven invalid or resolved/contained non-valid residue;
7. with no current result, a first directly inspected invalid head routes
   exact-head resolution; a later invalid moved head on the same PR routes once
   to stream containment; a directly inspected invalid candidate at a fresh PR
   identity after an earlier canonical invalid-candidate control routes once to
   candidate-set containment;
8. later inspectable-invalid or candidate-specifically inaccessible candidates
   covered by an exactly applicable canonical control are recorded as non-valid
   residue and cannot reset recovery; later inspectability always reopens direct
   validation. Continue as verifier only when no result, conflict or uncontained
   blocker remains.

### Final bridge check — immediately before Step 4 role commitment

Repeat the complete live check above against current canonical state/key and
candidate heads. No planning, branch creation or substantive verification
action may occur between this check and declaring/beginning the verifier
responsibility. Any changed or unavailable input uses the fail-closed route.

The bridge narrows but does not claim to eliminate publication after the final
check. That residual host edge remains explicit and uses later conflict handling.

### Activation close condition

After publishing the dedicated WP-021 evidence PR, do not change `STATE.md`. A
generic fresh session must still encounter the published exact-key result and
route to a separate Integrator before duplicate verification.

## Scope

- all twelve current WP-000 criteria;
- exact PR #26 target/base/eleven-file scope and PR #22 supersession relation;
- immutable WP-018 PASS, WP-019 **Requires repair** and F-AR-001 through
  F-AR-008;
- full-set epistemic classification before result routing;
- visible-valid + uncontained unknown, unknown alone, direct-invalid + unknown,
  multiple-visible-valid + unknown and contained-non-valid + unknown;
- current-looking locator metadata with inaccessible required records;
- later-inspectable valid/invalid outcomes and multiple-current conflict;
- exact-head resolved, stream-contained and candidate-set-contained
  inaccessible residue versus wrong-head/key/repository/authority controls;
- fixed-head, same-PR and cross-PR candidate convergence plus later-valid
  non-suppression;
- repository-wide discovery outage versus candidate-specific contained
  inaccessibility;
- exact repository/key/head freshness, canonical-before-use and Integrator-only
  control authority;
- initial/final timing checks and provisional activation;
- proposed ADR-0002 status, role separation and all remaining gates.

## Non-scope

- repairing the target or changing acceptance criteria;
- creating/applying any live resolution or containment record;
- advancing the result-control attempt;
- integrating the verifier's own result or performing adversarial re-review;
- accepting/rejecting ADR-0000/0001/0002;
- merging PR #26, PR #22 or PR #1;
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
6. active WP-020 and this WP;
7. immutable WP-007/WP-010/WP-013/WP-016/WP-019 adversarial review artefacts
   preserving F-AR-001 through F-AR-008;
8. WP-018 verifier artefact, SESSION-0032, WP-019 review, SESSION-0034 and
   SESSION-0035 Integrator handoff;
9. live PR #22/#25/#26 metadata, exact heads, states and scopes;
10. derived launch/index files only as subordinate views.

Persist the expected criterion/result matrix before continuing.

### B. Inspect producer material afterward

11. exact PR #26 diff and all eleven files at `a42101c...`;
12. target ADR-0002, all four producer evidence records, executable model and
    result-control template;
13. SESSION-0036 builder handoff only after expectations are fixed;
14. exact canonical provisional activation and binding commits;
15. independently authored oracle/mutations and repository checks; do not
    import the producer model as the verifier decision function.

Then execute the final activation-bridge check immediately before Step 4 role
commitment.

## Acceptance criteria

Issue PASS / FAIL / NOT VERIFIED for each item with exact evidence:

1. all current WP-000 criteria pass at the exact changed target;
2. PR #26 head/base/eleven-file scope remain exact and fresh;
3. PR #22 is superseded closed-unmerged without mutating historical bindings;
4. immutable WP-018/WP-019 results and F-AR-001 through F-AR-008 are preserved;
5. directly proven invalid, validly resolved/contained non-valid and uncontained
   uninspectable candidates are mechanically distinct;
6. visible-valid plus any uncontained uninspectable same-scope candidate blocks;
7. locator metadata, prior invalidity at another head and a visible result cannot
   convert an inaccessible candidate into invalid/non-valid residue;
8. with no unknown, exactly one current-valid result routes before directly
   inspected invalid or exactly resolved/contained non-valid residue;
9. multiple current-valid results remain explicit conflict, including when a
   formerly unknown candidate becomes inspectable-valid;
10. a formerly unknown inspectable-invalid candidate preserves sole-result
    routing rather than creating a false conflict;
11. every inspectable head is directly validated under either containment mode;
12. exact-head resolution covers later inaccessibility only for the same
    immutable head after proven invalidity; wrong-head/key/unproven records fail;
13. valid stream/set containment permits candidate-specific inaccessible
    non-valid residue without suppressing later validity;
14. fixed-head, same-PR and cross-PR convergence remain bounded under one exact
    repository/key and a long fresh-identity sequence needs no new controls;
15. wrong-key/repository, local, forged, candidate-authored or unproven controls
    cannot unblock, suppress or accept anything;
16. any canonical key/repository boundary change ends prior control scope;
17. repository-wide discovery failure remains fail-closed regardless of any
    visible result or candidate containment;
18. the producer model passes all 84 declared routes, both deliberate mutations
    fail red at the claimed causal boundaries, and neither is reused as
    independent proof;
19. normative text, executable model, template and current F-AR-008 evidence use
    the same state classes and route ordering;
20. `STATE.md` + active WP remain canonical; PR/evidence/control records remain
    subordinate;
21. verifier/reviewer/Integrator/owner authority remains separate;
22. provisional activation is exact and protects WP-021 close without accepting
    general governance;
23. ADR-0002 remains proposed and every ADR/PR/human/Phase gate stays separate;
24. verifier performs no repair, control, attempt advancement, result
    integration, re-review, acceptance or merge.

Overall PASS requires every current WP-000 criterion and every applicable item
above to PASS.

## Methods

- exact Git commit/blob and live PR metadata/scope inspection;
- independently derived decision oracle and mutations, including red cases;
- mixed visible/unknown, later-valid/invalid and multiple-current replay;
- fixed-head, multi-generation and multi-PR lifecycle replay;
- canonical activation, repository identity and authority comparison;
- semantic review where deterministic evidence is insufficient.

## Outputs and publication

- uniquely named exact-target verification artefact under `development/06_reviews/`;
- fresh verifier handoff under `development/07_sessions/`;
- dedicated evidence PR targeting `phase0/development-os` containing exactly
  those two files and exposing the complete WP-021 key;
- no repair/control record/state transition/acceptance/merge.

## Result routing

After publication, a separate Integrator validates/integrates the evidence and
transitions canonical state without reinterpretation.

- PASS -> fresh separate adversarial re-review of the same exact target;
- FAIL -> smallest bounded separate repair and a new exact target;
- NOT VERIFIED -> smallest bounded investigation/repair, then fresh verification.

## Completion state

Proposed — awaiting separate Integrator validation, canonical activation and
exact activation binding. No verification result exists for `a42101c...`.

## Handoff

Exact next responsibility before verification: fresh separate Integrator to
validate/integrate the builder-close routing records and canonically activate
this WP with an exact binding. Only then does a fresh separate verifier execute
attempt 1, publish only verification artefact + handoff PR, and stop for another
separate Integrator.
