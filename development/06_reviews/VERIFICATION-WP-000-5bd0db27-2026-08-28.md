# VERIFICATION — WP-018 / CANDIDATE-SET CONVERGENCE REPAIR

**Verifier session:** SESSION-0032
**Result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Material target PR:** #22
**Provisional activation:** `fbe517bef10b5e820dc096a8a82e2c1a3047a38c`
**Activation binding:** `e62075228054f43f4dc8d318210ce9de0bf8b8ae`
**Verifier branch:** `codex/wp018-verifier-fresh-20260828`
**Date:** 2026-08-28

## Pre-producer expected criterion/result matrix

This matrix was fixed after canonical COLD_START Steps 1–2, the first complete
WP-018 live activation-bridge check and the Step-3A authoritative readings, but
before opening the exact PR #22 material diff/files, producer evidence/model,
producer control template or SESSION-0030 builder handoff. Producer claims
necessarily visible in canonical WP-017 and live PR metadata are hypotheses to
test, not proof and not the verifier decision function.

Decision rule: overall **PASS** requires current, exact and directly supported
PASS for all twelve WP-000 criteria and all twenty-three WP-018 criteria. A
demonstrated criterion violation is **FAIL**. Missing, stale, conflicting or
unavailable evidence that prevents the required determination is **NOT
VERIFIED**. Producer case counts cannot override this rule.

### First activation-bridge observation

- canonical `origin/phase0/development-os` at clone time:
  `c8b3cb97dfdf95f8b6f7f49e3e7140950128b560`;
- complete key:
  `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`;
- activation/binding chain: `fbe517b...` then `e620752...`; later canonical
  `c8b3cb9...` changes only SESSION-0031 plus its subordinate index row;
- exhaustive live all-state PR enumeration against `phase0/development-os`
  found only merged PR #23 mentioning WP-018; direct head/content/scope
  inspection classified it as the three-file WP-017 builder-close/routing
  package, not a verifier-result candidate;
- no current WP-018 result, conflict, canonical candidate control,
  uncontained invalid/uninspectable candidate or repository-wide discovery
  failure was observed, so Step 3 was permitted to continue.

### WP-000 expectations

| # | Expected property | Required independent evidence | Red / non-pass condition | Pre-producer state |
|---:|---|---|---|---|
| 1 | Cold-start sufficiency | A fresh canonical bootstrap identifies phase, active WP, complete key, role, readings and next responsibility; both live bridge checks execute. | Old-chat dependence, an undiscoverable current result, an uncontained blocker or ambiguous next responsibility. | Expected PASS; pending execution |
| 2 | Single-source discipline | `STATE.md` + the active WP remain canonical; same-level conflicts block; PR/evidence/control/index data remain subordinate. | A locator or control silently overrides canonical state, or a conflict is selected for convenience. | Expected PASS; pending execution |
| 3 | Work boundedness | WP-000/WP-018 expose objective, scope/non-scope, outputs, criteria, evidence, verification and handoff. | Verification or completion escapes the declared WP. | Expected PASS; pending execution |
| 4 | Role separation | Producer, verifier, reviewer, Integrator and owner authorities remain distinct. | Verifier can repair, resolve/contain, advance, integrate, re-review, accept or merge. | Expected PASS; pending execution |
| 5 | Decision governance | Architecture changes remain proposed ADR material with explicit review/owner gates. | Evidence or implementation silently becomes accepted architecture truth. | Expected PASS; pending execution |
| 6 | Verification discipline | Exact target/key freshness, PASS/FAIL/NOT VERIFIED, deterministic-first checks and direct evidence/provenance inspection remain required. | Stale, metadata-only, self-certified or circular evidence can pass. | Expected PASS; pending execution |
| 7 | Change safety | WP-000 criteria and governing authority remain unchanged; constrained actors cannot self-authorise controls. | Target relaxes criteria or lets candidate/producer/verifier widen authority. | Expected PASS; pending execution |
| 8 | Session continuity | Exact-key artefact + handoff publication is discoverable and routes a fresh session without prior-chat replay. | Published WP-018 result interval duplicates verification or becomes a dead end. | Expected PASS; pending execution |
| 9 | Development/product separation | Ten-file repair and verifier outputs do not alter or copy into `system/`. | Development governance/evidence leaks into product without an accepted reason. | Expected PASS; pending execution |
| 10 | Roadmap completeness | The existing full dependency chain remains present and unweakened. | Target removes or short-circuits required phases/dependencies. | Expected PASS; pending execution |
| 11 | No false completion | Verification, re-review, ADR, owner, PR and Phase gates remain separate and outstanding. | PASS/evidence integration is treated as target, ADR, PR or Phase acceptance. | Expected PASS; pending execution |
| 12 | Reasoning-policy sufficiency without duplicate authority | One canonical reasoning policy is loaded through COLD_START and preserves epistemic, proportional-depth, owner/technical and private-reasoning boundaries. | A second bootstrap/reasoning authority or self-verification path appears. | Expected PASS; pending execution |

Historical F2-R1 red condition: any surviving unmarked competing current-work
pointer, including `BUILDER_STOP.md`, fails criterion 2.

### WP-018 expectations

| # | Expected property | Required independent evidence | Red / non-pass condition | Pre-producer state |
|---:|---|---|---|---|
| 1 | All current WP-000 criteria pass | Twelve-row assessment above plus exact repository invariants. | Any WP-000 row is FAIL or NOT VERIFIED. | Expected PASS; pending execution |
| 2 | PR #22 identity/freshness | Live open/draft PR, base ref/SHA, source/pull refs, merge-base and exactly ten declared paths agree at start, pre-publication and close. | Head/base/scope moves or cannot be inspected. | Expected PASS; pending execution |
| 3 | PR #19 supersession preserves history | Live PR #19 remains closed-unmerged at `2f5508c...`; historic exact bindings remain unchanged. | Old target/result evidence is mutated, reused or PR #19 is merged/amended materially. | Expected PASS; pending execution |
| 4 | WP-015/WP-016 and F-AR-001–007 preservation | Immutable blobs/results/targets compare unchanged; new result does not inherit certification. | Finding wording/result/target is weakened, erased or retargeted. | Expected PASS; pending execution |
| 5 | First fixed invalid head resolves exactly once | Independent oracle: unresolved invalid routes exact-head resolution; exact canonical resolution then permits the role absent other blockers. | Fixed invalid blocks forever or is ignored before exact resolution. | Expected PASS; pending execution |
| 6 | Same-PR movement escalates once | After exact `h1` resolution, directly inspected invalid `h2` requires one stream-containment event. | `h2` is ignored or endlessly handled as fresh exact-head resolution. | Expected PASS; pending execution |
| 7 | Fresh-PR identity escalates once | After an earlier canonical invalid-candidate control, a directly inspected invalid claim at a distinct PR identity requires one candidate-set-containment event. | Fresh PR is ignored or restarts an unbounded per-PR cycle. | Expected PASS; pending execution |
| 8 | Long fresh-identity sequence converges | With valid candidate-set containment, many later inspectable-invalid fresh PRs require no new canonical controls. | Any later invalid identity resets recovery or requires another control. | Expected PASS; pending execution |
| 9 | Candidate-set identity/authority exact | Exact canonical repository plus WP, role, target and attempt are bound; control is canonical-before-use and Integrator-only. | Partial/wrong repository/key, local, forged, candidate-authored or unproven control unblocks. | Expected PASS; pending execution |
| 10 | Every inspectable head is directly validated | Containment is applied only after candidate inspection and never substitutes for result validity. | A contained/known candidate bypasses direct head validation. | Expected PASS; pending execution |
| 11 | One current-valid result always wins | Valid + first/moved/multiple/inaccessible invalid residue routes result Integrator before invalid-control work. | Any invalid residue delays or suppresses the sole current-valid result. | Expected PASS; pending execution |
| 12 | Multiple current-valid results conflict | Two or more current exact-key results remain explicit conflict despite invalid residue/containment. | Ordering, recency or control selects/suppresses a current result. | Expected PASS; pending execution |
| 13 | Invalid controls cannot unblock/suppress/accept | Wrong-key/repo, local, forged, candidate-authored, noncanonical and unproven records all fail closed. | Any such record enables the role, hides a result or implies acceptance. | Expected PASS; pending execution |
| 14 | Active-key change ends containment scope | Changing any of WP, role, target or attempt invalidates prior candidate-set containment. | Old-key containment affects a new active key. | Expected PASS; pending execution |
| 15 | Candidate lifecycle is bounded and non-accepting | Closed, force-pushed, deleted/inaccessible, reopened and later-corrected states follow explicit routes without reset or validity inference. | Lifecycle state fails open, resets forever or becomes evidence validity. | Expected PASS; pending execution |
| 16 | Discovery and inspection failures fail closed | Repository-wide discovery and uncontained/candidate-uncovered inspection failure block; only exactly covered candidate-specific inaccessibility is contained non-valid. | Global outage or uncovered candidate becomes a clean role route. | Expected PASS; pending execution |
| 17 | F-AR-001–005 controls remain intact | Current-result discovery, fixed recovery, activation, timing, exact movement convergence and later-valid behavior are replayed. | Any prior repaired failure reappears. | Expected PASS; pending execution |
| 18 | Producer model matches normative precedence and can fail red | Independently derive the oracle first; inspect/run producer model afterward; deliberate invalid-first mutation must fail. | Producer model is the verifier oracle, keeps invalid-first behavior or cannot demonstrate red. | Expected PASS; pending execution |
| 19 | Canonical authority remains unchanged | Direct semantic comparison leaves `STATE.md` + active WP canonical and PR/evidence/control records subordinate. | Candidate-set control becomes a current-state or acceptance authority. | Expected PASS; pending execution |
| 20 | Role authority remains separate | Policy/template/output scope reserve control, attempt, integration, review and acceptance authority. | Verifier or candidate gains any reserved power. | Expected PASS; pending execution |
| 21 | WP-018 activation is exact and self-hosting | `fbe517b...` is substantive provisional rollout, `e620752...` binds it exactly, unbound state fails closed and publication interval is protected without accepting general governance. | Binding/key drift, material misclassification, unprotected close or implied acceptance. | Expected PASS; pending execution |
| 22 | ADR/PR/human/Phase gates stay separate | ADR-0002 remains proposed; PR #22/#1 and Phase 0 remain unaccepted/unmerged; re-review remains required. | Verification collapses or waives a later gate. | Expected PASS; pending execution |
| 23 | Verifier scope discipline | Evidence PR contains exactly this artefact and SESSION-0032 handoff. | Repair, control, state/WP transition, attempt advancement, re-review, acceptance or merge appears. | Expected PASS; pending execution |

## Overall result

**PENDING EXECUTION.**

The expected-result checkpoint above is not a verification result. It is the
pre-producer decision matrix required by WP-018. The exact material files,
producer evidence/model and builder handoff have not yet been used to decide any
row.
