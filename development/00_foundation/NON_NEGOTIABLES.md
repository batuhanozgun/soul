# SOUL NON-NEGOTIABLES

These are architectural constraints, not implementation preferences. Changing one requires an explicit architecture decision and evidence that the replacement preserves or improves the underlying property.

1. **Repository state outranks conversation memory.** No critical project truth may exist only in chat history or model memory.
2. **The producer does not certify its own success.** Self-declared completion is never sufficient for material work.
3. **Evidence is not narrative.** A plausible explanation cannot substitute for an observable trace, source, computation, artefact, or explicit human decision when those are required.
4. **Authority is explicit and bounded.** Agents, tools, workflows, and generated capabilities cannot silently widen their own permissions or decision scope.
5. **State, memory, context, and knowledge are different concepts.** They must not be collapsed into a single ever-growing prompt or undifferentiated store.
6. **A human is neither a fallback search engine nor a hidden orchestrator.** Researchable, derivable, and system-internal questions remain system responsibilities; human involvement is reserved for genuine judgement, values, authority, approval, and defined risk gates.
7. **Fresh-session continuation is a design requirement.** A correctly prepared new session must be able to continue without depending on latent recollection of previous sessions.
8. **Missing capability is explicit.** The system may create or integrate a missing capability only through a defined build/test/verify/admit process; it may not improvise an unregistered capability invisibly inside a task.
9. **Critical state cannot be controlled solely by the component it constrains.** Budgets, permissions, acceptance criteria, verification state, and similar control inputs require authority separation or protected storage appropriate to their risk.
10. **Failure must be representable.** Unknown, unverified, blocked, partially complete, stale, conflicted, and failed are legitimate states; the architecture must not force them into success/failure prose.
11. **Repeated failures should become controls where practicable.** If a failure class can be prevented or detected deterministically, adding another prompt reminder is not the preferred final fix.
12. **One fact should have one authoritative home.** Derived views may exist, but duplicated authoritative state that can drift is prohibited.
13. **General-purpose does not mean one fixed workflow.** Domain-specific operating systems are generated above a stable core; domain assumptions must not leak into the core merely because a pilot needs them.
14. **Core evolution is governed.** A running task cannot silently rewrite the rules by which its own correctness, authority, or completion are judged.
15. **Observability is part of correctness.** If the system cannot explain what state it is in, why it took an action, what evidence supports a material result, or why it stopped, the work is not considered fully controlled.
