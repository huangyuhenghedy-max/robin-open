from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable, Iterable, Sequence
import concurrent.futures
import time
import uuid


@dataclass(frozen=True)
class Candidate:
    """One independently produced answer in a Best-of-N workflow."""

    value: str
    score: float
    worker: str
    rationale: str = ""


@dataclass(frozen=True)
class Event:
    """Append-only runtime event suitable for a UI, log, or audit sink."""

    name: str
    run_id: str
    timestamp: str
    data: dict[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class WorkflowResult:
    run_id: str
    task: str
    answer: str
    candidates: tuple[Candidate, ...]
    events: tuple[Event, ...]
    failures: tuple[str, ...]
    elapsed_ms: int


Worker = Callable[[str], Candidate]


class Workflow:
    """Small, dependency-free runtime for transparent parallel agent workflows."""

    def __init__(self, workers: Sequence[tuple[str, Worker]], *, max_workers: int | None = None) -> None:
        if not workers:
            raise ValueError("at least one worker is required")
        self._workers = tuple(workers)
        self._max_workers = max_workers or len(self._workers)

    def run(self, task: str, *, timeout: float = 30.0) -> WorkflowResult:
        if not task.strip():
            raise ValueError("task must not be empty")
        run_id = uuid.uuid4().hex
        started = time.perf_counter()
        events: list[Event] = []
        failures: list[str] = []

        def emit(name: str, **data: object) -> None:
            events.append(
                Event(
                    name=name,
                    run_id=run_id,
                    timestamp=datetime.now(timezone.utc).isoformat(),
                    data=data,
                )
            )

        emit("workflow.started", task=task, workers=len(self._workers))
        candidates: list[Candidate] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._max_workers) as pool:
            futures = {pool.submit(worker, task): name for name, worker in self._workers}
            for future in concurrent.futures.as_completed(futures, timeout=timeout):
                worker_name = futures[future]
                try:
                    candidate = future.result()
                    if candidate.worker != worker_name:
                        candidate = Candidate(candidate.value, candidate.score, worker_name, candidate.rationale)
                    candidates.append(candidate)
                    emit("worker.completed", worker=worker_name, score=candidate.score)
                except Exception as exc:
                    message = f"{worker_name}: {type(exc).__name__}: {exc}"
                    failures.append(message)
                    emit("worker.failed", worker=worker_name, error=message)

        if not candidates:
            emit("workflow.failed", failures=len(failures))
            raise RuntimeError("all workers failed: " + "; ".join(failures))
        chosen = max(candidates, key=lambda candidate: candidate.score)
        emit("workflow.selected", worker=chosen.worker, score=chosen.score)
        elapsed_ms = round((time.perf_counter() - started) * 1000)
        emit("workflow.finished", elapsed_ms=elapsed_ms, failures=len(failures))
        return WorkflowResult(run_id, task, chosen.value, tuple(candidates), tuple(events), tuple(failures), elapsed_ms)


def keyword_worker(name: str, *, keywords: Iterable[str], answer: str) -> tuple[str, Worker]:
    """Build a deterministic demo worker for examples and smoke tests."""
    terms = tuple(word.lower() for word in keywords)

    def worker(task: str) -> Candidate:
        hits = sum(term in task.lower() for term in terms)
        return Candidate(value=answer, score=float(hits), worker=name, rationale=f"matched {hits} keywords")

    return name, worker
