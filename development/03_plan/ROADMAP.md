# SOUL ROADMAP

The roadmap is ordered by dependency, not convenience. Later phases may inform earlier assumptions, but they do not bypass the acceptance gates of earlier phases.

## Phase 0 — Development Operating System

Establish the repository-based working system that makes long-running SOUL development independent from one chat or one agent's memory.

Outputs: source-of-truth hierarchy, work-package protocol, role separation, decision process, verification process, change process, session handoff, evidence/review templates, project state.

Gate: independent verification + accepted PR.

## Phase 1 — Definition

Produce the complete definition of SOUL: purpose, boundaries, actors, lifecycle, completion semantics, autonomy/human-governance principles, and system/non-system boundary.

Gate: definition is internally consistent with foundation and independently verified.

## Phase 2 — Capability Architecture

Derive the complete capability map required for the vision without using current KEEL folders or mechanisms as the organising principle. Include missing-capability creation and governance as first-class capability.

Gate: capability coverage tested against materially different target scenarios.

## Phase 3 — Failure Model

Build the agentic failure taxonomy and map each failure class to observable signals, prevention, detection, containment, recovery, and regression strategy.

Gate: architecture-critical failure classes have explicit control ownership.

## Phase 4 — Core Domain Model

Define the canonical entities and contracts: goal, task, role, agent, capability, tool, state, context, knowledge, decision, assumption, claim, evidence, artefact, verification, evaluation, approval, event, failure, handoff, policy.

Gate: concepts have single meanings and ownership; no duplicate authoritative semantics.

## Phase 5 — State, Memory, Context, Knowledge and Retrieval Architecture

Separate persistent state, episodic/session state, long-term memory, knowledge stores, retrieval, context assembly, freshness, trust and access control.

Gate: fresh-session continuation and selective context assembly are demonstrable by specification and prototype tests.

## Phase 6 — Runtime and Orchestration Architecture

Define task lifecycle, planning, decomposition, scheduling, agent spawning, handoff, tool execution, dependency handling, stopping, budgets, concurrency and recovery.

Gate: runtime state machine can represent success, partial, blocked, failed, stale, conflicted and unverified states without prose interpretation.

## Phase 7 — Evidence, Provenance, Verification and Evaluation Architecture

Define workflow provenance and analytical provenance, claim/evidence binding, reproducibility, verifier independence, deterministic validation, semantic evaluation, completion gates and human review.

Gate: a decision-support scenario can prove how a material recommendation derives from evidence and computation rather than narrative alone.

## Phase 8 — Authority, Policy, Safety and Human Governance

Define permissions, tool boundaries, protected controls, approval classes, owner decision area, irreversible actions, policy enforcement, secrets/data handling and escalation.

Gate: constrained agents cannot silently widen authority or rewrite the controls that constrain them.

## Phase 9 — Self-Extension Architecture

Define missing-capability detection and the specify → research/build/integrate → isolate → test → verify → register → enable/disable lifecycle.

Gate: newly generated capability cannot self-admit or change its own admission rules.

## Phase 10 — Observability and Operational Model

Define traces, events, state views, costs, latency, tool activity, agent transitions, policy decisions, verification state, failure state and human-facing observability.

Gate: an operator can determine what is happening, why, what evidence exists, what is blocked and why the system stopped.

## Phase 11 — Reference Implementation Architecture and Build Plan

Choose technologies only after the required architecture is known. Map accepted architecture to components, interfaces, storage and execution environments. Map existing KEEL mechanisms as candidate prior art, not defaults.

Gate: implementation plan traces every component to accepted capabilities/contracts and avoids unowned infrastructure.

## Phase 12 — Implementation, Pilots and Evaluation

Build the reference implementation and validate it on at least three materially different pilots: software production, analytical decision support, and an open-ended multidisciplinary design/operations task.

Gate: success criteria in `00_foundation/SUCCESS_CRITERIA.md` are measured across pilots; one successful domain is not sufficient.

## Phase 13 — Migration, Hardening and v1

Decide what, if anything, migrates from KEEL; remove prototype-only development assumptions from `system/`; run security, reliability, adversarial and regression suites; define distribution and versioning.

Gate: `system/` is independently usable and contains no hidden dependency on development conversations or repository-only scaffolding.
