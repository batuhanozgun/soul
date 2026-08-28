# SESSION-0032 — Phase 0 Candidate-Set Convergence Verifier

**Date:** 2026-08-28
**Work package:** WP-018 — Phase 0 Candidate-Set Convergence Verification
**Role:** fresh separate verifier
**Result:** **PASS**
**Result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Verifier branch:** `codex/wp018-verifier-fresh-20260828`
**Exact verified material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Material target PR:** #22
**Provisional activation:** `fbe517bef10b5e820dc096a8a82e2c1a3047a38c`
**Activation binding:** `e62075228054f43f4dc8d318210ce9de0bf8b8ae`
**Canonical state inspected through:** `c8b3cb97dfdf95f8b6f7f49e3e7140950128b560`
**Verifier evidence PR:** #24
**Initial published PASS head:** `73988f806fcf554885b12c3e8fd394ee9a766d24`

## Entry, independence and responsibility

The session used a new clean isolated clone created directly from live
`origin/phase0/development-os` and a new verifier branch. It did not use or
modify the dirty `/Users/Batu/SOUL` worktree, its uncommitted/divergent state or
`.DS_Store`.

The session entered through canonical `development/03_plan/COLD_START.md` and
completed Steps 1–2 in exact order: `STATE.md`, active WP-018,
`SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, common `REASONING_POLICY.md`, then
verifier `ROLE_MODEL.md` and `VERIFICATION_POLICY.md`.

The first all-state WP-018 activation-bridge check found no current result,
conflict, uncontained invalid/uninspectable candidate, discovery failure or
canonical candidate control. The sole WP-018 PR locator was merged PR #23;
direct inspection proved it was the three-file WP-017 close/routing package,
not a verifier-result candidate.

Before opening the exact PR #22 material files, producer evidence/model or
SESSION-0030, the session fixed the 12-row WP-000 and 23-row WP-018 expected
matrix in the verification artefact at checkpoint
`ade3d3219f74ec7ab038f9c68f50ba1780193232` (initial SHA-256 `7c6cca23...`).
Canonical WP-017 and live metadata necessarily exposed producer claims during
required A-stage reading; they were treated only as hypotheses.

Only afterward did the session inspect all ten exact target files, ADR-0002,
all three producer evidence records, the control template, executable model,
SESSION-0030 and the exact activation/binding/SESSION-0031 chain.

The final bridge check then refreshed origin and live GitHub. Canonical state,
key and activation remained exact; PR #22/#19/#21 pull refs remained exact; PR
#23 remained the only WP-018 locator and no WP-018 result candidate or blocker
existed. The verifier role and one responsibility were declared immediately
afterward with no intervening reading, planning, branch creation or substantive
action. All decision evidence was re-executed after commitment.

The sole responsibility was to issue PASS / FAIL / NOT VERIFIED for exact PR
#22 material plus exact activation, publish only the verification artefact and
this handoff, and stop for a separate Integrator. No repair, candidate
resolution/containment, attempt advancement, canonical transition, adversarial
re-review, ADR acceptance, target merge, Phase acceptance or Phase 1 work was
authorised or performed.

## Required inputs read

- canonical COLD_START Steps 1–2 and all WP-018 Step-3A readings;
- all four foundation files, WP-000, roadmap, relevant templates and complete
  source/working/reasoning/role/decision/change/verification governance and
  PR/Phase gates;
- immutable F-AR-001 through F-AR-007 review records;
- WP-015 verification, SESSION-0026, WP-016 review, SESSION-0028 and
  SESSION-0029;
- live PR #19/#21/#22/#23/#1 metadata, refs and exact scopes;
- exact PR #22 diff and all ten blobs at `5bd0db2...`;
- target ADR-0002, three producer evidence records, executable model and
  result-control template;
- SESSION-0030 builder and SESSION-0031 activation-Integrator handoffs;
- activation `fbe517b...`, binding `e620752...` and later session/index-only
  `c8b3cb9...` changes;
- subordinate launch/index views only after authoritative inputs.

## Work and evidence

- Live PR #22 remained open/draft/unmerged at exact `5bd0db2...`, based on and
  merge-based at exact `4524f21...`, with four commits and ten files. Every API
  file SHA matched the fetched target blob; `git diff --check` passed.
- Live PR #19 remained closed/draft/unmerged at immutable `2f5508c...`, nine
  files, with explicit supersession text preserving WP-015/WP-016 bindings.
- PR #21 remained merged evidence-only from `c2c4460...` as `276132a8...` with
  exactly the WP-016 review + SESSION-0028.
- All immutable F-AR review, WP-015/WP-016 and protected foundation/governance/
  roadmap/Phase/product blobs were compared unchanged. Exactly one COLD_START
  exists and historical `BUILDER_STOP.md` remains absent.
- Live canonical repository identity was inspected directly as GitHub
  repository id `1345974984`, node id `R_kgDOUDnyyA`, full name
  `batuhanozgun/soul`; candidate-set provenance must bind the immutable canonical
  identity rather than mutable locator spellings.
- Independent oracle `/private/tmp/wp018_independent_oracle.py`, SHA-256
  `237dadfbc25ca156dddb601b014ead0756f120ea4cbc9c35f941bc575d386b02`, imported
  no producer code and passed **33/33** routes; invalid-first and blind-set
  mutants were both rejected red.
- Producer-subject adversarial harness
  `/private/tmp/wp018_producer_adversarial.py`, SHA-256
  `2d907d1ee2ba82283a3d375e913f54693e2d51c664d8950cf6c31d4b2b6ec7d5`, passed
  **29/29** extra ordering, identity, authority, outage and lifecycle checks.
- Exact producer model SHA-256 `05e9ce33...` passed **67/67** declared cases
  only as corroboration. Its opt-in invalid-first mutation failed non-zero/red
  after 26 prior PASS observations at the first mixed valid/invalid case.
- Total positive deterministic observations: **129**, plus three mutant
  rejections.

## Verification status

**PASS** for all twelve current WP-000 criteria and all twenty-three WP-018
criteria, bound only to exact target/base/activation/binding/key above.

No evidence-backed verification failure was found. The exact artefact is:

`development/06_reviews/VERIFICATION-WP-000-5bd0db27-2026-08-28.md`.

PASS does not accept ADR-0000/0001/0002, PR #22, PR #1, WP-000 or Phase 0 and
does not substitute for fresh separate adversarial re-review.

## Preserved limitations

- repository-wide GitHub discovery/inspection outage fails closed;
- contained candidate-specific inaccessibility is non-valid and later
  inspectability must still validate directly;
- canonical repository identity/provenance must use immutable host identity,
  not only mutable name/URL metadata;
- publication after the final check is a documented residual host edge, not a
  platform lock;
- deterministic models abstract host transactions;
- same-model isolated verification is not true model diversity;
- ADR-0002 remains proposed and fresh adversarial re-review remains mandatory.

## Outputs

- exact-target verification artefact above;
- this SESSION-0032 handoff;
- dedicated evidence PR #24 targeting `phase0/development-os`, initially
  published at immutable PASS head `73988f806fcf554885b12c3e8fd394ee9a766d24`
  with exactly these two files. Immediate all-state discovery found PR #24 as
  the sole current valid WP-018 verifier result and routes a fresh session to a
  separate Integrator.

## Decisions

None. The verifier issued evidence only.

## Unresolved items

- separate Integrator validation/integration of the dedicated evidence PR;
- canonical PASS transition and routing to fresh separate adversarial re-review;
- later reviewer-result integration and any finding repair/resolution;
- ADR-0000/0001/0002, PR #22/#1, owner/PR/Phase gates;
- Phase 1 remains blocked.

## Exact next responsibility

**Separate Integrator for the dedicated WP-018 verifier evidence PR.**

The Integrator must validate immutable head, exact two-file scope, both exact
key/target/base/activation/binding records and **PASS** without reinterpretation;
integrate evidence only; transition canonical state; and route to fresh separate
adversarial re-review. It must not repair the target, accept ADR-0002, merge PR
#22/#1, accept Phase 0 or begin Phase 1.
