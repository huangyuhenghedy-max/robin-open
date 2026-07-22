# Robin Open

**A transparent, local-first runtime for multi-agent workflows.**

Robin Open is the small, understandable core behind a bigger idea: let several specialists work in parallel, keep the evidence, isolate failures, and make the final selection inspectable. It runs with Python’s standard library and is designed to grow into MCP/A2A adapters, memory providers, sandboxes, and desktop companions without hiding the control flow.

> This repository is an independent open-source core. It does not contain competition deliverables, private data, credentials, or internal runtime state.

## Why this exists

Most agent demos show a single prompt and a final answer. Production systems need the parts around the model call:

- **Parallel specialists** — run independent workers without serial bottlenecks.
- **Best-of-N selection** — compare candidates with explicit scores and rationales.
- **Failure isolation** — one broken worker does not erase useful results.
- **Append-only trace** — every start, completion, failure, selection, and finish is inspectable.
- **Local-first design** — bring your own model, API, or deterministic worker.

## Quickstart

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -e .
robin-open "Design a safe agent workflow with memory and observability"
pytest
```

No API key is needed for the demo. Replace `keyword_worker` with an OpenAI-compatible, local-model, HTTP, MCP, or A2A worker when you are ready.

## Architecture

```text
Task
  │
  ├──► specialist A ──┐
  ├──► specialist B ──┼──► scored candidates ──► selected answer
  └──► specialist N ──┘              │
                                      └──► append-only events
```

The runtime deliberately has few concepts: `Workflow`, `Candidate`, `Event`, and `WorkflowResult`. This makes it easy to embed in a FastAPI service, CLI, desktop companion, or test harness.

## Roadmap

- [ ] Model adapter protocol (OpenAI-compatible and local)
- [ ] MCP tool worker with explicit permission policy
- [ ] A2A transport adapter
- [ ] SQLite event store and replay UI
- [ ] Memory provider interface with local-first defaults
- [ ] Benchmark suite for latency, cost, and answer quality
- [ ] Electron desktop companion integration

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), open a focused issue, and include a reproducible example. Please do not submit private data, credentials, or competition deliverables.

## License

MIT — see [LICENSE](LICENSE).
