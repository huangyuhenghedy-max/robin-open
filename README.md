# Robin Open

[![CI](https://github.com/huangyuhenghedy-max/robin-open/actions/workflows/ci.yml/badge.svg)](https://github.com/huangyuhenghedy-max/robin-open/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/huangyuhenghedy-max/robin-open)](https://github.com/huangyuhenghedy-max/robin-open/releases)
[![License](https://img.shields.io/github/license/huangyuhenghedy-max/robin-open)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**A transparent, local-first runtime for Best-of-N multi-agent workflows.**

Run specialists in parallel, preserve every candidate and failure, then select a result with an inspectable event trace. Robin Open is for builders who need agent workflows they can debug, replay, and extend instead of opaque autonomous loops.

> This independent open-source core contains no competition deliverables, private data, credentials, or internal runtime state.

## See It Work In 30 Seconds

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e .
python examples/trace_demo.py
```

```text
ROBIN OPEN  /  transparent multi-agent runtime
------------------------------------------------------------
task     Design a local-first agent workflow with memory, safety, and observability

candidate board
  * architect      91/100  clear decomposition + inspectable handoff
  . safety         88/100  permission boundary + failure containment
  . pragmatist     84/100  small slice + measurable iteration
  ! 1 worker failure kept outside the result

event trace
  01  workflow started | 4 workers launched in parallel
  02  unavailable failed | isolated (simulated upstream timeout)
  03  safety completed | score 88
  04  architect completed | score 91
  05  pragmatist completed | score 84
  06  selected architect | score 91

answer  Split the task into specialists, preserve evidence, and select the strongest result.
```

The output is the product: parallel candidates, an isolated failure, a deterministic selection, and a trace suitable for a UI or audit log.

## What You Get Today

- **Parallel specialists**: independent workers run concurrently.
- **Best-of-N selection**: candidates carry explicit scores and rationales.
- **Failure isolation**: a failing or slow worker does not discard useful results.
- **Append-only trace**: starts, completions, failures, selection, and finish are inspectable.
- **OpenAI-compatible adapter**: works with compatible hosted or local endpoints through runtime environment variables.
- **Zero-key demo**: clone and run without an API key.

## Real Model Example

Robin Open makes no model vendor mandatory. Set credentials only in your shell, then run three model specialists in parallel:

```bash
# Any OpenAI-compatible endpoint, including a local gateway.
export ROBIN_OPEN_API_KEY="..."
export ROBIN_OPEN_BASE_URL="https://api.openai.com/v1"
export ROBIN_OPEN_MODEL="gpt-4o-mini"
python -m examples.openai_compatible
```

On Windows PowerShell, use `$env:ROBIN_OPEN_API_KEY = "..."`. Credentials are never stored in the workflow trace or repository. See [examples/openai_compatible.py](examples/openai_compatible.py).

## Minimal API

```python
from robin_open import Workflow
from robin_open.runtime import keyword_worker

workflow = Workflow([
    keyword_worker("architect", keywords=["agent"], answer="Split work into independent specialists."),
    keyword_worker("reviewer", keywords=["safe"], answer="Add a permission policy before tools run."),
])

result = workflow.run("Design a safe agent workflow")
print(result.answer)
print([event.name for event in result.events])
```

## Who It Is For

Use Robin Open when you need a small, explicit runtime for experiments, internal tools, CLI assistants, or services that benefit from parallel reasoning and a visible decision trail.

It is not a full agent platform yet. It does not currently ship tool permissions, persistence, MCP, A2A, a web UI, or a model SDK. Those are planned adapters, not claims about the current release.

## Architecture

```text
Task
  鈹?  鈹溾攢鈹€鈻?specialist A 鈹€鈹€鈹?  鈹溾攢鈹€鈻?specialist B 鈹€鈹€鈹尖攢鈹€鈻?scored candidates 鈹€鈹€鈻?selected answer
  鈹斺攢鈹€鈻?specialist N 鈹€鈹€鈹?             鈹?                                      鈹斺攢鈹€鈻?append-only events
```

## Development

```bash
python -m pytest
python -m compileall -q robin_open examples
```

Supported and tested in CI: Python 3.10, 3.11, and 3.12. Read [CHANGELOG.md](CHANGELOG.md) for release changes.

## Roadmap

- [ ] MCP worker with explicit permission policy
- [ ] A2A transport adapter
- [ ] SQLite event store and replay UI
- [ ] Memory provider interface with local-first defaults
- [ ] Benchmark suite for latency, cost, and selection quality

## Join The Project

- Ask questions or share a workflow through GitHub Discussions.
- Pick a starter task labeled `good first issue`.
- Propose larger changes through an RFC.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

MIT 鈥?see [LICENSE](LICENSE).

