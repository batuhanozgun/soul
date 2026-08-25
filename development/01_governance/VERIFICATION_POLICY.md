# VERIFICATION POLICY

Verification asks whether the work satisfies the authoritative specification and whether material claims are actually supported. It is distinct from evaluation, which asks how good, useful, or robust the result is.

## Core rules

1. The producer's declaration is not proof.
2. Tool success or exit code is not sufficient when the claim concerns the semantic result of the tool.
3. Another model instance agreeing is not independent evidence by itself.
4. Deterministic checks are preferred when the property can be checked deterministically.
5. Evidence must be inspected at the level needed by the claim; a citation that merely exists is not enough if its content does not support the claim.
6. `NOT VERIFIED` is a legitimate outcome and must not be coerced into pass/fail confidence language.
7. Verification must use the current artefact and current acceptance criteria; stale green results do not certify later changes.

## Verification hierarchy

Use the strongest applicable layer first:

1. invariant / schema / type / permission checks,
2. deterministic tests and reproducible commands,
3. direct artefact and source inspection,
4. analytical/statistical validation when relevant,
5. semantic model-based review when deterministic validation is insufficient,
6. human review for declared human-authority decisions or risk gates.

Higher numbered layers do not replace lower numbered checks that are available.

## Verification record

A material verification artefact should state:

- claim or acceptance criterion,
- evidence inspected,
- method,
- result: PASS / FAIL / NOT VERIFIED,
- limitations,
- verifier session,
- artefact/version/commit verified.

## Independence

For material architecture and control changes, the verifier must operate in a fresh session or isolated execution and read the authoritative specification before reading the builder's rationale. The purpose is to reduce anchoring and self-confirmation; it does not create true model independence when the same underlying model is used.

## Analytical work

When a claim depends on calculation or data, verification must be able to inspect the relevant chain at a level appropriate to the risk: claim → computation → input data → source/version. Merely showing that real data or a tool was used does not prove the final claim was derived from it.

## Completion gate

A WP may be marked `verified-complete` only after every required acceptance criterion has a current PASS or an explicitly authorised exception. The working session that produced the artefact cannot grant this state to itself.
