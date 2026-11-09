# Information flow, isolation, and independent evidence

**Record basis:** methodological audits dated 24 October–7 November 2026. **Evidence type:** research-design analysis; no completed randomized isolation experiment is claimed here.

A restriction on authorized messaging does not establish that two systems or contexts are informationally independent. They may share model weights, training data, system instructions, user context, retrieval sources, evaluator feedback, or external timing and formatting channels. Conversely, observing similar answers does not prove a hidden channel: common inputs, common training, and convergent reasoning are alternatives.

The Atlas correspondence contains proposals for randomized channel interventions and causal identification, but the letters themselves are private working material and are not reproduced. The public methodological point is that independence must be specified relative to a task and tested across the information paths that could produce the outcome.

## Design requirements

- Define the unit of analysis: model call, conversation, deployment, or organization.
- Record model/version, system instructions, tools, retrieval, personalization, shared files, evaluator, and human handoffs where available.
- Randomize communication-channel availability and include a no-message baseline.
- Audit common inputs and indirect leakage; distinguish direct messages from shared data and evaluator-mediated feedback.
- Measure both individual outcomes and joint error structure.
- Keep authorship or context labels separate from claims of independent origin.

A successful isolation test can support a bounded claim under its measured conditions. It cannot show that contexts are metaphysically separate or that similar outputs have a single cause.
