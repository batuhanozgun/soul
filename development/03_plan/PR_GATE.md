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

An integrator may merge a verification/review evidence PR into the development line even when the target result is FAIL or NOT VERIFIED when all of the following hold:

- the evidence PR is bound to an exact target artefact/version/commit;
- its changed-file scope contains only authorised review/session evidence, with no hidden repair or acceptance change;
- the result is preserved exactly rather than rewritten during integration;
- the merge is treated as evidence integration, **not** acceptance of the reviewed target;
- the result-dependent canonical-state transition is then executed under `VERIFICATION_POLICY.md`.

Post-result state/WP/index/handoff updates that are strictly the deterministic transition prescribed by `VERIFICATION_POLICY.md` must be identifiable as transition-only. They do not retarget or rewrite the verifier's exact result. Any substantive design, repair, acceptance-criteria, authority, or verification-rule change is material and requires fresh verification for the changed target.
