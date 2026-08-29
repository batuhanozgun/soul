# WP-021 Function Necessity and Role-Motivation Analysis

**Status:** design evidence; non-authoritative; supports proposed Development Lifecycle / ADR-0003  
**Date:** 2026-08-29  
**WP:** WP-021 — Development OS Lifecycle and Work-Selection Improvement

## Purpose

Test proposed lifecycle functions **before** turning them into permanent roles. This record follows the existing Development OS reasoning rule and predecessor research principle that `many functions = many roles` is not assumed; each function must first show a concrete need, then be placed according to motivation/authority/conflict cost.

## Test method

For each function:

1. identify the concrete failure/need it addresses;
2. identify what happens if the function is absent;
3. ask whether an existing function/control can provide the same result more simply;
4. identify coordination/authority/cognitive costs;
5. determine whether the function shares a role's single success objective or creates a distinct/competing success criterion.

The result is a candidate placement, not proof that the role architecture is optimal. WP-021 replay and pre-build adversarial review must attempt to falsify it.

## F1 — Select the correct next substantive work

**Need:** current negative-result integration can mechanically choose `repair`/`investigation-repair` before a separate responsibility asks whether the correct response is local repair, reframing, research, architecture redesign, dependency/roadmap revision or a true owner decision.

**If absent:** result integration continues to embed substantive project-planning choices; Builder/Designer receives an already-shaped task and may reason only inside that frame.

**Can an existing role own it?**

- **Integrator:** poor fit. Integrator's success criterion is faithful, non-interpretive state/result integration. Choosing what substantive work should happen next requires interpreting project objectives, dependencies and evidence. Combining them weakens the reason Integrator exists.
- **Builder:** poor fit. Builder is rewarded for completing selected work; choosing whether that work should exist or be reframed creates completion/closure conflict.
- **Designer:** partial fit but different horizon. Designer optimises the technical design for a selected problem. Selecting which project problem should be next and the minimum process depth is program/work sequencing, not technical solution quality.
- **Human Owner:** wrong default. It would recreate hidden orchestration and transfer researchable technical sequencing to the owner.

**Candidate placement:** distinct **Development Planner** role/motivation.

**Single motivation:** maintain the best evidence-backed sequence of work toward the accepted project/phase objective.

**Cost/risk:** new handoff and possible bottleneck/hidden-owner behaviour. Mitigation: Planner is invoked only when a substantive next-work choice exists; deterministic already-specified transitions remain mechanical.

**Falsification:** if replay/pilot shows the Integrator or Designer can safely provide the function without result reinterpretation/closure bias and with lower coordination cost, remove the permanent Planner role.

## F2 — Classify required reasoning depth

**Need:** not every task should pay full architecture-analysis cost, but cross-cutting/high-uncertainty/repeated-failure work should not go directly to implementation.

**If absent:** either under-analysis or universal ceremony.

**Separate role needed?** No. This is instrumental to selecting the next work path and shares Development Planner's success objective.

**Candidate placement:** Development Planner.

**Falsification:** if route classification proves reliably deterministic from WP metadata/invariants, migrate the function toward a mechanical rule rather than retaining model judgement.

## F3 — Define the problem independently of the current mechanism

**Need:** existing mechanisms can attract repairs into their own abstraction; current reasoning policy already identifies this hazard.

**If absent:** design begins from `how do I patch X?` rather than `what property failed and at what layer should it be solved?`.

**Separate role needed?** Not yet. Problem framing and technical design both optimise the quality of the selected technical solution. Splitting a permanent Problem Framer would add handoff/fragmentation without established motivational conflict.

**Candidate placement:** Designer.

**Countermeasure to anchoring:** fresh pre-build adversarial challenge, independent evidence/alternatives where justified, and explicit design reopen conditions.

**Falsification:** if future evidence shows Designers consistently preserve their own framing despite independent challenge, test a separate framing responsibility.

## F4 — Acquire decision-relevant evidence

**Need:** technical design can depend on external standards/literature/prior art, repository history or empirical tests not already established.

**If absent:** architecture may be reinvented or selected from incomplete local evidence.

**Separate role needed?** Existing Researcher already has a clean motivation: establish trustworthy evidence. Preserve it.

**Candidate placement:** Researcher.

**Boundary:** research is conditional; it does not decide architecture.

## F5 — Explore credible technical alternatives/layers

**Need:** material architecture choices can have multiple genuinely different solution layers; first plausible option should not silently become the design.

**If absent:** premature commitment / existing-tool bias.

**Separate role needed?** Generally no. Alternative exploration is part of Designer's design-quality objective. Independent alternative producers can be temporary fresh executions when the solution space is materially underdetermined; this does not justify another permanent role by itself.

**Candidate placement:** Designer, with temporary independent perspectives only where justified.

## F6 — Challenge the frame/design before build

**Need:** post-build adversarial review repeatedly exposes issues after implementation; high-risk design can benefit from attack before another build loop.

**If absent:** all adversarial learning occurs after implementation cost is paid.

**Separate role needed?** No new role. Existing Adversarial Reviewer has exactly the required motivation: find material failure modes/hidden assumptions. Reuse it in a fresh pre-build execution against a frozen design.

**Candidate placement:** Adversarial Reviewer.

**Boundary:** pre-build and post-build reviews are separate fresh executions when both are required.

## F7 — Synthesize a build-ready technical design

**Need:** research, alternatives and challenge must converge into one implementation-ready plan with protected properties, boundaries and verification obligations.

**If absent:** Builder receives unresolved options/ambiguity and silently becomes Designer again.

**Separate role needed?** Shares Designer's objective of best defensible technical design.

**Candidate placement:** Designer.

## F8 — Realise the accepted design

**Need:** implementation is a distinct success objective: produce the accepted design correctly and observably.

**If absent as separate motivation:** the same agent can alter the design to make implementation easier or complete the WP, weakening evidence about whether the design itself was sound.

**Can Designer also own it?** For simple Route-1 local work, design is already accepted and no separate Designer pass is needed. For material Route-2/3 work, combining design + implementation creates a distinct completion pressure and is the primary role-split hypothesis under test.

**Candidate placement:** separate Builder for Route 2/3; direct Builder for Route 1.

**Builder success includes:** stopping/reopening design if implementation falsifies a material design premise.

## F9 — Independently verify realised work

**Need:** producer confidence/tool success is not proof.

**Existing role fit:** Verifier is already purpose-built and load-bearing.

**Candidate placement:** preserve Verifier.

## F10 — Adversarially review realised work

**Need:** ordinary verification may miss hidden assumptions, boundary failures and false completion.

**Existing role fit:** preserve Adversarial Reviewer.

## F11 — Integrate independent results into canonical state

**Need:** issued results must become repository truth without the issuing reviewer/verifier self-transitioning or acceptance being inferred.

**Existing role fit:** Integrator is load-bearing.

**Required change:** narrow substantive routing. Integrator may follow a uniquely prescribed next step, but when new evidence creates a real choice about the next work type, it must route to Development Planner rather than inventing a repair/design itself.

## F12 — Evaluate whether Development OS itself is effective

**Need:** more process is not automatically better; controls can exist without producing reliability value.

**If absent:** Development OS may accumulate ritual/roles/handoffs based on plausible governance logic without evidence that escaped failure or owner burden improves.

**Separate permanent role needed?** Not initially. The function can be a Researcher/evaluation WP because its motivation is trustworthy empirical evidence about process performance, not process approval.

**Candidate placement:** Researcher under explicitly scoped evaluation work; final acceptance remains under normal governance.

## Candidate role set

### Development Planner — proposed new permanent role

**Motivation:** maintain the best evidence-backed sequence of work toward the accepted phase/project objective.

Owns: F1, F2.

Does not own: technical design, implementation, verification, independent review, result reinterpretation, owner value authority.

### Designer — proposed split from current Designer / Builder

**Motivation:** produce the most defensible build-ready technical design for the selected problem.

Owns: F3, F5, F7. Invokes/consumes F4 and F6 as needed.

Does not own: material implementation under Route 2/3, independent verification, owner value authority.

### Builder — proposed split

**Motivation:** realise an accepted design correctly, completely and observably.

Owns: F8.

Does not own: silent material redesign or self-certification.

### Researcher — preserve

Motivation: establish trustworthy evidence. Owns F4; may execute F12 under an evaluation WP.

### Verifier — preserve

Motivation: determine exact-target compliance/evidence sufficiency. Owns F9.

### Adversarial Reviewer — preserve

Motivation: find material failure modes/hidden assumptions. Owns F6 and F10 in separate fresh executions where both are required.

### Integrator — preserve and narrow

Motivation: faithfully translate authorised decisions/independent results into canonical state. Owns F11.

### Human Owner — preserve

Motivation/authority: project vision, values, scope and declared owner gates. Not a technical scheduler/verifier/fallback planner.

## Roles deliberately not added

### Permanent Problem Framer

Not justified yet. Framing + design synthesis share design-quality motivation; current evidence does not show the coordination benefit of another permanent boundary exceeds its cost.

### Pre-build Critic

Not justified. Existing Adversarial Reviewer motivation already fits.

### Dedicated Development-OS Evaluator

Not justified initially. Evaluation can be bounded Researcher work with independent acceptance gates.

### Multi-agent Council / Consensus Panel

Rejected as a default role group. More agents do not create independent evidence by themselves; consensus can add anchoring/conformity and cost.

## Main unresolved hypothesis

The most consequential design hypothesis is that **Development Planner is truly a separate motivation rather than a function Designer or Integrator can safely absorb**.

WP-021 pre-build adversarial review and replay must attack this explicitly. Evidence that Planner adds bottleneck/coordination failure without earlier detection should lead to simplification rather than defending the new role because it has already been designed.
