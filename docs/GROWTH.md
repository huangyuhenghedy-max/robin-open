# Robin Open Growth Plan

This plan targets sustained adoption, not artificial metrics. A star is meaningful only when a real developer can install, understand, and reuse the project.

## North-star signals

- Weekly star and fork growth
- Successful first-run reports from users
- Issues with reproducible examples
- First-time contributors and merged external pull requests
- References from technical writing, demos, and downstream projects

## First 30 days

1. Keep `main` releasable: every change has a test and a runnable example.
2. Publish one focused technical note each week:
   - transparent Best-of-N selection;
   - failure isolation and event traces;
   - adapter path for MCP/A2A and local models;
   - local-first agent runtime tradeoffs.
3. Turn questions into well-labeled issues and small starter tasks.
4. Ship `v0.2.0` only after the model-adapter interface has a verified example.

## Days 31-90

1. Add a replayable event store and lightweight web or terminal trace viewer.
2. Publish integration demos for an OpenAI-compatible model and one local model.
3. Run public benchmark comparisons with methodology and reproducible scripts.
4. Maintain a monthly changelog and a contributor acknowledgement section.

## Distribution checklist

Before sharing a release in any technical community:

- The quickstart works in a clean virtual environment.
- README states the user problem, constraints, and architecture in under two minutes.
- Release notes describe upgrades, compatibility, and rollback.
- The demo includes an inspectable result, not only a screenshot.
- No private data, credentials, internal state, or competition deliverables are included.

## Community principles

- Never buy stars, automate engagement, or use misleading claims.
- Respond to reproducible issues with concrete next actions.
- Favor small, reviewable contributions over opaque feature drops.
- Preserve transparent traces and clear safety boundaries as the project grows.
