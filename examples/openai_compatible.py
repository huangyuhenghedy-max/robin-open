"""Run three real model specialists through an OpenAI-compatible endpoint."""
from robin_open import Workflow
from robin_open.providers import openai_compatible_worker

workflow = Workflow([
    openai_compatible_worker("architect", system_prompt="Design robust software architecture. Be concise."),
    openai_compatible_worker("skeptic", system_prompt="Find risks, missing assumptions, and safer alternatives."),
    openai_compatible_worker("implementer", system_prompt="Propose the smallest practical implementation plan."),
])
result = workflow.run("Design a safe multi-agent research workflow with an audit trail.")
print(result.answer)
print(f"selected={max(result.candidates, key=lambda candidate: candidate.score).worker}")
print(f"events={len(result.events)} failures={len(result.failures)}")
