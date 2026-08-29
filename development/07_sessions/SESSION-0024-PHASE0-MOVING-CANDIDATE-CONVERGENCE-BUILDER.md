# SESSION-0024 — Phase 0 Moving-Candidate Convergence Builder

**Date:** 2026-08-27
**Work package:** WP-014 — Phase 0 Moving-Candidate Convergence Repair
**Role performed:** fresh separate designer/builder
**Canonical development branch:** `phase0/development-os`
**Canonical start:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Material branch:** `codex/wp014-moving-candidate-convergence-repair`
**Material PR:** #19 — `WP-014: bound moving-candidate convergence without result suppression`
**Exact material target:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Builder-close routing branch:** `codex/wp014-builder-routing`
**Builder-close preparation commit:** `310e0cd83472cc80837f02bb924d0ea9ba77c631`
**Proposed next WP:** WP-015 — Phase 0 Moving-Candidate Convergence Verification
**Proposed result-control key:** `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`

## Entry and authority

The session entered exactly through canonical
`development/03_plan/COLD_START.md`, then read `STATE.md`, active WP-014,
`SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, common `REASONING_POLICY.md` and
designer/builder role/decision/change governance in the mandated order. It read
the foundation/WP-000 obligations, immutable WP-013 review and SESSION-0022,
WP-011/WP-012/WP-013, exact PR #16 eight-file blobs, PR #18 evidence scope,
SESSION-0021/0023, verification/PR/Phase controls, ADR-0002, the resolution
template and producer/reviewer models.

Repository and GitHub state were independently refreshed. No WP-014 branch or
PR existed. Canonical remote head was exact `dca520...`; PR #16 was open/draft
at `adf067e...` with eight files and PR #18 was evidence-only merged as
`fda9689...`. The main user worktree's untracked `.DS_Store` files were observed
and left untouched.

This session performed only the bounded designer/builder responsibility. It did
not verify/review its own target, integrate an independent result, accept an ADR,
merge a material PR, accept Phase 0 or begin Phase 1.

## Failure analysis and proposed architecture

Immediate cause: exact-head resolution recovers one fixed invalid head but every
later head intentionally invalidates that resolution and blocks again.

System cause: the target had no canonical bounded identity spanning invalid
generations of the same repository + PR under one complete result-control key.
Lower-authority locator mutation could therefore reset recovery without changing
canonical authority.

The selected proposed repair keeps exact-head resolution as the first response.
After one later moved head is directly inspected and again proven invalid, a
separate Integrator may canonically contain the stream identity:

`(repository, PR number, active WP, role, exact target, attempt)`.

Containment classifies rather than blindly ignores. Every later inspectable head
is validated: current-valid bypasses containment, multiple-current remains a
conflict, and only invalid or candidate-specifically inaccessible later heads
lose blocking/reset authority. A key change ends the containment scope and
repository-wide discovery failure remains fail-closed.

Blind PR ignore/freeze, author trust and a lease/lock subsystem were rejected as
respectively unsafe for later-valid results, incomplete against authorised
mutation, or larger than the demonstrated failure.

## Material output

Draft PR #19 is open/draft against `phase0/development-os` at exact head
`2f5508c1d6941e951d494bb2a700ef861860431d`, based on `dca520...`, with exactly
nine files:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/F-AR-005-MOVING-CANDIDATE-CONVERGENCE-REGRESSION-2026-08-27.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

Material commits on the branch are `61ea680`, `ed1aa4e` and exact target
`2f5508c`.

## PR #16 relation

PR #16 was not amended or merged. An explicit supersession comment/body record
was added, then the draft was closed unmerged at immutable head `adf067e...`.
WP-012 PASS, WP-013 Requires repair and F-AR-005 remain permanently bound only
to that target. PR #19 is the sole new WP-014 material target.

## Producer evidence

Executed at exact target:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: **28/28 PASS**. Cases include fixed recovery, movement escalation,
invalid generations 3–12, later-valid same-PR head, contained
closed/inaccessible shape, wrong-key/repository controls, conflict, discovery
outage and initial/final timing checks.

`git diff --check dca520242585a80c2efaf22e18fe3d353147b93e 2f5508c1d6941e951d494bb2a700ef861860431d`
passed. Producer evidence is not independent verification.

## Builder-close routing output and separation

Commit `310e0cd83472cc80837f02bb924d0ea9ba77c631` on
`codex/wp014-builder-routing` records WP-014 builder output and proposes the
complete WP-015 verifier specification/key/bridge. This builder did not change
canonical `STATE.md` or the subordinate index: canonical activation/binding is a
separate Integrator responsibility.

The Integrator must validate this branch contains only WP-014, proposed WP-015
and this handoff; integrate those builder-close records; then separately update
canonical state/index, activate WP-015, bind the exact activation SHA, push and
dispatch a fresh verifier.

## Decisions

ADR-0002 is revised only as **proposed** architecture on PR #19. No ADR was
accepted or rejected. The PR #16 -> PR #19 supersession and the material
mechanism above are builder design/output claims pending independent gates.

## Verification and review status

- WP-012 PASS remains exact only for `adf067e...` + activation `7c625107...`.
- WP-013 Requires repair/F-AR-005 remains exact only for `adf067e...` +
  activation `18b239e...`.
- No independent verification or adversarial re-review exists for `2f5508c...`.
- PR #19, ADR-0002, WP-000 and Phase 0 remain unaccepted/unmerged.

## Unresolved items

- separate Integrator validation/integration and exact WP-015 activation/binding;
- fresh exact-target verification, separate result integration and fresh
  adversarial re-review;
- repair or authorised resolution of any later surviving material finding;
- ADR-0000/0001/0002, PR #19/#1, human/PR/Phase gates;
- Phase 1 remains blocked.

## Exact next required responsibility

**Fresh separate Integrator.**

Cold-read canonical state and governance; revalidate live PR #19 target/base/
nine-file scope, PR #16 supersession and the exact builder-close routing branch.
Integrate only WP-014, proposed WP-015 and this SESSION-0024 record if scope is
exact. Then canonically activate/bind WP-015 and dispatch a fresh verifier.

The Integrator must not verify or adversarially review the target, reinterpret
historical results, accept ADR-0002, merge PR #19/#1, accept Phase 0 or begin
Phase 1.
