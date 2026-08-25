# DEVELOPMENT ROLE MODEL

These roles govern how SOUL is developed before SOUL can enforce the same separation itself.

## 1. Designer / Builder

Purpose: create the proposed architecture, specification, implementation, or artefact required by the active WP.

May:
- analyse the problem,
- propose alternatives,
- produce the primary artefact,
- identify assumptions and risks,
- propose ADRs.

May not:
- be the sole independent verifier of its own material output,
- silently change acceptance criteria to fit the result,
- convert its own confidence into evidence.

## 2. Researcher

Purpose: establish external or empirical evidence needed by a decision.

May:
- survey standards, literature, frameworks, implementations, and experiments,
- compare alternatives,
- record source quality, uncertainty, and limitations.

May not:
- silently turn research findings into architecture decisions,
- omit conflicting evidence merely because one option is preferred.

## 3. Verifier

Purpose: determine whether the artefact satisfies the work definition and whether material claims are actually supported.

Rules:
- derive expected results from the authoritative specification before relying on the producer's explanation,
- inspect evidence directly where possible,
- distinguish verified, false, and not-verifiable,
- prefer deterministic checks over another model's opinion when deterministic checks are possible,
- report gaps without fixing them inside the same verification act unless the WP explicitly assigns a separate repair responsibility,
- leave canonical result integration and result-dependent state routing to a separate integrator under `VERIFICATION_POLICY.md`.

## 4. Adversarial Reviewer

Purpose: try to break the proposed solution and identify failure modes that ordinary verification may miss.

Focus areas include:
- hidden assumptions,
- circular verification,
- duplicated or stale state,
- authority leaks,
- self-modification of controls,
- provenance gaps,
- silent failure,
- false completion,
- privilege escalation,
- context poisoning or uncontrolled context growth,
- agent-to-agent error propagation,
- recovery dead ends.

The reviewer is not rewarded for finding a fixed number of issues. No finding is a legitimate result if the evidence supports it.

## 5. Integrator

Purpose: reconcile verified work and completed independent-review results into repository state without smuggling unresolved decisions into `main`.

May:
- assemble accepted artefacts,
- resolve mechanical integration conflicts,
- ensure indexes and state references are coherent,
- inspect and integrate dedicated verifier/reviewer evidence,
- perform the explicit result-dependent canonical-state transition authorised by `VERIFICATION_POLICY.md`, including mechanical WP/status/state routing that does not alter the verifier's result or the parent acceptance criteria.

May not:
- decide unresolved architecture disputes merely to make a merge easy,
- reinterpret PASS / FAIL / NOT VERIFIED,
- perform substantive repair while claiming to execute a transition-only integration,
- use evidence integration as acceptance of the reviewed target,
- waive owner, ADR, adversarial-review, or fresh-verification gates.

## 6. Human Owner

The owner is the authority for:
- project vision and value judgements,
- explicit approval gates assigned to the owner,
- irreversible/high-impact choices when governance requires human approval,
- accepting or rejecting architecture decisions that are designated owner decisions.

The owner is not expected to act as:
- a search engine,
- a technical verifier,
- a substitute orchestrator for questions the system can research or derive.

## Separation rule

For material architecture work, design and independent verification must occur in separate sessions or clearly isolated executions with fresh context. Adversarial review is separate from both when the WP requires it. Verification-result integration is likewise a separate integrator responsibility when canonical state must change after a verifier closes.
