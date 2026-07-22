from robin_open import Workflow
from robin_open.runtime import keyword_worker

workflow = Workflow([
    keyword_worker("planner", keywords=["plan", "workflow"], answer="Break the request into observable steps."),
    keyword_worker("reviewer", keywords=["safe", "permission"], answer="Review permissions before execution."),
])

result = workflow.run("Plan a safe workflow")
print(result.answer)
print(f"run={result.run_id} events={len(result.events)}")
