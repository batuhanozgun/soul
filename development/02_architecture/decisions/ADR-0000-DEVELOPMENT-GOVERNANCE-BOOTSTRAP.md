# ADR-0000 — Development Governance Bootstrap

**Status:** proposed  
**Date:** 2026-08-25  
**Decision owner:** human owner after Phase 0 verification  
**Supersedes:** none  
**Superseded by:** none

## Problem

SOUL must be designed over many sessions before SOUL itself exists. Without a controlled development environment, project truth would be distributed across long conversations, implicit model memory, ad hoc summaries, and implementation artefacts. That would reproduce the same drift, false-completion, self-verification, and state-loss problems SOUL is intended to solve.

## Scope

This decision governs the development process used to design SOUL. It does not decide SOUL's final runtime architecture or implementation technology.

## Constraints

- the work will span multiple fresh sessions,
- current LLM sessions are fallible and context-limited,
- the GitHub repository is durable, versioned, reviewable, and accessible across sessions,
- verification must not depend solely on the producing session,
- development scaffolding must remain separable from the eventual reusable product.

## Options considered

### Option A — One long conversation

Low setup cost but high dependence on growing context, hidden memory, and fragile handoff. Rejected.

### Option B — ChatGPT workspace/project memory as primary state

Improves continuity but leaves authoritative decisions and verification too dependent on product-specific memory behaviour and is less explicit/versioned than repository state. Rejected as primary source of truth; may remain supporting context.

### Option C — Repository-authoritative development operating system + fresh sessions

Use GitHub as canonical state; define bounded work packages, cold-start required readings, role-separated sessions, ADRs, evidence, verification, reviews, handoffs, branches and PR gates. Selected.

## Evidence

The prior KEEL analysis showed that externalised state, fresh-agent calls, independent verification, explicit completion gates, and deterministic controls are among its strongest properties. The production decision-support reference architecture reinforced the same general principles for state, verification, provenance, human governance, and observability.

No external product claim is required for this decision: repository-authoritative continuity is deliberately chosen so that development does not depend on any one chat product's memory implementation.

## Decision

SOUL development will use the `soul` GitHub repository as the authoritative source of project truth. Fresh sessions are the default execution unit for materially separate roles. Chat history and model memory are non-authoritative supporting context. Development artefacts live under `development/`; the reusable product lives under `system/`.

## Rationale

This provides explicit, versioned, reviewable state; reduces reliance on latent conversational memory; enables independent fresh-context verification; and lets the development process prototype the properties SOUL is intended to automate later.

## Consequences and new risks

- More explicit artefacts and process are required before product architecture begins.
- Poorly designed templates could create bureaucracy or duplicate state.
- Same-model fresh sessions reduce anchoring but are not true model independence.
- Repository discipline must be maintained; documents alone are not enforcement.

## Rejected alternatives

Options A and B were rejected as primary state mechanisms because they make continuity materially dependent on conversation/product memory rather than explicit project state.

## Verification required

WP-000 must independently verify that a fresh session can identify the project state, active work, authority hierarchy, required readings, role and next action from repository contents alone.

## Reopen conditions

Reopen if a stronger durable state/orchestration environment can provide equal or better explicit versioning, provenance, independent verification, portability and cold-start reproducibility without reintroducing hidden state or product lock-in.
