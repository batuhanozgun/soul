# PR GATE — PHASE 0 AND LATER WORK

A material PR is not accepted because its author says it is ready. Before merge, the integrator checks:

- [ ] Active WP exists and names this PR.
- [ ] Required outputs exist.
- [ ] Acceptance criteria are individually verifiable.
- [ ] Current independent verification exists for the exact reviewed commit.
- [ ] Required adversarial review exists.
- [ ] Material findings are repaired and re-verified, or explicitly accepted through the decision policy.
- [ ] Required ADRs are present and in the correct status.
- [ ] `STATE.md` reflects the post-merge truth that will exist, not an aspirational future state.
- [ ] Session handoff identifies the next responsibility.
- [ ] No development-only artefact has been copied into `system/` without an accepted architecture reason.

If a checked condition becomes stale because the branch changes materially, the relevant check is reopened.
