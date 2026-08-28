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

Pending post-checkpoint attack execution.

## Overall judgement

Pending post-checkpoint attack execution.
