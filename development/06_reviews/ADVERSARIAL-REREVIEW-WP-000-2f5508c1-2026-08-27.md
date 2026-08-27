# ADVERSARIAL RE-REVIEW — WP-000 / MOVING-CANDIDATE CONVERGENCE REPAIR

**Reviewer session:** SESSION-0028
**Reviewed commit/artefact:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Material target PR:** #19 — `WP-014: bound moving-candidate convergence without result suppression`
**Authoritative specification:** `development/04_work/WP-000-DEVELOPMENT-OS.md`; `development/04_work/WP-016-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEW.md`
**Result-control key:** `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**Provisional activation commit:** `94bcc9bf9d0352bde67459635a6073c7e65171e2`
**Activation-binding commit:** `91db45818f324a1c1aef4dd16d48e40591a3f4e1`
**Reviewer output branch:** `codex/wp016-adversarial-reviewer`
**Date:** 2026-08-27

## Pre-evidence attack model

This attack model was persisted after canonical COLD_START Steps 1–2, the first
WP-016 bridge check and WP-016 Step 3A. It precedes inspection of WP-014's
repair rationale, the exact nine-file target as a preferred solution, proposed
ADR-0002 rationale, producer evidence/model, SESSION-0024 builder conclusions,
WP-015 verifier conclusions and SESSION-0027's claims as evidence of
suitability. Routing facts necessarily exposed by canonical state, the active
WP and the mandatory live bridge/activation-chain inspection are not treated as
proof that the material control works.

### First bridge-check observation

- live canonical `origin/phase0/development-os` head:
  `acf163f3073e25d9390b883786143d520d0859cf`;
- live PR #19: open/draft, base `phase0/development-os`, API material base
  `dca520242585a80c2efaf22e18fe3d353147b93e`, exact head
  `2f5508c1d6941e951d494bb2a700ef861860431d`, exactly nine declared files;
- superseded PR #16: closed/unmerged, exact head
  `adf067e4289e4c0b51cf40c1940193e8252b22e0`, exactly eight historical files;
- current complete key:
  `WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`;
- exact activation/binding chain: `94bcc9bf...` then `91db4581...`; later
  canonical `acf163f...` adds only SESSION-0027 plus its subordinate index row;
- repository-wide live PR discovery against `phase0/development-os` found no
  open or merged/closed candidate claiming WP-016, and canonical inspection
  found no WP-016 resolution or containment record.

The first bridge check therefore permits Step 3 review preparation to
continue. It is not the required final bridge check and is not evidence that
the reviewed material survives the attacks below.

### Attack surfaces and hypotheses to test

1. **F-AR-001 replay — current-result discoverability:** a completed exact-key
   result can be absent from discovery, accepted from metadata alone, or
   misclassified during the post-result/pre-Integrator interval, permitting
   duplicate work or false routing.
2. **F-AR-002 replay — self-hosting activation:** the WP-local activation may
   fail to protect WP-015/WP-016 close intervals, depend circularly on the
   unmerged target, or be silently treated as target verification/acceptance.
3. **F-AR-003 replay — fixed-candidate recovery:** a fixed invalid, stale,
   malformed, closed or uninspectable same-WP candidate may remain blocking
   after an exact canonical resolution.
4. **F-AR-004 replay — timing:** publication between initial and final checks
   may escape detection; publication after the final check may be laundered
   into unique valid completion rather than recovered as duplicate/conflict.
5. **F-AR-005 replay — repeated movement:** one resolved candidate may keep
   invalidating exact-head resolution indefinitely despite the new movement
   containment rule.
6. **Candidate-identity rotation:** a lower-authority source may move from PR
   `p1` to newly opened same-key PRs `p2...pn`, resetting any per-PR movement
   containment and retaining an unbounded repository-level denial path even if
   each individual PR converges.
7. **Repository/key aliasing:** containment may match a repository by mutable
   name, fork/source identity, case, URL spelling or local remote rather than
   exact canonical repository identity and destination PR number.
8. **Partial-key containment:** equality on WP/target while omitting role or
   attempt may suppress a later legitimate result or leak historical controls
   into the active attempt.
9. **Candidate-authored/forged control:** text in PR metadata, evidence files,
   handoffs or a local branch may masquerade as canonical Integrator resolution
   or containment and unblock execution.
10. **Noncanonical-before-canonical race:** a validly shaped containment may be
    consumed before it is committed on the authoritative development line, or
    may remain effective after its canonical identity changes.
11. **Containment-as-validity:** the system may stop inspecting heads once a PR
    is contained, turning a recovery control into evidence validity or an
    arbitrary ignore rule.
12. **Later-current-valid suppression:** a contained PR may later carry a fully
    current exact-key result but remain ignored because containment is bound to
    candidate identity rather than the invalid head generations it observed.
13. **Valid/invalid mixture ordering:** one current-valid result plus one
    uncontained invalid candidate, or a valid result plus contained invalid
    residue, may be routed by arbitrary ordering and either suppress the valid
    result or prematurely treat the set as clean.
14. **Multiple-current selection:** two current valid results may be selected by
    recency, PR number, open/closed state or containment history instead of
    preserving conflict for Integrator-only attempt advancement.
15. **First moved head is valid:** a head corrected immediately after fixed-head
    resolution may be sent into movement containment before direct validation,
    suppressing the newly valid result.
16. **Alternating validity:** a candidate alternating invalid, valid and
    inaccessible heads may exploit stale observations or containment to create
    false completion, false conflict or indefinite blocking.
17. **Closed/reopened/force-pushed lifecycle:** PR closure, reopening, merged
    state, force-push, branch deletion and pull-ref persistence may change which
    immutable head is inspected or whether an old control applies.
18. **Candidate-specific inaccessibility ambiguity:** a deleted/inaccessible
    candidate head may be incorrectly classified as repository-wide discovery
    failure, or a repository-wide/API outage may be incorrectly contained as a
    candidate-local fault.
19. **Inaccessible-before-proof:** containment may be authorised for a head
    whose repository/PR/key identity or invalidity was never directly
    inspectable, allowing an attacker or transient outage to erase a possible
    current result.
20. **Pagination/search omission:** repository-wide discovery may silently omit
    older, closed, renamed or paginated same-key candidates and still report a
    clean reviewer route.
21. **Resolution/containment disagreement:** multiple canonical controls for
    the same PR/key with different repository identity, heads or conclusions
    may be arbitrarily chosen instead of preserved as a blocking conflict.
22. **Attempt advancement leakage:** a reviewer, verifier, builder or candidate
    may imply attempt advancement through filenames/body text or containment;
    only an authorised Integrator may advance the complete key.
23. **Real PR #20 interval special-casing:** the WP-015 close interval may have
    routed correctly only because a remembered/specially selected Integrator
    found PR #20, not because a generic execution of the bridge deterministically
    discovered and validated it.
24. **Activation-binding split brain:** the two-commit activation/binding
    sequence may admit work in its intentionally unbound intermediate state, or
    the later binding may be mislabeled mechanical despite changing the
    execution precondition.
25. **Transition-only laundering:** a canonical commit after material base may
    change design, acceptance, authority or verification semantics while being
    described as evidence/routing/session-only, leaving WP-015 PASS stale or
    widening WP-016 authority.
26. **Canonical-authority inversion:** evidence PRs, containment/resolution
    records, handoffs, PR metadata, launch views or `WORKSPACE_INDEX.md` may
    override `STATE.md` + active WP rather than serving as subordinate routing
    evidence.
27. **False gate collapse:** WP-015 PASS or a clean WP-016 result may be treated
    as ADR-0002 acceptance, PR #19/#1 merge approval, owner acceptance, Phase 0
    acceptance or Phase 1 activation.
28. **Scope-smuggling:** the nine-file target, evidence PRs or activation chain
    may change historical reviews, WP-000 acceptance criteria, higher-authority
    foundation/governance, or `system/` content outside the claimed repair.
29. **Executable-model circularity:** producer/verifier models may encode the
    proposed transition table and demonstrate only internal consistency; an
    independently derived state machine or direct semantic trace may expose
    unmodelled order, identity, outage or lifecycle combinations.
30. **Operational non-convergence:** even if each PR has a bounded two-control
    lifecycle, the number of candidate identities, canonical control records or
    live inspections may grow without a project-level bound and make fresh
    bootstrap practically or logically non-terminating.
31. **Role-start ambiguity:** branch creation, planning or substantive attack
    work may occur after a stale final check while still being presented as
    immediate Step-4 commitment.
32. **Broader WP-000 regression:** the repair or provisional rollout may weaken
    any current WP-000 criterion, especially cold-start sufficiency, role
    separation, change safety, session continuity, no-false-completion or the
    single reasoning-policy/bootstrap authority.

### Disconfirming evidence sought

The review will try to disprove these hypotheses through exact commit/blob and
live PR inspection, an independently authored routing oracle that imports no
producer code, multi-generation and multi-PR identity mutation, later-valid and
multiple-current cases, outage/inaccessibility/timing replay, historical PR #20
lifecycle reconstruction, canonical activation/change classification and
semantic authority analysis. A finding will survive only with an exact claim,
evidence, failure path, impact, severity, disproof attempt and result.

## Findings

Pending adversarial execution.

## Overall judgement

Pending adversarial execution.
