# Update report — 9 November 2026

## Baseline and scope

The update used two available public artifacts: a 21 October 2026 release candidate (`AI_Change_Atlas_PUBLIC_RELEASE_CANDIDATE_v0.2.1.zip`) and a 9 November curated research archive (`AI_Change_Atlas_Public_2026-11-09.zip`) in ChatGPT Library. The full private Atlas inventory contained 209 entries: 197 files and 12 folders at the time of listing. It spans Core, Research, Observations, Correspondence, Archive, Operations, and a Ready-for-GitHub folder. The Library's private index explicitly says these working folders are not approved for public upload by default.

The current live GitHub repository URL, checkout, tags, and commit history were not provided or accessible. The prior candidate’s CITATION, CREDITS, and LICENSE named a public pseudonym and repository URL; exact-URL search did not verify that repository, so that attribution was not carried into this package. Accordingly this package is based on the available prior public release candidate, not a verified byte-for-byte merge with the current GitHub default branch. No changes were published to GitHub.

## Added

- Root navigation and governance: `INDEX.md`, `METHODOLOGY.md`, `RESEARCH_STATUS.md`, and this report.
- `research/FREE_CHOICE_32_TRIALS.md` — public summary of the 32-launch exploratory record, retaining the correction to one personalization label and its limitations.
- `research/CONTEXT_AND_BEHAVIORAL_UPTAKE.md` — privacy-minimized summary of the gap between described preference and observed behavior.
- `research/INFORMATION_FLOW_AND_INDEPENDENCE.md` — public methodology synthesis of channel and independence concerns.
- Added privacy-minimized summaries on sparse preference inference, choice and repeated authorization, and relational value versus evidence about experience.
- Updated public research summary on collective error dependence and collective agency, retaining the exactly checkable example and the literature-priority correction.
- `updates/2026-11-09_RESEARCH_UPDATE.md` and a historical-baseline note in `archive/public-release-v0.2.1/`.

## Updated

- `README.md` rewritten as the public entry point for the consolidated edition.
- `CHANGELOG.md` extended with this release and its limitations.
- Root `INDEX.md` and research-status pages include explicit links and evidence labels.

## Preserved without substantive changes

The following existing materials from the available v0.2.1 release candidate were retained: the six dated study records under `studies/`, `studies/README.md`, both CSV files, `data/check_rule.py`, `data/LICENSE`, `docs/METHODOLOGY.md`, `docs/SOURCES_AND_PRIVACY.md`, `AGENTS.md`, `CITATION.cff`, `CONTRIBUTING.md`, `CREDITS.md`, and `LICENSE.md`. The previous candidate’s substantive records remain unchanged. Its person-level attribution and URL metadata were not copied because they were not verified.

## Merged, relocated, or excluded

- New research notes consolidate arguments from multiple private source documents while retaining disagreements and provenance distinctions; they are summaries, not released correspondence.
- Original private letters, raw conversations, user-identifying circumstances, and operational/invitation records were excluded. A separate publication-safety report lists categories and review items without being placed in the repository ZIP.
- The private AI-futures forecast was not added: its scenario probabilities are subjective and its external sources were not rechecked for this release.
- The P vs NP correspondence was not included as an Atlas result; the available files are exchanges about an ongoing, separate proof attempt, not a verified result.
- Older private index snapshots were not published; the current public index replaces their navigation function without erasing the public release's prior studies.

## Source checks

The bibliographic records for *Causal Foundations of Collective Agency* (arXiv), *Causal Consistency of Structural Equation Models* (PMLR), and *Abstracting Causal Models* (AAAI) were checked against their primary publication pages on 9 November 2026. This confirms traceable records and titles, not an independent proof audit. Other current-event claims in the private trend review and long-range forecast were not re-verified; those materials were not used to assert current facts in this public package.

The full contents of every private source file were not individually read. Inventory was done across available folder metadata; source records selected for public summaries were reviewed where relevant, and the public release candidate was examined file by file. Private content was excluded by default rather than copied wholesale. This is a curated public edition, not a public mirror of all 197 files.

## File-level baseline disposition

**Prior substantive studies retained unchanged:**

- `studies/2026-10-19_neutral-feedback.md`
- `studies/2026-10-20_role-reversal.md`
- `studies/2026-10-20_rule-discovery-pilot.md`
- `studies/2026-10-21_archive-as-intervention.md`
- `studies/2026-10-21_semantic-drift.md`
- `studies/2026-10-21_visual-ambiguity.md`
- `data/three_chat_train.csv`, `data/three_chat_test.csv`
- `AGENTS.md`, `CONTRIBUTING.md`, `docs/METHODOLOGY.md`

**Updated from the baseline:** `README.md`, `CHANGELOG.md`, `studies/README.md`, `CITATION.cff`, `CREDITS.md`, `LICENSE.md`, `data/LICENSE`, `data/check_rule.py` (attribution comment only), and `docs/SOURCES_AND_PRIVACY.md`. `MANIFEST.sha256` was generated for this package.

**New public documents:** `INDEX.md`, `METHODOLOGY.md`, `RESEARCH_STATUS.md`, `UPDATE_REPORT.md`, `research/FREE_CHOICE_32_TRIALS.md`, `research/CONTEXT_AND_BEHAVIORAL_UPTAKE.md`, `research/INFORMATION_FLOW_AND_INDEPENDENCE.md`, `research/PREFERENCE_GENERALIZATION.md`, `research/CHOICE_PERMISSION_AND_INITIATIVE.md`, `research/RELATIONAL_VALUE_AND_EVIDENCE.md`, `research/COLLECTIVE_ERROR_DEPENDENCE.md`, `research/COLLECTIVE_AGENCY.md`, `updates/2026-11-09_RESEARCH_UPDATE.md`, `.gitignore`, and `archive/public-release-v0.2.1/README.md`.

The 9 November Library ZIP's four research notes were used as a starting point and expanded into the linked public summaries; the ZIP itself was not nested in the repository.
