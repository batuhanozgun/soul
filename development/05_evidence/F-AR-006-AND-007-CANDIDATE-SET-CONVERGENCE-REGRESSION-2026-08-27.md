# F-AR-006/F-AR-007 Candidate-Set Convergence Regression Evidence

**Date:** 2026-08-27
**WP:** WP-017
**Role:** designer/builder
**Status:** producer evidence only — fresh independent verification and adversarial re-review required

## Objective and evidence boundary

Exercise the repository/key candidate-set convergence rule against immutable
WP-016 F-AR-006 and reconcile the executable decision model with the normative
current-valid-result precedence exposed by F-AR-007. Preserve F-AR-001 through
F-AR-005, exact freshness, conflict, fail-closed discovery/inspection and
Integrator-only canonical control authority.

This is producer evidence, not independent proof. It does not reinterpret
WP-015 **PASS**, WP-016 **Requires repair**, accept ADR-0002, merge a material
PR, accept Phase 0 or begin Phase 1.

## Observed repository and GitHub inputs

Re-read live before material work:

- canonical `origin/phase0/development-os`:
  `4524f21cced54c71fb2219b7f42119adbbb5b033`;
- draft PR #19: open/draft against `phase0/development-os`, exact immutable head
  `2f5508c1d6941e951d494bb2a700ef861860431d`, API base
  `dca520242585a80c2efaf22e18fe3d353147b93e`, exactly nine material files;
- PR #21: merged evidence-only from exact head
  `c2c44604ea1694bd84e34bed950e38efe557ff71` as
  `276132a8ad3bcaa5263aba725f6f006019f79287`, exactly the WP-016 review and
  SESSION-0028 handoff;
- canonical state preserves WP-015 **PASS** only for `2f5508c...` and WP-016
  **Requires repair** with F-AR-006 medium/material and F-AR-007
  low/evidence-model correctness;
- no WP-017 repair branch or PR existed before this builder responsibility.

The live public GitHub API and fetched immutable PR #19 commit were inspected
directly. PR metadata was treated as locator only; all nine target blobs and the
integrated two-file WP-016 evidence scope were read.

## Failure analysis

**F-AR-006 immediate cause:** moving-candidate containment binds repository +
PR number + complete active key. Each fresh PR number therefore starts a new
exact-head/stream lifecycle.

**F-AR-006 system cause:** recovery state was bounded at the mutable locator
identity while the independent responsibility and its complete key are
repository-level canonical facts. Lower-authority locator creation could reset
recovery without changing the canonical key.

**F-AR-007 immediate cause:** the producer decision table computed current and
invalid sets but routed uncontained invalid candidates before the single-current
branch.

**F-AR-007 system cause:** the executable evidence encoded control escalation as
the primary ordering instead of encoding the normative validity-first invariant
once for the complete candidate set. The declared tests omitted mixed
current-valid/uncontained-invalid states.

## Selected invariant

1. Every inspectable same-WP head is directly validated before invalid residue
   is routed.
2. Exactly one current-valid result routes to Integrator regardless of resolved,
   stream-contained, set-contained or uncontained invalid residue.
3. Multiple current-valid results remain conflict; no ordering or control
   selects one.
4. Exact-head resolution remains the first narrow response. A moved invalid
   head on the same PR may escalate once to PR-stream containment.
5. After an earlier canonical invalid-candidate control and a later directly
   inspected invalid candidate at a distinct PR identity under the same exact
   canonical repository and complete key, a separate Integrator may create one
   candidate-set containment:

   `(canonical repository, active WP, role, exact target, attempt)`.

6. Fresh PR/head/state/branch mutation cannot reset that set control. Every
   later inspectable head remains eligible for validity-first routing. Invalid
   or candidate-specifically inaccessible residue is contained non-valid,
   never accepted or treated as absent.
7. Wrong-key/repository, local, candidate-authored or malformed controls have no
   effect. A key change ends containment scope.
8. Repository-wide discovery failure and uncontained candidate inspection
   failure remain fail-closed.

## Alternatives considered

- **Resolve/contain each PR separately:** rejected because it reproduces
  F-AR-006 under unlimited fresh identities.
- **Blind repository/key ignore:** rejected because it can suppress a later
  current-valid result.
- **Freeze PR admission, trust authors or rate-limit host operations:** rejected
  because mutable host administration is not repository-only continuation and
  can block legitimate result publication.
- **Lease/lock or external registry:** rejected as a larger ownership, expiry,
  authority and recovery subsystem than the demonstrated failure requires.
- **Canonical repository/key candidate-set containment with validity-first
  override:** selected because it adds one final Integrator escalation at the
  failure-class identity while retaining direct head validation and canonical
  key authority.

## Deterministic model

Normal command:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: **67/67 PASS**.

The cases include all 28 prior producer routes plus:

- valid + first invalid, valid + moved invalid, valid + multiple fresh invalid,
  valid + inaccessible invalid and multiple-valid + invalid;
- uncontained inaccessible inspection failure;
- second invalid PR identity candidate-set escalation;
- 20 successive later fresh invalid PR identities that cannot reset recovery;
- later valid and multiple-valid states under candidate-set containment;
- set-contained candidate-specific inaccessibility;
- wrong-attempt, wrong-repository, local, candidate-authored and malformed
  same-PR candidate-set controls;
- unproven trigger/control rejection and foreign-repository candidate isolation;
- next-attempt isolation;
- preserved same-PR movement, later-valid, fixed-head, conflict, discovery
  outage and publication-timing cases.

Deliberate invalid-first mutation command:

`WP017_MUTATE_INVALID_FIRST=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: expected non-zero failure after **26 prior PASS** observations:

`valid plus first invalid routes current result: expected INTEGRATOR_RESULT, got INTEGRATOR_RESOLUTION`

The mutation is opt-in and absent from normal routing. It demonstrates that the
mixed-state regression fails red if F-AR-007 ordering is reintroduced.

The executable remains a routing decision-table model, not a GitHub transaction
test or independent verifier oracle.

## Red and falsification conditions

The producer claim is disproved if:

- a third or later fresh invalid PR identity demands another canonical control
  after valid candidate-set containment;
- candidate authors, local branches, mutable metadata or wrong repository/key
  controls can create, widen or reset containment;
- any inspectable current-valid result is routed after invalid residue;
- multiple current-valid results are selected instead of preserved as conflict;
- containment becomes validity, acceptance or absence;
- repository-wide discovery failure or uncontained inaccessibility fails open;
- a canonical key change inherits old candidate-set containment;
- historical F-AR-001 through F-AR-007 evidence or exact-target bindings change;
- the repair is treated as independently verified, ADR-accepted, merged or
  Phase-accepted by producer evidence.

## Limitations and fresh gates

- The model abstracts GitHub discovery and assumes a separate Integrator
  directly validates the triggering heads and canonical repository identity.
- Candidate-set containment is repository/key scoped, not a generic cross-host
  abuse-prevention system. No broader attack class is claimed closed without a
  demonstrated dependency and a new governed decision path.
- Candidate-specific inaccessibility after set containment is non-valid
  contained residue. Later inspectability always reopens direct validation.
- The existing post-final-check host edge remains explicit and is not converted
  into an atomic platform-lock claim.
- Fresh separate verification must inspect the exact new target, all current
  WP-000 criteria and F-AR-001 through F-AR-007. A later fresh separate
  adversarial re-review remains required.

## PR #19 relation

PR #19 is not amended or merged. Its exact target `2f5508c...`, WP-015 PASS and
WP-016 **Requires repair** remain immutable. WP-017 publishes one new
superseding draft material PR from canonical base `4524f21...`; its exact target
is frozen only after the final material commit is published.
