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
**Reviewer evidence PR:** #21 — initial published head `85673cbd291a5571c1cb5ce4601a8ffd4eb1bc62`
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

### F-AR-006 — Rotating to fresh PR identities resets per-candidate containment and restores unbounded denial

- **Claim:** the repair bounds repeated invalid movement only for one identity
  `(repository, PR number, active key)`. A lower-authority source can publish the
  same invalid same-WP claim through fresh PR identities. Each new PR is outside
  every prior containment and therefore restarts exact-head resolution followed
  by movement containment. The repository-level independent-role route remains
  indefinitely suppressible even though every individual PR converges.
- **Evidence:** exact target `VERIFICATION_POLICY.md` binds the final escalation
  to `(repository, PR number, active key)` and calls it final only “for that
  identity”; target `COLD_START.md`, `PR_GATE.md`, ADR-0002 and the control
  template use the same PR-scoped identity. Neither canonical policy nor the
  WP-local bridge defines candidate admission, a repository/key-wide convergence
  boundary, or a bounded response to fresh PR identities. ADR-0002 explicitly
  names distinct-PR creation as a reopen condition, and producer/verifier records
  preserve many-PR flooding as an unclosed limitation. The independent oracle
  replayed PR identities 100 through 108 under one unchanged key: PRs 100–107
  each required a first exact-head resolution and then movement containment;
  after all eight containments existed, fresh PR 108 again routed exact-head
  resolution. The exact producer decision function reproduced the same reset for
  PRs 300–308. Both traces were re-run after the final WP-016 bridge/role gate.
- **Failure path:** invalid same-WP PR `p1/h1` blocks → Integrator resolves
  `p1/h1` → source moves `p1` to invalid `h2` → Integrator contains `p1` → source
  publishes the same invalid claim as fresh PR `p2` → no `p1` control matches
  `p2` → resolution/containment repeats for `p2...pn` → canonical verifier or
  reviewer responsibility never becomes stable. Closing, deleting or containing
  earlier PRs does not affect the next identity, and each new PR may be created
  after the latest canonical recovery commit.
- **Impact:** lower-authority locator creation retains an unbounded
  denial-of-progress capability and can force an unlimited sequence of separate
  Integrator inspections/control commits. This violates WP-000 cold-start
  sufficiency and session-continuity expectations during a supported active-key
  state and fails the broader bounded-agency/recovery property the F-AR-005
  repair is intended to restore. Canonical truth is not silently corrupted,
  which limits severity.
- **Severity:** **medium — material**.
- **Disproof attempt:** confirmed that one fixed invalid head resolves and one
  repeatedly moving PR converges after containment; h3–h12 on the same PR no
  longer reset recovery. Confirmed wrong-repository/key, local,
  candidate-authored and unproven controls remain ineffective, so broad forged
  suppression is not the answer. Checked whether closing, attempt advancement,
  or batching current invalid PRs bounds future identities; none prevents a new
  PR under the still-active key. Checked for author trust, freeze, admission,
  repository/key-wide conflict or bounded-many-identity escalation; the target
  deliberately defines none and records the attack only as a reopen condition.
  An acknowledged reopen condition bounds the claim but does not disprove the
  reproduced failure against current WP-000 continuity.
- **Result:** **stands**.

### F-AR-007 — The executable routing model lets an invalid candidate outrank a current-valid result

- **Claim:** the exact target's executable decision-table model contradicts the
  normative rule that one current-valid candidate wins routing. When one valid
  current result coexists with any uncontained invalid candidate, the model
  returns resolution or containment before checking the single current result.
- **Evidence:** target `VERIFICATION_POLICY.md` states “Current valid result wins
  routing” and target `COLD_START.md` says one current match routes to
  Integrator and a current-valid head always routes normally. In
  `pending_result_control_regression.py`, `current` and `uncontained_invalid` are
  both computed, but lines 118–131 return invalid resolution/containment before
  lines 132–133 return the single-current result. Post-gate mutations produced:
  valid + first invalid → `INTEGRATOR_RESOLUTION`; valid + moved invalid →
  `INTEGRATOR_CONTAINMENT`; valid + two fresh invalids →
  `INTEGRATOR_RESOLUTION`, while the normative outcome is
  `INTEGRATOR_RESULT`. The declared 28-case producer suite has no mixed
  current-valid/uncontained-invalid case.
- **Failure path:** a complete exact-key result is published → an invalid
  same-WP candidate coexists → a consumer following the shipped executable
  model chooses candidate-control work instead of normal result integration →
  the invalid source can repeat identity rotation before its control completes →
  valid result routing is delayed indefinitely despite the normative
  non-suppression rule.
- **Impact:** the producer evidence/model can remain 28/28 green while encoding
  the wrong precedence for a material mixed state. This weakens the
  claim-to-trace evidence and gives a future implementation or reviewer a
  concrete path to reintroduce result suppression. The canonical prose still
  supplies the correct rule and the executable is labelled producer evidence
  rather than an enforcing runtime, so this does not independently establish the
  same material severity as F-AR-006.
- **Severity:** **low — evidence/model correctness**.
- **Disproof attempt:** confirmed the model correctly routes valid + contained
  invalid to result and two valid + invalid to conflict; the defect is limited
  to coexistence with an uncontained invalid. Confirmed no current canonical
  runtime automatically imports this producer model and that all evidence files
  call it non-independent, limiting operational impact. Re-read the normative
  policy to test whether invalid-first was intended; it explicitly gives the
  current-valid route precedence. The mismatch therefore remains real even
  though the prose control is correct.
- **Result:** **stands**.

## Historical finding replay and other attack results

- **F-AR-001 — completed-result discovery:** disproved for a single current
  result. The real PR #20 interval had one exact-key, completed, two-file
  evidence candidate while canonical WP-015 remained active; generic bridge
  evaluation routes Integrator rather than duplicate verification.
- **F-AR-002 — provisional activation:** disproved for WP-015 and WP-016.
  Activation/binding chains are exact; WP-016 activation `94bcc9b...` is
  substantive provisional rollout, `91db458...` binds it, and the only later
  canonical commit is SESSION-0027 plus its subordinate index row. Both live
  WP-016 bridge checks completed with no candidate or blocker.
- **F-AR-003 — fixed invalid residue:** disproved for a fixed head. One directly
  proven invalid head plus exact canonical resolution unblocks. An uncontained
  inaccessible head remains fail-closed.
- **F-AR-004 — check timing:** disproved inside the declared boundary.
  Publication during Step 2/3 is observed by the final check; a second valid
  result after commitment is later preserved as conflict. The explicit
  post-final-check host edge remains a limitation, not an atomic-lock claim.
- **F-AR-005 — repeated movement of one PR:** disproved for the same contained
  identity. Invalid h3–h12 converged without further resolution; later valid,
  closed/inaccessible, wrong-key/repository and changed-state cases retained the
  specified routes. Candidate-identity rotation is the distinct surviving
  F-AR-006 generalisation.
- **Containment forgery and authority leakage:** wrong key/repository, local,
  candidate-authored, noncanonical and unproven containment did not unblock.
  Controls remain Integrator-only and canonical-before-use.
- **Later-valid and conflict preservation:** the independent oracle routed a
  later-valid contained stream and a first corrected moved head to Integrator;
  two current-valid results remained conflict. F-AR-007 records the narrower
  inconsistency in the shipped producer model for mixed valid/uncontained sets.
- **Outage and lifecycle:** repository-wide discovery loss and uncontained
  candidate inaccessibility fail closed; contained candidate-specific
  inaccessibility remains explicit non-valid residue and later validity reopens
  direct routing.
- **Freshness/transition laundering:** all canonical commits after material base
  were classified individually. Builder routing/session records, WP-015
  substantive activation/binding, verifier evidence PR #20, WP-016 substantive
  activation/binding and SESSION-0027 remain separate from the frozen nine-file
  material target. No historical review, foundation, WP-000 criterion or
  `system/` path is changed by PR #19.
- **Authority/gate collapse:** `STATE.md` + active WP remain canonical;
  evidence/control/PR/index records remain subordinate. WP-015 PASS remains
  exact verification evidence only. ADR-0000/0001/0002, PR #19/#1, owner and
  Phase gates remain unaccepted.

## Deterministic and repository evidence

All deterministic evidence below was re-executed after the final live WP-016
bridge check and immediate reviewer-role commitment.

- independent oracle `/private/tmp/wp016_adversarial_oracle.py`, SHA-256
  `8490ac183dd79ff2eb3805485277a0c6840302fe0bf86f1e8bd2825649cbb515`:
  **51/51 expected routes passed**;
- exact producer model, SHA-256
  `7eee4c9ae3cbe38265640dcdafe03bb4f00dae505a5f1909e820ab467261a99f`:
  **28/28 declared cases passed** as corroboration only;
- producer mutation harness `/private/tmp/wp016_producer_mutations.py`, SHA-256
  `8074207d379df294200c83ffdcad62783c2b1efae76baec6e71c3f8e6acb4faa`:
  **3/4 mixed-state cases exposed the invalid-first precedence mismatch**,
  **1/4 conflict case passed**, and **9/9 successive fresh PR identities reset
  recovery** through 17 resolution/containment route assertions;
- total deterministic route assertions/observations: **100** (51 independent,
  28 producer-declared, 4 mixed-state, 17 identity-rotation);
- `git diff --check dca520... 2f5508c...` passed; exact scope remains nine
  files; exactly one `COLD_START.md` exists; historical `BUILDER_STOP.md` is
  absent; foundation, WP-000, immutable F-AR-001–005 review files and `system/`
  are unchanged.

## WP-000 and WP-016 acceptance assessment

- WP-000 criteria 2–7 and 9–12 survive direct inspection. Criteria **1
  cold-start sufficiency** and **8 session continuity** do not survive F-AR-006:
  fresh PR identities can repeatedly replace the required independent role with
  control handling under an unchanged active key.
- WP-016 criteria 1–6 and 8–20 are satisfied for their declared exact-target,
  same-candidate, authority, timing, history and publication obligations, subject
  to final publication freshness. Criterion 7's normative current-valid
  non-suppression rule is present, but the included executable evidence model
  contradicts it in mixed valid/uncontained sets (F-AR-007).
- Producer/verifier evidence was used as input only after the hypothesis
  checkpoint and was independently attacked rather than inherited as proof.

## Limitations

- The independent oracle and mutation harness are deterministic routing
  abstractions, not live GitHub transaction tests. Their attacks follow the
  exact specified identity transitions, and the target itself records
  distinct-PR flooding as a reopen condition.
- No malicious live PRs or candidate controls were created because that would
  mutate project state outside reviewer authority. The live repository supplied
  exact target/result lifecycle evidence; synthetic mutations supplied the
  disproof traces.
- The post-final-check publication edge remains real and intentionally bounded,
  not eliminated. Same-model isolated review is not true model diversity.
- Reviewer publication/close freshness and the generic WP-016 post-publication
  route are recorded after the dedicated evidence PR exists.

## Publication and close evidence

Dedicated reviewer evidence PR #21 was published against
`phase0/development-os` at initial head
`85673cbd291a5571c1cb5ce4601a8ffd4eb1bc62`. Immediate direct inspection found:

- source branch and `refs/pull/21/head` both resolved to that exact head;
- PR #21 was open/non-draft and its changed-file scope was exactly this review
  artefact plus SESSION-0028;
- both records carried the identical complete WP-016 key, target, base,
  activation/binding and completed **Requires repair** judgement with F-AR-006
  and F-AR-007;
- live all-state discovery found exactly one WP-016 candidate, PR #21;
- canonical `origin/phase0/development-os` remained exact `acf163f...`, still
  assigning WP-016 and the same key/activation;
- live PR #19 remained open/draft at exact `2f5508c...` from `dca520...` with
  exactly nine files; PR #16 remained closed/unmerged at `adf067e...`.

The generic WP-016 bridge therefore routes a fresh session to a separate
Integrator rather than repeating adversarial review. The only later evidence
branch change is this publication/close locator update inside the same two
authorised records. The reviewer does not update `STATE.md`, integrate the
result or create a candidate control.

## Overall judgement

**Requires repair.**

The exact material target
`2f5508c1d6941e951d494bb2a700ef861860431d`, material base
`dca520242585a80c2efaf22e18fe3d353147b93e` and WP-016 provisional activation
are not suitable to proceed directly to ADR/PR/Phase acceptance because
F-AR-006 stands medium/material. F-AR-007 also stands low as an exact-target
evidence/model correctness defect.

This judgement is bound only to:

`WP-016 / adversarial reviewer / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`

and activation/binding `94bcc9bf...` / `91db4581...`. The reviewer publishes
only this artefact and SESSION-0028, then stops for a separate Integrator. The
Integrator must preserve **Requires repair**, F-AR-006 and F-AR-007 without
reinterpretation, validate exact two-file scope and route the smallest bounded
separate repair/resolution responsibility. This review does not repair either
finding, create candidate controls, advance the attempt, accept/reject ADR-0002,
merge PR #19/#1, accept Phase 0 or begin Phase 1.
