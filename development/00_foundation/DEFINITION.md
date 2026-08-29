# SOUL DEFINITION

## What SOUL is

SOUL is a general-purpose agentic operating architecture that receives an intended outcome and establishes the controlled system required to pursue it.

That system may include task decomposition, specialised roles, tools, retrieval, state and memory mechanisms, evidence structures, policy gates, verification, evaluation, human approval, observability, recovery, and newly created capabilities.

SOUL must separate at least four concerns:

1. **Core** — invariant concepts, contracts, state transitions, authority rules, evidence rules, and safety/control principles that task-specific systems may not silently redefine.
2. **Genesis** — analysis of a new goal and construction of the task-specific operating system required to pursue it.
3. **Runtime** — execution, orchestration, context assembly, tool use, handoff, verification, evaluation, recovery, and completion of actual work.
4. **Evolution** — controlled conversion of observed failures, missing capabilities, and validated lessons into system changes without allowing the running system to silently rewrite its own rules.

## What SOUL is not

SOUL is not defined by a particular directory structure, current KEEL implementation, LLM provider, agent framework, programming language, retrieval technology, database, or user interface.

SOUL is not a claim that one fixed architecture is appropriate for every task. Its generality comes from being able to derive a task-specific working architecture under a stable control model.

SOUL is not an autonomous authority over the human owner. It must know which decisions can be researched or derived, which belong to bounded system roles, and which require human judgement or explicit approval.

## Input

At minimum, the user provides an intended outcome and enough interaction for SOUL to distinguish missing factual information from preferences, values, constraints, and approval boundaries that only the human can supply.

## Output

The output is not merely a final answer or artefact. A successful SOUL run produces:

- the requested outcome or a justified non-completion state,
- a traceable record of the work and decisions that materially led to it,
- evidence and verification appropriate to the risk of the work,
- explicit remaining uncertainty, limitations, and human decisions where relevant,
- persistent state sufficient for another fresh session to continue correctly.

## Completion

An agent saying that work is complete is never sufficient. Completion is a system state reached only when the active work definition's acceptance conditions, required verification, policy gates, evidence obligations, and human approvals have been satisfied.
