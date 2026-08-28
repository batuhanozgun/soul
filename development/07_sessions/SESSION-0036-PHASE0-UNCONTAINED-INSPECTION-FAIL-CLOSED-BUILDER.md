# SESSION-0036 — Phase 0 Uncontained Inspection Fail-Closed Builder

**Date:** 2026-08-28
**Work package:** WP-020 — Phase 0 Uncontained Inspection Fail-Closed Repair
**Role performed:** fresh recovery designer/builder
**Canonical development branch:** `phase0/development-os`
**Canonical start:** `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`
**Material branch:** `codex/wp020-uncontained-inspection-fail-closed-repair`
**Material PR:** #26 — `WP-020: fail closed on uncontained inspection unknowns`
**Exact material target:** `a42101cfc7fef58ac169150458ff3f889f10527b`
**Material base:** `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`
**Builder-close routing branch:** `codex/wp020-builder-close-routing`
**Builder-close preparation commit:** pending first routing commit
**Builder-close routing PR:** pending publication
**Proposed next WP:** WP-021 — Phase 0 Uncontained Inspection Fail-Closed Verification
**Proposed result-control key:** `WP-021 / verifier / a42101cfc7fef58ac169150458ff3f889f10527b / attempt 1`

## Entry, recovery and authority

The session recovered after a host crash in the isolated clone
`/private/tmp/soul-wp020-builder.idxw2v/repo`. It did not inspect or modify the
dirty root `/Users/Batu/SOUL`, its local changes or `.DS_Store`.

Before mutation, recovery inspected branch/status, index/worktree differences,
commit ancestry and live GitHub state. HEAD was exact canonical `c4ebef9...`.
The index contained byte-identical copies of all ten PR #22 material blobs and
the worktree contained a coherent six-file F-AR-008 draft. No recovered change
was discarded or silently redesigned.

The session then entered through canonical `COLD_START.md`: `STATE.md`, active
WP-020, `SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, common
`REASONING_POLICY.md`, designer/builder role/decision/change governance, all
foundation files and the complete WP-required evidence chain. Live PR #22/#25
metadata, exact heads/scopes, immutable PR #22 material, all producer records,
model/template and WP-018/WP-019 result history were directly inspected.

The sole responsibility was the smallest coherent F-AR-008 repair, one exact
material target, producer evidence and routing to fresh separate verification.
No independent verification, adversarial re-review, candidate control, attempt
advancement, result integration, ADR acceptance, material merge, Phase
acceptance or Phase 1 work was performed.

## Failure analysis and proposed architecture

**Immediate cause:** PR #22 routes one visible current-valid result before an
uncontained uninspectable same-scope candidate.

**System cause:** normative and executable controls collapsed directly proven
invalid, validly resolved/contained non-valid and epistemically unknown
uninspectable candidates into one non-current/invalid-residue class.

The selected invariant classifies the complete discovered set before routing:

1. repository-wide discovery failure blocks;
2. any uncontained uninspectable same-scope candidate blocks before visible
   result/conflict routing;
3. with no unknown, multiple current-valid results remain conflict;
4. exactly one current-valid result then routes before directly inspected
   invalid or exactly resolved/contained non-valid residue.

Every inspectable head remains directly validated. Existing exact-head,
moving-stream and repository/key candidate-set controls remain canonical-before-
use and Integrator-only. No new authority or control type was added.

A route-specific exception, visible-result-first handling, permanent blocking
of validly contained inaccessibility and a new lease/lock/control plane were
rejected as respectively incomplete, the exact failure, regression-causing or
larger than the demonstrated classification/order defect.

## Material output

Draft PR #26 is open/draft against `phase0/development-os` at exact head
`a42101cfc7fef58ac169150458ff3f889f10527b`, exact base `c4ebef9...`, with
exactly eleven files:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/F-AR-005-MOVING-CANDIDATE-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/F-AR-008-UNCONTAINED-INSPECTION-FAIL-CLOSED-REGRESSION-2026-08-28.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

The material commit changes no foundation file, WP-000 criterion, canonical
STATE/WP, immutable review/verification record, session record or `system/`
content. ADR-0002 remains proposed.

## PR #22 relation

PR #26 was published and live-validated before PR #22 was superseded. PR #22's
body/head were not amended; it received an explicit supersession comment and
was closed unmerged at immutable head `5bd0db27...`, base `4524f21...`, with
ten files. WP-018 **PASS**, WP-019 **Requires repair** and F-AR-008 remain
permanently bound only to that target.

## Producer evidence and audits

Normal command:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: **84/84 PASS**.

Preserved F-AR-007 mutation:

`WP017_MUTATE_INVALID_FIRST=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: exit 1/red after **26 PASS** observations at the valid-over-directly-
invalid boundary.

F-AR-008 mutation:

`WP020_MUTATE_UNKNOWN_AFTER_RESULT=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: exit 1/red after **30 PASS** observations at visible-valid plus
uncontained unknown.

`git diff --check c4ebef9... a42101c...` passed. Commit/base ancestry, exact
eleven-file scope, prior PR #22 blob preservation, canonical history and live
remote/pull refs were audited. These are builder checks and producer evidence,
not independent verification.

## Builder-close routing output and separation

The `codex/wp020-builder-close-routing` branch records WP-020 builder output,
proposes the complete WP-021 verifier specification/key/bridge and adds this
SESSION-0036 handoff. It changes neither canonical `STATE.md` nor subordinate
`WORKSPACE_INDEX.md`. Canonical activation/binding is a separate Integrator
responsibility.

The routing PR must contain exactly:

- `development/04_work/WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`;
- `development/04_work/WP-021-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-VERIFICATION.md`;
- this SESSION-0036 handoff.

The only post-publication routing-branch change permitted is a locator update
inside this same handoff. The Integrator must validate the final branch/PR scope,
integrate only these three builder-close records if exact, then separately
update canonical state/index and activate/bind WP-021.

## Decisions

ADR-0002 is revised only as **proposed** architecture on PR #26. No ADR was
accepted or rejected. The PR #22 -> PR #26 supersession and epistemic
classification/order repair are builder design/output claims pending independent
gates.

## Verification and review status

- WP-018 PASS and WP-019 **Requires repair** remain exact only for
  `5bd0db27...` and their recorded activation/bindings;
- no independent verification or adversarial re-review exists for
  `a42101c...`;
- PR #26, ADR-0002, WP-000 and Phase 0 remain unaccepted/unmerged.

## Unresolved items

- separate Integrator validation/integration and exact WP-021 activation/binding;
- fresh exact-target verification, separate result integration and fresh
  adversarial re-review;
- repair or authorised resolution of any later surviving material finding;
- ADR-0000/0001/0002, PR #26/#1, human/PR/Phase gates;
- Phase 1 remains blocked.

## Exact next required responsibility

**Fresh separate Integrator.**

Cold-read canonical state and governance; revalidate live PR #26 target/base/
eleven-file scope, PR #22 supersession and the exact builder-close routing PR.
Integrate only WP-020, proposed WP-021 and this SESSION-0036 record if scope is
exact. Then canonically activate/bind WP-021 and dispatch a fresh verifier.

The Integrator must not verify or adversarially review the target, reinterpret
historical results, accept ADR-0002, merge PR #26/#1, accept Phase 0 or begin
Phase 1.
