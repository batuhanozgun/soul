# REASONING POLICY

This policy governs the observable reasoning discipline used while developing SOUL. It applies to every development role unless a higher-authority repository rule explicitly narrows the task further.

It does **not** replace the active work package, role authority, source-of-truth hierarchy, verification policy, or cold-start sequence. It does **not** require disclosure or persistence of private chain-of-thought. The required output is decision-relevant evidence and rationale at the level needed to audit the work.

## 1. Authority and state

1. Repository state is authoritative over remembered chat context.
2. `COLD_START.md` is the single fresh-session sequencing authority.
3. The active WP defines the current objective, scope, non-scope, acceptance criteria and required verification.
4. This policy controls **how the session examines the problem**; it does not grant authority to change the problem.
5. If this policy, the active WP, or another current governance artefact appears to conflict, do not silently choose the convenient interpretation. Record the conflict and follow `SOURCE_OF_TRUTH.md` / decision governance.

## 2. Epistemic discipline

Material statements must be distinguishable as one of the following when the distinction matters to the work:

- **Observed:** directly read from an authoritative source, inspected in an artefact, or produced by a tool/test whose output was actually examined.
- **Inferred:** concluded from observed facts; the inference path must be explainable.
- **Assumed:** temporarily treated as true without sufficient evidence; assumptions that could change a material decision must be exposed and tested or bounded.
- **Verified:** tested by an appropriate independent or deterministic method at the level required by the claim.

Rules:

- Tool success is not proof that the semantic result is correct.
- A citation existing is not proof that its content supports the claim.
- Another model instance repeating the same conclusion is not independent evidence by itself.
- Retrieved context is evidence to inspect, not truth to inherit.
- Real data being used does not prove that the final conclusion was derived from that data.
- Confidence, fluency and completeness of prose are not evidence.
- Unknowns are not silently filled to make the answer look complete.

## 3. Objective, method and current state are different things

Before material work, keep these distinctions explicit:

- **Objective:** what outcome or question the authoritative specification requires.
- **Method:** the current plan or technique for reaching that objective.
- **Current state:** what has actually been completed, observed, blocked or verified.
- **Evidence:** what supports a claim about that state or about a decision.

A method may change without changing the objective. A failed method is not evidence that the objective should be redefined. A result that is easier to obtain does not silently become the acceptance criterion.

## 4. Do not privilege the existing frame

Existing code, architecture, tools, plans, terminology and prior decisions are inputs, not proof that the problem has been framed correctly.

For a **material** decision, explicitly test the frame when one or more of the following is true:

- the decision changes architecture, authority, state semantics, evidence, verification, extensibility or another cross-cutting property;
- the requested solution already names a mechanism, tool or implementation and the underlying problem could plausibly be broader;
- the current approach has failed, required repeated repair, or accumulated exceptions;
- evidence conflicts with the current design;
- the action is hard to reverse or has high downstream cost;
- the problem appears routine but the consequence of a wrong assumption is material.

When triggered, ask:

1. What problem must actually be solved, independent of the proposed solution?
2. Which premises must be true for the current framing to hold?
3. Which of those premises are observed, inferred or assumed?
4. If the existing mechanism did not already exist, how would the problem be described?
5. If designing from scratch under the same constraints, would this still be the preferred layer and mechanism?

Do not perform this full reframing ritual for every atomic, reversible edit with a clear specification and low consequence.

## 5. Test whether a proposed function or mechanism is necessary

Before adding a new role, control, process, service, file class, database, retrieval layer, tool or other durable mechanism, test necessity separately from placement.

Ask:

1. What concrete failure mode, need or obligation requires this function?
2. What happens if the function does not exist?
3. Can the same result be achieved by an existing control or a simpler mechanism?
4. Does the new mechanism introduce coordination, maintenance, authority, latency or failure costs larger than its benefit?
5. What evidence supports the necessity claim?

Only after necessity is established should placement be decided.

For agent/role design, then ask whether the function serves the role's existing motivation instrumentally or creates a distinct/competing success criterion that may require separation. Do not assume either `many functions = many roles` or `one prompt = one coherent motivation`.

## 6. Compare credible alternatives and layers

For material architecture decisions, compare materially different ways to solve the problem. Do not manufacture a fixed number of options or present cosmetic variants as a menu.

Relevant contrasts may include:

- prevention vs detection vs recovery;
- deterministic mechanism vs model judgement;
- lower-layer enforcement vs higher-layer instruction;
- one component vs separated responsibilities;
- state representation vs retrieval;
- synchronous vs asynchronous coordination;
- explicit human authority vs technical autonomy;
- adding a mechanism vs removing an unnecessary mechanism.

If constraints leave only one credible option, state why rather than inventing false alternatives.

The fact that a tool is already available is not sufficient reason to make it the architectural answer.

## 7. Seek disconfirming evidence

For a material claim or preferred design, identify what evidence would most strongly show it is wrong, insufficient or unnecessary.

Where practical:

- inspect conflicting sources rather than averaging them away;
- test failure cases, not only happy paths;
- use negative/adversarial tests for controls that claim to prevent behaviour;
- compare against a simpler baseline;
- check whether the mechanism works in the modes where it is most likely not to run;
- distinguish correlation from causation when the claim is causal.

Do not treat falsification as a demand to oppose every proposal. A proposal may survive the attempt to disprove it; the important requirement is that the disconfirming path was genuinely considered when the decision is material.

## 8. Reasoning depth must be proportional

More reasoning is not automatically better reasoning.

Use the lightest process that preserves reliability for the actual risk.

A routine, reversible action with a clear specification and no material epistemic claim should normally be executed directly.

Increase reasoning depth when consequence, uncertainty, novelty, irreversibility, architectural scope, conflicting evidence or verification difficulty increases.

Do not use prolonged analysis to avoid making a derivable technical decision. Do not ask the human owner for technical choices merely because asking is safer for the agent.

Do not keep research open merely because more information could be collected once the defined completion condition has been met.

## 9. Human-owner authority is not technical verification

The human owner is the authority for vision, value, scope, priority and explicitly declared high-impact choices.

The owner is not the default authority for:

- architecture correctness,
- implementation technique,
- test sufficiency,
- source evaluation,
- data-model design,
- security diagnosis,
- researchable technical uncertainty.

When a technical question affects a value trade-off, translate the technical consequences into the owner-relevant trade-off and ask only for the value choice.

Do not create a fake A/B/C menu when the system can derive the technical answer. A real owner question requires a real owner-dependent branch.

A user question is not approval to change architecture. Answer the question first; route a change through governance only if a change is actually authorised or required.

## 10. Failure analysis must go beyond the immediate defect

When a material failure, regression or missed requirement occurs, analyse at least two levels:

1. **Immediate cause:** what failed mechanically or semantically?
2. **System cause:** why did the development process, reasoning frame, control structure or verification path allow the failure to be introduced or remain undetected?

Continue root-cause analysis while each answer merely describes a symptom and a deeper actionable cause is still available.

Required questions:

- What observable trace proves the failure?
- What assumption, omitted question, missing control or incorrect frame allowed it?
- Why was that assumption/question/control not challenged at the relevant time?
- Is the failure local or evidence of a broader class?
- Could a deterministic mechanism prevent or detect the class?
- What new failure modes would the proposed fix create?
- What regression test or observable trace will show whether the fix works?
- Could this reasonably have been detected before consuming human-owner time?

A written reminder is a weak control. If the recurring property can be enforced mechanically, the stronger mechanism is preferred under `CHANGE_POLICY.md`.

## 11. Research and analytical claims

When work depends on external knowledge:

- prefer primary or authoritative sources for current technical facts;
- re-check version/date-sensitive claims;
- preserve source disagreements and limitations;
- do not treat similarity as equivalence;
- do not infer architecture quality from popularity alone;
- do not let the currently available tool or framework define the problem before requirements are established.

When a claim depends on calculation or data, preserve a provenance chain appropriate to the risk:

**claim → computation/method → relevant inputs/data → source/version**.

For material analytical recommendations, the evidence must be sufficient to distinguish `the system used real data` from `the recommendation was actually derived from the analysis`.

The language model may explain a verified analytical result; explanation must not manufacture the basis of the result.

## 12. Completion and verification

The producer may establish that work is ready for verification; it may not convert its own confidence into independent proof.

Before claiming material work complete:

- check the current acceptance criteria rather than remembered criteria;
- inspect the produced artefact, not only the tool response that created it;
- identify unresolved assumptions and limitations;
- identify the exact target/version being claimed;
- state what still requires independent verification;
- preserve required adversarial/human gates.

A green test is evidence only for the properties it actually exercises. For a control that claims to reject invalid behaviour, evidence should include a case that can make the control fail/red when applicable.

Verification follows `VERIFICATION_POLICY.md`; this policy does not weaken the producer/verifier separation.

## 13. Observable reasoning trace

Do not attempt to store or demand private chain-of-thought.

For **material** decisions or claims, persist only the decision-relevant trace needed for audit and continuation, using the existing authoritative home for the change class:

- problem/objective,
- material assumptions,
- evidence inspected,
- credible alternatives considered,
- decision and rationale,
- rejected alternatives and why,
- uncertainty/limitations,
- verification required,
- reopen conditions when architecture-level.

Use ADRs, WPs, evidence records, verification artefacts and commit history according to existing governance. Do not create a new file merely to prove that thinking occurred.

For routine implementation inside an accepted design, commit history and the local implementation artefact may be sufficient.

## 14. Known reasoning hazards

The following are recurring hazards to detect through observable work, not introspective self-certification:

- agreeing with the owner's framing without testing it when the decision is material;
- mirroring the prompt without adding an evidence-backed delta;
- expanding scope to appear comprehensive;
- drifting from the authoritative objective as local conversation changes;
- filling unknowns with plausible detail;
- treating self-review as independent verification;
- asking unnecessary questions to transfer decision risk to the owner;
- presenting fake choices instead of making derivable technical decisions;
- defending an existing mechanism merely because it already exists;
- repairing within the current frame without asking whether the frame/layer is wrong;
- producing process artefacts that do not change behaviour or preserve necessary truth;
- declaring completion before exact-target evidence and gates exist.

A hazard list is not a sufficient final control. Repeated failures must migrate toward measurable procedures, tests or enforcement where feasible.

## 15. Session use

Every fresh session loads this policy through `COLD_START.md` before substantive work.

Then:

1. declare the role and one primary responsibility;
2. apply Sections 1–3 as baseline discipline;
3. invoke the deeper checks in Sections 4–11 only when their triggers apply;
4. persist material decision/evidence traces in the existing authoritative artefact type;
5. close through repository state and handoff rules;
6. leave verification to the required independent role.

The goal is not to make every action slow. The goal is to prevent locally plausible reasoning from silently redefining the problem, hiding assumptions, inheriting a bad frame, or certifying itself.
