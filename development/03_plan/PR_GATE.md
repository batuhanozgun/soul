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

### Publication and result-control binding

A completed published verifier/reviewer result requires a dedicated evidence PR targeting the active development branch and containing exactly the completed result artefact plus corresponding handoff. Both records bind the complete active result-control key: WP, independent role, exact target and attempt number.

PR metadata is a locator only. Current-result validation requires direct inspection of both records, immutable PR head SHA and changed-file scope. A local/branch-only result or an evidence PR with repair, state/WP transition, acceptance, ADR, target-merge or Phase changes is not a current valid result.

`COLD_START.md` checks candidates after canonical state discovery and repeats the live check immediately before independent-role commitment. Discovery/inspection failure fails closed.

### Durable candidate resolution and moving-candidate containment

An Integrator exact-head resolution can stop repeated routing only for one exact
candidate identity: repository + PR number + immutable PR head SHA. The
canonical record also contains expected and observed result-control keys,
classification, changed-file inspection, evidence, Integrator session and
canonical integration commit.

- a record is effective only after it exists on the canonical development branch;
- a moved head invalidates exact-head resolution for the new head;
- after one resolved invalid head and one later directly inspected invalid moved
  head under the same complete active key, a separate Integrator may canonically
  create moving-candidate containment bound to repository + PR + that exact key;
- canonical containment survives later head, branch and open/closed state
  movement, so inspectable-invalid or candidate-specifically inaccessible later
  heads cannot demand an unbounded series of canonical resolutions;
- every inspectable later head is still directly validated; a current valid head
  bypasses containment and routes normally, and multiple current valid results
  remain a conflict;
- a first invalid head, global discovery outage or uncontained uninspectable
  candidate cannot be converted directly into containment;
- closing/merging a candidate does not itself resolve or contain it;
- a candidate that validates as a current result cannot be excluded by a resolution record;
- multiple current valid results remain a conflict and require a fresh canonically routed attempt/key rather than arbitrary selection;
- unavailable repository-wide discovery remains blocked until available.

Resolution and containment records are subordinate evidence for bounded routing.
They do not replace `STATE.md` + the active WP, reinterpret results, accept a
target, or grant verifier/reviewer self-transition authority. A key change ends
the scope of prior containment; only a canonical Integrator can create or
correct it.

### Provisional self-hosting activation

When the general guard is still proposed/unmerged, the exact verification/re-review WP may contain a WP-local activation bridge as permitted by `WORKING_PROTOCOL.md`. The Integrator must verify that the bridge is canonically active before the independent role starts, is scoped to one exact key/activation commit, preserves COLD_START Steps 1–2, requires the final live re-check, and is explicitly classified as provisional material rollout control rather than accepted general governance or a transition-only change.

An integrator may merge a verification/review evidence PR into the development line even when the target result is FAIL or NOT VERIFIED when all of the following hold:

- the evidence PR is bound to an exact target artefact/version/commit;
- its changed-file scope contains only authorised review/session evidence, with no hidden repair or acceptance change;
- the result is preserved exactly rather than rewritten during integration;
- the merge is treated as evidence integration, **not** acceptance of the reviewed target;
- the result-dependent canonical-state transition is then executed under `VERIFICATION_POLICY.md`.

Post-result state/WP/index/handoff updates that are strictly the deterministic transition prescribed by `VERIFICATION_POLICY.md` must be identifiable as transition-only. They do not retarget or rewrite the verifier's exact result. Any substantive design, repair, acceptance-criteria, authority, or verification-rule change is material and requires fresh verification for the changed target.
