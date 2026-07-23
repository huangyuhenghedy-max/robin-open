# Case Study: Transparent Best-of-N Research

## Problem

A single model call can produce a plausible answer without making it clear whether the result was considered, contradicted, or partially failed. That makes debugging and review expensive.

## Robin Open workflow

1. Send the same task to independent specialists.
2. Keep each candidate's answer, score, worker name, and rationale.
3. Isolate a failed or slow worker instead of discarding all results.
4. Select the highest-scoring completed candidate.
5. Emit an append-only event trace for a UI, audit log, or replay tool.

```text
Task
  ├─ architect ─┐
  ├─ skeptic   ─┼─ candidates ── selected answer
  └─ builder   ─┘       └─────── event trace
```

## Why it matters

The value is not the claim that parallel calls are always better. The value is that the tradeoff becomes visible: teams can compare latency, cost, candidate quality, and failure rate instead of trusting an opaque loop.

## Run it

```bash
pip install -e .
robin-open-demo --no-color
```

The zero-key demo intentionally includes a simulated failing worker. It lets contributors inspect failure isolation before connecting a model or tool provider.

## Extension point

Replace the deterministic worker with `openai_compatible_worker()` or an adapter for a local gateway. Keep provider credentials in environment variables, not in code or traces.

## What this is not

Robin Open is not a complete autonomous-agent platform. It does not claim to provide a sandbox, permissions, persistence, MCP, or A2A transport in this release. Those are explicit extension points on the roadmap.
