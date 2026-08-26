# PR GATE — PHASE 0 AND LATER WORK

A material PR is not accepted because its author says it is ready. Before merge, the integrator checks:

- [ ] Active WP exists and names this PR.
- [ ] Required outputs exist.
- [ ] Acceptance criteria are individually verifiable.
- [ ] Current independent verification exists for the exact reviewed target commit.
- [ ] Required adversarial review exists.
- [ ] Material findings are repaired and re-verified, or explicitly accepted through the decision policy.
- [ ] Required ADRs are present and in the correct status.
- [ ] `STATE.md` reflects the post-merge truth that will exist, not an aspirational future state.
- [ ] Session handoff identifies the next responsibility.
- [ ] No development-only artefact has been copied into `system/` without an accepted architecture reason.

If a checked condition becomes stale because the reviewed target changes materially, the relevant check is reopened.

## Verification/review evidence PRs

A dedicated verifier or reviewer PR is not the same object as the material target PR it evaluates.

### Publication contract

A verifier/adversarial-review result becomes a **completed published independent result** only when a dedicated evidence PR targets the active development branch and contains both:

- the completed verification/review artefact; and
- the corresponding role handoff.

The artefact and handoff must identify the active WP/independent role and exact target artefact/version/commit. The evidence PR title/body should expose the WP identifier and target for discovery, but those fields are locators only; direct changed-file and artefact inspection remains required.

The evidence PR must contain only authorised review/session evidence. A branch-only result, local draft, or evidence branch without the dedicated PR is not a completed published result for the `COLD_START.md` pending-result guard. If publication cannot be completed, the independent session is blocked/incomplete rather than silently leaving an undiscoverable completed result.

### Pending-result discovery and ambiguity

When canonical `STATE.md` still assigns an independent verifier/reviewer, `COLD_START.md` inspects evidence PRs targeting the active development branch before starting that role again.

For a candidate to route directly to a pending Integrator transition, direct inspection must establish:

- same active WP and independent role;
- same exact target required by the active WP;
- completed result artefact + handoff;
- evidence/session-only changed-file scope;
- no hidden repair, state/WP transition, acceptance, ADR, target-merge, or Phase change.

A same-WP candidate that is stale, target-mismatched, conflicting, incomplete, or cannot be proved evidence-only does not get silently ignored and does not get selected as truth. It blocks duplicate independent execution and routes to bounded Integrator freshness/conflict/publication resolution. Clearly unrelated historical evidence for another WP is ignored only after that mismatch is established.

This discovery path does not make the evidence PR canonical current-work state. `STATE.md` + active WP remain canonical until the Integrator validates the evidence and executes the authorised transition.

### Evidence integration

An integrator may merge a verification/review evidence PR into the development line even when the target result is FAIL or NOT VERIFIED when all of the following hold:

- the evidence PR is bound to an exact target artefact/version/commit;
- its changed-file scope contains only authorised review/session evidence, with no hidden repair or acceptance change;
- the result is preserved exactly rather than rewritten during integration;
- the merge is treated as evidence integration, **not** acceptance of the reviewed target;
- the result-dependent canonical-state transition is then executed under the applicable result-transition governance.

Post-result state/WP/index/handoff updates that are strictly the deterministic transition prescribed by current governance must be identifiable as transition-only. They do not retarget or rewrite the independent result. Any substantive design, repair, acceptance-criteria, authority, or verification-rule change is material and requires fresh verification for the changed target.
