# ADR-0002 — Pending Independent Result Discovery Before Role Selection

**Status:** proposed — pending independent verification, adversarial re-review, and Phase 0 acceptance  
**Decision class:** Architecture decision  
**Date:** 2026-08-26  
**Supersedes:** none  
**Superseded by:** none

## Problem

WP-007 established material finding F-AR-001: a generic fresh-session cold start can begin a duplicate independent verifier/reviewer execution during the legitimate interval after that independent role has completed its result but before a separate Integrator has transitioned canonical `STATE.md`.

The observed verifier case is SESSION-0011: canonical state still assigned WP-006 verifier work while completed verifier evidence existed in PR #10, and a generic cold-start created duplicate verifier work before discovering that evidence. The reviewer-close case reproduced the same lifecycle shape: PR #12 contained the completed WP-007 adversarial review + handoff while canonical state still assigned WP-007 reviewer work until the separate Integrator acted.

The existing separation is intentional and must remain: verifier/reviewer roles may publish evidence, but they may not canonically integrate their own result. Therefore the repair cannot simply let the independent producer edit `STATE.md` on close.

## Decision scope

This decision governs the SOUL **development operating system** cold-start/result-publication lifecycle for independent verifier and adversarial-review results.

It does not define the eventual reusable SOUL runtime architecture, change WP-000 acceptance criteria, reinterpret F-AR-001/WP-007, or grant new acceptance authority to evidence producers.

## Constraints

- `STATE.md` + active WP remain the canonical current-work authority.
- `COLD_START.md` remains the single fresh-session sequencing authority.
- Verifier/reviewer output remains non-canonical until a separate Integrator performs the authorised transition.
- The repair must cover both the verifier and reviewer lifecycle cases, not a verifier-only special case.
- Ambiguous, conflicting, stale, target-mismatched, or uninspectable evidence must fail closed rather than silently selecting a result or starting duplicate work.
- Historical evidence and WP-000 acceptance criteria must remain unchanged.
- The mechanism must be repository-visible and usable without old-chat replay.

## Options considered

### A. Keep current flow and rely on handoff text / human awareness

Continue reading `STATE.md` and the active WP, with Integrator discovery happening only if the new session happens to notice prior evidence.

**Rejected:** this is the observed failure mode. SESSION-0011 demonstrates that reminder-level discovery is not reliable enough before role selection.

### B. Let verifier/reviewer advance canonical `STATE.md` when they close

Remove the post-result/pre-Integrator interval by granting the independent role canonical-transition authority.

**Rejected:** this collapses evidence production and canonical integration, violating role separation and the existing no-self-transition controls. It would solve discoverability by weakening a higher-value authority boundary.

### C. Add a second canonical pending-result pointer/file

Maintain a separate `PENDING_RESULT` current-state artefact that the independent role can update while `STATE.md` remains unchanged.

**Rejected:** this creates a second authoritative current-work surface that can drift or conflict with `STATE.md`, reproducing the stale/duplicate-state class Phase 0 already removed.

### D. Require discoverable evidence-PR publication and add a pre-role cold-start guard

Define a completed independent result as published only when its result artefact + handoff are placed in a dedicated evidence PR targeting the active development branch. Before loading/declaring an independent verifier/reviewer role, `COLD_START.md` deterministically checks for a same-WP pending evidence PR, validates its target/scope, and routes to a separate Integrator when a current result exists. Same-WP stale/conflicting/ambiguous evidence fails closed into bounded Integrator resolution.

**Decision:** chosen.

### E. Use only a PR label/title/sentinel as the result trigger

Use a label, title prefix, or small marker file as the authoritative signal that a result is ready.

**Rejected as sole mechanism:** these may help discovery but are not sufficient proof. Metadata or a marker can drift from the actual result/handoff/changed-file scope. The chosen design permits metadata as a locator but requires direct inspection before routing a current result.

## Evidence used

- `development/06_reviews/ADVERSARIAL-REVIEW-WP-000-c690f858-2026-08-26.md` — canonical F-AR-001 finding and disproof record.
- `development/07_sessions/SESSION-0011-PHASE0-WP006-INTEGRATOR.md` — observed duplicate-verifier execution before PR #10 discovery.
- `development/07_sessions/SESSION-0012-PHASE0-ADVERSARIAL-REVIEWER.md` — reviewer-close reproduction with PR #12.
- PR #10 — verifier evidence-only PR for WP-006 / target `c690f858e7682f5bdf0511c0f10b0e932d868b0e`.
- PR #12 — adversarial-review evidence-only PR for WP-007 / the same material target.
- `development/05_evidence/F-AR-001-PENDING-RESULT-REGRESSION-2026-08-26.md` — repair regression matrix and expected routing outcomes.

## Decision

SOUL development will preserve canonical state separation and add a **pending independent-result discovery guard** before independent role selection.

The architecture is:

1. **Publication boundary.** A verifier/adversarial-review result counts as a completed published repository result only after the role publishes its completed result artefact + handoff in a dedicated evidence PR targeting the active development branch. Branch-only output is incomplete publication.
2. **Canonical state remains unchanged on producer close.** The evidence producer does not edit `STATE.md` or integrate its own result.
3. **Pre-role guard.** After `COLD_START.md` Step 1 reads `STATE.md`, active WP, `SOURCE_OF_TRUTH.md`, and `WORKING_PROTOCOL.md`, but before Step 2 chooses role-relevant governance, it checks for a pending independent result when the active WP assigns verifier/adversarial-review work.
4. **Exact binding.** The guard resolves the expected target from the active WP and repository/PR metadata, then directly inspects same-WP evidence PR contents and changed-file scope. PR title/body are only discovery aids.
5. **Deterministic routing.** No same-WP published result means normal independent execution. Exactly one current same-WP/role/target evidence-only result means the session loads/declares Integrator instead and validates/transitions the pending result. Same-WP stale, target-mismatched, conflicting, ambiguous, incomplete, or uninspectable evidence blocks duplicate independent work and routes to bounded Integrator resolution.
6. **No authority promotion.** The guard only changes the fresh session's execution path. It does not make evidence canonical, reinterpret result semantics, or update project state. Canonical transition still belongs to the separate Integrator.

## Rationale

The defect is not that canonical `STATE.md` fails to change immediately; that delay is a deliberate authority-separation property. The defect is that the bootstrap procedure previously treated canonical role assignment as sufficient to begin execution without first checking whether the role had already published its lower-authority result.

The chosen design repairs the missing lifecycle guard at the bootstrap boundary rather than weakening producer/Integrator separation or adding a second current-state store. Standardising evidence-PR publication makes the pending result enumerable and inspectable. Exact target/scope validation prevents stale or narrative-only PR metadata from becoming a hidden authority channel.

The fail-closed path is necessary because the repository already contains historical/stale evidence PRs and future repeated executions could create multiple same-WP candidates. The guard must not choose whichever result is convenient.

## Consequences

### Positive

- generic cold-start cannot legitimately begin duplicate WP-006-style verifier work after a completed evidence PR is published;
- the same control covers adversarial-review close rather than special-casing verification;
- canonical state remains single-source and Integrator-owned;
- stale/conflicting evidence becomes an explicit bounded state instead of being silently ignored or selected;
- the control is repository/PR observable and auditable without old chat context.

### Costs and new risks

- independent result close now depends on creating an evidence PR; if PR publication is unavailable, the session must report incomplete publication rather than completion;
- cold-start incurs an additional PR discovery/inspection operation only when canonical state assigns an independent verifier/reviewer;
- repositories with many historical evidence PRs require correct active-WP/target filtering;
- a malformed evidence PR can block duplicate work until an Integrator resolves the ambiguity;
- the mechanism remains a development-process control executed by the agent/tooling layer rather than a platform-enforced transaction.

These costs are accepted because they preserve stronger authority separation while closing the observed duplicate-execution path. A stronger native transactional mechanism would be a reopen condition, not a reason to retain the current failure.

## Rejected alternatives and why

See Options A–C and E. They either retain the observed failure, collapse role authority, create duplicate canonical state, or treat weak metadata as proof.

## Verification required

Fresh independent verification must establish at the exact repaired target that:

1. `COLD_START.md` still has one bootstrap authority and keeps Step 1 semantic reading order intact;
2. the pending-result guard executes before independent role selection/Step 2 role-specific loading;
3. evidence publication requires result + handoff PR and does not grant verifier/reviewer canonical-transition authority;
4. historical WP-006 verifier state + PR #10 routes to Integrator rather than duplicate verifier;
5. historical WP-007 reviewer state + PR #12 routes to Integrator rather than duplicate reviewer;
6. unrelated historical evidence (including older WP evidence) does not become a false current result;
7. same-WP stale/target-mismatched/conflicting/ambiguous evidence fails closed into bounded Integrator resolution;
8. no WP-000 acceptance criterion, historical result, F-AR-001 wording, or WP-007 judgement was changed;
9. `CHATGPT_PROJECT_ENTRY.md` remains a derived pointer to `COLD_START.md` rather than a second copy of the guard;
10. the builder does not self-certify the repair.

After fresh verification, a separate adversarial re-review must attempt to break the new publication/discovery guard, including metadata spoofing, stale-result noise, multiple-result conflicts, discovery-tool failure, and authority leakage.

## Reopen conditions

Reopen this decision if:

- a supported repository host/tool cannot reliably enumerate evidence PRs during cold-start;
- evidence-PR publication materially harms independent-result workflow or creates recurring blockage;
- empirical use shows active-WP/target filtering produces false current-result matches;
- a stronger platform-native atomic handoff/transition primitive becomes available and can preserve producer/Integrator separation with less ceremony;
- fresh verification/re-review finds that the guard creates a second authority, weakens exact-target freshness, or fails either historical lifecycle case.
