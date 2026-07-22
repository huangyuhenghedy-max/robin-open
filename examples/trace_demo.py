"""A copy-pasteable terminal demo of selection, failures, and the event trace."""
from __future__ import annotations

from robin_open import Candidate, Workflow
from robin_open.runtime import keyword_worker


def unavailable_worker(_: str) -> Candidate:
    raise ConnectionError("demo tool endpoint is unavailable")


workflow = Workflow([
    keyword_worker("architect", keywords=["agent", "memory", "trace"], answer="Split the request among independent specialists and preserve their evidence."),
    keyword_worker("safety", keywords=["safe", "permission", "trace"], answer="Require explicit permissions and record every tool decision in an append-only trace."),
    ("tool-worker", unavailable_worker),
])
result = workflow.run("Design a safe agent workflow with memory and an event trace")

print("Robin Open trace demo\n")
for candidate in sorted(result.candidates, key=lambda item: item.score, reverse=True):
    print(f"candidate  worker={candidate.worker:<11} score={candidate.score:.1f}  {candidate.value}")
for failure in result.failures:
    print(f"isolated   {failure}")
print(f"\nselected  {result.answer}")
print("events    " + " -> ".join(event.name for event in result.events))
