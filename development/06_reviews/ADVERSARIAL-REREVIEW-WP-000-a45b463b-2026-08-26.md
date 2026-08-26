# ADVERSARIAL RE-REVIEW — WP-000 / F-AR-001 REPAIR

**Reviewer session:** SESSION-0017  
**Reviewed commit/artefact:** `a45b463b083604d3f59d75bdca5ba97d5bc170e6`  
**Authoritative specification:** `development/04_work/WP-000-DEVELOPMENT-OS.md`; `development/04_work/WP-010-PHASE0-F-AR-001-REPAIR-ADVERSARIAL-REREVIEW.md`  
**Reviewer output branch:** `review/wp010-f-ar-001-repair-adversarial-rereview-2026-08-26-1247`  
**Date:** 2026-08-26

## Pre-evidence attack model

This attack model was persisted after COLD_START Steps 1–2 and WP-010 Step 3A, and before inspecting WP-008 builder rationale, the six-file repair diff, WP-009 verifier conclusions, or the WP-009 Integrator routing conclusion. Initial attack-model commit: `6ba3db435afb859b1e1b4ac10a2c58044c1d5d51`.

The pre-evidence hypotheses covered guard discovery shape, metadata/content spoofing, stale/target-mismatched evidence, conflicting/ambiguous/incomplete evidence, discovery/inspection failure, verifier/reviewer asymmetry, freshness races, transition-only laundering, evidence-to-authority leakage, self-transition, false completion, historical-result confusion, hidden non-evidence changes, recovery dead ends, denial-of-progress, cross-WP contamination, circular assurance, and broader WP-000 regressions.

## Exact target and transition inspection

### PR #13 freshness at review start

Direct PR #13 inspection at review start showed:

- state: open;
- draft: true;
- base: `phase0/development-os`;
- head: `repair/wp008-f-ar-001-cold-start-result-discovery`;
- exact head SHA: `a45b463b083604d3f59d75bdca5ba97d5bc170e6`;
- exactly six changed files, matching the WP-008 declared repair scope.

The material target therefore matched WP-010's fixed target at review start.

### Exact repaired control surface inspected

The reviewer directly inspected the exact target versions of:

- `development/03_plan/COLD_START.md`;
- `development/01_governance/WORKING_PROTOCOL.md`;
- `development/01_governance/VERIFICATION_POLICY.md`;
- `development/03_plan/PR_GATE.md`;
- proposed `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
- producer regression record `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md`.

The six-file repair does not edit WP-000 acceptance criteria or the historical WP-007 review evidence.

### WP-009 / PR #14 transition inspection

WP-009 issued **PASS** for exact target `a45b463...`. Verifier evidence PR #14:

- targeted `phase0/development-os`;
- contained exactly the WP-009 verification artefact and SESSION-0015 verifier handoff;
- was merged evidence-only as `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`.

The development-line transition from PR #14 base `b226e62f19e75510bf955b637fe3c3bea67d3069` to current `phase0/development-os` changes only verifier evidence/session files plus WP-009 completion, WP-010 routing, canonical `STATE.md`, subordinate index, and SESSION-0016 Integrator handoff. Those post-verification development-line changes are transition/routing evidence rather than edits to the six-file repair target. PR #13 remained unmerged and its material head remained separately frozen.

This classification does not cure the findings below.

## Findings

### F-AR-002 — The repair has no safe activation path for its own verifier/reviewer result intervals

- **Claim:** the pending-result guard being reviewed exists only on unmerged PR #13. Canonical `phase0/development-os`, which `COLD_START.md` requires fresh sessions to enter through, still contains the pre-repair cold-start without Step 1A. Therefore the WP-009 verifier-close interval and the current WP-010 reviewer-close interval are not actually protected by the repair. A generic fresh `Başlat` after evidence publication but before the separate Integrator can still repeat the just-completed independent role — the exact F-AR-001 lifecycle.
- **Evidence:** PR #13 is still open/draft and unmerged at exact head `a45b463...`. The exact target `COLD_START.md` contains Step 1A pending-result discovery; current canonical `phase0/development-os/development/03_plan/COLD_START.md` does not. WP-009 verifier PR #14 was published while canonical state still assigned WP-009 until SESSION-0016 Integrator transitioned it. WP-010 explicitly requires this reviewer to publish evidence while leaving canonical state unchanged until another Integrator acts. No transition-only commit cherry-picks or otherwise activates Step 1A on the canonical development line before PR #13 acceptance.
- **Failure path:** reviewer/verifier completes → publishes dedicated evidence PR → canonical `STATE.md` still assigns the same independent WP/role → generic fresh `Başlat` reads canonical pre-repair `COLD_START.md` → no pending-result scan occurs → the same verifier/reviewer role is declared and may begin again before the evidence PR is discovered through non-canonical context → duplicate or conflicting independent work is created.
- **Impact:** the repair is not self-hosting during the very lifecycle required to verify and adversarially review it. WP-000 cold-start/session-continuity controls remain unreliable during the repair's own mandatory gates, and the project still depends on a specially selected Integrator session or human awareness during that interval — the mechanism F-AR-001 rejected as insufficient. Canonical corruption is still mitigated by later Integrator checks, so the current evidence supports material rather than catastrophic severity.
- **Severity:** **medium — material**.
- **Disproof attempt:** checked whether Step 1A was already present on canonical `phase0/development-os` — it is not. Checked whether PR #14 integration or WP-009→WP-010 routing activated the repaired cold-start as a transition-only change — they did not. Checked whether derived Project/index/handoff surfaces may substitute — repository governance explicitly makes them subordinate and they cannot replace `COLD_START.md`. Checked whether the successful SESSION-0016 Integrator disproves the defect — it shows an explicitly selected Integrator can recover, not that generic cold-start can discover the pending result.
- **Result:** **stands**.

### F-AR-003 — Same-WP stale/ambiguous evidence can create a persistent cold-start livelock

- **Claim:** once the repaired Step 1A is active, it deliberately inspects open and merged/closed evidence PRs and routes any same-WP stale, target-mismatched, conflicting, ambiguous, incomplete, or uninspectable candidate to Integrator. However no durable resolution state, exclusion rule, or completion condition records that a particular invalid/stale candidate has already been resolved. Because closed/merged candidates remain in the discovery set, a stale or malformed same-WP PR can force every later fresh cold-start back into Integrator and permanently suppress the legitimate verifier/reviewer role.
- **Evidence:** exact target `COLD_START.md` Step 1A explicitly includes open and merged/closed evidence PRs, classifies same-WP stale/target-mismatched and conflicting/ambiguous candidates as fail-closed, and routes them to Integrator. `PR_GATE.md` repeats the fail-closed rule. `WORKING_PROTOCOL.md`, `VERIFICATION_POLICY.md`, ADR-0002 and the regression evidence define no persisted `resolved-invalid`, `superseded-for-guard`, quarantine, or equivalent mechanism by which a subsequent cold-start can distinguish an already-resolved stale/malformed same-WP candidate from a newly unresolved blocker. The rule to ignore historical evidence applies only after another-WP/role mismatch is established.
- **Failure path:** active WP `W` requires verifier/reviewer for target `T2` → a same-WP evidence PR exists for stale target `T1` or is incomplete/malformed → Step 1A correctly fails closed to Integrator → Integrator determines that the PR is not a current result, so there is no valid result to integrate and canonical state still correctly requires the independent role → closing the PR does not remove it from the next guard because closed PRs are explicitly searched → next generic cold-start sees the same candidate and routes to Integrator again → the independent role has no defined way to become executable without ad hoc mutation, a new WP invented to escape the residue, or another unspecified exception.
- **Impact:** the repair converts some unsafe duplicate-start cases into an unrecoverable or repeatedly recurring blocked state. That is safer than arbitrary result selection, but it does not satisfy the claimed **bounded** resolution property and creates a denial-of-progress/recovery-dead-end class against fresh-session continuity. A malformed or stale same-WP PR can become a durable control-plane obstruction.
- **Severity:** **medium — material**.
- **Disproof attempt:** checked whether closing a bad PR resolves it — Step 1A explicitly includes closed PRs. Checked for a persisted resolution/ignore status or candidate registry — none exists. Checked whether the Integrator is authorised to switch within the same session into the verifier/reviewer after classifying the candidate — current role separation and one-primary-responsibility rules provide no such transition, and the guard explicitly changes the effective role to Integrator. Checked whether creating a different WP is the declared resolution — no such rule or acceptance condition exists; doing so merely to escape historical residue would be an ad hoc control change.
- **Result:** **stands**.

### F-AR-004 — One-shot pending-result discovery has a check-then-act race

- **Claim:** the repaired guard is a one-time check immediately after Step 1. There is no lease, lock, atomic handoff, or mandatory re-check immediately before Step 4/substantive independent execution. A second session can publish the completed evidence PR after this session's Step 1A scan but before this session starts verifier/reviewer work, so the newly pending result is missed and duplicate work begins.
- **Evidence:** exact target `COLD_START.md` performs Step 1A once, then proceeds through Step 2 role governance and potentially extensive Step 3 required reading before Step 4 role declaration/work. No later freshness re-check is required. ADR-0002 explicitly records that the mechanism remains an agent/tooling-layer process rather than a platform-enforced transaction. The WP-009 verifier also records non-atomicity as a limitation.
- **Failure path:** sessions A and B start for the same independent role → B executes Step 1A while no evidence PR exists and proceeds → A finishes and publishes its evidence PR during B's Step 2/3 work → B has no mandatory second pending-result check and proceeds with the independent role despite a now-completed pending result → duplicate evidence may be produced.
- **Impact:** this is a narrower concurrency race than F-AR-002/F-AR-003, but it contradicts an unconditional interpretation of "before duplicate independent execution" and can still create duplicate/conflicting evidence. Later conflict handling contains canonical-state corruption but does not prevent the duplicated work.
- **Severity:** **low — real but timing-dependent**.
- **Disproof attempt:** checked whether Step 4 requires re-running Step 1A — it does not. Checked for repository locking/lease semantics or an atomic evidence-publication/state transition — none exists. The design acknowledges the non-transactional nature but does not bound this race with a second check.
- **Result:** **stands**.

## Candidate findings that did not survive as separate material findings

- **Metadata-only spoofing:** disproved as a direct canonical-authority bypass in the specified flow. PR title/body are locators only; current-match routing requires direct artefact/handoff and changed-file-scope inspection, and canonical transition remains a separate Integrator action. Malformed same-WP evidence can still block progress, but that impact is captured by F-AR-003 rather than counted twice.
- **Verifier/reviewer asymmetry:** no semantic asymmetry survived at the exact target; the publication/guard language explicitly covers both roles. F-AR-002 instead concerns activation timing before that common mechanism becomes canonical.
- **Transition-only laundering in WP-009→WP-010:** not established. The inspected post-PR-14 development-line changes are verifier evidence, WP-009 status, WP-010 routing, canonical state/index, and Integrator handoff. They do not edit the six-file repair target or WP-000 acceptance criteria.
- **Evidence becomes a second canonical state authority:** no direct path survived. The repaired text consistently states that evidence PRs are lower-authority triggers and that `STATE.md` + active WP remain canonical until Integrator transition.
- **False completion / ADR gate collapse:** disproved in the inspected target/transition. WP-009 PASS, ADR-0002 proposal status, adversarial re-review, PR #13 merge, Phase 0 acceptance and Phase 1 remain distinct gates.
- **Historical F-AR-001 rewriting:** disproved. The old WP-007 review artefact remains unchanged with F-AR-001 `stands`, medium/material, and overall `Requires repair` against old target `c690f858...`.
- **Hidden repair in verifier evidence PR #14:** disproved by exact changed-file scope; PR #14 contains only the verifier artefact and SESSION-0015 handoff.

## Acceptance-criteria assessment

WP-010 criteria for exact-target binding, adversarial independence, authority containment, historical preservation, reviewer scope discipline and evidence-backed close are satisfied by this review activity.

The repaired target does **not** survive the broader adversarial suitability test because:

- the original lifecycle remains reproducible during the repair's own unmerged verification/re-review rollout (F-AR-002);
- fail-closed stale/ambiguous same-WP handling lacks a durable bounded recovery state (F-AR-003);
- the one-shot guard retains a narrower TOCTOU duplicate-start race (F-AR-004).

No repair is performed in this reviewer session.

## Overall judgement

**Requires repair.**

The exact repair target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` should not proceed directly to ADR/PR/Phase acceptance. F-AR-002 and F-AR-003 are surviving medium/material findings; F-AR-004 is a surviving low timing-dependent weakness.

This reviewer evidence must be published in a dedicated evidence PR and then handled by a **separate Integrator**. The Integrator must preserve the findings and judgement without reinterpretation, integrate only authorised review/session evidence, and route the smallest bounded repair/resolution responsibility. Any material repair requires a new exact target and fresh verification/re-review as required by current governance.
