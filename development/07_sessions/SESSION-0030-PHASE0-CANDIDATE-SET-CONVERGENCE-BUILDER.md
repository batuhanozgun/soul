# SESSION-0030 — Phase 0 Candidate-Set Convergence Builder

**Date:** 2026-08-27
**Work package:** WP-017 — Phase 0 Candidate-Set Convergence Repair
**Role performed:** fresh separate designer/builder
**Canonical development branch:** `phase0/development-os`
**Canonical start:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Material branch:** `codex/wp017-candidate-set-convergence-repair`
**Material PR:** #22 — `WP-017: bound candidate-set convergence and restore result precedence`
**Exact material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Builder-close routing branch:** `codex/wp017-builder-routing`
**Builder-close routing PR:** publication locator pending
**Proposed next WP:** WP-018 — Phase 0 Candidate-Set Convergence Verification
**Proposed result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`

## Entry and authority

The session used a new clean isolated clone based directly on live
`origin/phase0/development-os` at exact `4524f21...`. It did not use or modify
the dirty root `/Users/Batu/SOUL`, its divergent commits, uncommitted files or
`.DS_Store`.

The session entered through canonical `development/03_plan/COLD_START.md` and
completed Steps 1–2 in order: `STATE.md`, active WP-017,
`SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, common `REASONING_POLICY.md`, then
designer/builder `ROLE_MODEL.md`, `DECISION_POLICY.md` and `CHANGE_POLICY.md`.
It declared one responsibility: produce the smallest coherent F-AR-006/F-AR-007
repair and one new exact material target, then stop for separate gates.

Step 3 read all foundation files, WP-000, immutable WP-016 review and
SESSION-0028, WP-014/WP-015/WP-016, exact PR #19 diff/all nine blobs, exact PR
#21 two-file scope/evidence merge, SESSION-0027/0029, all required governance
and gates, proposed ADR-0002, both prior producer evidence records, exact model
and control template.

Live GitHub inspection confirmed PR #19 open/draft at exact `2f5508c...` from
`dca520...` with nine files before repair; PR #21 merged evidence-only from
exact `c2c4460...` as `276132a8...` with two files; canonical remote remained
`4524f21...`; and no pre-existing remote WP-017 repair branch existed.

This session performed only designer/builder work. It did not independently
verify or adversarially review the target, integrate an independent result,
resolve/contain a live candidate, advance an attempt, accept an ADR, merge a
material PR, accept Phase 0 or begin Phase 1.

## Failure analysis and proposed architecture

**F-AR-006 immediate cause:** recovery was bounded per repository + PR + key,
so each fresh PR identity restarted exact-head and stream containment.

**F-AR-006 system cause:** the recovery identity was narrower than the
repository-level canonical responsibility/key. Lower-authority locator creation
could reset control without changing canonical work.

**F-AR-007 immediate cause:** the executable model routed uncontained invalid
residue before its single-current branch.

**F-AR-007 system cause:** the evidence model privileged escalation order over
the normative candidate-set validity invariant and omitted mixed-state tests.

The selected proposed repair keeps exact-head resolution and same-PR stream
containment as narrow first responses. After an earlier canonical
invalid-candidate control and a later directly inspected invalid candidate at a
distinct PR identity, a separate Integrator may create candidate-set
containment bound to:

`(exact canonical repository, active WP, role, exact target, attempt)`.

Fresh PR/head/state/branch mutation cannot reset that control. Every inspectable
head remains directly validated before invalid residue: one current-valid result
routes to Integrator, multiple current-valid results remain conflict, and only
invalid or candidate-specifically inaccessible residue is contained non-valid.
Repository-wide discovery and uncontained candidate inspection failures remain
fail-closed.

Resolving every PR, blind repository/key ignore, host admission/freeze/rate
policy, author trust and lease/lock/external-registry mechanisms were rejected
as respectively non-convergent, suppressive or larger/more host-dependent than
the demonstrated failure requires.

## Material output

Draft PR #22 is open/draft against `phase0/development-os` at exact head
`5bd0db27fc3df368c9e112f01b7eed49a64402ab`, exact base `4524f21...`, with
exactly ten files:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/F-AR-005-MOVING-CANDIDATE-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

Material commits are `18b4ad3`, `e375967`, `2622d13` and exact target
`5bd0db2`. The two prior producer evidence records are byte-identical to PR #19.

## PR #19 relation

PR #19 was not amended or merged. Its body received an explicit supersession
locator and it was closed unmerged at immutable head `2f5508c...`, base
`dca520...`, with the same nine files. WP-015 PASS, WP-016 **Requires repair**
and F-AR-006/F-AR-007 remain permanently bound only to that target. PR #22 is
the sole new WP-017 material candidate.

## Producer evidence

Normal command:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: **67/67 PASS**.

The suite preserves all prior routes and covers the required mixed states, one
uncontained inspection outage, candidate-set trigger, 20 successive fresh
invalid PR identities, later-valid/conflict, exact key/repository/authority
negatives, global discovery outage and timing.

Deliberate mutation command:

`WP017_MUTATE_INVALID_FIRST=1 PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: expected non-zero/red after 26 prior PASS observations at `valid plus
first invalid`: expected `INTEGRATOR_RESULT`, got `INTEGRATOR_RESOLUTION`.

`git diff --check 4524f21... 5bd0db2...` passed. Producer evidence is not
independent verification.

## Builder-close routing output and separation

The `codex/wp017-builder-routing` branch records WP-017 builder output, proposes
the complete WP-018 verifier specification/key/bridge and adds this SESSION-0030
handoff. This builder does not change canonical `STATE.md` or the subordinate
index. Canonical activation/binding is a separate Integrator responsibility.

The Integrator must validate this branch contains only WP-017, proposed WP-018
and this handoff; integrate those builder-close records; then separately update
canonical state/index, activate WP-018, bind the exact activation SHA, push and
dispatch a fresh verifier.

## Decisions

ADR-0002 is revised only as **proposed** architecture on PR #22. No ADR was
accepted or rejected. The PR #19 -> PR #22 supersession and candidate-set
mechanism are builder design/output claims pending independent gates.

## Verification and review status

- WP-015 PASS remains exact only for `2f5508c...` + its activation/binding.
- WP-016 **Requires repair**/F-AR-006/F-AR-007 remains exact only for
  `2f5508c...` + its activation/binding.
- No independent verification or adversarial re-review exists for `5bd0db2...`.
- PR #22, ADR-0002, WP-000 and Phase 0 remain unaccepted/unmerged.

## Unresolved items

- separate Integrator validation/integration and exact WP-018 activation/binding;
- fresh exact-target verification, separate result integration and fresh
  adversarial re-review;
- repair or authorised resolution of any later surviving material finding;
- ADR-0000/0001/0002, PR #22/#1, human/PR/Phase gates;
- Phase 1 remains blocked.

## Exact next required responsibility

**Fresh separate Integrator.**

Cold-read canonical state and governance; revalidate live PR #22 target/base/
ten-file scope, PR #19 supersession and the exact builder-close routing branch.
Integrate only WP-017, proposed WP-018 and this SESSION-0030 record if scope is
exact. Then canonically activate/bind WP-018 and dispatch a fresh verifier.

The Integrator must not verify or adversarially review the target, reinterpret
historical results, accept ADR-0002, merge PR #22/#1, accept Phase 0 or begin
Phase 1.
