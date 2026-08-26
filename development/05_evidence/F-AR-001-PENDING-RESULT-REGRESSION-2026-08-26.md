# F-AR-001 Pending Independent-Result Regression Evidence

**Date:** 2026-08-26  
**WP:** WP-008 — Phase 0 F-AR-001 Repair  
**Role producing this evidence:** designer/builder  
**Status:** producer regression evidence only — fresh independent verification required

## Purpose

Exercise the repaired cold-start/result-publication control against both lifecycle cases required by WP-008 and against obvious stale/conflict failure modes.

This record does not reinterpret F-AR-001 or independently verify the repair. It states the observable historical inputs and the deterministic routing outcome required from the repaired control.

## Repair invariant under test

When canonical `STATE.md` + active WP assign an independent verifier/adversarial reviewer whose result must be integrated by a separate Integrator:

1. a completed result must be published as a dedicated evidence PR containing the result artefact + handoff;
2. before loading/declaring the independent role, `COLD_START.md` resolves the expected exact target and checks same-WP evidence PRs targeting the active development branch;
3. exactly one current same-WP/role/target evidence-only result routes to Integrator, not duplicate independent execution;
4. same-WP stale/target-mismatched/conflicting/ambiguous evidence fails closed to bounded Integrator resolution;
5. evidence from a different historical WP is not treated as the current result;
6. evidence discovery does not mutate canonical state or reinterpret the result.

## Case V — observed verifier duplicate-start regression

### Historical authoritative state

At exact material commit `c690f858e7682f5bdf0511c0f10b0e932d868b0e`:

- `development/03_plan/STATE.md` named **WP-006** as active;
- required next responsibility was a fresh verifier;
- WP-006 required the verifier to capture the exact draft PR #1 head at verification start;
- draft PR #1 material head was `c690f858e7682f5bdf0511c0f10b0e932d868b0e`.

### Completed published independent result

Verifier evidence PR **#10** targeted `phase0/development-os` and was bound to:

- WP: **WP-006**;
- role: verifier;
- exact target: `c690f858e7682f5bdf0511c0f10b0e932d868b0e`;
- result: **PASS**.

Exact changed files:

- `development/06_reviews/VERIFICATION-WP-000-c690f858-2026-08-26.md`
- `development/07_sessions/SESSION-0010-PHASE0-REASONING-REVERIFIER.md`

SESSION-0011 records the observed pre-repair failure: a generic cold-start followed canonical verifier-required state and created duplicate verifier work before discovering PR #10.

### Repaired guard evaluation

- active independent WP/role: WP-006 / verifier;
- expected exact target: `c690f858...`;
- same-WP evidence candidate: PR #10;
- target match: yes;
- completed result + handoff: yes;
- evidence-only scope: yes;
- candidate count after validation: exactly one current match.

**Required repaired outcome:** effective fresh-session role becomes **Integrator** for pending result validation/integration. The verifier role must not begin again.

**Regression expectation:** SESSION-0011's duplicate-verifier branch creation path is blocked before substantive verifier execution.

## Case R — reviewer-close lifecycle regression

### Historical authoritative state

At pre-review development head `572f25be68d438a800ebbce3a854b3bcd09bb0b1`:

- `development/03_plan/STATE.md` named **WP-007** as active;
- required next responsibility was a fresh adversarial reviewer;
- WP-007 material review target was exactly `c690f858e7682f5bdf0511c0f10b0e932d868b0e`.

### Completed published independent result

Reviewer evidence PR **#12** targeted `phase0/development-os` and was bound to:

- WP: **WP-007**;
- role: adversarial reviewer;
- exact material target: `c690f858e7682f5bdf0511c0f10b0e932d868b0e`;
- overall judgement: **Requires repair**;
- surviving finding: **F-AR-001**, medium/material, stands.

Exact changed files:

- `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md`
- `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md`

SESSION-0012 records that after reviewer close the canonical development state still assigned WP-007 reviewer work until a separate Integrator transitioned it.

### Repaired guard evaluation

- active independent WP/role: WP-007 / adversarial reviewer;
- expected exact target: `c690f858...`;
- same-WP evidence candidate: PR #12;
- target match: yes;
- completed result + handoff: yes;
- evidence-only scope: yes;
- candidate count after validation: exactly one current match.

**Required repaired outcome:** effective fresh-session role becomes **Integrator** for pending review-result validation/integration. A second WP-007 adversarial review must not begin.

## Case N — unrelated historical evidence noise

Current repository history contains older evidence PRs for **WP-003** against exact old target `a02e36e5e71522995b74fb018a6b28235f1d7848` (including PRs #3–#8). Some remain open historically even though later WPs/targets superseded them.

When the active WP is WP-006 or WP-007:

- WP-003 != active WP;
- `a02e36e5...` != expected target `c690f858...`;
- those PRs are therefore unrelated historical evidence, not same-WP current candidates.

**Required repaired outcome:** they must not route the session as the current result and must not create a false conflict once their different WP/target is established.

This case is important because the guard must not equate "an evidence PR exists" with "the active result is complete."

## Case S — same-WP stale/target-mismatch (synthetic decision-table check)

Input condition:

- canonical state assigns verifier/reviewer for active WP `W`;
- expected target is `T2`;
- one published evidence PR contains a completed result for the same WP/role but exact target `T1`, where `T1 != T2`.

**Required repaired outcome:** do not begin another independent execution and do not treat the stale result as current. Route to bounded Integrator freshness/result-publication resolution so the stale result can be preserved/handled without being promoted.

This is a decision-table test; it is not claimed as an additional observed SOUL incident.

## Case C — conflicting same-WP current candidates (synthetic decision-table check)

Input condition:

- canonical state assigns verifier/reviewer for active WP `W` and expected target `T`;
- two or more published evidence PRs plausibly claim the same WP/role/target, or candidate records disagree on result/target/scope.

**Required repaired outcome:** fail closed. Do not choose one result and do not begin a further duplicate independent execution. Route to bounded Integrator conflict resolution.

This is a decision-table test for the failure mode that repeated independent executions could create multiple evidence results.

## Case U — discovery capability unavailable (synthetic decision-table check)

Input condition:

- active WP assigns verifier/reviewer;
- repository/PR discovery required by the guard cannot be performed or candidate changed-file/artefact scope cannot be inspected.

**Required repaired outcome:** the guard has not passed. Record the blocker/missing capability and do not assume "no pending result" merely because discovery failed.

## Builder assessment against WP-008 acceptance criteria

| WP-008 criterion | Producer evidence from repair |
|---|---|
| 1 — deterministic repository-visible pre-duplicate path | `COLD_START.md` Step 1A + evidence-PR publication contract |
| 2 — preserve canonical `STATE.md` + active WP | guard explicitly changes execution path only; evidence remains lower authority |
| 3 — preserve separate Integrator transition | verifier/reviewer publish PR but cannot update/integrate canonical state |
| 4 — SESSION-0011 verifier path blocked | Case V routes to Integrator before verifier execution |
| 5 — reviewer-close duplicate path blocked | Case R routes to Integrator before adversarial-review execution |
| 6 — ambiguity/stale/conflict handling | Cases S/C/U fail closed to bounded resolution |
| 7 — no historical/acceptance weakening | no WP-000 criterion or historical review/verifier artefact edited by this repair |
| 8 — exact repair target / independent gates | builder close must publish exact repair PR target and route fresh independent verification + re-review |

## Limitations / independent verification required

This is builder-produced evidence. It does not prove that the repaired controls are sufficient or that a fresh model/tool execution will obey them.

A fresh verifier must independently replay at least Case V and Case R from the exact historical state/PR evidence, test same-WP stale/conflict handling, inspect the exact repair target, and verify that no second bootstrap/state authority was created. A fresh adversarial re-review must then attempt to bypass or spoof the publication/discovery guard.
