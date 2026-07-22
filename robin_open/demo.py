"""A polished, deterministic terminal demo for Robin Open."""

from __future__ import annotations

import argparse
import sys
import time
from collections.abc import Sequence

from .runtime import Candidate, Event, Worker, Workflow, WorkflowResult


DEFAULT_TASK = "Design a local-first agent workflow with memory, safety, and observability"


class _Style:
    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    def apply(self, code: str, text: str) -> str:
        if not self.enabled:
            return text
        return f"\033[{code}m{text}\033[0m"


def demo_workers() -> Sequence[tuple[str, Worker]]:
    """Return workers whose behavior makes each runtime feature visible."""

    def architect(_: str) -> Candidate:
        time.sleep(0.12)
        return Candidate(
            value="Split the task into specialists, preserve evidence, and select the strongest result.",
            score=91.0,
            worker="architect",
            rationale="clear decomposition + inspectable handoff",
        )

    def safety(_: str) -> Candidate:
        time.sleep(0.07)
        return Candidate(
            value="Gate tools explicitly, isolate failures, and keep an append-only audit trail.",
            score=88.0,
            worker="safety",
            rationale="permission boundary + failure containment",
        )

    def pragmatist(_: str) -> Candidate:
        time.sleep(0.16)
        return Candidate(
            value="Start with deterministic workers, measure outcomes, then add model adapters.",
            score=84.0,
            worker="pragmatist",
            rationale="small slice + measurable iteration",
        )

    def isolated_failure(_: str) -> Candidate:
        time.sleep(0.04)
        raise TimeoutError("simulated upstream timeout")

    return (
        ("architect", architect),
        ("safety", safety),
        ("pragmatist", pragmatist),
        ("unavailable", isolated_failure),
    )


def run_demo(task: str = DEFAULT_TASK) -> WorkflowResult:
    """Run the showcase workflow without requiring an API key."""

    return Workflow(demo_workers()).run(task)


def _event_line(event: Event) -> str:
    data = event.data
    if event.name == "workflow.started":
        return f"workflow started | {data['workers']} workers launched in parallel"
    if event.name == "worker.completed":
        return f"{data['worker']} completed | score {float(data['score']):.0f}"
    if event.name == "worker.failed":
        return f"{data['worker']} failed | isolated ({data['error']})"
    if event.name == "workflow.selected":
        return f"selected {data['worker']} | score {float(data['score']):.0f}"
    if event.name == "workflow.finished":
        return f"workflow finished | {data['elapsed_ms']}ms | {data['failures']} failure isolated"
    return event.name


def render_demo(result: WorkflowResult, *, color: bool = True) -> str:
    """Render a compact terminal-first view suitable for a README or recording."""

    style = _Style(color)
    selected_worker = max(result.candidates, key=lambda item: item.score).worker
    lines = [
        style.apply("1;36", "ROBIN OPEN  /  transparent multi-agent runtime"),
        style.apply("2", "------------------------------------------------------------"),
        f"task     {result.task}",
        style.apply("1", "parallel workers"),
        "  architect   safety   pragmatist   unavailable",
        "",
        style.apply("1", "candidate board"),
    ]
    for candidate in sorted(result.candidates, key=lambda item: item.score, reverse=True):
        marker = "*" if candidate.worker == selected_worker else "."
        lines.append(
            f"  {marker} {candidate.worker:<11} {candidate.score:>5.0f}/100  {candidate.rationale}"
        )
    if result.failures:
        lines.append(style.apply("33", f"  ! {len(result.failures)} worker failure kept outside the result"))
    lines.extend(["", style.apply("1", "event trace")])
    for index, event in enumerate(result.events, start=1):
        if event.name == "worker.failed":
            line = style.apply("33", _event_line(event))
        elif event.name == "workflow.selected":
            line = style.apply("32", _event_line(event))
        else:
            line = _event_line(event)
        lines.append(f"  {index:02d}  {line}")
    lines.extend(
        [
            "",
            style.apply("1;32", f"answer  {result.answer}"),
            f"run_id   {result.run_id[:12]}...   elapsed {result.elapsed_ms}ms",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show Robin Open's transparent workflow in the terminal")
    parser.add_argument("task", nargs="?", default=DEFAULT_TASK)
    parser.add_argument("--no-color", action="store_true", help="disable ANSI colors for logs and CI")
    args = parser.parse_args(argv)
    result = run_demo(args.task)
    print(render_demo(result, color=not args.no_color and sys.stdout.isatty()))


if __name__ == "__main__":
    main()
