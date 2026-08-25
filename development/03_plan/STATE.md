# SOUL PROJECT STATE

**Current phase:** Phase 0 — Development Operating System  
**Current work package:** WP-000 — Development Operating System  
**Current branch:** `phase0/development-os`  
**State:** builder work in progress; independent verification not yet performed  
**Authoritative product branch:** `main`

## Current objective

Establish the repository-based operating discipline required to design SOUL across many fresh ChatGPT sessions without relying on chat memory or a single agent's self-assessment.

## Accepted foundation currently proposed on the Phase 0 branch

- SOUL is a general-purpose agentic architecture that creates the task-specific working system needed to pursue an intended outcome.
- Generality means generating domain/task-specific operating systems above a stable core, not forcing every problem through one fixed workflow.
- Persistent project truth must live outside chat/model memory.
- Missing capability creation is a first-class architectural requirement, governed by specification, isolation, testing, independent verification and admission.
- Completion is a system state, not an agent declaration.

These statements are not yet accepted into `main`; they are Phase 0 branch content pending independent verification and review.

## Completed builder outputs in WP-000

- development workspace definition,
- vision, definition, success criteria, non-negotiables,
- source-of-truth hierarchy,
- working protocol,
- role model,
- decision, verification and change policies,
- ADR, WP, verification, evidence, adversarial-review and session templates,
- roadmap,
- architecture-workspace boundary.

## Required next responsibility

1. Finish WP-000 metadata and builder session handoff.
2. Open a Phase 0 pull request.
3. Run **independent verifier session** against the exact PR/commit using `06_reviews/VERIFICATION_TEMPLATE.md`.
4. If verification passes, run a separate **adversarial review session** because Phase 0 governs all future work and is therefore high leverage.
5. Repair findings through a builder session if required, then re-verify the changed commit.
6. Merge only after current verification passes and unresolved high-impact findings are closed or explicitly accepted through the decision policy.

## Phase 1 gate

Phase 1 does not begin until WP-000 is `verified-complete` and the Phase 0 PR is accepted into `main`.
