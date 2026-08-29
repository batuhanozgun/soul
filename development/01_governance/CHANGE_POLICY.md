# CHANGE POLICY

SOUL must be able to evolve without allowing the running system or a convenient implementation patch to silently redefine the rules by which it is judged.

## Change classes

- **Foundation change** — vision, definition, non-negotiable properties.
- **Architecture change** — cross-cutting contracts, state semantics, authority, evidence, verification, runtime control, capability model, extensibility.
- **Work-package change** — scope, outputs, acceptance criteria, dependencies, required verification.
- **Implementation change** — local realisation inside accepted contracts.

Each class follows the decision requirements in `DECISION_POLICY.md`.

## No silent acceptance-criteria changes

Once substantive work begins, the producing role cannot relax or rewrite acceptance criteria merely because implementation proves difficult. A criterion may change only through an explicit WP change with rationale and impact analysis; architecture-level consequences trigger an ADR.

## Failure-to-change path

A repeated or high-impact failure should produce the following analysis:

1. What actually failed?
2. What observable trace proves the failure?
3. Why did existing controls not prevent or detect it?
4. Is the failure local or a class of failures?
5. Can it be prevented or detected deterministically?
6. What new control, invariant, test, policy, capability, or architecture change is justified?
7. What new failure modes does that change create?
8. How will the fix be regression-tested?

A prompt reminder may be used as a temporary mitigation only when no stronger enforceable mechanism is currently available and the limitation is explicitly recorded. It is not the preferred final answer to a mechanically preventable recurring failure.

## Self-extension

A capability created by SOUL or by the development process is not trusted merely because it was successfully generated.

Admission requires:

- explicit capability specification,
- authority and tool boundaries,
- dependency and risk analysis,
- isolated build or integration,
- tests appropriate to the capability,
- independent verification,
- registration into the capability model,
- rollback or disable path where practicable.

A generated capability may not modify the rules that govern its own admission or verification.

## Supersession

Accepted decisions and specifications are not silently edited to erase history when the semantics materially change. The change must preserve traceability through version history and, for architecture decisions, explicit supersession links.
