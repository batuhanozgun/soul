# ADVERSARIAL RE-REVIEW — WP-000 / CANDIDATE-SET CONVERGENCE REPAIR

**Reviewer session:** SESSION-0034
**Reviewed commit/artefact:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Material target PR:** #22 — `WP-017: bound candidate-set convergence and restore result precedence`
**Authoritative specification:** `development/04_work/WP-000-DEVELOPMENT-OS.md`; `development/04_work/WP-019-PHASE0-CANDIDATE-SET-CONVERGENCE-ADVERSARIAL-REREVIEW.md`
**Result-control key:** `WP-019 / adversarial reviewer / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Provisional activation commit:** `3b91acf02df2852c43404ec164725ac5748b9bad`
**Activation-binding commit:** `fa6f208e6133f746a69a4a51faff3f2485798d24`
**Canonical state inspected through:** `39a91e9a4d11f10ce720458686f33c98a87d20a4`
**Reviewer output branch:** `codex/wp019-adversarial-rereview`
**Reviewer evidence PR:** #25 — initial published head `6b328cdeb127f56b163b999eaa8621fd6d5ead19`, base `39a91e9a4d11f10ce720458686f33c98a87d20a4`
**Date:** 2026-08-28

## Pre-evidence attack model

This attack model was persisted after canonical COLD_START Steps 1–2, the first
live WP-019 bridge check and WP-019 Step 3A. It precedes inspection of WP-017's
repair rationale, the exact ten-file target as a preferred solution, proposed
ADR-0002 rationale, producer evidence/model, SESSION-0030 builder conclusions,
WP-018 verifier conclusions and SESSION-0033's claims as evidence of
suitability. Routing facts necessarily exposed by canonical `STATE.md`, the
active WP and the mandatory bridge/activation-chain inspection are not treated
as proof that the material control works.

### First bridge-check observation

- a fresh isolated clone of live `origin/phase0/development-os` resolved to
  `39a91e9a4d11f10ce720458686f33c98a87d20a4`;
- the active complete key remained
  `WP-019 / adversarial reviewer / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`;
- the exact activation/binding chain was `3b91acf...` then `fa6f208...`; later
  canonical `39a91e9...` added only SESSION-0033 plus one subordinate index row;
- repository-wide live all-state PR discovery against
  `phase0/development-os` succeeded and found no PR metadata/body claiming
  WP-019;
- therefore no current result, multiple-result conflict, uncontained invalid or
  uninspectable candidate, repository-wide discovery outage, or applicable
  canonical WP-019 candidate control blocked Step 3 preparation.

This observation is not the required final bridge check and is not evidence
that the reviewed material survives the attacks below.

### Attack surfaces and hypotheses to test

1. **F-AR-001 replay — result discoverability:** a completed exact-key result
   may be omitted by search, pagination, metadata mutation or lifecycle state,
   allowing duplicate independent work during a real post-result interval.
2. **F-AR-002 replay — self-hosting activation:** the WP-019 bridge may depend
   circularly on unmerged PR #22 governance, admit work in its unbound
   intermediate state, or be misrepresented as verification/acceptance.
3. **F-AR-003 replay — fixed invalid residue:** an exact-head resolution may
   fail to converge for a fixed invalid, stale, malformed, closed or
   uninspectable candidate.
4. **F-AR-004 replay — timing:** publication between initial and final checks
   may escape detection, or a post-final publication may be laundered into
   unique completion rather than later result/conflict handling.
5. **F-AR-005 replay — same-PR movement:** repeated force-pushes or corrected,
   invalid and inaccessible heads may keep resetting exact-head resolution
   despite stream containment.
6. **F-AR-006 replay — fresh-identity rotation:** candidate-set containment may
   still be scoped to known PRs or past controls, letting a long sequence of
   new same-key PR identities reset recovery.
7. **F-AR-007 replay — precedence:** normative text, executable model or any
   consumer route may still handle invalid residue before exactly one current
   valid result.
8. **Repository identity aliasing:** repository name, URL, owner rename, case,
   fork/source identity or local remote may match a candidate-set control
   without the immutable canonical repository identity required by policy.
9. **Partial-key containment:** equality on target or WP while omitting role,
   attempt or another key field may leak a control across roles/attempts and
   suppress a legitimate result.
10. **Active-key rotation:** changing any one of WP, role, target or attempt may
    fail to terminate the prior candidate-set containment scope.
11. **Candidate-authored control:** PR title/body, evidence files, handoffs,
    local commits or candidate branches may masquerade as canonical Integrator
    resolution/stream/candidate-set containment.
12. **Canonical-before-use race:** a correctly shaped but unmerged control may
    be consumed before reaching the authoritative branch, or an old canonical
    control may survive after its repository/key identity changes.
13. **Control-authority provenance gap:** commit content or authorship may be
    insufficient to establish that a separate authorised Integrator produced a
    candidate-set control, allowing self-issued suppression.
14. **Conflicting controls:** multiple canonical resolution or containment
    records with incompatible repository, key, PR, head or invalidity claims
    may be arbitrarily selected rather than fail closed.
15. **Containment becomes validity:** a contained candidate may stop receiving
    direct validation, turning a progress control into evidence validity,
    absence, acceptance or a permanent ignore rule.
16. **Later-valid suppression:** a fixed, stream-contained or candidate-set-
    contained identity may later publish a fully current result but remain
    suppressed by containment history.
17. **Corrected first moved head:** a candidate fixed immediately after an
    exact-head resolution may be stream-contained before its new head is
    directly validated.
18. **Valid plus first invalid:** one current result plus a fresh invalid
    candidate may still route resolution instead of Integrator result.
19. **Valid plus moved/contained invalid:** one current result plus moved,
    stream-contained or candidate-set-contained residue may be delayed or
    treated as clean without preserving the residue's explicit non-valid state.
20. **Valid plus inaccessible residue:** a candidate-specific inaccessible
    head may either suppress the valid result indefinitely or be treated as
    invalid without sufficient prior direct proof.
21. **Multiple-current conflict:** two current results may be selected by
    recency, PR number, open/closed state or containment history, especially
    when invalid residue coexists.
22. **Alternating lifecycle:** invalid -> valid -> inaccessible -> valid
    transitions may exploit stale observation or containment to create false
    absence, false conflict or false completion.
23. **Closed/reopened/deleted lifecycle:** closure, reopen, merge, source-branch
    deletion and pull-ref persistence may alter the inspected head or silently
    change whether a control applies.
24. **Force-push observation race:** API head, pull ref and fetched commit may
    disagree across a mutation, permitting validation of one head and routing
    another.
25. **Inaccessible-before-proof:** candidate-set containment may cover a fresh
    inaccessible identity whose repository/key relation or invalidity was never
    directly established.
26. **Candidate outage vs repository outage:** a repository-wide discovery/API
    failure may be misclassified as contained candidate-specific
    inaccessibility, or one deleted candidate may unnecessarily block the whole
    repository.
27. **Pagination and search omission:** older, closed, renamed, metadata-free or
    later-page same-key candidates may be silently omitted while discovery is
    still called successful.
28. **Hidden valid result:** a PR with exact artefact/handoff key but missing or
    altered locator metadata may be invisible to the discovery query, so
    metadata being "locator only" does not guarantee locator completeness.
29. **Hidden invalid/acceptance claim:** renamed paths, case changes, extra
    commits, deletions or non-obvious files may evade evidence/session-only
    scope validation or smuggle repair/state/acceptance into a result PR.
30. **Judgement ambiguity:** a complete key and two-file shape may be accepted
    without an explicit completed judgement, finding/no-finding statement and
    consistent handoff.
31. **Candidate-set threshold ambiguity:** the preconditions for escalating
    from exact-head to stream to candidate-set containment may be satisfied by
    unrelated invalid candidates, historical controls or observations from a
    different key/repository.
32. **Fresh-identity convergence bound:** after valid candidate-set containment,
    20, 100 or arbitrarily many later invalid PR identities must remain
    contained without new canonical controls, while every head is still
    inspected when inspectable.
33. **Control-state growth:** even if route count is bounded, unbounded PR/control
    enumeration or direct validation cost may make a fresh cold-start
    practically or logically non-terminating.
34. **Real PR #24 interval special-casing:** WP-018 may have routed correctly
    only because a remembered or manually selected Integrator found PR #24,
    rather than because generic discovery deterministically found and validated
    it.
35. **Activation-binding split brain:** `3b91acf...` may contain substantive
    material not protected by fail-closed pending binding, while `fa6f208...`
    may be mislabeled mechanical despite changing the execution precondition.
36. **Transition-only laundering:** a canonical commit after material base may
    change design, acceptance, authority or verification semantics while being
    called evidence/routing/session-only, leaving WP-018 PASS stale or widening
    reviewer authority.
37. **Canonical-authority inversion:** evidence PRs, candidate controls,
    handoffs, PR metadata, launch views or `WORKSPACE_INDEX.md` may override
    `STATE.md` + active WP rather than remain subordinate routing evidence.
38. **Gate collapse:** WP-018 PASS or a clean WP-019 result may be treated as
    ADR-0002 acceptance, PR #22/#1 merge approval, owner acceptance, Phase 0
    acceptance or Phase 1 activation.
39. **Attempt advancement leakage:** reviewer, verifier, builder or candidate
    content may imply attempt advancement or candidate suppression that only a
    separate authorised Integrator may perform.
40. **Executable-model circularity:** producer/verifier models may encode the
    proposed decision function and prove only internal consistency; an
    independently derived oracle may expose omitted order, identity, lifecycle,
    outage or timing states.
41. **Mutation red-path weakness:** a deliberate invalid-first mutation may fail
    for an incidental assertion rather than proving that current-valid
    precedence is causally protected.
42. **Broader WP-000 regression:** the ten-file repair or provisional rollout
    may weaken any current WP-000 criterion, especially cold-start sufficiency,
    single-source discipline, role separation, change safety, session
    continuity, evidence-backed completion or no-false-completion.
43. **Scope smuggling/history mutation:** PR #22 may change foundation, WP-000
    criteria, immutable historical review/verifier records or `system/` content
    outside the declared candidate-set repair.
44. **Role-start ambiguity:** planning, branch creation, material reading or
    attack execution may occur after a stale final bridge check while still
    being presented as immediate Step-4 commitment.

### Disconfirming evidence sought

The review will try to disprove these hypotheses through exact commit/blob and
live PR inspection, a separately authored routing oracle that imports no
producer code, multi-generation and multi-PR mutations, mixed valid/invalid and
multiple-current states, key/repository/control-authority negatives, outage and
lifecycle replay, the real PR #24 interval, canonical activation/change
classification and semantic authority analysis. A finding will survive only
with an exact claim, evidence, failure path, impact, severity, disproof attempt
and result.

## Findings

### F-AR-008 — A visible result suppresses an uncontained inspection blocker that may conceal a second current result

- **Claim:** The repaired routing rule fails open in the mixed state containing
  one directly validated current result plus one uncontained, uninspectable
  same-WP candidate. It selects the visible result even though the inaccessible
  candidate cannot yet be proven invalid and may become a second current result.
- **Evidence:**
  - `development/01_governance/VERIFICATION_POLICY.md:109-115` says a sole
    current-valid result routes before *invalid* residue, but `:168-172` says an
    uninspectable candidate without canonical containment remains blocked.
  - `development/03_plan/COLD_START.md:47-55` requires direct validation of
    inspectable heads, while `:77-78` says uncontained uninspectable candidates
    fail closed.
  - WP-017 acceptance criterion 6 at
    `development/04_work/WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md:166-168`
    preserves fail-closed uncontained inspection failure; criterion 4 preserves
    multiple-current conflict.
  - The exact model defines currentness as requiring `inspectable` at
    `development/05_evidence/pending_result_control_regression.py:79-85`, puts
    every non-current candidate into `invalid` at `:135-149`, and returns the
    single visible result at `:159-162` before testing uncontained
    inaccessibility at `:163-164`.
  - Its declared regression at `:392-405` therefore expects `INTEGRATOR_RESULT`
    for visible-valid + inaccessible and `BLOCKED_INSPECTION` for the identical
    inaccessible candidate alone. The producer evidence simultaneously claims
    visible-result precedence at
    `F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md:64-68`
    and fail-closed uncontained inspection at `:83-86`.
  - A separate no-import safety oracle classified visible-valid + uncontained
    uninspectable as `BLOCKED_INSPECTION`; the exact subject returned
    `INTEGRATOR_RESULT` for that same boundary probe.
- **Failure path:** A directly inspectable evidence PR A validates under the
  complete active key. PR B is discoverable as a same-WP candidate but its
  immutable head or required artefact/handoff cannot be inspected and no
  canonical stream/set containment covers it. PR metadata is only a locator,
  so B's full key, judgement and scope cannot establish invalidity. The target
  nevertheless places B in `invalid`, selects A, and routes integration. If B
  becomes inspectable and validates, the earlier state was a two-current-result
  conflict, but the repaired decision already selected A rather than failing
  closed until the ambiguity cleared.
- **Impact:** Uncontained inspection failure no longer fails closed when a
  visible result coexists. A potential multiple-current conflict can be
  suppressed, weakening exact result validation, conflict preservation and the
  authority boundary repaired for F-AR-006/F-AR-007.
- **Severity:** **medium — material.** This is encoded in normative governance
  and the executable decision table, and it changes the Integrator route. It is
  not merely a missing test or wording defect.
- **Disproof attempt:** I distinguished candidate-specific inaccessibility after
  valid canonical containment; that state is explicitly contained non-valid and
  did not reproduce the defect. I also tried treating B's locator key as proof
  of staleness, but the target says metadata is locator-only and the control
  template says `uninspectable` is not resolvable by exclusion. Multiple visible
  results correctly route conflict, and a sole inaccessible candidate correctly
  blocks; neither invalidates the mixed-state counterexample.
- **Result:** **stands.** The repair must separate directly proven invalid
  residue from epistemically unknown uncontained candidates; result precedence
  cannot convert the latter into invalidity.

## Attack execution and deterministic evidence

The exact target was fetched by immutable SHA into a detached worktree. Live
PR #22 remained open/draft/unmerged at target `5bd0db27...`, base
`4524f21...`, canonical destination GitHub repository id `1345974984` / node id
`R_kgDOUDnyyA`, with four commits and exactly ten changed files. Its merge-base
with the fetched canonical material base was exact. PR #19 remained
closed/draft/unmerged at historical head `2f5508c...` and was not modified.

Deterministic execution:

- exact producer model SHA-256
  `05e9ce33a6db32ba0009c0b95ee92a7087affa3847dc44c82bafb281d72093f3`:
  **67/67 PASS**;
- its deliberate `WP017_MUTATE_INVALID_FIRST=1` run: expected non-zero after
  **26 PASS**, failing the intended valid + first-invalid assertion;
- independent no-import oracle `/private/tmp/wp019_adversarial_oracle.py`,
  SHA-256
  `d51288a801bf552c9e03dce6ecf87d1b497318d9e8ce3afdec37255ca251d538`:
  **50/50 PASS** across discovery/inspection outage, exact four-field key and
  immutable destination-repository identity, forged control, visible/unknown,
  multiple-valid, containment and 2/10/100/1000-residue states;
- exact-subject boundary harness `/private/tmp/wp019_subject_mutations.py`,
  SHA-256
  `839ba85ab6b4eb1be5c2d3e04d6130ba9eb84eabc0c6d2ccc5ef9baba7827900`:
  **8/8 PASS**, including the observable mixed-inaccessibility fail-open and the
  model's mutable repository-string boundary;
- total passing route assertions/probes: **125**, plus the expected red
  mutation. Producer passes corroborate only declared behavior; they do not
  disprove F-AR-008 because the unsafe expectation is itself one of the 67.

The oracle was independently derived before importing the subject. Its safety
rule was: after repository-wide discovery, preserve multiple directly valid
results as conflict; block any uncontained uninspectable in-scope candidate;
only then route one directly valid result; allow inaccessible residue to become
non-blocking only under a fully bound, canonical, Integrator-owned, proven
control. This distinguishes unknown from directly inspected invalid evidence.

Exact diff inspection found no foundation, WP-000, immutable historical review,
`system/`, acceptance or target-merge mutation in PR #22. `git diff --check`
passed. The target preserves PR #19/WP-015/WP-016 history and does not itself
accept ADR-0002, Phase 0 or PR #22/#1.

## Disposition of the persisted hypotheses

| # | Result | Evidence-backed disposition |
|---:|---|---|
| 1 | disproved | All-state, base-targeted repository enumeration plus direct two-record/head/scope validation is normative; the real PR #24 interval was discoverable. |
| 2 | disproved | Activation `3b91acf...` was fail-closed until binding `fa6f208...`; neither certifies PR #22. |
| 3 | disproved | Fixed invalid heads converge only through exact canonical resolution; uninspectable heads remain blocked. |
| 4 | disproved with declared edge | The mandatory final bridge catches in-interval publication; post-final host mutation remains explicitly non-atomic and later routes result/conflict. |
| 5 | disproved | Same-PR moved heads reopen once, then canonical stream containment survives head/state/branch movement while later validity still wins. |
| 6 | disproved for the claimed governance-reset class | Candidate-set containment is the final canonical escalation across fresh PR identities under one repository/key; 2/10/100/1000 residue mutations did not create new control routes. |
| 7 | disproved for directly proven invalid residue | Single visible validity precedes first/moved/set-contained inspectable-invalid residue and the deliberate invalid-first mutation fails red. F-AR-008 is the unknown-candidate boundary, not a revival of invalid-first ordering. |
| 8 | limitation, no separate finding | Policy binds immutable canonical identity and forbids mutable names/forks/URLs from widening/resetting; the model uses an abstract repository value and does not perform GitHub identity proof. A real control must persist host identity. |
| 9-10 | disproved | Wrong role/target/attempt controls fail; any complete-key change ends containment. |
| 11-14 | disproved at the specified authority boundary | Only a separate canonical Integrator record with exact provenance has effect; wrong/local/candidate-authored/unproven controls do not. Conflicting/contradictory canonical control evidence must fail exact validation rather than be chosen by the model. |
| 15-17 | disproved | Containment classifies only; every later inspectable head is validated, later validity routes, and the first corrected moved head is checked before escalation. |
| 18-19 | disproved | Visible-valid plus first, moved and contained directly invalid residue routes the result without erasing the residue classification. |
| 20 | **stands as F-AR-008** | Visible-valid plus uncontained uninspectable routes result although the unknown candidate may conceal a second valid result. |
| 21 | disproved for inspectable results | Two directly valid current heads remain conflict with invalid or contained residue. F-AR-008 covers the unresolved unknown case. |
| 22-24 | limitation, no separate finding | Lifecycle never erases containment and immutable-head comparison is required. A live force-push race requires refetch/recheck and the final bridge; no atomic host lock is claimed. |
| 25-26 | disproved | Fresh inaccessibility before a valid trigger remains blocked; only candidate-specific inaccessibility after applicable canonical containment is non-blocking. Repository-wide outage is never containable. |
| 27-28 | disproved in live/canonical procedure | Discovery says inspect repository PRs across states with metadata only as locator. Live enumeration was smaller than one API page and direct records, not locator claims, controlled validity. |
| 29-30 | disproved | Exact changed-file lists and both complete records are mandatory; repair/state/acceptance/ADR/merge/Phase scope invalidates a candidate, and completed judgement is required. |
| 31 | disproved | Set escalation requires an earlier canonical invalid-candidate control plus a later directly inspected invalid distinct PR in the same immutable repository and complete key. |
| 32 | disproved for control-state convergence | Large fresh-identity sequences remained contained while later-valid and multiple-valid cases still routed. |
| 33 | explicit non-scope/limitation | Validation work scales with observed candidates; generic host admission/abuse prevention is not claimed. The repair bounds canonical control escalation, not adversarial host traffic. |
| 34 | disproved | Generic all-state enumeration found the exact PR #24 two-file result; no remembered PR number was needed. |
| 35 | disproved | Activation introduced provisional WP-019 while binding supplied the exact target/key; canonical execution stayed fail-closed between them. |
| 36 | disproved | Every canonical post-base commit was path/diff classified; material semantics are in the frozen target, while later canonical changes are activation/binding or evidence/session/index routing only. |
| 37-39 | disproved | `STATE.md` + active WP remain canonical; evidence/control/index records are subordinate, and only a separate Integrator may transition or advance attempts. |
| 40 | **confirmed as review method** | The independent oracle exposed F-AR-008 despite 67/67 producer and verifier agreement. |
| 41 | disproved | The opt-in mutation fails causally at the first mixed valid/invalid precedence assertion after 26 unaffected routes. |
| 42-43 | disproved except F-AR-008 | Exact ten-file scope preserves foundation, WP-000, historical findings and `system/`; no hidden acceptance or history mutation was found. |
| 44 | disproved | The final bridge is executed after attack completion and immediately before result commitment/publication; role scope remains reviewer-only. |

## No-finding boundary beyond F-AR-008

No additional finding survived the attacks. In particular, repository/key
isolation, canonical-before-use, separate Integrator provenance, same-PR and
cross-PR lifecycle convergence, later-valid non-suppression, directly visible
multiple-result conflict, discovery-outage separation, exact scope/history and
gate separation held within the target's stated evidence boundary. External
GitHub availability, immutable host-identity capture in a future real control,
scaling under unbounded host traffic and the declared post-final-check edge
remain explicit limitations rather than claims proven by the producer model.

## Final live bridge

Immediately before result commitment/publication on 2026-08-28, the reviewer
re-fetched all pull heads and repeated the canonical bridge:

- live `origin/phase0/development-os` remained
  `39a91e9a4d11f10ce720458686f33c98a87d20a4` and contained activation
  `3b91acf...` plus binding `fa6f208...` in order;
- canonical `STATE.md` + WP-019 still named the exact complete attempt-1 key;
- live PR #22 remained open/draft/unmerged at exact head `5bd0db27...`, base
  `4524f21...`, canonical repository id `1345974984`, and ten files;
- live PR #19 remained closed/draft/unmerged at exact historical head
  `2f5508c...`, base `dca520...`, and nine files;
- all-state GitHub enumeration returned 23 PRs targeting
  `phase0/development-os`; direct changed review/session-record inspection plus
  locator inspection found **zero WP-019 candidates**;
- therefore no result, conflict, uncontained candidate, discovery/inspection
  outage or applicable control displaced this review. The fresh reviewer role
  and sole result-publication responsibility were recommitted immediately after
  this PASS; no further material reading or attack design intervened.

The result was then initially published as PR #25 at immutable head
`6b328cdeb127f56b163b999eaa8621fd6d5ead19` against base
`39a91e9a4d11f10ce720458686f33c98a87d20a4`. Its authorised and observed
changed-file scope is exactly this review artefact plus SESSION-0034. The only
later branch change permitted is the locator-only update binding that
publication in those same two records; the final PR head is recorded in the PR
close update and post-publication bridge rather than through impossible
self-reference.

## Overall judgement

**Requires repair.** Exact target `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
is not suitable for integration under the bound WP-019 key because F-AR-008
materially violates fail-closed uncontained inspection and can suppress a
multiple-current-result conflict. This judgement neither supplies a repair nor
accepts/rejects ADR-0002, merges PR #22/#1, changes canonical state/attempt,
accepts Phase 0 or begins Phase 1.
