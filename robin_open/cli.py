from __future__ import annotations

import argparse
import json

from .runtime import Workflow, keyword_worker


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a transparent Robin Open workflow")
    parser.add_argument("task", nargs="?", default="Design a safe multi-agent workflow with memory and observability")
    args = parser.parse_args()
    workflow = Workflow([
        keyword_worker("architect", keywords=["workflow", "agent", "memory"], answer="Decompose the task, run independent specialists, then select with evidence."),
        keyword_worker("safety", keywords=["safe", "sandbox", "observability"], answer="Add explicit permissions, failure isolation, and an append-only event trail."),
        keyword_worker("pragmatist", keywords=["design", "run", "select"], answer="Start with a small deterministic slice, measure it, and expand only after verification."),
    ])
    result = workflow.run(args.task)
    print(json.dumps({"run_id": result.run_id, "answer": result.answer, "candidates": [candidate.__dict__ for candidate in result.candidates], "failures": list(result.failures), "events": [event.__dict__ for event in result.events], "elapsed_ms": result.elapsed_ms}, indent=2))
