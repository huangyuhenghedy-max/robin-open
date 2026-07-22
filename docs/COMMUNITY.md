# Community Workflow

Robin Open grows through reusable evidence: a clear problem, a runnable artifact, and an inspectable result. Use the right entry point so maintainers can respond with useful context and contributors can find work that is ready to build.

## Choose an Entry Point

| Goal | Use | Expected result |
| --- | --- | --- |
| Report a reproducible defect | Bug report | A minimal reproduction, environment details, and expected behavior |
| Request a contained improvement | Feature request | A user problem, proposed boundary, and alternatives |
| Find or prepare a small starter task | `good first issue` | Clear starting files, acceptance criteria, and maintained scope |
| Share an integration or outcome | Show and tell discussion | A public artifact plus results, failure modes, and tradeoffs |
| Decide a cross-cutting direction | RFC discussion | A reviewed decision before implementation issues are created |

Questions, early ideas, and integration comparisons belong in Discussions. Public issues are reserved for reproducible defects and actionable work.

## Good First Issue Standard

A `good first issue` is a maintained contract, not a vague invitation. Before applying the label, a maintainer verifies that the issue has:

1. A user-facing outcome expressed in plain language.
2. A concrete starting point in public code or docs.
3. Acceptance criteria that another reviewer can verify.
4. A stated scope boundary and no unresolved architecture decision.
5. No dependency on credentials, private data, or competition material.

Label the issue `help wanted` as well. Remove `good first issue` when it becomes blocked, grows beyond a focused change, or needs a prior RFC. Welcome new contributors with a short ownership note, and close inactive claims so the task remains discoverable.

## Showcase Standard

A useful showcase lets another developer inspect the design rather than infer it from screenshots. Include the user problem, worker roles, selection policy, reproduction path, and observed tradeoffs. Link a public repository, command, trace excerpt, benchmark, or documented demo. State dependencies and license for linked work.

Do not post API keys, private traces, customer data, internal runtime state, or competition deliverables. A showcase can inspire an issue or RFC, but it does not imply endorsement or inclusion in the core project.

## RFC Lifecycle

1. Start an RFC discussion for decisions that change public APIs, event records, adapters, permissions, storage, or roadmap priorities.
2. Explain the problem, proposal, alternatives, validation, and rollout plan.
3. Maintain discussion until a maintainer records one outcome: accepted, revised, deferred, or declined.
4. Create focused implementation issues only after the decision is accepted.
5. Link implementation pull requests and release notes back to the RFC.

RFCs are design records. They must use public, reproducible context and must not include private data or competition material.

## Contributor Path

1. Read the quickstart and [contribution guide](../CONTRIBUTING.md).
2. Join a `good first issue`, or open a discussion to confirm direction.
3. Keep changes small, include tests or a reproducible example, and preserve trace visibility.
4. Open a pull request with verification results and scope checks.
5. After a merged first contribution, maintainers should invite the contributor to review docs, examples, or another scoped task.

Maintainers should acknowledge contributions in release notes or project updates when they materially improve the public runtime, documentation, or examples.
