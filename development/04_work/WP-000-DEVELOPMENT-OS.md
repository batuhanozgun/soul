# WP-000 — SOUL Development Operating System

**Status:** verification  
**Owner role:** designer/builder  
**Decision authority:** foundation changes require human-owner approval; governance design requires independent verification  
**Branch:** `phase0/development-os`  
**PR:** #1 — draft

## Objective

Create the durable repository-based operating system required to design SOUL over many fresh sessions without depending on one long chat, hidden model memory, or a producing agent's own declaration that the work is correct.

## Problem

SOUL does not yet exist, but building it will require long-running, multi-session architecture work. Without a prior operating discipline, decisions, assumptions, evidence, open work, and verification would live partly in conversation history and would drift as sessions grow or are replaced. That would reproduce the exact agentic failure classes SOUL is intended to control.

## Scope

- authoritative project-state hierarchy,
- foundation definition for the development effort,
- work-package model,
- cold-start and handoff protocol,
- development role separation,
- decision and change governance,
- independent verification rules,
- evidence/research separation,
- adversarial review discipline,
- project roadmap and current state,
- explicit separation of development artefacts from the eventual reusable `system/` product.

## Non-scope

- deciding SOUL's complete capability architecture,
- choosing implementation technologies,
- mapping current KEEL folders into the new system,
- writing SOUL runtime code,
- selecting databases, agent frameworks, retrieval engines, model providers, or UI technologies.

These exclusions do not postpone required architecture; they protect Phase 0 from making product decisions before the process for making those decisions is controlled.

## Required reading

For builder/reviewer sessions:

1. `development/00_foundation/VISION.md`
2. `development/00_foundation/DEFINITION.md`
3. `development/00_foundation/SUCCESS_CRITERIA.md`
4. `development/00_foundation/NON_NEGOTIABLES.md`
5. `development/01_governance/SOURCE_OF_TRUTH.md`
6. `development/01_governance/WORKING_PROTOCOL.md`
7. this WP
8. `development/03_plan/STATE.md`

Verifier additionally reads `development/01_governance/VERIFICATION_POLICY.md` before builder rationale or session notes.

## Inputs and dependencies

- the stated goal for the rebuilt KEEL/SOUL architecture,
- analysis of the existing KEEL architecture,
- the production decision-support reference scenario and its control/evidence requirements,
- empty `batuhanozgun/soul` repository.

## Unknowns and assumptions

- Exact ChatGPT product features may evolve; repository state must therefore remain sufficient even if Project/Work behaviour changes.
- The current development protocol is manual scaffolding, not the final SOUL architecture.
- Same-model verifier sessions reduce context anchoring but do not provide true model independence; this limitation must remain explicit.

## Outputs

- `development/README.md`
- all Phase 0 foundation and governance documents,
- reusable ADR/WP/evidence/review/session templates,
- `development/03_plan/ROADMAP.md`
- `development/03_plan/STATE.md`
- architecture and product boundary README files,
- builder session handoff,
- Phase 0 PR.

## Acceptance criteria

1. **Cold-start sufficiency:** a fresh session can identify the current phase, active WP, authority hierarchy, mandatory readings, role, and next responsibility from the repository without reading the previous chat.
2. **Single-source discipline:** the governance explicitly prevents chat history or derived summaries from silently overriding canonical state and defines how same-level conflicts are handled.
3. **Work boundedness:** substantial work has an explicit WP schema with scope, non-scope, outputs, acceptance criteria, verification, evidence and handoff requirements.
4. **Role separation:** producing, researching, verifying, adversarial reviewing, integrating and human-owner responsibilities are explicitly separated; a producer cannot independently certify material output.
5. **Decision governance:** foundation and architecture decisions have explicit classes, required records, evidence and reopen conditions; research cannot silently become architecture truth.
6. **Verification discipline:** verification distinguishes PASS / FAIL / NOT VERIFIED, binds results to exact artefact/commit freshness, prefers deterministic validation, and covers analytical provenance when claims depend on data/computation.
7. **Change safety:** acceptance criteria, authority and self-extension controls cannot be silently rewritten by the component or session they constrain.
8. **Session continuity:** session close requires a repository handoff sufficient for a fresh session to continue without old-chat replay.
9. **Development/product separation:** temporary development evidence, sessions and governance are not automatically part of the distributable `system/` product.
10. **Roadmap completeness:** the roadmap contains the full dependency chain from development governance through definition, capability/failure architecture, core models, memory/context/retrieval, runtime, evidence/verification/evaluation, authority/safety, self-extension, observability, implementation, pilots and hardening.
11. **No false completion:** Phase 0 remains unaccepted until independent verification is current for the exact reviewed commit, and high-impact adversarial findings are resolved or explicitly accepted.

## Required verification

- fresh verifier session using `development/06_reviews/VERIFICATION_TEMPLATE.md`,
- direct inspection of every acceptance criterion against the exact PR commit,
- separate adversarial-review session using `ADVERSARIAL_REVIEW_TEMPLATE.md`,
- re-verification after any material repair,
- human-owner acceptance only after verifier/adversarial outputs are visible.

## Evidence obligations

The verifier must cite exact repository artefacts for every criterion. Claims about ChatGPT product behaviour are not required to prove this WP's repository continuity because repository sufficiency is the design target; any product-specific assumptions used later require fresh external evidence.

## Risks

- overfitting the new operating system to current KEEL terminology,
- creating bureaucracy that does not protect an identifiable failure property,
- allowing templates to become duplicate sources of authoritative semantics,
- confusing same-model fresh-context review with independent ground truth,
- letting Phase 0 expand into product architecture before its own gate is passed.

## Completion state

Current: **verification**. Builder output exists; independent verification and adversarial review are still required.

## Handoff

Next responsibility: **Verifier** — cold-read the required files, derive expected acceptance conditions from this WP before reading builder session rationale, and verify the exact Phase 0 PR commit. Do not repair findings during the verification session.
