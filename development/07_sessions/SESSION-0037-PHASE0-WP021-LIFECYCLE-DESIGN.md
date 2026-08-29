# SESSION-0037 — Phase 0 WP-021 Lifecycle Design

**Date:** 2026-08-29  
**WP:** WP-021 — Development OS Lifecycle and Work-Selection Improvement  
**Role under current governance:** designer/builder  
**Primary responsibility:** design-only — produce the candidate lifecycle/ADR/evaluation protocol; do not implement operational governance
**Design branch:** `work/wp021-development-lifecycle-improvement`
**Canonical activation base:** `6fca29474ab97d22e363108b8be6438456316e01`

## Inputs read

Canonical/current SOUL:

- `development/03_plan/STATE.md`
- active WP-021 and blocked WP-020
- `SOURCE_OF_TRUTH.md`
- `WORKING_PROTOCOL.md`
- `REASONING_POLICY.md` in full
- `ROLE_MODEL.md`
- `DECISION_POLICY.md`
- `CHANGE_POLICY.md`
- `VERIFICATION_POLICY.md`
- `COLD_START.md`
- `PR_GATE.md`
- `PHASE_GATE.md`
- `ROADMAP.md`
- `WP-000-DEVELOPMENT-OS.md`
- `WP-005-DEVELOPMENT-REASONING-POLICY.md`
- `ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
- `ADR_TEMPLATE.md`
- `ADVERSARIAL_REVIEW_TEMPLATE.md`
- historical WP-011, WP-014, WP-017 and WP-020 repair lineage/findings used by WP-021.

Non-authoritative evidence/input:

- owner-directed Turn-1/2/3 exploratory records in the isolated `batuhanozgun/keel-research` scratch branch;
- predecessor evidence from `os-architect`, `keel`, `keel-research` and `KEEL-Work` inspected during the planning study;
- refreshed external primary/authoritative prior art from NASA Systems Engineering decision analysis, CMU SEI QAW/ATAM architecture-analysis guidance, Anthropic context-engineering/agent-eval guidance and OpenAI eval guidance.

## Observed design premise

Current `REASONING_POLICY.md` already contains the important material-work questions: frame inspection, necessity, alternatives, disconfirming evidence, proportional depth and root-cause analysis. Therefore the design does not justify itself as `agents need more reasoning instructions`.

The proposed architectural change instead moves responsibilities/timing:

- substantive next-work selection is separated from faithful result integration;
- material technical design is separated from implementation completion;
- high-risk work receives pre-build challenge before implementation;
- repair becomes one possible conclusion after work selection/reframing rather than the automatic result-routing default;
- process depth is risk-proportional, preserving a direct route for routine accepted-design work.

This remains a design hypothesis until independently challenged/evaluated.

## Outputs produced on candidate branch

1. proposed `development/02_architecture/DEVELOPMENT_LIFECYCLE.md`;
2. proposed `development/02_architecture/decisions/ADR-0003-DEVELOPMENT-WORK-SELECTION-AND-RISK-PROPORTIONAL-PREBUILD-LIFECYCLE.md`;
3. `development/05_evidence/WP-021-FUNCTION-ROLE-MOTIVATION-ANALYSIS-2026-08-29.md`;
4. `development/05_evidence/WP-021-HISTORICAL-BLIND-REPLAY-PROTOCOL-2026-08-29.md`;
5. this handoff.

No existing operational governance policy was modified to enact the proposed lifecycle.

## Key design choices — producer claims only

- Candidate new permanent role: Development Planner, with one motivation — maintain the best evidence-backed sequence of work toward the accepted project/phase objective.
- Planner is **not** required on every transition; accepted deterministic next steps remain mechanical so Planner does not become a universal bottleneck.
- Material Designer and Builder responsibilities are separated; Route-1 routine work can still go directly to Builder when an accepted design already determines behaviour.
- Existing Researcher, Verifier, Adversarial Reviewer, Integrator and Human Owner motivations are retained.
- Existing Adversarial Reviewer is reused for pre-build challenge rather than inventing a new critic role.
- No permanent Problem-Framer or Development-OS-Evaluator role is added without further evidence.
- Three routes distinguish direct build, separate design and full pre-build investigation.
- Strong repeated-failure/frame/layer/state/authority triggers force deeper investigation; there is no pseudo-precise universal risk score.
- Context selection is specified only at the minimum lifecycle contract level; major STATE/history compaction remains a later separate change.
- Historical replay is explicitly labelled contaminated development/regression evidence and cannot prove generalisation.

## Producer concerns requiring independent attack

The next reviewer should try to show that:

- Development Planner is unnecessary and Designer/Integrator can own work selection more simply without the identified motivational conflict;
- Planner can become a hidden owner/architecture dictator or bottleneck;
- `substantive choice` is too ambiguous and lets Integrator/Planner move authority opportunistically;
- Route-3 triggers over-escalate normal work or create route oscillation;
- Designer still contains conflicting framing/design motivations;
- pre-build Adversarial Review increases correlated consensus rather than independence;
- the technical ADR decision-owner proposal creates self-acceptance/circularity;
- context-selection metadata can hide required evidence or create duplicate truth;
- the replay protocol is contaminated/unfair/too weak to justify implementation;
- the design adds more handoffs/process artefacts than reliability value;
- the proposed lifecycle is solving the recent result-control history rather than a general Development OS need.

## Verification / implementation status

- Design producer responsibility: ready to freeze as an exact candidate commit.
- Pre-build independent adversarial review: **not performed by this session**.
- Historical replay execution: **not yet performed**; protocol only.
- Operational governance implementation: **not begun and not authorised by this design session**.
- ADR-0003: proposed only.
- WP-020/F-AR-008: still blocked/unresolved; no repair performed.

## Exact next responsibility

Fresh separate **pre-build Adversarial Reviewer** against the exact frozen design commit, using WP-021, proposed lifecycle, ADR-0003, function/motivation analysis and replay protocol as the review target.

The reviewer must not implement/repair the design. It should issue findings/judgement against the design and leave integration/synthesis to a later separate responsibility.

In parallel or after the design review according to available isolated execution capacity, execute the historical replay protocol with future findings hidden from work-producing trials. Operational governance implementation remains blocked until both challenge and replay/evaluation have been synthesised and no unresolved material design finding makes build premature.
