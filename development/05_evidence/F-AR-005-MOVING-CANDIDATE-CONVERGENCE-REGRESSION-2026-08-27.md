# F-AR-005 Moving-Candidate Convergence Regression Evidence

**Date:** 2026-08-27
**WP:** WP-014
**Role:** designer/builder
**Status:** producer evidence only — fresh independent verification and
adversarial re-review required

## Objective and evidence boundary

Exercise the bounded moving-candidate convergence rule against the immutable
WP-013 F-AR-005 failure path while preserving the fixed-head, current-result,
conflict, outage and timing properties established for F-AR-001 through
F-AR-004. This record is not independent proof, does not reinterpret WP-012
**PASS** or WP-013 **Requires repair**, and does not accept ADR-0002 or the
repair.

## Observed repository and GitHub inputs

Re-read live before material work:

- canonical `origin/phase0/development-os`:
  `dca520242585a80c2efaf22e18fe3d353147b93e`;
- draft PR #16: open, base `phase0/development-os`, exact head
  `adf067e4289e4c0b51cf40c1940193e8252b22e0`, exactly eight declared material
  files;
- PR #18: merged evidence-only at head
  `2e78421f1c618995fe0cc0c8eb62104ecae63be1` as
  `fda9689107cf96ad2cc01e1b1bbe74b86055e771`, exactly the WP-013 review and
  SESSION-0022 handoff;
- no local or remote WP-014 repair branch and no open/closed WP-014 PR existed;
- canonical `STATE.md` and active WP-014 preserved WP-012 **PASS** only for
  `adf067e...`, WP-013 **Requires repair**, and F-AR-005 medium/material,
  stands.

Live PR metadata came from the public GitHub API and remote heads were checked
with `git ls-remote`. The immutable eight-file PR #16 blobs and WP-013 failure
trace were inspected directly.

## Failure analysis

**Immediate cause:** exact-head resolution intentionally expires whenever the
candidate PR head changes, while every unresolved invalid same-WP head blocks.

**System cause:** the control modeled only immutable candidate generations. It
had no canonical state for the bounded identity that persists across those
generations: repository + PR + complete active result-control key. A subordinate
locator could therefore reset recovery without changing canonical authority.

The repair retains exact-head resolution as the first, narrow response. After a
later invalid moved head is directly inspected, a separate Integrator may add
canonical moving-candidate containment for that stream identity. Subsequent
candidate mutation cannot reset that state.

## Selected invariant

1. A first invalid fixed head requires direct inspection and exact-head
   resolution.
2. A moved head is inspected anew. If it is invalid under the same complete key,
   routing escalates once to canonical movement containment.
3. Containment is bound to repository + PR + WP + role + exact target + attempt;
   only a separate Integrator can create or correct it.
4. Every inspectable later head is still validated. Current-valid bypasses
   containment and routes to Integrator; multiple current-valid remains a
   conflict.
5. Inspectable-invalid later generations and candidate-specific inaccessible or
   deleted heads are explicit contained non-valid states and do not require
   another canonical resolution.
6. A later inspectable corrected head is not hidden. A changed canonical key does
   not inherit old containment.
7. Repository-wide discovery failure remains fail-closed; containment cannot
   manufacture absence, validity, acceptance or canonical transition.

## Alternatives considered

- **Keep resolving every exact head:** rejected because it reproduces F-AR-005.
- **Blindly ignore/freeze the PR identity:** rejected because it can suppress a
  later corrected current-valid head.
- **Trust selected authors/branches:** rejected because authorised producers can
  still mutate accidentally or after compromise, and host identity policy is
  not the control property.
- **Lease/lock:** rejected as a larger authority, expiry and stale-lock subsystem
  than the observed failure requires.
- **Canonical stream containment with validity override:** selected because it
  adds one bounded Integrator escalation, cannot be reset by candidate mutation,
  and keeps every later valid head eligible.

## Deterministic model

Command:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: **28/28 PASS**.

The passing cases cover:

- PR #14/#15-shaped current-result routing;
- one unresolved and one canonically resolved fixed invalid head;
- the first moved invalid head escalating to containment;
- invalid generations 3 through 12 remaining contained, extending beyond the
  reviewer's five-generation trace;
- a later corrected current-valid head on the same contained PR routing to
  Integrator;
- a contained closed/inaccessible/deleted-fork-shaped head remaining non-valid
  without resetting recovery;
- malformed fixed-head recovery;
- exact-head resolution and containment both failing to suppress a valid current
  result;
- multiple-valid conflict preservation;
- another-WP isolation;
- repository-wide discovery outage remaining blocked;
- wrong-attempt and wrong-repository containment having no effect;
- publication between initial and final checks routing to Integrator.

The executable is a routing decision-table model, not a GitHub transaction test.

## Red and falsification conditions

The producer claim is disproved if:

- containment can be created for a first invalid or uninspected moved head;
- a candidate author can create/reset containment or a PR/head mutation clears
  it under the same active key;
- a valid later head is skipped, excluded or treated as contained;
- a wrong WP/role/target/attempt containment unblocks work;
- a contained invalid generation still requires unbounded canonical resolution
  commits;
- multiple current results are selected rather than preserved as conflict;
- global discovery failure is treated as containment or no candidate;
- historical WP-012/WP-013 exact-target bindings or F-AR-001 through F-AR-005
  wording are changed;
- the repair is treated as verified, ADR-accepted, merged or Phase-accepted by
  producer evidence.

## Limitations and fresh gates

- The model abstracts GitHub responses and assumes the Integrator directly
  validates the two triggering invalid heads before canonical containment.
- Candidate-specific inaccessibility after containment is intentionally a
  contained non-valid state. It is not proof of absence or validity; later
  inspectability and validity must route normally.
- The existing publication-after-final-check host edge remains explicit and is
  not converted into a platform lock claim.
- The mechanism bounds repeated movement of the same candidate identity. A
  broader many-PR flooding attack is an ADR reopen condition, not silently
  claimed closed here.
- Fresh verification must inspect the exact new target, live PR scope, canonical
  activation and all current WP-000/F-AR-001–005 obligations. Fresh separate
  adversarial re-review remains required afterward.
