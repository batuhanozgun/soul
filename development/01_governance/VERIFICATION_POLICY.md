# VERIFICATION POLICY

Verification asks whether the work satisfies the authoritative specification and whether material claims are actually supported. It is distinct from evaluation, which asks how good, useful, or robust the result is.

## Core rules

1. The producer's declaration is not proof.
2. Tool success or exit code is not sufficient when the claim concerns the semantic result of the tool.
3. Another model instance agreeing is not independent evidence by itself.
4. Deterministic checks are preferred when the property can be checked deterministically.
5. Evidence must be inspected at the level needed by the claim; a citation that merely exists is not enough if its content does not support the claim.
6. `NOT VERIFIED` is a legitimate outcome and must not be coerced into pass/fail confidence language.
7. Verification must use the current artefact and current acceptance criteria; stale green results do not certify later material changes.

## Verification hierarchy

Use the strongest applicable layer first:

1. invariant / schema / type / permission checks,
2. deterministic tests and reproducible commands,
3. direct artefact and source inspection,
4. analytical/statistical validation when relevant,
5. semantic model-based review when deterministic validation is insufficient,
6. human review for declared human-authority decisions or risk gates.

Higher numbered layers do not replace lower numbered checks that are available.

## Verification record

A material verification artefact should state:

- claim or acceptance criterion,
- evidence inspected,
- method,
- result: PASS / FAIL / NOT VERIFIED,
- limitations,
- verifier session,
- artefact/version/commit verified.

## Independence

For material architecture and control changes, the verifier must operate in a fresh session or isolated execution and read the authoritative specification before reading the builder's rationale. The purpose is to reduce anchoring and self-confirmation; it does not create true model independence when the same underlying model is used.

The verifier writes the verification artefact and verifier handoff and publishes both through the dedicated evidence-PR contract in `WORKING_PROTOCOL.md` / `PR_GATE.md`. A branch-only verifier result is not a completed published result for canonical transition or cold-start routing. If the evidence PR cannot be published, verifier close is blocked/incomplete rather than silently leaving an undiscoverable "completed" result.

The verifier does not repair findings or use verifier authority to integrate its own result into canonical project state. After evidence-PR publication, a separate Integrator owns result validation/integration and the canonical transition below.

## Pending verifier-result discovery

During the intentional post-publication/pre-Integrator interval, canonical `STATE.md` may still assign the verifier role. `COLD_START.md` therefore applies its pending independent-result guard before a fresh session begins duplicate verification.

The guard may use the published evidence PR only to determine that an Integrator check is required. It may not reinterpret PASS / FAIL / NOT VERIFIED, treat PR metadata as proof, update canonical state, or select among conflicting/stale results. Those actions remain bounded by the Integrator preconditions and transition sequence below. Ambiguous, conflicting, stale, target-mismatched, or uninspectable same-WP evidence fails closed into bounded Integrator resolution rather than another verifier execution.

## Exact-target freshness

Every verification result remains permanently bound to the exact artefact/version/commit it inspected. A later result must never overwrite that historical binding.

A **material target change** makes the prior result stale for the changed target. Material target changes include edits to the design, implementation, acceptance criteria, authority rules, verification rules, or other acceptance inputs whose semantics the verifier evaluated.

Repository commits that only record or mechanically route an already-issued verification result do not retarget that result. They must be explicitly identifiable as **transition-only** changes and are checked by the integrator for conformity to the result-transition procedure below. Transition-only changes may:

- integrate the immutable verifier artefact and verifier handoff,
- record completion of the verification activity and its issued result,
- update canonical `STATE.md` to the result-dependent next responsibility,
- activate the result-required repair/review work package without changing the verified target's acceptance criteria,
- update explicitly subordinate navigational views and transition handoffs.

A transition-only commit does **not** become the commit certified by the verifier; the verification remains bound to the exact earlier target SHA. If a transition commit contains any substantive repair, design, acceptance, authority, or verification-rule change beyond the prescribed transition, the prior verification is stale for the changed target and fresh independent verification is required.

## Verifier-result → canonical-state transition

A completed verification does not become canonical project state merely because the verifier wrote a result or published an evidence PR. A separate **Integrator** owns this control-plane transition.

### Trigger and preconditions

The transition begins only when all of the following are available:

1. the verification WP/specification being executed;
2. a verifier artefact with PASS / FAIL / NOT VERIFIED;
3. a verifier handoff;
4. the exact target artefact/version/commit SHA;
5. the dedicated evidence PR targeting the active development branch;
6. enough repository/PR evidence to confirm that the verifier records correspond to that target and that no unreviewed material target change was smuggled into the verifier output branch/PR.

If the claimed target changed materially before verification closed, the integrator must not promote the result as current verification. The result may be integrated as historical evidence, but routing must preserve the stale/not-current condition and require fresh verification.

### Authorised integration sequence

The integrator performs these steps in order:

1. **Inspect the verifier output scope.** Confirm the verifier produced only authorised verification/session artefacts and did not perform repair or acceptance changes.
2. **Bind the result.** Record the exact target SHA and issued PASS / FAIL / NOT VERIFIED without reinterpretation.
3. **Integrate verifier evidence.** A dedicated verification branch/PR may be merged into the development line even when the target result is FAIL or NOT VERIFIED, provided the merge is only integrating verifier evidence. Evidence integration is not acceptance of the target.
4. **Close the verification activity.** Update the verification WP/status to record that the verification responsibility completed and what result it issued. Completion of the verification activity is distinct from the target being verified-complete.
5. **Transition canonical state.** Update `03_plan/STATE.md` from the prior verifier-required state to the result-dependent next responsibility.
6. **Route by result.** Apply the result table below without widening authority or weakening the parent acceptance criteria.
7. **Update subordinate views and leave an integrator handoff.** Any index/launch view must remain explicitly subordinate to `STATE.md` and the active WP.
8. **Check freshness after the transition.** Classify every post-target change as transition-only or material. Any material change reopens independent verification for the changed target.

### Result routing

- **PASS** → activate a separate adversarial-review responsibility when the parent WP requires it. PASS does not by itself accept the target, accept an ADR, satisfy a human-owner gate, or begin the next phase.
- **FAIL** → create or activate a bounded builder repair WP that references the exact findings and preserves the unchanged parent acceptance criteria. After material repair, activate a fresh verifier responsibility for the new exact target.
- **NOT VERIFIED** → create or activate the smallest bounded investigation/repair responsibility needed to resolve the verification blocker, then require fresh verification of the resulting exact target. NOT VERIFIED must not be treated as PASS or as evidence that the target failed semantically.

A repair/review WP created by the integrator is a routing artefact, not a hidden architecture decision. It may scope the next responsibility to the verifier's findings and existing controls; it may not prescribe substantive repair design beyond existing authority or change acceptance criteria merely to make the result pass.

### No-false-completion controls

The integrator may not:

- rewrite or soften the verifier's result,
- edit historical verifier evidence to make a failure disappear,
- use integration of verifier records as evidence that the target was accepted,
- perform substantive repair while claiming the commit is transition-only,
- waive an ADR or human-owner gate,
- route PASS directly to Phase acceptance when adversarial review or another gate remains,
- reuse a prior result to certify a materially changed target.

This transition is mechanical governance integration. Any unresolved architecture dispute exposed by the result follows `DECISION_POLICY.md`; the integrator cannot decide it merely to make state movement convenient.

## Analytical work

When a claim depends on calculation or data, verification must be able to inspect the relevant chain at a level appropriate to the risk: claim → computation → input data → source/version. Merely showing that real data or a tool was used does not prove the final claim was derived from it.

## Completion gate

A WP may be marked `verified-complete` only after every required acceptance criterion has a current PASS or an explicitly authorised exception. The working session that produced the artefact cannot grant this state to itself.

A verification-activity WP can separately be marked complete as an activity when it has correctly executed its own verification acceptance criteria, issued its result, and published the required evidence PR; that status must not be confused with the verified target's completion state.
