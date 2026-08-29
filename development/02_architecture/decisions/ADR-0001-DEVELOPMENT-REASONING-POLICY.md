# ADR-0001 — Canonical Development Reasoning Policy

**Status:** proposed — human-owner direction approved 2026-08-26; pending independent review and Phase 0 acceptance  
**Decision class:** Architecture decision  
**Date:** 2026-08-26  
**Supersedes:** none  
**Superseded by:** none

## Problem

Phase 0 currently governs repository state, work packages, authority, verification and session continuity, but it does not yet define a single shared discipline for how development sessions should examine premises, framing, necessity, evidence, alternatives, failure causes and completion claims.

Prior KEEL, KEEL-Work, OS Architect and KEEL Research work contains relevant lessons, but they are distributed across environment-specific `CLAUDE.md`, `AGENTS.md`, research and rule files. Copying those files wholesale would import obsolete product-specific assumptions and create multiple instruction authorities. Leaving them outside SOUL would also allow fresh development sessions to repeat known reasoning failure classes.

## Decision scope

This decision governs the **SOUL development operating system**, not the eventual reusable SOUL runtime/product reasoning architecture. It defines the shared reasoning discipline that every Phase 0+ development role loads before substantive work.

It does not change the active WP's objective, role authority, verification independence or repository source-of-truth hierarchy.

## Constraints

- `COLD_START.md` must remain the single fresh-session sequencing authority.
- The policy must not require disclosure or persistence of private chain-of-thought.
- The policy must not force expensive first-principles analysis on every atomic, reversible action.
- Technical questions that can be researched or derived must not be offloaded to the human owner merely to reduce agent risk.
- Material outputs remain subject to independent verification; the policy cannot convert self-discipline into proof.
- Established domain terminology is preferred over invented local jargon.
- Project memory/chat context remains non-authoritative relative to repository state.

## Options considered

### A. No shared reasoning policy

Rely on model defaults plus role/WP instructions.

**Rejected:** known failure classes would remain dependent on model memory and prompt luck. Current Phase 0 would control workflow without controlling the reasoning discipline used to create the architecture.

### B. Copy prior KEEL/OS Architect instructions wholesale

Import `CLAUDE.md`, `AGENTS.md`, defect-model and research rules into SOUL.

**Rejected:** those sources mix general principles with Claude Code hooks, KEEL-specific paths, historical operating constraints and product-specific terminology. Wholesale import would overfit SOUL to its predecessor and create instruction duplication.

### C. Put a long reasoning prompt in ChatGPT Project Instructions

Use Project Instructions as the primary policy layer.

**Rejected:** Project Instructions are product-specific, less auditable than repository governance, can drift independently from GitHub state and would create a second session-bootstrap authority. The repository must remain sufficient even if ChatGPT product behaviour changes.

### D. Canonical repository policy loaded by `COLD_START.md`

Create `development/01_governance/REASONING_POLICY.md`; load it from the one authoritative cold-start sequence; keep Project Instructions minimal and limited to entering that sequence.

**Decision:** chosen.

## Evidence used

Primary synthesis record: `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`.

The evidence records the exact source files/blob identifiers and separates source-derived principles from SOUL-specific synthesis decisions.

## Decision

SOUL development will use one canonical repository-based reasoning policy shared by all development roles.

The policy will:

- define always-on epistemic rules;
- trigger deeper checks for material/ambiguous/novel/irreversible/risky decisions rather than every atomic action;
- require premise and framing inspection for material decisions;
- test whether proposed mechanisms/functions are necessary before deciding their placement;
- compare credible alternatives and solution layers without manufacturing fake menus;
- seek falsifying evidence and preserve uncertainty/conflicting evidence;
- separate owner value/scope authority from technical/epistemic responsibility;
- require proximal-cause plus root-cause analysis after failures;
- require appropriate analytical provenance when claims depend on computation/data;
- preserve independent verification and exact-target freshness;
- externalise only decision-relevant rationale, assumptions, evidence, uncertainty and verification obligations, not private chain-of-thought.

`COLD_START.md` remains the only sequencing authority. The reasoning policy is loaded as common governance inside that sequence.

## Rationale

The chosen design preserves the useful lessons from prior systems while removing their environment-specific implementation assumptions. It also avoids the two main failure modes of instruction architecture here: a duplicated bootstrap sequence and an oversized universal prompt that encourages ritualised overthinking.

The policy is deliberately a **development bootstrap control**, not a claim that prompt text alone can solve reasoning reliability. Where later failures show a property can be enforced deterministically, `CHANGE_POLICY.md` requires stronger controls and regression tests.

## Consequences

### Positive

- every fresh development session receives the same explicit epistemic discipline;
- known reasoning failures become inspectable requirements rather than informal memory;
- architecture work gains explicit premise/framing/necessity/falsification checks;
- Project Instructions can remain minimal and repo-directed;
- the policy is versioned, reviewable and independently verifiable with the rest of Phase 0.

### Costs and new risks

- additional reading and cognitive load at cold start;
- agents may turn checks into ceremony rather than useful reasoning;
- an over-broad policy could suppress speed on routine work;
- self-reported compliance can create false confidence;
- the policy itself can become stale as empirical evidence about agent behaviour changes.

Mitigations are built into the policy: risk-triggered depth, concise observable traces, no fixed-count alternative ritual, and explicit preference for mechanical enforcement when feasible.

## Rejected alternatives and why

See Options A–C above. They were rejected because they either leave known failure classes unmanaged, import predecessor-specific architecture, or create a second product-specific instruction authority outside the repository.

## Verification required

Independent verification must establish that:

1. every fresh development role loads the policy through the single `COLD_START.md` sequence;
2. no second bootstrap order is created in Project Instructions, WP files or launch views;
3. the policy does not widen role/WP authority;
4. it includes the required epistemic, framing, necessity, alternative/layer, falsification, root-cause, analytical-provenance, anti-overthinking and completion controls;
5. it explicitly avoids chain-of-thought disclosure requirements;
6. WP-000 acceptance criteria are strengthened transparently rather than weakened to obtain a PASS;
7. prior verifier results are treated as stale for the materially changed target.

A separate adversarial review should attempt to show that the policy creates ceremony, duplicated authority, hidden owner-decision transfer, or prompt-only false assurance.

## Reopen conditions

Reopen this decision if any of the following occurs:

- empirical use shows the policy materially reduces task performance through overthinking or ritualisation;
- a stronger platform-level mechanism can enforce the same properties more reliably with less prompt load;
- ChatGPT/agent execution gains a stable native policy mechanism that is versioned and auditable at least as well as repository governance;
- verification or adversarial review finds an authority or sequencing conflict;
- later SOUL architecture establishes a more general reasoning-control layer that should supersede this development-only policy.
