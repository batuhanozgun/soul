# VERIFICATION — WP-018 / CANDIDATE-SET CONVERGENCE REPAIR

**Verifier session:** SESSION-0032
**Result-control key:** `WP-018 / verifier / 5bd0db27fc3df368c9e112f01b7eed49a64402ab / attempt 1`
**Material target:** `5bd0db27fc3df368c9e112f01b7eed49a64402ab`
**Material base:** `4524f21cced54c71fb2219b7f42119adbbb5b033`
**Material target PR:** #22
**Provisional activation:** `fbe517bef10b5e820dc096a8a82e2c1a3047a38c`
**Activation binding:** `e62075228054f43f4dc8d318210ce9de0bf8b8ae`
**Verifier branch:** `codex/wp018-verifier-fresh-20260828`
**Verifier evidence PR:** pending publication
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

**PASS** for exact material target
`5bd0db27fc3df368c9e112f01b7eed49a64402ab`, material base
`4524f21cced54c71fb2219b7f42119adbbb5b033`, and exact provisional WP-018
activation `fbe517bef10b5e820dc096a8a82e2c1a3047a38c` bound by
`e62075228054f43f4dc8d318210ce9de0bf8b8ae` under attempt 1.

All twelve current WP-000 criteria and all twenty-three WP-018 criteria PASS.
This result is permanently bound only to those exact inputs. It does not accept
ADR-0000/0001/0002, PR #22, PR #1, WP-000 or Phase 0; it does not merge any
target or substitute for the required fresh adversarial re-review.

## Independence and activation-bridge execution

The verifier used a new clean isolated clone from live
`origin/phase0/development-os`, never used or modified the dirty
`/Users/Batu/SOUL` worktree and did not read model memory or prior chat as
project authority.

Canonical COLD_START Steps 1–2 were completed in order. The first complete
WP-018 bridge check then re-read the active key, performed all-state live PR
discovery and directly inspected the only WP-018 locator, merged PR #23. Its
three-file scope is WP-017 close + proposed WP-018 + SESSION-0030, so it is not
a verifier-result candidate. No result, conflict, control or uncontained
blocker existed.

The 12-row + 23-row expected matrix above was persisted before producer
material at checkpoint commit `ade3d3219f74ec7ab038f9c68f50ba1780193232`,
initial SHA-256
`7c6cca23915565bb38b40a900f1f4cc5d71aaa1e587f60d2eb8098666ae2a959`.
Only afterward were the ten exact target files, ADR, three producer records,
control template, executable model and SESSION-0030 read.

The final bridge check then refreshed origin and GitHub immediately before role
commitment. Canonical head remained `c8b3cb97...`, the exact key/activation and
PR #19/#21/#22 pull refs remained unchanged, and PR #23 remained the sole
WP-018 locator with no current result candidate. The verifier role and this one
responsibility were declared immediately, with no intervening reading,
planning, branch creation or substantive action. All decision evidence below
was re-executed after that commitment.

## Exact target, supersession and freshness

- Live GitHub and fetched `refs/pull/22/head` agree on open/draft/unmerged PR
  #22, base `phase0/development-os`, exact base/merge-base `4524f21...`, exact
  head `5bd0db2...`, four commits, 1728 insertions / 6 deletions and ten files.
- Every GitHub changed-file blob SHA matched the corresponding exact target Git
  blob. `git diff --check 4524f21... 5bd0db2...` passed.
- Live PR #19 remains closed/draft/unmerged at exact `2f5508c...` from
  `dca520...` with nine files. Its body explicitly records supersession without
  amendment and preserves WP-015 PASS / WP-016 **Requires repair** plus
  F-AR-006/F-AR-007 only for that old target.
- Live PR #21 remains merged evidence-only from exact `c2c4460...` as
  `276132a8...`. The merge has parents `acf163f...` + `c2c4460...` and adds
  exactly the immutable WP-016 review and SESSION-0028.
- PR #1 remains open/draft/unmerged against `main`; PR #22 remains
  open/draft/unmerged. No material or Phase merge occurred.

Exact PR #22 scope:

1. `development/01_governance/VERIFICATION_POLICY.md`;
2. `development/01_governance/WORKING_PROTOCOL.md`;
3. `development/02_architecture/decisions/ADR-0002-PENDING-INDEPENDENT-RESULT-DISCOVERY.md`;
4. `development/03_plan/COLD_START.md`;
5. `development/03_plan/PR_GATE.md`;
6. `development/05_evidence/F-AR-001-TO-004-PENDING-RESULT-CONTROL-REGRESSION-2026-08-26.md`;
7. `development/05_evidence/F-AR-005-MOVING-CANDIDATE-CONVERGENCE-REGRESSION-2026-08-27.md`;
8. `development/05_evidence/F-AR-006-AND-007-CANDIDATE-SET-CONVERGENCE-REGRESSION-2026-08-27.md`;
9. `development/05_evidence/PENDING-RESULT-RESOLUTION-TEMPLATE.md`;
10. `development/05_evidence/pending_result_control_regression.py`.

## Executed WP-000 assessment

| # | Direct evidence and method | Result | Limitation |
|---:|---|---|---|
| 1 | Fresh canonical bootstrap resolved Phase 0, WP-018, exact key/activation, role/readings/next responsibility and both live bridge checks. | PASS | GitHub discovery is external and fails closed. |
| 2 | `SOURCE_OF_TRUTH.md`, `STATE.md` + active WP and target controls preserve one canonical current-work home; PR/evidence/control/index data are subordinate. Historical parent-WP handoff text is not the active current-work authority. | PASS | Same-level canonical conflict still blocks. |
| 3 | WP-000/WP-018 and the WP/session templates bind objective, scope/non-scope, outputs, criteria, evidence, verification and handoff. | PASS | None material. |
| 4 | `ROLE_MODEL.md`, policies, target template and output scope keep producer/verifier/reviewer/Integrator/owner powers separate. | PASS | Same-model isolated context is not true model diversity. |
| 5 | `DECISION_POLICY.md` remains unchanged and all three ADRs remain proposed. | PASS | All decision gates remain outstanding. |
| 6 | Target policy requires exact key/head/scope, PASS/FAIL/NOT VERIFIED, deterministic-first checks and direct artefact inspection; live refs/blobs were inspected. | PASS | Semantic Integrator classification remains reviewable governance. |
| 7 | WP-000 criteria and protected authority files are unchanged; controls are canonical-before-use, Integrator-only and non-accepting. | PASS | A wrongly canonicalised control remains correctable governance evidence, not invisible trust. |
| 8 | Exact-key two-record publication plus first/final/close bridge checks preserve fresh-session continuation. | PASS | Post-publication route is rechecked after the evidence PR exists. |
| 9 | Exact material diff and verifier outputs contain no `system/` path; `system/README.md` boundary is unchanged. | PASS | None. |
| 10 | Unchanged `ROADMAP.md` retains the complete Phase 0–13 dependency chain. | PASS | Later execution is outside WP-018. |
| 11 | Verification, Integrator transition, fresh re-review, ADR, owner, material PR and Phase gates remain explicitly distinct. | PASS | PASS is evidence, not acceptance. |
| 12 | Exactly one `COLD_START.md` exists; unchanged `REASONING_POLICY.md` retains epistemic, proportional-depth, owner/technical and private-reasoning boundaries; `BUILDER_STOP.md` remains absent. | PASS | General target governance remains proposed until later gates. |

## Executed WP-018 assessment

| # | Direct evidence and method | Result | Limitation |
|---:|---|---|---|
| 1 | Complete twelve-row WP-000 assessment above plus exact repository invariants. | PASS | As stated per row. |
| 2 | Live API, pull/source refs, Git merge-base, commit graph, ten API/blob matches and repeated freshness checks agree on exact PR #22. | PASS | Rechecked again immediately before result commit/publication/close. |
| 3 | Live PR #19 state/head/base/scope/body and fetched pull ref preserve closed-unmerged supersession. | PASS | PR metadata is locator; immutable head/blobs were also fetched. |
| 4 | Blob equality preserved immutable F-AR-001–007 review files plus WP-015/WP-016 records; no historical result/review/session path is in the target diff. | PASS | Historical results remain exact to old inputs only. |
| 5 | Independent oracle: first invalid `h1` -> exact resolution; exact canonical `h1` resolution -> canonical role. | PASS | No live malicious candidate was created. |
| 6 | Independent oracle: moved invalid `h2` after `h1` resolution -> one stream containment; later same-PR invalid heads converge. | PASS | Trigger proof remains direct Integrator inspection. |
| 7 | Independent oracle and producer-SUT harness: distinct invalid PR after prior exact/stream control -> one candidate-set containment. | PASS | No live control was created by this verifier. |
| 8 | Independent oracle replayed 50 fresh invalid identities; producer-SUT harness replayed 100; exact producer suite replayed 20. All converge after valid set containment without new controls. | PASS | Models abstract host transactions. |
| 9 | Policy/template bind exact canonical repository + all four key fields, canonical history and Integrator provenance. Live repository identity was independently fixed as GitHub repository id `1345974984` / node id `R_kgDOUDnyyA`; wrong repo/key/local/candidate/unproven controls were rejected. | PASS | A real control record must persist that immutable identity/provenance explicitly. |
| 10 | Normative policy requires direct validation before controls; independent and producer-SUT valid-under-containment tests prove no blind skip. | PASS | Inspectability remains required unless exact containment permits explicit non-valid inaccessibility. |
| 11 | All permutations and valid + first/moved/many/inaccessible invalid cases route the sole current result first. | PASS | Result routing is not acceptance. |
| 12 | Independent oracle and all six producer-SUT order permutations preserve two-current-result conflict despite invalid residue/containment. | PASS | Fresh attempt activation remains separate Integrator work. |
| 13 | Wrong WP/role/target/attempt, repository, head, local/noncanonical, candidate-authored and unproven controls never unblock, suppress or accept. | PASS | Control truth is established through canonical history/direct evidence. |
| 14 | Attempt-2 and wrong-key mutations demonstrate prior candidate-set controls end at any complete-key change. | PASS | Later canonical activation must expose the new complete key. |
| 15 | Closed/reopened/merged/force-pushed, deleted/inaccessible and later-corrected cases remain non-valid/non-resetting; later valid routes normally. | PASS | State labels alone never establish validity. |
| 16 | Global discovery failure and uncontained inaccessibility block; exactly covered candidate-specific inaccessibility is contained non-valid and later validation reopens. | PASS | External availability is not eliminated. |
| 17 | Real historical records plus independent routes preserve F-AR-001 discovery, F-AR-002 activation, F-AR-003 fixed recovery, F-AR-004 timing and F-AR-005 same-PR convergence. | PASS | The documented post-final host edge remains explicit. |
| 18 | Producer model SHA-256 `05e9ce33...` passed 67/67 only after the independent oracle. Invalid-first mutation failed red after 26 PASS observations at the first mixed case. Producer code was not the verifier oracle. | PASS | The model is routing evidence, not a GitHub runtime. |
| 19 | `STATE.md` + active WP remain canonical; target text repeatedly makes evidence/control/PR/template data subordinate and non-accepting. | PASS | None material. |
| 20 | Role policy, governance, template and actual verifier branch scope preserve verifier/reviewer/Integrator/owner separation. | PASS | Separate Integrator must validate publication. |
| 21 | `fbe517b...` immediately follows builder-routing head `7645ab1...` and is explicitly substantive provisional rollout; `e620752...` immediately binds it; later `c8b3cb9...` is session/index evidence only. Both bridge checks passed. | PASS | The bridge does not accept general PR #22 governance or eliminate the post-final host edge. |
| 22 | ADR-0000/0001/0002 remain proposed; PR #22/#1 and Phase 0 remain unaccepted/unmerged; fresh re-review remains required. | PASS | All gates intentionally remain open. |
| 23 | Verifier branch/PR is limited to this uniquely named artefact and SESSION-0032; no prohibited repair/control/state/review/acceptance/merge action is included. | PASS | Final evidence PR scope/head is inspected after publication. |

## Independent deterministic and repository evidence

- Independent oracle `/private/tmp/wp018_independent_oracle.py`, SHA-256
  `237dadfbc25ca156dddb601b014ead0756f120ea4cbc9c35f941bc575d386b02`, imports
  no producer code and passed **33/33** expected routes; its invalid-first and
  blind-containment mutants were both rejected red.
- Separate producer-subject harness
  `/private/tmp/wp018_producer_adversarial.py`, SHA-256
  `2d907d1ee2ba82283a3d375e913f54693e2d51c664d8950cf6c31d4b2b6ec7d5`, used
  the exact model only as the subject under test and passed **29/29** additional
  order/identity/provenance/lifecycle observations.
- Exact producer model, SHA-256
  `05e9ce33a6db32ba0009c0b95ee92a7087affa3847dc44c82bafb281d72093f3`, passed
  **67/67** declared cases as corroboration only. The opt-in invalid-first
  mutation failed non-zero/red after 26 prior PASS observations at
  `valid plus first invalid`.
- Positive deterministic observations total **129** (33 independent + 29
  adversarial producer-subject + 67 producer-declared), plus three red-capable
  mutant rejections.
- Protected foundation, WP-000, source/reasoning/role/decision/change, roadmap,
  Phase gate, historical review/session and `system/` paths are unchanged from
  material base. F-AR-001/F-AR-005 producer records are byte-identical to PR
  #19, while the exact repair delta adds/changes only the declared F-AR-006/
  F-AR-007 control surfaces.

## Findings and limitations

No evidence-backed verification failure was found.

Preserved limitations:

- GitHub repository/PR discovery and immutable-head inspection remain external
  capabilities; repository-wide loss fails closed.
- Candidate-specific inaccessibility after exact containment is deliberately a
  non-valid contained state, never proof of absence or validity.
- The repository/key identity must be recorded with immutable canonical host
  identity/provenance, not only mutable name/URL spellings.
- The deterministic models abstract host transactions and do not replace live
  PR/blob/scope inspection.
- Publication after the final bridge check remains the documented residual host
  edge with later conflict handling, not an atomic lock.
- Same-model fresh-context verification reduces anchoring but is not true model
  diversity.
- ADR-0002 and the general control remain proposed; fresh separate adversarial
  re-review is still mandatory.

## Publication and close evidence

Pending dedicated evidence-PR publication and immediate post-publication
all-state bridge inspection. The evidence PR must contain exactly this artefact
plus SESSION-0032, both carrying the complete key/target/base/activation/binding
and completed PASS.

## Required next responsibility

After publication, a **separate Integrator** must inspect the immutable evidence
PR head, exact two-file scope, both complete-key records and this PASS; integrate
evidence only; transition canonical state without reinterpretation; and route
PASS to a fresh separate adversarial re-review of exact target `5bd0db2...`.

The Integrator must not accept ADR-0002, merge PR #22/#1, accept Phase 0 or begin
Phase 1. This verifier does not perform that transition.
