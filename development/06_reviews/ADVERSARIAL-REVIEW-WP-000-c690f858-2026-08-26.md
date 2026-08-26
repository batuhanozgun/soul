# ADVERSARIAL REVIEW — WP-000 / PHASE 0 DEVELOPMENT OS

**Reviewer session:** SESSION-0012  
**Reviewed commit/artefact:** `c690f858e7682f5bdf0511c0f10b0e932d868b0e`  
**Authoritative specification:** `development/04_work/WP-000-DEVELOPMENT-OS.md`; `development/04_work/WP-007-PHASE0-ADVERSARIAL-REVIEW.md`; foundation/governance controls named by WP-007  
**Reviewer output branch:** `review/wp007-phase0-adversarial-2026-08-26-1030`  
**Date:** 2026-08-26

## Pre-evidence attack model

This attack model was recorded after COLD_START Steps 1–2 and WP-007 Step 3A, and before reading the WP-006 verifier artefact, builder rationale, or Integrator conclusions required by Step 3B. It is intentionally hypothesis-first rather than conclusion-first.

### Attack surfaces and hypotheses to test

1. **Verifier-result transition discoverability:** canonical `STATE.md` may temporarily remain verifier-required after verification has actually completed elsewhere, causing a generic cold-start to duplicate verifier work or act on stale next-responsibility state.
2. **Freshness laundering through `transition-only`:** a post-target commit may be labelled or interpreted as mechanical routing while containing a semantic design, acceptance, authority, or verification-rule change that should stale the prior PASS.
3. **Authority leakage / role confusion:** builder, verifier, adversarial reviewer, Integrator, or owner boundaries may contain paths that allow one role to convert evidence into acceptance, repair its own finding, or transfer a derivable technical decision to the human owner.
4. **False completion / gate collapse:** PASS, evidence integration, ADR status, owner approval, PR merge readiness, and Phase acceptance may be conflated so that one gate accidentally substitutes for another.
5. **Duplicate bootstrap/current-state authority:** derived launch/index/session artefacts or policy text may materialise current role/WP/target values and drift from `STATE.md` or `COLD_START.md`.
6. **Reasoning-policy ritualisation:** `REASONING_POLICY.md` may add substantial prompt/process burden without a measurable behavioural control, creating ritualised overthinking or self-reported assurance instead of stronger controls for recurring failures.
7. **Hidden owner-decision transfer:** language about high-impact or uncertain choices may allow technical architecture/test/evidence decisions to be escalated to the owner even though the governance says they should be derived by the responsible technical role.
8. **Private-chain-of-thought boundary erosion:** observable-reasoning requirements may be interpreted as requiring persistence or disclosure of private chain-of-thought despite explicit prohibitions.
9. **PD-002 recurrence / fail-open activation order:** the active-WP/current-state mechanism may still permit work to begin from a not-yet-canonical WP or leave contradictory activation state without a deterministic stop.
10. **Change-safety / self-modification:** a constrained component/session may have a path to rewrite the acceptance criteria, authority, verification rules, or controls that judge its own success without the required decision process.
11. **Evidence/provenance weakness:** material claims, especially analytical or externally sourced claims, may be able to survive on narrative/citation existence without inspectable claim→method→input→source lineage.
12. **Development/product boundary leakage:** development governance, evidence, sessions, or review artefacts may be copied into `system/` or treated as product architecture without an accepted architecture reason.
13. **Recovery dead ends and stale/conflicted states:** blocked, stale, conflicted, NOT VERIFIED, or partial states may lack an explicit bounded next responsibility, encouraging conversational improvisation.
14. **Context growth / poisoning:** fresh-session loading obligations may grow until role context becomes indiscriminate or prior-session evidence crowds out current-authority material.

## Exact-target and post-target freshness check

The material review target is exactly `c690f858e7682f5bdf0511c0f10b0e932d868b0e`.

At review time draft PR #1 remained open/draft on `phase0/development-os`, whose head was `572f25be68d438a800ebbce3a854b3bcd09bb0b1`. Direct comparison from `c690f858...` to `572f25be...` is ahead by 11 commits and changes only verifier evidence/session records plus result-routing/current-state/review-routing surfaces.

The post-target ancestry was inspected at commit level:

- `53236f0862f7dc92e622e2b74f6a6542b03dc35b` — verifier pre-rationale expectation artefact only;
- `8daa4f92e393f353ea47e23e4ee82e95f47b130b` — verifier artefact completion only;
- `af089862c278ed38acc26cce0b89e25c81c99c12` — verifier session handoff only;
- `856c2cdf0a791501477d43dbe7419219f5dd62f0` — evidence-only merge of the two verifier output files;
- `4320627fce7e997bede76de6d388a0783987c21f` — creation/activation of WP-007 review routing package;
- `84072a2d71c60da505ee4285c420c496688d744c` — close WP-006 as verification activity and bind its issued result;
- `fff17d619ce5586bdca5f5d7e5477766ad510973` — canonical `STATE.md` result-dependent routing to WP-007;
- `d1648f8ef69c0204e875f0c2864293e1da6b6447` — subordinate index update;
- `71c04a180879c36046828dff8c79fa203257f394` — Integrator handoff only;
- `7dd70128d12280f68b4893fee03f04bf9c820456` — adds the Integrator-observed discoverability path to WP-007's attack scope; it changes review routing, not the verified material target or its acceptance criteria;
- `572f25be68d438a800ebbce3a854b3bcd09bb0b1` — subordinate index of SESSION-0011.

No post-target commit changes foundation, material design, WP-000 acceptance criteria, authority rules, verification rules, reasoning-policy semantics, or `system/` product content. The WP-006 PASS therefore remains current for the exact material target under the transition-only rule. The freshness-laundering hypothesis did not survive this check.

## Findings

### F-AR-001 — Generic cold-start cannot reliably discover a completed but unintegrated verifier result

- **Claim:** the verifier-result → canonical-state procedure defines what an Integrator must do after a verifier closes, but the generic cold-start path has no deterministic step that detects that closure while the result still exists only on the verifier branch/evidence PR. During that legitimate pre-integration interval, canonical `STATE.md` continues to assign the verifier role. A fresh generic `Başlat` can therefore start a duplicate verifier instead of selecting the required Integrator.
- **Evidence:** at material target `c690f858...`, canonical `STATE.md` assigns WP-006 / fresh verifier and says a separate Integrator acts only *after verifier close*. `COLD_START.md` resolves role/current responsibility from `STATE.md` + active WP before substantive work and does not require a pre-role scan for completed verifier evidence PRs/branches. `VERIFICATION_POLICY.md` correctly prevents the verifier from performing its own canonical transition, so verifier close intentionally leaves canonical state unchanged until an Integrator acts. SESSION-0010 records a completed PASS and Integrator handoff on verifier evidence PR #10. SESSION-0011 then records the concrete failure: a new generic cold-start followed canonical state, created duplicate branch `verification/wp006-phase0-reasoning-reverification-2026-08-26-1009`, and wrote one pre-rationale draft commit before discovering the already-completed verifier evidence. `CHATGPT_PROJECT_ENTRY.md` adds repository/PR resolution for the current development line but does not require discovery of completed verifier-result PRs before role selection.
- **Failure path:** verifier completes isolated verification and leaves evidence/handoff → canonical development `STATE.md` necessarily still says “fresh verifier required” → a later generic cold-start reads that authoritative state and declares verifier → duplicate verification begins before lower-authority verifier evidence is discovered → multiple verifier executions/results for the same target can exist, wasting work and potentially creating conflicting evidence that a later Integrator must disambiguate. The mechanism detects/corrects the condition only after duplicate work has already started; it does not prevent the wrong next responsibility from being selected.
- **Impact:** this breaks the intended repository-only cold-start/session-continuity property during an explicitly supported lifecycle state. In particular, WP-000 criterion 1 requires a fresh session to identify the current phase, active WP, authority, required readings, role, and **next responsibility** from repository state; criterion 8 requires handoff-based continuation without old-chat dependence. The repository contains the completed result, but the authoritative generic bootstrap path does not surface it before role selection. Canonical state integrity is not automatically corrupted because duplicate branches remain lower authority, which limits the severity, but autonomous multi-session routing is not reliable.
- **Severity:** **medium — material**. The defect has an observed execution trace and can select the wrong role / duplicate a material independent-verification activity. Existing separation/integration controls reduce the likelihood of silent canonical corruption, so high severity is not justified on current evidence.
- **Disproof attempt:** checked whether `COLD_START.md` searches completed verifier outputs before resolving the active role — it does not. Checked whether `CHATGPT_PROJECT_ENTRY.md` performs that discovery — it only resolves the current development line/open development PR. Checked whether `VERIFICATION_POLICY.md` makes verifier close canonical or permits the verifier to advance state — correctly, it does not; a separate Integrator owns the transition. Checked whether the risk was merely hypothetical — SESSION-0011 records an actual duplicate verifier branch and pre-rationale commit. Checked whether the later force-reset disproves the defect — it shows recovery after discovery, not prevention or correct initial next-responsibility resolution.
- **Result:** **stands**.

## Candidate findings that did not survive review

- **Freshness laundering:** disproved for the inspected post-target chain; every changed file/commit is verifier evidence or authorised routing/state/handoff/review-routing material and no verified-target semantic input changed.
- **Authority leakage / gate collapse:** no surviving path found. Verifier, reviewer and Integrator authorities remain separated; WP-006 PASS is repeatedly distinguished from ADR acceptance, Phase acceptance and PR merge authority; ADR-0000 and ADR-0001 remain proposed.
- **Duplicate bootstrap/current-state authority:** no current material defect found. `BUILDER_STOP.md` is absent; `NEXT_SESSION.md` stores no mutable current values; `CHATGPT_PROJECT_ENTRY.md` is explicitly derived; `WORKSPACE_INDEX.md` is explicitly subordinate. F-AR-001 is a transition-discoverability defect, not a second authoritative state home.
- **Reasoning-policy ritualisation / prompt-only assurance:** no material failure could be established from repository evidence alone. The policy uses risk-triggered depth, explicitly rejects self-reported compliance as verification, and ADR-0001 records ceremony/performance risk and reopen conditions. Empirical performance degradation remains unverified rather than assumed.
- **Hidden owner-decision transfer:** disproved at the architecture level inspected. `REASONING_POLICY.md` and `DECISION_POLICY.md` explicitly keep derivable technical/epistemic decisions with the responsible technical role rather than using the owner as a risk sink.
- **Private-chain-of-thought erosion:** disproved in current governance; the policy explicitly prohibits demanding or persisting private chain-of-thought and requires only decision-relevant observable rationale/evidence.
- **PD-002 recurrence as a separate current defect:** not established. PD-002 is preserved; current cold-start/working-protocol text makes active-WP discipline explicit. One bootstrap incident plus procedural/manual enforcement is residual risk, but this review found no second activation-order recurrence that would independently justify a new finding. F-AR-001 is a distinct observed lifecycle transition failure.
- **Self-modification/change-safety escape:** no concrete path survived. Material acceptance, authority and verification-rule changes require explicit governance and stale prior verification; the reviewer itself has no repair/acceptance authority.
- **Evidence/provenance gap:** no current acceptance claim was found that survives solely on citation existence or unsupported computation. Governance requires claim→method/computation→inputs/data→source/version where applicable.
- **Development/product leakage:** disproved at the exact target; `system/` contains only `README.md` and no development governance/review/session artefact was copied into product architecture.
- **Other recovery dead ends:** PASS/FAIL/NOT VERIFIED and repair/investigation routing are represented. The specific stale transition interval is captured by F-AR-001.
- **Cold-start/context burden:** additional reading cost exists and ADR-0001 acknowledges it, but this review found no empirical evidence establishing a material performance failure. It remains a reopen/measurement risk, not a surviving finding.

## Overall judgement

**Requires repair.**

The exact material target `c690f858e7682f5bdf0511c0f10b0e932d868b0e` is not suitable to proceed directly to the remaining Phase 0 ADR/human-owner/PR acceptance gates because F-AR-001 is a surviving material adversarial finding against the cold-start/session-continuity architecture.

This review evidence itself is ready for a **separate Integrator**. The reviewer performs no repair and no canonical transition. The Integrator should preserve this finding without reinterpretation and route the smallest bounded repair/decision responsibility allowed by current governance. Any material repair must trigger fresh exact-target verification and appropriate re-review before Phase 0 acceptance.
