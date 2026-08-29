# WP-020 — Phase 0 Uncontained Inspection Fail-Closed Repair

**Status:** blocked — unresolved F-AR-008 preserved; execution deferred while WP-021 evaluates and strengthens Development OS lifecycle/work-selection  
**Owner role:** designer/builder when/if this repair is reactivated under the then-current accepted lifecycle
**Decision authority:** bounded repair of F-AR-008 within existing
foundation/governance and unchanged WP-000 acceptance criteria unless a later accepted Development OS change explicitly supersedes this routing;
architecture-level choices must follow `DECISION_POLICY.md`; no independent
verification, adversarial-review self-approval, canonical independent-result
integration, ADR acceptance, PR #22/#1 merge, Phase acceptance or Phase 1
authority
**Development branch:** `phase0/development-os`
**Rejected material target:** draft/unmerged PR #22 exact commit
`5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Parent:** `WP-000-DEVELOPMENT-OS.md`
**Prior repair package:** `WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md`
**Current blocker:** `WP-021-DEVELOPMENT-LIFECYCLE-WORK-SELECTION-IMPROVEMENT.md` — Development OS must decide/evaluate whether the correct next work is still this bounded repair before implementation proceeds
**Exact-target verification:** WP-018 — **PASS** for exact target
`5bd0db27fc3df368c9e112f01b7eed49a64402ab`, activation
`fbe517bef10b5e820dc096a8a82e2c1a3047a38c` and binding
`e62075228054f43f4dc8d318210ce9de0bf8b8ae`
**Adversarial re-review:** WP-019 — **Requires repair**; F-AR-008
medium/material, stands
**Reviewer evidence:**
`development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-5bd0db27-2026-08-28.md`
**Reviewer evidence PR:** #25, initial immutable result commit
`6b328cdeb127f56b163b999eaa8621fd6d5ead19`, final locator head
`16b5aacb12d05157e183cb9257025f30636e0f71`, integrated evidence-only as
`8022ca6fb30fc32e6a95f22c5c1d58c5ab8c1745`
**Completed review result-control key:** `WP-019 / adversarial reviewer / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Completed review activation/binding:**
`3b91acf02df2852c43404ec164725ac5748b9bad` /
`fa6f208e6133f746a69a4a51faff3f2485798d24`

## Objective

If reactivated after WP-021 work-selection/design evaluation, produce the smallest coherent material repair for F-AR-008 so the pending
independent-result route does not convert an uncontained, uninspectable
same-key candidate into invalid residue merely because one current-valid result
is visible.

The repaired control must preserve current-valid-result precedence over
directly proven invalid or validly contained non-valid residue while remaining
fail closed when an uncontained candidate is epistemically unknown and could
conceal a second current result. The builder must derive the repair
architecture; this routing WP does not preselect a particular implementation,
control record, ordering expression or PR disposition.

This objective remains an unresolved candidate work path, not a current instruction to implement. WP-021 may conclude through an accepted lifecycle/work-selection process that a broader reframing or another authorised path supersedes this bounded repair. Such a conclusion must preserve F-AR-008 as an unresolved obligation rather than erase it.

## Exact finding preserved

### F-AR-008 — A visible result suppresses an uncontained inspection blocker that may conceal a second current result

**Result:** stands.
**Severity:** medium — material.

The exact PR #22 target routes one directly validated current result before an
uncontained, uninspectable same-WP candidate. Because candidate metadata is
only a locator, the inaccessible candidate cannot be proven invalid and may be
a second current result. The route therefore fails open on an explicit
inspection blocker and can suppress the required multiple-current conflict.

The complete claim, evidence, failure path, impact, disproof attempt and
limitations remain authoritative in the immutable WP-019 review artefact. This
WP must not rewrite, soften or reinterpret them.

## Scope

If this WP is reactivated:

- analyse both the immediate decision-order/type defect and the system cause
  that collapsed directly proven invalid residue and epistemically unknown
  uncontained candidates into one class;
- preserve a mechanically explicit distinction between a directly inspected
  invalid candidate, a validly contained non-valid candidate and an
  uncontained candidate whose required head or records cannot be inspected;
- preserve exactly-one-current-valid routing before directly proven invalid or
  validly contained non-valid residue;
- fail closed when any uncontained in-scope candidate remains uninspectable,
  including the mixed state with one visible current-valid result;
- preserve multiple-current-result conflict when the formerly unknown
  candidate becomes inspectable and validates;
- preserve later-valid non-suppression, direct validation of every inspectable
  head, exact repository/key/head identity, canonical-before-use and
  Integrator-only control authority;
- preserve fixed-head, same-PR stream and cross-PR candidate-set convergence
  without allowing containment to become validity, absence or acceptance;
- reconcile every changed normative rule, executable decision model, template
  and evidence claim so their state classifications and route ordering agree;
- add deterministic red-capable regression evidence for visible-valid plus
  uncontained-uninspectable, the same candidate alone, later-inspectable valid,
  later-inspectable invalid, multiple-current conflict, contained inaccessible
  residue and repository-wide discovery failure;
- preserve historical F-AR-001 through F-AR-008 wording, results and exact-
  target bindings;
- identify one new exact material target, its base and complete changed-file
  scope, and explicitly record whether PR #22 is amended, superseded or
  otherwise related to it;
- route changed material to fresh separate verification and, after result
  integration, fresh separate adversarial re-review.

## Non-scope

- executing this repair while WP-021 remains the active blocker;
- prescribing the substantive repair design from this routing package;
- changing or weakening WP-000 acceptance criteria;
- rewriting, deleting or reinterpreting F-AR-001 through F-AR-008 or any
  immutable verifier/reviewer evidence;
- treating WP-018 PASS as certification of a changed target or treating WP-019
  evidence integration as target acceptance;
- accepting or rejecting ADR-0000, ADR-0001 or ADR-0002;
- independently verifying or adversarially re-reviewing the builder's own
  repair;
- resolving/containing a live evidence candidate, advancing an independent-role
  attempt or integrating an independent result;
- merging PR #22 or PR #1, accepting Phase 0 or beginning Phase 1;
- absorbing generic host abuse prevention, platform administration or product-
  runtime architecture without a demonstrated direct dependency and explicit
  governance path.

## Required reading

If this WP is reactivated, enter through `development/03_plan/COLD_START.md` and complete Steps 1–2 first.
Within Step 3, read:

1. `development/04_work/WP-000-DEVELOPMENT-OS.md`;
2. `development/06_reviews/ADVERSARIAL-REREVIEW-WP-000-5bd0db27-2026-08-28.md`;
3. `development/07_sessions/SESSION-0034-PHASE0-CANDIDATE-SET-CONVERGENCE-ADVERSARIAL-REREVIEWER.md`;
4. `development/04_work/WP-017-PHASE0-CANDIDATE-SET-CONVERGENCE-REPAIR.md`;
5. `development/04_work/WP-018-PHASE0-CANDIDATE-SET-CONVERGENCE-VERIFICATION.md`;
6. `development/04_work/WP-019-PHASE0-CANDIDATE-SET-CONVERGENCE-ADVERSARIAL-REREVIEW.md`;
7. exact PR #22 metadata/diff and all ten files at `5bd0db27fc3df368c9e112f01b7eed49a64402ab`;
8. exact PR #25 metadata, initial/final heads, two-file evidence scope and
   evidence merge `8022ca6fb30fc32e6a95f22c5c1d58c5ab8c1745`;
9. `development/07_sessions/SESSION-0033-PHASE0-WP018-RESULT-INTEGRATOR-RECOVERY.md`
   and the WP-019 result-Integrator handoff;
10. canonical `SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`,
    `REASONING_POLICY.md`, `ROLE_MODEL.md`, `DECISION_POLICY.md`,
    `CHANGE_POLICY.md` and `VERIFICATION_POLICY.md`;
11. `development/03_plan/COLD_START.md`, `PR_GATE.md` and `PHASE_GATE.md`;
12. proposed ADR-0002, all three producer evidence records, exact executable
    model and result-control template on PR #22;
13. the accepted WP-021 lifecycle/work-selection artefacts that determine why this bounded repair is being reactivated rather than superseded.

## Inputs and dependencies

- immutable WP-019 judgement **Requires repair** for exact target `5bd0db27...`;
- F-AR-008 medium/material, standing;
- WP-018 historical **PASS** permanently bound only to exact target
  `5bd0db27...` and its activation/binding;
- PR #22 remaining draft, unaccepted and unmerged until a new-target relation
  and all later gates are established;
- accepted output of WP-021 establishing that this bounded repair is the correct next work, if reactivated;
- then-current WP-000 criteria and foundation/governance authority boundaries.

## Outputs

If reactivated:

- a bounded material repair candidate on an explicit repair branch/PR;
- one new exact material target SHA and base with complete changed-file scope;
- any required proposed ADR update/supersession/new ADR under
  `DECISION_POLICY.md` without accepting it;
- deterministic, red-capable F-AR-008 regression evidence plus preservation
  coverage for F-AR-001 through F-AR-007;
- a documented relation to PR #22 and its rejected exact target;
- a fresh builder session handoff;
- routing to fresh separate verification and later fresh separate adversarial
  re-review, without performing either.

## Acceptance criteria

If reactivated:

1. **Finding fidelity:** F-AR-008 wording, medium/material severity, standing
   result and exact target/key/activation/binding remain unchanged.
2. **State distinction:** directly proven invalid, validly contained non-valid
   and uncontained uninspectable candidates cannot be conflated.
3. **Fail-closed mixed state:** one visible current-valid result plus any
   uncontained uninspectable in-scope candidate blocks rather than integrating.
4. **Valid precedence boundary:** exactly one current-valid result still routes
   before all directly proven invalid or validly contained non-valid residue.
5. **Conflict preservation:** multiple current-valid results remain explicit
   conflict, including after an unknown candidate becomes inspectable.
6. **Direct validation:** every inspectable head is directly validated; locator
   metadata, containment and prior invalidity never become current validity.
7. **Convergence preserved:** fixed-head, same-PR and cross-PR recovery remain
   bounded under one exact repository/key without suppressing later validity.
8. **Outage separation:** repository-wide discovery failure and uncontained
   candidate inspection failure remain fail closed; only an exactly applicable
   canonical control may classify candidate-specific inaccessible residue as
   contained non-valid.
9. **Authority and freshness:** repository/PR/head plus all four key fields stay
   exact; controls remain canonical-before-use and Integrator-only.
10. **Model and evidence correctness:** normative text, executable model,
    templates and evidence agree, and the unsafe mixed-state ordering fails red.
11. **Current parent criteria:** every then-current WP-000 criterion is preserved
    and freshly re-verified for the new exact target.
12. **Exact target and fresh gates:** one new target/base/scope is frozen and
    receives fresh separate verification plus fresh separate adversarial
    re-review before any ADR/PR/Phase acceptance.
13. **No false completion:** the repair accepts no ADR, merges no PR #22/#1,
    accepts no Phase and begins no Phase 1 work.
14. **Scope discipline:** unrelated host administration, historical PR noise
    and product-runtime architecture are not silently absorbed.

## Required verification and review

If reactivated:

- fresh separate verifier against the new exact target, including all then-current
  WP-000 criteria and explicit regression of F-AR-001 through F-AR-008;
- separate Integrator result transition after verifier close;
- fresh separate adversarial re-review of the exact verified repair target;
- fresh result integration after reviewer close;
- ADR/human-owner/PR/Phase gates remain separate and unchanged.

## Evidence obligations

Preserve a claim-to-trace chain for F-AR-008 and every retained safety
property, including exact target/base/scope, negative cases that can fail red,
mixed visible/unknown traces, later-inspectable valid/invalid traces,
limitations, credible alternatives and why the selected mechanism is necessary
and smaller than those alternatives.

## Risks

- losing or softening F-AR-008 merely because its prior repair routing is blocked;
- reactivating the old repair automatically after WP-021 without an explicit work-selection conclusion;
- fixing the mixed state by suppressing legitimate current-valid-result
  precedence over directly proven invalid residue;
- treating every inaccessible contained candidate as unknown forever and
  reintroducing the convergence denial class;
- treating locator metadata or past invalidity as proof that an inaccessible
  current head is invalid;
- hiding the state distinction only in the executable model while normative
  governance remains ambiguous;
- laundering material repair as transition-only change;
- expanding the fix into generic platform admission or abuse control before
  Phase 0 acceptance.

## Completion state

**Blocked, unresolved.** No F-AR-008 repair, new exact material target, verification or re-review exists. The finding and all historical exact-target evidence remain unchanged. Execution may resume only after WP-021 establishes through the accepted Development OS lifecycle that this bounded repair is the correct next work, or WP-020 is explicitly superseded by a successor work package that carries F-AR-008 unchanged as an unresolved acceptance obligation.

## Handoff

No Builder should execute this WP while WP-021 is active. The current next responsibility is defined by `STATE.md` and WP-021. If a later accepted work-selection decision reactivates WP-020, use the then-current Development OS lifecycle and this preserved F-AR-008 obligation rather than assuming the old repair route is automatically valid.
