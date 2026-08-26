# F-AR-001–F-AR-004 Pending-Result Control Regression Evidence

**Date:** 2026-08-26  
**WP:** WP-011  
**Role:** designer/builder  
**Status:** producer evidence only — fresh independent verification and adversarial re-review required

## Objective and evidence boundary

Exercise the revised result-control state machine against the real PR #14/#15 close intervals and the stale/malformed/conflict/discovery/timing cases required by WP-011. This record is not independent verification and does not accept ADR-0002 or the repair.

## Observed repository/GitHub inputs

Re-read on 2026-08-26 before material work:

- canonical local and live remote `phase0/development-os`: `8dcdc750600b336a2e97fde3433926b6a2217f26`;
- rejected PR #13: open/draft, base `phase0/development-os`, head `a45b463b083604d3f59d75bdca5ba97d5bc170e6`, six declared repair files;
- verifier PR #14: closed/merged, exact evidence head `814e58860fe3ea623e9394f35db4674d60aec80d`, merge `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`, exactly verifier artefact + SESSION-0015;
- reviewer PR #15: closed/merged, exact evidence head `51fcdd0a23c467749f17381898602dd643e2ad6c`, merge `c8fc17bc50ca04893cc6a87e492408c078c79311`, exactly review artefact + SESSION-0017;
- canonical `COLD_START.md` at that head contains no pending-result guard, reproducing the activation premise in F-AR-002;
- immutable WP-010 review preserves F-AR-002/F-AR-003/F-AR-004 and overall `Requires repair` for `a45b463...`.

The live metadata was inspected directly through the authenticated GitHub connector; exact remote refs were independently re-read with `git ls-remote`.

## Revised invariant

For an active independent WP:

1. canonical WP/role/target/attempt form one result-control key;
2. evidence artefact and handoff must match the complete key and evidence-only scope;
3. discovery runs after Step 1 and again immediately before independent-role commitment;
4. an invalid historical candidate can stop blocking only through a canonical Integrator resolution bound to its exact PR head SHA;
5. head movement invalidates the old resolution;
6. a validating current result cannot be excluded;
7. multiple current results remain a conflict and route a fresh canonical attempt;
8. discovery/inspection unavailability remains blocked;
9. while general governance remains proposed, the active verification/re-review WP carries a key-bound provisional activation bridge.

## Deterministic model

Command executed from the material worktree:

`python3 development/05_evidence/pending_result_control_regression.py`

Observed output:

```text
PASS PR14 post-result interval: INTEGRATOR_RESULT
PASS PR15 post-result interval: INTEGRATOR_RESULT
PASS unresolved stale head: INTEGRATOR_RESOLUTION
PASS canonically resolved exact stale head: INDEPENDENT
PASS head movement reopens inspection: INTEGRATOR_RESOLUTION
PASS malformed candidate: INTEGRATOR_RESOLUTION
PASS resolved exact malformed head: INDEPENDENT
PASS resolution cannot suppress valid current result: BLOCKED_INVALID_RESOLUTION
PASS multiple valid results preserved as conflict: INTEGRATOR_CONFLICT
PASS another-WP history: INDEPENDENT
PASS discovery unavailable: BLOCKED_DISCOVERY
PASS initial check before publication: INDEPENDENT
PASS final re-check after publication: INTEGRATOR_RESULT
```

The executable is a routing decision-table model, not a GitHub integration test. An independent verifier must inspect the live candidates, canonical blobs and activation commit directly.

## Finding trace

### F-AR-001 — completed pending result

PR #14/#15-shaped one-current-result inputs route to Integrator rather than repeat independent execution. Evidence metadata remains subordinate and direct content/scope validation remains required.

### F-AR-002 — safe activation during this repair's own gates

The general `COLD_START.md` change remains only on the unaccepted material PR. Builder close therefore routes fresh verification through a canonical active WP containing a provisional, exact-key activation bridge. The bridge preserves COLD_START Steps 1–2, runs candidate handling at the end of Step 3 and repeats the live check immediately before Step 4 commitment. Its canonical activation commit is recorded separately in the builder handoff and must be inspected by the verifier. This is explicit temporary rollout control, not acceptance/merge of general governance.

Expected observable close state: after the verifier publishes its key-bound evidence PR but before an Integrator transition, a generic fresh session reads the still-active verification WP, executes its bridge and routes to Integrator. The later adversarial-review WP must use the same bridge pattern until general governance is accepted.

### F-AR-003 — bounded stale/malformed recovery

- unresolved stale/malformed candidate → Integrator resolution;
- canonical exact-head resolution → later independent execution may proceed;
- moved head → old resolution no longer applies;
- forged resolution against a valid current candidate → blocker, not suppression;
- multiple valid current results → preserved conflict and fresh canonical attempt.

Closing or merging a candidate alone has no exclusion effect. Uninspectable/discovery-unavailable candidates cannot be resolved by assertion.

### F-AR-004 — publication timing

The model executes an initial no-result check, introduces a current result during Steps 2/3, and observes `INTEGRATOR_RESULT` at the mandatory final check. No substantive action may occur between that check and role commitment.

Residual boundary: the host supplies no atomic transaction joining PR publication to a model session's first action. Publication after the final check can still race; the repair explicitly narrows the window to that immediate edge and preserves later conflict handling. A platform-native transaction/lease is a reopen condition.

## Red/falsification conditions

The producer claim is disproved if any of the following occurs:

- the canonical verification/review WP lacks the activation bridge while general governance remains unmerged;
- a generic session can reach independent work without the final live check;
- a resolution without exact PR head identity unblocks work;
- an old resolution still applies after head movement;
- a current valid result is excluded;
- multiple valid results are arbitrarily selected;
- discovery failure is treated as no candidate;
- the active key is derived from PR metadata instead of the active WP;
- bridge/routing changes are mislabelled transition-only or treated as general-governance acceptance.

## Limitations and required independent work

- The model does not prove agent compliance, GitHub availability or semantic correctness of a future Integrator classification.
- The WP-local bridge intentionally duplicates only the temporary rollout control and must be compared byte-for-semantics with the proposed general rules.
- The final-check residual edge is bounded, not eliminated by a platform transaction.
- Fresh verification must cover all WP-000 criteria plus F-AR-001–004, the exact material target, exact activation commit and live PR state.
- Fresh adversarial re-review must attack forged resolutions, moved heads, attempt confusion, bridge drift and the residual timing edge.
