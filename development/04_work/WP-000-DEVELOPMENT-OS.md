# WP-000 — SOUL Development Operating System

**Status:** material change — current exact-target verification PASS; fresh adversarial re-review required
**Owner role:** designer/builder  
**Decision authority:** foundation changes require human-owner approval; governance design requires independent verification  
**Branch:** `phase0/development-os`  
**PR:** #1 — draft

## Objective

Create the durable repository-based operating system required to design SOUL over many fresh sessions without depending on one long chat, hidden model memory, or a producing agent's own declaration that the work is correct.

## Problem

SOUL does not yet exist, but building it will require long-running, multi-session architecture work. Without a prior operating discipline, decisions, assumptions, evidence, open work, and verification would live partly in conversation history and would drift as sessions grow or are replaced. That would reproduce the exact agentic failure classes SOUL is intended to control.

Phase 0 must therefore control not only workflow/state/verification, but also the shared **observable reasoning discipline** used by development sessions when they examine premises, framing, necessity, evidence, failure causes and completion claims. This does not make reasoning self-verifying; it makes the development process explicit enough to review and improve.

## Scope

- authoritative project-state hierarchy,
- foundation definition for the development effort,
- work-package model,
- cold-start and handoff protocol,
- development role separation,
- decision and change governance,
- shared repository-based development reasoning policy,
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
- selecting databases, agent frameworks, retrieval engines, model providers, or UI technologies,
- claiming that prompt-level reasoning policy alone is the final SOUL reasoning/control architecture.

These exclusions do not postpone required architecture; they protect Phase 0 from making product decisions before the process for making those decisions is controlled.

## Required reading

Every session enters through `development/03_plan/COLD_START.md`; the sequence below is **Step 3 material only** and cannot replace or reorder COLD_START Steps 1–2.

For builder/reviewer sessions, Step 3 includes:

1. `development/00_foundation/VISION.md`
2. `development/00_foundation/DEFINITION.md`
3. `development/00_foundation/SUCCESS_CRITERIA.md`
4. `development/00_foundation/NON_NEGOTIABLES.md`
5. `development/01_governance/SOURCE_OF_TRUTH.md`
6. `development/01_governance/WORKING_PROTOCOL.md`
7. `development/01_governance/REASONING_POLICY.md`
8. this WP
9. `development/03_plan/STATE.md`

Verifier additionally reads `development/01_governance/VERIFICATION_POLICY.md` according to the active verification WP's Step-3 independence order before builder rationale or session notes.

## Inputs and dependencies

- the stated goal for the rebuilt KEEL/SOUL architecture,
- analysis of the existing KEEL architecture,
- the production decision-support reference scenario and its control/evidence requirements,
- prior KEEL-Work, keel-dev, os-architect, oyun2 and keel-research reasoning/governance lessons recorded in `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`,
- empty `batuhanozgun/soul` repository at bootstrap.

## Unknowns and assumptions

- Exact ChatGPT product features may evolve; repository state must therefore remain sufficient even if Project/Work behaviour changes.
- The current development protocol is manual scaffolding, not the final SOUL architecture.
- Same-model verifier sessions reduce context anchoring but do not provide true model independence; this limitation must remain explicit.
- `REASONING_POLICY.md` is a bootstrap governance control. Repeated failures that can be prevented or detected mechanically should migrate toward stronger controls rather than accumulating prompt text indefinitely.

## Outputs

- `development/README.md`
- all Phase 0 foundation and governance documents,
- `development/01_governance/REASONING_POLICY.md`,
- reusable ADR/WP/evidence/review/session templates,
- `development/03_plan/ROADMAP.md`
- `development/03_plan/STATE.md`
- minimal derived ChatGPT Project entry instruction that points to repository cold-start rather than duplicating governance,
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
12. **Reasoning-policy sufficiency without duplicate authority:** every fresh development role loads one canonical repository reasoning policy through `COLD_START.md`; the policy distinguishes observation/inference/assumption/verification, separates objective/method/state/evidence, applies deeper premise/framing/necessity/alternative/falsification/root-cause checks proportionally to risk, preserves owner-vs-technical authority and analytical provenance, explicitly avoids private chain-of-thought requirements, and does not create a second bootstrap or self-verification path.

Criterion 12 was added on 2026-08-26 as an explicit owner-directed Phase 0 scope strengthening under WP-005/ADR-0001. It does not reinterpret or weaken the historical criteria or historical verification results. All prior verification is stale for the materially changed target.

## Required verification

- fresh verifier session using `development/06_reviews/VERIFICATION_TEMPLATE.md`,
- direct inspection of every acceptance criterion against the exact PR commit, including the new criterion 12,
- explicit regression test for historical F2-R1 after removal of the stale duplicate pointer,
- verification that ChatGPT Project entry guidance does not create a second bootstrap authority,
- separate adversarial-review session using `ADVERSARIAL_REVIEW_TEMPLATE.md`,
- re-verification after any later material repair,
- human-owner acceptance only after verifier/adversarial outputs are visible.

## Evidence obligations

The verifier must cite exact repository artefacts for every criterion. Claims about ChatGPT product behaviour are not required to prove this WP's repository continuity because repository sufficiency is the design target; any product-specific assumptions used later require fresh external evidence.

The reasoning-policy synthesis evidence must distinguish observed predecessor-source rules from SOUL-specific design choices and must not count duplicate predecessor files as independent corroboration.

## Risks

- overfitting the new operating system to current KEEL terminology,
- creating bureaucracy that does not protect an identifiable failure property,
- allowing templates to become duplicate sources of authoritative semantics,
- confusing same-model fresh-context review with independent ground truth,
- letting Phase 0 expand into product architecture before its own gate is passed,
- turning the reasoning policy into ritualised overthinking or self-reported false assurance,
- allowing Project Instructions to become an independently drifting copy of repository governance.

## Completion state

Current: **materially changed — WP-015 exact-target verification PASS; fresh
adversarial re-review required**. The PASS remains bound only to PR #19 exact
target `2f5508c...`; adversarial, ADR, owner, PR and Phase gates remain open.

## Handoff

The next responsibility is a **fresh separate adversarial reviewer** under
`WP-016-PHASE0-MOVING-CANDIDATE-CONVERGENCE-ADVERSARIAL-REREVIEW.md` against
the same exact PR #19 target. The reviewer must establish attack hypotheses
before relying on producer/verifier conclusions and perform no repair,
integration, ADR acceptance, material merge or Phase work in the review act.
