# Evidence — SOUL Development Reasoning Policy Synthesis

**Date:** 2026-08-26  
**Purpose:** Record the source material and the distinction between observed source rules and the SOUL-specific synthesis used to design `REASONING_POLICY.md`.

This is development evidence, not an authority that overrides the resulting policy, active WP, or repository state.

## Source material inspected

### KEEL-Work

- `CLAUDE.md` — blob `fb43ad9a9facfecf61bfb9a6c149e813134da801`: Claude entry is only a router; durable session rules live behind `AGENTS.md`/`SISTEM.md`.
- `AGENTS.md` — blob `5b745a9062daa1450f2b185bd42b27170bcb2fd3`: deterministic cold-start, one canonical writer, evidence-before-state close, writer cannot grant final closure, repository state over chat memory.
- `SISTEM.md` was read through the routing chain: source homes are separated by responsibility; derived views do not override sources; observed/inferred/assumed/verified claims are distinguished; same-text second reading is not external proof; owner value judgement is separated from technical verification.

### keel-dev

- root `CLAUDE.md` — blob `dbc2d8fb5892d823c8f5b6f3ab6b1108387f006a`: state-dependent routing and no execution before the full active-step specification is loaded.
- `00_genesis/CLAUDE.md` — blob `cd1b5bd2a80dc06ba8348fd85e6b5f9d936ac626`: deterministic session opening and machine-carried progression.
- `GENESIS.md` — blob `a04b80607915644ea56524d2fa87c6177f34949d`: every Genesis session must load the defect model; producer declaration is not completion; templates exist to prevent silent category evaporation; durable state is externalised.
- `00_genesis/DEFO_MODELI.md` — blob `e9bddf5e04e13d90dbb6014eb432fba18357f6ac`: documented failure tendencies include sycophancy, mirroring, scope inflation, drift, fabrication, self-approval, over-questioning, decision dumping and concealment; the common control principle is observable trace or mechanical enforcement rather than introspective self-judgement.

### oyun2

- root `CLAUDE.md` — blob `dbc2d8fb5892d823c8f5b6f3ab6b1108387f006a`.
- `00_genesis/CLAUDE.md` — blob `f2f41fbf3e0d128d417a7fb2d8f869e8f089d21d`.
- `00_genesis/GENESIS.md` — blob `9de57b6e28e4094143da05a198c641acb97c91a6`.

These confirm that the KEEL development rules were propagated into an installed project instance. They are not treated as independent conceptual evidence from keel-dev when the content is the same.

### os-architect

- `CLAUDE.md` — blob `2eb682f06d75295facfc58681eb6b9d0123d1342`: do not obey the plan or queue blindly; understand the work and why it exists; question whether a mechanism would exist if designed from scratch; separate product-manager/planner, producer and verifier motivations; environment and project truth must outlive model memory.
- `kurallar/calisma-disiplini.md` — blob `96bf6a5ab77825e77d718254cb8c70ad669947ce`: acceptance before work, red-capable tests, evidence anchors outside the controlled side, claims and rationales require measurement, inspect modes where controls do not run, do not skip unexpected errors.
- `bilgi/keel/sahip-seansi-2026-08-cerceve-korlugu.md` — blob `8b46b92a07276bd4dc9ebfde8dbf94f97cd66717`: repairing inside the existing frame can hide the question of whether the mechanism belongs at that layer at all; missing questions can be more important than missing answers; current mechanisms exert anchoring pressure; ask whether the mechanism should exist and whether another layer is superior.
- `bilgi/keel/sahip-seansi-2026-08-13-kok-neden.md` — blob `b7577de3f974becef1b23debe1f2897d645fd427`: distinguish the immediate defect from why the defect was not anticipated; continue root-cause questioning until the controlling cause is reached; learned lessons need a mechanism that invokes them at the relevant moment.
- `bilgi/keel/arastirma-seansi-2026-08-akil-yurutme.md` — blob `5be6e1f3ea26b6e8ccf0bff70fdb3f7aa73ceaac`: reported reasoning is not a reliable window into causal internal process; more reasoning can worsen incomplete-premise tasks; premise checking should be a distinct short pass; deterministic verification and fresh critic separation outperform unsupported self-correction; retrieval does not make retrieved content true.
- `kurallar/batu-ile-konusma.md` — blob `e1b56792019fc72203e36b892a5fae2bcef068b7`: do not invent terminology, do not create fake owner choices, technical validation is not an owner responsibility, answer a question before converting it into a plan.
- `kurallar/yazma-kapilari.md` — blob `40683777619e6056596e48e44e9d81cff3bc67a4`: avoid duplicate knowledge homes and remove persistent artefacts that do not change behaviour.

### keel-research

- `START_HERE.md` — blob `f52884aab74e2c763d67f751f4a84b13d8fcffa6`: a fresh context must recover purpose, active package, current result and next action from repository state rather than conversation replay.
- `FOUNDATION.md` — blob `708cad94e9733611f2468981245bacd4f148df27`: owner value judgement is distinct from technical/epistemic judgement; use established terminology; one role should have one coherent motivation unless counter-evidence shows coordination cost dominates; function necessity and motivation placement are separate questions.
- `OPERATING.md` — blob `5922a8909d9e9a35cf5c41d4241a98a5b804fe42`: research method may change without silently changing the owner-defined objective; primary sources and falsification are preferred; similarity is not equivalence; existing tools must not determine architecture by default; ask whether a function is needed before deciding which role owns it; avoid unmeasured architectural machinery.

## Source-derived principles carried forward

The sources support the following recurring principles:

1. Persist project truth outside chat/model memory.
2. Separate objective, method, current state, evidence and decision authority.
3. Distinguish direct observation from inference, assumption and verified result.
4. Do not treat producer confidence, tool success, repeated model agreement or retrieved content as proof.
5. Treat existing plans, mechanisms and tools as hypotheses rather than privileged defaults.
6. For material architecture, test framing, necessity, alternatives/layers and falsifying evidence.
7. Separate owner value/scope decisions from technical questions the system can research or derive.
8. On failure, analyse both the immediate defect and why the system failed to anticipate/prevent/detect it.
9. Prefer observable traces and enforceable controls over self-instruction when the property can be mechanised.
10. Avoid both under-thinking and indiscriminate over-thinking; deeper reasoning should be triggered by risk, ambiguity, novelty, irreversibility or material claims.
11. Preserve independent verification and exact-target freshness.
12. Record decision-relevant rationale/evidence, not purported hidden chain-of-thought.

## SOUL-specific synthesis decisions

The following are design choices made for SOUL from those principles; they are not verbatim rules asserted by every source:

- one canonical `development/01_governance/REASONING_POLICY.md` will apply to all SOUL development roles;
- `COLD_START.md` remains the only session sequencing authority and loads the reasoning policy as shared governance, avoiding a second bootstrap order;
- the policy uses always-on epistemic rules plus trigger-based deeper checks rather than forcing full first-principles analysis for every atomic action;
- material architecture decisions require explicit framing, necessity, alternatives/layer, falsification, evidence/uncertainty and authority checks;
- failures require proximal-cause plus root-cause analysis and a regression path;
- analytical claims require a claim-to-computation/input/source chain appropriate to risk;
- observable records must capture assumptions, evidence, alternatives, rationale, uncertainty and verification obligations when material, while explicitly not requiring private chain-of-thought.

These synthesis choices require architecture review and fresh Phase 0 verification before acceptance.
