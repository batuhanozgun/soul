# F-AR-008 Uncontained Inspection Fail-Closed Regression Evidence

**Date:** 2026-08-28
**WP:** WP-020
**Role:** designer/builder
**Status:** producer evidence only — fresh independent verification and
adversarial re-review required

## Objective and evidence boundary

Exercise the bounded F-AR-008 repair without weakening the historical
F-AR-001 through F-AR-007 controls. The model must distinguish directly
inspected invalid residue, exactly resolved or validly contained non-valid
residue, and an uncontained candidate whose immutable head or required records
cannot be inspected. The last class is epistemically unknown and must block in
every mixed state because it may conceal another current-valid result.

This record is producer evidence, not independent proof. It does not reinterpret
WP-018 **PASS** or WP-019 **Requires repair**, accept ADR-0002, merge a material
PR, accept Phase 0 or begin Phase 1.

## Observed repository and GitHub inputs

Re-read live before continuing the recovered builder work:

- canonical `origin/phase0/development-os` and the isolated recovery base:
  `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`;
- draft PR #22: open/draft/unmerged against `phase0/development-os`, exact head
  `5bd0db27fc3df368c9e112f01b7eed49a64402ab`, API and merge base
  `4524f21cced54c71fb2219b7f42119adbbb5b033`, four commits, ten material files,
  mergeable/clean;
- PR #25: merged evidence-only from final head
  `16b5aacb12d05157e183cb9257025f30636e0f71` as
  `8022ca6fb30fc32e6a95f22c5c1d58c5ab8c1745`, exactly the WP-019 review and
  SESSION-0034 handoff;
- canonical state preserves WP-018 **PASS** and WP-019 **Requires repair** only
  for `5bd0db27...`; F-AR-008 medium/material stands;
- the recovered index contains byte-identical copies of all ten PR #22 material
  blobs, while the recovered worktree changes only the bounded F-AR-008
  governance/model surfaces before this evidence record.

The live public GitHub API, fetched immutable Git objects, index/worktree diffs
and commit ancestry were inspected directly. PR metadata remained locator-only
and was not used as result validity evidence.

## Failure analysis

**Immediate cause:** PR #22 routes exactly one visible current-valid result
before checking for an uncontained uninspectable same-scope candidate.

**System cause:** the decision model and normative prose collapse all
non-current candidates into one invalid-residue class. An inaccessible locator
therefore inherits an invalidity classification that direct evidence never
established.

The repair changes classification and ordering, not authority. Every inspectable
head is still directly validated. Existing exact-head resolution, moving-stream
containment and repository/key candidate-set containment remain the only bounded
recovery controls and remain canonical-before-use and Integrator-only.

## Selected invariant

After successful repository-wide discovery:

1. directly inspect every available same-scope head;
2. classify current-valid, directly inspected invalid, exactly resolved or
   validly contained non-valid, and uncontained uninspectable separately;
3. if any uncontained uninspectable candidate remains, return
   `BLOCKED_INSPECTION` before result/conflict routing;
4. otherwise preserve multiple-current conflict, then route exactly one
   current-valid result before directly proven invalid or resolved/contained
   non-valid residue;
5. locator metadata, prior invalidity at a different head and the presence of a
   visible result never prove an inaccessible candidate non-valid;
6. later inspectability always reopens direct validation, producing conflict if
   the formerly unknown candidate validates and preserving sole-result routing
   if it is directly invalid;
7. repository-wide discovery failure always returns `BLOCKED_DISCOVERY` and
   cannot be covered by candidate-specific control.

## Alternatives considered

- **Special-case only visible-valid plus inaccessible:** rejected because it
  leaves the invalid/unknown state collapse in other consumers and mixtures.
- **Route visible validity before every blocker:** rejected because it is the
  F-AR-008 failure path and can suppress a second current result.
- **Treat every inaccessible candidate as blocking forever:** rejected because
  it would discard valid exact-head/stream/set controls and revive the bounded
  convergence failures repaired for F-AR-003/F-AR-005/F-AR-006.
- **Add a new lock, lease or authority record:** rejected as unnecessary. The
  existing controls already establish when candidate-specific inaccessible
  residue is bounded non-valid; only classification/order was wrong.
- **Three-way epistemic classification with unknown-before-result routing:**
  selected as the smallest repair that matches the evidence boundary.

## Deterministic producer suite

Normal command:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: **84/84 PASS**. Exact producer model SHA-256:
`1ed364080e2c78fd21597eebbbdae8611f02cdb5ffef8ffe56294b83429d8f6f`.

The retained cases cover every historical F-AR-001 through F-AR-007 producer
route. The WP-020 boundary cases additionally cover:

- visible valid plus uncontained unknown;
- unknown alone, directly proven invalid plus unknown and two visible valid plus
  unknown;
- a current-looking locator whose head/records remain inaccessible;
- exact same-head resolution versus wrong-head, wrong-key and unproven
  resolution records;
- later-inspectable valid and invalid outcomes;
- repository-wide outage despite visible validity;
- stream-contained and set-contained inaccessible non-valid residue;
- an uncontained unknown coexisting with contained inaccessible residue;
- foreign-repository and another-WP inaccessible candidates outside the exact
  candidate scope.

## Red-capable mutations

Historical precedence mutation:

`WP017_MUTATE_INVALID_FIRST=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: exit 1/non-zero red after **26 PASS** observations at
`valid plus first invalid routes current result`. This preserves the F-AR-007
valid-over-proven-invalid boundary.

F-AR-008 mutation:

`WP020_MUTATE_UNKNOWN_AFTER_RESULT=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Observed result: exit 1/non-zero red after **30 PASS** observations at
`visible valid plus uncontained unknown fails closed`. This causally demonstrates
that moving unknown routing after sole-result routing breaks the repaired
boundary.

## Red and falsification conditions

The producer claim is disproved if:

- any uncontained same-scope uninspectable candidate is treated as invalid,
  absent, resolved or contained without the exact canonical proof;
- one or more visible current-valid results route while such an unknown remains;
- a wrong-head, wrong-key, unproven, local or candidate-authored control unblocks
  the unknown;
- a directly inspected invalid or validly resolved/contained non-valid residue
  suppresses exactly one current-valid result;
- a formerly unknown later-valid candidate does not expose conflict;
- repository-wide discovery outage is covered by candidate containment;
- fixed-head, same-PR or cross-PR convergence, direct validation, exact
  repository/key identity, Integrator authority or historical result bindings
  regress;
- producer evidence is presented as independent verification or target/ADR/PR/
  Phase acceptance.

## Limitations and fresh gates

- The executable is a routing decision-table model, not a GitHub transaction
  test and not an independent verifier oracle.
- It assumes candidate discovery already established exact repository and
  same-WP scope; live result validity still requires direct artefact, handoff,
  immutable-head and changed-file inspection.
- The existing post-final-check host edge remains explicit and is not converted
  into an atomic lock claim.
- Fresh separate verification must inspect the exact new target, all current
  WP-000 criteria and explicit F-AR-001 through F-AR-008 regression. Fresh
  separate adversarial re-review remains required after result integration.

## PR #22 relation

PR #22 is not amended or merged. Its exact target `5bd0db27...`, WP-018
**PASS** and WP-019 **Requires repair**/F-AR-008 remain immutable. WP-020 will
publish one new superseding draft material PR from canonical base `c4ebef9...`;
the exact target is frozen only after the final material commit is published.
