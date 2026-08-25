# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-001 — Phase 0 Independent Verification  
**Current branch:** `phase0/development-os`  
**Current PR:** #1 — draft  
**State:** builder work complete; fresh independent verifier required  
**Authoritative product branch:** `main`

## Current objective

Independently verify whether the Phase 0 repository-based operating discipline is sufficient to carry SOUL design across many fresh sessions without relying on chat memory or builder self-assessment.

## Proposed foundation on the Phase 0 branch

- SOUL is a general-purpose agentic architecture that creates the task-specific working system needed to pursue an intended outcome.
- Generality means generating domain/task-specific operating systems above a stable core, not forcing every problem through one fixed workflow.
- Persistent project truth must live outside chat/model memory.
- Missing capability creation is a first-class architectural requirement, governed by specification, isolation, testing, independent verification and admission.
- Completion is a system state, not an agent declaration.

These statements are not yet accepted into `main`; they are proposed Phase 0 content pending independent verification, adversarial review, and human-owner acceptance where required.

## Completed builder outputs in WP-000

- development workspace definition,
- vision, definition, success criteria, non-negotiables,
- source-of-truth hierarchy,
- cold-start and working protocol,
- development role model,
- decision, verification and change policies,
- ADR, WP, verification, evidence, adversarial-review and session templates,
- roadmap, phase gate, PR gate, workspace index and next-session pointer,
- architecture decision registry and proposed ADR-0000,
- product/development boundary,
- builder handoff,
- draft PR #1,
- verifier work package WP-001.

## Required next responsibility

**Fresh verifier session.** Follow `development/03_plan/COLD_START.md` and `development/04_work/WP-001-PHASE0-VERIFICATION.md`. Verify the exact live PR #1 head commit. Do not repair findings in the verifier session.

After verifier outcome:

- PASS → separate adversarial-review session before Phase 0 acceptance.
- FAIL / NOT VERIFIED → fresh builder repair session, followed by re-verification of the changed commit.

## Builder stop

The current builder conversation must not perform WP-001 verification, accept ADR-0000, merge PR #1, or begin Phase 1. The authority boundary is recorded in `BUILDER_STOP.md`.

## Phase 1 gate

Phase 1 does not begin until WP-000 is `verified-complete`, required adversarial review is resolved, relevant decisions have the correct status, and the Phase 0 PR is accepted into `main`.
