# WP-021 Historical Blind-Replay Protocol

**Status:** design/evaluation protocol; non-authoritative evidence artefact until executed  
**Date:** 2026-08-29  
**WP:** WP-021 — Development OS Lifecycle and Work-Selection Improvement

## Purpose

Evaluate whether the proposed Development OS pre-build lifecycle can surface material failure classes **before implementation** more often than the prior combined Designer/Builder workflow, without relying on knowledge that was unavailable at the historical point.

This is a development/regression experiment, not proof of generalisation. The candidate lifecycle was designed partly in response to the same historical failure lineage, so contamination is structurally possible even when individual replay agents do not see later findings.

## Core experimental rule

Each replay arm receives an isolated historical repository snapshot and only evidence that existed at that checkpoint. Later findings are withheld from all work-producing trajectories and are visible only to the evaluator after those trajectories are frozen.

Replay agents must not inspect current SOUL branches, later WP files, later PRs, later reviews, current chat summaries or the WP-021 design rationale beyond the specific process instructions assigned to their arm.

## Historical checkpoints

### Replay A — before WP-011 repair design

**Snapshot/base:** `8dcdc750600b336a2e97fde3433926b6a2217f26`

**Known at checkpoint:** F-AR-001 through F-AR-004 as recorded by the then-current repository state/review evidence.

**Held out from work trajectories:** F-AR-005 and all later findings.

**Primary hidden target for evaluator:** whether the trajectory anticipates or materially models the class later expressed by F-AR-005 — mutable lower-authority candidate movement can repeatedly reset recovery and deny progress.

### Replay B — before WP-014 repair design

**Snapshot/base:** `dca520242585a80c2efaf22e18fe3d353147b93e`

**Known at checkpoint:** F-AR-001 through F-AR-005 and then-current controls/evidence.

**Held out:** F-AR-006, F-AR-007 and all later findings.

**Primary hidden targets:**
- F-AR-006 class — fresh PR/candidate identities can reset per-candidate containment and restore unbounded denial;
- F-AR-007 class — executable model/routing precedence can contradict normative valid-result precedence.

### Replay C — before WP-017 repair design

**Snapshot/base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`

**Known at checkpoint:** F-AR-001 through F-AR-007 and then-current controls/evidence.

**Held out:** F-AR-008 and any later work.

**Primary hidden target:** F-AR-008 class — visible valid result must not suppress an uncontained uninspectable candidate whose epistemic state is unknown and may conceal a second current result.

## Experimental arms

### Baseline arm — combined current-style design/build reasoning

Use a fresh execution instructed to operate as the then-current `Designer / Builder` on the historical repair problem, with then-current authoritative governance and a comparable tool/model budget.

The baseline is allowed to analyse root causes and alternatives exactly as the then-current Development OS permits. Do not deliberately weaken it or remove `REASONING_POLICY` rules that existed at the snapshot.

For the pre-build comparison, stop once the baseline has frozen its proposed repair/design and expected tests; implementation itself is not necessary for the primary detection measure.

### Candidate arm — proposed lifecycle

Use the same historical problem/evidence but apply the WP-021 proposed process:

1. Development Planner-style work/route selection from the historical objective/evidence;
2. Designer problem definition independent of the assumed repair mechanism;
3. conditional Researcher work only if a material evidence gap is identified;
4. independent alternative/layer generation where the solution space is materially underdetermined;
5. fresh pre-build Adversarial Reviewer against the frozen problem/design;
6. Designer synthesis/build-readiness.

Stop before implementation for the primary comparison.

The candidate arm may not cite later findings or current WP-021 analysis as technical evidence. It may use only the process structure being evaluated.

## Independence requirements

- Each work-producing trial starts in a fresh isolated execution/context.
- Baseline and candidate trials do not read one another's outputs.
- Pre-build adversarial reviewer does not read the future hidden finding.
- The evaluator receives frozen outputs only after the trials complete.
- Where the same underlying model is used, record that independence is contextual/trajectory separation, not model-level independence.

## Trial count

Minimum directional-development evidence:

- **3 fresh baseline trials and 3 fresh candidate trials per historical checkpoint** when execution budget permits.

This yields 18 work-producing trials across the three checkpoints before evaluator adjudication.

The purpose is not statistical significance. Multiple trials are required only to avoid treating one stochastic trajectory as the process itself.

If execution budget cannot support the declared count, the protocol must record the shortfall and the result cannot be represented as a completed comparison.

Do not increase the trial count after seeing favourable/unfavourable results merely to change the conclusion. Any extension rule must be declared before inspecting the evaluated outputs.

## Budget fairness

Before trials begin, record comparable resource bounds for each arm:

- model/configuration where controllable;
- maximum elapsed/agent budget;
- tool/web access;
- maximum externally loaded evidence not already in the snapshot;
- number of independent perspective/reviewer executions.

The candidate arm may legitimately use more executions because that is the process under test, but its added cost must be measured rather than hidden.

## Frozen evaluator rubric

The evaluator applies this rubric only after all relevant work outputs are frozen.

### Primary metric — hidden material failure-class pre-build coverage

For each held-out finding classify each trial:

- **0 — missed:** no materially equivalent concern/model appears;
- **1 — partial:** related concern appears but does not expose the failure path/property strongly enough to alter the design or verification plan;
- **2 — surfaced:** materially equivalent failure class/property is identified before build and changes the proposed design, protected-property model, route or negative test plan.

Exact wording is not required. Merely naming generic risk terms is not sufficient.

The evaluator must cite the frozen trial output that supports the score.

### Protected-property generality

Classify whether the trial reasons at:

- local example/patch level;
- identity/stream level;
- candidate-set/state-space level;
- explicit epistemic/protected-property level where applicable.

This is descriptive evidence, not an automatic quality score.

### False/unsupported concerns

Count concerns that would materially expand/reject the design but lack support in the historical state or credible external evidence.

Do not penalise a legitimate uncertainty merely because it was not the eventual historical finding.

### Scope expansion

Record whether the proposed work remains bounded to the Phase-0 problem or unnecessarily expands into generic platform/product architecture.

### Cost/coordination measures

Record per trial/arm where measurable:

- number of model executions/roles;
- wall-clock time;
- approximate token/context input where available;
- number/size of required files loaded;
- web/research calls;
- handoffs;
- owner interventions/questions;
- blocked/ambiguous routing events.

### Owner-burden test

Any technical question transferred to the Human Owner that could reasonably have been derived/researched counts as a negative process event.

### Completion/decision quality

Record whether the trajectory ends with:

- one clear build-ready design or justified decision not to build yet;
- explicit protected properties/reopen conditions;
- a verification/negative-test plan capable of failing red;
- unresolved ambiguity clearly routed rather than silently filled.

## Evaluator comparison

The candidate process is not considered better merely because it produces more text, more risks or more artefacts.

Directional evidence in favour of the candidate requires:

1. at least one held-out material failure class is surfaced more reliably/strongly before implementation than in the baseline trials; and
2. the improvement is not explained by future-information leakage; and
3. no new systemic owner-orchestration or route-livelock failure appears; and
4. added cost/coordination is recorded and judged proportionate to the observed reliability benefit.

If the candidate provides no material pre-build detection advantage, or its coordination/owner burden is clearly worse, WP-021 design must be simplified/reopened before governance implementation.

No fixed aggregate score or arbitrary pass percentage is established before baseline data exists. The evaluator must publish the per-trial rubric evidence and a bounded synthesis rather than hide judgement behind a composite number.

## Contamination checks

Before accepting a replay result, verify:

- no trial loaded branches/files after the historical checkpoint;
- no prompt included names/descriptions of held-out findings;
- no current SOUL chat/memory summary was used as task evidence;
- candidate process instructions describe **how to work**, not the hidden answer;
- external research, if used, was prompted by a contemporaneous evidence gap and not by knowledge of the later finding;
- evaluator did not alter the rubric after reading candidate results.

Any contaminated trial is invalid and must be discarded/re-run before synthesis. Do not silently treat it as partial evidence.

## Prospective limitation

Even a strong historical replay result cannot establish generalisation because the lifecycle was designed using lessons from this failure lineage.

Therefore WP-021 requires at least one prospective material trajectory after lifecycle adoption. The standing F-AR-008/result-control lineage is the planned first prospective use because the **next** post-build reviewer finding, if any, is not known when this protocol is written.

## Required artefacts when executed

- environment/snapshot manifest for each replay checkpoint;
- frozen baseline and candidate instructions;
- one record per trial with exact execution identity/context boundary and outputs;
- contamination check per trial;
- frozen evaluator rubric/version;
- per-trial scoring/evidence;
- synthesis separating observation from inference;
- explicit cost/coordination comparison;
- limitations/generalisation warning.

## Stop conditions

Stop/reopen the replay design rather than continuing if:

- exact historical snapshots cannot be isolated from later history;
- the execution harness cannot prevent current-branch/future-finding access;
- baseline and candidate budgets are so different that comparison becomes uninterpretable;
- evaluator independence is compromised;
- trial cost materially exceeds the declared WP-021 evaluation budget without owner-authority justification.
