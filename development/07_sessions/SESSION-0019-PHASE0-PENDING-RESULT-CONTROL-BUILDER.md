# SESSION-0019 — Phase 0 Pending-Result Control Builder

**Date:** 2026-08-26
**Work package:** WP-011 — Phase 0 Pending Independent-Result Control Repair
**Role performed:** fresh separate designer/builder
**Canonical development branch:** `phase0/development-os`
**Canonical start:** `8dcdc750600b336a2e97fde3433926b6a2217f26`
**Material branch:** `codex/wp011-pending-result-control-repair`
**Material PR:** #16 — `WP-011: repair pending independent-result control lifecycle`
**Exact material target:** `adf067e4289e4c0b51cf40c1940193e8252b22e0`
**Material base:** `8dcdc750600b336a2e97fde3433926b6a2217f26`
**Provisional activation commit:** `7c625107c09788d6066249c67d66cbf7c0c4b576`
**Activation-binding commit:** `4dd7f83a3da6d3ec6ab99de00c839aee094e2595`
**Next work package:** WP-012 — Phase 0 Pending-Result Control Verification
**Next result-control key:** `WP-012 / verifier / adf067e4289e4c0b51cf40c1940193e8252b22e0 / attempt 1`

## Entry and authority

The session entered through `development/03_plan/COLD_START.md`, then canonical `STATE.md`, active WP-011, source-of-truth/governance in mandated order, the WP-000/foundation obligations, immutable WP-010 review, historical result intervals and live GitHub PR/ref state. It performed only the bounded WP-011 designer/builder responsibility.

No independent verification, adversarial re-review, result integration, candidate resolution, ADR acceptance, PR acceptance/merge, Phase acceptance or Phase 1 authority was exercised.

## Problem and architecture

The three findings are one lifecycle failure rather than three unrelated prompt defects:

- F-AR-002: unmerged general governance could not protect its own verifier/reviewer close intervals;
- F-AR-003: unresolved invalid same-WP residue could fail closed forever;
- F-AR-004: a single early discovery check left a later publication interval exposed.

The repair introduces:

1. a canonical result-control key of WP, independent role, exact target and positive attempt;
2. initial discovery plus a complete live re-check immediately before independent role commitment;
3. exact repository/PR/head-bound Integrator resolution records, invalidated by head movement;
4. a prohibition on using a resolution to suppress a currently valid result;
5. conflict preservation and fresh canonical attempt activation rather than arbitrary winner selection;
6. fail-closed discovery/inspection with explicit recovery conditions;
7. a provisional WP-local activation bridge for the repair's own verification/re-review rollout interval;
8. an explicit residual publication-after-final-check boundary rather than a false atomic-lock claim.

A lease/lock subsystem was rejected as larger and unsafe without its own authority, stale-lease and recovery lifecycle. The mandatory final re-check plus explicit residual boundary is the smallest coherent bounded control available on the current platform.

## Frozen material output

PR #16 changes exactly eight files relative to the material base:

- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- `development/03_plan/COLD_START.md`;
- `development/03_plan/PR_GATE.md`;
- `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
- `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
- `development/05_evidence/pending_result_control_regression.py`.

Material commits:

- `f78757b` — `WP-011 repair pending-result control lifecycle`;
- `adf067e` — `WP-011 normalize material records`.

PR #13 was closed unmerged as superseded. Its exact head `a45b463b083604d3f59d75bdca5ba97d5bc170e6` and all historical WP-009/WP-010 bindings remain preserved. PR #16 is draft, unaccepted and unmerged. ADR-0002 remains proposed.

## Producer checks

Executed at exact material target:

`PYTHONDONTWRITEBYTECODE=1 python3 development/05_evidence/pending_result_control_regression.py`

Result: **PASS**, 13/13 declared cases, including PR #14 and PR #15 intervals, unresolved/resolved stale candidates, moved heads, malformed candidates, valid-result suppression prevention, multiple-valid conflict, other-WP isolation, unavailable discovery, initial no-result and final publication re-check.

`git diff --check` passed. These are builder checks and producer evidence only; they do not certify the candidate.

## Canonical activation and routing

Commit `7c625107c09788d6066249c67d66cbf7c0c4b576` activates WP-012, the exact target/key and its WP-local bridge. Commit `4dd7f83a3da6d3ec6ab99de00c839aee094e2595` records that exact activation binding.

This activation is a provisional material rollout control. It is not a transition-only relabel, does not modify or retarget the frozen PR #16 material target, and does not accept the proposed general governance. Its bounded purpose is to protect the exact independent verification close interval while the general change remains unmerged.

Canonical files changed for routing/activation:

- `development/03_plan/STATE.md`;
- `development/03_plan/WORKSPACE_INDEX.md`;
- `development/04_work/WP-011-PHASE0-PENDING-RESULT-CONTROL-REPAIR.md`;
- `development/04_work/WP-012-PHASE0-PENDING-RESULT-CONTROL-VERIFICATION.md`;
- this SESSION-0019 handoff.

The frozen material target remains `adf067e...`; canonical activation commits are separate rollout/routing evidence and must be inspected independently by the verifier.

## Exact next responsibility

Fresh separate verifier under WP-012, exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0`, attempt 1.

The verifier must follow WP-012's independence reading order, execute the first bridge check after COLD_START Steps 1–2 and the final complete live re-check immediately before Step 4 role commitment, independently test all current WP-000 and F-AR-001–004 obligations, publish only its evidence artefact + handoff PR, and stop for a separate Integrator.

This builder stops here. It does not verify, re-review, integrate, resolve, accept or merge anything.
