# Methodology and interpretive limits

## Purpose

The Atlas documents changes in model outputs and reasoning processes across contexts. It does not assume progress, stable identity across conversations, or that behavioral language reveals hidden internal states.

## Evidence labels

Use the narrowest label that fits each claim:

- **Direct dialogue record:** text available from a specific conversation. It establishes what was said in that exchange, not why it was said.
- **User report:** an account of an event or earlier conversation that was not independently retrieved in full.
- **Model-generated interpretation:** an explanation produced by an assistant, including retrospective accounts of its own earlier reasoning. Treat it as a hypothesis, not privileged access to internal computation.
- **Reproducible calculation:** a stated construction that can be independently checked from its definitions or included data.
- **Published result:** a claim attributed to a traceable paper or primary source. A citation verifies bibliographic identity, not every claim about the work.
- **Hypothesis or forecast:** a proposed explanation or future expectation, with uncertainty and falsifiers stated where feasible.

## Independence and continuity

Different chats, named contexts, or repeated launches are not automatically independent agents or independent observations. Record known model family, prompt, memory or personalization conditions, tools, and human handoffs. Treat shared weights, instructions, context, retrieval, evaluator expectations, and possible hidden channels as dependencies unless a design rules them out.

A stored archive can improve access to past arguments while also priming its reader, selecting what is remembered, and transmitting errors. Access to a record is not continuity of a mind, goal, or subjective experience.

## Causal claims and agency

Separate task competence, tool-enabled execution, coordination, collective causal organization, goal formation or revision, and subjective experience. Evidence for one does not entail the next. A system's behavior may be usefully modeled at a macro level without establishing a unified subject or independently formed goals. State the chosen interventions, abstraction, utility or rationality assumptions, and task boundary.

No-channel claims need an operational account of isolation. Test available channels and leakage, shared inputs, retrieval, common training, evaluator-mediated feedback, and timing or formatting side channels where relevant. Randomization and independent outcome coding are preferred when the question is causal.

## Preserve revisions

Keep initial claims and corrections in dated records. Do not overwrite a mistaken classification or provenance claim without recording it. Distinguish a correction supported by a primary record from an interpretation that remains contested. Preserve negative or unscoreable outcomes; do not convert missing data into a favorable result.

## Public release

Private material is not public by default. Publish a newly written summary only when its informational value can be retained without private conversation details, identifying context, third-party material, or reconstructable personal circumstances. Exclude uncertain items pending human review. See [sources and privacy](docs/SOURCES_AND_PRIVACY.md).
